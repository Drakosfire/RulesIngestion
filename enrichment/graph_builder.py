"""Graph building utilities for enriched chunks."""

from __future__ import annotations

import hashlib
import os
import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set, Tuple

from .chunks import EnrichedChunk
from .extractors import extract_feat_title_from_text, extract_spell_title_from_text, normalize_space


@dataclass
class Graph:
    """Simple node/edge graph for RAG queries."""

    nodes: List[Dict[str, Any]] = field(default_factory=list)
    edges: List[Dict[str, Any]] = field(default_factory=list)
    stats: Dict[str, Any] = field(default_factory=dict)

    def add_node(self, node_id: str, node_type: str, payload: Dict[str, Any]) -> None:
        self.nodes.append({"id": node_id, "type": node_type, **payload})

    def add_edge(
        self,
        source: str,
        target: str,
        relation: str,
        payload: Optional[Dict[str, Any]] = None,
    ) -> None:
        edge_payload = {"source": source, "target": target, "relation": relation}
        if payload:
            edge_payload.update(payload)
        self.edges.append(edge_payload)

    def to_dict(self) -> Dict[str, Any]:
        payload = {"nodes": self.nodes, "edges": self.edges}
        if self.stats:
            payload["stats"] = self.stats
        return payload


def _normalize_entity_name(text: str) -> str:
    cleaned = normalize_space(text or "").strip()
    if not cleaned:
        return ""
    cleaned = cleaned.replace("*", "")
    cleaned = re.sub(r"\[[^\]]+\]", " ", cleaned)
    cleaned = re.sub(r"[^A-Za-z0-9\s'\-]", " ", cleaned)
    cleaned = normalize_space(cleaned)
    return cleaned


def _normalize_entity_key(text: str) -> str:
    normalized = _normalize_entity_name(text)
    return normalized.lower()


