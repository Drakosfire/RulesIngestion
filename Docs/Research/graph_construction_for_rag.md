
# Graph Construction for Enhanced Retrieval in TTRPG RAG Systems

This guide details how to build and apply knowledge graphs from parsed TTRPG rulebooks to enhance retrieval quality in a Retrieval-Augmented Generation (RAG) system.

## Objectives

- Structure TTRPG content into graph-based formats
- Support entity linking, disambiguation, and reference resolution
- Integrate graph-enhanced retrieval with vector-based search
- Align with the World Engine Contract schema

## Graph Design

### Node Types

- `Spell`, `Monster`, `Item`, `Condition`, `Class`, `Feat`, `Ability`, `Rule`
- `Section`, `Chapter`, `Table`, `Paragraph`

### Edge Types

- `has_effect`, `requires_level`, `grants_ability`, `belongs_to`, `references`
- `cites_rule`, `uses_spell`, `in_table`, `aliases`, `contradicts`

### Entity Extraction

- From structured JSON (using headings and labels)
- NLP-enhanced:
  - Named Entity Recognition (NER)
  - Coreference resolution
  - Heuristics for stat block parsing

### Schema Alignment

- Use foundational schema (e.g., World Engine Contract v1.1)
- Align entity types, field names, and nested relationships

## Storage & Query

### Options

- **Neo4j** with Cypher: full graph traversal, entity reasoning
- **MongoDB** with `$graphLookup`: embedded tree joins
- **PostgreSQL** + pgvector + recursive CTEs or graph extensions
- **Embedded graphs** using NetworkX or RDFLib for in-memory traversal

### Query Interfaces

- Expose filtered traversals (e.g., “all spells that cause paralysis and belong to school of necromancy”)
- Provide API endpoints for common node+relation queries
- Build DSL or query templates for LLM chaining

## Retrieval Enhancement

### Graph-Augmented Retrieval (GAR)

- Use connected nodes to enrich retrieval context (e.g., get related rules when a spell is retrieved)
- Node-centric: retrieve documents linked to query-matched nodes
- Path-centric: retrieve based on reasoning chains or rules

### Graph Embeddings

- Use Node2Vec, GraphSAGE, or Knowledge Graph Embedding models
- Embed nodes into dense space for hybrid vector + symbolic search
- Use embeddings as filters or reranking signals

### RAG Integration

- Use graph for:
  - Clarifying ambiguous queries (“Which resistances do dragons have?”)
  - Expanding context windows for better generation
  - Filtering document retrieval based on connectedness

## Maintenance & QA

- Keep graph in sync with evolving corpus (detect drift)
- Validate edges using string matching, pattern checks, and crowd labels
- Normalize synonyms and aliases (e.g., “firebolt” == “fire bolt”)

## Tooling

- Neo4j Bloom, Graphistry for visualization
- GraphQL APIs over graph databases
- Python graph toolkits for extraction and patching (NetworkX, RDFLib)
