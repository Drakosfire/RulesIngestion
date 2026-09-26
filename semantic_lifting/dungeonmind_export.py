"""Publish the reviewed occupancy package through generic DungeonMind vNext."""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from dungeonmind.application.vnext.authority import revision_from_command
from dungeonmind.application.vnext.builder import build_parsed_knowledge_revision
from dungeonmind.application.vnext.materialization import (
    NATIVE_VNEXT_GRAPH_SCHEMA,
    GovernedPublicationIdentity,
    decode_native_graph_payload,
    encode_native_graph_payload,
)
from dungeonmind.application.vnext.prospective import publish_prospective_contribution
from dungeonmind.contracts.semantic_profile import SemanticProfileRef
from dungeonmind.contracts.vnext.common import (
    EpistemicBasis,
    KnowledgeStanding,
    PublicVisibility,
    TimelessTemporalScope,
)
from dungeonmind.contracts.vnext.contribution import ContributionDisposition
from dungeonmind.contracts.vnext.domain import (
    AssertionMetadata,
    DomainContractDescriptor,
    DomainContractRef,
    LiteralValue,
    OpenPredicateNamespace,
    SemanticProfileDescriptorV3,
)
from dungeonmind.contracts.vnext.knowledge import PublishKnowledgeRevisionCommand
from dungeonmind.contracts.vnext.prospective import (
    ProspectiveCreateAssertion,
    ProspectiveCreateEntity,
    ProspectiveEntityRef,
    ProspectiveKnowledgeContribution,
)
from dungeonmind.contracts.vnext.source import (
    EvidenceRefV3,
    SourceArtifactV3,
    SourceRevisionV2,
)
from dungeonmind.domain.canonical import canonical_sha256

from semantic_lifting.occupancy import load_exact_evidence

DUNGEONMIND_REVISION = "54a419f99057d96e0c4e7620d8bd8ccc6816fb62"
SPACE_ID = "space:rules-occupancy-srd-5-2-1-v1"
CREATED_AT = datetime(2026, 9, 26, tzinfo=UTC)
FIXTURE = Path(__file__).resolve().parents[1] / "evals/semantic_lifting/occupancy_v1"


def descriptors() -> tuple[DomainContractDescriptor, SemanticProfileDescriptorV3]:
    domain = DomainContractDescriptor(
        domain_id="rules.occupancy",
        domain_revision="1",
        claim_modes=["rules:source-grounded"],
        admission_policy_id="rules.reviewed-human-gold-v1",
    )
    profile = SemanticProfileDescriptorV3(
        profile_id="rules.occupancy",
        profile_revision="1",
        term_namespaces=["rules", "rules.occupancy"],
        open_predicate_namespaces=[
            OpenPredicateNamespace(
                namespace="rules.occupancy", allowed_value_kinds=["literal"]
            )
        ],
    )
    return domain, profile


def source_contracts(
    fixture: Path = FIXTURE,
) -> tuple[SourceArtifactV3, SourceRevisionV2, EvidenceRefV3]:
    manifest = json.loads((fixture / "source_manifest.json").read_text())
    source_sha = manifest["source_sha256"]
    evidence_id = manifest["evidence_unit_id"]
    artifact_id = f"art:srd-5-2-1:{source_sha}"
    revision_id = f"srcrev:srd-5-2-1:{source_sha}"
    artifact = SourceArtifactV3(
        source_artifact_id=artifact_id,
        source_classification="rules:srd",
        current_revision_id=revision_id,
        authority="primary",
        visibility=PublicVisibility(),
        status="active",
        uri=manifest["source_url"],
        foreign_refs=[f"rulesingestion:evidence-unit:{evidence_id}"],
    )
    revision = SourceRevisionV2(
        source_revision_id=revision_id,
        source_artifact_id=artifact_id,
        content_sha256=source_sha,
        body_storage="external:official-srd-pdf",
        locator=f"printed-page:{manifest['printed_page']};section:{manifest['section']}",
        created_at=CREATED_AT,
    )
    evidence = EvidenceRefV3(
        evidence_ref_id=f"ev:rulesingestion:{evidence_id}",
        source_artifact_id=artifact_id,
        source_revision_id=revision_id,
        evidence_role="support",
        can_open_source=True,
        can_highlight_span=False,
        uri=manifest["source_url"],
        locator=f"printed-page:{manifest['printed_page']};section:{manifest['section']}",
        source_locator=f"rulesingestion:evidence-unit:{evidence_id}",
    )
    return artifact, revision, evidence


def _accepted_candidates(fixture: Path) -> tuple[list[dict[str, Any]], list[str]]:
    package = json.loads((fixture / "candidate_package.json").read_text())
    gold = json.loads((fixture / "human_gold.json").read_text())["decisions"]
    exact_ids = {unit.unit_id for unit in load_exact_evidence(fixture)}
    candidates = package["candidates"]
    if {item["candidate_id"] for item in candidates} != set(gold):
        raise ValueError("Human gold does not cover the candidate package")
    if any(
        not item["evidence_unit_ids"] or not set(item["evidence_unit_ids"]) <= exact_ids
        for item in candidates
    ):
        raise ValueError("Candidate has missing or inexact evidence")
    accepted = [
        item
        for item in candidates
        if gold[item["candidate_id"]]["disposition"] == "accept"
    ]
    excluded = [item["candidate_id"] for item in candidates if item not in accepted]
    if not accepted:
        raise ValueError("No accepted candidates")
    return accepted, excluded


