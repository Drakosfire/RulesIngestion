"""RLH-03 consumer proof against exact pinned DungeonMind contracts."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from dungeonmind.infrastructure.memory.vnext_knowledge import (
    InMemoryKnowledgeRevisionRepository,
)

from semantic_lifting.dungeonmind_export import FIXTURE, publish_occupancy


def test_accepted_claims_publish_and_reopen_with_exact_evidence() -> None:
    repo = InMemoryKnowledgeRevisionRepository()
    witness = publish_occupancy(FIXTURE, repo)
    assert witness["genesis_revision_id"] != witness["published_revision_id"]
    assert len(witness["accepted_candidate_ids"]) == 2
    assert len(witness["excluded_candidate_ids"]) == 2
    assert len(witness["reopened_assertions"]) == 2
    evidence_id = witness["evidence_ref"]["evidence_ref_id"]
    for assertion in witness["reopened_assertions"]:
        assert assertion["metadata"]["evidence_ref_ids"] == [evidence_id]
    assert witness["evidence_ref"]["source_locator"].endswith(
        json.loads((FIXTURE / "source_manifest.json").read_text())["evidence_unit_id"]
    )
    assert (
        repo.get_head(witness["space_id"]).head_revision_id
        == witness["published_revision_id"]
    )
    assert all(
        excluded not in json.dumps(witness["reopened_assertions"])
        for excluded in witness["excluded_candidate_ids"]
    )
    published_text = json.dumps(witness["reopened_assertions"]).lower()
    assert "prone ally" not in published_text
    assert "gains condition" not in published_text


def test_missing_gold_or_evidence_fails_before_publication(tmp_path: Path) -> None:
    for name in (
        "source_manifest.json",
        "stageA.surface.ast.json",
        "stageB.evidence_units.json",
        "candidate_package.json",
        "human_gold.json",
    ):
        (tmp_path / name).write_bytes((FIXTURE / name).read_bytes())
    package_path = tmp_path / "candidate_package.json"
    package = json.loads(package_path.read_text())
    package["candidates"][0]["evidence_unit_ids"] = ["missing"]
    package_path.write_text(json.dumps(package))
    repo = InMemoryKnowledgeRevisionRepository()
    with pytest.raises(ValueError, match="inexact evidence"):
        publish_occupancy(tmp_path, repo)
    assert repo.get_head("space:rules-occupancy-srd-5-2-1-v1") is None
