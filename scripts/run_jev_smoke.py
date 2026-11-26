"""Opt-in live Jev connectivity witness through GenerationEngine."""

from __future__ import annotations

import argparse
import asyncio
import os
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from generationengine import (
    BinaryDecisionQuestion, ChoiceDecisionQuestion, DecisionRequest,
    GenerationClient, GenerationEngineError, ScoreDecisionQuestion,
)
from semantic_lifting.contracts import canonical_json, digest, ge_contract, ge_receipt


async def smoke(output: Path) -> int:
    state = {"message": "Please route this simple question to the rules team."}
    questions = (
        ChoiceDecisionQuestion(name="route", question="Which team should handle this?",
                               options=("rules", "other")),
        ScoreDecisionQuestion(name="urgency", question="How urgent is the request?",
                              levels=("low", "medium", "high")),
        BinaryDecisionQuestion(name="rules_question", question="Is this a rules question?"),
    )
    request = DecisionRequest(state=state, questions=questions,
                              provider="typesafe", model="typesafe-ai/jev",
                              max_transport_retries=0)
    client = GenerationClient.from_env()
    try:
        result = await client.decide(request)
    except GenerationEngineError as exc:
        print(f"Jev smoke: {exc.failure.code.value}")
        return 1
    finally:
        await client.aclose()
    contract = ge_contract(operation="decide", provider="typesafe", model=request.model,
                           input_digest=digest(state),
                           questions_hash=digest([q.model_dump(mode="json") for q in questions]))
    receipt = ge_receipt(contract, result.observation,
                         {name: answer.model_dump(mode="json") for name, answer in result.answers.items()})
    fd = os.open(output, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as stream:
        stream.write(canonical_json(receipt) + "\n")
    print(f"Jev smoke: success; receipt={output}; decision_digest={receipt['semantic_digest']}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="New path for a redacted receipt")
    args = parser.parse_args()
    return asyncio.run(smoke(args.output))


if __name__ == "__main__":
    raise SystemExit(main())
