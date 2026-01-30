"""
Tuning framework for hybrid retrieval experiments.

Provides:
- Grid search over weight configurations
- Model comparison experiments
- Few-shot prompt tuning
- Result persistence and comparison
"""

from __future__ import annotations

import json
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime
from itertools import product
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Set, Tuple

from traversal.index import TraversalIndex
from traversal.hybrid_retriever import (
    HybridConfig,
    HybridRetriever,
    HybridRetrievalResult,
)
from traversal.model_adapter import EXPANSION_MODELS

from .metrics import (
    ExperimentMetrics,
    aggregate_experiment_metrics,
    compute_recall_at_k,
    STANDARD_K_VALUES,
)


@dataclass
class ExperimentQuery:
    """
    A query for evaluation with gold chunks.
    
    Attributes:
        query_id: Unique identifier
        query_text: The user query
        gold_chunk_ids: Set of expected correct chunk IDs
        intent: Optional pre-classified intent
        metadata: Optional additional metadata
    """
    query_id: str
    query_text: str
    gold_chunk_ids: Set[str]
    intent: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ExperimentQuery":
        """Create from dict (e.g., from JSON)."""
        return cls(
            query_id=data.get("id", data.get("query_id", "")),
            query_text=data.get("query_text", data.get("question", "")),
            gold_chunk_ids=set(data.get("gold_chunk_ids", data.get("expected_chunk_ids", []))),
            intent=data.get("intent"),
            metadata=data.get("metadata", {}),
        )


