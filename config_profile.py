"""Ruleset profiling utilities."""

from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from enrichment import extract_text_from_html

MONGODB_URI_ENV = "MONGODB_URI"
DEFAULT_MONGODB_URI = "mongodb://localhost:27017"


def resolve_mongo_uri(mongo_uri: Optional[str] = None) -> str:
    """Resolve MongoDB URI from argument or environment."""
    if mongo_uri:
        return mongo_uri
    return os.getenv(MONGODB_URI_ENV, DEFAULT_MONGODB_URI)


class RulesetProfile(BaseModel):
    """Summary of a chapter's parsed structure."""

    ruleset_id: str
    doc_signature: str
    heading_hierarchy: List[str]
    block_type_distribution: Dict[str, int]
    samples: Optional[List[str]] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


def compute_doc_signature(
    heading_hierarchy: List[str], block_type_distribution: Dict[str, int]
) -> str:
    """Compute stable signature from heading hierarchy and block distribution."""

    payload = {
        "heading_hierarchy": heading_hierarchy,
        "block_type_distribution": block_type_distribution,
    }
    normalized = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def build_ruleset_profile(
    raw_blocks: List[Dict[str, Any]],
    ruleset_id: str,
    sample_size: int = 5,
) -> RulesetProfile:
    heading_hierarchy: List[str] = []
    block_type_distribution: Dict[str, int] = {}
    samples: List[str] = []

    for block in raw_blocks:
        block_type = block.get("block_type", "Unknown")
        block_type_distribution[block_type] = block_type_distribution.get(block_type, 0) + 1

        html = block.get("html", "") if isinstance(block, dict) else ""
        if block_type == "SectionHeader" and html:
            heading_text = extract_text_from_html(html).strip()
            if heading_text:
                heading_hierarchy.append(heading_text)

        if len(samples) < sample_size and html:
            text = extract_text_from_html(html).strip()
            if text:
                samples.append(text)

    doc_signature = compute_doc_signature(heading_hierarchy, block_type_distribution)

    return RulesetProfile(
        ruleset_id=ruleset_id,
        doc_signature=doc_signature,
        heading_hierarchy=heading_hierarchy,
        block_type_distribution=block_type_distribution,
        samples=samples,
    )


def detect_structure_drift(base: RulesetProfile, candidate: RulesetProfile) -> bool:
    """Drift requires both heading hierarchy and block distribution changes."""
    headings_changed = base.heading_hierarchy != candidate.heading_hierarchy
    distribution_changed = base.block_type_distribution != candidate.block_type_distribution
    return headings_changed and distribution_changed
