"""
Dashboard and report generation for hybrid retrieval experiments.

Generates:
- Markdown reports with tables and charts
- Comparison views across runs
- Attribution analysis visualizations
- Weight sensitivity plots
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from .metrics import (
    ExperimentMetrics,
    STANDARD_K_VALUES,
    format_recall_table,
    format_attribution_summary,
)
from .hybrid_tuning import ExperimentRun


def generate_run_report(run: ExperimentRun) -> str:
    """
    Generate a Markdown report for a single experiment run.
    
    Args:
        run: ExperimentRun to report on
        
    Returns:
        Markdown string
    """
    m = run.metrics
    
    lines = [
        f"# Experiment Run: {run.run_id}",
        "",
        f"**Timestamp:** {run.timestamp}",
        f"**Duration:** {run.duration_seconds:.1f}s",
        "",
        "## Configuration",
        "",
        "| Parameter | Value |",
        "|-----------|-------|",
        f"| Expansion Model | {run.config.expansion_model} |",
        f"| Expansion Terms | {run.config.expansion_terms} |",
        f"| Deterministic Weight | {run.config.deterministic_weight:.2f} |",
        f"| Semantic Weight | {run.config.semantic_weight:.2f} |",
        f"| Anchor Bonus | {run.config.anchor_bonus:.2f} |",
        f"| Term Coverage Bonus | {run.config.term_coverage_bonus:.2f} |",
        f"| Top-K | {run.config.top_k} |",
        "",
        "## Recall Metrics",
        "",
        "| K | Recall@K | Full Recall Rate |",
        "|---|----------|------------------|",
    ]
    
    for k in STANDARD_K_VALUES:
        recall = m.avg_recall_at_k.get(k, 0.0)
        full_rate = m.full_recall_rate_at_k.get(k, 0.0)
        lines.append(f"| {k:2d} | {recall:.1%} | {full_rate:.1%} |")
    
    lines.extend([
        "",
        "## Attribution Analysis",
        "",
        "| Path | Gold Chunks Found |",
        "|------|-------------------|",
        f"| Deterministic Only | {m.attribution.deterministic_only} |",
        f"| Semantic Only | {m.attribution.semantic_only} |",
        f"| Both Paths | {m.attribution.both} |",
        f"| Neither (Missed) | {m.attribution.neither} |",
        "",
        f"**Total Gold Found:** {m.attribution.gold_found}/{m.attribution.gold_count}",
        "",
        "## Latency",
        "",
        f"- **Average:** {m.avg_latency_ms:.0f}ms",
        f"- **P50:** {m.p50_latency_ms:.0f}ms",
        f"- **P95:** {m.p95_latency_ms:.0f}ms",
        "",
    ])
    
    # Add per-query results if available
    if run.per_query_results:
        lines.extend([
            "## Per-Query Results",
            "",
            "| Query | Gold | R@1 | R@5 | R@10 | Latency |",
            "|-------|------|-----|-----|------|---------|",
        ])
        
        for pq in run.per_query_results[:20]:  # Limit to 20
            query_short = pq["query_text"][:40] + "..." if len(pq["query_text"]) > 40 else pq["query_text"]
            r1 = pq["recall_at_k"].get(1, 0)
            r5 = pq["recall_at_k"].get(5, 0)
            r10 = pq["recall_at_k"].get(10, 0)
            lines.append(f"| {query_short} | {pq['gold_count']} | {r1:.0%} | {r5:.0%} | {r10:.0%} | {pq['latency_ms']:.0f}ms |")
    
    return "\n".join(lines)


def generate_grid_search_report(runs: List[ExperimentRun]) -> str:
    """
    Generate a Markdown report for grid search results.
    
    Args:
        runs: List of ExperimentRun (should be sorted by recall@10)
        
    Returns:
        Markdown string
    """
    lines = [
        "# Grid Search Results",
        "",
        f"**Total Configurations:** {len(runs)}",
        f"**Generated:** {datetime.now().isoformat()}",
        "",
        "## Top 10 Configurations",
        "",
        "| Rank | Weights | R@1 | R@5 | R@10 | R@30 | Latency |",
        "|------|---------|-----|-----|------|------|---------|",
    ]
    
    for i, run in enumerate(runs[:10]):
        m = run.metrics
        weights = f"({run.config.deterministic_weight:.1f}, {run.config.semantic_weight:.1f})"
        r1 = f"{m.avg_recall_at_k.get(1, 0):.1%}"
        r5 = f"{m.avg_recall_at_k.get(5, 0):.1%}"
        r10 = f"{m.avg_recall_at_k.get(10, 0):.1%}"
        r30 = f"{m.avg_recall_at_k.get(30, 0):.1%}"
        lat = f"{m.avg_latency_ms:.0f}ms"
        lines.append(f"| {i+1} | {weights} | {r1} | {r5} | {r10} | {r30} | {lat} |")
    
    # Weight sensitivity analysis
    lines.extend([
        "",
        "## Weight Sensitivity",
        "",
        "| Det Weight | Sem Weight | R@10 | Delta from 50/50 |",
        "|------------|------------|------|------------------|",
    ])
    
    # Find baseline (50/50)
    baseline_recall = 0.0
    for run in runs:
        if run.config.deterministic_weight == 0.5:
            baseline_recall = run.metrics.avg_recall_at_k.get(10, 0)
            break
    
    for run in runs:
        m = run.metrics
        r10 = m.avg_recall_at_k.get(10, 0)
        delta = r10 - baseline_recall
        delta_str = f"+{delta:.1%}" if delta >= 0 else f"{delta:.1%}"
        lines.append(
            f"| {run.config.deterministic_weight:.1f} | {run.config.semantic_weight:.1f} | "
            f"{r10:.1%} | {delta_str} |"
        )
    
    # Attribution comparison
    lines.extend([
        "",
        "## Attribution by Weight Configuration",
        "",
        "| Weights | Det-Only | Sem-Only | Both | Missed |",
        "|---------|----------|----------|------|--------|",
    ])
    
    for run in runs[:10]:
        m = run.metrics
        weights = f"({run.config.deterministic_weight:.1f}, {run.config.semantic_weight:.1f})"
        lines.append(
            f"| {weights} | {m.attribution.deterministic_only} | "
            f"{m.attribution.semantic_only} | {m.attribution.both} | "
            f"{m.attribution.neither} |"
        )
    
    return "\n".join(lines)


def generate_model_comparison_report(runs: List[ExperimentRun]) -> str:
    """
    Generate a Markdown report comparing models.
    
    Args:
        runs: List of ExperimentRun (one per model)
        
    Returns:
        Markdown string
    """
    lines = [
        "# Model Comparison Report",
        "",
        f"**Generated:** {datetime.now().isoformat()}",
        "",
        "## Recall Comparison",
        "",
        "| Model | R@1 | R@5 | R@10 | R@30 |",
        "|-------|-----|-----|------|------|",
    ]
    
    for run in runs:
        m = run.metrics
        model = run.config.expansion_model if isinstance(run.config.expansion_model, str) else run.config.expansion_model.name
        r1 = f"{m.avg_recall_at_k.get(1, 0):.1%}"
        r5 = f"{m.avg_recall_at_k.get(5, 0):.1%}"
        r10 = f"{m.avg_recall_at_k.get(10, 0):.1%}"
        r30 = f"{m.avg_recall_at_k.get(30, 0):.1%}"
        lines.append(f"| {model} | {r1} | {r5} | {r10} | {r30} |")
    
    lines.extend([
        "",
        "## Latency Comparison",
        "",
        "| Model | Avg Latency | P50 | P95 |",
        "|-------|-------------|-----|-----|",
    ])
    
    for run in runs:
        m = run.metrics
        model = run.config.expansion_model if isinstance(run.config.expansion_model, str) else run.config.expansion_model.name
        lines.append(
            f"| {model} | {m.avg_latency_ms:.0f}ms | "
            f"{m.p50_latency_ms:.0f}ms | {m.p95_latency_ms:.0f}ms |"
        )
    
    lines.extend([
        "",
        "## Cost-Performance Tradeoff",
        "",
        "| Model | R@10 | Latency | Efficiency Score |",
        "|-------|------|---------|------------------|",
    ])
    
    for run in runs:
        m = run.metrics
        model = run.config.expansion_model if isinstance(run.config.expansion_model, str) else run.config.expansion_model.name
        r10 = m.avg_recall_at_k.get(10, 0)
        lat = m.avg_latency_ms
        # Efficiency = recall per second of latency
        efficiency = (r10 * 1000) / max(1, lat)
        lines.append(f"| {model} | {r10:.1%} | {lat:.0f}ms | {efficiency:.2f} |")
    
    return "\n".join(lines)


def save_report(
    report: str,
    name: str,
    output_dir: Optional[Path] = None,
) -> Path:
    """
    Save a report to file.
    
    Args:
        report: Markdown content
        name: Report name (without extension)
        output_dir: Output directory
        
    Returns:
        Path to saved file
    """
    output_dir = output_dir or Path("experiments/reports")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    path = output_dir / f"{name}-{timestamp}.md"
    
    with open(path, "w") as f:
        f.write(report)
    
    print(f"📊 Report saved: {path}")
    return path


def load_run_from_json(path: Path) -> ExperimentRun:
    """
    Load an ExperimentRun from JSON file.
    
    Args:
        path: Path to JSON file
        
    Returns:
        ExperimentRun
    """
    from traversal.hybrid_retriever import HybridConfig
    from .metrics import ExperimentMetrics, AttributionMetrics, ExpansionQualityMetrics
    
    with open(path) as f:
        data = json.load(f)
    
    config = HybridConfig(
        expansion_model=data["config"]["expansion_model"],
        expansion_terms=data["config"]["expansion_terms"],
        deterministic_weight=data["config"]["deterministic_weight"],
        semantic_weight=data["config"]["semantic_weight"],
        anchor_bonus=data["config"]["anchor_bonus"],
        term_coverage_bonus=data["config"]["term_coverage_bonus"],
        top_k=data["config"]["top_k"],
    )
    
    attr_data = data["metrics"].get("attribution", {})
    attribution = AttributionMetrics(
        deterministic_only=attr_data.get("deterministic_only", 0),
        semantic_only=attr_data.get("semantic_only", 0),
        both=attr_data.get("both", 0),
        neither=attr_data.get("neither", 0),
    )
    
    metrics = ExperimentMetrics(
        total_queries=data["metrics"]["total_queries"],
        avg_recall_at_k={int(k): v for k, v in data["metrics"]["avg_recall_at_k"].items()},
        full_recall_rate_at_k={int(k): v for k, v in data["metrics"].get("full_recall_rate_at_k", {}).items()},
        attribution=attribution,
        avg_latency_ms=data["metrics"].get("avg_latency_ms", 0),
        p95_latency_ms=data["metrics"].get("p95_latency_ms", 0),
    )
    
    return ExperimentRun(
        run_id=data["run_id"],
        config=config,
        metrics=metrics,
        timestamp=data.get("timestamp", ""),
        duration_seconds=data.get("duration_seconds", 0),
    )


def generate_comparison_report(
    run_paths: List[Path],
    title: str = "Run Comparison",
) -> str:
    """
    Generate a comparison report from multiple run files.
    
    Args:
        run_paths: List of paths to run JSON files
        title: Report title
        
    Returns:
        Markdown string
    """
    runs = [load_run_from_json(p) for p in run_paths]
    
    lines = [
        f"# {title}",
        "",
        f"**Runs Compared:** {len(runs)}",
        f"**Generated:** {datetime.now().isoformat()}",
        "",
        "## Configuration Summary",
        "",
        "| Run ID | Model | Weights | Anchor Bonus |",
        "|--------|-------|---------|--------------|",
    ]
    
    for run in runs:
        weights = f"({run.config.deterministic_weight:.1f}, {run.config.semantic_weight:.1f})"
        lines.append(
            f"| {run.run_id} | {run.config.expansion_model} | "
            f"{weights} | {run.config.anchor_bonus:.1f} |"
        )
    
    lines.extend([
        "",
        "## Recall Comparison",
        "",
        "| Run ID | R@1 | R@5 | R@10 | R@20 | R@30 |",
        "|--------|-----|-----|------|------|------|",
    ])
    
    for run in runs:
        m = run.metrics
        vals = [f"{m.avg_recall_at_k.get(k, 0):.1%}" for k in [1, 5, 10, 20, 30]]
        lines.append(f"| {run.run_id} | {' | '.join(vals)} |")
    
    lines.extend([
        "",
        "## Performance",
        "",
        "| Run ID | Avg Latency | P95 Latency | Duration |",
        "|--------|-------------|-------------|----------|",
    ])
    
    for run in runs:
        m = run.metrics
        lines.append(
            f"| {run.run_id} | {m.avg_latency_ms:.0f}ms | "
            f"{m.p95_latency_ms:.0f}ms | {run.duration_seconds:.1f}s |"
        )
    
    return "\n".join(lines)


def print_dashboard(runs: List[ExperimentRun]) -> None:
    """
    Print a quick dashboard view to console.
    
    Args:
        runs: List of experiment runs
    """
    print("\n" + "="*70)
    print("HYBRID RETRIEVAL EXPERIMENT DASHBOARD")
    print("="*70)
    
    if not runs:
        print("No runs to display.")
        return
    
    print(f"\n📊 {len(runs)} runs loaded\n")
    
    # Best run summary
    best_run = max(runs, key=lambda r: r.metrics.avg_recall_at_k.get(10, 0))
    print("🏆 BEST RUN:")
    print(f"   ID: {best_run.run_id}")
    print(f"   Model: {best_run.config.expansion_model}")
    print(f"   Weights: ({best_run.config.deterministic_weight:.1f}, {best_run.config.semantic_weight:.1f})")
    print(f"   Recall@10: {best_run.metrics.avg_recall_at_k.get(10, 0):.1%}")
    
    # Quick comparison table
    print("\n📈 RECALL SUMMARY:")
    print("-" * 50)
    print(f"{'Run ID':<20} {'R@5':>8} {'R@10':>8} {'R@30':>8}")
    print("-" * 50)
    
    for run in sorted(runs, key=lambda r: r.metrics.avg_recall_at_k.get(10, 0), reverse=True)[:5]:
        m = run.metrics
        print(
            f"{run.run_id[:20]:<20} "
            f"{m.avg_recall_at_k.get(5, 0):>7.1%} "
            f"{m.avg_recall_at_k.get(10, 0):>7.1%} "
            f"{m.avg_recall_at_k.get(30, 0):>7.1%}"
        )
    
    print("="*70 + "\n")
