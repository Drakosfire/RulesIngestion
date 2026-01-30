"""Benchmark evaluation using RuleFacts (semantic traversal only).

Extended per HANDOFF-Entity-Only-Traversal-Experiment-2026-01-30.md:
- Entity-only traversal mode
- Entity-only metrics (semantic purity, compactness, assertion load)
- Per-query correlation logging
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from dataclasses import dataclass, field, asdict
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
from enrichment.graph_builder import build_fact_graph, is_entity_like
from enrichment.mentions import extract_mentions
from enrichment.rule_facts import extract_rule_facts
from enrichment.vocabulary_loader import load_mention_type_mappings, load_vocabulary_from_graph_data
from traversal.index import (
    TraversalMode,
    TraversalProjection,
    traverse_entity_only,
    run_entity_only_traversal,
)


@dataclass
class QueryMetrics:
    """Per-query metrics for correlation analysis.
    
    Per Step 3.1 of the handoff, log these fields for each query:
    - total_entity_count: Entities in explanation
    - total_fact_count: Facts attached
    - entity_traversal_depth: Max hops in entity-only path
    - entity_semantic_purity: From Step 2.1
    - assertion_load: From Step 2.2 (facts per entity)
    - gold_hit: 1 if gold chunks found, 0 otherwise
    - causal_coverage: Fraction of causal gold covered
    """
    query_id: str = ""
    
    # Entity path metrics
    total_entity_count: int = 0
    total_fact_count: int = 0
    entity_traversal_depth: int = 0
    
    # Entity-only purity (Step 2.1)
    entity_semantic_purity: float = 0.0
    entity_semantic_edges: int = 0
    entity_total_edges: int = 0
    
    # Entity compactness (Step 2.2)
    entity_count: int = 0
    frame_count: int = 0
    
    # Assertion load (Step 2.2)
    facts_per_entity: float = 0.0
    chunks_per_entity: float = 0.0
    
    # Gold coverage
    gold_hit: int = 0  # 1 if any gold found, 0 otherwise
    gold_found: int = 0
    gold_total: int = 0
    
    # Causal coverage
    causal_coverage: float = 0.0
    
    # Traversal mode used
    traversal_mode: str = "full"
    
    def to_dict(self) -> Dict[str, object]:
        """Convert to dict for JSON serialization."""
        return asdict(self)


RELATION_WHITELIST = {
    "applies_to_role",
    "requires_level",
    "same_subject",
    "same_mechanic_frame",
    "requires_level_supports",
    "replaces_effect",
    "has_failure_mode",
    "contrasts_with",
    "overridden_by",
    "changes_outcome",
    "triggers",
    "unless",
    "references_mechanic",
    "requires_mechanic",
    "modifies_mechanic",
    "targets_procedure",
    "targets_step",
    "suppresses",
    "excludes_outcome",
    "modifies_parameter",
    "belongs_to",
    "affects",
    "results_in",
    "part_of",
    "branches_from",
    "step_of",
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
    "step_of",
}

MECHANIC_FRAME_TYPES = {"MechanicFrame", "Spell", "Feat", "Rule", "Action", "Ability"}

OWNERSHIP_RELATIONS = {"belongs_to", "asserts_about"}
ANCHOR_RELATIONS = {"belongs_to", "asserts_about"}

SEMANTIC_FACT_RELATIONS = {
    "applies_to_role",
    "requires_level",
    "same_subject",
    "same_mechanic_frame",
    "requires_level_supports",
    "replaces_effect",
    "has_failure_mode",
    "contrasts_with",
    "overridden_by",
    "changes_outcome",
    "triggers",
    "unless",
    "targets_procedure",
    "targets_step",
    "suppresses",
    "excludes_outcome",
    "modifies_parameter",
}

NEGATION_FACT_TYPES = {"prevents", "requires", "triggers", "unless"}

SINGLE_MECHANIC_FACT_BOUND = 5
MULTI_MECHANIC_FACT_BOUND = 8
FRAME_FANOUT_BOUND = 3

PHASE1_BEHAVIORAL_QUERIES = {
    "blind_001_01",
    "blind_001_03",
    "blind_001_04",
    "blind_001_06",
    "blind_001_07",
    "blind_001_08",
    "blind_001_09",
    "blind_001_10",
}

PHASE1_STRUCTURAL_QUERIES = {
    "blind_001_02",
    "blind_001_05",
}


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
    sorted_edges = sorted(
        edges,
        key=lambda edge: (
            str(edge.get("relation") or ""),
            str(edge.get("source") or ""),
            str(edge.get("target") or ""),
        ),
    )
    for edge in sorted_edges:
        relation = edge.get("relation")
        if relation not in relation_whitelist:
            continue
        source = edge.get("source")
        target = edge.get("target")
        if not source or not target:
            continue
        adjacency[source].append((target, str(relation)))
        adjacency[target].append((source, str(relation)))
    for node_id in adjacency:
        adjacency[node_id].sort(key=lambda item: (item[1], item[0]))
    return adjacency


def _build_causal_edges(edges: Iterable[Dict[str, object]]) -> List[Dict[str, object]]:
    causal_edges: List[Dict[str, object]] = []
    for edge in edges:
        relation = edge.get("relation")
        if relation not in SEMANTIC_FACT_RELATIONS:
            continue
        source = edge.get("source")
        target = edge.get("target")
        if not source or not target:
            continue
        causal_edges.append(edge)
    return causal_edges


def _build_causal_adjacency(
    edges: Iterable[Dict[str, object]],
) -> Dict[str, List[Tuple[str, str]]]:
    adjacency: Dict[str, List[Tuple[str, str]]] = defaultdict(list)
    sorted_edges = sorted(
        edges,
        key=lambda edge: (
            str(edge.get("relation") or ""),
            str(edge.get("source") or ""),
            str(edge.get("target") or ""),
        ),
    )
    for edge in sorted_edges:
        relation = edge.get("relation")
        if relation not in SEMANTIC_FACT_RELATIONS:
            continue
        source = edge.get("source")
        target = edge.get("target")
        if not source or not target:
            continue
        adjacency[source].append((target, str(relation)))
    for node_id in adjacency:
        adjacency[node_id].sort(key=lambda item: (item[1], item[0]))
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
    condition_terms = [
        m for m in query_mentions if m.startswith("condition:") or m.startswith("state:")
    ]
    mechanic_terms = {m for m in query_mentions if m.startswith("mechanic:")}
    mechanic_names = {_normalize_name_key(m.split(":", 1)[-1]) for m in mechanic_terms}
    condition_names = {
        _normalize_name_key(m.split(":", 1)[-1]) for m in condition_terms
    }

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

        if condition_terms:
            if subject in condition_terms:
                seeds.add(fact_id)
            elif condition_names and (
                any(name in condition for name in condition_names)
                or any(name in obj_text for name in condition_names)
                or any(name in scope for name in condition_names)
                or any(name in subject for name in condition_names)
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
    condition_terms = {
        m for m in query_mentions if m.startswith("condition:") or m.startswith("state:")
    }
    condition_names = {
        _normalize_name_key(m.split(":", 1)[-1]) for m in condition_terms
    }
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
    for name in condition_names:
        for entity_id in entity_name_index.get(name, set()):
            entity_type = entity_nodes.get(entity_id, {}).get("type")
            if entity_type != "Condition":
                continue
            seeds.add(entity_id)
            described_chunks = describes_by_entity.get(entity_id, set())
            described_facts = sum(
                chunk_to_fact_count.get(chunk_id, 0) for chunk_id in described_chunks
            )
            print(
                f"  🎯 Condition seed: '{name}' → {entity_id} "
                f"(described_chunks: {len(described_chunks)}, "
                f"facts_in_described_chunks: {described_facts})"
            )
    return seeds


def _traverse(
    seeds: Set[str],
    adjacency: Dict[str, List[Tuple[str, str]]],
    max_hops: int = 3,
) -> Tuple[Set[str], List[Tuple[str, str, str]], List[str]]:
    if not seeds:
        return set(), [], []
    ordered_seeds = sorted(seeds)
    visited = set(ordered_seeds)
    visited_order = list(ordered_seeds)
    queue = deque([(seed, 0) for seed in ordered_seeds])
    traversed_edges: List[Tuple[str, str, str]] = []
    while queue:
        node, depth = queue.popleft()
        if depth >= max_hops:
            continue
        for neighbor, relation in adjacency.get(node, []):
            if neighbor in visited:
                continue
            visited.add(neighbor)
            visited_order.append(neighbor)
            traversed_edges.append((node, neighbor, relation))
            queue.append((neighbor, depth + 1))
    return visited, traversed_edges, visited_order


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


def _collect_explanation_nodes_from_facts(
    fact_ids: Set[str],
    fact_nodes: Dict[str, Dict[str, object]],
    edges: List[Dict[str, object]],
) -> Set[str]:
    nodes = set(fact_ids)
    for fact_id in fact_ids:
        chunk_id = fact_nodes.get(fact_id, {}).get("source_chunk_id")
        if chunk_id:
            nodes.add(str(chunk_id))
    for edge in edges:
        relation = edge.get("relation")
        source = edge.get("source")
        target = edge.get("target")
        if not source or not target:
            continue
        if relation == "belongs_to" and source in fact_ids:
            nodes.add(str(target))
        if relation in {"targets_procedure", "targets_step", "replaces_effect", "suppresses", "modifies_parameter"} and source in fact_ids:
            nodes.add(str(target))
    return nodes


def _apply_phase2_applicability(
    reachable_nodes: Set[str],
    fact_nodes: Dict[str, Dict[str, object]],
    edges: List[Dict[str, object]],
) -> Tuple[Set[str], Set[str], Set[str], Set[str]]:
    reachable_facts = {node for node in reachable_nodes if node in fact_nodes}
    gate_relations = {
        "requires_condition",
        "requires_state",
        "requires_trait",
        "requires_level",
        "requires_context",
    }

    gate_targets_by_fact: Dict[str, Set[str]] = defaultdict(set)
    for edge in edges:
        relation = edge.get("relation")
        if relation not in gate_relations:
            continue
        source = edge.get("source")
        target = edge.get("target")
        if source in reachable_facts and target:
            gate_targets_by_fact[str(source)].add(str(target))

    active_facts: Set[str] = set()
    for fact_id in reachable_facts:
        gate_targets = gate_targets_by_fact.get(fact_id)
        if not gate_targets:
            active_facts.add(fact_id)
            continue
        if all(target in reachable_nodes for target in gate_targets):
            active_facts.add(fact_id)

    target_procedures: Set[str] = set()
    target_steps: Set[str] = set()
    disabled_procedures: Set[str] = set()
    disabled_steps: Set[str] = set()
    for edge in edges:
        relation = edge.get("relation")
        source = edge.get("source")
        target = edge.get("target")
        if source not in active_facts or not target:
            continue
        target_id = str(target)
        if relation in {"targets_procedure", "replaces_effect", "suppresses"}:
            if target_id.startswith("procedure:") and "#step:" not in target_id:
                target_procedures.add(target_id)
        if relation in {"targets_step", "replaces_effect", "suppresses"}:
            if "#step:" in target_id:
                target_steps.add(target_id)
        if relation in {"replaces_effect", "suppresses"}:
            if "#step:" in target_id:
                disabled_steps.add(target_id)
            elif target_id.startswith("procedure:"):
                disabled_procedures.add(target_id)

    enabled_procedures = target_procedures - disabled_procedures
    enabled_steps = target_steps - disabled_steps

    explanation_facts: Set[str] = set()
    for edge in edges:
        relation = edge.get("relation")
        source = edge.get("source")
        target = edge.get("target")
        if source not in active_facts or not target:
            continue
        target_id = str(target)
        if relation == "targets_procedure" and target_id in enabled_procedures:
            explanation_facts.add(str(source))
        elif relation == "targets_step" and target_id in enabled_steps:
            explanation_facts.add(str(source))
        elif relation in {"replaces_effect", "suppresses"}:
            explanation_facts.add(str(source))

    return explanation_facts, active_facts, enabled_procedures, enabled_steps


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


def _compute_effective_semantic_purity(
    explanation_nodes: Set[str],
    edges: List[Dict[str, object]],
) -> Tuple[float, int, int]:
    belongs_to_pairs: Set[Tuple[str, str]] = set()
    has_fact_edges: Set[Tuple[str, str]] = set()
    describes_edges: Set[Tuple[str, str]] = set()
    for edge in edges:
        relation = edge.get("relation")
        source = edge.get("source")
        target = edge.get("target")
        if not source or not target:
            continue
        if relation == "belongs_to":
            belongs_to_pairs.add((str(source), str(target)))
        elif relation == "has_fact":
            has_fact_edges.add((str(source), str(target)))
        elif relation == "describes":
            describes_edges.add((str(source), str(target)))

    collapsed_chunk_facts: Set[Tuple[str, str]] = set()
    collapsed_chunk_frames: Set[Tuple[str, str]] = set()
    for chunk_id, fact_id in has_fact_edges:
        for fact, frame in belongs_to_pairs:
            if fact != fact_id:
                continue
            if (chunk_id, frame) in describes_edges:
                collapsed_chunk_facts.add((chunk_id, fact_id))
                collapsed_chunk_frames.add((chunk_id, frame))

    total = 0
    semantic = 0
    for edge in edges:
        source = edge.get("source")
        target = edge.get("target")
        if source not in explanation_nodes or target not in explanation_nodes:
            continue
        relation = edge.get("relation")
        if relation in OWNERSHIP_RELATIONS:
            continue
        if relation in RELATION_WHITELIST:
            semantic += 1
            total += 1
        elif relation in STRUCTURAL_RELATIONS:
            if relation == "has_fact" and (str(source), str(target)) in collapsed_chunk_facts:
                continue
            if relation == "describes" and (str(source), str(target)) in collapsed_chunk_frames:
                continue
            total += 1
    ratio = (semantic / total) if total else 0.0
    return ratio, semantic, total


# =============================================================================
# Entity-Only Metrics (per HANDOFF-Entity-Only-Traversal-Experiment-2026-01-30.md)
# =============================================================================

# Semantic edges between entities (for entity-only purity)
ENTITY_SEMANTIC_RELATIONS = {
    "requires",
    "modifies",
    "replaces_effect",
    "triggers",
    "contrasts_with",
    "overridden_by",
    "changes_outcome",
    "unless",
    "suppresses",
    "excludes_outcome",
    "references_mechanic",
    "requires_mechanic",
    "modifies_mechanic",
    "affects",
    "results_in",
    "part_of",
    "branches_from",
    "structural_coreference",
    "mentions_same_entity",
}


def _compute_entity_semantic_purity(
    entity_path: Set[str],
    entity_nodes: Dict[str, Dict[str, object]],
    edges: List[Dict[str, object]],
) -> Tuple[float, int, int]:
    """Compute semantic purity over entity-only structure.
    
    Per Step 2.1 of the handoff:
    Entity Semantic Purity = 
        (# semantic edges between entities in the explanation path)
        / (total entity–entity edges traversed)
    
    Facts are EXCLUDED entirely from this ratio.
    This measures REASONING QUALITY, not verbosity.
    
    Args:
        entity_path: Set of entity IDs in the explanation
        entity_nodes: Dict of entity_id -> node dict
        edges: List of all graph edges
        
    Returns:
        Tuple of (ratio, semantic_count, total_count)
    """
    entity_path_set = set(entity_path)
    total = 0
    semantic = 0
    
    for edge in edges:
        source = edge.get("source")
        target = edge.get("target")
        relation = edge.get("relation")
        
        # Only count edges between entities in the path
        if source not in entity_path_set or target not in entity_path_set:
            continue
        
        # INVARIANT: Both endpoints must be entities, not facts
        if source not in entity_nodes or target not in entity_nodes:
            continue
        
        total += 1
        if relation in ENTITY_SEMANTIC_RELATIONS:
            semantic += 1
    
    ratio = (semantic / total) if total else 0.0
    return ratio, semantic, total


def _compute_entity_compactness(
    entity_path: Set[str],
    entity_nodes: Dict[str, Dict[str, object]],
    mechanic_frame_types: Set[str],
) -> Tuple[int, int]:
    """Compute entity compactness metrics.
    
    Per Step 2.2 of the handoff:
    Entity Compactness = Number of entity nodes in explanation; 
                         number of entity frames used
    
    A good explanation is STRUCTURALLY COMPACT (few entities, tight paths).
    
    Args:
        entity_path: Set of entity IDs in the explanation
        entity_nodes: Dict of entity_id -> node dict
        mechanic_frame_types: Set of types that are mechanic frames
        
    Returns:
        Tuple of (entity_count, frame_count)
    """
    entity_count = len(entity_path)
    frame_count = sum(
        1 for entity_id in entity_path
        if entity_nodes.get(entity_id, {}).get("type") in mechanic_frame_types
    )
    return entity_count, frame_count


def _compute_assertion_load(
    entity_path: Set[str],
    attached_facts: Set[str],
    entity_to_chunks: Dict[str, Set[str]],
) -> Tuple[float, float]:
    """Compute assertion load metrics.
    
    Per Step 2.2 of the handoff:
    Assertion Load = Number of facts attached per entity;
                     Number of chunks cited per entity
    
    A good explanation is allowed to have many facts if they all support
    the same structure. This DECOUPLES density from quality.
    
    Args:
        entity_path: Set of entity IDs in the explanation
        attached_facts: Set of fact IDs attached to the entity path
        entity_to_chunks: Dict of entity_id -> set of chunk_ids
        
    Returns:
        Tuple of (facts_per_entity, chunks_per_entity)
    """
    if not entity_path:
        return 0.0, 0.0
    
    facts_per_entity = len(attached_facts) / len(entity_path)
    
    # Count unique chunks cited across all entities
    cited_chunks: Set[str] = set()
    for entity_id in entity_path:
        cited_chunks.update(entity_to_chunks.get(entity_id, set()))
    chunks_per_entity = len(cited_chunks) / len(entity_path)
    
    return facts_per_entity, chunks_per_entity


def _compute_causal_coverage(
    explanation_facts: Set[str],
    edges: List[Dict[str, object]],
    procedure_nodes: Set[str],
) -> Tuple[float, int, int]:
    if not explanation_facts:
        return 0.0, 0, 0
    supported: Set[str] = set()
    for edge in edges:
        relation = edge.get("relation")
        if relation not in SEMANTIC_FACT_RELATIONS:
            continue
        source = edge.get("source")
        target = edge.get("target")
        if source in explanation_facts and target in explanation_facts:
            supported.add(str(source))
            supported.add(str(target))
        elif source in explanation_facts and target in procedure_nodes:
            supported.add(str(source))
        elif target in explanation_facts and source in procedure_nodes:
            supported.add(str(target))
    total = len(explanation_facts)
    return (len(supported) / total) if total else 0.0, len(supported), total


def _compute_hubbed_causal_coverage(
    explanation_facts: Set[str],
    edges: List[Dict[str, object]],
    seeded_frames: Set[str],
    procedure_nodes: Set[str],
) -> Tuple[float, int, int]:
    if not explanation_facts:
        return 0.0, 0, 0
    fact_to_frame: Dict[str, str] = {}
    for edge in edges:
        relation = edge.get("relation")
        if relation not in ANCHOR_RELATIONS:
            continue
        source = edge.get("source")
        target = edge.get("target")
        if source in explanation_facts and target:
            fact_to_frame[str(source)] = str(target)

    semantic_facts: Set[str] = set()
    for edge in edges:
        relation = edge.get("relation")
        if relation not in SEMANTIC_FACT_RELATIONS:
            continue
        source = edge.get("source")
        target = edge.get("target")
        if source in explanation_facts and target in explanation_facts:
            semantic_facts.add(str(source))
            semantic_facts.add(str(target))
        elif source in explanation_facts and target in procedure_nodes:
            semantic_facts.add(str(source))
        elif target in explanation_facts and source in procedure_nodes:
            semantic_facts.add(str(target))

    frame_has_semantic = {fact_to_frame[fact] for fact in semantic_facts if fact in fact_to_frame}
    active_frames = set(seeded_frames) | frame_has_semantic
    supported = set(semantic_facts)
    for fact_id, frame_id in fact_to_frame.items():
        if frame_id in active_frames:
            supported.add(fact_id)

    total = len(explanation_facts)
    return (len(supported) / total) if total else 0.0, len(supported), total


def _print_override_audit(
    fact_nodes: Dict[str, Dict[str, object]],
    fact_to_entity: Dict[str, str],
    procedure_nodes: Set[str],
    edges: List[Dict[str, object]],
) -> None:
    override_facts = [
        payload
        for payload in fact_nodes.values()
        if payload.get("fact_type") in {"overrides", "instead_of"}
    ]
    if not override_facts:
        print("\n=== Override Audit ===")
        print("No override facts found.")
        return

    procedure_edge_counts: Dict[str, int] = defaultdict(int)
    for edge in edges:
        source = edge.get("source")
        target = edge.get("target")
        if source in procedure_nodes:
            procedure_edge_counts[str(source)] += 1
        if target in procedure_nodes:
            procedure_edge_counts[str(target)] += 1

    owner_to_targets: Dict[str, Counter] = defaultdict(Counter)
    procedure_target_counts: Counter = Counter()
    raw_target_counts: Counter = Counter()
    for payload in override_facts:
        fact_id = str(payload.get("fact_id", ""))
        target = str(payload.get("override_target") or "").strip()
        owner = fact_to_entity.get(fact_id, "unowned")
        if not target:
            target = "(missing)"
        owner_to_targets[owner][target] += 1
        if target.startswith("procedure:"):
            procedure_target_counts[target] += 1
        else:
            raw_target_counts[target] += 1

    print("\n=== Override Audit ===")
    print(f"Override facts: {len(override_facts)}")
    print(f"Procedure targets: {sum(procedure_target_counts.values())}")
    print(f"Raw targets: {sum(raw_target_counts.values())}")

    if procedure_target_counts:
        print("Procedure targets (top 10):")
        for target, count in procedure_target_counts.most_common(10):
            edge_count = procedure_edge_counts.get(target, 0)
            node_status = "node" if target in procedure_nodes else "missing"
            print(f"  - {target}: {count} ({node_status}, edges={edge_count})")

    if raw_target_counts:
        print("Raw targets (top 10):")
        for target, count in raw_target_counts.most_common(10):
            print(f"  - {target}: {count}")

    print("Owners with override targets (top 10):")
    owner_items = sorted(
        owner_to_targets.items(),
        key=lambda item: (-sum(item[1].values()), item[0]),
    )[:10]
    for owner, counter in owner_items:
        total = sum(counter.values())
        top_targets = ", ".join(
            f"{target}({count})" for target, count in counter.most_common(3)
        )
        print(f"  - {owner}: {total} -> {top_targets}")


def _is_negative_expected(expected_summary: str) -> bool:
    text = (expected_summary or "").strip().lower()
    if not text:
        return False
    return text.startswith("no") or text.startswith("cannot") or text.startswith("can't")


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
        "--score-with-causal-adjacency",
        action="store_true",
        help="Use directed semantic-only adjacency for scoring traversal.",
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
    parser.add_argument(
        "--batch-paths",
        type=str,
        default="",
        help="Comma-separated batch JSON paths (overrides --batch-path).",
    )
    parser.add_argument(
        "--traversal-mode",
        choices=["full", "entity"],
        default="full",
        help="Traversal mode: 'full' (entity+fact mixed) or 'entity' (entity-only projection).",
    )
    parser.add_argument(
        "--save-query-metrics",
        type=str,
        default="",
        help="Path to save per-query metrics as JSON (for correlation analysis).",
    )
    args = parser.parse_args()

    base_path = Path(args.base_path)
    batch_paths: List[Path] = []
    if args.batch_paths:
        batch_paths = [Path(p.strip()) for p in args.batch_paths.split(",") if p.strip()]
    if not batch_paths:
        batch_paths = [Path(args.batch_path)]
    print(f"📂 Loading data from: {base_path}")
    print("📦 Loading batches:")
    for batch_path in batch_paths:
        print(f"  - {batch_path}")

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
    procedure_nodes = {
        n["id"]
        for n in graph.nodes
        if n.get("type") in {"Procedure", "ProcedureStep"}
    }
    relation_whitelist = set(RELATION_WHITELIST)
    if not args.enable_belongs_to and "belongs_to" in relation_whitelist:
        relation_whitelist.remove("belongs_to")
    adjacency = _build_adjacency(graph.edges, relation_whitelist)
    causal_edges = _build_causal_edges(graph.edges)
    causal_adjacency = _build_causal_adjacency(graph.edges)
    graph_payload = graph.to_dict()
    graph_payload["chunks"] = [chunk.to_dict() for chunk in chunks]
    vocabularies = load_vocabulary_from_graph_data(graph_payload, mention_type_mappings)
    mechanic_vocab = vocabularies.get("mechanic", set())
    entity_nodes = {n["id"]: n for n in graph.nodes if is_entity_like(n)}
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

    mechanic_kind_counts: Dict[str, int] = defaultdict(int)
    for entity_id, entity in entity_nodes.items():
        if entity.get("type") in MECHANIC_FRAME_TYPES:
            kind = entity.get("mechanic_kind") or "behavioral"
            mechanic_kind_counts[kind] += 1

    print(f"Entity nodes: {len(entity_nodes)}")
    print(f"Entity name index entries: {len(entity_name_index)}")
    print(f"Facts with BELONGS_TO: {len(fact_to_entity)}")
    coverage, exact_one, total_facts = _compute_ownership_coverage(fact_nodes, graph.edges)
    print(
        "Ownership coverage: "
        f"{exact_one}/{total_facts} facts with exactly 1 belongs_to ({coverage:.1%})"
    )

    if mechanic_kind_counts:
        counts_display = ", ".join(
            f"{kind}={count}" for kind, count in sorted(mechanic_kind_counts.items())
        )
        print(f"MechanicFrame kinds: {counts_display}")

    _print_override_audit(fact_nodes, fact_to_entity, procedure_nodes, graph.edges)

    global_invariant_violations = 0
    global_negative_expected = 0
    global_negative_justified = 0
    global_mentions_total = 0
    global_mentions_resolved = 0

    debug_mechanic_key = _normalize_name_key(args.debug_mechanic)

    # Determine traversal mode from CLI
    traversal_mode = TraversalMode.ENTITY_ONLY if args.traversal_mode == "entity" else TraversalMode.FULL
    print(f"🔧 Traversal mode: {traversal_mode.value}")
    
    # Build entity-only projection if needed
    entity_projection: Optional[TraversalProjection] = None
    if traversal_mode == TraversalMode.ENTITY_ONLY:
        entity_projection = TraversalProjection.build(graph_payload, mode=traversal_mode)
        print(f"  Entity projection: {len(entity_projection.entity_ids)} entities, {len(entity_projection.fact_nodes)} facts")
    
    # For per-query metrics (for correlation analysis)
    all_query_metrics: List[QueryMetrics] = []
    
    def run_batch(batch_path: Path) -> Tuple[int, int, int, int, int, List[QueryMetrics]]:
        print(f"\n=== Batch: {batch_path.name} ===")
        queries = _load_queries(batch_path)
        total_gold = 0
        total_found = 0
        total_found_at_5 = 0
        total_found_at_10 = 0
        evaluated_total = 0
        evaluated_scored = 0
        skipped_non_behavioral = 0
        behavioral_total = 0
        behavioral_active = 0
        structural_total = 0
        structural_silent = 0
        purity_scores: List[float] = []
        effective_purity_scores: List[float] = []
        compact_fact_counts: List[int] = []
        compact_frame_counts: List[int] = []
        compact_chunk_counts: List[int] = []
        causal_coverages: List[float] = []
        hubbed_causal_coverages: List[float] = []
        causal_coverage_failures = 0
        hubbed_causal_coverage_failures = 0
        minimality_passes = 0
        minimality_total = 0
        negative_expected_total = 0
        negative_justified_total = 0
        invariant_violations = 0
        mechanic_mentions_total = 0
        mechanic_mentions_resolved = 0
        
        # Entity-only metrics lists (Step 2)
        entity_semantic_purity_scores: List[float] = []
        entity_compactness_counts: List[int] = []
        frame_compactness_counts: List[int] = []
        facts_per_entity_scores: List[float] = []
        chunks_per_entity_scores: List[float] = []
        
        # Per-query metrics for correlation (Step 3)
        batch_query_metrics: List[QueryMetrics] = []

        for query in queries:
            query_id = query.get("id")
            question = query.get("question", "")
            gold_chunks = query.get("gold_chunk_ids", [])
            expected_summary = str(query.get("expected_answer_summary", "") or "")
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

            phase1_kind = "unknown"
            if query_id in PHASE1_BEHAVIORAL_QUERIES:
                phase1_kind = "behavioral"
            elif query_id in PHASE1_STRUCTURAL_QUERIES:
                phase1_kind = "structural"

            mechanic_mentions = [
                m for m in mentions if m.mention_type.value == "mechanic"
            ]
            resolved_mechanic_ids: Set[str] = set()
            behavioral_targets: Set[str] = set()
            resolved_kinds: Set[str] = set()
            for mention in mechanic_mentions:
                raw_text = mention.normalized or mention.surface or ""
                if raw_text.startswith("mechanic:"):
                    raw_text = raw_text.split(":", 1)[-1]
                name_key = _normalize_name_key(raw_text)
                if not name_key:
                    continue
                for entity_id in entity_name_index.get(name_key, set()):
                    if entity_nodes.get(entity_id, {}).get("type") not in MECHANIC_FRAME_TYPES:
                        continue
                    resolved_mechanic_ids.add(entity_id)
                    entity = entity_nodes.get(entity_id, {})
                    kind = entity.get("mechanic_kind") or "behavioral"
                    retrieval_target = entity.get("retrieval_target")
                    if retrieval_target is None:
                        retrieval_target = False
                    resolved_kinds.add(kind)
                    if retrieval_target:
                        behavioral_targets.add(entity_id)

            scoring_enabled = True
            if phase1_kind == "structural":
                scoring_enabled = False
            elif phase1_kind == "behavioral":
                scoring_enabled = True
            elif mechanic_mentions and resolved_mechanic_ids and not behavioral_targets:
                scoring_enabled = False

            if args.audit_mechanic_names:
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

            reachable, traversed_edges, visited_order = _traverse(
                seeds, adjacency, max_hops=args.max_hops
            )
            scoring_reachable = reachable
            if args.score_with_causal_adjacency:
                scoring_reachable, _, _ = _traverse(
                    seeds, causal_adjacency, max_hops=args.max_hops
                )
            
            # =========================================================
            # Entity-only traversal and metrics (per handoff Step 1-3)
            # =========================================================
            entity_path: Set[str] = set()
            attached_facts: Set[str] = set()
            entity_traversal_depth = 0
            
            if traversal_mode == TraversalMode.ENTITY_ONLY and entity_projection is not None:
                # Filter seeds to only entities
                entity_seeds = {s for s in seeds if s in entity_projection.entity_ids}
                
                # Run entity-only traversal
                entity_path, entity_edges, entity_order = traverse_entity_only(
                    entity_seeds, entity_projection, max_hops=args.max_hops
                )
                
                # Attach facts post-hoc
                attached_facts = entity_projection.attach_facts_post_hoc(entity_path)
                
                # Compute traversal depth
                entity_traversal_depth = len(entity_edges) if entity_edges else 0
            else:
                # In FULL mode, entity_path is entities from reachable set
                entity_path = {n for n in reachable if n in entity_nodes}
                # attached_facts are facts from reachable set
                attached_facts = {n for n in reachable if n in fact_nodes}
            
            # Compute entity-only metrics (Step 2)
            entity_purity, entity_sem_edges, entity_total_edges = _compute_entity_semantic_purity(
                entity_path, entity_nodes, graph.edges
            )
            entity_semantic_purity_scores.append(entity_purity)
            
            entity_count, frame_count = _compute_entity_compactness(
                entity_path, entity_nodes, MECHANIC_FRAME_TYPES
            )
            entity_compactness_counts.append(entity_count)
            frame_compactness_counts.append(frame_count)
            
            facts_per_entity, chunks_per_entity = _compute_assertion_load(
                entity_path, attached_facts, describes_by_entity
            )
            facts_per_entity_scores.append(facts_per_entity)
            chunks_per_entity_scores.append(chunks_per_entity)

            reachable_facts = {fact_id for fact_id in reachable if fact_id in fact_nodes}
            scoring_reachable_facts = {
                fact_id for fact_id in scoring_reachable if fact_id in fact_nodes
            }
            reachable_chunks = {
                fact_nodes[fact_id].get("source_chunk_id")
                for fact_id in reachable_facts
                if fact_nodes[fact_id].get("source_chunk_id")
            }

            gold_set = set(gold_chunks)
            found = gold_set & reachable_chunks
            ranked_chunks = _rank_chunks_from_reachable(
                visited_order,
                fact_nodes,
            )
            found_at_5 = gold_set & set(ranked_chunks[:5])
            found_at_10 = gold_set & set(ranked_chunks[:10])

            explanation_facts, active_facts, enabled_procedures, enabled_steps = (
                _apply_phase2_applicability(scoring_reachable, fact_nodes, graph.edges)
            )
            explanation_nodes = _collect_explanation_nodes_from_facts(
                explanation_facts, fact_nodes, graph.edges
            )
            purity, semantic_edges, total_edges = _compute_traversal_purity(
                explanation_nodes,
                graph.edges,
            )
            purity_scores.append(purity)
            eff_purity, eff_semantic, eff_total = _compute_effective_semantic_purity(
                explanation_nodes,
                graph.edges,
            )
            effective_purity_scores.append(eff_purity)

            explanation_frames = {
                node_id
                for node_id in explanation_nodes
                if entity_nodes.get(node_id, {}).get("type") in MECHANIC_FRAME_TYPES
            }
            explanation_chunks = {
                node_id for node_id in explanation_nodes if node_id in chunk_nodes
            }
            compact_fact_counts.append(len(explanation_facts))
            compact_frame_counts.append(len(explanation_frames))
            compact_chunk_counts.append(len(explanation_chunks))

            if explanation_facts - scoring_reachable_facts:
                invariant_violations += 1

            ccr, supported_facts, total_facts = _compute_causal_coverage(
                explanation_facts, causal_edges, procedure_nodes
            )
            causal_coverages.append(ccr)
            if ccr < 0.9 and total_facts:
                causal_coverage_failures += 1

            seeded_frames = {seed for seed in seeds if seed in explanation_frames}
            hub_ccr, hub_supported, hub_total = _compute_hubbed_causal_coverage(
                explanation_facts, causal_edges, seeded_frames, procedure_nodes
            )
            hubbed_causal_coverages.append(hub_ccr)
            if hub_ccr < 0.9 and hub_total:
                hubbed_causal_coverage_failures += 1

            multi_mechanic = len(resolved_mechanic_ids) > 1
            fact_bound = MULTI_MECHANIC_FACT_BOUND if multi_mechanic else SINGLE_MECHANIC_FACT_BOUND
            minimality_ok = (
                len(explanation_facts) <= fact_bound
                and len(explanation_frames) <= FRAME_FANOUT_BOUND
            )
            minimality_total += 1
            if minimality_ok:
                minimality_passes += 1

            negative_expected = _is_negative_expected(expected_summary)
            if negative_expected:
                negative_expected_total += 1
                explanation_fact_types = {
                    str(fact_nodes[fact_id].get("fact_type"))
                    for fact_id in explanation_facts
                    if fact_id in fact_nodes
                }
                if explanation_fact_types & NEGATION_FACT_TYPES:
                    negative_justified_total += 1
            
            # =============================================================
            # Create QueryMetrics for correlation analysis (Step 3)
            # =============================================================
            query_metrics = QueryMetrics(
                query_id=str(query_id),
                # Entity path metrics
                total_entity_count=len(entity_path),
                total_fact_count=len(attached_facts),
                entity_traversal_depth=entity_traversal_depth,
                # Entity-only purity
                entity_semantic_purity=entity_purity,
                entity_semantic_edges=entity_sem_edges,
                entity_total_edges=entity_total_edges,
                # Entity compactness
                entity_count=entity_count,
                frame_count=frame_count,
                # Assertion load
                facts_per_entity=facts_per_entity,
                chunks_per_entity=chunks_per_entity,
                # Gold coverage
                gold_hit=1 if found else 0,
                gold_found=len(found),
                gold_total=len(gold_set),
                # Causal coverage
                causal_coverage=ccr,
                # Mode
                traversal_mode=traversal_mode.value,
            )
            batch_query_metrics.append(query_metrics)

            print(f"\nQuery: {query_id}")
            print(f"  Mentions: {', '.join(mention_summary) if mention_summary else '(none)'}")
            print(f"  Seeds: {len(seeds)}")
            print(f"  Reachable facts: {len(reachable_facts)}")
            if args.score_with_causal_adjacency:
                print(f"  Scoring reachable facts: {len(scoring_reachable_facts)}")
            print(f"  Active facts (phase2 gates): {len(active_facts)}")
            print(
                "  Enabled procedures: "
                f"{len(enabled_procedures)} (steps: {len(enabled_steps)})"
            )
            print(f"  Gold found: {len(found)}/{len(gold_set)}")
            print(
                "  Traversal purity: "
                f"{semantic_edges}/{total_edges} semantic edges ({purity:.1%})"
            )
            print(
                "  Effective semantic purity (excludes belongs_to): "
                f"{eff_semantic}/{eff_total} semantic edges ({eff_purity:.1%})"
            )
            # Entity-only metrics (Step 2)
            if traversal_mode == TraversalMode.ENTITY_ONLY:
                print(
                    "  Entity semantic purity: "
                    f"{entity_sem_edges}/{entity_total_edges} semantic edges ({entity_purity:.1%})"
                )
                print(
                    "  Entity compactness: "
                    f"{entity_count} entities, {frame_count} frames"
                )
                print(
                    "  Assertion load: "
                    f"{facts_per_entity:.1f} facts/entity, {chunks_per_entity:.1f} chunks/entity"
                )
            print(
                "  Explanation compactness: "
                f"{len(explanation_facts)} facts, "
                f"{len(explanation_frames)} frames, "
                f"{len(explanation_chunks)} chunks"
            )
            if total_facts:
                print(
                    "  Causal coverage: "
                    f"{supported_facts}/{total_facts} facts supported ({ccr:.1%})"
                )
                print(
                    "  Hubbed causal coverage: "
                    f"{hub_supported}/{hub_total} facts supported ({hub_ccr:.1%})"
                )
            if minimality_total:
                bound_label = "multi" if multi_mechanic else "single"
                print(
                    "  Minimality: "
                    f"facts≤{fact_bound} ({bound_label}), "
                    f"frames≤{FRAME_FANOUT_BOUND} — {'ok' if minimality_ok else 'fail'}"
                )
            if negative_expected:
                neg_status = (
                    "justified" if explanation_fact_types & NEGATION_FACT_TYPES else "missing"
                )
                print(f"  Negation check: {neg_status}")
            if total_facts and ccr < 0.9:
                frames_sorted = sorted(explanation_frames)
                seeded_sorted = sorted(seeded_frames)
                incidental_frames = sorted(set(explanation_frames) - set(seeded_frames))
                print("  CCR failure analysis:")
                print(f"    Frames (seeded): {len(seeded_sorted)}")
                if seeded_sorted:
                    print(f"      - {', '.join(seeded_sorted[:6])}")
                print(f"    Frames (incidental): {len(incidental_frames)}")
                if incidental_frames:
                    print(f"      - {', '.join(incidental_frames[:6])}")

                fact_to_frame: Dict[str, str] = {}
                for edge in graph.edges:
                    relation = edge.get("relation")
                    if relation not in ANCHOR_RELATIONS:
                        continue
                    source = edge.get("source")
                    target = edge.get("target")
                    if source in explanation_facts and target:
                        fact_to_frame[str(source)] = str(target)

                facts_by_frame: Dict[str, List[str]] = defaultdict(list)
                for fact_id in explanation_facts:
                    frame_id = fact_to_frame.get(fact_id, "unowned")
                    facts_by_frame[frame_id].append(fact_id)
                for frame_id, fact_ids in sorted(
                    facts_by_frame.items(), key=lambda item: (-len(item[1]), item[0])
                ):
                    label = "seeded" if frame_id in seeded_frames else "incidental"
                    print(f"    Frame {frame_id} ({label}) -> {len(fact_ids)} facts")

                within_frame = 0
                cross_frame = 0
                for edge in causal_edges:
                    relation = edge.get("relation")
                    if relation not in SEMANTIC_FACT_RELATIONS:
                        continue
                    source = edge.get("source")
                    target = edge.get("target")
                    if source not in explanation_facts or target not in explanation_facts:
                        continue
                    source_frame = fact_to_frame.get(str(source))
                    target_frame = fact_to_frame.get(str(target))
                    if source_frame and target_frame and source_frame == target_frame:
                        within_frame += 1
                    else:
                        cross_frame += 1
                print(
                    "    Semantic edges: "
                    f"within-frame={within_frame}, cross-frame={cross_frame}"
                )

                structural_counts: Dict[str, int] = defaultdict(int)
                for edge in graph.edges:
                    relation = edge.get("relation")
                    source = edge.get("source")
                    target = edge.get("target")
                    if source not in explanation_nodes or target not in explanation_nodes:
                        continue
                    if relation in STRUCTURAL_RELATIONS:
                        structural_counts[str(relation)] += 1
                if structural_counts:
                    top_structural = sorted(
                        structural_counts.items(), key=lambda item: (-item[1], item[0])
                    )[:5]
                    formatted = ", ".join(f"{name}:{count}" for name, count in top_structural)
                    print(f"    Top structural edges: {formatted}")

                reachable_override_facts = [
                    fact_id
                    for fact_id in explanation_facts
                    if fact_nodes.get(fact_id, {}).get("fact_type") in {"overrides", "instead_of"}
                ]
                reachable_override_procedure = [
                    fact_id
                    for fact_id in reachable_override_facts
                    if str(fact_nodes.get(fact_id, {}).get("override_target") or "").startswith(
                        "procedure:"
                    )
                ]
                print(
                    "    Override facts reachable: "
                    f"{len(reachable_override_facts)} "
                    f"(procedure targets: {len(reachable_override_procedure)})"
                )
                for fact_id in reachable_override_facts[:3]:
                    payload = fact_nodes.get(fact_id, {})
                    owner = fact_to_entity.get(fact_id, "unowned")
                    target = payload.get("override_target")
                    print(
                        "    Override fact sample: "
                        f"{fact_id}({owner}) "
                        f"type={payload.get('fact_type')} "
                        f"target={target}"
                    )

                replaces_edges = [
                    edge for edge in graph.edges if edge.get("relation") == "replaces_effect"
                ]
                reachable_touching = [
                    edge
                    for edge in replaces_edges
                    if edge.get("source") in reachable or edge.get("target") in reachable
                ]
                explanation_internal = [
                    edge
                    for edge in replaces_edges
                    if edge.get("source") in explanation_nodes
                    and edge.get("target") in explanation_nodes
                ]
                print(
                    "    replaces_effect edges: "
                    f"global={len(replaces_edges)}, "
                    f"reachable_touching={len(reachable_touching)}, "
                    f"explanation_internal={len(explanation_internal)}"
                )
                if explanation_internal or reachable_touching:
                    sample_edges = (explanation_internal or reachable_touching)[:3]
                    for edge in sample_edges:
                        source_id = str(edge.get("source"))
                        target_id = str(edge.get("target"))
                        source_owner = fact_to_entity.get(source_id, "unowned")
                        target_owner = fact_to_entity.get(target_id, "unowned")
                        source_fact = fact_nodes.get(source_id, {})
                        target_fact = fact_nodes.get(target_id, {})
                        print(
                            "    replaces_effect sample: "
                            f"{source_id}({source_owner})[{source_fact.get('fact_type')}] "
                            f"-> {target_id}({target_owner})[{target_fact.get('fact_type')}] "
                            f"obj={source_fact.get('object')}"
                        )
            if mechanic_mentions:
                kind_display = (
                    ", ".join(sorted(resolved_kinds)) if resolved_kinds else "unresolved"
                )
                scoring_note = "enabled" if scoring_enabled else "skipped (non-behavioral)"
                print(f"  Mechanic kinds: {kind_display} — scoring {scoring_note}")
            if phase1_kind != "unknown":
                print(f"  Phase 1 kind: {phase1_kind}")
            if found:
                for chunk_id in sorted(found):
                    print(f"   - {chunk_id}")

            if debug_mechanic_key and args.mode == "mechanic_frames":
                if any(debug_mechanic_key in term for term in query_terms):
                    print("\n[Debug Mechanic] Clause/Facts dump")
                    for entity_id in sorted(seeds):
                        entity_name = _normalize_name_key(
                            entity_nodes.get(entity_id, {}).get("name", "")
                        )
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
                                clause_facts = extract_rule_facts(
                                    clause, mentions, resolved_config=None
                                )
                                mention_types = ",".join(
                                    sorted({m.mention_type.value for m in mentions})
                                )
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

            evaluated_total += 1
            if scoring_enabled:
                evaluated_scored += 1
                total_gold += len(gold_set)
                total_found += len(found)
                total_found_at_5 += len(found_at_5)
                total_found_at_10 += len(found_at_10)
            else:
                skipped_non_behavioral += 1

            if phase1_kind == "behavioral":
                behavioral_total += 1
                if reachable_facts:
                    behavioral_active += 1
            elif phase1_kind == "structural":
                structural_total += 1
                if not reachable_facts:
                    structural_silent += 1

            if args.query_limit and evaluated_total >= args.query_limit:
                break

        recall = (total_found / total_gold) if total_gold else 0.0
        recall_at_5 = (total_found_at_5 / total_gold) if total_gold else 0.0
        recall_at_10 = (total_found_at_10 / total_gold) if total_gold else 0.0
        avg_purity = sum(purity_scores) / len(purity_scores) if purity_scores else 0.0
        avg_eff_purity = (
            sum(effective_purity_scores) / len(effective_purity_scores)
            if effective_purity_scores
            else 0.0
        )
        avg_ccr = sum(causal_coverages) / len(causal_coverages) if causal_coverages else 0.0
        avg_hub_ccr = (
            sum(hubbed_causal_coverages) / len(hubbed_causal_coverages)
            if hubbed_causal_coverages
            else 0.0
        )
        avg_ccr = sum(causal_coverages) / len(causal_coverages) if causal_coverages else 0.0
        minimality_rate = (minimality_passes / minimality_total) if minimality_total else 0.0
        negation_rate = (
            (negative_justified_total / negative_expected_total) if negative_expected_total else 0.0
        )
        avg_facts = sum(compact_fact_counts) / len(compact_fact_counts) if compact_fact_counts else 0.0
        avg_frames = sum(compact_frame_counts) / len(compact_frame_counts) if compact_frame_counts else 0.0
        avg_chunks = sum(compact_chunk_counts) / len(compact_chunk_counts) if compact_chunk_counts else 0.0
        
        # Entity-only metric averages (Step 2)
        avg_entity_purity = (
            sum(entity_semantic_purity_scores) / len(entity_semantic_purity_scores)
            if entity_semantic_purity_scores else 0.0
        )
        avg_entity_compactness = (
            sum(entity_compactness_counts) / len(entity_compactness_counts)
            if entity_compactness_counts else 0.0
        )
        avg_frame_compactness = (
            sum(frame_compactness_counts) / len(frame_compactness_counts)
            if frame_compactness_counts else 0.0
        )
        avg_facts_per_entity = (
            sum(facts_per_entity_scores) / len(facts_per_entity_scores)
            if facts_per_entity_scores else 0.0
        )
        avg_chunks_per_entity = (
            sum(chunks_per_entity_scores) / len(chunks_per_entity_scores)
            if chunks_per_entity_scores else 0.0
        )
        
        print("\n=== Summary ===")
        print(f"Queries evaluated: {evaluated_total}")
        if skipped_non_behavioral:
            print(
                "Queries skipped (non-behavioral frames only): "
                f"{skipped_non_behavioral}"
            )
        if evaluated_scored != evaluated_total:
            print(f"Queries scored: {evaluated_scored}")
        if behavioral_total:
            activation_rate = behavioral_active / behavioral_total
            print(
                "Behavioral activation rate: "
                f"{behavioral_active}/{behavioral_total} ({activation_rate:.1%})"
            )
        if structural_total:
            silence_rate = structural_silent / structural_total
            print(
                "Structural silence correctness: "
                f"{structural_silent}/{structural_total} ({silence_rate:.1%})"
            )
        print(f"Gold chunks found: {total_found}/{total_gold} ({recall:.2%})")
        print(f"Recall@5: {total_found_at_5}/{total_gold} ({recall_at_5:.2%})")
        print(f"Recall@10: {total_found_at_10}/{total_gold} ({recall_at_10:.2%})")
        print(f"Avg traversal purity: {avg_purity:.2%}")
        if effective_purity_scores:
            print(f"Avg effective semantic purity (excludes belongs_to): {avg_eff_purity:.2%}")
        print(
            f"Avg explanation compactness: {avg_facts:.1f} facts, "
            f"{avg_frames:.1f} frames, {avg_chunks:.1f} chunks"
        )
        if causal_coverages:
            print(
                "Causal coverage (CCR): "
                f"{avg_ccr:.1%} avg "
                f"(failures <0.9: {causal_coverage_failures}/{len(causal_coverages)})"
            )
        if hubbed_causal_coverages:
            print(
                "Hubbed causal coverage (CCR’): "
                f"{avg_hub_ccr:.1%} avg "
                f"(failures <0.9: {hubbed_causal_coverage_failures}/{len(hubbed_causal_coverages)})"
            )
        scoring_label = (
            "directed semantic-only adjacency"
            if args.score_with_causal_adjacency
            else "retrieval adjacency"
        )
        print(f"Scoring traversal: {scoring_label}")
        if minimality_total:
            print(
                "Minimality pass rate: "
                f"{minimality_passes}/{minimality_total} ({minimality_rate:.1%})"
            )
        if negative_expected_total:
            print(
                "Justified negation rate: "
                f"{negative_justified_total}/{negative_expected_total} ({negation_rate:.1%})"
            )
        if invariant_violations:
            print(f"⚠️  Invariant violations: {invariant_violations}")
        if mechanic_mentions_total:
            resolvability = mechanic_mentions_resolved / mechanic_mentions_total
            print(
                "Name resolvability: "
                f"{mechanic_mentions_resolved}/{mechanic_mentions_total} "
                f"({resolvability:.1%})"
            )
        
        # Entity-only metrics summary (Step 2)
        if traversal_mode == TraversalMode.ENTITY_ONLY:
            print("\n=== Entity-Only Metrics ===")
            print(f"Avg entity semantic purity: {avg_entity_purity:.2%}")
            print(
                f"Avg entity compactness: {avg_entity_compactness:.1f} entities, "
                f"{avg_frame_compactness:.1f} frames"
            )
            print(
                f"Avg assertion load: {avg_facts_per_entity:.1f} facts/entity, "
                f"{avg_chunks_per_entity:.1f} chunks/entity"
            )

        return (
            invariant_violations,
            negative_expected_total,
            negative_justified_total,
            mechanic_mentions_total,
            mechanic_mentions_resolved,
            batch_query_metrics,
        )

    for batch_path in batch_paths:
        result = run_batch(batch_path)
        inv, neg_total, neg_justified, mentions_total, mentions_resolved, query_metrics = result
        global_invariant_violations += inv
        global_negative_expected += neg_total
        global_negative_justified += neg_justified
        global_mentions_total += mentions_total
        global_mentions_resolved += mentions_resolved
        all_query_metrics.extend(query_metrics)

    print("\n=== Global Invariants ===")
    print(f"Invariant violations: {global_invariant_violations}")
    if global_negative_expected:
        global_neg_rate = global_negative_justified / global_negative_expected
        print(
            "Justified negation rate (global): "
            f"{global_negative_justified}/{global_negative_expected} ({global_neg_rate:.1%})"
        )
    if global_mentions_total:
        global_res_rate = global_mentions_resolved / global_mentions_total
        print(
            "Name resolvability (global): "
            f"{global_mentions_resolved}/{global_mentions_total} ({global_res_rate:.1%})"
        )
    
    # =============================================================
    # Save query metrics and compute correlations (Step 3.2-3.3)
    # =============================================================
    if all_query_metrics:
        print(f"\n=== Correlation Analysis ({len(all_query_metrics)} queries) ===")
        
        # Extract values for correlation
        purity_vals = [m.entity_semantic_purity for m in all_query_metrics]
        coverage_vals = [m.causal_coverage for m in all_query_metrics]
        compactness_vals = [float(m.entity_count) for m in all_query_metrics]
        gold_hit_vals = [float(m.gold_hit) for m in all_query_metrics]
        assertion_load_vals = [m.facts_per_entity for m in all_query_metrics]
        
        # Simple Pearson correlation (manual calculation to avoid numpy dependency)
        def pearson_corr(x: List[float], y: List[float]) -> float:
            """Compute Pearson correlation coefficient."""
            n = len(x)
            if n < 3:
                return 0.0
            mean_x = sum(x) / n
            mean_y = sum(y) / n
            cov = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)) / n
            std_x = (sum((xi - mean_x) ** 2 for xi in x) / n) ** 0.5
            std_y = (sum((yi - mean_y) ** 2 for yi in y) / n) ** 0.5
            if std_x == 0 or std_y == 0:
                return 0.0
            return cov / (std_x * std_y)
        
        # Key correlations per Step 3.3
        corr_purity_coverage = pearson_corr(purity_vals, coverage_vals)
        corr_compactness_gold = pearson_corr(compactness_vals, gold_hit_vals)
        corr_assertion_purity = pearson_corr(assertion_load_vals, purity_vals)
        
        print(f"  entity_semantic_purity vs causal_coverage: r={corr_purity_coverage:.3f}")
        print(f"  entity_compactness vs gold_hit: r={corr_compactness_gold:.3f}")
        print(f"  assertion_load vs entity_semantic_purity: r={corr_assertion_purity:.3f}")
        
        # Interpretation per Step 3.3
        print("\nExpected patterns (entity-only mode):")
        print("  - purity vs coverage: should be positive (purity correlates with causal coverage)")
        print("  - compactness vs gold_hit: should be negative (fewer entities = better hit rate)")
        print("  - assertion_load vs purity: should be uncorrelated or weakly positive")
    
    # Save metrics to JSON if requested
    if args.save_query_metrics and all_query_metrics:
        metrics_path = Path(args.save_query_metrics)
        metrics_data = {
            "traversal_mode": traversal_mode.value,
            "query_count": len(all_query_metrics),
            "queries": [m.to_dict() for m in all_query_metrics],
        }
        with open(metrics_path, "w") as f:
            json.dump(metrics_data, f, indent=2)
        print(f"\n📊 Query metrics saved to: {metrics_path}")


if __name__ == "__main__":
    run()
