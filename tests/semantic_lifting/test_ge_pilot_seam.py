"""RIGE-01 owner-boundary proof against a fake GenerationEngine client."""

from __future__ import annotations

import asyncio
import json
import tomllib
from pathlib import Path

from generationengine import (
    BinaryDecisionAnswer,
    ChoiceDecisionAnswer,
    DecisionResult,
    GenerationClient,
    InferenceObservation,
    ObservationState,
    TextGenerationResult,
    TextResult,
)

from scripts.run_occupancy_semantic_pilot import run
from semantic_lifting.adjudication import (
    CLASSIFICATION_CRITERIA,
    DISPOSITION_CRITERIA,
    adjudicate_structured,
)
from semantic_lifting.contracts import GENERATIONENGINE_COMMIT, ge_contract, ge_receipt
from semantic_lifting.proposal import propose

FIXTURE = Path(__file__).resolve().parents[2] / "evals/semantic_lifting/occupancy_v1"


def observation(provider: str, model: str, *, latency_ms: int = 1) -> InferenceObservation:
    return InferenceObservation(
        provider=provider, requested_model=model, resolved_model=model,
        response_model=model,
        provider_transport="vercel_ai_gateway" if provider == "typesafe" else None,
        input_tokens=0, output_tokens=2, latency_ms=latency_ms,
        retry_count=0, provider_attempt_count=1, state=ObservationState.COMPLETED,
    )


class FakeGE:
    def __init__(self):
        self.structured_calls = []
        self.decision_calls = []

    async def generate_structured(self, request):
        self.structured_calls.append(request)
        assert request.provider == "openai"
        assert request.temperature is None
        assert request.json_schema
        if request.schema_name == "ProposalBatch":
            output = json.loads((FIXTURE / "provider_receipts/proposal.json").read_text())["output"]
        else:
            candidate_id = json.loads(request.user_prompt)["candidate"]["candidate_id"]
            output = json.loads((FIXTURE / "provider_receipts/structured" / f"{candidate_id}.json").read_text())["output"]
        return TextResult(parsed=output, observation=observation("openai", request.model))

    async def decide(self, request):
        self.decision_calls.append(request)
        candidate_id = request.state["candidate"]["candidate_id"]
        legacy = json.loads((FIXTURE / "provider_receipts/jev" / f"{candidate_id}.json").read_text())
        output = legacy["output"]
        assert request.provider == "typesafe"
        assert request.questions[0].option_descriptions == CLASSIFICATION_CRITERIA
        assert request.questions[2].option_descriptions == DISPOSITION_CRITERIA
        return DecisionResult(
            answers={
                "classification": ChoiceDecisionAnswer(selected=output["classification"]),
                "evidence_sufficient": BinaryDecisionAnswer(
                    value=output["evidence_sufficient"],
                    probability_true=output["evidence_sufficient_probability"],
                ),
                "disposition": ChoiceDecisionAnswer(selected=output["disposition"]),
            },
            observation=observation("typesafe", request.model),
        )


def test_ge_pilot_preserves_frozen_gold_and_writes_only_versioned_receipts(tmp_path: Path):
    for name in ("stageA.surface.ast.json", "stageB.evidence_units.json", "source_manifest.json",
                 "human_gold.json", "candidate_package.json"):
        (tmp_path / name).write_bytes((FIXTURE / name).read_bytes())
    fake = FakeGE()
    summary = asyncio.run(run(tmp_path, proposal_model="gpt-5.3-codex",
                              adjudicator_model="gpt-5.3-codex", jev_model="typesafe-ai/jev",
                              live=True, client=fake))
    assert summary["generationengine_commit"] == GENERATIONENGINE_COMMIT
    assert summary["proposal_delta"]["same_candidate_ids"] is True
    assert summary["rates"]["structured_llm"]["correct"] == 4
    assert summary["rates"]["jev"]["correct"] == 4
    assert len(fake.structured_calls) == 5
    assert len(fake.decision_calls) == 4
    assert not (tmp_path / "provider_receipts").exists()
    assert (tmp_path / "generationengine_v2/provider_receipts/proposal.json").exists()
    assert (tmp_path / "candidate_package.json").read_bytes() == (FIXTURE / "candidate_package.json").read_bytes()
    replay = asyncio.run(run(tmp_path, proposal_model="gpt-5.3-codex",
                             adjudicator_model="gpt-5.3-codex", jev_model="typesafe-ai/jev",
                             live=False))
    assert replay == summary


def test_ge_receipt_semantic_digest_ignores_transport_telemetry():
    contract = ge_contract(operation="decide", provider="typesafe", model="alias",
                           input_digest="state", questions_hash="questions")
    first = ge_receipt(contract, observation("typesafe", "alias", latency_ms=1), {"choice": "a"})
    second = ge_receipt(contract, observation("typesafe", "alias", latency_ms=999), {"choice": "a"})
    assert first["semantic_digest"] == second["semantic_digest"]
    assert first["request_digest"] == second["request_digest"]
    assert first["observation"]["latency_ms"] != second["observation"]["latency_ms"]


def test_experiment_commit_matches_exact_dependency_pin():
    root = Path(__file__).resolve().parents[2]
    project = tomllib.loads((root / "pyproject.toml").read_text())
    locked = tomllib.loads((root / "uv.lock").read_text())
    assert project["tool"]["uv"]["sources"]["generationengine"]["rev"] == GENERATIONENGINE_COMMIT
    ge_package = next(package for package in locked["package"] if package["name"] == "generationengine")
    assert ge_package["source"]["git"].endswith("#" + GENERATIONENGINE_COMMIT)


def test_real_ge_structured_boundary_accepts_occupancy_schemas():
    class FakeProvider:
        def __init__(self):
            self.calls = []

        async def generate(self, call):
            self.calls.append(call)
            if len(self.calls) == 1:
                output = json.loads((FIXTURE / "provider_receipts/proposal.json").read_text())["output"]
            else:
                output = json.loads((FIXTURE / "provider_receipts/structured/occ-f3debc71f994db571810.json").read_text())["output"]
            return TextGenerationResult(text=json.dumps(output), parsed=output,
                                        response_model=call.model, input_tokens=1, output_tokens=1)

    async def exercise():
        provider = FakeProvider()
        client = GenerationClient(text_provider=provider)
        evidence = json.loads((FIXTURE / "stageB.evidence_units.json").read_text())["units"]
        proposed = await propose(client, model="gpt-5.3-codex", evidence_payload=evidence)
        state = {"candidate": json.loads((FIXTURE / "candidate_package.json").read_text())["candidates"][0],
                 "evidence_units": evidence}
        judged = await adjudicate_structured(client, model="gpt-5.3-codex", state=state)
        assert proposed["output"]["candidates"]
        assert judged["output"]["disposition"] == "accept"
        assert len(provider.calls) == 2
        assert all(call.temperature is None for call in provider.calls)

    asyncio.run(exercise())
