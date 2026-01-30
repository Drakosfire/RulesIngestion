# RulesIngestion

Tools for ingesting tabletop rulebooks into structured, deterministic artifacts used by
DungeonMind and RulesLawyer (enriched chunks, graphs, and evaluation assets).

## Quick start

```bash
# Recommended: full pipeline with auto-config
uv run python ingest.py \
  --ruleset StarFinder2e \
  --ruleset-id sf2e-galaxyguide \
  --book GalaxyGuide \
  --profile full \
  --auto-config
```

## Entry points

- `ingest.py` - primary CLI with `full`, `enrich-only`, and `eval-only` profiles
- `rules_ingestion_pipeline.py` - legacy lower-level pipeline (use `ingest.py` unless needed)
- `ingestion_service.py` - FastAPI service wrapper for ingestion jobs
- `main.py` - thin CLI wrapper around the pipeline

## What the pipeline produces

- Enriched chunks with TTRPG metadata (content kind, tags, traits)
- Deterministic graph edges for traversal and eligibility
- Evaluation queries and reports for retrieval benchmarking
- Ruleset configs for system-specific extraction behavior

## Common workflows

```bash
# Re-enrich existing chunks
uv run python ingest.py \
  --ruleset StarFinder2e \
  --book GalaxyGuide \
  --profile enrich-only \
  --run-dir Rules/StarFinder2e/GalaxyGuide/outputs/runs/<timestamp>

# Evaluation only (on an existing run)
uv run python ingest.py \
  --ruleset StarFinder2e \
  --book GalaxyGuide \
  --profile eval-only \
  --run-dir Rules/StarFinder2e/GalaxyGuide/outputs/runs/<timestamp>
```

## Output layout

Runs and configs live under each ruleset/book:

```
Rules/<Ruleset>/<Book>/outputs/
├── configs/<ruleset-id>/
└── runs/<timestamp>/
    ├── marker_raw/
    ├── enriched/
    └── reports/
```

## Configuration and environment

- `--auto-config` uses LLM-backed config generation
- `MONGODB_URI` enables config/run persistence
- `OPENAI_API_KEY` is required for LLM config generation and LLM enrichment

## Evaluation

Retrieval evaluation is run via the RulesLawyer harness in `DungeonMindServer`.
See `Docs/rule_ingestion_evaluation_criteria.md` and
`Docs/ingestion_polishing_guidebook.md` for metrics and baselines.

## Documentation

### Core Documentation (Start Here)

- `Docs/ARCHITECTURE.md` - System architecture, module map, dependencies
- `Docs/INGESTION_PIPELINE.md` - Pipeline stages, entry points, transformations
- `Docs/RETRIEVAL_END_TO_END.md` - How RulesLawyer uses ingested data
- `Docs/CLEANUP_RECOMMENDATIONS.md` - Technical debt and improvement opportunities

### Reference Documentation

- `Docs/rule_ingestion_philosophy.md` - Design principles
- `Docs/ingestion_polishing_guidebook.md` - Operational reference
- `Docs/rule_ingestion_evaluation_criteria.md` - Evaluation metrics
- `Docs/manual_end_to_end_galaxy_guide.md` - Step-by-step walkthrough

### Deprecated (see new docs above)

- ~~`Docs/rule_ingestion_pipeline_overview.md`~~ → Use `INGESTION_PIPELINE.md`
- ~~`Docs/rules_ingestion_architecture.md`~~ → Use `ARCHITECTURE.md`
- ~~`Docs/rules_ingestion_cleanup_plan.md`~~ → Use `CLEANUP_RECOMMENDATIONS.md`

## Testing

```bash
uv run pytest tests/
```

> We maintain a static rule graph that encodes mechanics, states, and procedures without time.  
> A separate immutable frame timeline carries concrete world state.  
> For each query or tick, we traverse the rule graph to determine which procedures are legal, modified, or blocked given the current frame state.  
> Traversal never mutates state.  
> Only after a procedure is selected do we commit symbolic effects to produce the next frame.  
> Procedures are the sole bridge between rule semantics and temporal state change.
