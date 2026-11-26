"""
R3: Cross-page continuity and table groups.

Detect and merge EvidenceUnits that span page boundaries (split paragraphs,
tables, lists). Assign table_group_id for retrieval expansion.
"""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass

import blake3

from extraction.schemas import EvidenceUnit


@dataclass
class JoinCandidate:
    """A pair of units to join (last on page N, first on page N+1)."""

    unit_n_id: str
    unit_n1_id: str
    join_type: str  # "paragraph" | "table" | "list"
    structural_path_match: bool


def detect_split_paragraphs(
    units_page_n: list[EvidenceUnit],
    units_page_n1: list[EvidenceUnit],
) -> list[JoinCandidate]:
    """Join only a visibly unfinished paragraph at the actual page boundary."""
    if not units_page_n or not units_page_n1:
        return []
    left, right = units_page_n[-1], units_page_n1[0]
    prose_types = {"prose", "paragraph"}
    if left.unit_type not in prose_types or right.unit_type not in prose_types:
        return []
    before, after = left.text.rstrip(), right.text.lstrip()
    if not before or not re.match(r"[a-z]", after):
        return []
    if re.search(r'[.!?…][”"’\')\]]*$', before):
        return []
    left_path, right_path = left.structural_path, right.structural_path
    same_scope = bool(left_path) and left_path == right_path
    # Contents and index entries use repeating dot leaders and page numbers.
    if any(len(re.findall(r"\.{4,}\s*\d+", text)) >= 5 for text in (before, after)):
        return []
    # A page-level bookmark is a fallback, never a new local section heading.
    fallback_scope = not right_path or bool((right.join_metadata or {}).get("publisher_outline"))
    if not (same_scope or fallback_scope):
        return []
    return [JoinCandidate(left.unit_id, right.unit_id, "paragraph", same_scope)]


def apply_joins(
    all_units: list[EvidenceUnit],
    candidates: list[JoinCandidate],
) -> list[EvidenceUnit]:
    """Apply join candidates: merge text, update page_fingerprints, add anomaly_flags.

    For each candidate, we merge unit_n and unit_n1 into a single unit (keep unit_n,
    append text from unit_n1, add page_fingerprints, mark cross_page_join). Unit_n1
    is removed from the output.
    """
    id_to_unit: dict[str, EvidenceUnit] = {u.unit_id: u for u in all_units}
    units_to_drop: set[str] = set()
    join_map: dict[str, tuple[EvidenceUnit, EvidenceUnit]] = {}  # unit_n_id -> (unit_n, unit_n1)

    join_type_map: dict[str, str] = {}
    for c in candidates:
        u_n = id_to_unit.get(c.unit_n_id)
        u_n1 = id_to_unit.get(c.unit_n1_id)
        if u_n is None or u_n1 is None:
            continue
        join_map[c.unit_n_id] = (u_n, u_n1)
        join_type_map[c.unit_n_id] = c.join_type
        units_to_drop.add(c.unit_n1_id)

    result: list[EvidenceUnit] = []
    for u in all_units:
        if u.unit_id in units_to_drop:
            continue
        if u.unit_id in join_map:
            u_n, u_n1 = join_map[u.unit_id]
            join_type = join_type_map.get(u.unit_id, "paragraph")
            # Merge: append text, expand page_fingerprints
            fp_n = u_n.page_fingerprint
            fp_n1 = u_n1.page_fingerprint
            page_fingerprints = [fp_n, fp_n1]
            merged_text = u_n.text.rstrip() + "\n\n" + u_n1.text.lstrip()
            flags = list(u_n.anomaly_flags)
            if "cross_page_join" not in flags:
                flags.append("cross_page_join")
            source_ids_n = u_n.source_unit_ids or [u_n.unit_id]
            source_ids_n1 = u_n1.source_unit_ids or [u_n1.unit_id]
            combined_source_ids = list(dict.fromkeys(source_ids_n + source_ids_n1))
            merged = EvidenceUnit(
                unit_id=u_n.unit_id,
                unit_type=u_n.unit_type,
                text=merged_text,
                structural_path=u_n.structural_path,
                ordering_key=u_n.ordering_key,
                page_fingerprint=fp_n,
                page_fingerprints=page_fingerprints,
                content_hash=blake3.blake3(merged_text.encode()).hexdigest(),
                source_line_start=u_n.source_line_start,
                source_line_end=u_n1.source_line_end,
                anomaly_flags=flags,
                content_version=u_n.content_version,
                table_group_id=getattr(u_n, "table_group_id", None),
                join_metadata={
                    "join_type": join_type,
                    "merged_unit_id": u_n1.unit_id,
                },
                source_unit_ids=combined_source_ids,
            )
            result.append(merged)
        else:
            result.append(
                EvidenceUnit(
                    unit_id=u.unit_id,
                    unit_type=u.unit_type,
                    text=u.text,
                    structural_path=u.structural_path,
                    ordering_key=u.ordering_key,
                    page_fingerprint=u.page_fingerprint,
                    page_fingerprints=u.page_fingerprints or [u.page_fingerprint],
                    content_hash=u.content_hash,
                    source_line_start=u.source_line_start,
                    source_line_end=u.source_line_end,
                    anomaly_flags=u.anomaly_flags,
                    content_version=u.content_version,
                    table_group_id=u.table_group_id,
                    join_metadata=u.join_metadata,
                    source_unit_ids=u.source_unit_ids or [u.unit_id],
                )
            )
    return result


