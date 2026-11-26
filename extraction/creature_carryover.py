"""Carry a recognized stat-block owner into a leading continuation section."""

import re
from dataclasses import replace

from extraction.schemas import EvidenceUnit
from extraction.unit_identity import compute_evidence_unit_id

SECTIONS = {"Traits", "Actions", "Bonus Actions", "Reactions", "Legendary Actions"}
SIZE = re.compile(r"^(Tiny|Small|Medium|Large|Huge|Gargantuan)\s+\S+")
AC = re.compile(r"\bAC \d+\b")
HP = re.compile(r"\bHP \d+\b")


def continuation_scopes(document: dict) -> dict[int, tuple[str, str]]:
    """Match an adjacent page's initial section with the preceding stat block."""
    pages: dict[int, list[tuple[str, str]]] = {}
    for item in document["texts"]:
        if item["label"] in {"page_header", "page_footer"}:
            continue
        for page in {span["page_no"] for span in item["prov"]}:
            pages.setdefault(page, []).append((item["label"], item["text"].strip()))

    scopes = {}
    for page, current in pages.items():
        label, section = current[0]
        if label != "section_header" or section != "Actions":
            continue
        previous = pages.get(page - 1, [])
        headings = [
            i for i, (kind, title) in enumerate(previous)
            if kind == "section_header" and title not in SECTIONS
        ]
        if not headings:
            continue
        start = headings[-1]
        if ("section_header", section) in previous[start + 1:]:
            continue
        stats = []
        for kind, value in previous[start + 1:]:
            if kind == "section_header":
                break
            stats.append(value)
        if stats and SIZE.match(stats[0]) and AC.search(" ".join(stats)) and HP.search(" ".join(stats)):
            scopes[page] = (previous[start][1], section)
    return scopes


def bind_continuation(
    units: list[EvidenceUnit], page: int, scope: tuple[str, str] | None,
) -> list[EvidenceUnit]:
    """Add owner ancestry without merging or changing the source text."""
    if scope is None:
        return units
    owner, section = scope
    bound = []
    for unit in units:
        if unit.structural_path != [section] or unit.unit_type == "image_ref":
            break
        path = [owner, section]
        bound.append(replace(
            unit,
            structural_path=path,
            unit_id=compute_evidence_unit_id(
                text=unit.text, structural_path=path,
                page_fingerprint=unit.page_fingerprint,
                source_line_start=unit.source_line_start,
                source_line_end=unit.source_line_end, unit_type=unit.unit_type,
            ),
            join_metadata={
                **(unit.join_metadata or {}),
                "creature_carryover": {
                    "owner_pdf_page": page - 1,
                    "original_unit_id": unit.unit_id,
                },
            },
        ))
    return bound + units[len(bound):]