def _slugify_name(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")


def _normalize_book_id(document_id: str) -> str:
    if not document_id:
        return "unknown"
    match = re.match(r"^(.*?)(?:-\d{3}-\d{3}|-\d{3})$", document_id)
    if match:
        return match.group(1)
    return document_id


def _derive_chapter_id(book_id: str, section_path: List[str]) -> Optional[str]:
    if not section_path:
        return None
    chapter_title = section_path[0]
    chapter_slug = _slugify_name(chapter_title)
    if not chapter_slug:
        return None
    return f"chapter:{book_id}:{chapter_slug}"


def _canonical_entity_id(ruleset_id: str, entity_type: str, name: str, fallback_key: str) -> str:
    ruleset_slug = _slugify_name(ruleset_id) or "unknown"
    name_slug = _slugify_name(name)
    if not name_slug:
        name_slug = hashlib.sha1(fallback_key.encode("utf-8")).hexdigest()[:12]
    return f"canon:{ruleset_slug}:{entity_type.lower()}:{name_slug}"


def _is_canonical_id(value: str) -> bool:
    return isinstance(value, str) and value.startswith("canon:")


def _is_abbreviation(token: str) -> bool:
    return bool(re.fullmatch(r"[A-Z]{2,10}[0-9]?", token or ""))


def _is_reasonable_canonical(name: str) -> bool:
    if not name:
        return False
    if len(name) < 4:
        return False
    return bool(re.search(r"[A-Za-z]", name))


def _extract_alias_pairs(text: str) -> List[Tuple[str, str]]:
    if not text:
        return []
    patterns = [
        re.compile(r"\b([A-Z][A-Za-z0-9\s'\-]{3,80})\s*\(\s*([A-Z]{2,10}[0-9]?)\s*\)"),
        re.compile(r"\b([A-Z]{2,10}[0-9]?)\s*\(\s*([A-Z][A-Za-z0-9\s'\-]{3,80})\s*\)"),
    ]
    pairs: List[Tuple[str, str]] = []
    for pattern in patterns:
        for match in pattern.findall(text):
            left, right = match[0].strip(), match[1].strip()
            if _is_abbreviation(left) and not _is_abbreviation(right):
                pairs.append((left, right))
            elif _is_abbreviation(right) and not _is_abbreviation(left):
                pairs.append((right, left))
    return pairs


def _merge_alias_map(base: Dict[str, str], additions: Dict[str, str]) -> Dict[str, str]:
    for alias, canonical in additions.items():
        if alias and canonical and alias != canonical:
            base.setdefault(alias, canonical)
    return base


def _build_entity_alias_map(
    chunks: List[EnrichedChunk], resolved_config: Optional[Any]
) -> Dict[str, str]:
    alias_map: Dict[str, str] = {}
    deterministic_rules = (resolved_config.deterministic_rules or {}) if resolved_config else {}
    config_aliases = deterministic_rules.get("entity_aliases", {})

    if isinstance(config_aliases, dict):
        for alias, canonical in config_aliases.items():
            alias_key = _normalize_entity_key(str(alias))
            canonical_norm = _normalize_entity_name(str(canonical))
            if alias_key and canonical_norm:
                alias_map[alias_key] = canonical_norm
    elif isinstance(config_aliases, list):
        for entry in config_aliases:
            if not isinstance(entry, dict):
                continue
            alias = _normalize_entity_key(str(entry.get("alias", "")))
            canonical = _normalize_entity_name(str(entry.get("canonical", "")))
            if alias and canonical:
                alias_map[alias] = canonical

    derived_aliases: Dict[str, str] = {}
    for chunk in chunks:
        for alias_raw, canonical_raw in _extract_alias_pairs(chunk.text):
            alias_norm = _normalize_entity_key(alias_raw)
            canonical_norm = _normalize_entity_name(canonical_raw)
            if not _is_reasonable_canonical(canonical_norm):
                continue
            if alias_norm and canonical_norm and alias_norm != canonical_norm:
                derived_aliases[alias_norm] = canonical_norm

    return _merge_alias_map(alias_map, derived_aliases)


def _resolve_alias_name(name: str, alias_map: Dict[str, str]) -> Tuple[str, Optional[str]]:
    normalized = _normalize_entity_key(name)
    if not normalized:
        return "", None
    canonical = alias_map.get(normalized)
    if canonical and canonical != normalized:
        return canonical, _normalize_entity_name(name)
    return name, None


def _extract_entity_name(chunk: EnrichedChunk) -> str:
    if chunk.content_kind == "spell":
        title = extract_spell_title_from_text(chunk.text)
        return _normalize_entity_name(title or "")
    if chunk.content_kind == "feat":
        title = extract_feat_title_from_text(chunk.text)
        return _normalize_entity_name(title or "")
    if chunk.content_kind == "rule":
        if chunk.block_type in {"SectionHeader", "Title"}:
            if chunk.section_path:
                return _normalize_entity_name(chunk.section_path[-1])
            first_line = (chunk.text or "").splitlines()[0] if chunk.text else ""
            return _normalize_entity_name(first_line[:120])
        return ""
    if chunk.section_path:
        return _normalize_entity_name(chunk.section_path[-1])
    first_line = (chunk.text or "").splitlines()[0] if chunk.text else ""
    return _normalize_entity_name(first_line[:120])


SECTION_ENTITY_KEYWORDS = {
    "conditions": "Condition",
    "condition": "Condition",
    "classes": "Class",
    "class": "Class",
    "ancestries": "Ancestry",
    "ancestry": "Ancestry",
    "backgrounds": "Background",
    "background": "Background",
    "monsters": "Monster",
    "bestiary": "Monster",
}

RELATION_PATTERNS = [
    ("requires", re.compile(r"\brequires?\s+\*\*([A-Z][A-Za-z0-9\s'\-]{2,80})\*\*", re.IGNORECASE)),
    ("requires", re.compile(r"\brequires?\s+([A-Z][A-Za-z0-9\s'\-]{2,80})(?=[\.,;:\n])")),
    ("grants", re.compile(r"\bgrants?\s+\*\*([A-Z][A-Za-z0-9\s'\-]{2,80})\*\*", re.IGNORECASE)),
    ("grants", re.compile(r"\bgrants?\s+([A-Z][A-Za-z0-9\s'\-]{2,80})(?=[\.,;:\n])")),
    ("affects", re.compile(r"\baffects?\s+\*\*([A-Z][A-Za-z0-9\s'\-]{2,80})\*\*", re.IGNORECASE)),
    ("affects", re.compile(r"\baffects?\s+([A-Z][A-Za-z0-9\s'\-]{2,80})(?=[\.,;:\n])")),
    ("has_effect", re.compile(r"\bhas effect(?:s)?\s+(?:of\s+)?\*\*([A-Z][A-Za-z0-9\s'\-]{2,80})\*\*", re.IGNORECASE)),
    ("has_effect", re.compile(r"\bhas effect(?:s)?\s+(?:of\s+)?([A-Z][A-Za-z0-9\s'\-]{2,80})(?=[\.,;:\n])")),
]

RELATION_TARGET_LIMIT = 4
CHUNK_ADJACENCY_LIMIT = 12
MECHANIC_FRAME_TYPES = {"MechanicFrame", "Spell", "Feat", "Rule", "Action", "Ability"}
MECHANIC_FRAME_TYPE_PRIORITY = ["MechanicFrame", "Spell", "Feat", "Rule", "Action", "Ability"]
STRUCTURAL_COREFERENCE_RELATION = "structural_coreference"
CORE_ENTITY_TYPES = {
    "Spell",
    "Feat",
    "Item",
    "Rule",
    "Condition",
    "Class",
    "Ancestry",
    "Background",
    "Monster",
}


def _strip_markdown_title(text: str) -> str:
    cleaned = (text or "").strip()
    cleaned = cleaned.replace("**", "")
    cleaned = cleaned.replace("__", "")
    cleaned = normalize_space(cleaned)
    return cleaned


def _extract_bold_title(text: str) -> str:
    match = re.match(r"^\s*\*\*(.+?)\*\*", text or "")
    if not match:
        return ""
    return _normalize_entity_name(match.group(1))


def _infer_section_entity_type(chunk: EnrichedChunk) -> Optional[str]:
    if chunk.block_type not in {"SectionHeader", "Title"}:
        return None
    for segment in chunk.section_path:
        segment_lower = segment.lower()
        for keyword, entity_type in SECTION_ENTITY_KEYWORDS.items():
            if keyword in segment_lower:
                return entity_type
    return None


def _infer_entity_type_from_header_text(text: str) -> Optional[str]:
    normalized = _normalize_entity_name(_strip_markdown_title(text)).lower()
    if not normalized:
        return None
    if normalized in SECTION_ENTITY_KEYWORDS:
        return SECTION_ENTITY_KEYWORDS[normalized]
    if normalized.startswith("chapter ") or normalized.startswith("part "):
        for keyword, entity_type in SECTION_ENTITY_KEYWORDS.items():
            if keyword in normalized:
                return entity_type
    return None


def _extract_section_entity_name(chunk: EnrichedChunk) -> str:
    if not chunk.section_path:
        return _normalize_entity_name(_strip_markdown_title(chunk.text))
    last_segment = chunk.section_path[-1]
    last_lower = last_segment.lower()
    if any(keyword in last_lower for keyword in SECTION_ENTITY_KEYWORDS):
        if len(chunk.section_path) > 1:
            return _normalize_entity_name(chunk.section_path[-2])
        return _normalize_entity_name(_strip_markdown_title(chunk.text))
    return _normalize_entity_name(last_segment)


def _infer_tag_entity_type(chunk: EnrichedChunk) -> Optional[str]:
    if not chunk.tags:
        return None
    for tag in chunk.tags:
        tag_lower = tag.lower()
        entity_type = SECTION_ENTITY_KEYWORDS.get(tag_lower)
        if entity_type:
            return entity_type
    return None


# Category keywords to filter out when extracting specific entity names
_PATH_CATEGORY_KEYWORDS = {
    "ancestries", "ancestry", "classes", "class",
    "backgrounds", "background", "chapter", "appendix",
    "versatile heritages", "mixed ancestries", "heritages",
    "conditions", "condition", "monsters", "bestiary",
    "feats", "spells", "items", "equipment", "gear",
    "skills", "actions", "activities", "traits",
}

# Keywords that indicate a SectionHeader is a category header, not an entity name
_CATEGORY_HEADER_KEYWORDS = {
    # Category headers
    "ancestries", "ancestry", "classes", "class", "backgrounds", "background",
    "feats", "spells", "equipment", "gear", "skills", "actions",
    "chapter", "appendix", "heritages", "heritage", "conditions",
    "introduction", "overview", "appendix", "index", "glossary",
    # Level headers
    "level", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th",
    # Attribute/stat headers
    "attribute", "boosts", "flaw", "languages", "traits", "physical description",
    "hit points", "proficiencies", "perception", "saving throws", "defenses",
    "key attribute", "class dc", "initial", "armor", "attacks", "weapons", "size", "speed",
    # Social/descriptive headers
    "society", "beliefs", "sample names", "sample character", "playing", "others probably",
    "you might", "key terms", "prerequisites", "faith", "allies", "your allies",
    "character sheet", "port of call", "home world", "deity", "age", "gender",
    # Credits/metadata
    "authors", "author", "editing", "editor", "editors", "development",
    "artist", "artists", "art direction", "graphic design", "publisher",
    "creative", "manager", "special thanks", "based on",
    # Generic document structure
    "example", "examples", "overview", "summary", "using", "format",
    "reading", "step", "during", "while", "in downtime", "encounters",
    "exploration", "combat", "social", "downtime",
    # Game mechanics
    "hero points", "bulk", "currency", "rarity", "round", "turn",
    "perception", "proficiency", "dice", "gaming", "tools of play",
    "basics", "rules", "advancement", "multiclass", "dedication",
    # Feature header fields
    "trigger", "effect", "effects", "requirements", "frequency", "cost", "duration",
    "benefit", "special", "access", "source",
    # Other noise patterns
    "the first", "the players", "the game", "the galaxy", "player core", "starfinder", "versatile",
    "cover", "interior", "devotee benefits", "archetypes", "archetype",
    "spell repertoire", "cantrips", "heightening", "swapping",
}


def _extract_named_entity_from_path(
    chunk: EnrichedChunk,
    entity_type: str
) -> Optional[str]:
    """
    Extract specific entity name from section path.
    
    For a chunk with section_path = ["Chapter 2", "Ancestries", "Example"]
    and entity_type = "Ancestry", returns "Example".
    
    Filters out:
    - Category keywords ("ancestries", "classes", etc.)
    - Chapter headers ("chapter N ...")
    - Generic subsections
    """
    if not chunk.section_path:
        return None
    
    # Walk section_path from end to find specific entity name
    for segment in reversed(chunk.section_path):
        segment_lower = segment.lower().strip()
        
        # Skip empty segments
        if not segment_lower:
            continue
        
        # Skip category keywords
        if any(kw in segment_lower for kw in _PATH_CATEGORY_KEYWORDS):
            continue
        
        # Skip chapter/appendix headers (e.g., "Chapter 2", "Chapter 3 Classes")
        if segment_lower.startswith("chapter ") or segment_lower.startswith("appendix "):
            continue
        
        # Skip very short names (likely abbreviations or noise)
        if len(segment_lower) < 3:
            continue
        
        # Found a specific name
        return _normalize_entity_name(segment)
    
    return None


def _has_entity_signature(
    chunks: List[EnrichedChunk],
    chunk_idx: int,
    entity_type: str,
    window_size: int = 20,
) -> bool:
    """Check nearby headers for ancestry/class signature fields."""
    if entity_type not in {"Ancestry", "Class"}:
        return True

    signature_map = {
        "Ancestry": {"attribute boosts", "hit points", "size", "speed", "languages", "traits"},
        "Class": {"key attribute", "key attributes", "hit points", "initial proficiencies"},
    }
    threshold_map = {"Ancestry": 1, "Class": 2}
    signatures = signature_map.get(entity_type, set())
    threshold = threshold_map.get(entity_type, 2)
    hits = 0

    for neighbor in chunks[chunk_idx + 1 : chunk_idx + window_size]:
        if neighbor.block_type not in {"SectionHeader", "Title"}:
            continue
        header_raw = _strip_markdown_title(neighbor.text)
        header = _normalize_entity_name(header_raw).lower()
        if not header:
            continue
        if header in signatures:
            hits += 1
            if hits >= threshold:
                return True
        # Stop once we hit another entity-like header (likely next entry)
        if _is_simple_entity_name(header_raw):
            return False
    return False


def _has_rule_bearing_followup(
    chunks: List[EnrichedChunk],
    chunk_idx: int,
    window_size: int = 8,
) -> bool:
    """Check if a header is followed by rule-bearing content before next header."""
    for neighbor in chunks[chunk_idx + 1 : chunk_idx + window_size + 1]:
        if neighbor.block_type in {"SectionHeader", "Title"}:
            header_text = _strip_markdown_title(neighbor.text)
            if _is_simple_entity_name(header_text):
                return False
        if neighbor.is_rule_bearing:
            return True
    return False


def _should_inherit_mechanic_frame(chunk: EnrichedChunk) -> bool:
    if chunk.is_rule_bearing:
        return True
    if chunk.block_type in {"Text", "Table", "TableCell"}:
        return True
    if chunk.content_kind in {"rule", "feat", "spell", "item"}:
        return True
    return False


def _is_simple_entity_name(text: str) -> bool:
    """
    Check if text looks like a simple entity name (e.g., "EXAMPLE NAME").
    
    Returns True for simple names, False for category headers or complex text.
    """
    if not text:
        return False
    
    cleaned = text.strip().replace("*", "").replace("_", "").strip()
    cleaned_lower = cleaned.lower()
    
    # Skip empty or too short
    if len(cleaned) < 4:  # Most entity names are 4+ characters
        return False
    
    # Skip if it contains category keywords
    if any(kw in cleaned_lower for kw in _CATEGORY_HEADER_KEYWORDS):
        return False
    
    # Skip if it looks like a feat/spell (contains "FEAT", "SPELL", "[action]", etc.)
    if "feat" in cleaned_lower or "spell" in cleaned_lower:
        return False
    if "[" in cleaned or "]" in cleaned:  # Action markers
        return False
    
    # Skip if it's too long (probably a description, not a name)
    if len(cleaned) > 30:  # Entity names are typically short
        return False
    
    # Skip if it contains common non-name patterns
    if ":" in cleaned or "—" in cleaned or "..." in cleaned:
        return False
    
    # Skip generic game terms
    generic_terms = {
        "action", "attack", "check", "save", "skill", "speed", "trait",
        "bonuses", "penalties", "initiative", "modifier", "bonus", "penalty",
        "constitution", "strength", "dexterity", "intelligence", "wisdom", "charisma",
        "damage", "defense", "defenses", "resistance", "immunity", "vulnerable",
        "narrative", "characters", "defining", "creating", "exploring",
        "directive", "directives", "ability", "abilities", "power", "powers",
    }
    if cleaned_lower in generic_terms or any(term in cleaned_lower for term in generic_terms if len(term) > 5):
        return False
    
    # Accept if it's 1-2 words (ancestry/class names are typically 1-2 words)
    words = cleaned.split()
    if len(words) > 2:
        return False
    
    # Must start with capital letter (proper noun pattern)
    if not cleaned[0].isupper():
        return False
    
    return True


def _build_entity_type_context(
    chunks: List[EnrichedChunk],
    window_size: int = 30
) -> Dict[int, str]:
    """
    Build a mapping from chunk index to inferred entity type context.
    
    Uses nearby tags within a window to infer context.
    
    Returns dict mapping chunk_index -> entity_type (e.g., "Ancestry", "Class")
    """
    context_map: Dict[int, str] = {}
    
    # First, identify chunks with relevant tags for fallback
    tagged_indices: Dict[int, str] = {}
    for i, chunk in enumerate(chunks):
        if not chunk.tags:
            continue
        for tag in chunk.tags:
            tag_lower = tag.lower()
            if "ancestr" in tag_lower or "heritage" in tag_lower:
                tagged_indices[i] = "Ancestry"
                break
            elif "class" in tag_lower and "subclass" not in tag_lower:
                tagged_indices[i] = "Class"
                break
            elif "background" in tag_lower:
                tagged_indices[i] = "Background"
                break
    
    # Build context from explicit chapter/category headers
    current_context: Optional[str] = None
    for i, chunk in enumerate(chunks):
        if chunk.block_type != "SectionHeader":
            continue

        header_context = _infer_entity_type_from_header_text(chunk.text or "")
        if header_context:
            current_context = header_context
            continue

        if current_context:
            context_map[i] = current_context

    # Backfill context from nearby tags within window
    for i, chunk in enumerate(chunks):
        if chunk.block_type != "SectionHeader":
            continue
        if i in context_map:
            continue
        for j in range(max(0, i - window_size), min(len(chunks), i + window_size)):
            if j in tagged_indices:
                context_map[i] = tagged_indices[j]
                break
    
    return context_map


def _extract_tag_entity_name(chunk: EnrichedChunk) -> str:
    title = _extract_bold_title(chunk.text or "")
    if title:
        return title
    if chunk.block_type not in {"SectionHeader", "Title"}:
        return ""
    return _normalize_entity_name(_strip_markdown_title(chunk.text))


def _extract_relation_mentions(text: str) -> List[Tuple[str, str]]:
    if not text:
        return []
    mentions: List[Tuple[str, str]] = []
    for relation, pattern in RELATION_PATTERNS:
        for match in pattern.findall(text):
            raw = match if isinstance(match, str) else match[0]
            target = _normalize_entity_name(raw)
            if target:
                mentions.append((relation, target))
                if len([m for m in mentions if m[0] == relation]) >= RELATION_TARGET_LIMIT:
                    break
    return mentions


def _add_entity_index(
    index: Dict[str, str],
    canonical_id: str,
    names: List[str],
) -> None:
    for name in names:
        canonical_key = _normalize_entity_key(name)
        if not canonical_key:
            continue
        index.setdefault(canonical_key, canonical_id)


def _connect_chunks_by_entity(
    graph: Graph,
    entity_to_chunks: Dict[str, Set[str]],
    max_neighbors_per_chunk: int = CHUNK_ADJACENCY_LIMIT,
) -> None:
    for entity_id, chunk_ids in entity_to_chunks.items():
        if len(chunk_ids) <= 1:
            continue
        ordered = sorted(chunk_ids)
        for idx, chunk_id in enumerate(ordered):
            neighbor_count = 0
            for neighbor_id in ordered[idx + 1 :]:
                graph.add_edge(
                    chunk_id,
                    neighbor_id,
                    STRUCTURAL_COREFERENCE_RELATION,
                    {"entity_id": entity_id, "semantic": False},
                )
                neighbor_count += 1
                if neighbor_count >= max_neighbors_per_chunk:
                    break


def _summarize_graph(graph: Graph) -> Dict[str, Any]:
    node_type_counts: Dict[str, int] = {}
    edge_relation_counts: Dict[str, int] = {}
    alias_lengths: List[int] = []
    entity_type_counts: Dict[str, int] = {}

    for node in graph.nodes:
        node_type = node.get("type", "unknown")
        node_type_counts[node_type] = node_type_counts.get(node_type, 0) + 1
        if node_type not in {"document", "section", "chunk"}:
            entity_type_counts[node_type] = entity_type_counts.get(node_type, 0) + 1
            aliases = node.get("aliases") or []
            alias_lengths.append(len(aliases))

    for edge in graph.edges:
        relation = edge.get("relation", "unknown")
        edge_relation_counts[relation] = edge_relation_counts.get(relation, 0) + 1

    total_entities = sum(entity_type_counts.values())
    alias_with_multiple = sum(1 for length in alias_lengths if length > 1)
    avg_alias_length = round(sum(alias_lengths) / len(alias_lengths), 3) if alias_lengths else 0.0

    return {
        "node_counts": node_type_counts,
        "entity_type_counts": entity_type_counts,
        "edge_relation_counts": edge_relation_counts,
        "entity_count": total_entities,
        "entities_with_multiple_aliases": alias_with_multiple,
        "avg_aliases_per_entity": avg_alias_length,
        "max_aliases_per_entity": max(alias_lengths) if alias_lengths else 0,
    }


def _validate_graph(graph: Graph) -> None:
    missing_canonical = [
        node
        for node in graph.nodes
        if node.get("type") not in {"document", "section", "chunk"}
        and not _is_canonical_id(node.get("id", ""))
        and not node.get("canonical_id")
    ]
    if missing_canonical:
        sample_ids = [node.get("id") for node in missing_canonical[:5]]
        print(
            "⚠️  Graph validation: missing canonical_id for "
            f"{len(missing_canonical)} entity nodes (sample: {sample_ids})"
        )

    missing_relation = [edge for edge in graph.edges if not edge.get("relation")]
    if missing_relation:
        print(
            "⚠️  Graph validation: edges missing relation="
            f"{len(missing_relation)}"
        )


def build_chunk_graph(
    doc_id: str,
    chunks: List[EnrichedChunk],
    ruleset_id: Optional[str] = None,
    resolved_config: Optional[Any] = None,
) -> Graph:
    """Build a doc → section → chunk graph with semantic entity nodes."""
    graph = Graph()
    if not ruleset_id:
        print(
            "⚠️  Graph build: ruleset_id missing; defaulting to doc_id "
            f"({doc_id}). Canonical IDs will be book-scoped."
        )
    resolved_ruleset_id = ruleset_id or doc_id
    book_id = _normalize_book_id(doc_id)

    graph.add_node(
        doc_id,
        "document",
        {
            "name": doc_id,
            "ruleset_id": resolved_ruleset_id,
            "book_id": book_id,
        },
    )

    section_nodes: Dict[str, str] = {}
    prev_chunk_id: Optional[str] = None
    entity_nodes: Dict[str, str] = {}
    entity_ids_by_name: Dict[str, str] = {}
    entity_to_chunks: Dict[str, Set[str]] = {}
    active_mechanic_frame_id: Optional[str] = None

    alias_map = _build_entity_alias_map(chunks, resolved_config)
    
    # Build context for inferring entity types from SectionHeader blocks
    # Use large window because tags may be sparse across document sections
    entity_type_context = _build_entity_type_context(chunks, window_size=500)

    for chunk_idx, chunk in enumerate(chunks):
        if not chunk.text.strip():
            continue

        chunk_id = chunk.id

        graph.add_node(
            chunk_id,
            "chunk",
            {
                "content_kind": chunk.content_kind,
                "page": chunk.page,
                "is_rule_bearing": chunk.is_rule_bearing,
                "tags": chunk.tags,
                "spell_rank": chunk.spell_rank,
                "source_document": doc_id,
                "ruleset_id": resolved_ruleset_id,
                "book_id": book_id,
                "chapter_id": _derive_chapter_id(book_id, chunk.section_path),
                "section_path": chunk.section_path,
                "extraction_method": "marker_enrichment",
            },
        )

        graph.add_edge(
            doc_id,
            chunk_id,
            "contains",
            {
                "source_document": doc_id,
                "page": chunk.page,
                "source_chunk_id": chunk_id,
                "extraction_method": "marker_enrichment",
            },
        )

        if chunk.section_path:
            section_key = " > ".join(chunk.section_path)
            if section_key not in section_nodes:
                section_node_id = f"{doc_id}::section::{section_key}"
                section_nodes[section_key] = section_node_id
                graph.add_node(
                    section_node_id,
                    "section",
                    {
                        "section_path": chunk.section_path,
                        "name": chunk.section_path[-1] if chunk.section_path else "",
                        "source_document": doc_id,
                        "ruleset_id": resolved_ruleset_id,
                        "book_id": book_id,
                        "chapter_id": _derive_chapter_id(book_id, chunk.section_path),
                    },
                )
                graph.add_edge(
                    doc_id,
                    section_node_id,
                    "contains",
                    {
                        "source_document": doc_id,
                        "page": chunk.page,
                        "source_chunk_id": chunk_id,
                        "extraction_method": "marker_enrichment",
                    },
                )

            graph.add_edge(
                section_nodes[section_key],
                chunk_id,
                "contains",
                {
                    "source_document": doc_id,
                    "page": chunk.page,
                    "source_chunk_id": chunk_id,
                    "extraction_method": "marker_enrichment",
                },
            )

        if prev_chunk_id:
            graph.add_edge(
                prev_chunk_id,
                chunk_id,
                "next",
                {
                    "source_document": doc_id,
                    "page": chunk.page,
                    "source_chunk_id": chunk_id,
                    "extraction_method": "marker_enrichment",
                },
            )
        prev_chunk_id = chunk_id

        entity_type_map = {
            "spell": "Spell",
            "feat": "Feat",
            "item": "Item",
            "rule": "Rule",
        }

        def _add_entity_node(entity_type: str, entity_name: str) -> Optional[str]:
            if not entity_name:
                return None
            resolved_name, alias_source = _resolve_alias_name(entity_name, alias_map)
            if not resolved_name:
                return None
            canonical_id = _canonical_entity_id(
                resolved_ruleset_id,
                entity_type,
                resolved_name,
                fallback_key=f"{doc_id}:{chunk_id}:{entity_type}",
            )
            if canonical_id not in entity_nodes:
                graph.add_node(
                    canonical_id,
                    entity_type,
                    {
                        "name": resolved_name,
                        "normalized_name": _normalize_entity_name(resolved_name),
                        "canonical_key": _normalize_entity_key(resolved_name),
                        "canonical_id": canonical_id,
                        "ruleset_id": resolved_ruleset_id,
                        "entity_role": "mechanic_frame"
                        if entity_type in MECHANIC_FRAME_TYPES
                        else "entity",
                        "aliases": [resolved_name],
                        "source_documents": [doc_id],
                        "source_chunk_ids": [chunk_id],
                        "source_pages": [chunk.page],
                        "extraction_method": "heuristic",
                        "spell_rank": chunk.spell_rank,
                        "spell_stats": chunk.spell_stats,
                        "traits": chunk.traits,
                        "traditions": chunk.traditions,
                        "tags": chunk.tags,
                    },
                )
                entity_nodes[canonical_id] = canonical_id
                _add_entity_index(entity_ids_by_name, canonical_id, [resolved_name])
                graph.add_edge(
                    doc_id,
                    canonical_id,
                    "mentions",
                    {
                        "source_document": doc_id,
                        "page": chunk.page,
                        "source_chunk_id": chunk_id,
                        "extraction_method": "heuristic",
                    },
                )
            else:
                for node in graph.nodes:
                    if node.get("id") == canonical_id:
                        node.setdefault("source_documents", [])
                        node.setdefault("source_chunk_ids", [])
                        node.setdefault("source_pages", [])
                        if doc_id not in node["source_documents"]:
                            node["source_documents"].append(doc_id)
                        if chunk_id not in node["source_chunk_ids"]:
                            node["source_chunk_ids"].append(chunk_id)
                        if chunk.page not in node["source_pages"]:
                            node["source_pages"].append(chunk.page)
                        for alias in [resolved_name, alias_source]:
                            if alias and alias not in node.get("aliases", []):
                                node.setdefault("aliases", []).append(alias)
                        break
                _add_entity_index(
                    entity_ids_by_name,
                    canonical_id,
                    [resolved_name, alias_source] if alias_source else [resolved_name],
                )

            graph.add_edge(
                chunk_id,
                canonical_id,
                "describes",
                {
                    "source_document": doc_id,
                    "page": chunk.page,
                    "source_chunk_id": chunk_id,
                    "extraction_method": "heuristic",
                },
            )
            graph.add_edge(
                canonical_id,
                chunk_id,
                "mentioned_in",
                {
                    "source_document": doc_id,
                    "page": chunk.page,
                    "source_chunk_id": chunk_id,
                    "extraction_method": "heuristic",
                },
            )
            if entity_type in CORE_ENTITY_TYPES:
                entity_to_chunks.setdefault(canonical_id, set()).add(chunk_id)
            return canonical_id

        entity_type = entity_type_map.get(chunk.content_kind)
        canonical_id = None
        if entity_type:
            entity_name = _extract_entity_name(chunk)
            if entity_type == "Rule" and not entity_name:
                entity_name = ""
            if entity_name:
                canonical_id = _add_entity_node(entity_type, entity_name)
                if chunk.content_kind in {"feat", "spell", "rule", "item"}:
                    active_mechanic_frame_id = _add_entity_node("MechanicFrame", entity_name)

        section_entity_type = _infer_section_entity_type(chunk)
        if section_entity_type and section_entity_type != entity_type:
            section_entity_name = _extract_section_entity_name(chunk)
            # Filter out category headers and noise
            if section_entity_name and _is_simple_entity_name(section_entity_name):
                _add_entity_node(section_entity_type, section_entity_name)

        tag_entity_type = _infer_tag_entity_type(chunk)
        if (
            tag_entity_type
            and tag_entity_type != entity_type
            and tag_entity_type != section_entity_type
        ):
            tag_entity_name = _extract_tag_entity_name(chunk)
            # Filter out category headers and noise
            if tag_entity_name and _is_simple_entity_name(tag_entity_name):
                _add_entity_node(tag_entity_type, tag_entity_name)

        # Extract specific ancestry/class entities from section path (if available)
        if chunk.section_path and chunk.tags:
            for tag in chunk.tags:
                tag_lower = tag.lower()
                if "ancestr" in tag_lower or "heritage" in tag_lower:
                    path_entity_name = _extract_named_entity_from_path(chunk, "Ancestry")
                    if path_entity_name:
                        _add_entity_node("Ancestry", path_entity_name)
                elif "class" in tag_lower and "subclass" not in tag_lower:
                    path_entity_name = _extract_named_entity_from_path(chunk, "Class")
                    if path_entity_name:
                        _add_entity_node("Class", path_entity_name)
                elif "background" in tag_lower:
                    path_entity_name = _extract_named_entity_from_path(chunk, "Background")
                    if path_entity_name:
                        _add_entity_node("Background", path_entity_name)

        # Promote named headers to generic MechanicFrame entities
        mechanic_frame_id: Optional[str] = None
        if chunk.block_type in {"SectionHeader", "Title"}:
            header_text = _strip_markdown_title(chunk.text)
            if _is_simple_entity_name(header_text) and (
                chunk.is_rule_bearing or _has_rule_bearing_followup(chunks, chunk_idx)
            ):
                mechanic_frame_id = _add_entity_node("MechanicFrame", header_text)
                active_mechanic_frame_id = mechanic_frame_id
            elif _is_simple_entity_name(header_text):
                active_mechanic_frame_id = None

        if (
            active_mechanic_frame_id
            and _should_inherit_mechanic_frame(chunk)
            and active_mechanic_frame_id != mechanic_frame_id
        ):
            graph.add_edge(
                chunk_id,
                active_mechanic_frame_id,
                "describes",
                {
                    "source_document": doc_id,
                    "page": chunk.page,
                    "source_chunk_id": chunk_id,
                    "extraction_method": "header_scope",
                    "semantic": False,
                },
            )

        # Extract ancestry/class entities from SectionHeader text using context
        # This handles cases where section_path is empty but nearby chunks have tags
        if chunk.block_type == "SectionHeader" and chunk_idx in entity_type_context:
            header_text = _strip_markdown_title(chunk.text)
            if _is_simple_entity_name(header_text):
                context_entity_type = entity_type_context[chunk_idx]
                entity_name = _normalize_entity_name(header_text)
                if (
                    entity_name
                    and entity_name.lower() not in _PATH_CATEGORY_KEYWORDS
                    and _has_entity_signature(chunks, chunk_idx, context_entity_type)
                ):
                    _add_entity_node(context_entity_type, entity_name)

        if canonical_id:
            for trait in chunk.traits:
                trait_name_raw = _normalize_entity_name(trait)
                trait_name, trait_alias = _resolve_alias_name(trait_name_raw, alias_map)
                trait_id = _canonical_entity_id(
                    resolved_ruleset_id,
                    "Trait",
                    trait_name,
                    fallback_key=f"{doc_id}:{chunk_id}:trait:{trait}",
                )
                if trait_id not in entity_nodes:
                    graph.add_node(
                        trait_id,
                        "Trait",
                        {
                            "name": trait_name,
                            "canonical_id": trait_id,
                            "ruleset_id": resolved_ruleset_id,
                            "entity_role": "entity",
                            "aliases": [trait_name] + ([trait_alias] if trait_alias else []),
                            "source_documents": [doc_id],
                            "source_chunk_ids": [chunk_id],
                            "source_pages": [chunk.page],
                            "extraction_method": "heuristic",
                        },
                    )
                    entity_nodes[trait_id] = trait_id
                    _add_entity_index(
                        entity_ids_by_name,
                        trait_id,
                        [trait_name, trait_alias] if trait_alias else [trait_name],
                    )
                graph.add_edge(
                    canonical_id,
                    trait_id,
                    "has_trait",
                    {
                        "source_document": doc_id,
                        "page": chunk.page,
                        "source_chunk_id": chunk_id,
                        "extraction_method": "heuristic",
                    },
                )

            for tradition in chunk.traditions:
                tradition_raw = _normalize_entity_name(tradition)
                tradition_name, tradition_alias = _resolve_alias_name(tradition_raw, alias_map)
                tradition_id = _canonical_entity_id(
                    resolved_ruleset_id,
                    "Tradition",
                    tradition_name,
                    fallback_key=f"{doc_id}:{chunk_id}:tradition:{tradition}",
                )
                if tradition_id not in entity_nodes:
                    graph.add_node(
                        tradition_id,
                        "Tradition",
                        {
                            "name": tradition_name,
                            "canonical_id": tradition_id,
                            "ruleset_id": resolved_ruleset_id,
                            "entity_role": "entity",
                            "aliases": [tradition_name] + ([tradition_alias] if tradition_alias else []),
                            "source_documents": [doc_id],
                            "source_chunk_ids": [chunk_id],
                            "source_pages": [chunk.page],
                            "extraction_method": "heuristic",
                        },
                    )
                    entity_nodes[tradition_id] = tradition_id
                    _add_entity_index(
                        entity_ids_by_name,
                        tradition_id,
                        [tradition_name, tradition_alias] if tradition_alias else [tradition_name],
                    )
                graph.add_edge(
                    canonical_id,
                    tradition_id,
                    "has_tradition",
                    {
                        "source_document": doc_id,
                        "page": chunk.page,
                        "source_chunk_id": chunk_id,
                        "extraction_method": "heuristic",
                    },
                )

            if chunk.spell_rank is not None:
                rank_name = f"Rank {chunk.spell_rank}"
                rank_id = _canonical_entity_id(
                    resolved_ruleset_id,
                    "SpellRank",
                    rank_name,
                    fallback_key=f"{doc_id}:{chunk_id}:rank:{chunk.spell_rank}",
                )
                if rank_id not in entity_nodes:
                    graph.add_node(
                        rank_id,
                        "SpellRank",
                        {
                            "name": rank_name,
                            "canonical_id": rank_id,
                            "ruleset_id": resolved_ruleset_id,
                            "entity_role": "entity",
                            "aliases": [str(chunk.spell_rank)],
                            "source_documents": [doc_id],
                            "source_chunk_ids": [chunk_id],
                            "source_pages": [chunk.page],
                            "extraction_method": "heuristic",
                        },
                    )
                    entity_nodes[rank_id] = rank_id
                    _add_entity_index(entity_ids_by_name, rank_id, [rank_name, str(chunk.spell_rank)])
                graph.add_edge(
                    canonical_id,
                    rank_id,
                    "has_rank",
                    {
                        "source_document": doc_id,
                        "page": chunk.page,
                        "source_chunk_id": chunk_id,
                        "extraction_method": "heuristic",
                    },
                )

            for tag in chunk.tags:
                tag_raw = _normalize_entity_name(tag)
                tag_name, tag_alias = _resolve_alias_name(tag_raw, alias_map)
                tag_id = _canonical_entity_id(
                    resolved_ruleset_id,
                    "Tag",
                    tag_name,
                    fallback_key=f"{doc_id}:{chunk_id}:tag:{tag}",
                )
                if tag_id not in entity_nodes:
                    graph.add_node(
                        tag_id,
                        "Tag",
                        {
                            "name": tag_name,
                            "canonical_id": tag_id,
                            "ruleset_id": resolved_ruleset_id,
                            "entity_role": "entity",
                            "aliases": [tag_name] + ([tag_alias] if tag_alias else []),
                            "source_documents": [doc_id],
                            "source_chunk_ids": [chunk_id],
                            "source_pages": [chunk.page],
                            "extraction_method": "heuristic",
                        },
                    )
                    entity_nodes[tag_id] = tag_id
                    _add_entity_index(
                        entity_ids_by_name,
                        tag_id,
                        [tag_name, tag_alias] if tag_alias else [tag_name],
                    )
                graph.add_edge(
                    canonical_id,
                    tag_id,
                    "has_tag",
                    {
                        "source_document": doc_id,
                        "page": chunk.page,
                        "source_chunk_id": chunk_id,
                        "extraction_method": "heuristic",
                    },
                )

            for stat_key, stat_value in (chunk.spell_stats or {}).items():
                stat_name = _normalize_entity_name(f"{stat_key}: {stat_value}")
                stat_id = _canonical_entity_id(
                    resolved_ruleset_id,
                    "SpellStat",
                    stat_name,
                    fallback_key=f"{doc_id}:{chunk_id}:stat:{stat_key}:{stat_value}",
                )
                if stat_id not in entity_nodes:
                    graph.add_node(
                        stat_id,
                        "SpellStat",
                        {
                            "name": stat_name,
                            "canonical_id": stat_id,
                            "ruleset_id": resolved_ruleset_id,
                            "entity_role": "entity",
                            "stat_key": stat_key,
                            "stat_value": stat_value,
                            "source_documents": [doc_id],
                            "source_chunk_ids": [chunk_id],
                            "source_pages": [chunk.page],
                            "extraction_method": "heuristic",
                        },
                    )
                    entity_nodes[stat_id] = stat_id
                    _add_entity_index(
                        entity_ids_by_name,
                        stat_id,
                        [stat_name, stat_key, stat_value],
                    )
                graph.add_edge(
                    canonical_id,
                    stat_id,
                    "has_stat",
                    {
                        "source_document": doc_id,
                        "page": chunk.page,
                        "source_chunk_id": chunk_id,
                        "extraction_method": "heuristic",
                    },
                )

        relation_mentions = _extract_relation_mentions(chunk.text)
        if relation_mentions:
            for relation, target_name in relation_mentions:
                resolved_target, alias_source = _resolve_alias_name(target_name, alias_map)
                if not resolved_target:
                    continue
                target_id = entity_ids_by_name.get(_normalize_entity_key(resolved_target))
                if not target_id:
                    target_id = _canonical_entity_id(
                        resolved_ruleset_id,
                        "Concept",
                        resolved_target,
                        fallback_key=f"{doc_id}:{chunk_id}:relation:{resolved_target}",
                    )
                    if target_id not in entity_nodes:
                        graph.add_node(
                            target_id,
                            "Concept",
                            {
                                "name": resolved_target,
                                "normalized_name": _normalize_entity_name(resolved_target),
                                "canonical_id": target_id,
                                "ruleset_id": resolved_ruleset_id,
                                "entity_role": "provisional",
                                "provisional": True,
                                "aliases": [resolved_target] + ([alias_source] if alias_source else []),
                                "source_documents": [doc_id],
                                "source_chunk_ids": [chunk_id],
                                "source_pages": [chunk.page],
                                "extraction_method": "relation_pattern",
                            },
                        )
                        entity_nodes[target_id] = target_id
                        _add_entity_index(
                            entity_ids_by_name,
                            target_id,
                            [resolved_target, alias_source] if alias_source else [resolved_target],
                        )
                source_id = canonical_id or chunk_id
                graph.add_edge(
                    source_id,
                    target_id,
                    relation,
                    {
                        "source_document": doc_id,
                        "page": chunk.page,
                        "source_chunk_id": chunk_id,
                        "extraction_method": "relation_pattern",
                    },
                )
                graph.add_edge(
                    target_id,
                    chunk_id,
                    "mentioned_in_relation",
                    {
                        "source_document": doc_id,
                        "page": chunk.page,
                        "source_chunk_id": chunk_id,
                        "extraction_method": "relation_pattern",
                    },
                )
                if target_id and chunk_id and graph.nodes:
                    for node in graph.nodes:
                        if node.get("id") == target_id and node.get("entity_role") == "entity":
                            entity_to_chunks.setdefault(target_id, set()).add(chunk_id)
                            break
                    entity_to_chunks.setdefault(target_id, set()).add(chunk_id)

    _connect_chunks_by_entity(graph, entity_to_chunks)
    summary = _summarize_graph(graph)
    summary["ruleset_id"] = resolved_ruleset_id
    summary["document_id"] = doc_id
    graph.stats = summary
    _validate_graph(graph)
    return graph


def build_fact_graph(
    doc_id: str,
    chunks: List[EnrichedChunk],
    ruleset_id: Optional[str] = None,
    resolved_config: Optional[Any] = None,
    include_fact_chunk_links: bool = True,
    include_partial: bool = False,
    allow_cross_section: bool = True,
    vocabularies: Optional[Dict[str, Set[str]]] = None,
    mention_type_mappings: Optional[Dict[str, Set[str]]] = None,
) -> Graph:
    """Build a graph with RuleFacts as nodes and typed relations as edges."""
    from .clause_units import extract_clause_units
    from .fact_relations import generate_fact_relations
    from .mentions import MentionType, extract_mentions
    from .rule_facts import extract_rule_facts
    from .vocabulary_loader import (
        _extract_mechanic_terms_from_chunk,
        load_mention_type_mappings,
        load_vocabulary_from_graph_data,
    )

    graph = build_chunk_graph(
        doc_id=doc_id,
        chunks=chunks,
        ruleset_id=ruleset_id,
        resolved_config=resolved_config,
    )

    resolved_ruleset_id = ruleset_id or doc_id
    book_id = _normalize_book_id(doc_id)

    chunk_map = {chunk.id: chunk for chunk in chunks}
    clause_map: Dict[str, Any] = {}
    clause_mechanic_keys: Dict[str, Set[str]] = {}
    facts = []
    mechanic_mentions_by_chunk: Dict[str, Set[str]] = {}

    if vocabularies is None:
        if mention_type_mappings is None:
            mention_type_mappings = load_mention_type_mappings(config=resolved_config)
        vocabularies = load_vocabulary_from_graph_data(graph.to_dict(), mention_type_mappings)

    mechanic_entity_types = {
        term.lower() for term in (mention_type_mappings.get("mechanic") or set())
    }

    for chunk_idx, chunk in enumerate(chunks):
        chunk_terms = _extract_mechanic_terms_from_chunk(
            {
                "text": chunk.text,
                "content_kind": chunk.content_kind,
                "block_type": chunk.block_type,
                "tags": chunk.tags,
            },
            mechanic_entity_types,
        )
        if chunk_terms and (
            chunk.is_rule_bearing or _has_rule_bearing_followup(chunks, chunk_idx)
        ):
            names = mechanic_mentions_by_chunk.setdefault(chunk.id, set())
            for term in chunk_terms:
                normalized_name = _normalize_entity_name(term)
                if normalized_name:
                    names.add(normalized_name)

        clauses = extract_clause_units(chunk)
        for clause in clauses:
            clause_map[clause.clause_id] = clause
            mentions = extract_mentions(clause, vocabularies=vocabularies)
            mechanic_mentions = [
                mention
                for mention in mentions
                if mention.mention_type == MentionType.MECHANIC
            ]
            if mechanic_mentions:
                names = mechanic_mentions_by_chunk.setdefault(chunk.id, set())
                for mention in mechanic_mentions:
                    normalized = mention.normalized or ""
                    if normalized.startswith("mechanic:"):
                        normalized = normalized.split(":", 1)[-1]
                    normalized_name = _normalize_entity_name(normalized)
                    if normalized_name:
                        names.add(normalized_name)
                        clause_mechanic_keys.setdefault(clause.clause_id, set()).add(
                            _normalize_entity_key(normalized_name)
                        )
            clause_facts = extract_rule_facts(clause, mentions, resolved_config=resolved_config)
            if not include_partial:
                clause_facts = [fact for fact in clause_facts if fact.is_complete]
            facts.extend(clause_facts)

    existing_node_ids = {node.get("id") for node in graph.nodes}
    existing_describes = {
        (edge.get("source"), edge.get("target"))
        for edge in graph.edges
        if edge.get("relation") == "describes"
    }
    mechanic_frame_by_chunk: Dict[str, str] = {}
    for chunk_id, mention_names in mechanic_mentions_by_chunk.items():
        chunk = chunk_map.get(chunk_id)
        for mention_name in sorted(mention_names):
            canonical_id = _canonical_entity_id(
                resolved_ruleset_id,
                "MechanicFrame",
                mention_name,
                fallback_key=f"{doc_id}:{chunk_id}:mechanic:{mention_name}",
            )
            if chunk_id not in mechanic_frame_by_chunk:
                mechanic_frame_by_chunk[chunk_id] = canonical_id
            if canonical_id not in existing_node_ids:
                graph.add_node(
                    canonical_id,
                    "MechanicFrame",
                    {
                        "name": mention_name,
                        "normalized_name": _normalize_entity_name(mention_name),
                        "canonical_key": _normalize_entity_key(mention_name),
                        "canonical_id": canonical_id,
                        "ruleset_id": resolved_ruleset_id,
                        "entity_role": "mechanic_frame",
                        "aliases": [mention_name],
                        "source_documents": [doc_id],
                        "source_chunk_ids": [chunk_id],
                        "source_pages": [chunk.page] if chunk else [],
                        "extraction_method": "mention_promotion",
                    },
                )
                existing_node_ids.add(canonical_id)
            if (chunk_id, canonical_id) not in existing_describes:
                graph.add_edge(
                    chunk_id,
                    canonical_id,
                    "describes",
                    {
                        "source_document": doc_id,
                        "page": chunk.page if chunk else None,
                        "source_chunk_id": chunk_id,
                        "extraction_method": "mention_promotion",
                    },
                )
                existing_describes.add((chunk_id, canonical_id))

    active_mention_frame_id: Optional[str] = None
    for chunk in chunks:
        if chunk.id in mechanic_frame_by_chunk:
            active_mention_frame_id = mechanic_frame_by_chunk[chunk.id]
        elif chunk.block_type in {"SectionHeader", "Title"}:
            header_text = _strip_markdown_title(chunk.text)
            if _is_simple_entity_name(header_text):
                active_mention_frame_id = None

        if active_mention_frame_id and _should_inherit_mechanic_frame(chunk):
            if (chunk.id, active_mention_frame_id) not in existing_describes:
                graph.add_edge(
                    chunk.id,
                    active_mention_frame_id,
                    "describes",
                    {
                        "source_document": doc_id,
                        "page": chunk.page,
                        "source_chunk_id": chunk.id,
                        "extraction_method": "mention_scope",
                        "semantic": False,
                    },
                )
                existing_describes.add((chunk.id, active_mention_frame_id))

    for fact in facts:
        clause = clause_map.get(fact.clause_id)
        chunk_id = clause.parent_chunk_id if clause else fact.clause_id.split("::clause_")[0]
        chunk = chunk_map.get(chunk_id)
        section_path = list(chunk.section_path) if chunk else []
        chapter_id = _derive_chapter_id(book_id, section_path)

        graph.add_node(
            fact.fact_id,
            "RuleFact",
            {
                **fact.to_dict(),
                "source_document": doc_id,
                "ruleset_id": resolved_ruleset_id,
                "book_id": book_id,
                "chapter_id": chapter_id,
                "source_chunk_id": chunk_id,
                "section_path": section_path,
                "extraction_method": "rule_fact_extraction",
            },
        )

        if include_fact_chunk_links and chunk_id:
            graph.add_edge(
                chunk_id,
                fact.fact_id,
                "has_fact",
                {
                    "source_document": doc_id,
                    "source_chunk_id": chunk_id,
                    "clause_id": fact.clause_id,
                    "extraction_method": "rule_fact_extraction",
                },
            )

    entity_type_by_id: Dict[str, str] = {}
    entity_name_by_id: Dict[str, str] = {}
    for node in graph.nodes:
        node_id = node.get("id")
        node_type = node.get("type")
        if node_id and node_type:
            entity_type_by_id[node_id] = node_type
            if node.get("name"):
                entity_name_by_id[node_id] = node.get("name")

    chunk_to_entities: Dict[str, List[str]] = {}
    describes_meta: Dict[Tuple[str, str], Dict[str, object]] = {}
    for edge in graph.edges:
        if edge.get("relation") == "describes":
            chunk_id = edge.get("source")
            entity_id = edge.get("target")
            if chunk_id and entity_id:
                chunk_to_entities.setdefault(chunk_id, []).append(entity_id)
                key = (chunk_id, entity_id)
                existing = describes_meta.get(key)
                if existing and existing.get("extraction_method") == "header_scope":
                    continue
                describes_meta[key] = edge

    debug_chunk_ids: Set[str] = set()
    debug_chunks_env = os.environ.get("DM_DEBUG_BELONGS_TO_CHUNKS")
    if debug_chunks_env:
        debug_chunk_ids = {
            chunk_id.strip()
            for chunk_id in debug_chunks_env.split(",")
            if chunk_id.strip()
        }

    belongs_to_count = 0
    multi_candidate_count = 0
    missing_candidate_count = 0
    for fact in facts:
        clause = clause_map.get(fact.clause_id)
        chunk_id = clause.parent_chunk_id if clause else fact.clause_id.split("::clause_")[0]
        candidate_ids = [
            entity_id
            for entity_id in chunk_to_entities.get(chunk_id, [])
            if entity_type_by_id.get(entity_id) in MECHANIC_FRAME_TYPES
        ]
        entity_id = None
        if candidate_ids:
            if chunk_id in debug_chunk_ids:
                debug_candidates = []
                for candidate in candidate_ids:
                    debug_candidates.append(
                        {
                            "id": candidate,
                            "name": entity_name_by_id.get(candidate, ""),
                            "type": entity_type_by_id.get(candidate, ""),
                            "extraction_method": describes_meta.get((chunk_id, candidate), {}).get(
                                "extraction_method"
                            ),
                        }
                    )
                print(
                    f"🔎 [BELONGS_TO DEBUG] chunk={chunk_id} "
                    f"fact={fact.fact_id} subject={fact.subject} "
                    f"candidates={debug_candidates}"
                )

            subject_key = _normalize_entity_key(fact.subject or "")
            if subject_key:
                subject_matched = [
                    candidate
                    for candidate in candidate_ids
                    if _normalize_entity_key(entity_name_by_id.get(candidate, "")) == subject_key
                ]
                if subject_matched:
                    candidate_ids = subject_matched
            if (
                fact.fact_type.value == "requires"
                and fact.object
                and len(candidate_ids) > 1
            ):
                object_key = _normalize_entity_key(fact.object)
                if object_key:
                    object_matched = [
                        candidate
                        for candidate in candidate_ids
                        if _normalize_entity_key(entity_name_by_id.get(candidate, ""))
                        == object_key
                    ]
                    if object_matched:
                        candidate_ids = object_matched
            clause_keys = clause_mechanic_keys.get(fact.clause_id, set())
            if clause_keys and len(candidate_ids) > 1:
                mention_matched = [
                    candidate
                    for candidate in candidate_ids
                    if _normalize_entity_key(entity_name_by_id.get(candidate, "")) in clause_keys
                ]
                if mention_matched:
                    candidate_ids = mention_matched
            if len(candidate_ids) > 1:
                header_scope_candidates = [
                    candidate
                    for candidate in candidate_ids
                    if describes_meta.get((chunk_id, candidate), {}).get("extraction_method")
                    == "header_scope"
                ]
                if header_scope_candidates:
                    candidate_ids = header_scope_candidates
            if len(candidate_ids) > 1:
                multi_candidate_count += 1
            candidate_ids.sort(
                key=lambda candidate: (
                    MECHANIC_FRAME_TYPE_PRIORITY.index(entity_type_by_id.get(candidate, ""))
                    if entity_type_by_id.get(candidate) in MECHANIC_FRAME_TYPES
                    else len(MECHANIC_FRAME_TYPE_PRIORITY),
                    _normalize_entity_key(entity_name_by_id.get(candidate, "")),
                    candidate,
                )
            )
            entity_id = candidate_ids[0]
        else:
            missing_candidate_count += 1

        if entity_id:
            graph.add_edge(
                fact.fact_id,
                entity_id,
                "belongs_to",
                {
                    "source_document": doc_id,
                    "source_chunk_id": chunk_id,
                    "clause_id": fact.clause_id,
                    "extraction_method": "structural_join",
                },
            )
            belongs_to_count += 1

    print(
        "✅ Added "
        f"{belongs_to_count} BELONGS_TO edges ({belongs_to_count}/{len(facts)} facts)"
    )
    if multi_candidate_count:
        print(
            "⚠️  BELONGS_TO: "
            f"{multi_candidate_count} facts had multiple mechanic-frame candidates."
        )
    if missing_candidate_count:
        print(
            "⚠️  BELONGS_TO: "
            f"{missing_candidate_count} facts had no mechanic-frame candidate."
        )

    relations = generate_fact_relations(
        facts,
        chunk_map,
        resolved_config=resolved_config,
        allow_cross_section=allow_cross_section,
        include_partial=include_partial,
    )

    for relation in relations:
        graph.add_edge(
            relation.source_fact_id,
            relation.target_fact_id,
            relation.relation_type.value,
            {
                "relation_id": relation.relation_id,
                "structural_distance": relation.structural_distance,
                "same_clause": relation.same_clause,
                "same_chunk": relation.same_chunk,
                "same_section": relation.same_section,
                "inference_method": relation.inference_method,
                "confidence": relation.confidence,
            },
        )

    summary = _summarize_graph(graph)
    summary["ruleset_id"] = resolved_ruleset_id
    summary["document_id"] = doc_id
    summary["fact_count"] = len(facts)
    summary["fact_relation_count"] = len(relations)
    graph.stats = summary
    _validate_graph(graph)
    return graph
