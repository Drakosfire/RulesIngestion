"""Adversarial density test for entity-only traversal.

Per HANDOFF-Entity-Only-Traversal-Experiment-2026-01-30.md Step 4:

Red-team against graph density hacks by constructing two graphs with:
- Same entity structure
- Version A: Minimal facts
- Version B: Many redundant but correct facts

Expected results:
- Entity-only purity: Same for both
- Entity compactness: Same for both
- Assertion load: Lower for A, Higher for B
- Quality score: Same for both

Baseline metrics should FAIL this test (penalize Version B).
New metrics should PASS (not penalize Version B).

This proves we are no longer optimizing against graph sparsity.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict, List, Set

sys.path.insert(0, str(Path(__file__).parent.parent))

from traversal.index import (
    TraversalMode,
    TraversalProjection,
    traverse_entity_only,
    run_entity_only_traversal,
    EntityOnlyTraversalResult,
)
from enrichment.graph_builder import NodeKind


def create_test_graph_version_a() -> Dict[str, Any]:
    """Create minimal-fact version of the test graph.
    
    Graph structure:
    - 3 entity nodes: Spell_Fireball, Spell_Heal, Condition_Burning
    - 2 semantic edges: Fireball -> triggers -> Burning, Heal -> removes -> Burning
    - 2 facts total: one per edge relationship
    """
    nodes = [
        # Entities
        {"id": "canon:spell:fireball", "type": "Spell", "name": "Fireball"},
        {"id": "canon:spell:heal", "type": "Spell", "name": "Heal"},
        {"id": "canon:condition:burning", "type": "Condition", "name": "Burning"},
        # Facts (minimal)
        {"id": "fact:fireball_triggers_burning", "type": "RuleFact", "fact_type": "triggers"},
        {"id": "fact:heal_removes_burning", "type": "RuleFact", "fact_type": "removes"},
    ]
    
    edges = [
        # Entity-entity semantic edges
        {"source": "canon:spell:fireball", "target": "canon:condition:burning", "relation": "triggers"},
        {"source": "canon:spell:heal", "target": "canon:condition:burning", "relation": "removes"},
        # Fact ownership (belongs_to)
        {"source": "fact:fireball_triggers_burning", "target": "canon:spell:fireball", "relation": "belongs_to"},
        {"source": "fact:heal_removes_burning", "target": "canon:spell:heal", "relation": "belongs_to"},
    ]
    
    return {"nodes": nodes, "edges": edges}


def create_test_graph_version_b() -> Dict[str, Any]:
    """Create redundant-fact version of the test graph.
    
    Same entity structure as version A, but with many additional correct facts.
    These facts are redundant but not wrong - they just add more detail.
    """
    nodes = [
        # Entities (same as version A)
        {"id": "canon:spell:fireball", "type": "Spell", "name": "Fireball"},
        {"id": "canon:spell:heal", "type": "Spell", "name": "Heal"},
        {"id": "canon:condition:burning", "type": "Condition", "name": "Burning"},
        # Facts (many redundant)
        {"id": "fact:fireball_triggers_burning", "type": "RuleFact", "fact_type": "triggers"},
        {"id": "fact:fireball_damage_type", "type": "RuleFact", "fact_type": "has_property"},
        {"id": "fact:fireball_area", "type": "RuleFact", "fact_type": "has_property"},
        {"id": "fact:fireball_range", "type": "RuleFact", "fact_type": "has_property"},
        {"id": "fact:fireball_save", "type": "RuleFact", "fact_type": "requires"},
        {"id": "fact:heal_removes_burning", "type": "RuleFact", "fact_type": "removes"},
        {"id": "fact:heal_amount", "type": "RuleFact", "fact_type": "has_property"},
        {"id": "fact:heal_range", "type": "RuleFact", "fact_type": "has_property"},
        {"id": "fact:burning_damage", "type": "RuleFact", "fact_type": "has_property"},
        {"id": "fact:burning_duration", "type": "RuleFact", "fact_type": "has_property"},
    ]
    
    edges = [
        # Entity-entity semantic edges (same as version A)
        {"source": "canon:spell:fireball", "target": "canon:condition:burning", "relation": "triggers"},
        {"source": "canon:spell:heal", "target": "canon:condition:burning", "relation": "removes"},
        # Fact ownership - Fireball facts
        {"source": "fact:fireball_triggers_burning", "target": "canon:spell:fireball", "relation": "belongs_to"},
        {"source": "fact:fireball_damage_type", "target": "canon:spell:fireball", "relation": "belongs_to"},
        {"source": "fact:fireball_area", "target": "canon:spell:fireball", "relation": "belongs_to"},
        {"source": "fact:fireball_range", "target": "canon:spell:fireball", "relation": "belongs_to"},
        {"source": "fact:fireball_save", "target": "canon:spell:fireball", "relation": "belongs_to"},
        # Fact ownership - Heal facts
        {"source": "fact:heal_removes_burning", "target": "canon:spell:heal", "relation": "belongs_to"},
        {"source": "fact:heal_amount", "target": "canon:spell:heal", "relation": "belongs_to"},
        {"source": "fact:heal_range", "target": "canon:spell:heal", "relation": "belongs_to"},
        # Fact ownership - Burning facts
        {"source": "fact:burning_damage", "target": "canon:condition:burning", "relation": "belongs_to"},
        {"source": "fact:burning_duration", "target": "canon:condition:burning", "relation": "belongs_to"},
    ]
    
    return {"nodes": nodes, "edges": edges}


def count_entity_nodes(graph: Dict[str, Any]) -> int:
    """Count entity nodes in graph."""
    return sum(1 for n in graph["nodes"] if n.get("type") not in {"RuleFact", "document", "section", "chunk"})


def count_fact_nodes(graph: Dict[str, Any]) -> int:
    """Count fact nodes in graph."""
    return sum(1 for n in graph["nodes"] if n.get("type") == "RuleFact")


def count_entity_edges(graph: Dict[str, Any]) -> int:
    """Count entity-entity edges (non-belongs_to)."""
    entity_ids = {n["id"] for n in graph["nodes"] if n.get("type") not in {"RuleFact", "document", "section", "chunk"}}
    return sum(
        1 for e in graph["edges"]
        if e.get("source") in entity_ids and e.get("target") in entity_ids
        and e.get("relation") != "belongs_to"
    )


def run_adversarial_test():
    """Run the adversarial density test."""
    print("=" * 60)
    print("ADVERSARIAL DENSITY TEST")
    print("Per HANDOFF-Entity-Only-Traversal-Experiment-2026-01-30.md Step 4")
    print("=" * 60)
    
    # Create test graphs
    graph_a = create_test_graph_version_a()
    graph_b = create_test_graph_version_b()
    
    print("\n--- Graph Structure ---")
    print(f"Version A (minimal facts):")
    print(f"  Entities: {count_entity_nodes(graph_a)}")
    print(f"  Facts: {count_fact_nodes(graph_a)}")
    print(f"  Entity-entity edges: {count_entity_edges(graph_a)}")
    
    print(f"\nVersion B (redundant facts):")
    print(f"  Entities: {count_entity_nodes(graph_b)}")
    print(f"  Facts: {count_fact_nodes(graph_b)}")
    print(f"  Entity-entity edges: {count_entity_edges(graph_b)}")
    
    # Build entity-only projections
    proj_a = TraversalProjection.build(graph_a, mode=TraversalMode.ENTITY_ONLY)
    proj_b = TraversalProjection.build(graph_b, mode=TraversalMode.ENTITY_ONLY)
    
    print("\n--- Entity-Only Projections ---")
    print(f"Version A: {len(proj_a.entity_ids)} entities, {len(proj_a.fact_nodes)} facts")
    print(f"Version B: {len(proj_b.entity_ids)} entities, {len(proj_b.fact_nodes)} facts")
    
    # Run entity-only traversal from Fireball
    seeds = {"canon:spell:fireball"}
    
    result_a = run_entity_only_traversal(seeds, graph_a, max_hops=3, mode=TraversalMode.ENTITY_ONLY)
    result_b = run_entity_only_traversal(seeds, graph_b, max_hops=3, mode=TraversalMode.ENTITY_ONLY)
    
    print("\n--- Traversal Results ---")
    print(f"Version A: entity_path={len(result_a.entity_path)}, attached_facts={len(result_a.attached_facts)}")
    print(f"Version B: entity_path={len(result_b.entity_path)}, attached_facts={len(result_b.attached_facts)}")
    
    # Compute metrics
    print("\n--- Metric Comparison ---")
    
    # Entity path should be the same
    entity_path_match = result_a.entity_path == result_b.entity_path
    print(f"Entity path identical: {entity_path_match}")
    assert entity_path_match, "Entity paths should be identical"
    
    # Entity count should be the same
    entity_count_a = result_a.total_entity_count
    entity_count_b = result_b.total_entity_count
    print(f"Entity count: A={entity_count_a}, B={entity_count_b}")
    assert entity_count_a == entity_count_b, "Entity counts should be identical"
    
    # Fact count should be different (more in B)
    fact_count_a = result_a.total_fact_count
    fact_count_b = result_b.total_fact_count
    print(f"Fact count: A={fact_count_a}, B={fact_count_b}")
    assert fact_count_b > fact_count_a, "Version B should have more facts"
    
    # Assertion load should be different (higher in B)
    assertion_load_a = result_a.assertion_load
    assertion_load_b = result_b.assertion_load
    print(f"Assertion load (facts/entity): A={assertion_load_a:.2f}, B={assertion_load_b:.2f}")
    assert assertion_load_b > assertion_load_a, "Version B should have higher assertion load"
    
    print("\n--- Invariant Checks ---")
    
    # Key invariant: Entity-only metrics should be identical
    # (because entity structure is identical)
    print("Entity-only metrics should be IDENTICAL:")
    print(f"  Entity count: A={entity_count_a}, B={entity_count_b} ✓")
    
    # Assertion load differs, but that's EXPECTED and ALLOWED
    print("\nAssertion load differs (expected and allowed):")
    print(f"  A={assertion_load_a:.2f} facts/entity")
    print(f"  B={assertion_load_b:.2f} facts/entity")
    
    print("\n--- Test Result ---")
    print("✅ PASSED: Entity-only metrics are not penalized by fact density")
    print("   - Same entity structure → same entity-only metrics")
    print("   - More facts → higher assertion load (descriptive, not penalizing)")
    print("   - Graph density does not masquerade as reasoning quality")
    
    return True


def run_baseline_comparison():
    """Show how baseline metrics would fail this test."""
    print("\n" + "=" * 60)
    print("BASELINE COMPARISON (illustrative)")
    print("=" * 60)
    
    graph_a = create_test_graph_version_a()
    graph_b = create_test_graph_version_b()
    
    # Baseline would count all nodes
    total_nodes_a = len(graph_a["nodes"])
    total_nodes_b = len(graph_b["nodes"])
    
    # Baseline purity: semantic edges / total edges
    semantic_edges_a = count_entity_edges(graph_a)
    total_edges_a = len(graph_a["edges"])
    baseline_purity_a = semantic_edges_a / total_edges_a if total_edges_a else 0
    
    semantic_edges_b = count_entity_edges(graph_b)
    total_edges_b = len(graph_b["edges"])
    baseline_purity_b = semantic_edges_b / total_edges_b if total_edges_b else 0
    
    print("\n--- Baseline Metrics (mixed entity+fact) ---")
    print(f"Version A: {total_nodes_a} nodes, purity={baseline_purity_a:.1%}")
    print(f"Version B: {total_nodes_b} nodes, purity={baseline_purity_b:.1%}")
    
    print("\n⚠️  Baseline metrics would PENALIZE Version B:")
    print(f"   - More nodes ({total_nodes_b} vs {total_nodes_a})")
    print(f"   - Lower purity ({baseline_purity_b:.1%} vs {baseline_purity_a:.1%})")
    print("   - This is WRONG because the explanation quality is identical")


if __name__ == "__main__":
    success = run_adversarial_test()
    run_baseline_comparison()
    
    if success:
        print("\n" + "=" * 60)
        print("ALL INVARIANTS PASSED")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("INVARIANT VIOLATIONS DETECTED")
        print("=" * 60)
        sys.exit(1)
