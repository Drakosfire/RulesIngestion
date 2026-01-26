from __future__ import annotations

from collections import Counter
import re
from typing import Any, Dict, List, Optional, Set, Tuple

from scripts.discover_deterministic_edges_constants import (
    CUE_KEYWORDS,
    REFERENCE_PATTERNS,
    STRICT_RELATIONS,
)
from scripts.discover_deterministic_edges_text import (
    _extract_page_cue_title_from_match,
    _normalize_label,
    _normalize_title,
)


def _count_keywords(text: str, keyword_counts: Counter) -> None:
    lowered = text.lower()
    for keyword in CUE_KEYWORDS:
        if keyword in lowered:
            keyword_counts[keyword] += lowered.count(keyword)


def _score_page_match(
    normalized_cue: str,
    cue_title: str,
    block_type: str,
    heading_text: Optional[str],
    section_tail: Optional[str],
    first_line: Optional[str],
) -> Tuple[int, int, int]:
    if not normalized_cue:
        return 0, 0, 0
    block_bonus = 1 if block_type in {"Title", "SectionHeader"} else 0
    type_bonus = 2 if block_type == "Table" else 1 if block_type == "TableCell" else 0
    cue_lower = (cue_title or "").lower()
    heading_norm = _normalize_title(heading_text) if heading_text else ""
    section_norm = _normalize_title(section_tail) if section_tail else ""
    first_line_norm = _normalize_title(first_line) if first_line else ""
    score = 0
    if heading_norm == normalized_cue:
        score = max(score, 3)
    if section_norm == normalized_cue:
        score = max(score, 3)
    if first_line_norm == normalized_cue:
        score = max(score, 3)
    if heading_norm.startswith(normalized_cue):
        score = max(score, 2)
    if section_norm.startswith(normalized_cue):
        score = max(score, 2)
    if first_line_norm.startswith(normalized_cue):
        score = max(score, 2)
    if "adjustments" in cue_lower and normalized_cue == "adjustments":
        if heading_norm.endswith("adjustments") or section_norm.endswith("adjustments"):
            score = max(score, 2)
            block_bonus = max(block_bonus, 1)
    if "table" in cue_lower:
        if block_type in {"Table", "TableCell"}:
            score = max(score, 2)
        if "table" in heading_norm or "table" in section_norm:
            score = max(score, 2)
    return score, block_bonus, type_bonus


def _select_page_targets(
    page_label: str,
    page_text_index: Dict[str, List[Tuple[str, Optional[str], Optional[str], Optional[str]]]],
    cue_title: str,
) -> List[str]:
    normalized_page = page_label
    if normalized_page.startswith("page "):
        normalized_page = normalized_page.replace("page ", "", 1).strip()
    candidates = page_text_index.get(page_label, []) or page_text_index.get(
        normalized_page, []
    )
    if not candidates:
        return []
    normalized_cue = _normalize_title(cue_title)
    cue_lower = (cue_title or "").lower()
    if "table" in cue_lower:
        filtered = [
            entry
            for entry in candidates
            if entry[1] in {"Table"}
            or (entry[2] and "table" in entry[2].lower())
            or (entry[3] and "table" in entry[3].lower())
        ]
        if filtered:
            candidates = filtered
    if "adjustments" in cue_lower:
        filtered = [
            entry
            for entry in candidates
            if (entry[2] and entry[2].lower().endswith("adjustments"))
            or (entry[3] and entry[3].lower().endswith("adjustments"))
        ]
        if filtered:
            candidates = filtered
    matches: List[Tuple[int, int, int, str]] = []
    for chunk_id, block_type, heading_text, section_tail, first_line in candidates:
        score, block_bonus, type_bonus = _score_page_match(
            normalized_cue,
            cue_title,
            block_type or "",
            heading_text,
            section_tail,
            first_line,
        )
        if score > 0:
            matches.append((score, block_bonus, type_bonus, chunk_id))
    if not matches:
        return []
    best_score = max(score for score, _, _, _ in matches)
    scored = [entry for entry in matches if entry[0] == best_score]
    best_bonus = max(bonus for _, bonus, _, _ in scored)
    scored = [entry for entry in scored if entry[1] == best_bonus]
    best_type_bonus = max(type_bonus for _, _, type_bonus, _ in scored)
    best = [chunk_id for _, _, type_bonus, chunk_id in scored if type_bonus == best_type_bonus]
    return sorted(set(best))


def _score_page_candidate(
    normalized_cue: str,
    cue_title: str,
    block_type: str,
    heading_text: Optional[str],
    section_tail: Optional[str],
    first_line: Optional[str],
) -> Tuple[int, int]:
    score, block_bonus, _ = _score_page_match(
        normalized_cue,
        cue_title,
        block_type,
        heading_text,
        section_tail,
        first_line,
    )
    return score, block_bonus


