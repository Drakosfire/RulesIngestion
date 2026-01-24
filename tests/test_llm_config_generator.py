# Tests for LLM config generator utilities.

from config_profile import RulesetProfile
from llm_config_generator import build_config_prompt, parse_llm_response


def test_build_config_prompt_includes_profile_fields() -> None:
    profile = RulesetProfile(
        ruleset_id="sf2e",
        doc_signature="sig",
        heading_hierarchy=["A", "B"],
        block_type_distribution={"Text": 2},
        samples=["Sample text"],
    )

    prompt = build_config_prompt(profile)

    assert "ruleset_id" in prompt
    assert "sf2e" in prompt
    assert "heading_hierarchy" in prompt
    assert "Sample text" in prompt


def test_parse_llm_response_loads_json() -> None:
    payload = parse_llm_response('{"ruleset_id":"sf2e","version":"v1"}')

    assert payload["ruleset_id"] == "sf2e"
    assert payload["version"] == "v1"
