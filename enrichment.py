"""
Rules Ingestion - Enrichment Helpers

Contains TTRPG-specific enrichment logic used by the ingestion pipeline.
This keeps the pipeline file focused on orchestration.
"""

from __future__ import annotations

import hashlib
import re
import uuid
from dataclasses import dataclass, field, asdict
from html.parser import HTMLParser
from pathlib import Path
from collections import Counter
from typing import Any, Dict, List, Optional, Tuple, Set, TYPE_CHECKING

if TYPE_CHECKING:
    from config_generator import RulesetConfiguration


# =============================================================================
# TTRPG VOCABULARIES (extracted from legacy pipeline)
# =============================================================================

SECTION_TAGS: Dict[str, str] = {
    "character creation": "character_creation",
    "leveling up": "leveling_up",
    "exploring the galaxy": "exploration",
    "religion": "religion",
    "ancestries": "ancestries",
    "backgrounds": "backgrounds",
    "classes": "classes",
    "skills": "skills",
    "feats": "feats",
    "equipment": "equipment",
    "spells": "spells",
    "playing the game": "playing_the_game",
    "conditions": "conditions",
    "glossary": "glossary",
    "index": "glossary",
    "introduction": "introduction",
    "encounters": "combat",
    "downtime": "downtime",
    "exploration": "exploration",
    "dice": "dice",
    "action": "actions",
    "saving throw": "saving_throws",
    "armor class": "ac",
    "hit points": "hp",
    "proficiency": "proficiency",
    "initiative": "initiative",
    "key terms": "glossary",
}

CONTENT_TYPE_BY_KIND: Dict[str, str] = {
    "rule": "rule",
    "constraint": "rule",
    "definition": "rule",
    "narrative": "narrative",
    "example": "example",
    "table": "table",
    "toc": "toc",
    "nav": "nav",
    "credits": "credits",
    "heading": "heading",
    "trait": "trait",
    "spell": "spell",
    "feat": "feat",
    "item": "item",
    "glossary": "other",
}

RULE_KEYWORDS = {
    "dc",
    "saving throw",
    "check",
    "action",
    "actions",
    "damage",
    "spell",
    "spells",
    "hit points",
    "armor class",
    "ac",
    "modifier",
    "proficiency",
    "initiative",
    "skill",
    "feat",
    "trait",
    "rarity",
}

TRAIT_KEYWORDS = {
    "attack",
    "auditory",
    "aura",
    "cold",
    "concentrate",
    "curse",
    "darkness",
    "emotion",
    "fire",
    "healing",
    "illusion",
    "incapacitation",
    "linguistic",
    "manipulate",
    "mental",
    "polymorph",
    "prediction",
    "radiation",
    "sonic",
    "subtle",
    "unholy",
    "visual",
    "vitality",
    "void",
    "detection",
}

CONSTRAINT_KEYWORDS = {
    "must",
    "cannot",
    "must not",
    "only if",
    "requires",
    "required",
    "prerequisite",
    "prerequisites",
}

SPELL_STAT_PREFIXES = (
    "cast",
    "range",
    "targets",
    "target",
    "area",
    "duration",
    "saving throw",
    "cost",
    "trigger",
    "requirements",
    "effect",
    "traditions",
    "defense",
)

# High-value tags to keep for RAG
HIGH_VALUE_TAGS = {
    "spells", "feats", "classes", "ancestries", "equipment",
    "conditions", "skills", "playing_the_game", "actions",
    "character_creation", "combat",
}


# =============================================================================
# HTML TEXT EXTRACTION
# =============================================================================

class HTMLTextExtractor(HTMLParser):
    """Extract plain text from HTML, preserving markdown-style formatting."""

    def __init__(self) -> None:
        super().__init__()
        self.text_parts: List[str] = []
        self.in_bold = False
        self.in_italic = False

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        if tag in ("b", "strong"):
            self.text_parts.append("**")
            self.in_bold = True
        elif tag in ("i", "em"):
            self.text_parts.append("*")
            self.in_italic = True
        elif tag == "br":
            self.text_parts.append("\n")
        elif tag == "p":
            if self.text_parts and not self.text_parts[-1].endswith("\n"):
                self.text_parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in ("b", "strong") and self.in_bold:
            self.text_parts.append("**")
            self.in_bold = False
        elif tag in ("i", "em") and self.in_italic:
            self.text_parts.append("*")
            self.in_italic = False
        elif tag == "p":
            self.text_parts.append("\n")

    def handle_data(self, data: str) -> None:
        self.text_parts.append(data)

    def get_text(self) -> str:
        return "".join(self.text_parts).strip()


