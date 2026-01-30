"""Traversal validation for Typed Relations (Phase 4)."""

from __future__ import annotations

from collections import defaultdict, deque
from pathlib import Path
from typing import Dict, Iterable, List, Set
import json
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from enrichment.chunks import EnrichedChunk
from enrichment.graph_builder import build_fact_graph
from enrichment.vocabulary_loader import load_mention_type_mappings


def _load_chunks(base_path: Path) -> List[EnrichedChunk]:
    with open(base_path) as f:
        data = json.load(f)

    valid_fields = {f.name for f in EnrichedChunk.__dataclass_fields__.values()}
    chunks = []
    for chunk_dict in data.get("chunks", []):
        filtered = {k: v for k, v in chunk_dict.items() if k in valid_fields}
        chunks.append(EnrichedChunk(**filtered))
    return chunks


def _build_adjacency(edges: Iterable[Dict[str, object]], relation_whitelist: Set[str]) -> Dict[str, Set[str]]:
    adjacency: Dict[str, Set[str]] = defaultdict(set)
    for edge in edges:
        relation = edge.get("relation")
        if relation not in relation_whitelist:
            continue
        source = edge.get("source")
        target = edge.get("target")
        if not source or not target:
            continue
        adjacency[source].add(target)
        adjacency[target].add(source)
    return adjacency


def _normalize_subject(value: object) -> str:
    return str(value or "").strip().lower()


def _has_subject_object(payload: Dict[str, object]) -> bool:
    subject = _normalize_subject(payload.get("subject"))
    obj = str(payload.get("object") or "").strip()
    return bool(subject and obj)


def _seed_facts(fact_nodes: Dict[str, Dict[str, object]]) -> Set[str]:
    seeds = set()
    for fact_id, payload in fact_nodes.items():
        scope = (payload.get("scope") or "").lower()
        fact_type = payload.get("fact_type")
        subject = _normalize_subject(payload.get("subject"))
        is_complete = bool(payload.get("is_complete", True))
        confidence = float(payload.get("confidence") or 0)
        has_subject_object = _has_subject_object(payload)
        subject_type = payload.get("subject_type")
        if (
            fact_type == "role_gate"
            and "role:" in scope
            and has_subject_object
            and is_complete
            and confidence >= 0.9
        ):
            seeds.add(fact_id)
        if (
            fact_type == "level_gate"
            and has_subject_object
            and is_complete
            and confidence >= 0.9
            and subject_type == "mechanic"
        ):
            seeds.add(fact_id)
    return seeds


def _traverse(seeds: Set[str], adjacency: Dict[str, Set[str]], max_hops: int = 3) -> Set[str]:
    if not seeds:
        return set()
    visited = set(seeds)
    queue = deque([(seed, 0) for seed in seeds])
    while queue:
        node, depth = queue.popleft()
        if depth >= max_hops:
            continue
        for neighbor in adjacency.get(node, set()):
            if neighbor in visited:
                continue
            visited.add(neighbor)
            queue.append((neighbor, depth + 1))
    return visited


def run() -> None:
    base_path = Path(
        "Rules/StarFinder2e/PlayerCore/outputs/runs/2026-01-25_19-16-02/enriched/merged.enriched.json"
    )
    print(f"📂 Loading data from: {base_path}")
    chunks = _load_chunks(base_path)

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
    relation_whitelist = {
        "applies_to_role",
        "requires_level",
        "same_subject",
        "triggers",
        "unless",
        "in_same_chunk",
    }
    adjacency = _build_adjacency(graph.edges, relation_whitelist)
    relation_counts = defaultdict(int)
    for edge in graph.edges:
        relation = edge.get("relation")
        if relation in relation_whitelist:
            relation_counts[relation] += 1

    seeds = _seed_facts(fact_nodes)
    print(f"Seeds: {len(seeds)}")
    if relation_counts:
        print("Relations:")
        for rel, count in sorted(relation_counts.items(), key=lambda item: (-item[1], item[0])):
            print(f"  {rel}: {count}")

    reachable = _traverse(seeds, adjacency, max_hops=4)
    reachable_facts = {fact_id for fact_id in reachable if fact_id in fact_nodes}
    print(f"Reachable facts: {len(reachable_facts)}")

    chunk_nodes = {n["id"] for n in graph.nodes if n.get("type") == "chunk"}
    reachable_chunks = {node_id for node_id in reachable if node_id in chunk_nodes}
    reachable_chunks.update(
        {
            fact_nodes[fact_id].get("source_chunk_id")
            for fact_id in reachable_facts
            if fact_nodes[fact_id].get("source_chunk_id")
        }
    )

    gold_chunks = {
        "sf2e-playercore-PZO22001-Starfinder-Player-Core-058-073::/page/1/Text/12",
        "sf2e-playercore-PZO22001-Starfinder-Player-Core-058-073::/page/3/SectionHeader/24",
        "sf2e-playercore-PZO22001-Starfinder-Player-Core-058-073::/page/3/SectionHeader/28",
        "sf2e-playercore-PZO22001-Starfinder-Player-Core-138-149::/page/2/Table/2",
        "sf2e-playercore-PZO22001-Starfinder-Player-Core-138-149::/page/3/Text/8",
    }

    found = gold_chunks & reachable_chunks
    print(f"Gold chunks found: {len(found)}/5")
    if found:
        print("Found chunks:")
        for chunk_id in sorted(found):
            print(f"  - {chunk_id}")


if __name__ == "__main__":
    run()
