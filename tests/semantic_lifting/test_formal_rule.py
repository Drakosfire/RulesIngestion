import json
from pathlib import Path

import pytest

from semantic_lifting.formal_rule import canonical_bytes, compile_occupancy, verify_digest


FIXTURE = Path(__file__).resolve().parents[2] / "evals/semantic_lifting/occupancy_v1"


def _review():
    return json.loads((FIXTURE / "formal_review.json").read_text())


def test_reviewed_artifact_is_deterministic_and_exactly_sourced():
    first = compile_occupancy(FIXTURE, _review())
    second = compile_occupancy(FIXTURE, _review())
    stored = json.loads((FIXTURE / "formal_rule_artifact.json").read_text())
    assert canonical_bytes(first) == canonical_bytes(second) == canonical_bytes(stored)
    assert verify_digest(first)
    assert first["decision"]["then"] == "reject"
    assert first["exceptions"] == []
    assert first["evidence"]["evidence_unit_ids"] == [
        "04786f12722f6b15ccb70b18995b060e473ac07115b43dfdba3ca59ae685061d"
    ]
    assert first["compiler"]["graph_closure_used"] is False


def test_unreviewed_or_rejected_candidate_cannot_be_compiled():
    for disposition in ("pending", "rejected"):
        review = {**_review(), "disposition": disposition}
        with pytest.raises(ValueError, match="approval"):
            compile_occupancy(FIXTURE, review)
    review = {**_review(), "approved_rule_id": "other"}
    with pytest.raises(ValueError, match="approval"):
        compile_occupancy(FIXTURE, review)


def test_digest_rejects_mutation():
    artifact = compile_occupancy(FIXTURE, _review())
    artifact["decision"]["then"] = "allow"
    assert not verify_digest(artifact)
