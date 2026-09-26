"""Bounded cited retrieval from one exact DungeonMind occupancy revision."""

from __future__ import annotations

import json
from pathlib import Path
from time import perf_counter
from typing import Any

from dungeonmind.application.vnext.admission import AlwaysAdmitPolicy
from dungeonmind.application.vnext.builder import build_parsed_knowledge_revision
from dungeonmind.application.vnext.evidence_reads import EvidenceReadService
from dungeonmind.application.vnext.materialization import decode_native_graph_payload
from dungeonmind.application.vnext.provenance import InMemoryKnowledgeSourceReader
from dungeonmind.application.vnext.read_context import KnowledgeReadContext
from dungeonmind.application.vnext.search import SearchReadService
from dungeonmind.contracts.vnext.common import KnowledgeStanding, ScopeSelector
from dungeonmind.contracts.vnext.projection import ProjectionRequest

from semantic_lifting.dungeonmind_export import (
    DUNGEONMIND_REVISION,
    SPACE_ID,
    descriptors,
    source_contracts,
)


def pinned_context(
    repository: Any, witness: dict[str, Any], *, fixture: Path
) -> KnowledgeReadContext:
    if (
        witness["dungeonmind_revision"] != DUNGEONMIND_REVISION
        or witness["space_id"] != SPACE_ID
    ):
        raise ValueError("Publication witness has a different DungeonMind pin or space")
    stored = repository.get_revision(SPACE_ID, witness["published_revision_id"])
    if (
        stored is None
        or stored.graph_payload_sha256 != witness["reopened_payload_sha256"]
    ):
        raise ValueError("Exact published revision is missing or changed")
    parsed = build_parsed_knowledge_revision(
        revision=stored.revision,
        decoded_content=decode_native_graph_payload(stored.graph_payload),
    )
    domain, profile = descriptors()
    artifact, revision, _evidence = source_contracts(fixture)
    return KnowledgeReadContext(
        parsed=parsed,
        request=ProjectionRequest(
            space_id=SPACE_ID,
            revision_id=witness["published_revision_id"],
            scope_selector=ScopeSelector(include_unscoped=True),
            standing_selector=[KnowledgeStanding.ESTABLISHED],
        ),
        domain_contract=domain,
        semantic_profile=profile,
        domain_policy=AlwaysAdmitPolicy(policy_id=domain.admission_policy_id),
        source_reader=InMemoryKnowledgeSourceReader(
            artifacts={artifact.source_artifact_id: artifact},
            revisions={revision.source_revision_id: revision},
        ),
    )


def retrieve(
    context: KnowledgeReadContext, query: str, *, top_k: int = 3
) -> dict[str, Any]:
    started = perf_counter()
    search = SearchReadService().search_entities(context, query, limit=top_k)
    evidence_reads = EvidenceReadService()
    hits: list[dict[str, Any]] = []
    mapped_ids: list[str] = []
    for rank, hit in enumerate(search.hits, start=1):
        for assertion in hit.admitted_match_assertions:
            support = evidence_reads.get_assertion_evidence(
                context, assertion.assertion_id
            )
            if not support.available or support.completeness.status != "complete":
                continue
            for evidence in support.evidence:
                marker = "rulesingestion:evidence-unit:"
                if (
                    not evidence.source_locator
                    or not evidence.source_locator.startswith(marker)
                ):
                    raise ValueError(
                        "Admitted evidence has no reversible RulesIngestion mapping"
                    )
                unit_id = evidence.source_locator.removeprefix(marker)
                if unit_id not in mapped_ids:
                    mapped_ids.append(unit_id)
                hits.append(
                    {
                        "rank": rank,
                        "entity_id": hit.entity.entity_id,
                        "assertion_id": assertion.assertion_id,
                        "evidence_ref_id": evidence.evidence_ref_id,
                        "evidence_unit_id": unit_id,
                        "source_artifact_id": evidence.source_artifact_id,
                        "source_revision_id": evidence.source_revision_id,
                        "source_uri": evidence.uri,
                        "search_score": hit.deterministic_score,
                        "search_match_kinds": list(hit.match_kinds),
                        "search_digest": search.result_digest,
                        "evidence_digest": support.result_digest,
                        "admission": "admitted",
                    }
                )
    return {
        "query": query,
        "revision_id": context.parsed.revision_id,
        "mapped_evidence_unit_ids": mapped_ids,
        "hits": hits,
        "completeness": search.completeness.status,
        "failure_reason": search.completeness.reason,
        "latency_ms": round((perf_counter() - started) * 1000, 3),
    }


def load_benchmark(path: Path) -> dict[str, Any]:
    benchmark = json.loads(path.read_text())
    queries = benchmark["queries"]
    if benchmark["metadata"]["query_count"] != len(queries):
        raise ValueError("Query count mismatch")
    ids = [query["id"] for query in queries]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate benchmark query ID")
    return benchmark
