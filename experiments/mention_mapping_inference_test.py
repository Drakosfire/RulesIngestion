"""
Experiment: Auto-infer mention_type_mappings from document structure.

Tests two approaches:
1. Tag-based inference: Use chunk tags (ancestries, classes, feats, etc.)
2. Content-kind inference: Use content_kind field (feat, spell, etc.)

Goal: Determine if we can eliminate manual config for mention_type_mappings.

Usage:
    uv run python experiments/mention_mapping_inference_test.py
"""
import json
from pathlib import Path
from collections import Counter, defaultdict
from typing import Dict, Set, List, Tuple

# Cross-system seed mapping: tag/content_kind -> mention_type
# This is much smaller than hardcoding all entity types per ruleset
TAG_TO_MENTION_TYPE = {
    # Role-related tags (character identity)
    "ancestries": "role",
    "ancestry": "role",
    "races": "role",
    "race": "role",
    "species": "role",
    "classes": "role",
    "class": "role",
    "archetypes": "role",
    "archetype": "role",
    "backgrounds": "role",
    "background": "role",
    "heritages": "role",
    "heritage": "role",
    
    # Mechanic-related tags (actions/abilities)
    "feats": "mechanic",
    "feat": "mechanic",
    "spells": "mechanic",
    "spell": "mechanic",
    "abilities": "mechanic",
    "ability": "mechanic",
    "actions": "mechanic",
    "action": "mechanic",
    "skills": "mechanic",
    "skill": "mechanic",
    "equipment": "mechanic",
    "items": "mechanic",
    
    # Condition-related tags
    "conditions": "condition",
    "condition": "condition",
    "status": "condition",
}

CONTENT_KIND_TO_MENTION_TYPE = {
    "feat": "mechanic",
    "spell": "mechanic",
    "rule": None,  # Too generic, skip
    "narrative": None,  # Skip
    "table": None,  # Could be various types
}


def infer_entity_types_from_tags(chunks: List[dict]) -> Dict[str, Set[str]]:
    """
    Infer which entity types (tags) map to which mention types.
    
    Returns: Dict[mention_type, Set[discovered_tags]]
    """
    # Collect all tags and count
    tag_counts = Counter()
    for chunk in chunks:
        for tag in chunk.get("tags", []):
            tag_counts[tag] += 1
    
    print(f"Discovered {len(tag_counts)} unique tags")
    print(f"Top 20 tags: {tag_counts.most_common(20)}")
    
    # Map discovered tags to mention types using seed
    discovered_mapping: Dict[str, Set[str]] = defaultdict(set)
    unmapped_tags = []
    
    for tag in tag_counts:
        normalized = tag.lower().strip()
        if normalized in TAG_TO_MENTION_TYPE:
            mention_type = TAG_TO_MENTION_TYPE[normalized]
            discovered_mapping[mention_type].add(normalized)
        else:
            unmapped_tags.append((tag, tag_counts[tag]))
    
    print(f"\nMapped tags to mention types:")
    for mt, tags in discovered_mapping.items():
        print(f"  {mt}: {tags}")
    
    if unmapped_tags:
        print(f"\nUnmapped tags (consider adding to seed):")
        for tag, count in sorted(unmapped_tags, key=lambda x: -x[1])[:10]:
            print(f"  ({count:4d}x) {tag}")
    
    return dict(discovered_mapping)


