"""
Test whether RuleFact extraction enables semantic queries for blind_001_02.

Demonstrates:
1. Extract facts from all clauses
2. Build fact index by subject/type
3. Query for feats applicable to Lashunta + level 9
4. Compare retrieved chunks against gold

This is the validation experiment for Phase 3 of the fact-based retrieval architecture.
"""
from pathlib import Path
from collections import defaultdict
from datetime import datetime
import json
import sys

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from enrichment.clause_units import extract_clause_units
from enrichment.mentions import extract_mentions
from enrichment.vocabulary_loader import load_mention_type_mappings, load_vocabulary_from_graph
from enrichment.rule_facts import extract_rule_facts, FactType, Modality, RuleFact
from enrichment.chunks import EnrichedChunk


def run_experiment():
    """Run the RuleFact extraction validation experiment."""
    print("=" * 70)
    print("RuleFact Extraction Validation Experiment")
    print(f"Run at: {datetime.now().isoformat()}")
    print("=" * 70)
    
    # Try multiple possible paths for PlayerCore data
    possible_paths = [
        Path("Rules/StarFinder2e/PlayerCore/outputs/runs/latest/enriched/merged.enriched.json"),
        Path("../Rules/StarFinder2e/PlayerCore/outputs/runs/latest/enriched/merged.enriched.json"),
        Path("/media/drakosfire/Projects/DungeonOverMind/RulesIngestion/Rules/StarFinder2e/PlayerCore/outputs/runs/latest/enriched/merged.enriched.json"),
    ]
    
    base_path = None
    for path in possible_paths:
        if path.exists():
            base_path = path
            break
    
    if base_path is None:
        print("❌ PlayerCore data not found. Tried:")
        for path in possible_paths:
            print(f"   - {path}")
        print("\nRunning with sample data instead...")
        run_sample_experiment()
        return
    
    print(f"📂 Loading data from: {base_path}")
    
    with open(base_path) as f:
        data = json.load(f)
    
    # Load vocabularies for role/mechanic mentions (if graph exists)
    base_dir = base_path.parent
    graph_path_candidates = [
        base_dir / "merged.graph.fixed.json",
        base_dir / "merged.graph.json",
    ]
    graph_path = next((p for p in graph_path_candidates if p.exists()), None)
    vocabularies = None
    if graph_path:
        mappings = load_mention_type_mappings(enriched_path=base_path)
        vocabularies = load_vocabulary_from_graph(graph_path, mappings)
        print(f"📚 Loaded vocabularies from: {graph_path}")
    else:
        print("⚠️  Graph not found; running without vocabulary mentions.")

    # Build fact indices
    subject_index = defaultdict(list)
    fact_type_index = defaultdict(list)
    scope_index = defaultdict(list)
    
    total_clauses = 0
    total_facts = 0
    clauses_with_facts = 0
    complete_facts = 0
    partial_facts = 0
    fact_type_counts = defaultdict(int)
    modality_counts = defaultdict(int)
    
    print("\n🔄 Extracting facts from chunks...")
    
    chunks_processed = 0
    for chunk_dict in data.get("chunks", []):
        chunk = EnrichedChunk(**chunk_dict)
        chunks_processed += 1
        
        for clause in extract_clause_units(chunk):
            total_clauses += 1
            mentions = extract_mentions(clause, vocabularies=vocabularies)
            facts = extract_rule_facts(clause, mentions)
            
            if facts:
                clauses_with_facts += 1
            
            for fact in facts:
                total_facts += 1
                fact_type_counts[fact.fact_type.value] += 1
                modality_counts[fact.modality.value] += 1
                
                if fact.is_complete:
                    complete_facts += 1
                else:
                    partial_facts += 1
                
                # Index by subject
                if fact.subject:
                    subject_index[fact.subject].append((fact, chunk.id))
                
                # Index by type
                fact_type_index[fact.fact_type].append((fact, chunk.id))
                
                # Index by scope (role-based)
                if fact.scope:
                    for scope_part in fact.scope.split(";"):
                        scope_part = scope_part.strip()
                        if scope_part:
                            scope_index[scope_part].append((fact, chunk.id))
    
    # Print statistics
    print(f"\n📊 Fact Extraction Statistics:")
    print(f"   Chunks processed: {chunks_processed:,}")
    print(f"   Total clauses: {total_clauses:,}")
    print(f"   Total facts: {total_facts:,}")
    print(f"   Clauses with facts: {clauses_with_facts:,}")
    print(f"   Facts per clause: {total_facts/max(total_clauses,1):.3f}")
    print(f"   Coverage: {100*clauses_with_facts/max(total_clauses,1):.1f}%")
    print(f"   Complete facts: {complete_facts:,} ({100*complete_facts/max(total_facts,1):.1f}%)")
    print(f"   Partial facts: {partial_facts:,} ({100*partial_facts/max(total_facts,1):.1f}%)")
    print(f"   Unique subjects: {len(subject_index):,}")
    print(f"   Unique scopes: {len(scope_index):,}")
    
    print(f"\n📊 Fact Type Distribution:")
    for ft, count in sorted(fact_type_counts.items(), key=lambda x: -x[1]):
        pct = 100 * count / max(total_facts, 1)
        print(f"   {ft}: {count:,} ({pct:.1f}%)")
    
    print(f"\n📊 Modality Distribution:")
    for mod, count in sorted(modality_counts.items(), key=lambda x: -x[1]):
        pct = 100 * count / max(total_facts, 1)
        print(f"   {mod}: {count:,} ({pct:.1f}%)")
    
    # Query experiments
    print("\n" + "=" * 70)
    print("Semantic Query Experiments")
    print("=" * 70)
    
    # Query: Find level 9 gates
    level_9_facts = [
        (f, cid) for f, cid in fact_type_index[FactType.LEVEL_GATE]
        if f.object and "9" in str(f.object)
    ]
    print(f"\n🎯 Level 9 gates found: {len(level_9_facts)}")
    if level_9_facts[:3]:
        print("   Sample:")
        for f, cid in level_9_facts[:3]:
            print(f"   - Subject: {f.subject}, Object: {f.object}")
    
    # Query: Find Lashunta-scoped facts
    lashunta_facts = [
        (f, cid) for scope, items in scope_index.items() 
        for f, cid in items
        if "lashunta" in scope.lower()
    ]
    print(f"\n🎯 Lashunta-scoped facts: {len(lashunta_facts)}")
    if lashunta_facts[:3]:
        print("   Sample:")
        for f, cid in lashunta_facts[:3]:
            print(f"   - Type: {f.fact_type.value}, Object: {f.object[:50] if f.object else 'None'}...")
    
    # Query: Find Solarian-scoped facts
    solarian_facts = [
        (f, cid) for scope, items in scope_index.items() 
        for f, cid in items
        if "solarian" in scope.lower()
    ]
    print(f"\n🎯 Solarian-scoped facts: {len(solarian_facts)}")
    if solarian_facts[:3]:
        print("   Sample:")
        for f, cid in solarian_facts[:3]:
            print(f"   - Type: {f.fact_type.value}, Object: {f.object[:50] if f.object else 'None'}...")
    
    # Gold chunks for blind_001_02
    gold_chunks = {
        "sf2e-playercore-PZO22001-Starfinder-Player-Core-058-073::/page/1/Text/12",
        "sf2e-playercore-PZO22001-Starfinder-Player-Core-058-073::/page/3/SectionHeader/24",
        "sf2e-playercore-PZO22001-Starfinder-Player-Core-058-073::/page/3/SectionHeader/28",
        "sf2e-playercore-PZO22001-Starfinder-Player-Core-138-149::/page/2/Table/2",
        "sf2e-playercore-PZO22001-Starfinder-Player-Core-138-149::/page/3/Text/8",
    }
    
    # Collect chunks from role-scoped facts
    lashunta_chunks = {cid for _, cid in lashunta_facts}
    solarian_chunks = {cid for _, cid in solarian_facts}
    level_9_chunks = {cid for _, cid in level_9_facts}
    
    print(f"\n📦 Chunk Coverage:")
    print(f"   Chunks with Lashunta scope: {len(lashunta_chunks)}")
    print(f"   Chunks with Solarian scope: {len(solarian_chunks)}")
    print(f"   Chunks with Level 9 gate: {len(level_9_chunks)}")
    
    # Check gold overlap
    found_via_lashunta = gold_chunks & lashunta_chunks
    found_via_solarian = gold_chunks & solarian_chunks
    found_via_level = gold_chunks & level_9_chunks
    
    combined = lashunta_chunks | solarian_chunks | level_9_chunks
    found_combined = gold_chunks & combined
    
    print(f"\n✅ Gold Chunks Found (blind_001_02):")
    print(f"   via Lashunta scope: {len(found_via_lashunta)}/5")
    print(f"   via Solarian scope: {len(found_via_solarian)}/5")
    print(f"   via Level 9 gate: {len(found_via_level)}/5")
    print(f"   combined (union): {len(found_combined)}/5")
    
    if found_combined:
        print("\n   Found chunks:")
        for chunk_id in found_combined:
            print(f"   - {chunk_id}")
    
    # List failure facts
    print("\n" + "=" * 70)
    print("Failure Facts Analysis")
    print("=" * 70)
    
    failure_facts = fact_type_index.get(FactType.ON_FAILURE, [])
    print(f"\n❌ Failure facts found: {len(failure_facts)}")
    
    if failure_facts[:5]:
        print("\n   Sample failure facts:")
        for f, cid in failure_facts[:5]:
            obj_preview = f.object[:60] + "..." if f.object and len(f.object) > 60 else f.object
            print(f"   - Subject: {f.subject or '(none)'}")
            print(f"     Object: {obj_preview}")
            print(f"     Complete: {f.is_complete}")
            print()
    
    # Critical success/failure facts
    critical_facts = fact_type_index.get(FactType.ON_CRITICAL, [])
    print(f"\n⚡ Critical outcome facts found: {len(critical_facts)}")
    
    # Sample output for handoff
    print("\n" + "=" * 70)
    print("Sample Extracted Facts (for handoff)")
    print("=" * 70)
    
    sample_count = 0
    for fact_type in [FactType.GRANTS, FactType.REQUIRES, FactType.ON_SUCCESS, FactType.LEVEL_GATE, FactType.INSTEAD_OF]:
        facts_of_type = fact_type_index.get(fact_type, [])
        if facts_of_type:
            f, cid = facts_of_type[0]
            print(f"\n📌 {fact_type.value.upper()}:")
            print(f"   Subject: {f.subject}")
            print(f"   Object: {f.object[:80] if f.object else 'None'}...")
            print(f"   Modality: {f.modality.value}")
            print(f"   Scope: {f.scope}")
            print(f"   Chunk: {cid[:50]}...")
            sample_count += 1
    
    print("\n" + "=" * 70)
    print("Experiment Complete")
    print("=" * 70)


