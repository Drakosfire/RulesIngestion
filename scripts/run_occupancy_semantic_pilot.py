"""Replay or execute the bounded occupancy comparison through GenerationEngine."""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
from collections.abc import Awaitable, Callable
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from generationengine import GenerationClient

from semantic_lifting.adjudication import (
    adjudicate_jev,
    adjudicate_structured,
    jev_contract,
    judgment_state,
    structured_contract,
)
from semantic_lifting.contracts import (
    GENERATIONENGINE_COMMIT,
    canonical_json,
    digest,
    verify_ge_receipt,
)
from semantic_lifting.occupancy import (
    SemanticCandidate,
    compare_with_gold,
    load_exact_evidence,
)
from semantic_lifting.proposal import proposal_contract, propose

DEFAULT_FIXTURE = Path(__file__).resolve().parents[1] / "evals/semantic_lifting/occupancy_v1"
GE_RUN_DIR = "generationengine_v2"


def _save(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


async def _receipt(path: Path, contract: dict, make: Callable[[], Awaitable[dict]] | None) -> dict:
    if path.exists():
        value = json.loads(path.read_text())
    elif make is not None:
        value = await make()
        verify_ge_receipt(value, contract)
        _save(path, value)
    else:
        raise FileNotFoundError(f"Missing GE provider receipt: {path}")
    verify_ge_receipt(value, contract)
    return value


async def run(fixture: Path, *, proposal_model: str, adjudicator_model: str,
              jev_model: str, live: bool, client: GenerationClient | None = None) -> dict:
    """Adjudicate the frozen human-gold package; record proposal differences separately."""
    evidence = [unit.to_dict() for unit in load_exact_evidence(fixture)]
    evidence_ids = {unit["unit_id"] for unit in evidence}
    package = json.loads((fixture / "candidate_package.json").read_text())
    if package["source_evidence_unit_ids"] != sorted(evidence_ids):
        raise ValueError("Frozen candidate package evidence identity drift")
    candidates = [
        SemanticCandidate.from_proposal(payload, evidence_ids=evidence_ids,
                                        origin=payload["origin"])
        for payload in package["candidates"]
    ]
    if [candidate.as_payload() for candidate in candidates] != package["candidates"]:
        raise ValueError("Frozen candidate package identity drift")
    gold_document = json.loads((fixture / "human_gold.json").read_text())
    gold = gold_document["decisions"]
    if set(gold) != {candidate.candidate_id for candidate in candidates}:
        raise ValueError("Human gold does not cover the frozen candidate package")

    output_dir = fixture / GE_RUN_DIR
    owned = client is None and live
    if owned:
        client = GenerationClient.from_env()
    try:
        proposal_spec = proposal_contract(evidence, proposal_model)
        proposal_receipt = await _receipt(
            output_dir / "provider_receipts/proposal.json", proposal_spec,
            (lambda: propose(client, model=proposal_model, evidence_payload=evidence)) if live else None,
        )
        proposed = [SemanticCandidate.from_proposal(payload, evidence_ids=evidence_ids,
                                                    origin=f"{proposal_model}-proposal")
                    for payload in proposal_receipt["output"]["candidates"]]
        frozen_proposed = [candidate for candidate in candidates if candidate.origin.endswith("-proposal")]
        proposal_delta = {
            "frozen_candidate_ids": [candidate.candidate_id for candidate in frozen_proposed],
            "ge_candidate_ids": [candidate.candidate_id for candidate in proposed],
            "same_candidate_ids": {c.candidate_id for c in frozen_proposed}
                                  == {c.candidate_id for c in proposed},
            "same_evidence_refs": all(set(c.evidence_unit_ids) <= evidence_ids for c in proposed),
        }

        outputs: dict[str, dict[str, dict]] = {"structured_llm": {}, "jev": {}}
        semantic_digests: dict[str, dict[str, str]] = {"structured_llm": {}, "jev": {}}
        model_identities: dict[str, set[str]] = {"structured_llm": set(), "jev": set()}
        routes: dict[str, set[str | None]] = {"structured_llm": set(), "jev": set()}
        for candidate in candidates:
            state = judgment_state(candidate.as_payload(), evidence)
            structured = await _receipt(
                output_dir / "provider_receipts/structured" / f"{candidate.candidate_id}.json",
                structured_contract(state, adjudicator_model),
                (lambda state=state: adjudicate_structured(client, model=adjudicator_model,
                                                           state=state)) if live else None,
            )
            jev = await _receipt(
                output_dir / "provider_receipts/jev" / f"{candidate.candidate_id}.json",
                jev_contract(state, jev_model),
                (lambda state=state: adjudicate_jev(client, model=jev_model,
                                                    state=state)) if live else None,
            )
            for name, receipt in (("structured_llm", structured), ("jev", jev)):
                outputs[name][candidate.candidate_id] = receipt["output"]
                semantic_digests[name][candidate.candidate_id] = receipt["semantic_digest"]
                model_identities[name].add(receipt["observation"]["response_model"] or "unknown")
                routes[name].add(receipt["observation"]["provider_transport"])
    finally:
        if owned and client is not None:
            await client.aclose()

    dispositions = {
        name: {candidate_id: value["disposition"] for candidate_id, value in decisions.items()}
        for name, decisions in outputs.items()
    }
    comparison = compare_with_gold(
        candidates, {candidate_id: decision["disposition"] for candidate_id, decision in gold.items()},
        dispositions,
    )
    field_correctness = {
        name: {field: sum(output[field] == gold[candidate_id][field]
                          for candidate_id, output in decisions.items())
               for field in ("classification", "evidence_sufficient", "disposition")}
        for name, decisions in outputs.items()
    }
    disagreements = [
        {"candidate_id": candidate.candidate_id, "human_gold": gold[candidate.candidate_id],
         "structured_llm": outputs["structured_llm"][candidate.candidate_id],
         "jev": outputs["jev"][candidate.candidate_id]}
        for candidate in candidates
        if any(outputs[name][candidate.candidate_id][field] != gold[candidate.candidate_id][field]
               for name in outputs for field in ("classification", "evidence_sufficient", "disposition"))
        or outputs["structured_llm"][candidate.candidate_id]["disposition"]
        != outputs["jev"][candidate.candidate_id]["disposition"]
    ]
    stable = {
        "schema_version": "occupancy-semantic-pilot-summary-ge-v2",
        "generationengine_commit": GENERATIONENGINE_COMMIT,
        "candidate_package_digest": digest(package),
        "human_gold_digest": digest(gold_document),
        "source_evidence_unit_ids": sorted(evidence_ids),
        "candidate_evidence_refs": {candidate.candidate_id: list(candidate.evidence_unit_ids)
                                    for candidate in candidates},
        "proposal_request_digest": proposal_receipt["request_digest"],
        "proposal_delta": proposal_delta,
        "provider_routes": {name: sorted(route or "unknown" for route in values)
                            for name, values in routes.items()},
        "treatment_models": {name: sorted(values) for name, values in model_identities.items()},
        "per_decision": comparison["per_candidate"],
        "rates": comparison["rates"],
        "field_correctness": field_correctness,
        "receipt_semantic_digests": semantic_digests,
    }
    summary = {**stable, "run_digest": digest(stable), "disagreements": disagreements}
    if live:
        _save(output_dir / "experiment_summary.json", summary)
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--proposal-model", default="gpt-5.3-codex")
    parser.add_argument("--adjudicator-model", default="gpt-5.3-codex")
    parser.add_argument("--jev-model", default="typesafe-ai/jev")
    parser.add_argument("--live", action="store_true", help="Call GE providers for missing receipts")
    args = parser.parse_args()
    summary = asyncio.run(run(args.fixture, proposal_model=args.proposal_model,
                              adjudicator_model=args.adjudicator_model,
                              jev_model=args.jev_model, live=args.live))
    print(canonical_json({"run_digest": summary["run_digest"], "rates": summary["rates"],
                          "proposal_delta": summary["proposal_delta"]}))


if __name__ == "__main__":
    main()
