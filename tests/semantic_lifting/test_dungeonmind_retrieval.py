"""RLH-04 exact cited search and truthful miss characterization."""

from __future__ import annotations

import json

import pytest
from dungeonmind.infrastructure.memory.vnext_knowledge import (
    InMemoryKnowledgeRevisionRepository,
)

from semantic_lifting.dungeonmind_export import FIXTURE, publish_occupancy
from semantic_lifting.dungeonmind_retrieval import pinned_context, retrieve


def test_bounded_queries_recover_exact_evidence_and_truthful_miss() -> None:
    repo = InMemoryKnowledgeRevisionRepository()
    witness = publish_occupancy(FIXTURE, repo)
    context = pinned_context(repo, witness, fixture=FIXTURE)
    benchmark = json.loads((FIXTURE / "retrieval_benchmark.json").read_text())
    expected = json.loads((FIXTURE / "source_manifest.json").read_text())[
        "evidence_unit_id"
    ]
    for query in benchmark["queries"]:
        first = retrieve(context, query["question"], top_k=3)
        second = retrieve(context, query["question"], top_k=3)
        first.pop("latency_ms")
        second.pop("latency_ms")
        assert first == second
        assert first["completeness"] == "complete"
        if query["required_gold"]:
            assert first["mapped_evidence_unit_ids"] == [expected]
            assert all(
                hit["source_uri"].startswith("https://") for hit in first["hits"]
            )
        else:
            assert first["mapped_evidence_unit_ids"] == []
            assert first["hits"] == []


def test_wrong_revision_is_rejected_before_search() -> None:
    repo = InMemoryKnowledgeRevisionRepository()
    witness = publish_occupancy(FIXTURE, repo)
    witness["published_revision_id"] = "rev:missing"
    with pytest.raises(ValueError, match="Exact published revision"):
        pinned_context(repo, witness, fixture=FIXTURE)
