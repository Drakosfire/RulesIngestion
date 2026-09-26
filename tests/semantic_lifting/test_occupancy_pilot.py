"""Evidence and replay guards for the bounded occupancy pilot."""

from __future__ import annotations

import json
import asyncio
from pathlib import Path

import pytest
from generationengine import InferenceObservation, ObservationState

from semantic_lifting.contracts import ge_receipt
from semantic_lifting.occupancy import SemanticCandidate, compare_with_gold, load_exact_evidence
from semantic_lifting.proposal import proposal_contract
from scripts.run_occupancy_semantic_pilot import run


FIXTURE = Path(__file__).resolve().parents[2] / "evals/semantic_lifting/occupancy_v1"


def test_exact_source_unit_replays_from_stage_b() -> None:
    units = load_exact_evidence(FIXTURE)
    manifest = json.loads((FIXTURE / "source_manifest.json").read_text())
    assert len(units) == 1
    assert units[0].unit_id == manifest["evidence_unit_id"]
    assert units[0].page_fingerprint == manifest["page_fingerprint"]
    assert "You can’t willingly end a move" in units[0].text
    assert "Prone condition" in units[0].text


def test_candidate_without_exact_evidence_is_rejected() -> None:
    with pytest.raises(ValueError, match="EvidenceUnit"):
        SemanticCandidate.from_proposal(
            {"kind": "exception", "subject": "ally", "predicate": "permits sharing", "value": "yes",
             "evidence_unit_ids": ["invented-unit"]},
            evidence_ids={"actual-unit"}, origin="test",
        )


def test_human_and_treatments_must_cover_same_candidates() -> None:
    unit_id = load_exact_evidence(FIXTURE)[0].unit_id
    candidate = SemanticCandidate.from_proposal(
        {"kind": "restriction", "subject": "creature", "predicate": "cannot share", "value": "occupied",
         "evidence_unit_ids": [unit_id]}, evidence_ids={unit_id}, origin="test",
    )
    with pytest.raises(ValueError, match="same candidates"):
        compare_with_gold([candidate], {candidate.candidate_id: "accept"}, {"jev": {}})


def test_offline_replay_rejects_receipt_contract_drift(tmp_path: Path) -> None:
    for name in ("stageA.surface.ast.json", "stageB.evidence_units.json", "source_manifest.json",
                 "human_gold.json", "candidate_package.json"):
        (tmp_path / name).write_bytes((FIXTURE / name).read_bytes())
    evidence = [unit.to_dict() for unit in load_exact_evidence(tmp_path)]
    contract = proposal_contract(evidence, "gpt-5.3-codex")
    source_receipt = json.loads((FIXTURE / "provider_receipts/proposal.json").read_text())
    observation = InferenceObservation(provider="openai", requested_model="gpt-5.3-codex",
                                       resolved_model="gpt-5.3-codex", latency_ms=1,
                                       retry_count=0, state=ObservationState.COMPLETED)
    receipt = ge_receipt(contract, observation, source_receipt["output"])
    target = tmp_path / "generationengine_v2/provider_receipts/proposal.json"
    target.parent.mkdir(parents=True)
    receipt["request_digest"] = "tampered"
    target.write_text(json.dumps(receipt))
    with pytest.raises(ValueError, match="contract drift"):
        asyncio.run(run(tmp_path, proposal_model="gpt-5.3-codex", adjudicator_model="gpt-5.3-codex",
                        jev_model="typesafe-ai/jev", live=False))
