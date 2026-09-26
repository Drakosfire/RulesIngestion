"""Audit whether the published fixture can support a graph-value comparison."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "evals/semantic_lifting/occupancy_v1"


def build_decision() -> dict:
    comparison = json.loads((FIXTURE / "retrieval_comparison.json").read_text())
    witness = json.loads((FIXTURE / "dungeonmind_publication_witness.json").read_text())
    source_units = json.loads((FIXTURE / "stageB.evidence_units.json").read_text())["units"]
    rows = comparison["rows"]
    published = witness["reopened_assertions"]
    assert comparison["citation_mapping_exact"] and comparison["repeated_run_deterministic"]
    assert len(source_units) == 1 and len(published) == 2
    grounded = [row for row in rows if row["required_gold"]]
    assert grounded
    baseline_coverage = sum(set(row["required_gold"]) <= set(row["baseline"]["mapped_evidence_unit_ids"])
                            for row in grounded)
    dm_coverage = sum(set(row["required_gold"]) <= set(row["dungeonmind"]["mapped_evidence_unit_ids"])
                      for row in grounded)
    return {
        "schema_version": "rlh05_graph_value_decision_v1",
        "disposition": "GRAPH_ASSIST_NO_PROMOTION",
        "acceptance_status": "blocked_substrate_gap",
        "scope": "published_2024_srd_occupancy_fixture_only",
        "decision_basis": "No incremental required-evidence opportunity on the available one-unit fixture; multihop comparison blocked by absent source-grounded substrate.",
        "published_revision_id": comparison["revision_id"],
        "source_evidence_units": len(source_units),
        "published_assertions": len(published),
        "grounding_queries": len(grounded),
        "treatments": {
            "A_existing_bm25": {"required_full_set": baseline_coverage, "total": len(grounded)},
            "B_dungeonmind_retrieval": {"required_full_set": dm_coverage, "total": len(grounded)},
            "C_graph_closure": {"status": "not_identifiable", "reason": "all accepted assertions cite the same EvidenceUnit"},
            "D_structured_edge_adjudication": {"status": "not_run", "reason": "no human-gold multihop edges"},
            "E_jev_edge_adjudication": {"status": "not_run", "reason": "no human-gold multihop edges"},
        },
        "metrics_not_estimable": [
            "added_evidence_precision", "edge_adjudication_accuracy", "answer_support_delta",
            "last_required_evidence_rank_delta", "edge_review_rate", "graph_latency_cost_delta",
        ],
        "promotion_allowed": False,
        "next_fixture_requirement": "At least two distinct exact source EvidenceUnits in a published multihop neighborhood with human-gold edges and required-evidence sets.",
    }


if __name__ == "__main__":
    print(json.dumps(build_decision(), indent=2, sort_keys=True))
