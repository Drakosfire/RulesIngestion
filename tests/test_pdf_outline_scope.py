from extraction.pdf_outline_scope import fill_missing_scope, outline_scope
from extraction.schemas import EvidenceUnit


def test_unheaded_unit_on_new_bookmark_page_keeps_unresolved_scope():
    unit = EvidenceUnit(
        unit_id="original", unit_type="prose", text="Continuation of chapter A.",
        structural_path=[], ordering_key=0, page_fingerprint="fingerprint",
        content_hash="hash", source_line_start=1, source_line_end=1,
        anomaly_flags=["no_heading_parent"], content_version="test",
    )
    destinations = outline_scope([(1, "Chapter A", 1), (1, "Chapter B", 12)])
    assert fill_missing_scope([unit], 12, destinations)[0] is unit
    assert fill_missing_scope([unit], 11, destinations)[0].structural_path == ["Chapter A"]
    assert fill_missing_scope([unit], 13, destinations)[0].structural_path == ["Chapter B"]
