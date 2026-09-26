"""One explicit generative proposal pass over the fixed occupancy EvidenceUnit."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field
from generationengine import GenerationClient, TextRequest

from semantic_lifting.contracts import canonical_json, digest, ge_contract, ge_receipt


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
    return ge_contract(operation="generate_structured", provider="openai", model=model,
                       input_digest=digest(evidence_payload), prompt_hash=digest(PROPOSAL_PROMPT),
                       schema_hash=digest(ProposalBatch.model_json_schema()), max_output_tokens=1500)


async def propose(client: GenerationClient, *, model: str, evidence_payload: list[dict]) -> dict:
    """Return a GE-backed experiment receipt; caller validates candidate evidence."""
    contract = proposal_contract(evidence_payload, model)
    result = await client.generate_structured(TextRequest(
        model=model, provider="openai", temperature=None,
        system_prompt=PROPOSAL_PROMPT, user_prompt=canonical_json(evidence_payload),
        json_schema=ProposalBatch.model_json_schema(), schema_name="ProposalBatch",
        max_output_tokens=1500,
    ))
    if result.parsed is None:
        raise ValueError("GE proposal response has no parsed output")
    output = ProposalBatch.model_validate(result.parsed).model_dump(mode="json")
    return ge_receipt(contract, result.observation, output)