def extract_text_from_html(html: str) -> str:
    """Extract plain text from HTML content."""
    if not html:
        return ""
    parser = HTMLTextExtractor()
    try:
        parser.feed(html)
        return parser.get_text()
    except Exception:
        # Fallback: strip tags with regex
        text = re.sub(r"<[^>]+>", " ", html)
        return re.sub(r"\s+", " ", text).strip()


# =============================================================================
# TTRPG CLASSIFICATION FUNCTIONS
# =============================================================================

def normalize_space(text: str) -> str:
    """Collapse whitespace to single spaces."""
    return re.sub(r"\s+", " ", text).strip()


def extract_tags(section_path: List[str], text: str, allow_text: bool = True) -> List[str]:
    """Extract TTRPG-relevant tags from section path and text."""
    tags: List[str] = []
    lower_section = " ".join(section_path).lower()

    for key, tag in SECTION_TAGS.items():
        if key in lower_section:
            tags.append(tag)

    if allow_text:
        lower_text = text.lower()
        for key, tag in SECTION_TAGS.items():
            if key in lower_text and tag not in tags:
                tags.append(tag)

    # Filter to high-value tags
    tags = [t for t in tags if t in HIGH_VALUE_TAGS]
    return sorted(set(tags))


def is_rule_bearing(text: str) -> bool:
    """Check if text contains mechanical rule keywords."""
    lower = text.lower()
    return any(keyword in lower for keyword in RULE_KEYWORDS)


def contains_constraints(text: str) -> bool:
    """Check if text contains constraint keywords."""
    lower = text.lower()
    return any(keyword in lower for keyword in CONSTRAINT_KEYWORDS)


def extract_traits(text: str) -> List[str]:
    """Extract trait keywords from text (usually in ALL CAPS lines)."""
    traits: List[str] = []

    # Look for bold trait lines like **CONCENTRATE MANIPULATE VOID**
    trait_pattern = r"\*\*([A-Z][A-Z\s]+)\*\*"
    matches = re.findall(trait_pattern, text)

    for match in matches:
        words = match.split()
        for word in words:
            word_lower = word.lower()
            if word_lower in TRAIT_KEYWORDS:
                traits.append(word.upper())

    return sorted(set(traits))


def extract_spell_rank(text: str) -> Optional[int]:
    """Extract spell rank from Marker output like 'SPELL 8' or 'CANTRIP 1'."""
    # Match **SPELL 8** or **CANTRIP 1**
    match = re.search(r"\*\*(?:SPELL|CANTRIP)\s+(\d+)\*\*", text, re.IGNORECASE)
    if match:
        return int(match.group(1))

    # Match SPELL 8 without markdown
    match = re.search(r"(?:SPELL|CANTRIP)\s+(\d+)", text, re.IGNORECASE)
    if match:
        return int(match.group(1))

    return None


def extract_traditions(text: str) -> List[str]:
    """Extract traditions from lines like '**Traditions** arcane, primal'."""
    match = re.search(r"\*\*Traditions\*\*\s+([^\n]+)", text, re.IGNORECASE)
    if match:
        traditions_str = match.group(1)
        traditions = re.split(r"[,;]", traditions_str)
        return [t.strip().lower() for t in traditions if t.strip()]

    # Fallback without markdown
    match = re.search(r"Traditions\s+([^\n]+)", text, re.IGNORECASE)
    if match:
        traditions_str = match.group(1)
        traditions = re.split(r"[,;]", traditions_str)
        return [t.strip().lower() for t in traditions if t.strip()]

    return []


def extract_spell_titles_from_markdown(markdown_text: str) -> List[str]:
    """Extract spell names from Marker markdown output."""
    pattern = r"^\*\*([A-Z][A-Z0-9\s'\-]+)\*\*(?:\s*\[.*?\])?\s*\*\*(SPELL|CANTRIP)\s+\d+\*\*"
    matches = re.findall(pattern, markdown_text, flags=re.MULTILINE)
    names = []
    for name, _ in matches:
        cleaned = normalize_space(name.replace("*", "")).strip()
        if cleaned:
            names.append(cleaned.upper())
    return names


