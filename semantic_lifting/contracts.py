"""Stable request and receipt contracts for typed Jev decisions."""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from typing import Any, Literal


ADAPTER_VERSION = "jev-adapter-v1"
RECEIPT_SCHEMA_VERSION = "jev-decision-receipt-v1"
QuestionKind = Literal["choice", "score", "noul"]


def canonical_json(value: Any) -> str:
    """Serialize stable JSON; reject values that cannot be replayed."""
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def digest(value: Any) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class DecisionQuestion:
    kind: QuestionKind
    instructions: str
    criteria: dict[str, str | None] | tuple[str, ...] | None = None

    def as_payload(self) -> dict[str, Any]:
        if not self.instructions.strip():
            raise ValueError("A question needs instructions")
        if self.kind == "choice":
            if not isinstance(self.criteria, dict) or len(self.criteria) < 2:
                raise ValueError("A choice needs at least two criteria")
        elif self.kind == "score":
            if not isinstance(self.criteria, tuple) or not self.criteria:
                raise ValueError("A score needs an ordered rubric")
        elif self.kind == "noul":
            if self.criteria is not None:
                raise ValueError("Noul criteria are not supported by this bounded adapter")
        else:
            raise ValueError("Unknown question kind")
        payload: dict[str, Any] = {"type": self.kind, "instructions": self.instructions}
        if self.criteria is not None:
            payload["criteria"] = self.criteria
        return payload


@dataclass(frozen=True)
class DecisionRequest:
    state: str | dict[str, Any] | list[Any]
    questions: dict[str, DecisionQuestion]
    model: str = "typesafe-ai/jev"

    def question_payload(self) -> dict[str, dict[str, Any]]:
        if not self.questions or not all(name.strip() for name in self.questions):
            raise ValueError("A decision needs named questions")
        if not self.model.strip():
            raise ValueError("A decision needs a model")
        return {name: question.as_payload() for name, question in sorted(self.questions.items())}


@dataclass(frozen=True)
class DecisionReceipt:
    input_digest: str
    questions_digest: str
    requested_model: str
    resolved_model: str
    answers: dict[str, dict[str, Any]]
    usage: dict[str, int | None]
    decision_digest: str
    adapter_version: str = ADAPTER_VERSION
    schema_version: str = RECEIPT_SCHEMA_VERSION

    def as_payload(self) -> dict[str, Any]:
        return {
            "adapter_version": self.adapter_version,
            "schema_version": self.schema_version,
            "input_digest": self.input_digest,
            "questions_digest": self.questions_digest,
            "requested_model": self.requested_model,
            "resolved_model": self.resolved_model,
            "answers": self.answers,
            "usage": self.usage,
            "decision_digest": self.decision_digest,
        }
