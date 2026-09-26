"""Bounded, evidence-checked contracts for the corrected occupancy pilot."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json
from typing import Any, Literal

from extraction.schemas import EvidenceUnit, SurfaceAST
from extraction.stage_b import run_stage_b
from semantic_lifting.contracts import digest


CandidateKind = Literal["restriction", "consequence", "exception", "definition", "example"]
Disposition = Literal["accept", "review", "reject", "unresolved"]


@dataclass(frozen=True)
class SemanticCandidate:
    candidate_id: str
    kind: CandidateKind
    subject: str
    predicate: str
    value: str
    evidence_unit_ids: tuple[str, ...]
    origin: str

    @classmethod
    def from_proposal(cls, payload: dict[str, Any], *, evidence_ids: set[str], origin: str) -> "SemanticCandidate":
        kind = payload.get("kind")
        if kind not in {"restriction", "consequence", "exception", "definition", "example"}:
            raise ValueError("Unknown candidate kind")
        fields = {name: str(payload.get(name, "")).strip() for name in ("subject", "predicate", "value")}
        if not all(fields.values()):
            raise ValueError("Candidate has an empty semantic field")
        refs = tuple(sorted(set(payload.get("evidence_unit_ids", []))))
        if not refs or not set(refs) <= evidence_ids:
            raise ValueError("Candidate lacks exact available EvidenceUnit refs")
        stable = {"kind": kind, **fields, "evidence_unit_ids": refs}
        return cls(candidate_id="occ-" + digest(stable)[:20], kind=kind, **fields, evidence_unit_ids=refs, origin=origin)

    def as_payload(self) -> dict[str, Any]:
        return {
            "candidate_id": self.candidate_id,
            "kind": self.kind,
            "subject": self.subject,
            "predicate": self.predicate,
            "value": self.value,
            "evidence_unit_ids": list(self.evidence_unit_ids),
            "origin": self.origin,
        }


def load_exact_evidence(fixture_dir: Path) -> list[EvidenceUnit]:
    """Replay Stage B on the checked-in AST and reject identity drift."""
    ast = SurfaceAST.from_dict(json.loads((fixture_dir / "stageA.surface.ast.json").read_text()))
    stored = json.loads((fixture_dir / "stageB.evidence_units.json").read_text())
    units = run_stage_b(ast, content_version="srd-5.2.1-p14-manual-structural-transcript-v1").units
    if [unit.to_dict() for unit in units] != stored["units"]:
        raise ValueError("EvidenceUnit fixture has drifted from Stage B replay")
    manifest = json.loads((fixture_dir / "source_manifest.json").read_text())
    if len(units) != 1 or units[0].unit_id != manifest["evidence_unit_id"]:
        raise ValueError("Source manifest and evidence identity disagree")
    if units[0].page_fingerprint != manifest["page_fingerprint"]:
        raise ValueError("Source page fingerprint disagrees")
    return units


def compare_with_gold(
    candidates: list[SemanticCandidate],
    gold: dict[str, Disposition],
    treatments: dict[str, dict[str, Disposition]],
) -> dict[str, Any]:
    ids = {candidate.candidate_id for candidate in candidates}
    if set(gold) != ids or any(set(decisions) != ids for decisions in treatments.values()):
        raise ValueError("Every treatment and human gold must cover the same candidates")
    per_candidate = [
        {
            "candidate_id": candidate.candidate_id,
            "human_gold": gold[candidate.candidate_id],
            "treatments": {
                name: {
                    "disposition": decisions[candidate.candidate_id],
                    "correct": decisions[candidate.candidate_id] == gold[candidate.candidate_id],
                }
                for name, decisions in sorted(treatments.items())
            },
        }
        for candidate in candidates
    ]
    rates = {
        name: {
            "correct": sum(item["treatments"][name]["correct"] for item in per_candidate),
            "total": len(candidates),
            "review_or_unresolved": sum(
                decisions[candidate.candidate_id] in {"review", "unresolved"} for candidate in candidates
            ),
        }
        for name, decisions in sorted(treatments.items())
    }
    return {"per_candidate": per_candidate, "rates": rates}
