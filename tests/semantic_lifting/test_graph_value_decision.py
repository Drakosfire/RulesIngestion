from scripts.run_graph_reasoning_benchmark import build_decision


def test_no_promotion_without_a_measurable_multihop_substrate():
    decision = build_decision()
    assert decision["disposition"] == "GRAPH_ASSIST_NO_PROMOTION"
    assert decision["promotion_allowed"] is False
    assert decision["treatments"]["A_existing_bm25"]["required_full_set"] == 5
    assert decision["treatments"]["B_dungeonmind_retrieval"]["required_full_set"] == 5
    assert decision["treatments"]["D_structured_edge_adjudication"]["status"] == "not_run"
