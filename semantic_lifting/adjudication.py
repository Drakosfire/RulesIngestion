"""Comparable structured-output and Jev judgments over fixed candidates."""

from __future__ import annotations

from typing import Literal

from generationengine import (
    BinaryDecisionQuestion,
    ChoiceDecisionQuestion,
    DecisionRequest,
    GenerationClient,
    TextRequest,
)
from pydantic import BaseModel, ConfigDict

from semantic_lifting.contracts import canonical_json, digest, ge_contract, ge_receipt

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
    return ge_contract(operation="generate_structured", provider="openai", model=model,
                       input_digest=digest(state), prompt_hash=digest(STRUCTURED_PROMPT),
                       schema_hash=digest(StructuredJudgment.model_json_schema()),
                       max_output_tokens=800)


async def adjudicate_structured(client: GenerationClient, *, model: str, state: dict) -> dict:
    contract = structured_contract(state, model)
    result = await client.generate_structured(TextRequest(
        model=model, provider="openai", temperature=None,
        system_prompt=STRUCTURED_PROMPT, user_prompt=canonical_json(state),
        json_schema=StructuredJudgment.model_json_schema(), schema_name="StructuredJudgment",
        max_output_tokens=800,
    ))
    if result.parsed is None:
        raise ValueError("GE structured adjudication has no parsed output")
    output = StructuredJudgment.model_validate(result.parsed).model_dump(mode="json")
    return ge_receipt(contract, result.observation, output)


def jev_contract(state: dict, model: str) -> dict:
    questions = _jev_questions()
    return ge_contract(operation="decide", provider="typesafe", model=model,
                       input_digest=digest(state),
                       questions_hash=digest([question.model_dump(mode="json") for question in questions]))


def _jev_questions() -> tuple[ChoiceDecisionQuestion | BinaryDecisionQuestion, ...]:
    return (
        ChoiceDecisionQuestion(name="classification", question=CLASSIFICATION_INSTRUCTION,
                               options=tuple(CLASSIFICATION_CRITERIA),
                               option_descriptions=CLASSIFICATION_CRITERIA),
        BinaryDecisionQuestion(name="evidence_sufficient", question=SUFFICIENCY_INSTRUCTION),
        ChoiceDecisionQuestion(name="disposition", question=DISPOSITION_INSTRUCTION,
                               options=tuple(DISPOSITION_CRITERIA),
                               option_descriptions=DISPOSITION_CRITERIA),
    )


async def adjudicate_jev(client: GenerationClient, *, model: str, state: dict) -> dict:
    contract = jev_contract(state, model)
    result = await client.decide(DecisionRequest(
        state=state, questions=_jev_questions(), provider="typesafe", model=model,
    ))
    answers = result.answers
    sufficient_probability = answers["evidence_sufficient"].probability_true
    if sufficient_probability is None:
        raise ValueError("Jev did not supply binary probability")
    output = {
        "classification": answers["classification"].selected,
        "evidence_sufficient": answers["evidence_sufficient"].value,
        "evidence_sufficient_probability": sufficient_probability,
        "disposition": answers["disposition"].selected,
    }
    return ge_receipt(contract, result.observation, output)
