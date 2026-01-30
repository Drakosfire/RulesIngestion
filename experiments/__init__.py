"""
Experiments package for hybrid retrieval tuning.

Modules:
- metrics: Per-path attribution, expansion quality, weight sensitivity metrics
- hybrid_tuning: Grid search tuning framework
- dashboard: Report generation and visualization
"""

from .metrics import (
    RecallAtK,
    FullRecallAtK,
    AttributionMetrics,
    ExpansionQualityMetrics,
    WeightSensitivityMetrics,
    ExperimentMetrics,
    compute_recall_at_k,
    compute_full_recall_at_k,
    compute_attribution_metrics,
    compute_expansion_quality_metrics,
    aggregate_experiment_metrics,
    STANDARD_K_VALUES,
)

from .hybrid_tuning import (
    ExperimentQuery,
    ExperimentRun,
    GridSearchConfig,
    ExperimentRunner,
    load_queries_from_json,
    print_run_summary,
    print_grid_search_summary,
)

from .dashboard import (
    generate_run_report,
    generate_grid_search_report,
    generate_model_comparison_report,
    generate_comparison_report,
    save_report,
    load_run_from_json,
    print_dashboard,
)

__all__ = [
    # Metrics
    "RecallAtK",
    "FullRecallAtK",
    "AttributionMetrics",
    "ExpansionQualityMetrics",
    "WeightSensitivityMetrics",
    "ExperimentMetrics",
    "compute_recall_at_k",
    "compute_full_recall_at_k",
    "compute_attribution_metrics",
    "compute_expansion_quality_metrics",
    "aggregate_experiment_metrics",
    "STANDARD_K_VALUES",
    # Tuning
    "ExperimentQuery",
    "ExperimentRun",
    "GridSearchConfig",
    "ExperimentRunner",
    "load_queries_from_json",
    "print_run_summary",
    "print_grid_search_summary",
    # Dashboard
    "generate_run_report",
    "generate_grid_search_report",
    "generate_model_comparison_report",
    "generate_comparison_report",
    "save_report",
    "load_run_from_json",
    "print_dashboard",
]
