"""Replay or execute the bounded, evidence-first 2024 occupancy comparison."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from openai import OpenAI

from semantic_lifting.adjudication import (
    adjudicate_jev, adjudicate_structured, jev_contract, judgment_state, structured_contract,
)
from semantic_lifting.contracts import canonical_json, digest
from semantic_lifting.occupancy import SemanticCandidate, compare_with_gold, load_exact_evidence
from semantic_lifting.proposal import proposal_contract, propose


DEFAULT_FIXTURE = Path(__file__).resolve().parents[1] / "evals/semantic_lifting/occupancy_v1"
PROBE = {
    "kind": "exception",
    "subject": "prone ally",
    "predicate": "permits willingly ending a move in the ally’s occupied space",
    "value": "allowed",
}


def _save(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _receipt(path: Path, expected_digest: str, make: object | None) -> dict:
    if path.exists():
        value = json.loads(path.read_text())
    elif make is not None:
        value = make()
        _save(path, value)
    else:
        raise FileNotFoundError(f"Missing provider receipt: {path}")
    if value.get("request_digest") != expected_digest:
        raise ValueError(f"Provider receipt contract drift: {path}")
    return value


def run(fixture: Path, *, proposal_model: str, adjudicator_model: str, jev_model: str, live: bool) -> dict:
    evidence = [unit.to_dict() for unit in load_exact_evidence(fixture)]
    evidence_ids = {unit["unit_id"] for unit in evidence}
    proposal_path = fixture / "provider_receipts/proposal.json"
    proposal_digest = digest(proposal_contract(evidence, proposal_model))

    openai_client = None
    if live:
        key = os.environ.get("OPENAI_API_KEY")
        if not key:
            raise ValueError("OPENAI_API_KEY is required for live model calls")
        openai_client = OpenAI(api_key=key)
    proposal_receipt = _receipt(
        proposal_path, proposal_digest,
        (lambda: propose(openai_client, model=proposal_model, evidence_payload=evidence)) if live else None,
    )

    candidates = [
        SemanticCandidate.from_proposal(payload, evidence_ids=evidence_ids, origin=f"{proposal_model}-proposal")
        for payload in proposal_receipt["output"]["candidates"]
    ]
    candidates.append(SemanticCandidate.from_proposal(
        {**PROBE, "evidence_unit_ids": sorted(evidence_ids)},
        evidence_ids=evidence_ids, origin="legacy-v0-negative-control",
    ))
    package = {
        "schema_version": "occupancy-semantic-candidates-v1",
        "source_evidence_unit_ids": sorted(evidence_ids),
        "proposal_request_digest": proposal_receipt["request_digest"],
        "candidates": [candidate.as_payload() for candidate in candidates],
    }
    package_path = fixture / "candidate_package.json"
    if package_path.exists() and json.loads(package_path.read_text()) != package:
        raise ValueError("Frozen candidate package differs from the proposal receipt")
    _save(package_path, package)

    gold_document = json.loads((fixture / "human_gold.json").read_text())
    gold = gold_document["decisions"]
    if set(gold) != {candidate.candidate_id for candidate in candidates}:
        raise ValueError("Human gold does not cover the exact frozen candidate package")

    outputs: dict[str, dict[str, dict]] = {"structured_llm": {}, "jev": {}}
    receipt_digests: dict[str, dict[str, str]] = {"structured_llm": {}, "jev": {}}
    model_identities: dict[str, set[str]] = {"structured_llm": set(), "jev": set()}
    for candidate in candidates:
        state = judgment_state(candidate.as_payload(), evidence)
        structured_request_digest = digest(structured_contract(state, adjudicator_model))
        structured_path = fixture / "provider_receipts/structured" / f"{candidate.candidate_id}.json"
        structured = _receipt(
            structured_path, structured_request_digest,
            (lambda state=state: adjudicate_structured(openai_client, model=adjudicator_model, state=state)) if live else None,
        )
        outputs["structured_llm"][candidate.candidate_id] = structured["output"]
        receipt_digests["structured_llm"][candidate.candidate_id] = digest(structured)
        model_identities["structured_llm"].add(structured["resolved_model"])

        jev_request_digest = digest(jev_contract(state, jev_model))
        jev_path = fixture / "provider_receipts/jev" / f"{candidate.candidate_id}.json"
        jev = _receipt(
            jev_path, jev_request_digest,
            (lambda state=state: adjudicate_jev(
                api_key=os.environ.get("TYPESAFE_JEV_API_KEY", ""), model=jev_model, state=state
            )) if live else None,
        )
        outputs["jev"][candidate.candidate_id] = jev["output"]
        receipt_digests["jev"][candidate.candidate_id] = digest(jev)
        model_identities["jev"].add(jev["provider_receipt"]["resolved_model"])

    dispositions = {
        treatment: {candidate_id: output["disposition"] for candidate_id, output in decisions.items()}
        for treatment, decisions in outputs.items()
    }
    comparison = compare_with_gold(
        candidates,
        {candidate_id: decision["disposition"] for candidate_id, decision in gold.items()},
        dispositions,
    )
    field_correctness = {
        treatment: {
            field: sum(
                output[field] == gold[candidate_id][field]
                for candidate_id, output in decisions.items()
            )
            for field in ("classification", "evidence_sufficient", "disposition")
        }
        for treatment, decisions in outputs.items()
    }
    disagreements = [
        {
            "candidate_id": candidate.candidate_id,
            "human_gold": gold[candidate.candidate_id],
            "structured_llm": outputs["structured_llm"][candidate.candidate_id],
            "jev": outputs["jev"][candidate.candidate_id],
        }
        for candidate in candidates
        if any(outputs[t][candidate.candidate_id]["disposition"] != gold[candidate.candidate_id]["disposition"] for t in outputs)
        or outputs["structured_llm"][candidate.candidate_id]["disposition"] != outputs["jev"][candidate.candidate_id]["disposition"]
    ]
    stable = {
        "schema_version": "occupancy-semantic-pilot-summary-v1",
        "candidate_package_digest": digest(package),
        "human_gold_digest": digest(gold_document),
        "proposal_request_digest": proposal_digest,
        "source_evidence_unit_ids": sorted(evidence_ids),
        "proposal_model": proposal_receipt["resolved_model"],
        "treatment_models": {name: sorted(values) for name, values in model_identities.items()},
        "per_decision": comparison["per_candidate"],
        "rates": comparison["rates"],
        "field_correctness": field_correctness,
    }
    summary = {
        **stable,
        "run_digest": digest(stable),
        "disagreements": disagreements,
        "provider_receipt_digests": receipt_digests,
    }
    _save(fixture / "experiment_summary.json", summary)
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--proposal-model", default="gpt-5.3-codex")
    parser.add_argument("--adjudicator-model", default="gpt-5.3-codex")
    parser.add_argument("--jev-model", default="typesafe-ai/jev")
    parser.add_argument("--live", action="store_true", help="Call providers for missing receipts")
    args = parser.parse_args()
    summary = run(args.fixture, proposal_model=args.proposal_model,
                  adjudicator_model=args.adjudicator_model, jev_model=args.jev_model, live=args.live)
    print(canonical_json({"run_digest": summary["run_digest"], "rates": summary["rates"]}))


if __name__ == "__main__":
    main()
