"""Comparable structured-output and Jev judgments over fixed candidates."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict

from semantic_lifting.contracts import DecisionQuestion, DecisionRequest, canonical_json, digest
from semantic_lifting.jev import decide


CLASSIFICATION_CRITERIA = {
    "restriction": "A prohibition or default rule about what cannot be done.",
    "consequence": "An outcome that follows if a condition occurs.",
    "exception": "An explicit exclusion or override to a named rule or consequence.",
    "definition": "A term definition without a behavioral rule.",
    "example": "An illustrative case rather than a rule.",
    "unsupported": "The candidate's claimed relationship is not established by the cited evidence.",
}
DISPOSITION_CRITERIA = {
    "accept": "Fully supported as worded, including conditions and exclusions.",
    "review": "Partly supported but a material qualifier or relationship must be reviewed.",
    "reject": "Contradicted or unsupported by the exact evidence.",
    "unresolved": "The evidence is insufficient to decide either way.",
}
CLASSIFICATION_INSTRUCTION = "Classify the candidate's claimed semantic relationship against the exact authored evidence."
SUFFICIENCY_INSTRUCTION = "Does the exact authored EvidenceUnit fully support the candidate as worded, including all conditions and exclusions?"
DISPOSITION_INSTRUCTION = "Choose accept, review, reject, or unresolved for this candidate based only on exact authored evidence. Do not treat confidence as source truth."


class StructuredJudgment(BaseModel):
    model_config = ConfigDict(extra="forbid")

    classification: Literal["restriction", "consequence", "exception", "definition", "example", "unsupported"]
    evidence_sufficient: bool
    disposition: Literal["accept", "review", "reject", "unresolved"]
    rationale: str


STRUCTURED_PROMPT = (
    "Judge one candidate only against the supplied exact authored EvidenceUnit. "
    + CLASSIFICATION_INSTRUCTION + " Classification criteria: " + canonical_json(CLASSIFICATION_CRITERIA)
    + " " + SUFFICIENCY_INSTRUCTION + " " + DISPOSITION_INSTRUCTION
    + " Disposition criteria: " + canonical_json(DISPOSITION_CRITERIA)
    + " Return the required JSON object."
)


def judgment_state(candidate: dict, evidence: list[dict]) -> dict:
    return {"candidate": candidate, "evidence_units": evidence}


def structured_contract(state: dict, model: str) -> dict:
    return {
        "model": model,
        "state_digest": digest(state),
        "prompt_hash": digest(STRUCTURED_PROMPT),
        "schema_hash": digest(StructuredJudgment.model_json_schema()),
    }


def adjudicate_structured(client: object, *, model: str, state: dict) -> dict:
    contract = structured_contract(state, model)
    response = client.responses.parse(
        model=model,
        input=[
            {"role": "developer", "content": STRUCTURED_PROMPT},
            {"role": "user", "content": canonical_json(state)},
        ],
        text_format=StructuredJudgment,
        max_output_tokens=800,
    )
    if response.status != "completed" or response.output_parsed is None:
        raise ValueError("Structured adjudication incomplete or unparseable")
    return {
        "contract": contract,
        "request_digest": digest(contract),
        "provider_response_id": response.id,
        "resolved_model": response.model,
        "usage": response.usage.model_dump(mode="json") if response.usage else None,
        "output": response.output_parsed.model_dump(mode="json"),
    }


def jev_contract(state: dict, model: str) -> dict:
    questions = _jev_questions()
    return {
        "model": model,
        "state_digest": digest(state),
        "questions_digest": digest({name: question.as_payload() for name, question in sorted(questions.items())}),
    }


def _jev_questions() -> dict[str, DecisionQuestion]:
    return {
        "classification": DecisionQuestion("choice", CLASSIFICATION_INSTRUCTION, CLASSIFICATION_CRITERIA),
        "evidence_sufficient": DecisionQuestion("noul", SUFFICIENCY_INSTRUCTION),
        "disposition": DecisionQuestion("choice", DISPOSITION_INSTRUCTION, DISPOSITION_CRITERIA),
    }


def adjudicate_jev(*, api_key: str, model: str, state: dict) -> dict:
    contract = jev_contract(state, model)
    outcome = decide(DecisionRequest(state=state, questions=_jev_questions(), model=model), api_key=api_key)
    if outcome.status != "success" or outcome.receipt is None:
        raise RuntimeError(f"Jev adjudication failed: {outcome.status}")
    answers = outcome.receipt.answers
    sufficient_probability = float(answers["evidence_sufficient"]["noul"])
    return {
        "contract": contract,
        "request_digest": digest(contract),
        "provider_receipt": outcome.receipt.as_payload(),
        "output": {
            "classification": answers["classification"]["choice"],
            "evidence_sufficient": sufficient_probability >= 0.5,
            "evidence_sufficient_probability": sufficient_probability,
            "disposition": answers["disposition"]["choice"],
        },
    }
