"""Benchmark evaluation using RuleFacts (semantic traversal only)."""

from __future__ import annotations

from collections import defaultdict, deque
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple
import json
import sys
import argparse
import difflib
import re

sys.path.insert(0, str(Path(__file__).parent.parent))

from enrichment.chunks import EnrichedChunk
from enrichment.clause_units import extract_clause_units
from enrichment.clause_units import ClauseUnit
from enrichment.graph_builder import build_fact_graph
from enrichment.mentions import extract_mentions
from enrichment.rule_facts import extract_rule_facts
from enrichment.vocabulary_loader import load_mention_type_mappings, load_vocabulary_from_graph_data


RELATION_WHITELIST = {
    "applies_to_role",
    "requires_level",
    "same_subject",
    "has_failure_mode",
    "contrasts_with",
    "overridden_by",
    "changes_outcome",
    "triggers",
    "unless",
    "belongs_to",
}

STRUCTURAL_RELATIONS = {
    "next",
    "contains",
    "has_fact",
    "in_same_chunk",
    "mentions_same_entity",
    "mentions_section",
    "structural_coreference",
    "describes",
    "mentioned_in",
    "mentioned_in_relation",
}

MECHANIC_FRAME_TYPES = {"MechanicFrame", "Spell", "Feat", "Rule", "Action", "Ability"}


def _normalize_name_key(value: str) -> str:
    """Normalize mechanic/entity names for deterministic matching."""
    text = str(value or "").lower()
    if not text:
        return ""
    # Remove bracketed/parenthetical metadata like [reaction], (feat)
    text = re.sub(r"\[[^\]]+\]", " ", text)
    text = re.sub(r"\([^)]+\)", " ", text)
    # Strip punctuation to whitespace, collapse spaces
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split()).strip()


def _normalize_vocab_key(value: str) -> str:
    return " ".join(str(value or "").lower().split()).strip()


def _closest_names(needle: str, candidates: List[str], top_k: int = 5) -> List[str]:
    normalized = _normalize_name_key(needle)
    if not normalized:
        return []
    scored = []
    for candidate in candidates:
        candidate_norm = _normalize_name_key(candidate)
        if not candidate_norm:
            continue
        score = difflib.SequenceMatcher(a=normalized, b=candidate_norm).ratio()
        scored.append((score, candidate))
    scored.sort(key=lambda item: (-item[0], item[1]))
    return [name for _, name in scored[:top_k]]


def _load_chunks(base_path: Path) -> List[EnrichedChunk]:
    with open(base_path) as f:
        data = json.load(f)

    valid_fields = {f.name for f in EnrichedChunk.__dataclass_fields__.values()}
    chunks = []
    for chunk_dict in data.get("chunks", []):
        filtered = {k: v for k, v in chunk_dict.items() if k in valid_fields}
        chunks.append(EnrichedChunk(**filtered))
    return chunks


def _build_adjacency(
    edges: Iterable[Dict[str, object]],
    relation_whitelist: Set[str],
) -> Dict[str, List[Tuple[str, str]]]:
    adjacency: Dict[str, List[Tuple[str, str]]] = defaultdict(list)
    for edge in edges:
        relation = edge.get("relation")
        if relation not in relation_whitelist:
            continue
        source = edge.get("source")
        target = edge.get("target")
        if not source or not target:
            continue
        adjacency[source].append((target, str(relation)))
        adjacency[target].append((source, str(relation)))
    return adjacency


def _build_query_clause(query_id: str, text: str) -> ClauseUnit:
    return ClauseUnit(
        clause_id=f"{query_id}::clause_0",
        text=text,
        parent_chunk_id=query_id,
        order_in_chunk=0,
        char_offsets=(0, len(text)),
        page=-1,
    )


