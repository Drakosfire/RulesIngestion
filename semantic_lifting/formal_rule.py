"""Compile one reviewed source-grounded occupancy restriction, deterministically."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


SCHEMA = "rules_formal_artifact_v1"
RULE_ID = "dnd5e-2024-srd-occupancy-end-move"
RULESET_ID = "dnd5e-2024-srd-occupancy-v1"
RESTRICTION_ID = "occ-f3debc71f994db571810"
EXCEPTION_ID = "occ-7154bb6597ce44cc9df4"
LEGACY_FALSE_EXCEPTION_ID = "occ-ac078aa3647a18cb9634"


def canonical_bytes(payload: dict) -> bytes:
    return json.dumps(payload, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":")).encode("utf-8")


def compile_occupancy(fixture: Path, review: dict) -> dict:
    package = json.loads((fixture / "candidate_package.json").read_text())
    gold = json.loads((fixture / "human_gold.json").read_text())["decisions"]
    publication = json.loads((fixture / "dungeonmind_publication_witness.json").read_text())
    source = json.loads((fixture / "source_manifest.json").read_text())
    candidates = {item["candidate_id"]: item for item in package["candidates"]}
    if (gold[RESTRICTION_ID]["disposition"] != "accept"
            or gold[EXCEPTION_ID]["disposition"] != "accept"
            or gold[LEGACY_FALSE_EXCEPTION_ID]["disposition"] != "reject"):
        raise ValueError("Human gold does not support corrected restriction")
    if review.get("disposition") != "approved" or review.get("approved_rule_id") != RULE_ID:
        raise ValueError("Explicit matching review approval required")
    if review.get("source") != "srd-5.2.1-human-gold-and-user-correction":
        raise ValueError("Review authority does not match corrected rule")
    if candidates[RESTRICTION_ID]["evidence_unit_ids"] != [source["evidence_unit_id"]]:
        raise ValueError("Restriction evidence differs from exact source")
    if RESTRICTION_ID not in publication["accepted_candidate_ids"]:
        raise ValueError("Restriction not in published authority")
    if LEGACY_FALSE_EXCEPTION_ID not in publication["excluded_candidate_ids"]:
        raise ValueError("False exception was not excluded")
    artifact = {
        "schema_version": SCHEMA,
        "rule_id": RULE_ID,
        "rule_version": "1",
        "ruleset_id": RULESET_ID,
        "ruleset_version": "srd-5.2.1",
        "statement": "A creature cannot willingly end a move in a space occupied by another creature.",
        "inputs": {
            "action": {"type": "enum", "values": ["end_move_in_cell"]},
            "willing": {"type": "boolean"},
            "destination_occupied_by_other_creature": {"type": "boolean"},
        },
        "decision": {
            "when": {"all": [
                {"input": "action", "equals": "end_move_in_cell"},
                {"input": "willing", "equals": True},
                {"input": "destination_occupied_by_other_creature", "equals": True},
            ]},
            "then": "reject",
            "otherwise": "no_restriction_from_this_rule",
        },
        "exceptions": [],
        "evidence": {
            "evidence_unit_ids": [source["evidence_unit_id"]],
            "source_uri": source["source_url"],
            "source_artifact_id": publication["source_artifact"]["source_artifact_id"],
            "source_revision_id": publication["source_revision"]["source_revision_id"],
            "dungeonmind_space_id": publication["space_id"],
            "dungeonmind_revision_id": publication["published_revision_id"],
            "dungeonmind_assertion_ids": [publication["result_bindings"][f"assertion:{RESTRICTION_ID}"]],
            "evidence_ref_ids": [publication["evidence_ref"]["evidence_ref_id"]],
        },
        "compiler": {"id": "rulesingestion.occupancy.formal.v1",
                     "input_candidate_ids": [RESTRICTION_ID],
                     "graph_closure_used": False},
        "review": review,
    }
    artifact["canonical_sha256"] = sha256(canonical_bytes(artifact)).hexdigest()
    return artifact


def verify_digest(artifact: dict) -> bool:
    digest = artifact.get("canonical_sha256")
    return isinstance(digest, str) and sha256(canonical_bytes({
        key: value for key, value in artifact.items() if key != "canonical_sha256"
    })).hexdigest() == digest
