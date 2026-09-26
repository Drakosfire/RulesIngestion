"""Stable RulesIngestion experiment digests and GE execution receipts."""

from __future__ import annotations

from hashlib import sha256
import json
from typing import Any

from generationengine import InferenceObservation


GENERATIONENGINE_COMMIT = "cf5bee24fa0a469a80c91c5e48992726eab8aa8d"
GE_RECEIPT_SCHEMA_VERSION = "semantic-ge-receipt-v2"


def canonical_json(value: Any) -> str:
    """Serialize stable JSON; reject values that cannot be replayed."""
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def digest(value: Any) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


def ge_contract(*, operation: str, provider: str, model: str, input_digest: str,
                prompt_hash: str | None = None, schema_hash: str | None = None,
                questions_hash: str | None = None, max_output_tokens: int | None = None) -> dict[str, Any]:
    """Caller-owned replay identity; transport telemetry never changes it."""
    return {
        "execution_contract_version": GE_RECEIPT_SCHEMA_VERSION,
        "generationengine_commit": GENERATIONENGINE_COMMIT,
        "operation": operation,
        "requested_provider": provider,
        "requested_model": model,
        "requested_profile": None,
        "input_digest": input_digest,
        "prompt_hash": prompt_hash,
        "schema_hash": schema_hash,
        "questions_hash": questions_hash,
        "max_output_tokens": max_output_tokens,
    }


def ge_receipt(contract: dict[str, Any], observation: InferenceObservation,
               output: dict[str, Any]) -> dict[str, Any]:
    """Persist GE call truth while excluding volatile telemetry from semantic identity."""
    if contract["generationengine_commit"] != GENERATIONENGINE_COMMIT:
        raise ValueError("GenerationEngine contract commit mismatch")
    receipt = {
        "schema_version": GE_RECEIPT_SCHEMA_VERSION,
        "contract": contract,
        "request_digest": digest(contract),
        "generationengine_commit": GENERATIONENGINE_COMMIT,
        "operation": contract["operation"],
        "observation": observation.model_dump(mode="json"),
        "output": output,
        "semantic_digest": digest({"contract": contract, "output": output}),
    }
    receipt["receipt_digest"] = digest(receipt)
    return receipt


def verify_ge_receipt(receipt: dict[str, Any], contract: dict[str, Any]) -> None:
    if (receipt.get("schema_version") != GE_RECEIPT_SCHEMA_VERSION
            or receipt.get("contract") != contract
            or receipt.get("request_digest") != digest(contract)
            or receipt.get("generationengine_commit") != GENERATIONENGINE_COMMIT
            or receipt.get("operation") != contract["operation"]
            or not isinstance(receipt.get("output"), dict)
            or receipt.get("semantic_digest") != digest({"contract": contract,
                                                           "output": receipt.get("output")})
            or receipt.get("receipt_digest") != digest({k: v for k, v in receipt.items()
                                                       if k != "receipt_digest"})):
        raise ValueError("GenerationEngine receipt contract drift")
    observed = receipt.get("observation")
    if not isinstance(observed, dict) or observed.get("provider") != contract["requested_provider"]:
        raise ValueError("GenerationEngine receipt provider drift")
    if observed.get("requested_model") != contract["requested_model"]:
        raise ValueError("GenerationEngine receipt model drift")