def _build_page_reference_debug(
    candidates: List[Dict[str, Any]],
    page_text_index: Dict[str, List[Tuple[str, Optional[str], Optional[str], Optional[str]]]],
    max_samples: int = 50,
    top_k: int = 5,
) -> Dict[str, Any]:
    samples: List[Dict[str, Any]] = []
    skipped = 0
    for candidate in candidates:
        if candidate.get("relation") != "references_page":
            continue
        if int(candidate.get("resolution_count", 0)) == 1:
            continue
        page_label = _normalize_label(candidate.get("parsed_target", {}).get("label", ""))
        if not page_label:
            skipped += 1
            continue
        cue_title = candidate.get("cue_title", "") or ""
        normalized_cue = _normalize_title(cue_title)
        candidates_on_page = page_text_index.get(page_label, []) or page_text_index.get(
            f"page {page_label}", []
        )
        if not candidates_on_page:
            skipped += 1
            continue
        ranked: List[Tuple[int, int, str, str, str, str]] = []
        for chunk_id, block_type, heading_text, section_tail, first_line in candidates_on_page:
            score, bonus = _score_page_candidate(
                normalized_cue,
                cue_title,
                block_type or "",
                heading_text,
                section_tail,
                first_line,
            )
            ranked.append(
                (
                    score,
                    bonus,
                    chunk_id,
                    block_type or "",
                    heading_text or "",
                    first_line or "",
                )
            )
        ranked.sort(key=lambda item: (item[0], item[1]), reverse=True)
        samples.append(
            {
                "source": candidate.get("from"),
                "page_label": page_label,
                "cue": candidate.get("cue", ""),
                "cue_title": cue_title,
                "top_candidates": [
                    {
                        "chunk_id": chunk_id,
                        "block_type": block_type,
                        "heading_text": heading_text,
                        "first_line": first_line,
                        "score": score,
                        "block_bonus": bonus,
                    }
                    for score, bonus, chunk_id, block_type, heading_text, first_line in ranked[:top_k]
                ],
            }
        )
        if len(samples) >= max_samples:
            break
    return {
        "sample_count": len(samples),
        "skipped": skipped,
        "samples": samples,
    }


def _extract_candidates(
    chunks: List[Dict[str, Any]],
    doc_id: str,
    indices: Dict[str, Dict[str, Set[str]]],
    page_text_index: Dict[str, List[Tuple[str, Optional[str], Optional[str], Optional[str]]]],
) -> Tuple[List[Dict[str, Any]], Counter]:
    candidates: List[Dict[str, Any]] = []
    keyword_counts: Counter = Counter()

    for chunk in chunks:
        text = chunk.get("text", "") or ""
        if not text.strip():
            continue
        _count_keywords(text, keyword_counts)
        if chunk.get("block_type") in {"Table", "Picture", "SectionHeader", "Title"}:
            continue

        for entry in REFERENCE_PATTERNS:
            for match in entry["regex"].finditer(text):
                label = match.group("label") if "label" in match.groupdict() else ""
                normalized_label = _normalize_label(label)
                target_type = entry["target_type"]
                if target_type == "section":
                    if normalized_label.startswith(
                        ("chapter ", "page", "pages", "table", "figure")
                    ):
                        continue
                anchor_variants = {normalized_label}
                relation_override: Optional[str] = None
                if target_type == "section":
                    has_number = bool(re.search(r"\d+(?:[.\-–]\d+)+", label))
                    exact_heading = _normalize_title(label)
                    if has_number or exact_heading in indices["section_exact"]:
                        relation_override = "references_named_section"
                        anchor_variants = set()
                        if exact_heading:
                            anchor_variants.add(exact_heading)
                    else:
                        relation_override = "mentions_section"
                elif target_type == "chapter":
                    anchor_variants.add(f"chapter {normalized_label}")
                elif target_type in {"table", "figure"}:
                    anchor_variants.add(f"{target_type} {normalized_label}")
                elif target_type == "page":
                    anchor_variants.add(normalized_label)
                    anchor_variants.add(f"page {normalized_label}")
                resolved_targets: Set[str] = set()
                if target_type == "section" and relation_override == "mentions_section":
                    resolved_targets = set()
                else:
                    for variant in anchor_variants:
                        normalized_variant = _normalize_title(variant)
                        if normalized_variant:
                            index_key = (
                                "section_exact"
                                if relation_override == "references_named_section"
                                else target_type
                            )
                            resolved_targets.update(
                                indices[index_key].get(normalized_variant, set())
                            )
                cue_title = ""
                if target_type == "page":
                    cue_title = _extract_page_cue_title_from_match(text, match)
                if target_type == "page" and resolved_targets:
                    selected = []
                    for variant in anchor_variants:
                        normalized_variant = _normalize_title(variant)
                        if not normalized_variant:
                            continue
                        selected = _select_page_targets(
                            normalized_variant, page_text_index, cue_title
                        )
                        if selected:
                            break
                    if selected:
                        resolved_targets = set(selected)
                resolved_targets_sorted = sorted(resolved_targets)
                is_ambiguous = len(resolved_targets_sorted) > 1 and (
                    relation_override or entry["relation"]
                ) in STRICT_RELATIONS
                candidates.append(
                    {
                        "from": chunk.get("id"),
                        "source_document": doc_id,
                        "page": chunk.get("page"),
                        "content_kind": chunk.get("content_kind"),
                        "section_path": chunk.get("section_path"),
                        "relation": relation_override or entry["relation"],
                        "cue": match.group(0).strip(),
                        "cue_title": cue_title,
                        "parsed_target": {
                            "type": target_type,
                            "label": normalized_label,
                            "raw": label,
                        },
                        "resolved_targets": resolved_targets_sorted,
                        "resolution_count": len(resolved_targets_sorted),
                        "is_ambiguous": is_ambiguous,
                    }
                )

    return candidates, keyword_counts