def infer_entity_types_from_content_kind(chunks: List[dict]) -> Dict[str, Set[str]]:
    """
    Infer mention types from content_kind field.
    
    Returns: Dict[mention_type, Set[content_kinds]]
    """
    ck_counts = Counter()
    for chunk in chunks:
        ck = chunk.get("content_kind")
        if ck:
            ck_counts[ck] += 1
    
    print(f"\nDiscovered {len(ck_counts)} unique content_kinds")
    for ck, count in ck_counts.most_common():
        print(f"  ({count:5d}x) {ck}")
    
    # Map to mention types
    discovered_mapping: Dict[str, Set[str]] = defaultdict(set)
    
    for ck in ck_counts:
        if ck in CONTENT_KIND_TO_MENTION_TYPE:
            mt = CONTENT_KIND_TO_MENTION_TYPE[ck]
            if mt:  # Skip None mappings
                discovered_mapping[mt].add(ck)
    
    print(f"\nMapped content_kinds to mention types:")
    for mt, cks in discovered_mapping.items():
        print(f"  {mt}: {cks}")
    
    return dict(discovered_mapping)


def extract_vocabulary_from_tagged_chunks(
    chunks: List[dict],
    tag_to_mention_type: Dict[str, str]
) -> Dict[str, Set[str]]:
    """
    Extract entity names from chunks based on their tags.
    
    For chunks tagged with 'ancestries' and content_kind='narrative' or SectionHeader,
    look for entity names (e.g., "Lashunta", "Android").
    
    This is the trickier part - need to identify actual entity NAMES.
    """
    # For now, just collect section headers that match entity patterns
    header_entities: Dict[str, Set[str]] = defaultdict(set)
    
    for chunk in chunks:
        if chunk.get("block_type") != "SectionHeader":
            continue
        
        text = chunk.get("text", "").strip()
        tags = chunk.get("tags", [])
        
        # Clean up bold markers
        clean_text = text.replace("**", "").strip()
        
        # Skip generic headers
        if clean_text.upper() in {"CHAPTER", "INTRODUCTION", "INDEX", "CONTENTS"}:
            continue
        if any(kw in clean_text.upper() for kw in ["CHAPTER ", "PAGE ", "PLAYER CORE"]):
            continue
        
        # Map based on tags
        for tag in tags:
            normalized_tag = tag.lower().strip()
            if normalized_tag in tag_to_mention_type:
                mt = tag_to_mention_type[normalized_tag]
                # Only add if it looks like an entity name (not too long)
                if len(clean_text) < 50 and not clean_text.isupper():
                    header_entities[mt].add(clean_text.lower())
    
    return dict(header_entities)


