"""
Test whether mention-based retrieval can find gold chunks for blind_001_02.

Uses config-driven vocabulary loading (not hardcoded lists).
Demonstrates the full config-driven pipeline:
1. Load entity_type -> mention_type mapping (from config or default)
2. Load vocabulary from graph using that mapping
3. Extract mentions from clauses

This is Phase 2 validation.
"""
from pathlib import Path
import json
import sys

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from enrichment.clause_units import extract_clause_units
from enrichment.mentions import extract_mentions
from enrichment.vocabulary_loader import (
    load_vocabulary_from_graph, 
    load_mention_type_mappings,
    extract_role_mentions,
)
from enrichment.chunks import EnrichedChunk


def run_experiment():
    # Find the latest run
    base_dir = Path("Rules/StarFinder2e/PlayerCore/outputs/runs")
    runs = sorted([d for d in base_dir.iterdir() if d.is_dir() and d.name.startswith("2026")])
    if not runs:
        print("❌ No runs found")
        return
    
    latest_run = runs[-1]
    base_path = latest_run / "enriched"
    print(f"📁 Using run: {latest_run.name}")
    
    # Step 1: Load mapping (config-driven, falls back to default)
    # In production, would load from RulesetConfiguration
    enriched_path = base_path / "merged.enriched.json"
    mappings = load_mention_type_mappings(enriched_path=enriched_path)
    
    print(f"\n📐 Entity types mapped to 'role': {sorted(mappings.get('role', set()))}")
    print(f"📐 Entity types mapped to 'mechanic': {sorted(mappings.get('mechanic', set()))}")
    print(f"📐 Entity types mapped to 'condition': {sorted(mappings.get('condition', set()))}")
    
    # Step 2: Load vocabulary from graph using the mapping
    graph_path = base_path / "merged.graph.json"
    if not graph_path.exists():
        print(f"❌ Graph not found: {graph_path}")
        return
        
    vocabularies = load_vocabulary_from_graph(graph_path, mappings)
    role_vocabulary = vocabularies.get("role", set())
    mechanic_vocabulary = vocabularies.get("mechanic", set())
    
    print(f"\n📚 Loaded {len(role_vocabulary)} role terms from graph")
    print(f"   Sample roles: {sorted(list(role_vocabulary))[:10]}...")
    print(f"📚 Loaded {len(mechanic_vocabulary)} mechanic terms from graph")
    print(f"   Sample mechanics: {sorted(list(mechanic_vocabulary))[:10]}...")
    
    # Step 3: Load all clauses and extract mentions
    with open(enriched_path) as f:
        data = json.load(f)
    
    print(f"\n🔍 Processing {len(data.get('chunks', []))} chunks...")
    
    # Build mention index: normalized -> [(clause_id, chunk_id)]
    mention_index = {}
    total_mentions = 0
    total_clauses = 0
    mention_type_counts = {}
    
    for chunk_dict in data.get("chunks", []):
        # Filter to only known EnrichedChunk fields
        known_fields = {'id', 'block_type', 'text', 'page', 'bbox', 'section_hierarchy',
                        'content_kind', 'is_rule_bearing', 'tags', 'traits', 'spell_rank',
                        'traditions', 'spell_stats', 'section_path'}
        filtered = {k: v for k, v in chunk_dict.items() if k in known_fields}
        chunk = EnrichedChunk(**filtered)
        for clause in extract_clause_units(chunk):
            total_clauses += 1
            
            # Pattern-based mentions (universal)
            mentions = extract_mentions(clause)
            # Vocabulary-based role mentions (from graph)
            mentions.extend(extract_role_mentions(clause, role_vocabulary, len(mentions)))
            
            for m in mentions:
                total_mentions += 1
                
                # Count by type
                mt = m.mention_type.value
                mention_type_counts[mt] = mention_type_counts.get(mt, 0) + 1
                
                if m.normalized not in mention_index:
                    mention_index[m.normalized] = []
                mention_index[m.normalized].append((clause.clause_id, chunk.id))
    
    print(f"\n📊 Mention extraction stats:")
    print(f"   Total clauses: {total_clauses}")
    print(f"   Total mentions: {total_mentions}")
    print(f"   Mentions per clause: {total_mentions / total_clauses:.2f}")
    print(f"   Unique normalized keys: {len(mention_index)}")
    
    print(f"\n📊 Mention type distribution:")
    for mt, count in sorted(mention_type_counts.items(), key=lambda x: -x[1]):
        print(f"   {mt}: {count} ({count/total_mentions*100:.1f}%)")
    
    # Query: Find clauses with lashunta AND (solarian OR level:9)
    lashunta_clauses = set(c[1] for c in mention_index.get("role:lashunta", []))
    solarian_clauses = set(c[1] for c in mention_index.get("role:solarian", []))
    level9_clauses = set(c[1] for c in mention_index.get("level:9", []))
    
    # Gold chunks for blind_001_02 (sample - may need adjustment)
    gold_chunks = {
        "sf2e-playercore-PZO22001-Starfinder-Player-Core-058-073::/page/1/Text/12",
        "sf2e-playercore-PZO22001-Starfinder-Player-Core-058-073::/page/3/SectionHeader/24",
        "sf2e-playercore-PZO22001-Starfinder-Player-Core-058-073::/page/3/SectionHeader/28",
        "sf2e-playercore-PZO22001-Starfinder-Player-Core-138-149::/page/2/Table/2",
        "sf2e-playercore-PZO22001-Starfinder-Player-Core-138-149::/page/3/Text/8",
    }
    
    print(f"\n🎯 Query: Find chunks with Lashunta/Solarian/Level 9")
    print(f"   Chunks with 'lashunta': {len(lashunta_clauses)}")
    print(f"   Chunks with 'solarian': {len(solarian_clauses)}")
    print(f"   Chunks with 'level:9': {len(level9_clauses)}")
    
    # Check overlap with gold
    found_via_lashunta = gold_chunks & lashunta_clauses
    found_via_solarian = gold_chunks & solarian_clauses
    found_via_level = gold_chunks & level9_clauses
    
    print(f"\n✅ Gold chunks found via mentions:")
    print(f"   via 'lashunta': {len(found_via_lashunta)}/5")
    print(f"   via 'solarian': {len(found_via_solarian)}/5")
    print(f"   via 'level:9': {len(found_via_level)}/5")
    
    # Combined retrieval
    combined = lashunta_clauses | solarian_clauses | level9_clauses
    found_combined = gold_chunks & combined
    print(f"   combined (union): {len(found_combined)}/5")
    
    # Report which gold chunks were NOT found
    missing = gold_chunks - combined
    if missing:
        print(f"\n❌ Missing gold chunks ({len(missing)}):")
        for chunk_id in sorted(missing):
            print(f"   - {chunk_id}")
    
    # Sample output for documentation
    print(f"\n📝 Sample mentions (first 5 clauses with mentions):")
    shown = 0
    for chunk_dict in data.get("chunks", [])[:100]:
        if shown >= 5:
            break
        filtered = {k: v for k, v in chunk_dict.items() if k in known_fields}
        chunk = EnrichedChunk(**filtered)
        for clause in extract_clause_units(chunk):
            mentions = extract_mentions(clause)
            mentions.extend(extract_role_mentions(clause, role_vocabulary, len(mentions)))
            if mentions:
                print(f"\n   Clause: {clause.text[:80]}...")
                for m in mentions[:5]:
                    print(f"     → {m.mention_type.value}: '{m.surface}' -> {m.normalized}")
                shown += 1
                if shown >= 5:
                    break


if __name__ == "__main__":
    run_experiment()