def _seed_facts(
    fact_nodes: Dict[str, Dict[str, object]],
    query_mentions: List[str],
    entity_name_index: Dict[str, Set[str]],
    entity_to_facts: Dict[str, Set[str]],
) -> Set[str]:
    seeds: Set[str] = set()
    role_terms = [m for m in query_mentions if m.startswith("role:")]
    level_terms = [m for m in query_mentions if m.startswith("level:")]
    mechanic_terms = {m for m in query_mentions if m.startswith("mechanic:")}
    mechanic_names = {_normalize_name_key(m.split(":", 1)[-1]) for m in mechanic_terms}

    for fact_id, payload in fact_nodes.items():
        scope = (payload.get("scope") or "").lower()
        fact_type = payload.get("fact_type")
        obj = payload.get("object")
        subject = (payload.get("subject") or "").lower()
        obj_text = (payload.get("object") or "").lower()
        condition = (payload.get("condition") or "").lower()

        if role_terms and any(term in scope for term in role_terms):
            seeds.add(fact_id)

        if fact_type == "level_gate" and obj and level_terms:
            if any(level.split(":", 1)[-1] in str(obj) for level in level_terms):
                seeds.add(fact_id)

        if mechanic_terms:
            if subject in mechanic_terms:
                seeds.add(fact_id)
            elif mechanic_names and (
                any(name in obj_text for name in mechanic_names)
                or any(name in condition for name in mechanic_names)
            ):
                seeds.add(fact_id)

    for name in mechanic_names:
        entity_ids = entity_name_index.get(name, set())
        if entity_ids:
            entity_facts = set()
            for entity_id in entity_ids:
                entity_facts.update(entity_to_facts.get(entity_id, set()))
            seeds.update(entity_facts)
            if entity_facts:
                print(f"  🎯 Entity seed: '{name}' → {len(entity_facts)} facts")

    return seeds


def _seed_mechanic_frames(
    query_mentions: List[str],
    entity_name_index: Dict[str, Set[str]],
    entity_nodes: Dict[str, Dict[str, object]],
    entity_to_facts: Dict[str, Set[str]],
    describes_by_entity: Dict[str, Set[str]],
    chunk_to_fact_count: Dict[str, int],
) -> Set[str]:
    seeds: Set[str] = set()
    mechanic_terms = {m for m in query_mentions if m.startswith("mechanic:")}
    mechanic_names = {_normalize_name_key(m.split(":", 1)[-1]) for m in mechanic_terms}
    for name in mechanic_names:
        for entity_id in entity_name_index.get(name, set()):
            entity_type = entity_nodes.get(entity_id, {}).get("type")
            if entity_type in MECHANIC_FRAME_TYPES:
                seeds.add(entity_id)
                fact_count = len(entity_to_facts.get(entity_id, set()))
                described_chunks = describes_by_entity.get(entity_id, set())
                described_facts = sum(
                    chunk_to_fact_count.get(chunk_id, 0) for chunk_id in described_chunks
                )
                print(
                    f"  🎯 Mechanic-frame seed: '{name}' → {entity_id} "
                    f"(facts: {fact_count}, described_chunks: {len(described_chunks)}, "
                    f"facts_in_described_chunks: {described_facts})"
                )
    return seeds


def _traverse(
    seeds: Set[str],
    adjacency: Dict[str, List[Tuple[str, str]]],
    max_hops: int = 3,
) -> Tuple[Set[str], List[Tuple[str, str, str]]]:
    if not seeds:
        return set(), []
    visited = set(seeds)
    queue = deque([(seed, 0) for seed in seeds])
    traversed_edges: List[Tuple[str, str, str]] = []
    while queue:
        node, depth = queue.popleft()
        if depth >= max_hops:
            continue
        for neighbor, relation in adjacency.get(node, []):
            if neighbor in visited:
                continue
            visited.add(neighbor)
            traversed_edges.append((node, neighbor, relation))
            queue.append((neighbor, depth + 1))
    return visited, traversed_edges


def _load_queries(batch_path: Path) -> List[Dict[str, object]]:
    with open(batch_path) as f:
        batch = json.load(f)
    return batch.get("queries", [])


def _compute_ownership_coverage(
    facts: Dict[str, Dict[str, object]],
    edges: List[Dict[str, object]],
) -> Tuple[float, int, int]:
    belongs_to_counts: Dict[str, int] = defaultdict(int)
    for edge in edges:
        if edge.get("relation") != "belongs_to":
            continue
        fact_id = edge.get("source")
        if fact_id in facts:
            belongs_to_counts[str(fact_id)] += 1
    exact_one = sum(1 for fact_id in facts if belongs_to_counts.get(fact_id, 0) == 1)
    total = len(facts)
    coverage = (exact_one / total) if total else 0.0
    return coverage, exact_one, total