def extract_spell_title_from_text(text: str) -> Optional[str]:
    """Extract a spell name from enriched chunk text."""
    if not text:
        return None
    pattern = r"\*\*([A-Z][A-Z0-9\s'\-]+)\*\*(?:\s*\[.*?\])?\s*\*\*(SPELL|CANTRIP)\s+\d+\*\*"
    match = re.search(pattern, text)
    if match:
        return normalize_space(match.group(1)).strip().upper()
    return None


def extract_feat_titles_from_markdown(markdown_text: str) -> List[str]:
    """Extract feat names from Marker markdown output."""
    pattern = r"^\*\*([A-Z][A-Z0-9\s'\-]+)\*\*\s*\*\*FEAT\s+\d+\*\*"
    matches = re.findall(pattern, markdown_text, flags=re.MULTILINE)
    names = []
    for name in matches:
        cleaned = normalize_space(name.replace("*", "")).strip()
        if cleaned:
            names.append(cleaned.upper())
    return names


def extract_feat_title_from_text(text: str) -> Optional[str]:
    """Extract a feat name from enriched chunk text."""
    if not text:
        return None
    pattern = r"\*\*([A-Z][A-Z0-9\s'\-]+)\*\*\s*\*\*FEAT\s+\d+\*\*"
    match = re.search(pattern, text)
    if match:
        return normalize_space(match.group(1)).strip().upper()
    return None


# =============================================================================
# METRICS & REVIEW
# =============================================================================

def _regex_count(markdown_text: str, pattern: str) -> int:
    return len(re.findall(pattern, markdown_text, flags=re.MULTILINE))


def _normalize_title(text: str) -> str:
    cleaned = normalize_space(text).strip()
    # Remove markdown emphasis
    cleaned = cleaned.replace("*", "")
    # Remove action icons like [two-actions]
    cleaned = re.sub(r"\[[^\]]+\]", " ", cleaned)
    # Remove common type suffixes (SPELL 4, CANTRIP 1, FEAT 2)
    cleaned = re.sub(r"\b(SPELL|CANTRIP|FEAT)\s+\d+\b", " ", cleaned, flags=re.IGNORECASE)
    # Remove leading numeric prefixes like "CHAPTER 7:" or "7."
    cleaned = re.sub(r"^(CHAPTER|PART|SECTION)\s+\d+\s*[:\-]?\s*", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"^\d+\s*[:\.\-]?\s*", "", cleaned)
    # Strip non-title characters
    cleaned = re.sub(r"[^A-Za-z0-9\s'\-]", "", cleaned)
    return normalize_space(cleaned).upper()


def extract_toc_titles_from_markdown(markdown_text: str) -> List[str]:
    """Extract likely TOC section titles from Marker markdown output."""
    heading_titles: List[str] = []
    bold_titles: List[str] = []
    lines = markdown_text.splitlines()

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        # Bold headings like **SPELLS**
        bold_match = re.match(r"^\*\*([^*]+)\*\*$", stripped)
        if bold_match:
            raw = bold_match.group(1)
            # Skip spell/feat title lines
            if re.search(r"\b(SPELL|CANTRIP|FEAT)\b", raw, flags=re.IGNORECASE):
                continue
            # Skip lines with lowercase words (likely list entries)
            if re.search(r"[a-z]", raw):
                continue
            title = _normalize_title(raw)
            # Prefer shorter TOC-style headings
            if title and len(title) <= 40:
                bold_titles.append(title)
            continue

        # Markdown headings like # CHAPTER 7: SPELLS
        md_match = re.match(r"^#{1,6}\s+(.+)$", stripped)
        if md_match:
            raw = md_match.group(1)
            if re.search(r"\b(SPELL|CANTRIP|FEAT)\b", raw, flags=re.IGNORECASE):
                continue
            title = _normalize_title(raw)
            if title and len(title) <= 60:
                heading_titles.append(title)

    # Prefer explicit markdown headings, fallback to bold headings
    titles = heading_titles if heading_titles else bold_titles

    # Deduplicate while preserving order
    seen = set()
    unique = []
    for t in titles:
        if t not in seen:
            seen.add(t)
            unique.append(t)
    return unique


def extract_section_titles_from_chunks(raw_chunks: List[Dict[str, Any]]) -> List[str]:
    """Extract section titles from JSON block types and section hierarchy."""
    titles: List[str] = []

    for chunk in raw_chunks:
        if chunk.get("block_type") == "SectionHeader":
            text = extract_text_from_html(chunk.get("html", ""))
            title = _normalize_title(text)
            if title:
                titles.append(title)

    # Deduplicate while preserving order
    seen = set()
    unique = []
    for t in titles:
        if t not in seen:
            seen.add(t)
            unique.append(t)
    return unique


