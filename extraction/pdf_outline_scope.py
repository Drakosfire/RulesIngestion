"""Fill missing page scope from publisher PDF bookmarks."""

from dataclasses import replace
from itertools import takewhile

from extraction.schemas import EvidenceUnit
from extraction.unit_identity import compute_evidence_unit_id


def outline_scope(entries: list[tuple[int, str, int]]) -> dict[int, list[str]]:
    """Return supported heading paths keyed by one-based PDF page."""
    usable = [(depth, title.strip(), page) for depth, title, page in entries
              if page > 0 and depth > 0 and title.strip()]
    stack: list[tuple[int, str]] = []
    paths: dict[int, list[str]] = {}
    for depth, title, page in usable:
        while stack and stack[-1][0] >= depth:
            stack.pop()
        stack.append((depth, title))
        path = [name for _, name in stack]
        if page in paths:
            # A bookmark gives a page destination, not a unit boundary.
            path = [a for a, _ in takewhile(lambda pair: pair[0] == pair[1], zip(paths[page], path))]
        paths[page] = path
    return paths


def fill_missing_scope(
    units: list[EvidenceUnit], page: int, destinations: dict[int, list[str]],
) -> list[EvidenceUnit]:
    """Supply publisher scope only to units without their own heading path."""
    prior = max((n for n in destinations if n <= page), default=None)
    path = destinations.get(prior, [])
    if not path:
        return units
    return [
        unit if unit.structural_path else replace(
            unit,
            structural_path=list(path),
            unit_id=compute_evidence_unit_id(
                text=unit.text, structural_path=path,
                page_fingerprint=unit.page_fingerprint,
                source_line_start=unit.source_line_start,
                source_line_end=unit.source_line_end, unit_type=unit.unit_type,
            ),
            anomaly_flags=[f for f in unit.anomaly_flags if f != "no_heading_parent"],
            join_metadata={
                **(unit.join_metadata or {}),
                "publisher_outline": {"destination_pdf_page": prior, "original_unit_id": unit.unit_id},
            },
        )
        for unit in units
    ]
