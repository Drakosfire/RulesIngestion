"""
Metrics for hybrid retrieval experiments.

Provides:
- Recall@K metrics at multiple K values
- Full Recall@K (all gold chunks found)
- Per-path attribution (deterministic-only, semantic-only, both, neither)
- Expansion quality metrics
- Weight sensitivity analysis
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set, Tuple

from traversal.hybrid_retriever import HybridRetrievalResult, RetrievalDiagnostics
from traversal.reranker import RerankResult


# Standard K values for recall measurement
STANDARD_K_VALUES = [1, 2, 5, 10, 20, 30]


@dataclass
class RecallAtK:
    """
    Recall@K for a single query.
    
    Recall@K = fraction of gold chunks that appear in top-K results.
    """
    k_values: Dict[int, float] = field(default_factory=dict)
    gold_count: int = 0
    
    def at(self, k: int) -> float:
        """Get recall at specific K."""
        return self.k_values.get(k, 0.0)
    
    @property
    def best_k(self) -> int:
        """K value where recall first reaches 1.0, or highest K."""
        for k in sorted(self.k_values.keys()):
            if self.k_values[k] >= 1.0:
                return k
        return max(self.k_values.keys()) if self.k_values else 0


@dataclass
class FullRecallAtK:
    """
    Full Recall@K = 1 if ALL gold chunks appear in top-K, else 0.
    
    More stringent than regular Recall@K.
    """
    k_values: Dict[int, bool] = field(default_factory=dict)
    gold_count: int = 0
    
    def at(self, k: int) -> bool:
        """Check if full recall achieved at K."""
        return self.k_values.get(k, False)


@dataclass
class AttributionMetrics:
    """
    Metrics for per-path attribution analysis.
    
    Tracks where gold chunks came from:
    - deterministic_only: Found only by deterministic search
    - semantic_only: Found only by semantic search
    - both: Found by both paths
    - neither: Not found by either path
    """
    deterministic_only: int = 0
    semantic_only: int = 0
    both: int = 0
    neither: int = 0
    
    gold_count: int = 0
    gold_found: int = 0
    
    @property
    def deterministic_contribution(self) -> float:
        """Fraction of gold found that came from deterministic (including both)."""
        found = self.deterministic_only + self.both
        return found / max(1, self.gold_found)
    
    @property
    def semantic_contribution(self) -> float:
        """Fraction of gold found that came from semantic (including both)."""
        found = self.semantic_only + self.both
        return found / max(1, self.gold_found)
    
    @property
    def exclusive_deterministic(self) -> float:
        """Fraction found ONLY by deterministic (semantic would have missed)."""
        return self.deterministic_only / max(1, self.gold_found)
    
    @property
    def exclusive_semantic(self) -> float:
        """Fraction found ONLY by semantic (deterministic would have missed)."""
        return self.semantic_only / max(1, self.gold_found)


@dataclass
class ExpansionQualityMetrics:
    """
    Metrics for query expansion quality.
    
    Measures:
    - Term coverage: How many expanded terms found chunks
    - Precision: Fraction of chunks that are gold
    - Marginal value: Unique gold chunks per term
    - Redundancy: How much terms overlap
    """
    total_terms: int = 0
    terms_with_hits: int = 0
    term_hit_rate: float = 0.0
    
    # How many unique chunks found
    unique_chunks: int = 0
    
    # Gold chunk analysis
    gold_chunks_found: int = 0
    precision: float = 0.0  # gold_found / unique_chunks
    
    # Per-term marginal value
    terms_contributing_gold: int = 0
    avg_gold_per_term: float = 0.0
    
    # Redundancy
    avg_term_overlap: float = 0.0  # Average shared chunks between terms


@dataclass
class WeightSensitivityMetrics:
    """
    Metrics for weight sensitivity analysis.
    
    Compare results at different weight settings to understand
    how sensitive the system is to weight tuning.
    """
    weight_configs: List[Tuple[float, float]] = field(default_factory=list)
    recall_by_weight: Dict[Tuple[float, float], Dict[int, float]] = field(default_factory=dict)
    
    # Rank shift when weights change
    avg_rank_shift: float = 0.0
    max_rank_shift: int = 0
    
    # Recall delta from baseline
    recall_deltas: Dict[int, float] = field(default_factory=dict)


@dataclass
class ExperimentMetrics:
    """
    Aggregated metrics for an experiment run.
    
    Summarizes performance across all queries in a batch.
    """
    # Query counts
    total_queries: int = 0
    queries_with_gold: int = 0
    
    # Recall@K (averaged across queries)
    avg_recall_at_k: Dict[int, float] = field(default_factory=dict)
    
    # Full Recall@K (fraction of queries achieving full recall)
    full_recall_rate_at_k: Dict[int, float] = field(default_factory=dict)
    
    # Attribution (aggregated)
    attribution: AttributionMetrics = field(default_factory=AttributionMetrics)
    
    # Expansion quality (averaged)
    avg_expansion: ExpansionQualityMetrics = field(default_factory=ExpansionQualityMetrics)
    
    # Timing
    avg_latency_ms: float = 0.0
    p50_latency_ms: float = 0.0
    p95_latency_ms: float = 0.0
    
    # Model info
    expansion_model: str = ""
    weights: Tuple[float, float] = (0.5, 0.5)
    
    # Candidate set size
    avg_candidate_size: float = 0.0


def compute_recall_at_k(
    result: HybridRetrievalResult,
    gold_chunk_ids: Set[str],
    k_values: List[int] = STANDARD_K_VALUES,
) -> RecallAtK:
    """
    Compute Recall@K for a single retrieval result.
    
    Args:
        result: HybridRetrievalResult
        gold_chunk_ids: Set of expected correct chunk IDs
        k_values: K values to compute recall at
        
    Returns:
        RecallAtK with recall values at each K
    """
    recall = RecallAtK(gold_count=len(gold_chunk_ids))
    
    for k in k_values:
        top_k_ids = set(result.get_chunk_ids(k))
        hits = len(top_k_ids & gold_chunk_ids)
        recall.k_values[k] = hits / max(1, len(gold_chunk_ids))
    
    return recall


def compute_full_recall_at_k(
    result: HybridRetrievalResult,
    gold_chunk_ids: Set[str],
    k_values: List[int] = STANDARD_K_VALUES,
) -> FullRecallAtK:
    """
    Compute Full Recall@K (all gold chunks found) for a single result.
    
    Args:
        result: HybridRetrievalResult
        gold_chunk_ids: Set of expected correct chunk IDs
        k_values: K values to check
        
    Returns:
        FullRecallAtK with boolean at each K
    """
    full_recall = FullRecallAtK(gold_count=len(gold_chunk_ids))
    
    for k in k_values:
        top_k_ids = set(result.get_chunk_ids(k))
        # Full recall means ALL gold chunks are in top-K
        full_recall.k_values[k] = gold_chunk_ids.issubset(top_k_ids)
    
    return full_recall


def compute_attribution_metrics(
    result: HybridRetrievalResult,
    gold_chunk_ids: Set[str],
) -> AttributionMetrics:
    """
    Compute per-path attribution for gold chunks.
    
    Analyzes whether gold chunks came from:
    - Deterministic search only
    - Semantic search only
    - Both paths
    - Neither path (not found)
    
    Args:
        result: HybridRetrievalResult
        gold_chunk_ids: Set of expected correct chunk IDs
        
    Returns:
        AttributionMetrics
    """
    metrics = AttributionMetrics(gold_count=len(gold_chunk_ids))
    
    # Get gold analysis from diagnostics
    gold_analysis = result.diagnostics.gold_analysis
    if gold_analysis:
        metrics.deterministic_only = gold_analysis.get("gold_from_deterministic_only", 0)
        metrics.semantic_only = gold_analysis.get("gold_from_semantic_only", 0)
        metrics.both = gold_analysis.get("gold_from_both", 0)
        metrics.neither = gold_analysis.get("gold_from_neither", 0)
        metrics.gold_found = gold_analysis.get("gold_found", 0)
    else:
        # Compute from rerank result if available
        if result.rerank_result:
            result_chunk_ids = set(result.get_chunk_ids())
            for chunk_id in gold_chunk_ids:
                if chunk_id in result_chunk_ids:
                    # Find which path it came from
                    for ranked in result.ranked_chunks:
                        if ranked.chunk_id == chunk_id:
                            if ranked.found_by == "deterministic":
                                metrics.deterministic_only += 1
                            elif ranked.found_by == "semantic":
                                metrics.semantic_only += 1
                            elif ranked.found_by == "both":
                                metrics.both += 1
                            metrics.gold_found += 1
                            break
                else:
                    metrics.neither += 1
    
    return metrics


def compute_expansion_quality_metrics(
    result: HybridRetrievalResult,
    gold_chunk_ids: Set[str],
) -> ExpansionQualityMetrics:
    """
    Compute expansion quality metrics.
    
    Args:
        result: HybridRetrievalResult
        gold_chunk_ids: Set of expected correct chunk IDs
        
    Returns:
        ExpansionQualityMetrics
    """
    diag = result.diagnostics
    
    metrics = ExpansionQualityMetrics(
        total_terms=len(diag.expanded_terms),
        terms_with_hits=diag.terms_with_hits,
        term_hit_rate=diag.term_hit_rate,
        unique_chunks=diag.deterministic_chunks_found,
    )
    
    # Compute gold chunk analysis
    result_chunk_ids = set(result.get_chunk_ids())
    gold_found = len(result_chunk_ids & gold_chunk_ids)
    metrics.gold_chunks_found = gold_found
    metrics.precision = gold_found / max(1, metrics.unique_chunks)
    
    # Per-term analysis would require access to term_results
    # For now, estimate based on hit rate
    if result.parallel_search_result:
        term_results = result.parallel_search_result.term_results
        terms_with_gold = 0
        total_gold_hits = 0
        
        for tr in term_results:
            if tr.chunk_ids & gold_chunk_ids:
                terms_with_gold += 1
                total_gold_hits += len(tr.chunk_ids & gold_chunk_ids)
        
        metrics.terms_contributing_gold = terms_with_gold
        metrics.avg_gold_per_term = total_gold_hits / max(1, len(term_results))
    
    return metrics


def aggregate_experiment_metrics(
    results: List[HybridRetrievalResult],
    gold_chunk_ids_list: List[Set[str]],
    k_values: List[int] = STANDARD_K_VALUES,
) -> ExperimentMetrics:
    """
    Aggregate metrics across multiple retrieval results.
    
    Args:
        results: List of HybridRetrievalResult
        gold_chunk_ids_list: Corresponding list of gold chunk ID sets
        k_values: K values for recall computation
        
    Returns:
        ExperimentMetrics with aggregated values
    """
    metrics = ExperimentMetrics(
        total_queries=len(results),
        queries_with_gold=sum(1 for g in gold_chunk_ids_list if g),
    )
    
    # Initialize accumulators
    recall_sums: Dict[int, float] = {k: 0.0 for k in k_values}
    full_recall_counts: Dict[int, int] = {k: 0 for k in k_values}
    attribution_totals = AttributionMetrics()
    expansion_totals = ExpansionQualityMetrics()
    latencies: List[float] = []
    candidate_sizes: List[int] = []
    
    for result, gold_ids in zip(results, gold_chunk_ids_list):
        if not gold_ids:
            continue
        
        # Recall@K
        recall = compute_recall_at_k(result, gold_ids, k_values)
        for k, val in recall.k_values.items():
            recall_sums[k] += val
        
        # Full Recall@K
        full_recall = compute_full_recall_at_k(result, gold_ids, k_values)
        for k, achieved in full_recall.k_values.items():
            if achieved:
                full_recall_counts[k] += 1
        
        # Attribution
        attr = compute_attribution_metrics(result, gold_ids)
        attribution_totals.deterministic_only += attr.deterministic_only
        attribution_totals.semantic_only += attr.semantic_only
        attribution_totals.both += attr.both
        attribution_totals.neither += attr.neither
        attribution_totals.gold_count += attr.gold_count
        attribution_totals.gold_found += attr.gold_found
        
        # Expansion quality
        exp = compute_expansion_quality_metrics(result, gold_ids)
        expansion_totals.total_terms += exp.total_terms
        expansion_totals.terms_with_hits += exp.terms_with_hits
        expansion_totals.unique_chunks += exp.unique_chunks
        expansion_totals.gold_chunks_found += exp.gold_chunks_found
        expansion_totals.terms_contributing_gold += exp.terms_contributing_gold
        
        # Timing
        latencies.append(result.diagnostics.total_latency_ms)
        
        # Candidate size
        candidate_sizes.append(result.diagnostics.deterministic_chunks_found)
    
    # Compute averages
    n = max(1, metrics.queries_with_gold)
    
    metrics.avg_recall_at_k = {k: v / n for k, v in recall_sums.items()}
    metrics.full_recall_rate_at_k = {k: v / n for k, v in full_recall_counts.items()}
    
    metrics.attribution = attribution_totals
    
    metrics.avg_expansion = ExpansionQualityMetrics(
        total_terms=expansion_totals.total_terms / n,
        terms_with_hits=expansion_totals.terms_with_hits / n,
        term_hit_rate=expansion_totals.terms_with_hits / max(1, expansion_totals.total_terms),
        unique_chunks=expansion_totals.unique_chunks / n,
        gold_chunks_found=expansion_totals.gold_chunks_found / n,
        precision=expansion_totals.gold_chunks_found / max(1, expansion_totals.unique_chunks),
        terms_contributing_gold=expansion_totals.terms_contributing_gold / n,
    )
    
    if latencies:
        sorted_latencies = sorted(latencies)
        metrics.avg_latency_ms = sum(latencies) / len(latencies)
        metrics.p50_latency_ms = sorted_latencies[len(sorted_latencies) // 2]
        metrics.p95_latency_ms = sorted_latencies[int(len(sorted_latencies) * 0.95)]
    
    if candidate_sizes:
        metrics.avg_candidate_size = sum(candidate_sizes) / len(candidate_sizes)
    
    # Model info from first result
    if results:
        metrics.expansion_model = results[0].diagnostics.expansion_model
    
    return metrics


def format_recall_table(metrics: ExperimentMetrics) -> str:
    """Format recall metrics as a table string."""
    lines = [
        "| K | Recall@K | Full Recall Rate |",
        "|---|----------|------------------|",
    ]
    
    for k in STANDARD_K_VALUES:
        recall = metrics.avg_recall_at_k.get(k, 0.0)
        full_rate = metrics.full_recall_rate_at_k.get(k, 0.0)
        lines.append(f"| {k:2d} | {recall:.1%} | {full_rate:.1%} |")
    
    return "\n".join(lines)


def format_attribution_summary(metrics: ExperimentMetrics) -> str:
    """Format attribution metrics as a summary string."""
    attr = metrics.attribution
    lines = [
        f"Gold chunks found: {attr.gold_found}/{attr.gold_count}",
        f"  - Deterministic only: {attr.deterministic_only} ({attr.exclusive_deterministic:.1%})",
        f"  - Semantic only: {attr.semantic_only} ({attr.exclusive_semantic:.1%})",
        f"  - Both paths: {attr.both}",
        f"  - Neither (missed): {attr.neither}",
    ]
    return "\n".join(lines)