def build_metrics_report(
    markdown_path: str,
    raw_chunks: List[Dict[str, Any]],
    enriched_chunks: List["EnrichedChunk"],
    doc_id: str,
) -> Dict[str, Any]:
    """Build a metrics report comparing JSON extraction to markdown regex counts."""
    markdown_path = Path(markdown_path)
    if not markdown_path.exists():
        raise FileNotFoundError(f"Markdown source not found: {markdown_path}")

    markdown_text = markdown_path.read_text(encoding="utf-8")

    # JSON counts by block type
    block_type_counts = Counter()
    for chunk in raw_chunks:
        block_type = chunk.get("block_type", "Unknown")
        block_type_counts[block_type] += 1

    # Enriched counts by content kind
    content_kind_counts = Counter()
    for chunk in enriched_chunks:
        content_kind_counts[chunk.content_kind] += 1

    # Markdown regex counts
    regex_patterns = [
        {"name": "markdown_heading", "pattern": r"^#{1,6}\s+"},
        {"name": "bold_heading", "pattern": r"^\*\*.+\*\*$"},
        {"name": "table_row", "pattern": r"^\|.*\|$"},
        {"name": "spell_title", "pattern": r"^\*\*[A-Z][A-Z0-9\s'\-]+\*\*(?:\s*\[.*?\])?\s*\*\*(SPELL|CANTRIP)\s+\d+\*\*"},
        {"name": "feat_title", "pattern": r"^\*\*[A-Z][A-Z0-9\s'\-]+\*\*\s*\*\*FEAT\s+\d+\*\*"},
    ]
    regex_counts = {p["name"]: _regex_count(markdown_text, p["pattern"]) for p in regex_patterns}

    # Dynamic TOC/section review
    toc_titles = extract_toc_titles_from_markdown(markdown_text)
    section_titles = extract_section_titles_from_chunks(raw_chunks)

    toc_title_counts = {}
    for title in toc_titles:
        if not title:
            continue
        pattern = rf"\\b{re.escape(title)}\\b"
        toc_title_counts[title] = _regex_count(markdown_text, pattern)

    section_title_counts = {}
    for title in section_titles:
        if not title:
            continue
        pattern = rf"\\b{re.escape(title)}\\b"
        section_title_counts[title] = _regex_count(markdown_text, pattern)

    # Titles missing from markdown or sections
    toc_title_set = set(toc_titles)
    section_title_set = set(section_titles)
    missing_toc_in_sections = sorted(toc_title_set - section_title_set)[:100]
    extra_section_titles = sorted(section_title_set - toc_title_set)[:100]

    # Direct title extraction (more accurate for spells/feats)
    markdown_spell_titles = extract_spell_titles_from_markdown(markdown_text)
    markdown_feat_titles = extract_feat_titles_from_markdown(markdown_text)

    enriched_spell_titles = [
        extract_spell_title_from_text(c.text)
        for c in enriched_chunks
        if c.content_kind == "spell"
    ]
    enriched_spell_titles = [t for t in enriched_spell_titles if t]

    enriched_feat_titles = [
        extract_feat_title_from_text(c.text)
        for c in enriched_chunks
        if c.content_kind == "feat"
    ]
    enriched_feat_titles = [t for t in enriched_feat_titles if t]

    markdown_spell_set = set(markdown_spell_titles)
    markdown_feat_set = set(markdown_feat_titles)
    enriched_spell_set = set(enriched_spell_titles)
    enriched_feat_set = set(enriched_feat_titles)

    # Coverage comparisons
    comparisons = [
        {
            "name": "spell_titles",
            "markdown_count": len(markdown_spell_titles),
            "enriched_count": len(enriched_spell_titles),
            "missing_in_enriched": sorted(markdown_spell_set - enriched_spell_set)[:50],
            "extra_in_enriched": sorted(enriched_spell_set - markdown_spell_set)[:50],
        },
        {
            "name": "feat_titles",
            "markdown_count": len(markdown_feat_titles),
            "enriched_count": len(enriched_feat_titles),
            "missing_in_enriched": sorted(markdown_feat_set - enriched_feat_set)[:50],
            "extra_in_enriched": sorted(enriched_feat_set - markdown_feat_set)[:50],
        },
    ]

    # Coverage thresholds
    min_coverage = 0.99
    coverage_results = []

    def _coverage(name: str, total: int, missing: int) -> Dict[str, Any]:
        ratio = 1.0 if total == 0 else (total - missing) / total
        result = {
            "name": name,
            "total": total,
            "missing": missing,
            "coverage": round(ratio, 4),
            "min_required": min_coverage,
            "passes": ratio >= min_coverage,
        }
        return result

    coverage_results.append(
        _coverage("toc_titles_vs_sections", len(toc_title_set), len(missing_toc_in_sections))
    )

    # Compare markdown headings to SectionHeader count (proxy for structure coverage)
    section_header_count = block_type_counts.get("SectionHeader", 0)
    markdown_heading_count = regex_counts.get("markdown_heading", 0) + regex_counts.get("bold_heading", 0)
    missing_heading = max(section_header_count - markdown_heading_count, 0)
    coverage_results.append(
        _coverage("section_headers_vs_markdown_headings", section_header_count, missing_heading)
    )

    # Enforce strict coverage
    failed = [c for c in coverage_results if not c["passes"]]
    if failed:
        failure_summary = ", ".join(
            f"{c['name']}={c['coverage']:.2%}" for c in failed
        )
        raise ValueError(
            f"Coverage check failed (< {min_coverage:.0%}): {failure_summary}"
        )

    # Review config for adaptive checks
    review_config = {
        "doc_id": doc_id,
        "json_block_type_counts": dict(block_type_counts),
        "enriched_content_kind_counts": dict(content_kind_counts),
        "toc_titles": toc_titles,
        "section_titles": section_titles,
        "toc_title_counts_in_markdown": toc_title_counts,
        "section_title_counts_in_markdown": section_title_counts,
        "missing_toc_in_sections": missing_toc_in_sections,
        "extra_section_titles": extra_section_titles,
        "markdown_regex_patterns": regex_patterns,
        "markdown_regex_counts": regex_counts,
        "comparisons": comparisons,
        "coverage_results": coverage_results,
        "notes": [
            "Counts are approximate; Markdown patterns depend on formatting.",
            "Use comparisons.missing_in_enriched to prioritize manual review.",
            "Use missing_toc_in_sections to spot TOC headings not found in sections.",
            f"Minimum coverage enforced: {min_coverage:.0%}.",
        ],
    }

    return review_config