@dataclass
class ExperimentRun:
    """
    A single experiment run with configuration and results.
    
    Attributes:
        run_id: Unique identifier for this run
        config: HybridConfig used
        metrics: Aggregated metrics
        per_query_results: Optional detailed per-query results
        timestamp: When the run was executed
        duration_seconds: How long the run took
    """
    run_id: str
    config: HybridConfig
    metrics: ExperimentMetrics
    per_query_results: Optional[List[Dict[str, Any]]] = None
    timestamp: str = ""
    duration_seconds: float = 0.0
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to serializable dict."""
        return {
            "run_id": self.run_id,
            "config": {
                "expansion_model": self.config.expansion_model if isinstance(self.config.expansion_model, str) else self.config.expansion_model.name,
                "expansion_terms": self.config.expansion_terms,
                "deterministic_weight": self.config.deterministic_weight,
                "semantic_weight": self.config.semantic_weight,
                "anchor_bonus": self.config.anchor_bonus,
                "term_coverage_bonus": self.config.term_coverage_bonus,
                "top_k": self.config.top_k,
            },
            "metrics": {
                "total_queries": self.metrics.total_queries,
                "avg_recall_at_k": self.metrics.avg_recall_at_k,
                "full_recall_rate_at_k": self.metrics.full_recall_rate_at_k,
                "attribution": {
                    "deterministic_only": self.metrics.attribution.deterministic_only,
                    "semantic_only": self.metrics.attribution.semantic_only,
                    "both": self.metrics.attribution.both,
                    "neither": self.metrics.attribution.neither,
                },
                "avg_latency_ms": self.metrics.avg_latency_ms,
                "p95_latency_ms": self.metrics.p95_latency_ms,
            },
            "timestamp": self.timestamp,
            "duration_seconds": self.duration_seconds,
        }


@dataclass
class GridSearchConfig:
    """
    Configuration for grid search experiments.
    
    Attributes:
        weight_pairs: List of (deterministic_weight, semantic_weight) pairs
        models: List of model names to try
        anchor_bonuses: List of anchor bonus values
        term_coverage_bonuses: List of term coverage bonus values
    """
    weight_pairs: List[Tuple[float, float]] = field(default_factory=lambda: [
        (1.0, 0.0),   # Deterministic only
        (0.8, 0.2),
        (0.6, 0.4),
        (0.5, 0.5),   # Balanced
        (0.4, 0.6),
        (0.2, 0.8),
        (0.0, 1.0),   # Semantic only
    ])
    models: List[str] = field(default_factory=lambda: ["gpt-4o-mini"])
    anchor_bonuses: List[float] = field(default_factory=lambda: [1.0])
    term_coverage_bonuses: List[float] = field(default_factory=lambda: [0.1])
    
    def all_configs(self) -> List[HybridConfig]:
        """Generate all configuration combinations."""
        configs = []
        
        for (det_w, sem_w), model, anchor_b, term_b in product(
            self.weight_pairs,
            self.models,
            self.anchor_bonuses,
            self.term_coverage_bonuses,
        ):
            configs.append(HybridConfig(
                expansion_model=model,
                deterministic_weight=det_w,
                semantic_weight=sem_w,
                anchor_bonus=anchor_b,
                term_coverage_bonus=term_b,
            ))
        
        return configs


class ExperimentRunner:
    """
    Runs hybrid retrieval experiments.
    
    Usage:
        runner = ExperimentRunner(index, queries)
        
        # Single config
        result = runner.run_single(config)
        
        # Grid search
        results = runner.run_grid_search(grid_config)
        
        # Model comparison
        results = runner.compare_models(["gpt-4o-mini", "claude-haiku"])
    """
    
    def __init__(
        self,
        index: TraversalIndex,
        queries: List[ExperimentQuery],
        semantic_search_fn: Optional[Callable[[str, int], List[Dict]]] = None,
        output_dir: Optional[Path] = None,
    ):
        """
        Initialize the experiment runner.
        
        Args:
            index: TraversalIndex
            queries: List of ExperimentQuery with gold chunks
            semantic_search_fn: Optional semantic search function
            output_dir: Optional directory to save results
        """
        self.index = index
        self.queries = queries
        self.semantic_search_fn = semantic_search_fn
        self.output_dir = output_dir or Path("experiments/results")
        self._run_counter = 0
    
    def _generate_run_id(self) -> str:
        """Generate unique run ID."""
        self._run_counter += 1
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        return f"run-{timestamp}-{self._run_counter:03d}"
    
    def run_single(
        self,
        config: HybridConfig,
        save_results: bool = True,
        save_per_query: bool = False,
    ) -> ExperimentRun:
        """
        Run experiment with a single configuration.
        
        Args:
            config: HybridConfig to use
            save_results: Whether to save to output_dir
            save_per_query: Whether to save per-query details
            
        Returns:
            ExperimentRun with results
        """
        run_id = self._generate_run_id()
        start_time = time.perf_counter()
        
        # Configure retriever
        if self.semantic_search_fn:
            config.semantic_search_fn = self.semantic_search_fn
            config.enable_semantic = True
        else:
            config.enable_semantic = False
        
        retriever = HybridRetriever(self.index, config)
        
        # Run retrieval for all queries
        results: List[HybridRetrievalResult] = []
        gold_ids_list: List[Set[str]] = []
        
        for query in self.queries:
            result = retriever.retrieve(
                query.query_text,
                gold_chunk_ids=query.gold_chunk_ids,
            )
            results.append(result)
            gold_ids_list.append(query.gold_chunk_ids)
        
        # Aggregate metrics
        metrics = aggregate_experiment_metrics(results, gold_ids_list)
        metrics.weights = (config.deterministic_weight, config.semantic_weight)
        
        duration = time.perf_counter() - start_time
        
        # Build per-query results if requested
        per_query = None
        if save_per_query:
            per_query = []
            for query, result in zip(self.queries, results):
                recall = compute_recall_at_k(result, query.gold_chunk_ids)
                per_query.append({
                    "query_id": query.query_id,
                    "query_text": query.query_text,
                    "gold_count": len(query.gold_chunk_ids),
                    "recall_at_k": recall.k_values,
                    "best_k": recall.best_k,
                    "latency_ms": result.diagnostics.total_latency_ms,
                    "expanded_terms": result.diagnostics.expanded_terms,
                })
        
        run = ExperimentRun(
            run_id=run_id,
            config=config,
            metrics=metrics,
            per_query_results=per_query,
            timestamp=datetime.now().isoformat(),
            duration_seconds=duration,
        )
        
        if save_results:
            self._save_run(run)
        
        return run
    
    def run_grid_search(
        self,
        grid_config: GridSearchConfig,
        save_results: bool = True,
    ) -> List[ExperimentRun]:
        """
        Run grid search over configuration space.
        
        Args:
            grid_config: GridSearchConfig defining search space
            save_results: Whether to save results
            
        Returns:
            List of ExperimentRun sorted by recall@10
        """
        configs = grid_config.all_configs()
        print(f"🔬 [GridSearch] Running {len(configs)} configurations...")
        
        runs = []
        for i, config in enumerate(configs):
            print(f"  [{i+1}/{len(configs)}] weights=({config.deterministic_weight:.1f}, {config.semantic_weight:.1f})")
            run = self.run_single(config, save_results=False)
            runs.append(run)
        
        # Sort by recall@10 (descending)
        runs.sort(key=lambda r: r.metrics.avg_recall_at_k.get(10, 0), reverse=True)
        
        if save_results:
            self._save_grid_search(runs)
        
        return runs
    
    def compare_models(
        self,
        model_names: List[str],
        base_config: Optional[HybridConfig] = None,
    ) -> List[ExperimentRun]:
        """
        Compare different expansion models.
        
        Args:
            model_names: List of model names from EXPANSION_MODELS
            base_config: Base config to modify (defaults to balanced weights)
            
        Returns:
            List of ExperimentRun sorted by recall@10
        """
        base = base_config or HybridConfig()
        
        runs = []
        for model_name in model_names:
            if model_name not in EXPANSION_MODELS:
                print(f"⚠️ Unknown model: {model_name}, skipping")
                continue
            
            config = base.with_model(model_name)
            print(f"🧪 [ModelCompare] Testing {model_name}...")
            run = self.run_single(config, save_results=False)
            runs.append(run)
        
        # Sort by recall@10
        runs.sort(key=lambda r: r.metrics.avg_recall_at_k.get(10, 0), reverse=True)
        
        self._save_model_comparison(runs)
        
        return runs
    
    def _save_run(self, run: ExperimentRun) -> None:
        """Save a single run to output directory."""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        path = self.output_dir / f"{run.run_id}.json"
        
        with open(path, "w") as f:
            json.dump(run.to_dict(), f, indent=2)
        
        print(f"💾 Saved: {path}")
    
    def _save_grid_search(self, runs: List[ExperimentRun]) -> None:
        """Save grid search results."""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        path = self.output_dir / f"grid-search-{timestamp}.json"
        
        data = {
            "type": "grid_search",
            "timestamp": timestamp,
            "run_count": len(runs),
            "best_config": runs[0].to_dict()["config"] if runs else None,
            "runs": [r.to_dict() for r in runs],
        }
        
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
        
        print(f"💾 Saved grid search: {path}")
    
    def _save_model_comparison(self, runs: List[ExperimentRun]) -> None:
        """Save model comparison results."""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        path = self.output_dir / f"model-compare-{timestamp}.json"
        
        data = {
            "type": "model_comparison",
            "timestamp": timestamp,
            "models_tested": [r.config.expansion_model for r in runs],
            "runs": [r.to_dict() for r in runs],
        }
        
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
        
        print(f"💾 Saved model comparison: {path}")


def load_queries_from_json(path: Path) -> List[ExperimentQuery]:
    """
    Load experiment queries from JSON file.
    
    Supports two formats:
    1. {"queries": [...]} - list of query objects
    2. [...] - direct list of query objects
    
    Each query object should have:
    - id/query_id: unique identifier
    - query_text/question: the query string
    - gold_chunk_ids/expected_chunk_ids: list of expected chunk IDs
    """
    with open(path) as f:
        data = json.load(f)
    
    if isinstance(data, list):
        queries_raw = data
    elif isinstance(data, dict) and "queries" in data:
        queries_raw = data["queries"]
    else:
        raise ValueError(f"Unexpected format in {path}")
    
    return [ExperimentQuery.from_dict(q) for q in queries_raw]


def print_run_summary(run: ExperimentRun) -> None:
    """Print a summary of an experiment run."""
    m = run.metrics
    
    print(f"\n{'='*50}")
    print(f"Run: {run.run_id}")
    print(f"Model: {run.config.expansion_model}")
    print(f"Weights: det={run.config.deterministic_weight:.1f}, sem={run.config.semantic_weight:.1f}")
    print(f"Duration: {run.duration_seconds:.1f}s")
    print(f"\nRecall@K:")
    for k in STANDARD_K_VALUES:
        print(f"  @{k:2d}: {m.avg_recall_at_k.get(k, 0):.1%}")
    print(f"\nAttribution:")
    print(f"  Det-only: {m.attribution.deterministic_only}")
    print(f"  Sem-only: {m.attribution.semantic_only}")
    print(f"  Both: {m.attribution.both}")
    print(f"  Missed: {m.attribution.neither}")
    print(f"\nLatency: avg={m.avg_latency_ms:.0f}ms, p95={m.p95_latency_ms:.0f}ms")
    print(f"{'='*50}\n")


def print_grid_search_summary(runs: List[ExperimentRun]) -> None:
    """Print grid search results as a table."""
    print(f"\n{'='*70}")
    print("Grid Search Results (sorted by Recall@10)")
    print(f"{'='*70}")
    print(f"{'Weights':<12} {'R@1':>6} {'R@5':>6} {'R@10':>6} {'R@30':>6} {'Latency':>10}")
    print(f"{'-'*12} {'-'*6} {'-'*6} {'-'*6} {'-'*6} {'-'*10}")
    
    for run in runs[:10]:  # Top 10
        m = run.metrics
        weights = f"({run.config.deterministic_weight:.1f},{run.config.semantic_weight:.1f})"
        r1 = f"{m.avg_recall_at_k.get(1, 0):.1%}"
        r5 = f"{m.avg_recall_at_k.get(5, 0):.1%}"
        r10 = f"{m.avg_recall_at_k.get(10, 0):.1%}"
        r30 = f"{m.avg_recall_at_k.get(30, 0):.1%}"
        lat = f"{m.avg_latency_ms:.0f}ms"
        print(f"{weights:<12} {r1:>6} {r5:>6} {r10:>6} {r30:>6} {lat:>10}")
    
    print(f"{'='*70}\n")
