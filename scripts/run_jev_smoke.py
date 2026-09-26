"""Opt-in live Jev connectivity witness; requires TYPESAFE_JEV_API_KEY."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from semantic_lifting.contracts import DecisionQuestion, DecisionRequest, canonical_json
from semantic_lifting.jev import decide


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="New path for a redacted receipt")
    args = parser.parse_args()

    request = DecisionRequest(
        state={"message": "Please route this simple question to the rules team."},
        questions={
            "route": DecisionQuestion("choice", "Which team should handle this?", {"rules": None, "other": None}),
            "urgency": DecisionQuestion("score", "How urgent is the request?", ("low", "medium", "high")),
            "rules_question": DecisionQuestion("noul", "Is this a rules question?"),
        },
    )
    outcome = decide(request)
    if outcome.status != "success" or outcome.receipt is None:
        print(f"Jev smoke: {outcome.status}")
        return 1

    # The receipt contains digests, typed answers, model identities, and usage;
    # it never contains the request state, API key, or HTTP headers.
    payload = canonical_json(outcome.receipt.as_payload()) + "\n"
    fd = os.open(args.output, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as stream:
        stream.write(payload)
    print(f"Jev smoke: success; receipt={args.output}; decision_digest={outcome.receipt.decision_digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