def extract_spell_stats(text: str) -> Dict[str, str]:
    """Extract spell statistics (Range, Targets, Defense, etc.)."""
    stats: Dict[str, str] = {}

    # Pattern for **Key** value or **Key** value; **Key2** value2
    for prefix in SPELL_STAT_PREFIXES:
        pattern = rf"\*\*{prefix.title()}\*\*\s+([^*\n;]+)"
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            stats[prefix] = match.group(1).strip()

    return stats


def is_spell_block(text: str) -> bool:
    """Check if text appears to be a spell entry."""
    if re.search(r"\*\*(?:SPELL|CANTRIP)\s+\d+\*\*", text, re.IGNORECASE):
        return True
    if re.search(r"(?:SPELL|CANTRIP)\s+\d+", text, re.IGNORECASE):
        return True
    if re.search(r"\*\*Traditions\*\*", text, re.IGNORECASE):
        return True
    return False


def is_feat_block(text: str) -> bool:
    """Check if text appears to be a feat entry."""
    if re.search(r"\*\*FEAT\s+\d+\*\*", text, re.IGNORECASE):
        return True
    if re.search(r"\*\*Prerequisites?\*\*", text, re.IGNORECASE):
        return True
    return False


def classify_content(text: str, section_path: List[str], block_type: str) -> str:
    """Classify block as spell/feat/item/rule/narrative/table."""
    if block_type == "Table":
        return "table"
    if block_type == "Picture":
        return "image"

    if is_spell_block(text):
        return "spell"
    if is_feat_block(text):
        return "feat"
    if contains_constraints(text):
        return "rule"
    if is_rule_bearing(text):
        return "rule"

    section_str = " ".join(section_path).lower()
    if "spell" in section_str:
        return "spell"
    if "feat" in section_str:
        return "feat"
    if "equipment" in section_str or "item" in section_str:
        return "item"

    return "narrative"


def build_section_path(section_hierarchy: Dict[str, Any]) -> List[str]:
    """Build a flat section path from Marker's nested section_hierarchy."""
    if not section_hierarchy:
        return []

    path: List[str] = []

    def extract_titles(node: Any) -> None:
        if isinstance(node, dict):
            if "title" in node:
                path.append(node["title"])
            for key, value in node.items():
                if key != "title":
                    extract_titles(value)
        elif isinstance(node, list):
            for item in node:
                extract_titles(item)

    extract_titles(section_hierarchy)
    return path


