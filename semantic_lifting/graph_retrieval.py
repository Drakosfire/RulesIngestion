"""Bounded graph closure over exact, source-backed assertion evidence."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class EvidenceNode:
    assertion_id: str
    evidence_ref_id: str
    evidence_unit_id: str
    source_artifact_id: str
    source_revision_id: str


@dataclass(frozen=True)
class GraphEdge:
    edge_id: str
    source_assertion_id: str
    target_assertion_id: str
    relation: str
    human_gold: Literal["retain", "reject", "review"]


def bounded_closure(
    *, query: str, seed_assertion_ids: list[str], nodes: dict[str, EvidenceNode],
    edges: list[GraphEdge], max_hops: int = 2, max_edges: int = 12,
    max_evidence: int = 8, retained_edge_ids: set[str] | None = None,
) -> dict:
    """Return admitted evidence and actual paths; an edge alone never cites."""
    if not 0 <= max_hops <= 2 or max_edges < 0 or max_evidence < 1:
        raise ValueError("Invalid bounded graph budget")
    if any(seed not in nodes for seed in seed_assertion_ids):
        raise ValueError("Seed assertion lacks evidence")
    if any(not all((node.evidence_ref_id, node.evidence_unit_id,
                    node.source_artifact_id, node.source_revision_id)) for node in nodes.values()):
        raise ValueError("Graph node lacks exact source evidence")
    seen = set(seed_assertion_ids)
    ordered = list(dict.fromkeys(seed_assertion_ids))[:max_evidence]
    frontier = [(seed, []) for seed in ordered]
    paths = [{"assertion_id": seed, "via_edges": [], "evidence_unit_id": nodes[seed].evidence_unit_id}
             for seed in ordered]
    traversed = 0
    for _hop in range(max_hops):
        next_frontier = []
        for current, path in frontier:
            for edge in edges:
                if traversed >= max_edges or len(ordered) >= max_evidence:
                    break
                if edge.source_assertion_id != current or edge.target_assertion_id in seen:
                    continue
                if retained_edge_ids is not None and edge.edge_id not in retained_edge_ids:
                    continue
                traversed += 1
                target = edge.target_assertion_id
                if target not in nodes:
                    continue
                seen.add(target)
                ordered.append(target)
                target_path = [*path, edge.edge_id]
                next_frontier.append((target, target_path))
                paths.append({"assertion_id": target, "via_edges": target_path,
                              "evidence_unit_id": nodes[target].evidence_unit_id})
        frontier = next_frontier
        if not frontier:
            break
    evidence = list(dict.fromkeys(nodes[assertion].evidence_unit_id for assertion in ordered))
    return {"query": query, "seed_assertion_ids": seed_assertion_ids,
            "traversed_edges": traversed, "paths": paths,
            "final_evidence_unit_ids": evidence}
