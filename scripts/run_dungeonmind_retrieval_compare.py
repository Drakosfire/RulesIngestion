"""Compare the bounded DungeonMind cited path with RulesIngestion BM25."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from dungeonmind.infrastructure.postgres.database import PostgresDatabase
from dungeonmind.infrastructure.postgres.vnext_knowledge import (
    PostgresKnowledgeRevisionRepository,
)

from retrieval_lab.benchmark_contract import (
    benchmark_query_alignment_summary,
    build_benchmark_contract,
    validate_benchmark_contract,
    write_benchmark_contract,
)
from retrieval_lab.sparse_retrieval import bm25_rank, build_bm25_index
from semantic_lifting.contracts import digest
from semantic_lifting.dungeonmind_export import DUNGEONMIND_REVISION, FIXTURE
from semantic_lifting.dungeonmind_retrieval import (
    load_benchmark,
    pinned_context,
    retrieve,
)


def _metrics(rows: list[dict], key: str, *, top_k: int) -> dict:
    positives = [row for row in rows if row["required_gold"]]
    negatives = [row for row in rows if not row["required_gold"]]
    ranks = []
    for row in positives:
        returned = row[key]["mapped_evidence_unit_ids"]
        ranks.append(
            next(
                (
                    i
                    for i, unit_id in enumerate(returned[:top_k], 1)
                    if unit_id in row["required_gold"]
                ),
                None,
            )
        )
    return {
        "queries": len(rows),
        "grounding_queries": len(positives),
        "required_full_set_hit_at_k": sum(
            set(row["required_gold"])
            <= set(row[key]["mapped_evidence_unit_ids"][:top_k])
            for row in positives
        ),
        "mrr": round(
            sum(1 / rank if rank else 0 for rank in ranks) / len(positives), 6
        ),
        "no_result_correct": sum(
            not row[key]["mapped_evidence_unit_ids"] for row in negatives
        ),
        "no_result_total": len(negatives),
    }


def run(fixture: Path, database_url: str, *, top_k: int = 3) -> dict:
    benchmark_path = fixture / "retrieval_benchmark.json"
    benchmark = load_benchmark(benchmark_path)
    witness = json.loads((fixture / "dungeonmind_publication_witness.json").read_text())
    repository = PostgresKnowledgeRevisionRepository(PostgresDatabase(database_url))
    context = pinned_context(repository, witness, fixture=fixture)
    units = json.loads((fixture / "stageB.evidence_units.json").read_text())["units"]
    corpus_ids = [unit["unit_id"] for unit in units]
    baseline = build_bm25_index([unit["text"] for unit in units])
    queries = benchmark["queries"]
    baseline_ranks, baseline_scores = bm25_rank(
        baseline, corpus_ids, queries, max_k=top_k
    )
    rows = []
    for query, ranked_ids, scores in zip(
        queries, baseline_ranks, baseline_scores, strict=True
    ):
        dm = retrieve(context, query["question"], top_k=top_k)
        rows.append(
            {
                "query_id": query["id"],
                "question": query["question"],
                "required_gold": query["required_gold"],
                "dungeonmind": dm,
                "baseline": {
                    "mapped_evidence_unit_ids": ranked_ids,
                    "scores": scores,
                    "method": "retrieval_lab.sparse_retrieval.BM25Okapi",
                },
            }
        )
    source = witness["source_artifact"]
    source_revision = witness["source_revision"]
    expected_evidence = witness["evidence_ref"]
    citation_mapping_exact = all(
        hit["evidence_unit_id"] in corpus_ids
        and hit["source_artifact_id"] == source["source_artifact_id"]
        and hit["source_revision_id"] == source_revision["source_revision_id"]
        and hit["evidence_ref_id"] == expected_evidence["evidence_ref_id"]
        and hit["source_uri"] == source["uri"]
        for row in rows
        for hit in row["dungeonmind"]["hits"]
    )
    repeated = [retrieve(context, query["question"], top_k=top_k) for query in queries]
    stable_dm = [
        {k: v for k, v in row["dungeonmind"].items() if k != "latency_ms"}
        for row in rows
    ]
    repeated_stable = [
        {k: v for k, v in item.items() if k != "latency_ms"} for item in repeated
    ]
    deterministic = stable_dm == repeated_stable
    if not deterministic:
        raise ValueError("Frozen DungeonMind retrieval membership/order changed")
    alignment = benchmark_query_alignment_summary(queries, corpus_ids=corpus_ids)
    benchmark_sha = hashlib.sha256(benchmark_path.read_bytes()).hexdigest()
    corpus_fingerprint = digest(units)
    run_id = digest(
        {
            "benchmark_sha": benchmark_sha,
            "revision_id": witness["published_revision_id"],
        }
    )
    with TemporaryDirectory(prefix="rlh04-contract-") as folder:
        contract_path = Path(folder) / "retrieval_benchmark.contract.json"
        contract = build_benchmark_contract(
            benchmark_path=benchmark_path,
            query_count=len(queries),
            run_id=run_id,
            substrate_version=benchmark["metadata"]["substrate_version"],
            corpus_fingerprint=corpus_fingerprint,
            corpus_unit_count=len(units),
            alignment_summary=alignment,
            benchmark_kind="manual",
        )
        write_benchmark_contract(contract_path, contract)
        validation = validate_benchmark_contract(
            benchmark_path=benchmark_path,
            contract_path=contract_path,
            query_count=len(queries),
            run_id=run_id,
            substrate_version=benchmark["metadata"]["substrate_version"],
            corpus_fingerprint=corpus_fingerprint,
            alignment_summary=alignment,
        )
    if not validation["valid"]:
        raise ValueError(
            f"Retrieval Lab benchmark contract invalid: {validation['errors']}"
        )
    dm_metrics = _metrics(rows, "dungeonmind", top_k=top_k)
    baseline_metrics = _metrics(rows, "baseline", top_k=top_k)
    canonical = [
        row
        for row in rows
        if row["query_id"] in {"ground_occ_2024_001", "ground_occ_2024_002"}
    ]
    product_ready = (
        all(
            set(row["required_gold"])
            <= set(row["dungeonmind"]["mapped_evidence_unit_ids"][:top_k])
            for row in canonical
        )
        and dm_metrics["no_result_correct"] == dm_metrics["no_result_total"]
        and deterministic
        and validation["valid"]
        and citation_mapping_exact
    )
    stable = {
        "schema_version": "rlh-04-retrieval-comparison-v1",
        "dungeonmind_commit": DUNGEONMIND_REVISION,
        "space_id": witness["space_id"],
        "revision_id": witness["published_revision_id"],
        "semantic_profile": "rules.occupancy@1",
        "benchmark_sha256": benchmark_sha,
        "corpus_fingerprint": corpus_fingerprint,
        "run_id": run_id,
        "top_k": top_k,
        "benchmark_contract_valid": validation["valid"],
        "benchmark_alignment": alignment,
        "repeated_run_deterministic": deterministic,
        "citation_mapping_exact": citation_mapping_exact,
        "metrics": {"dungeonmind": dm_metrics, "baseline_bm25": baseline_metrics},
        "product_ready": product_ready,
        "comparison_limit": "one exact SRD EvidenceUnit; baseline is RulesIngestion BM25, not the unavailable full PHB dense/hybrid corpus",
        "rows": [
            {
                **row,
                "dungeonmind": {
                    k: v for k, v in row["dungeonmind"].items() if k != "latency_ms"
                },
            }
            for row in rows
        ],
    }
    return {
        **stable,
        "run_digest": digest(stable),
        "latency_ms": {
            row["query_id"]: row["dungeonmind"]["latency_ms"] for row in rows
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=FIXTURE)
    parser.add_argument("--top-k", type=int, default=3)
    args = parser.parse_args()
    url = os.environ.get("DUNGEONMIND_DATABASE_URL")
    if not url:
        raise ValueError("DUNGEONMIND_DATABASE_URL is required")
    report = run(args.fixture, url, top_k=args.top_k)
    output = args.fixture / "retrieval_comparison.json"
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(
        json.dumps(
            {
                "product_ready": report["product_ready"],
                "run_digest": report["run_digest"],
                "metrics": report["metrics"],
            }
        )
    )


if __name__ == "__main__":
    main()