# =============================================================================
# ENRICHED CHUNK DATA STRUCTURE
# =============================================================================

@dataclass
class EnrichedChunk:
    """Marker chunk enhanced with TTRPG metadata."""

    id: str
    block_type: str
    text: str
    page: int
    bbox: List[float] = field(default_factory=list)
    section_hierarchy: Dict[str, Any] = field(default_factory=dict)

    content_kind: str = "narrative"  # spell, feat, item, rule, narrative, table, image
    is_rule_bearing: bool = False
    tags: List[str] = field(default_factory=list)
    traits: List[str] = field(default_factory=list)
    spell_rank: Optional[int] = None
    traditions: List[str] = field(default_factory=list)
    spell_stats: Dict[str, str] = field(default_factory=dict)
    section_path: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def is_trait_line(text: str) -> bool:
    """Check if text is a trait line (ALL CAPS words that are trait keywords)."""
    clean = re.sub(r"\*\*", "", text).strip()
    if not clean:
        return False

    words = clean.split()
    if not words:
        return False

    upper_words = [w for w in words if w.isupper()]
    trait_hits = sum(1 for w in words if w.lower() in TRAIT_KEYWORDS)
    return len(upper_words) >= 2 and trait_hits >= 1


def is_spell_entry_title(text: str) -> bool:
    """Check if text looks like a spell entry title line."""
    if not text:
        return False
    pattern = r"\*\*[A-Z][A-Z\s']+\*\*(?:\s*\[.*?\])?\s*\*\*(SPELL|CANTRIP)\s+\d+\*\*"
    return re.search(pattern, text) is not None


def is_spell_continuation(chunk: "EnrichedChunk") -> bool:
    """Check if a chunk is likely a continuation of a spell entry."""
    if chunk.block_type in {"SectionHeader", "Title"}:
        return False
    if is_spell_entry_title(chunk.text):
        return False
    lowered = chunk.text.strip().lower()
    return lowered.startswith(
        ("you ", "the ", "if ", "this ", "targets ", "range ", "defense ", "heightened")
    )


def merge_spell_chunks(chunks: List[EnrichedChunk]) -> List[EnrichedChunk]:
    """Merge adjacent spell-related chunks into complete spell entries."""
    if not chunks:
        return chunks

    merged: List[EnrichedChunk] = []
    current_spell: Optional[EnrichedChunk] = None
    spell_page: Optional[int] = None
    blocks_since_spell: int = 0
    max_blocks_to_merge: int = 10

    for chunk in chunks:
        if not chunk.text.strip():
            if current_spell is not None:
                blocks_since_spell += 1
            continue

        is_spell_title = (
            chunk.content_kind == "spell"
            and chunk.spell_rank is not None
            and is_spell_entry_title(chunk.text)
        )

        if is_spell_title:
            if current_spell is not None:
                merged.append(current_spell)

            current_spell = chunk
            spell_page = chunk.page
            blocks_since_spell = 0

        elif current_spell is not None and blocks_since_spell < max_blocks_to_merge:
            is_adjacent = (
                chunk.page is not None
                and spell_page is not None
                and abs(chunk.page - spell_page) <= 1
            )

            is_spell_content = (
                chunk.traditions
                or chunk.content_kind in ("spell", "rule")
                or any(prefix in chunk.text.lower() for prefix in SPELL_STAT_PREFIXES)
                or "heightened" in chunk.text.lower()
                or is_trait_line(chunk.text)
            )

            new_spell_title = (
                chunk.content_kind == "spell"
                and chunk.spell_rank is not None
                and is_spell_entry_title(chunk.text)
            )

            if new_spell_title:
                merged.append(current_spell)
                current_spell = chunk
                spell_page = chunk.page
                blocks_since_spell = 0
            elif is_adjacent and (is_spell_content or is_spell_continuation(chunk)):
                current_spell.text += "\n\n" + chunk.text
                if chunk.traditions and not current_spell.traditions:
                    current_spell.traditions = chunk.traditions
                if chunk.traits:
                    current_spell.traits = list(set(current_spell.traits + chunk.traits))
                if is_trait_line(chunk.text):
                    new_traits = extract_traits(chunk.text)
                    current_spell.traits = list(set(current_spell.traits + new_traits))
                if chunk.spell_stats:
                    current_spell.spell_stats.update(chunk.spell_stats)
                current_spell.spell_stats = extract_spell_stats(current_spell.text)
                if not current_spell.traditions:
                    current_spell.traditions = extract_traditions(current_spell.text)
                blocks_since_spell += 1
            else:
                merged.append(current_spell)
                current_spell = None
                spell_page = None
                blocks_since_spell = 0
                merged.append(chunk)
        else:
            if current_spell is not None:
                merged.append(current_spell)
                current_spell = None
                spell_page = None
                blocks_since_spell = 0
            merged.append(chunk)

    if current_spell is not None:
        merged.append(current_spell)

    return merged


