"""One explicit generative proposal pass over the fixed occupancy EvidenceUnit."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from semantic_lifting.contracts import canonical_json, digest


PROPOSAL_PROMPT = """Read only the supplied authored EvidenceUnit. Propose the smallest set of atomic rule claims that its text actually states. Separate a prohibition from any consequence or exclusion. Do not infer a prone-ally exception or cite model-generated text as evidence. Every candidate must cite the supplied EvidenceUnit ID. Normalize subject, predicate, and value as short strings. Do not publish any candidate as rule truth."""


class ProposedCandidate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    kind: Literal["restriction", "consequence", "exception", "definition", "example"]
    subject: str
    predicate: str
    value: str
    evidence_unit_ids: list[str] = Field(min_length=1)


class ProposalBatch(BaseModel):
    model_config = ConfigDict(extra="forbid")

    candidates: list[ProposedCandidate] = Field(min_length=1, max_length=5)


def proposal_contract(evidence_payload: list[dict], model: str) -> dict:
    return {
        "model": model,
        "prompt_hash": digest(PROPOSAL_PROMPT),
        "schema_hash": digest(ProposalBatch.model_json_schema()),
        "evidence_digest": digest(evidence_payload),
    }


def propose(client: object, *, model: str, evidence_payload: list[dict]) -> dict:
    """Return a redacted provider receipt; the caller validates its candidates."""
    contract = proposal_contract(evidence_payload, model)
    response = client.responses.parse(
        model=model,
        input=[
            {"role": "developer", "content": PROPOSAL_PROMPT},
            {"role": "user", "content": canonical_json(evidence_payload)},
        ],
        text_format=ProposalBatch,
        max_output_tokens=1500,
    )
    if response.status != "completed" or response.output_parsed is None:
        raise ValueError("Proposal response incomplete or unparseable")
    return {
        "contract": contract,
        "request_digest": digest(contract),
        "provider_response_id": response.id,
        "resolved_model": response.model,
        "usage": response.usage.model_dump(mode="json") if response.usage else None,
        "output": response.output_parsed.model_dump(mode="json"),
    }
