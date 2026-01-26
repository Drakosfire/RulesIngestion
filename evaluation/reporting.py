from __future__ import annotations

import json
import os
from typing import Any, Dict, Iterable, List, Optional, Tuple


def _table(lines: List[str], rows: Iterable[Tuple[str, str]]) -> None:
    lines.append("| Metric | Value |")
    lines.append("| --- | --- |")
    for label, value in rows:
        lines.append(f"| {label} | {value} |")


def _code_block(lines: List[str], payload: Any, language: str = "json") -> None:
    lines.append(f"```{language}")
    lines.append(json.dumps(payload, indent=2))
    lines.append("```")


def write_report(report: Dict[str, Any], report_dir: str, report_basename: str) -> Dict[str, str]:
    os.makedirs(report_dir, exist_ok=True)
    json_path = os.path.join(report_dir, f"{report_basename}.json")
    md_path = os.path.join(report_dir, f"{report_basename}.md")

    with open(json_path, "w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)

    lines = []
    summary = report["summary"]
    lines.append(f"# RulesLawyer Evaluation Report: {summary['model_id']}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("### Run")
    _table(
        lines,
        [
            ("Run ID", f"`{summary['run_id']}`"),
            ("Ruleset ID", f"`{summary.get('ruleset_id')}`"),
            ("Document ID", f"`{summary.get('document_id')}`"),
            ("Chunk source", f"`{summary['chunk_source']}`"),
            ("Chunk count", f"`{summary['chunk_count']}`"),
            ("Query count", f"`{summary['query_count']}`"),
            ("Evaluated queries", f"`{summary['evaluated_queries']}`"),
            ("Embeddings reused", f"`{summary.get('embedding_reused')}`"),
        ],
    )
    if summary.get("embedding_reuse_reason"):
        lines.append("")
        lines.append(f"Embedding reuse reason: `{summary.get('embedding_reuse_reason')}`")
    if summary.get("baseline_report"):
        lines.append("")
        lines.append(f"Baseline report: `{summary.get('baseline_report')}`")
    lines.append("")
    lines.append("### Strict Gold Metrics")
    _table(
        lines,
        [("Coverage", f"`{summary['coverage']:.4f}`"), ("MRR", f"`{summary['mrr']:.4f}`")]
        + [(key, f"`{value:.4f}`") for key, value in summary["hit_rates"].items()],
    )
    answer_similarity = summary.get("answer_similarity") or {}
    if answer_similarity:
        lines.append("")
        lines.append("### Answer Similarity (Reference Answer vs Top-k Chunks)")
        _table(
            lines,
            [
                (key, f"`{value:.4f}`" if value is not None else "`n/a`")
                for key, value in answer_similarity.items()
            ],
        )
    contamination = summary.get("cross_book_contamination") or {}
    if contamination:
        lines.append("")
        lines.append("### Cross-Book Contamination")
        _table(lines, [(key, f"`{value:.4f}`") for key, value in contamination.items()])
    graph_boost = summary.get("graph_boost") or {}
    if graph_boost.get("enabled"):
        lines.append("")
        lines.append("### Graph Boost")
        lines.append(
            f"- Value: `{graph_boost.get('value')}` (depth={graph_boost.get('depth')}, "
            f"top_k={graph_boost.get('top_k')}, source={graph_boost.get('source')}, "
            f"seed_top_n={graph_boost.get('seed_top_n')}, "
            f"same_kind_only={graph_boost.get('same_kind_only')}, decay={graph_boost.get('decay')})"
        )
    chapter_routing = summary.get("chapter_routing") or {}
    if chapter_routing.get("enabled"):
        lines.append("")
        lines.append("### Chapter Routing")
        lines.append(
            f"- top_n: `{chapter_routing.get('top_n')}` (source={chapter_routing.get('source')}, "
            f"chapters={chapter_routing.get('chapter_count')}, "
            f"avg_allowed_chunks={chapter_routing.get('avg_allowed_chunks')}, "
            f"expected_recall={chapter_routing.get('expected_recall')}, "
            f"rerank={chapter_routing.get('rerank')})"
        )
    lines.append("")

    traversal = report.get("traversal_eval") or summary.get("traversal_eval")
    if traversal and traversal.get("enabled") and traversal.get("baseline") and traversal.get("delta"):
        lines.append("### Traversal Eval (Baseline vs Chapter-Restricted)")
        lines.append("#### Baseline")
        _table(
            lines,
            [("Coverage", f"`{traversal['baseline']['coverage']:.4f}`"), ("MRR", f"`{traversal['baseline']['mrr']:.4f}`")]
            + [
                (f"{key}", f"`{value:.4f}`")
                for key, value in traversal["baseline"]["hit_rates"].items()
            ],
        )
        lines.append("")
        lines.append("#### Delta (Routing - Baseline)")
        _table(
            lines,
            [("Coverage Δ", f"`{traversal['delta']['coverage']:.4f}`"), ("MRR Δ", f"`{traversal['delta']['mrr']:.4f}`")]
            + [
                (f"{key} Δ", f"`{value:.4f}`")
                for key, value in traversal["delta"]["hit_rates"].items()
            ],
        )
        lines.append("")
        reachability = traversal.get("reachability_monotonicity")
        if reachability:
            lines.append("#### Reachability Monotonicity (Chapter Recall)")
            lines.append(
                f"- Pool recall: `{reachability.get('pool_recall', 0.0):.4f}` "
                f"({reachability.get('reachable_queries', 0) - reachability.get('lost_at_pool', 0)}/"
                f"{reachability.get('reachable_queries', 0)} queries)"
            )
            lines.append(
                f"- Final recall: `{reachability.get('final_recall', 0.0):.4f}` "
                f"({reachability.get('reachable_queries', 0) - reachability.get('lost_at_final', 0)}/"
                f"{reachability.get('reachable_queries', 0)} queries)"
            )
            lines.append(f"- Lost at pool (summary insufficiency): `{reachability.get('lost_at_pool', 0)}`")
            lines.append(f"- Lost at final (rerank failure): `{reachability.get('lost_at_final', 0)}`")
            lines.append(
                f"- **Reachability monotonic**: `{reachability.get('reachability_monotonic', False)}`"
            )
            lines.append("")
        cross_book = traversal.get("cross_book_reachability")
        if cross_book:
            lines.append("#### Cross-Book Reachability (Explicit References)")
            lines.append(
                f"- Explicit cross-book queries: `{cross_book.get('explicit_cross_book_queries', 0)}`"
            )
            lines.append(
                f"- Explicit with cross-book gold: `{cross_book.get('explicit_with_cross_gold', 0)}`"
            )
            lines.append(f"- Pool recall: `{cross_book.get('pool_recall', 0.0):.4f}`")
            lines.append(f"- Final recall: `{cross_book.get('final_recall', 0.0):.4f}`")
            lines.append("")
        rank_mono = traversal.get("rank_monotonicity")
        if rank_mono:
            lines.append("#### Rank Monotonicity (hit@k - weak constraint)")
            lines.append("- Regressions (baseline hit → routing miss):")
            for key, value in rank_mono["regressions"].items():
                ok = rank_mono["monotonic_ok"].get(key)
                lines.append(f"  - {key}: `{value}` (ok={ok})")
            lines.append("- Improvements (baseline miss → routing hit):")
            for key, value in rank_mono["improvements"].items():
                lines.append(f"  - {key}: `{value}`")
            lines.append("")

    if summary.get("expanded_query_count") is not None:
        lines.append("### Expanded Gold Metrics")
        _table(
            lines,
            [("Coverage", f"`{summary['coverage_expanded']:.4f}`"), ("MRR", f"`{summary['mrr_expanded']:.4f}`")]
            + [
                (key, f"`{value:.4f}`")
                for key, value in summary["hit_rates_expanded"].items()
            ],
        )
        lines.append("")
        lines.append("### Expanded Gold Expansion Stats")
        _table(
            lines,
            [
                ("Queries with additions", f"`{summary['expanded_queries_with_additions']}`"),
                ("Avg added per query", f"`{summary['expanded_avg_added']:.2f}`"),
                ("Max added", f"`{summary['expanded_max_added']}`"),
            ],
        )
        addition_reasons = summary.get("expanded_addition_reasons") or {}
        if addition_reasons:
            lines.append("")
            lines.append("#### Addition Reasons")
            _table(lines, [(key, f"`{value}`") for key, value in addition_reasons.items()])
        lines.append("")

        baseline_delta = summary.get("baseline_delta") or {}
        if baseline_delta:
            lines.append("### Expanded Gold Delta (Expanded - Strict)")
            if baseline_delta.get("coverage_expanded") is not None:
                coverage_delta = f"`{baseline_delta['coverage_expanded']:.4f}`"
            else:
                coverage_delta = "`n/a`"
            expanded_rates = baseline_delta.get("hit_rates_expanded") or {}
            _table(
                lines,
                [("Coverage Δ", coverage_delta), ("MRR Δ", f"`{baseline_delta['mrr_expanded']:.4f}`")]
                + [(f"{key} Δ", f"`{value:.4f}`") for key, value in expanded_rates.items()],
            )
        lines.append("")

    lines.append("## Timings (ms)")
    _table(
        lines,
        [
            ("Embedding (chunks)", f"`{summary['timings_ms']['embedding']}`"),
            ("Embedding (queries)", f"`{summary['timings_ms']['query_embedding']}`"),
            ("Embedding (answers)", f"`{summary['timings_ms'].get('answer_embedding', 0)}`"),
            ("Evaluation (strict)", f"`{summary['timings_ms']['evaluation_strict']}`"),
            ("Evaluation (expanded)", f"`{summary['timings_ms']['evaluation_expanded']}`"),
            ("Total", f"`{summary['timings_ms']['total']}`"),
        ],
    )
    timing_estimates = summary.get("timings_estimate_ms")
    if timing_estimates:
        lines.append("")
        lines.append("### Timing Estimates (ms)")
        _table(
            lines,
            [
                ("Evaluation (strict)", f"`{timing_estimates.get('evaluation_strict')}`"),
                ("Evaluation (expanded)", f"`{timing_estimates.get('evaluation_expanded')}`"),
                ("Total", f"`{timing_estimates.get('total')}`"),
            ],
        )
    lines.append("")

    lines.append("## Query Details")
    for detail in report["queries"]:
        lines.append(f"### Query {detail['query_index']}")
        lines.append("")
        lines.append(f"**Text:** {detail['query_text']}")
        lines.append("")
        lines.append("- Expected found: `{}`".format(detail["expected_found"]))
        lines.append("- Expected rank: `{}`".format(detail["expected_rank"]))
        answer_keys = [key for key in detail.keys() if key.startswith("answer_similarity@")]
        if answer_keys:
            for key in sorted(answer_keys):
                value = detail.get(key)
                lines.append(f"- {key}: `{value:.4f}`" if value is not None else f"- {key}: `n/a`")
        lines.append("")
        lines.append("#### Expected chunk IDs")
        _code_block(lines, detail["expected_chunk_ids"])
        if detail.get("chapter_routing_top_chapters"):
            lines.append("- Routed chapters:")
            for routed in detail["chapter_routing_top_chapters"]:
                score = routed.get("score")
                summary_score = routed.get("summary_score")
                rerank_score = routed.get("rerank_score")
                if summary_score is not None and rerank_score is not None:
                    lines.append(
                        f"  - {routed['chapter_id']}: `{score:.4f}` "
                        f"(summary={summary_score:.4f}, rerank={rerank_score:.4f})"
                    )
                else:
                    lines.append(f"  - {routed['chapter_id']}: `{score:.4f}`")
        if detail.get("graph_boost_applied") is not None:
            lines.append(f"- Graph boost applied: `{detail.get('graph_boost_applied')}`")
            lines.append(f"- Graph boosted count: `{detail.get('graph_boosted_count')}`")
            lines.append(f"- Graph boost seed source: `{detail.get('graph_boost_seed_source')}`")
            lines.append("")
            lines.append("#### Graph boost seed ids")
            _code_block(lines, detail.get("graph_boost_seed_ids"))
        if detail.get("expanded_expected_chunk_ids") is not None:
            lines.append("- Expanded expected found: `{}`".format(detail["expanded_expected_found"]))
            lines.append("- Expanded expected rank: `{}`".format(detail["expanded_expected_rank"]))
            lines.append("")
            lines.append("#### Expanded expected chunk IDs")
            _code_block(lines, detail["expanded_expected_chunk_ids"])
            added_chunks = detail.get("expanded_added_chunks") or []
            if added_chunks:
                lines.append("- Expanded additions:")
                for added in added_chunks:
                    reasons = ", ".join(added.get("reasons", [])) or "n/a"
                    lines.append(
                        f"  - `{added['chunk_id']}` (reasons: {reasons})"
                    )
        if detail["top_results"]:
            lines.append("")
            lines.append("| Rank | Chunk ID | Score | Preview |")
            lines.append("| --- | --- | --- | --- |")
            for result in detail["top_results"]:
                preview = " ".join((result.get("preview") or "").split())
                preview = preview.replace("|", "\\|")
                lines.append(
                    f"| {result['rank']} | `{result['chunk_id']}` | {result['score']:.6f} | {preview} |"
                )
        lines.append("")

    with open(md_path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines).strip() + "\n")

    return {"json": json_path, "md": md_path}
