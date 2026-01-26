"""Discover candidate deterministic edges from enriched chunks."""

from __future__ import annotations

import sys
import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Iterable, List

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from scripts.discover_deterministic_edges_candidates import (
    _build_page_reference_debug,
    _extract_candidates,
)
from scripts.discover_deterministic_edges_constants import (
    DEFAULT_NEAR_DUPLICATE_MAX,
    DEFAULT_NEAR_DUPLICATE_RATE_MAX,
    DEFAULT_SUSPECT_TOKEN_RATE_MAX,
    DEFAULT_UNRESOLVED_RATE_MAX,
)
from scripts.discover_deterministic_edges_gates import _run_ocr_spelling_gates
from scripts.discover_deterministic_edges_indexing import (
    _build_indices,
    _build_page_text_index,
    _load_enriched,
    _parse_doc_page_offset,
)
from scripts.discover_deterministic_edges_summary import (
    _print_summary,
    _summarize_candidates,
)


def _iter_enriched_paths(paths: List[str]) -> Iterable[Path]:
    if not paths:
        return []
    expanded: List[Path] = []
    for entry in paths:
        path = Path(entry)
        if path.is_dir():
            expanded.extend(path.rglob("*.enriched.json"))
        elif path.is_file() and path.name.endswith(".enriched.json"):
            expanded.append(path)
    return expanded


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Discover candidate deterministic edges from enriched outputs."
    )
    parser.add_argument(
        "paths",
        nargs="+",
        help="Enriched JSON files or directories containing outputs",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write sidecar candidate files next to enriched outputs",
    )
    parser.add_argument(
        "--skip-gates",
        action="store_true",
        help="Skip OCR/spelling gate checks before edge discovery",
    )
    parser.add_argument(
        "--allow-gate-fail",
        action="store_true",
        help="Continue even if OCR/spelling gates fail",
    )
    parser.add_argument(
        "--unresolved-rate-max",
        type=float,
        default=DEFAULT_UNRESOLVED_RATE_MAX,
        help="Max unresolved strict reference rate before failing gate",
    )
    parser.add_argument(
        "--suspect-token-rate-max",
        type=float,
        default=DEFAULT_SUSPECT_TOKEN_RATE_MAX,
        help="Max suspect token rate before failing gate",
    )
    parser.add_argument(
        "--near-duplicate-max",
        type=int,
        default=DEFAULT_NEAR_DUPLICATE_MAX,
        help="Max near-duplicate title pairs before failing gate",
    )
    parser.add_argument(
        "--near-duplicate-rate-max",
        type=float,
        default=DEFAULT_NEAR_DUPLICATE_RATE_MAX,
        help="Max near-duplicate title rate before failing gate",
    )
    args = parser.parse_args()

    enriched_paths = list(_iter_enriched_paths(args.paths))
    if not enriched_paths:
        print("No enriched outputs found.")
        return

    global_candidates: List[dict] = []
    global_keyword_counts: Counter = Counter()

    for path in sorted(enriched_paths):
        doc_id, chunks = _load_enriched(path)
        page_offset = _parse_doc_page_offset(doc_id)
        indices = _build_indices(chunks, doc_id, page_offset)
        page_text_index = _build_page_text_index(chunks, page_offset)
        candidates, keyword_counts = _extract_candidates(
            chunks, doc_id, indices, page_text_index
        )
        if not args.skip_gates:
            gate_summary = _run_ocr_spelling_gates(
                candidates=candidates,
                indices=indices,
                chunks=chunks,
                unresolved_rate_max=args.unresolved_rate_max,
                suspect_token_rate_max=args.suspect_token_rate_max,
                near_duplicate_max=args.near_duplicate_max,
                near_duplicate_rate_max=args.near_duplicate_rate_max,
                allow_gate_fail=args.allow_gate_fail,
            )
            print(f"  gates: {gate_summary}")
        summary = _summarize_candidates(candidates)
        _print_summary(doc_id, summary, keyword_counts)

        global_candidates.extend(candidates)
        global_keyword_counts.update(keyword_counts)

        if args.write:
            output_path = path.with_suffix(".edge_candidates.json")
            payload = {
                "document": doc_id,
                "summary": summary,
                "cue_keyword_counts": dict(keyword_counts),
                "candidates": candidates,
            }
            with output_path.open("w", encoding="utf-8") as handle:
                json.dump(payload, handle, indent=2)
            print(f"  wrote: {output_path}")
            debug_payload = _build_page_reference_debug(candidates, page_text_index)
            debug_path = path.with_suffix(".page_ref_debug.json")
            with debug_path.open("w", encoding="utf-8") as handle:
                json.dump(debug_payload, handle, indent=2)
            print(f"  wrote: {debug_path}")

    global_summary = _summarize_candidates(global_candidates)
    print("\nAll documents")
    print(f"  candidates: {global_summary.get('total_candidates', 0)}")
    for relation, count in sorted(global_summary.get("relation_counts", {}).items()):
        stats = global_summary.get("resolution_summary", {}).get(relation, {})
        print(
            "  - "
            f"{relation}: {count} "
            f"(unique={stats.get('unique', 0)}, "
            f"zero={stats.get('zero', 0)}, "
            f"multi={stats.get('multi', 0)}, "
            f"unique_rate={stats.get('unique_rate', 0)})"
        )
    if global_keyword_counts:
        print("  cue_keywords:")
        for keyword, count in global_keyword_counts.most_common():
            print(f"    - {keyword.strip()}: {count}")


if __name__ == "__main__":
    main()
