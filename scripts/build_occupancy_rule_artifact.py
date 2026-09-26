"""Rebuild the corrected reviewed formal artifact from exact checked-in inputs."""

from __future__ import annotations

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from semantic_lifting.formal_rule import compile_occupancy  # noqa: E402


FIXTURE = Path(__file__).resolve().parents[1] / "evals/semantic_lifting/occupancy_v1"


if __name__ == "__main__":
    review = json.loads((FIXTURE / "formal_review.json").read_text())
    artifact = compile_occupancy(FIXTURE, review)
    print(json.dumps(artifact, indent=2, ensure_ascii=False, sort_keys=True))
