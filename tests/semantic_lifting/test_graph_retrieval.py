from semantic_lifting.graph_retrieval import EvidenceNode, GraphEdge, bounded_closure


def _node(name):
    return EvidenceNode(name, f"ev:{name}", f"unit:{name}", "artifact:1", "revision:1")


def test_bounded_two_hop_closure_and_exact_evidence_paths():
    nodes = {name: _node(name) for name in ("a", "b", "c", "d")}
    edges = [GraphEdge("ab", "a", "b", "exception", "retain"),
             GraphEdge("bc", "b", "c", "prerequisite", "retain"),
             GraphEdge("cd", "c", "d", "remote", "reject")]
    result = bounded_closure(query="q", seed_assertion_ids=["a"], nodes=nodes,
                             edges=edges, retained_edge_ids={"ab", "bc"})
    assert result["final_evidence_unit_ids"] == ["unit:a", "unit:b", "unit:c"]
    assert result["paths"][-1]["via_edges"] == ["ab", "bc"]
    assert result["traversed_edges"] == 2


def test_no_hidden_node_or_unadmitted_edge_can_authorize_evidence():
    nodes = {"a": _node("a"), "b": _node("b")}
    edges = [GraphEdge("ab", "a", "b", "exception", "review")]
    result = bounded_closure(query="q", seed_assertion_ids=["a"], nodes=nodes,
                             edges=edges, retained_edge_ids=set())
    assert result["final_evidence_unit_ids"] == ["unit:a"]
    assert result["traversed_edges"] == 0
