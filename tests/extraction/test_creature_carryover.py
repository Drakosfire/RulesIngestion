import json
from pathlib import Path

from extraction.creature_carryover import bind_continuation, continuation_scopes
from extraction.cross_page_join import run_join_pass
from extraction.schemas import EvidenceUnit


def test_srd_leading_actions_keep_owner_and_source():
    cases = json.loads(Path(__file__).with_name("srd_creature_carryover.json").read_text())
    for case in cases:
        page, owner = case["page"], case["owner"]
        scopes = continuation_scopes({"texts": case["texts"]})
        assert scopes == {page: (owner, "Actions")}
        units = [EvidenceUnit.from_dict(row) for row in case["units"]]
        bound = run_join_pass([bind_continuation(units, page, scopes[page])])
        assert bound[0].structural_path == [owner, "Actions"]
        assert bound[0].page_fingerprints == [units[0].page_fingerprint]
        assert bound[0].join_metadata["creature_carryover"]["owner_pdf_page"] == page - 1
        assert bound[-1].structural_path == units[-1].structural_path
        assert [u.text for u in bound] == [u.text for u in units]


def test_no_owner_carryover_without_adjacent_source_page():
    cases = json.loads(Path(__file__).with_name("srd_creature_carryover.json").read_text())
    case = cases[0]
    current = [x for x in case["texts"] if x["prov"][0]["page_no"] == case["page"]]
    assert continuation_scopes({"texts": current}) == {}
