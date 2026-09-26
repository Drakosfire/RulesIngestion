"""Provider-isolated TypeSafe Jev adapter; no semantic policy lives here."""

from __future__ import annotations

from dataclasses import dataclass
import os
from time import perf_counter
from typing import Any, Literal, Protocol

from typesafe_sdk import (
    Choice,
    Noul,
    Score,
    TypeSafeAPIConnectionError,
    TypeSafeAPIError,
    TypeSafeAPIResponseValidationError,
    TypeSafeAPITimeoutError,
    TypeSafeAuthenticationError,
    TypeSafeClient,
    TypeSafeError,
    TypeSafePermissionDeniedError,
    TypeSafeRateLimitError,
)

from semantic_lifting.contracts import (
    ADAPTER_VERSION,
    RECEIPT_SCHEMA_VERSION,
    DecisionReceipt,
    DecisionRequest,
    digest,
)


Status = Literal[
    "success", "missing_key", "authentication_failure", "rate_limit", "timeout",
    "provider_failure", "invalid_response", "invalid_request",
]
TYPESAFE_GATEWAY_BASE_URL = "https://ai-gateway.vercel.sh/typesafe"


class DecisionClient(Protocol):
    def system_one(self, state: Any, questions: dict[str, Any], *, model: str) -> Any: ...


@dataclass(frozen=True)
class DecisionOutcome:
    status: Status
    receipt: DecisionReceipt | None = None
    # Measurement is deliberately outside the stable receipt/digest.
    elapsed_ms: float | None = None


def _sdk_questions(payload: dict[str, dict[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for name, question in payload.items():
        kind = question["type"]
        if kind == "choice":
            result[name] = Choice(instructions=question["instructions"], criteria=question["criteria"])
        elif kind == "score":
            result[name] = Score(instructions=question["instructions"], criteria=question["criteria"])
        else:
            result[name] = Noul(instructions=question["instructions"])
    return result


def _receipt(request: DecisionRequest, question_payload: dict[str, dict[str, Any]], response: Any) -> DecisionReceipt:
    if not isinstance(response.model, str) or not response.model.strip():
        raise ValueError("Missing resolved model")
    if set(response.answers) != set(question_payload):
        raise ValueError("Answer names do not match questions")
    answers: dict[str, dict[str, Any]] = {}
    for name, question in question_payload.items():
        answer = response.answers[name]
        if answer.type != question["type"]:
            raise ValueError("Answer type does not match question")
        answers[name] = answer.model_dump(mode="json")
    usage = {
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
    }
    stable = {
        "adapter_version": ADAPTER_VERSION,
        "schema_version": RECEIPT_SCHEMA_VERSION,
        "input_digest": digest(request.state),
        "questions_digest": digest(question_payload),
        "requested_model": request.model,
        "resolved_model": response.model,
        "answers": answers,
    }
    # Usage is an observation and may vary on provider replay; keep it in the
    # receipt but out of the semantic decision identity.
    return DecisionReceipt(**stable, usage=usage, decision_digest=digest(stable))


def decide(
    request: DecisionRequest,
    *,
    api_key: str | None = None,
    client: DecisionClient | None = None,
) -> DecisionOutcome:
    """Make one typed judgment; injected clients keep ordinary tests offline."""
    key = api_key if api_key is not None else os.environ.get("TYPESAFE_JEV_API_KEY")
    if not key or not key.strip():
        return DecisionOutcome("missing_key")

    try:
        question_payload = request.question_payload()
        # Validate replay inputs before any provider call.
        digest(request.state)
        digest(question_payload)
        questions = _sdk_questions(question_payload)
    except (TypeError, ValueError):
        return DecisionOutcome("invalid_request")

    started = perf_counter()
    try:
        if client is None:
            # The project key is supplied explicitly. Never mutate the SDK's
            # TYPESAFE_API_KEY environment fallback.
            with TypeSafeClient(api_key=key, base_url=TYPESAFE_GATEWAY_BASE_URL) as owned_client:
                response = owned_client.system_one(request.state, questions, model=request.model)
        else:
            response = client.system_one(request.state, questions, model=request.model)
    except (TypeSafeAuthenticationError, TypeSafePermissionDeniedError):
        return DecisionOutcome("authentication_failure", elapsed_ms=(perf_counter() - started) * 1000)
    except TypeSafeRateLimitError:
        return DecisionOutcome("rate_limit", elapsed_ms=(perf_counter() - started) * 1000)
    except TypeSafeAPITimeoutError:
        return DecisionOutcome("timeout", elapsed_ms=(perf_counter() - started) * 1000)
    except TypeSafeAPIResponseValidationError:
        return DecisionOutcome("invalid_response", elapsed_ms=(perf_counter() - started) * 1000)
    except (TypeSafeAPIError, TypeSafeAPIConnectionError, TypeSafeError):
        return DecisionOutcome("provider_failure", elapsed_ms=(perf_counter() - started) * 1000)

    try:
        receipt = _receipt(request, question_payload, response)
    except (AttributeError, KeyError, TypeError, ValueError):
        return DecisionOutcome("invalid_response", elapsed_ms=(perf_counter() - started) * 1000)
    return DecisionOutcome("success", receipt=receipt, elapsed_ms=(perf_counter() - started) * 1000)
