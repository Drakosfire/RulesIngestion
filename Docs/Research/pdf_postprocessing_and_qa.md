
# Post-Processing and QA for Parsed TTRPG PDFs

This guide outlines best practices for cleaning, validating, and structuring content extracted from TTRPG rulebooks after OCR or parsing.

## Key Objectives

- Clean layout artifacts (multi-column order, hyphenation, footers)
- Structure documents into meaningful entities
- Normalize tables and styled text
- Ensure data quality with QA metrics and visual validation

## Post-Processing Techniques

### Paragraph Reconstruction
- Merge broken lines across columns or pages
- Remove OCR-induced hyphenation
- Preserve correct reading order using layout geometry

### Semantic Segmentation
- Heuristic or LLM-based classification of text blocks: rules, flavor, stat blocks
- Use of document hierarchy (chapter headers) to infer context

### Table Recovery
- Normalize column alignment
- Merge multiline rows
- Remove footers injected as fake rows
- Export as CSV or schema-mapped JSON

### Style Interpretation
- Bold: field labels (e.g. “Armor Class”)
- Italics: conditions, spells, emphasis
- Small caps / underline: semantic signals if captured by OCR

### Entity Structuring
- Convert structured text into domain models (e.g., spells, monsters)
- Use regular expressions or prompt-guided LLMs with schema validation

### Reference Linking
- Detect and normalize page references (“see page 250”)
- Link entity mentions using lookup tables or fuzzy match

## QA Strategies

### Schema Validation
- Use JSON schema or Pydantic models
- Detect missing fields, type mismatches, pattern errors

### OCR Artifact Detection
- Spellcheck + domain dictionary
- Detect common misreads (e.g., “1” vs “l”, “O” vs “0”)

### Visual QA
- Side-by-side PDF and text renderers
- Overlay bounding boxes on original scans

### Manual Review
- Confidence thresholds for human intervention
- Editable interfaces showing source + parsed output

### Metrics
- Character Error Rate (CER)
- Structural similarity (e.g., heading/tables retained)
- Validation error density (per page, per field)

## Tools Recommended

- layoutparser
- pdfplumber / PyMuPDF
- Energent, Trieve, or Docling for visualization
