"""LLM-backed ruleset config generation."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, Optional

from config_profile import RulesetProfile

try:
    from openai import OpenAI
except ImportError as exc:  # pragma: no cover - runtime dependency guard
    raise RuntimeError("openai package is required for LLM config generation.") from exc


DEFAULT_LLM_MODEL = "gpt-4o-mini"
REQUIRED_KEYS = {
    "ruleset_id",
    "doc_signature",
    "version",
    "schema_version",
    "deterministic_rules",
    "nondeterministic_flags",
    "drift_criteria",
}


def build_config_prompt(profile: RulesetProfile) -> str:
    profile_payload = {
        "ruleset_id": profile.ruleset_id,
        "doc_signature": profile.doc_signature,
        "heading_hierarchy": profile.heading_hierarchy,
        "block_type_distribution": profile.block_type_distribution,
        "samples": profile.samples or [],
    }

    schema_hint = {
        "ruleset_id": "string",
        "doc_signature": "string",
        "version": "string (semantic or date)",
        "schema_version": "string",
        "deterministic_rules": {
            "entity_aliases": {"alias": "canonical"},
            "entity_blacklist": ["string"],
            "entity_type_overrides": {"entity_name": "EntityType"},
            "abbreviation_patterns": ["regex string"],
            "graph_edge_weights": {"relation": "float"},
            "graph_relation_patterns": [
                {"relation": "requires", "pattern": "regex string"}
            ],
            "graph_relation_target_limit": "int",
            "graph_chunk_adjacency_limit": "int",
            "graph_skip_relations": ["string"],
            "content_kind_overrides": {"section_or_tag": "content_kind"},
            "high_value_tags": ["string"],
            "merge_spell_blocks": "bool",
            "merge_spell_max_blocks": "int",
            "min_chunk_chars": "int",
            "max_chunk_chars": "int",
            "evaluation_query_type_defaults": {"content_kind": "query_type"},
            "evaluation_query_type_overrides": {"content_kind": "query_type"},
            "evaluation_query_templates": {
                "content_kind": "Prompt with {label}",
                "default": "Prompt with {label}",
            },
            "evaluation_query_max_per_kind": "int",
            "evaluation_paragraph_min_chars": "int",
            "evaluation_hypothetical_answer_max_chars": "int",
            "evaluation_hypothetical_answer_strategy": "first_paragraph|full_text",
            "eval_default_model_id": "string",
            "eval_query_limit": "int",
            "eval_query_seed": "int",
            "eval_document_prefixes": ["string"],
            "eval_best_practice_defaults": {
                "expand_gold": "bool",
                "graph_boost": "float",
                "graph_boost_source": "expected|top",
                "graph_boost_seed_top_n": "int",
                "graph_boost_depth": "int",
                "graph_boost_top_k": "int|null",
                "graph_boost_decay": "float",
            },
            "config_notes": "string",
            "version_tags": ["string"],
        },
        "nondeterministic_flags": ["string"],
        "drift_criteria": {
            "heading_hierarchy": ["string"],
            "block_type_distribution": {"BlockType": "count"},
        },
    }

    return (
        "You are generating a ruleset enrichment configuration. "
        "Return ONLY a valid JSON object matching the schema hint.\n\n"
        f"Schema hint:\n{json.dumps(schema_hint, indent=2)}\n\n"
        "Profile input:\n"
        f"{json.dumps(profile_payload, indent=2)}\n\n"
        "Rules:\n"
        "- Include drift_criteria.heading_hierarchy and drift_criteria.block_type_distribution "
        "matching the profile.\n"
        "- Use nondeterministic_flags as lowercase keywords for paragraph-level LLM targeting.\n"
        "- deterministic_rules.entity_aliases should map aliases to canonical names.\n"
        "- deterministic_rules keys are optional; include only when confident.\n"
        "- deterministic_rules.entity_blacklist: list names to drop from graph.\n"
        "- deterministic_rules.entity_type_overrides: map entity name -> type label.\n"
        "- deterministic_rules.abbreviation_patterns: regexes to detect abbreviation/canonical pairs.\n"
        "- deterministic_rules.graph_edge_weights: relation -> float weight (1.0 default).\n"
        "- deterministic_rules.graph_relation_patterns: add relation + regex pairs.\n"
        "- deterministic_rules.graph_relation_target_limit: max matches per relation per chunk.\n"
        "- deterministic_rules.graph_chunk_adjacency_limit: max same-entity neighbors per chunk.\n"
        "- deterministic_rules.graph_skip_relations: relation names to suppress entirely.\n"
        "- deterministic_rules.content_kind_overrides: section/tag -> content_kind mapping.\n"
        "- deterministic_rules.high_value_tags: tags to keep (override defaults).\n"
        "- deterministic_rules.merge_spell_blocks / merge_spell_max_blocks: spell merge controls.\n"
        "- deterministic_rules.min_chunk_chars / max_chunk_chars: coalesce sizing.\n"
        "- deterministic_rules.evaluation_query_type_defaults: base content_kind -> query_type map.\n"
        "- deterministic_rules.evaluation_query_type_overrides: map content_kind -> query_type.\n"
        "- deterministic_rules.evaluation_query_templates: map content_kind -> prompt (use {label}).\n"
        "- deterministic_rules.evaluation_query_max_per_kind: cap queries per content kind.\n"
        "- deterministic_rules.evaluation_paragraph_min_chars: min paragraph length for LLM targets.\n"
        "- deterministic_rules.evaluation_hypothetical_answer_max_chars: truncate generated answers.\n"
        "- deterministic_rules.evaluation_hypothetical_answer_strategy: first_paragraph or full_text.\n"
        "- deterministic_rules.eval_* keys: default eval settings (model, query limit/seed, document prefixes).\n"
        "- deterministic_rules.eval_best_practice_defaults: expand_gold + graph boost defaults.\n"
        "- deterministic_rules.config_notes: short rationale string for this config.\n"
        "- deterministic_rules.version_tags: short labels for experiment tracking.\n"
        "- deterministic_rules can be empty if unsure.\n"
        "- Do not include extra keys.\n"
    )


def parse_llm_response(text: str) -> Dict[str, Any]:
    return json.loads(text)


def validate_config_payload(profile: RulesetProfile, payload: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(payload, dict):
        raise ValueError("LLM payload must be a JSON object.")
    missing = [key for key in REQUIRED_KEYS if key not in payload]
    if missing:
        raise ValueError(f"LLM payload missing keys: {', '.join(missing)}")
    if payload.get("ruleset_id") != profile.ruleset_id:
        raise ValueError("LLM payload ruleset_id does not match profile.")
    if payload.get("doc_signature") != profile.doc_signature:
        raise ValueError("LLM payload doc_signature does not match profile.")
    drift = payload.get("drift_criteria") or {}
    if "heading_hierarchy" not in drift or "block_type_distribution" not in drift:
        raise ValueError("LLM payload drift_criteria is incomplete.")
    return payload


def generate_ruleset_config_payload(
    profile: RulesetProfile,
    model: Optional[str] = None,
    api_key: Optional[str] = None,
    prompt: Optional[str] = None,
    temperature: float = 0.2,
) -> Dict[str, Any]:
    api_key = api_key or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is required for LLM config generation.")

    model = model or os.getenv("OPENAI_MODEL", DEFAULT_LLM_MODEL)
    prompt = prompt or build_config_prompt(profile)

    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "Return JSON only."},
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
        response_format={"type": "json_object"},
    )

    content = response.choices[0].message.content or "{}"
    payload = parse_llm_response(content)
    return validate_config_payload(profile, payload)
