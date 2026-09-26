from __future__ import annotations

import json

import httpx2
import pytest
from typesafe_sdk import (
    Choice,
    Noul,
    Score,
    SystemOneResponse,
    TypeSafeAPIConnectionError,
    TypeSafeAPIResponseValidationError,
    TypeSafeAPITimeoutError,
    TypeSafeAuthenticationError,
    TypeSafePermissionDeniedError,
    TypeSafeInternalServerError,
    TypeSafeRateLimitError,
)

from semantic_lifting.contracts import DecisionQuestion, DecisionRequest
import semantic_lifting.jev as jev
from semantic_lifting.jev import decide


def request() -> DecisionRequest:
    return DecisionRequest(
        state={"text": "A sample question"},
        questions={
            "category": DecisionQuestion("choice", "Choose a category", {"rules": None, "other": None}),
            "urgency": DecisionQuestion("score", "Rate urgency", ("low", "medium", "high")),
            "is_rule": DecisionQuestion("noul", "Is this about rules?"),
        },
    )


def response() -> SystemOneResponse:
    return SystemOneResponse.model_validate(
        {
            "model": "jev-2026-09-15",
            "usage": {"input_tokens": 42, "output_tokens": 7},
            "answers": {
                "category": {
                    "type": "choice", "choice": "rules", "confidence": 0.8,
                    "probabilities": {"rules": 0.8, "other": 0.2},
                },
                "urgency": {
                    "type": "score", "score": 1.2, "confidence": 0.7,
                    "legend": {0: "low", 1: "medium", 2: "high"},
                    "probabilities": {0: 0.1, 1: 0.6, 2: 0.3},
                },
                "is_rule": {"type": "noul", "noul": 0.9},
            },
        }
    )


class FakeClient:
    def __init__(self, result: object):
        self.result = result
        self.calls: list[tuple[object, object, object]] = []

    def system_one(self, state: object, questions: object, *, model: str) -> object:
        self.calls.append((state, questions, model))
        if isinstance(self.result, BaseException):
            raise self.result
        return self.result


def test_typed_questions_and_stable_redacted_receipt() -> None:
    fake = FakeClient(response())
    first = decide(request(), api_key="private-test-key", client=fake)
    second = decide(request(), api_key="private-test-key", client=fake)

    assert first.status == second.status == "success"
    assert first.receipt is not None and second.receipt is not None
    assert first.receipt.decision_digest == second.receipt.decision_digest
    assert first.receipt.as_payload() == second.receipt.as_payload()
    assert first.receipt.requested_model == "typesafe-ai/jev"
    assert first.receipt.resolved_model == "jev-2026-09-15"
    assert first.receipt.usage == {"input_tokens": 42, "output_tokens": 7}
    assert first.elapsed_ms is not None
    assert "private-test-key" not in json.dumps(first.receipt.as_payload())
    assert "A sample question" not in json.dumps(first.receipt.as_payload())
    sent = fake.calls[0][1]
    assert isinstance(sent["category"], Choice)
    assert isinstance(sent["urgency"], Score)
    assert isinstance(sent["is_rule"], Noul)


def test_missing_key_never_calls_client(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("TYPESAFE_JEV_API_KEY", raising=False)
    fake = FakeClient(response())
    assert decide(request(), client=fake).status == "missing_key"
    assert not fake.calls


def test_project_key_is_passed_explicitly_without_environment_mutation(monkeypatch: pytest.MonkeyPatch) -> None:
    seen: list[str] = []

    class OwnedClient(FakeClient):
        def __init__(self, *, api_key: str, base_url: str):
            seen.append(api_key)
            assert base_url == "https://ai-gateway.vercel.sh/typesafe"
            super().__init__(response())

        def __enter__(self) -> "OwnedClient":
            return self

        def __exit__(self, *_: object) -> None:
            pass

    monkeypatch.setattr(jev, "TypeSafeClient", OwnedClient)
    monkeypatch.setenv("TYPESAFE_API_KEY", "upstream-unrelated-key")
    monkeypatch.setenv("TYPESAFE_JEV_API_KEY", "project-key")
    assert decide(request()).status == "success"
    assert seen == ["project-key"]
    assert jev.os.environ["TYPESAFE_API_KEY"] == "upstream-unrelated-key"


def test_usage_telemetry_does_not_change_decision_digest() -> None:
    first = response()
    second = first.model_copy(update={"usage": first.usage.model_copy(update={"input_tokens": 99})})
    first_receipt = decide(request(), api_key="test", client=FakeClient(first)).receipt
    second_receipt = decide(request(), api_key="test", client=FakeClient(second)).receipt
    assert first_receipt is not None and second_receipt is not None
    assert first_receipt.usage != second_receipt.usage
    assert first_receipt.decision_digest == second_receipt.decision_digest


@pytest.mark.parametrize(
    ("error", "status"),
    [
        (TypeSafeAuthenticationError(401, {}, httpx2.Headers()), "authentication_failure"),
        (TypeSafePermissionDeniedError(403, {}, httpx2.Headers()), "authentication_failure"),
        (TypeSafeRateLimitError(429, {}, httpx2.Headers()), "rate_limit"),
        (TypeSafeAPITimeoutError(1.0), "timeout"),
        (TypeSafeInternalServerError(500, {}, httpx2.Headers()), "provider_failure"),
        (TypeSafeAPIConnectionError("offline"), "provider_failure"),
        (TypeSafeAPIResponseValidationError(200, {}, httpx2.Headers(), "answers"), "invalid_response"),
    ],
)
def test_named_provider_failures(error: Exception, status: str) -> None:
    assert decide(request(), api_key="private-test-key", client=FakeClient(error)).status == status


def test_missing_or_mismatched_answers_fail_closed() -> None:
    partial = response().model_copy(update={"answers": {"is_rule": response().answers["is_rule"]}})
    assert decide(request(), api_key="private-test-key", client=FakeClient(partial)).status == "invalid_response"


def test_non_json_input_fails_before_provider_call() -> None:
    fake = FakeClient(response())
    bad = DecisionRequest(state={"bad": object()}, questions=request().questions)
    assert decide(bad, api_key="private-test-key", client=fake).status == "invalid_request"
    assert not fake.calls