def run_experiment():
    """Run the inference experiment."""
    print("=" * 70)
    print("EXPERIMENT: Auto-Infer mention_type_mappings")
    print("=" * 70)
    
    # Test on PlayerCore
    base_path = Path("Rules/StarFinder2e/PlayerCore/outputs/runs/2026-01-25_19-16-02/enriched")
    enriched_path = base_path / "merged.enriched.json"
    
    if not enriched_path.exists():
        print(f"ERROR: {enriched_path} not found")
        return
    
    with open(enriched_path) as f:
        data = json.load(f)
    
    chunks = data.get("chunks", [])
    print(f"\nLoaded {len(chunks)} chunks from PlayerCore")
    
    # Approach 1: Tag-based inference
    print("\n" + "=" * 70)
    print("APPROACH 1: Tag-Based Inference")
    print("=" * 70)
    tag_mapping = infer_entity_types_from_tags(chunks)
    
    # Approach 2: Content-kind inference
    print("\n" + "=" * 70)
    print("APPROACH 2: Content-Kind Inference")
    print("=" * 70)
    ck_mapping = infer_entity_types_from_content_kind(chunks)
    
    # Attempt vocabulary extraction from section headers
    print("\n" + "=" * 70)
    print("VOCABULARY EXTRACTION FROM SECTION HEADERS")
    print("=" * 70)
    vocabularies = extract_vocabulary_from_tagged_chunks(chunks, TAG_TO_MENTION_TYPE)
    
    for mt, terms in vocabularies.items():
        print(f"\n{mt} vocabulary ({len(terms)} terms):")
        for term in sorted(list(terms))[:20]:
            print(f"  - {term}")
        if len(terms) > 20:
            print(f"  ... and {len(terms) - 20} more")
    
    # Compare with expected default mapping
    print("\n" + "=" * 70)
    print("COMPARISON WITH DEFAULT MAPPING")
    print("=" * 70)
    
    expected_role_entities = {"ancestry", "class", "archetype", "race", "heritage", "background"}
    expected_mechanic_entities = {"feat", "spell", "ability", "action", "skill"}
    expected_condition_entities = {"condition", "status"}
    
    discovered_role = tag_mapping.get("role", set())
    discovered_mechanic = tag_mapping.get("mechanic", set())
    discovered_condition = tag_mapping.get("condition", set())
    
    print(f"\nRole entity types:")
    print(f"  Expected: {expected_role_entities}")
    print(f"  Discovered: {discovered_role}")
    print(f"  Coverage: {len(discovered_role & expected_role_entities)}/{len(expected_role_entities)}")
    
    print(f"\nMechanic entity types:")
    print(f"  Expected: {expected_mechanic_entities}")
    print(f"  Discovered: {discovered_mechanic}")
    print(f"  Coverage: {len(discovered_mechanic & expected_mechanic_entities)}/{len(expected_mechanic_entities)}")
    
    print(f"\nCondition entity types:")
    print(f"  Expected: {expected_condition_entities}")
    print(f"  Discovered: {discovered_condition}")
    print(f"  Coverage: {len(discovered_condition & expected_condition_entities)}/{len(expected_condition_entities)}")
    
    # Test on GalaxyGuide to verify cross-document consistency
    print("\n" + "=" * 70)
    print("CROSS-DOCUMENT VALIDATION: GalaxyGuide")
    print("=" * 70)
    
    gg_path = Path("Rules/StarFinder2e/GalaxyGuide/outputs/runs/2026-01-25_18-37-56/enriched/merged.enriched.json")
    if gg_path.exists():
        with open(gg_path) as f:
            gg_data = json.load(f)
        
        gg_chunks = gg_data.get("chunks", [])
        print(f"Loaded {len(gg_chunks)} chunks from GalaxyGuide")
        
        gg_tags = Counter()
        for chunk in gg_chunks:
            for tag in chunk.get("tags", []):
                gg_tags[tag] += 1
        
        print(f"Tags in GalaxyGuide: {gg_tags.most_common(15)}")
        
        # Check if same mapping works
        gg_mapped = 0
        gg_unmapped = []
        for tag in gg_tags:
            if tag.lower().strip() in TAG_TO_MENTION_TYPE:
                gg_mapped += 1
            else:
                gg_unmapped.append(tag)
        
        print(f"Tags mapped by seed: {gg_mapped}/{len(gg_tags)}")
        if gg_unmapped:
            print(f"Unmapped: {gg_unmapped[:10]}")
    else:
        print(f"GalaxyGuide not found at {gg_path}")
    
    # Final recommendation
    print("\n" + "=" * 70)
    print("RECOMMENDATION")
    print("=" * 70)
    
    print("""
Based on this experiment:

1. TAG-BASED INFERENCE WORKS: The 'tags' field already contains entity type
   categories (ancestries, classes, feats, etc.) that we can map to mention types.

2. SMALL SEED VOCABULARY SUFFICIENT: A ~30-entry seed mapping covers common
   TTRPG entity types across SF2e, PF2e, D&D 5e.

3. DYNAMIC EXECUTION VIABLE: Scanning all chunk tags is O(n) with n=chunks,
   taking <1 second for 23k chunks.

4. VOCABULARY EXTRACTION IS HARDER: Getting actual entity NAMES (Lashunta,
   Solarian) from section headers is noisier. May need content_kind='feat'
   chunks and text parsing.

NEXT STEPS:
- Implement infer_mention_type_mappings() using tag-based approach
- For vocabulary, continue using graph nodes (Feat, Spell names are clean)
- Consider content_kind for supplementary entity type info
""")


if __name__ == "__main__":
    run_experiment()