def _collect_explanation_nodes(
    reachable: Set[str],
    fact_nodes: Dict[str, Dict[str, object]],
    edges: List[Dict[str, object]],
) -> Set[str]:
    nodes = set(reachable)
    reachable_facts = {node for node in reachable if node in fact_nodes}
    for fact_id in reachable_facts:
        chunk_id = fact_nodes[fact_id].get("source_chunk_id")
        if chunk_id:
            nodes.add(str(chunk_id))
    for edge in edges:
        relation = edge.get("relation")
        if relation != "belongs_to":
            continue
        source = edge.get("source")
        target = edge.get("target")
        if source in reachable_facts and target:
            nodes.add(str(target))
    return nodes


def _compute_traversal_purity(
    explanation_nodes: Set[str],
    edges: List[Dict[str, object]],
) -> Tuple[float, int, int]:
    total = 0
    semantic = 0
    for edge in edges:
        source = edge.get("source")
        target = edge.get("target")
        if source not in explanation_nodes or target not in explanation_nodes:
            continue
        total += 1
        relation = edge.get("relation")
        if relation in RELATION_WHITELIST:
            semantic += 1
        elif relation in STRUCTURAL_RELATIONS:
            continue
    ratio = (semantic / total) if total else 0.0
    return ratio, semantic, total


def _rank_chunks_from_reachable(
    reachable_nodes: Iterable[str],
    fact_nodes: Dict[str, Dict[str, object]],
) -> List[str]:
    ranked_chunks: List[str] = []
    seen_chunks: Set[str] = set()
    for node_id in reachable_nodes:
        if node_id in fact_nodes:
            chunk_id = fact_nodes[node_id].get("source_chunk_id")
            if chunk_id and chunk_id not in seen_chunks:
                seen_chunks.add(chunk_id)
                ranked_chunks.append(chunk_id)
    return ranked_chunks