def run_sample_experiment():
    """Run experiment with sample data when real data is unavailable."""
    print("\n🔬 Running sample experiment with synthetic data...")
    
    # Create sample clauses
    sample_texts = [
        "On a success, you deal 2d6 fire damage to the target.",
        "Critical Failure: You fall prone and are stunned 1.",
        "At 5th level, you gain the ability to fly at half speed.",
        "Prerequisites: Level 9, trained in Athletics.",
        "You gain a +2 circumstance bonus to Perception checks.",
        "You must be trained in Stealth to use this action.",
        "This grants you resistance to fire damage equal to your level.",
        "Instead, you may make a ranged attack against the target.",
        "This affects all creatures within 30 feet.",
        "When you hit with a melee Strike, deal extra damage.",
        "Unless you have resistance, you take full damage.",
    ]
    
    from enrichment.clause_units import ClauseUnit
    
    total_facts = 0
    fact_type_counts = defaultdict(int)
    
    print("\n📊 Extracting facts from sample clauses:")
    
    for i, text in enumerate(sample_texts):
        clause = ClauseUnit(
            clause_id=f"sample::clause_{i}",
            text=text,
            parent_chunk_id="sample",
            order_in_chunk=i,
            char_offsets=(0, len(text)),
            page=1,
        )
        
        mentions = extract_mentions(clause)
        facts = extract_rule_facts(clause, mentions)
        
        if facts:
            print(f"\n   Clause: \"{text[:60]}...\"")
            for fact in facts:
                total_facts += 1
                fact_type_counts[fact.fact_type.value] += 1
                print(f"   → {fact.fact_type.value}: {fact.object[:50] if fact.object else '(no object)'}...")
    
    print(f"\n📊 Sample Statistics:")
    print(f"   Total clauses: {len(sample_texts)}")
    print(f"   Total facts: {total_facts}")
    print(f"   Facts per clause: {total_facts/len(sample_texts):.2f}")
    
    print(f"\n📊 Fact Type Distribution:")
    for ft, count in sorted(fact_type_counts.items(), key=lambda x: -x[1]):
        pct = 100 * count / max(total_facts, 1)
        print(f"   {ft}: {count} ({pct:.1f}%)")
    
    print("\n✅ Sample experiment complete - validates extraction patterns work")


if __name__ == "__main__":
    run_experiment()