def coalesce_chunks(
    chunks: List[EnrichedChunk],
    min_chars: int = 400,
    max_chars: int = 800,
) -> List[EnrichedChunk]:
    """Merge adjacent chunks until a minimum length is reached."""
    if not chunks:
        return []

    coalesced: List[EnrichedChunk] = []
    buffer: List[EnrichedChunk] = []
    buffer_len = 0

    def _flush() -> None:
        nonlocal buffer_len
        if not buffer:
            return
        text_parts = [c.text for c in buffer if c.text]
        merged_text = "\n\n".join(text_parts)
        content_kinds = {c.content_kind for c in buffer}
        spell_stats = (
            buffer[0].spell_stats
            if len({tuple(c.spell_stats.items()) for c in buffer}) == 1
            else {}
        )
        merged = EnrichedChunk(
            id=f"coalesced-{buffer[0].id}",
            block_type="Coalesced",
            text=merged_text,
            page=buffer[0].page,
            bbox=buffer[0].bbox,
            section_hierarchy=buffer[0].section_hierarchy,
            content_kind=buffer[0].content_kind if len(content_kinds) == 1 else "mixed",
            is_rule_bearing=any(c.is_rule_bearing for c in buffer),
            tags=sorted({tag for c in buffer for tag in c.tags}),
            traits=sorted({trait for c in buffer for trait in c.traits}),
            spell_rank=buffer[0].spell_rank if len({c.spell_rank for c in buffer}) == 1 else None,
            traditions=sorted({t for c in buffer for t in c.traditions}),
            spell_stats=spell_stats,
            section_path=buffer[0].section_path,
        )
        coalesced.append(merged)
        buffer.clear()
        buffer_len = 0

    for chunk in chunks:
        if not chunk.text.strip():
            continue

        is_header = chunk.block_type in {"SectionHeader", "Title"}
        section_changed = (
            buffer
            and chunk.section_path
            and buffer[0].section_path
            and chunk.section_path != buffer[0].section_path
        )

        if is_header and buffer:
            _flush()

        if section_changed and buffer_len >= min_chars:
            _flush()

        proposed_len = buffer_len + len(chunk.text)
        if buffer and buffer_len >= min_chars and proposed_len > max_chars:
            _flush()

        buffer.append(chunk)
        buffer_len += len(chunk.text)

        if buffer_len >= max_chars:
            _flush()

    _flush()
    return coalesced


# =============================================================================
# GRAPH BUILDING
# =============================================================================

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


def _slugify_name(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    return slug


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
    chunks: List[EnrichedChunk], resolved_config: Optional["RulesetConfiguration"]
) -> Dict[str, str]:
    alias_map: Dict[str, str] = {}
    deterministic_rules = (resolved_config.deterministic_rules or {}) if resolved_config else {}
    config_aliases = deterministic_rules.get("entity_aliases", {})

    if isinstance(config_aliases, dict):
        for alias, canonical in config_aliases.items():
            alias_norm = _normalize_entity_name(str(alias))
            canonical_norm = _normalize_entity_name(str(canonical))
            if alias_norm and canonical_norm:
                alias_map[alias_norm] = canonical_norm
    elif isinstance(config_aliases, list):
        for entry in config_aliases:
            if not isinstance(entry, dict):
                continue
            alias = _normalize_entity_name(str(entry.get("alias", "")))
            canonical = _normalize_entity_name(str(entry.get("canonical", "")))
            if alias and canonical:
                alias_map[alias] = canonical

    derived_aliases: Dict[str, str] = {}
    for chunk in chunks:
        for alias_raw, canonical_raw in _extract_alias_pairs(chunk.text):
            alias_norm = _normalize_entity_name(alias_raw)
            canonical_norm = _normalize_entity_name(canonical_raw)
            if not _is_reasonable_canonical(canonical_norm):
                continue
            if alias_norm and canonical_norm and alias_norm != canonical_norm:
                derived_aliases[alias_norm] = canonical_norm

    return _merge_alias_map(alias_map, derived_aliases)