def run() -> None:
    parser = argparse.ArgumentParser(description="Mechanic ownership closure test.")
    parser.add_argument(
        "--mode",
        choices=["facts", "mechanic_frames"],
        default="facts",
        help="Seed traversal from facts or mechanic frames.",
    )
    parser.add_argument(
        "--enable-belongs-to",
        action="store_true",
        help="Include belongs_to edges in traversal adjacency.",
    )
    parser.add_argument(
        "--max-hops",
        type=int,
        default=3,
        help="Max traversal hops.",
    )
    parser.add_argument(
        "--query-limit",
        type=int,
        default=0,
        help="Limit number of queries (0 = all).",
    )
    parser.add_argument(
        "--debug-mechanic",
        type=str,
        default="",
        help="Dump clause/fact diagnostics for this mechanic name.",
    )
    parser.add_argument(
        "--audit-mechanic-names",
        action="store_true",
        help="Print mechanic mention resolution diagnostics per query.",
    )
    parser.add_argument(
        "--base-path",
        type=str,
        default="Rules/StarFinder2e/PlayerCore/outputs/runs/2026-01-25_19-16-02/enriched/merged.enriched.json",
        help="Path to enriched merged JSON.",
    )
    parser.add_argument(
        "--batch-path",
        type=str,
        default="blind_eval/batches/batch_001.json",
        help="Path to benchmark batch JSON.",
    )
    args = parser.parse_args()

    base_path = Path(args.base_path)
    batch_path = Path(args.batch_path)
    print(f"📂 Loading data from: {base_path}")
    print(f"📦 Loading batch from: {batch_path}")

    chunks = _load_chunks(base_path)
    chunk_map = {chunk.id: chunk for chunk in chunks}
    mention_type_mappings = load_mention_type_mappings(enriched_path=base_path)
    graph = build_fact_graph(
        doc_id="sf2e-playercore",
        chunks=chunks,
        ruleset_id="StarFinder2e",
        mention_type_mappings=mention_type_mappings,
        include_fact_chunk_links=True,
        include_partial=False,
        allow_cross_section=True,
    )

    fact_nodes = {n["id"]: n for n in graph.nodes if n.get("type") == "RuleFact"}
    relation_whitelist = set(RELATION_WHITELIST)
    if not args.enable_belongs_to and "belongs_to" in relation_whitelist:
        relation_whitelist.remove("belongs_to")
    adjacency = _build_adjacency(graph.edges, relation_whitelist)
    graph_payload = graph.to_dict()
    graph_payload["chunks"] = [chunk.to_dict() for chunk in chunks]
    vocabularies = load_vocabulary_from_graph_data(graph_payload, mention_type_mappings)
    mechanic_vocab = vocabularies.get("mechanic", set())
    entity_nodes = {
        n["id"]: n
        for n in graph.nodes
        if n.get("type") not in {"document", "section", "chunk", "RuleFact"}
    }
    chunk_nodes = {n["id"] for n in graph.nodes if n.get("type") == "chunk"}
    entity_name_index: Dict[str, Set[str]] = defaultdict(set)
    entity_canonical_index: Dict[str, Set[str]] = defaultdict(set)
    entity_alias_index: Dict[str, Set[str]] = defaultdict(set)
    mechanic_frame_names: List[str] = []
    for entity_id, entity in entity_nodes.items():
        entity_type = entity.get("type")
        name = str(entity.get("name") or "")
        name_key = _normalize_name_key(name)
        if name_key:
            entity_name_index[name_key].add(entity_id)
            entity_canonical_index[name_key].add(entity_id)
        for alias in entity.get("aliases", []):
            alias_key = _normalize_name_key(str(alias))
            if alias_key:
                entity_name_index[alias_key].add(entity_id)
                entity_alias_index[alias_key].add(entity_id)
        if entity_type in MECHANIC_FRAME_TYPES and name:
            mechanic_frame_names.append(name)

    fact_to_entity: Dict[str, str] = {}
    entity_to_facts: Dict[str, Set[str]] = defaultdict(set)
    describes_by_entity: Dict[str, Set[str]] = defaultdict(set)
    chunk_to_fact_count: Dict[str, int] = defaultdict(int)
    for edge in graph.edges:
        if edge.get("relation") == "belongs_to":
            fact_id = edge.get("source")
            entity_id = edge.get("target")
            if fact_id and entity_id:
                fact_to_entity[fact_id] = entity_id
                entity_to_facts[entity_id].add(fact_id)
        if edge.get("relation") == "describes":
            chunk_id = edge.get("source")
            entity_id = edge.get("target")
            if chunk_id and entity_id:
                describes_by_entity[entity_id].add(chunk_id)

    for fact_id, payload in fact_nodes.items():
        chunk_id = payload.get("source_chunk_id")
        if chunk_id:
            chunk_to_fact_count[str(chunk_id)] += 1

    print(f"Entity nodes: {len(entity_nodes)}")
    print(f"Entity name index entries: {len(entity_name_index)}")
    print(f"Facts with BELONGS_TO: {len(fact_to_entity)}")
    coverage, exact_one, total_facts = _compute_ownership_coverage(fact_nodes, graph.edges)
    print(
        "Ownership coverage: "
        f"{exact_one}/{total_facts} facts with exactly 1 belongs_to ({coverage:.1%})"
    )

    queries = _load_queries(batch_path)
    total_gold = 0
    total_found = 0
    total_found_at_5 = 0
    total_found_at_10 = 0
    evaluated = 0
    purity_scores: List[float] = []
    compact_fact_counts: List[int] = []
    compact_frame_counts: List[int] = []
    compact_chunk_counts: List[int] = []

    mechanic_mentions_total = 0
    mechanic_mentions_resolved = 0

    debug_mechanic_key = _normalize_name_key(args.debug_mechanic)

    for query in queries:
        query_id = query.get("id")
        question = query.get("question", "")
        gold_chunks = query.get("gold_chunk_ids", [])
        if not query_id or not question or not gold_chunks:
            continue
        if any("TODO" in str(chunk) for chunk in gold_chunks):
            continue

        clause = _build_query_clause(str(query_id), str(question))
        mentions = extract_mentions(clause, vocabularies=vocabularies)
        query_terms = [m.normalized for m in mentions]
        mention_summary = [
            f"{m.mention_type.value}:{m.surface} -> {m.normalized}" for m in mentions
        ] if mentions else []

        if args.audit_mechanic_names:
            mechanic_mentions = [
                m for m in mentions if m.mention_type.value == "mechanic"
            ]
            for mention in mechanic_mentions:
                raw_text = mention.surface
                normalized_key = _normalize_name_key(raw_text)
                vocab_key = _normalize_vocab_key(mention.normalized.split(":", 1)[-1])
                exact_matches = [
                    entity_id
                    for entity_id in entity_canonical_index.get(normalized_key, set())
                    if entity_nodes.get(entity_id, {}).get("type") in MECHANIC_FRAME_TYPES
                ]
                alias_matches = [
                    entity_id
                    for entity_id in entity_alias_index.get(normalized_key, set())
                    if entity_nodes.get(entity_id, {}).get("type") in MECHANIC_FRAME_TYPES
                ]
                closest = _closest_names(raw_text, mechanic_frame_names, top_k=5)
                print(f"\n[Mechanic Name Audit] Query: \"{raw_text}\"")
                print(f"  Normalized mention key: \"{normalized_key}\"")
                print(f"  In mechanic vocab: {vocab_key in mechanic_vocab}")
                print(f"  Exact entity matches: {exact_matches}")
                print(f"  Alias matches: {alias_matches}")
                if closest:
                    print("  Closest canonical names (top 5):")
                    for name in closest:
                        print(f"    - \"{name}\"")

                mechanic_mentions_total += 1
                if exact_matches or alias_matches:
                    mechanic_mentions_resolved += 1
        if args.mode == "mechanic_frames":
            seeds = _seed_mechanic_frames(
                query_terms,
                entity_name_index,
                entity_nodes,
                entity_to_facts,
                describes_by_entity,
                chunk_to_fact_count,
            )
        else:
            seeds = _seed_facts(fact_nodes, query_terms, entity_name_index, entity_to_facts)

        reachable, traversed_edges = _traverse(seeds, adjacency, max_hops=args.max_hops)
        reachable_facts = {fact_id for fact_id in reachable if fact_id in fact_nodes}
        reachable_chunks = {
            fact_nodes[fact_id].get("source_chunk_id")
            for fact_id in reachable_facts
            if fact_nodes[fact_id].get("source_chunk_id")
        }

        gold_set = set(gold_chunks)
        found = gold_set & reachable_chunks
        ranked_chunks = _rank_chunks_from_reachable(
            [seed for seed, _, _ in traversed_edges] + list(reachable),
            fact_nodes,
        )
        found_at_5 = gold_set & set(ranked_chunks[:5])
        found_at_10 = gold_set & set(ranked_chunks[:10])

        explanation_nodes = _collect_explanation_nodes(reachable, fact_nodes, graph.edges)
        purity, semantic_edges, total_edges = _compute_traversal_purity(
            explanation_nodes,
            graph.edges,
        )
        purity_scores.append(purity)

        explanation_facts = {node_id for node_id in explanation_nodes if node_id in fact_nodes}
        explanation_frames = {
            node_id
            for node_id in explanation_nodes
            if entity_nodes.get(node_id, {}).get("type") in MECHANIC_FRAME_TYPES
        }
        explanation_chunks = {node_id for node_id in explanation_nodes if node_id in chunk_nodes}
        compact_fact_counts.append(len(explanation_facts))
        compact_frame_counts.append(len(explanation_frames))
        compact_chunk_counts.append(len(explanation_chunks))

        print(f"\nQuery: {query_id}")
        print(f"  Mentions: {', '.join(mention_summary) if mention_summary else '(none)'}")
        print(f"  Seeds: {len(seeds)}")
        print(f"  Reachable facts: {len(reachable_facts)}")
        print(f"  Gold found: {len(found)}/{len(gold_set)}")
        print(
            "  Traversal purity: "
            f"{semantic_edges}/{total_edges} semantic edges ({purity:.1%})"
        )
        print(
            "  Explanation compactness: "
            f"{len(explanation_facts)} facts, "
            f"{len(explanation_frames)} frames, "
            f"{len(explanation_chunks)} chunks"
        )
        if found:
            for chunk_id in sorted(found):
                print(f"   - {chunk_id}")

        if debug_mechanic_key and args.mode == "mechanic_frames":
            if any(debug_mechanic_key in term for term in query_terms):
                print("\n[Debug Mechanic] Clause/Facts dump")
                for entity_id in sorted(seeds):
                    entity_name = _normalize_name_key(entity_nodes.get(entity_id, {}).get("name", ""))
                    if entity_name != debug_mechanic_key:
                        continue
                    described_chunks = sorted(describes_by_entity.get(entity_id, set()))
                    print(f"  MechanicFrame: {entity_id}")
                    print(f"  Described chunks: {len(described_chunks)}")
                    for chunk_id in described_chunks:
                        chunk = chunk_map.get(chunk_id)
                        if not chunk:
                            continue
                        facts_in_chunk = [
                            fact_id
                            for fact_id, payload in fact_nodes.items()
                            if payload.get("source_chunk_id") == chunk_id
                        ]
                        print(f"  - Chunk: {chunk_id} (facts: {len(facts_in_chunk)})")
                        for fact_id in facts_in_chunk:
                            assigned = fact_to_entity.get(fact_id)
                            payload = fact_nodes.get(fact_id, {})
                            print(
                                f"    Fact {fact_id} -> belongs_to: {assigned} "
                                f"subject={payload.get('subject')} "
                                f"object={payload.get('object')} "
                                f"type={payload.get('fact_type')}"
                            )
                        clauses = extract_clause_units(chunk)
                        print(f"    Clauses: {len(clauses)}")
                        for clause in clauses:
                            mentions = extract_mentions(clause, vocabularies=vocabularies)
                            clause_facts = extract_rule_facts(clause, mentions, resolved_config=None)
                            mention_types = ",".join(sorted({m.mention_type.value for m in mentions}))
                            if clause_facts:
                                print(
                                    f"    Clause {clause.clause_id}: "
                                    f"facts={len(clause_facts)} mentions={mention_types} "
                                    f"text={clause.text.strip()[:160]}"
                                )
                            else:
                                print(
                                    f"    Clause {clause.clause_id}: "
                                    f"facts=0 mentions={mention_types} "
                                    f"text={clause.text.strip()[:160]}"
                                )

        evaluated += 1
        total_gold += len(gold_set)
        total_found += len(found)
        total_found_at_5 += len(found_at_5)
        total_found_at_10 += len(found_at_10)

        if args.query_limit and evaluated >= args.query_limit:
            break

    recall = (total_found / total_gold) if total_gold else 0.0
    recall_at_5 = (total_found_at_5 / total_gold) if total_gold else 0.0
    recall_at_10 = (total_found_at_10 / total_gold) if total_gold else 0.0
    avg_purity = sum(purity_scores) / len(purity_scores) if purity_scores else 0.0
    avg_facts = sum(compact_fact_counts) / len(compact_fact_counts) if compact_fact_counts else 0.0
    avg_frames = sum(compact_frame_counts) / len(compact_frame_counts) if compact_frame_counts else 0.0
    avg_chunks = sum(compact_chunk_counts) / len(compact_chunk_counts) if compact_chunk_counts else 0.0
    print("\n=== Summary ===")
    print(f"Queries evaluated: {evaluated}")
    print(f"Gold chunks found: {total_found}/{total_gold} ({recall:.2%})")
    print(f"Recall@5: {total_found_at_5}/{total_gold} ({recall_at_5:.2%})")
    print(f"Recall@10: {total_found_at_10}/{total_gold} ({recall_at_10:.2%})")
    print(f"Avg traversal purity: {avg_purity:.2%}")
    print(f"Avg explanation compactness: {avg_facts:.1f} facts, {avg_frames:.1f} frames, {avg_chunks:.1f} chunks")
    if mechanic_mentions_total:
        resolvability = mechanic_mentions_resolved / mechanic_mentions_total
        print(
            "Name resolvability: "
            f"{mechanic_mentions_resolved}/{mechanic_mentions_total} "
            f"({resolvability:.1%})"
        )


if __name__ == "__main__":
    run()