def assign_table_group_ids(units: list[EvidenceUnit]) -> list[EvidenceUnit]:
    """Assign table_group_id to table units: blake3(header_row_hash + "|" + structural_path_joined).

    Non-table units keep table_group_id=None.
    """
    import re
    result: list[EvidenceUnit] = []
    for u in units:
        if u.unit_type != "table":
            result.append(u)
            continue
        tr_match = re.search(r"<tr[^>]*>.*?</tr>", u.text, re.DOTALL | re.IGNORECASE)
        header_row = tr_match.group(0) if tr_match else u.text[:500]
        path_str = " > ".join(u.structural_path) if u.structural_path else ""
        group_input = blake3.blake3(header_row.encode()).hexdigest() + "|" + path_str
        table_group_id = blake3.blake3(group_input.encode()).hexdigest()
        updated = EvidenceUnit(
            unit_id=u.unit_id,
            unit_type=u.unit_type,
            text=u.text,
            structural_path=u.structural_path,
            ordering_key=u.ordering_key,
            page_fingerprint=u.page_fingerprint,
            page_fingerprints=u.page_fingerprints or [u.page_fingerprint],
            content_hash=u.content_hash,
            source_line_start=u.source_line_start,
            source_line_end=u.source_line_end,
            anomaly_flags=u.anomaly_flags,
            content_version=u.content_version,
            table_group_id=table_group_id,
            join_metadata=u.join_metadata,
            source_unit_ids=u.source_unit_ids or [u.unit_id],
        )
        result.append(updated)
    return result


def run_join_pass(units_by_page: list[list[EvidenceUnit]]) -> list[EvidenceUnit]:
    """Run full join pass: detect candidates across consecutive pages, apply joins, assign table_group_ids."""
    if not units_by_page:
        return []
    flat: list[EvidenceUnit] = []
    for page_units in units_by_page:
        flat.extend(page_units)
    candidates: list[JoinCandidate] = []
    for i in range(len(units_by_page) - 1):
        page_n = units_by_page[i]
        page_n1 = units_by_page[i + 1]
        candidates.extend(detect_split_paragraphs(page_n, page_n1))
        # A shared heading or header cannot establish table or list continuity.
    # The merge format records two source units. Leave overlapping candidates
    # separate rather than silently dropping the third fragment.
    counts = Counter(uid for c in candidates for uid in (c.unit_n_id, c.unit_n1_id))
    candidates = [c for c in candidates if counts[c.unit_n_id] == counts[c.unit_n1_id] == 1]
    joined = apply_joins(flat, candidates)
    return assign_table_group_ids(joined)