def publish_occupancy(fixture: Path, repository: Any) -> dict[str, Any]:
    """Create one fresh space, publish accepted claims, and reopen exact authority."""
    accepted, excluded = _accepted_candidates(fixture)
    domain, profile = descriptors()
    artifact, revision, evidence = source_contracts(fixture)
    domain_ref = DomainContractRef(
        domain_id=domain.domain_id,
        domain_revision=domain.domain_revision,
        descriptor_sha256=canonical_sha256(domain.model_dump(mode="json")),
    )
    profile_ref = SemanticProfileRef(
        profile_id=profile.profile_id,
        profile_revision=profile.profile_revision,
        descriptor_sha256=canonical_sha256(profile.model_dump(mode="json")),
    )
    genesis_command = PublishKnowledgeRevisionCommand(
        space_id=SPACE_ID,
        operation_ids=["op:rules-occupancy-genesis-v1"],
        graph_schema=NATIVE_VNEXT_GRAPH_SCHEMA,
        graph_payload=encode_native_graph_payload(
            entities={},
            assertions={},
            aliases={},
            evidence={evidence.evidence_ref_id: evidence},
        ),
        domain_contract_ref=domain_ref,
        semantic_profile_ref=profile_ref,
        created_at=CREATED_AT,
    )
    existing_head = repository.get_head(SPACE_ID)
    if existing_head is None:
        genesis = repository.publish_revision(genesis_command)
    else:
        genesis = repository.get_revision(
            SPACE_ID, revision_from_command(genesis_command).revision_id
        )
        if genesis is None:
            raise ValueError("Existing space lacks the exact expected genesis")
    parent = build_parsed_knowledge_revision(
        revision=genesis.revision,
        decoded_content=decode_native_graph_payload(genesis.graph_payload),
    )
    items: list[Any] = []
    dispositions: list[ContributionDisposition] = []
    for candidate in accepted:
        candidate_id = candidate["candidate_id"]
        entity_op = f"entity:{candidate_id}"
        assertion_op = f"assertion:{candidate_id}"
        entity_item = f"create-entity:{candidate_id}"
        assertion_item = f"create-assertion:{candidate_id}"
        items.append(
            ProspectiveCreateEntity(item_id=entity_item, client_op_id=entity_op)
        )
        items.append(
            ProspectiveCreateAssertion(
                item_id=assertion_item,
                client_op_id=assertion_op,
                subject=ProspectiveEntityRef(client_op_id=entity_op),
                predicate=f"rules.occupancy:{candidate['kind']}",
                value=LiteralValue(
                    value=" ".join(
                        (
                            candidate["subject"],
                            candidate["predicate"],
                            candidate["value"],
                        )
                    )
                ),
                metadata=AssertionMetadata(
                    visibility=PublicVisibility(),
                    epistemic_basis=EpistemicBasis.ASSERTED,
                    claim_mode="rules:source-grounded",
                    standing=KnowledgeStanding.ESTABLISHED,
                    evidence_ref_ids=[evidence.evidence_ref_id],
                    temporal_scope=TimelessTemporalScope(),
                ),
            )
        )
        dispositions.extend(
            (
                ContributionDisposition(item_id=entity_item, disposition="accepted"),
                ContributionDisposition(item_id=assertion_item, disposition="accepted"),
            )
        )
    publication_id = f"publication:rules-occupancy:{canonical_sha256([item['candidate_id'] for item in accepted])}"
    result = publish_prospective_contribution(
        parent=parent,
        prospective_contribution=ProspectiveKnowledgeContribution(
            contribution_id="contribution:rules-occupancy-reviewed-v1",
            space_id=SPACE_ID,
            producer="producer:rulesingestion",
            produced_at=CREATED_AT,
            source_refs=[revision.source_revision_id],
            status="finalized",
            items=items,
        ),
        dispositions=dispositions,
        publication=GovernedPublicationIdentity(
            operation_ids=("op:rules-occupancy-reviewed-v1",),
            created_at=CREATED_AT,
            expected_parent_revision_id=parent.revision_id,
        ),
        publication_id=publication_id,
        domain_contract=domain,
        semantic_profile=profile,
        repository=repository,
    )
    child_id = result.publication_receipt.published_revision_id
    reopened = repository.get_revision(SPACE_ID, child_id)
    head = repository.get_head(SPACE_ID)
    if reopened is None or head is None or head.head_revision_id != child_id:
        raise ValueError("Published revision failed exact reopen")
    payload = reopened.graph_payload
    result_ids = {
        binding.client_op_id: binding.durable_id
        for binding in result.prospective_result.results
    }
    if len(payload["assertions"]) != len(accepted):
        raise ValueError("Accepted assertion count drift")
    if {item["metadata"]["evidence_ref_ids"][0] for item in payload["assertions"]} != {
        evidence.evidence_ref_id
    }:
        raise ValueError("Published assertion lost exact evidence")
    if any(candidate_id in json.dumps(payload) for candidate_id in excluded):
        raise ValueError("Excluded candidate published")
    return {
        "schema_version": "rlh-03-publication-witness-v1",
        "dungeonmind_revision": DUNGEONMIND_REVISION,
        "space_id": SPACE_ID,
        "genesis_revision_id": genesis.revision.revision_id,
        "published_revision_id": child_id,
        "publication_id": publication_id,
        "publication_receipt": result.publication_receipt.model_dump(mode="json"),
        "source_artifact": artifact.model_dump(mode="json"),
        "source_revision": revision.model_dump(mode="json"),
        "evidence_ref": evidence.model_dump(mode="json"),
        "accepted_candidate_ids": [item["candidate_id"] for item in accepted],
        "excluded_candidate_ids": excluded,
        "result_bindings": result_ids,
        "reopened_payload_sha256": canonical_sha256(payload),
        "reopened_assertions": payload["assertions"],
        "reopened_evidence": payload["evidence"],
    }