def _resolve_alias_name(name: str, alias_map: Dict[str, str]) -> Tuple[str, Optional[str]]:
    normalized = _normalize_entity_name(name)
    if not normalized:
        return "", None
    canonical = alias_map.get(normalized)
    if canonical and canonical != normalized:
        return canonical, normalized
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
    "Concept",
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
        normalized = _normalize_entity_name(name)
        if not normalized:
            continue
        index.setdefault(normalized, canonical_id)


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
                    "mentions_same_entity",
                    {"entity_id": entity_id},
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
    avg_alias_length = (
        round(sum(alias_lengths) / len(alias_lengths), 3) if alias_lengths else 0.0
    )

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
    resolved_config: Optional["RulesetConfiguration"] = None,
) -> Graph:
    """Build a doc → section → chunk graph with semantic entity nodes."""
    graph = Graph()
    resolved_ruleset_id = ruleset_id or doc_id

    # Add document node
    graph.add_node(
        doc_id,
        "document",
        {
            "name": doc_id,
            "ruleset_id": resolved_ruleset_id,
        },
    )

    # Track sections
    section_nodes: Dict[str, str] = {}
    prev_chunk_id: Optional[str] = None
    entity_nodes: Dict[str, str] = {}
    entity_ids_by_name: Dict[str, str] = {}
    entity_to_chunks: Dict[str, Set[str]] = {}

    alias_map = _build_entity_alias_map(chunks, resolved_config)

    for chunk in chunks:
        # Skip empty chunks
        if not chunk.text.strip():
            continue

        chunk_id = chunk.id

        # Add chunk node
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
                "extraction_method": "marker_enrichment",
            },
        )

        # Link chunk to document
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

        # Handle section hierarchy
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

        # Link sequential chunks
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

        # Semantic entity nodes
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
                        "canonical_id": canonical_id,
                        "ruleset_id": resolved_ruleset_id,
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
                # Update provenance on existing entity node
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

        section_entity_type = _infer_section_entity_type(chunk)
        if section_entity_type and section_entity_type != entity_type:
            section_entity_name = _extract_section_entity_name(chunk)
            _add_entity_node(section_entity_type, section_entity_name)

        tag_entity_type = _infer_tag_entity_type(chunk)
        if (
            tag_entity_type
            and tag_entity_type != entity_type
            and tag_entity_type != section_entity_type
        ):
            tag_entity_name = _extract_tag_entity_name(chunk)
            _add_entity_node(tag_entity_type, tag_entity_name)

        if canonical_id:
            # Trait nodes
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

            # Tradition nodes
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

            # Spell rank nodes
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

            # Tag nodes
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

            # Spell stats nodes
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
                target_id = entity_ids_by_name.get(_normalize_entity_name(resolved_target))
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
                if target_id and chunk_id:
                    entity_to_chunks.setdefault(target_id, set()).add(chunk_id)

    _connect_chunks_by_entity(graph, entity_to_chunks)
    graph.stats = _summarize_graph(graph)
    _validate_graph(graph)
    return graph


def enrich_chunk(chunk: Dict[str, Any]) -> EnrichedChunk:
    """Add TTRPG metadata to a Marker chunk."""
    html = chunk.get("html", "")
    text = extract_text_from_html(html)

    section_hierarchy = chunk.get("section_hierarchy", {})
    section_path = build_section_path(section_hierarchy)

    block_type = chunk.get("block_type", "Text")
    content_kind = classify_content(text, section_path, block_type)

    spell_rank = None
    traditions: List[str] = []
    spell_stats: Dict[str, str] = {}

    if content_kind == "spell":
        spell_rank = extract_spell_rank(text)
        traditions = extract_traditions(text)
        spell_stats = extract_spell_stats(text)

    return EnrichedChunk(
        id=chunk.get("id", str(uuid.uuid4())),
        block_type=block_type,
        text=text,
        page=chunk.get("page", 0),
        bbox=chunk.get("bbox", []),
        section_hierarchy=section_hierarchy,
        content_kind=content_kind,
        is_rule_bearing=is_rule_bearing(text),
        tags=extract_tags(section_path, text),
        traits=extract_traits(text),
        spell_rank=spell_rank,
        traditions=traditions,
        spell_stats=spell_stats,
        section_path=section_path,
    )
