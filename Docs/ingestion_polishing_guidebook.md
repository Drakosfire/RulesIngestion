# Rules Ingestion Polishing Guidebook
**Date:** 2026-01-22

## Purpose
This guidebook captures the current goal and progress for polishing the rules ingestion pipeline so it yields rich, reliable chunks for hybrid search and high-quality graph construction. It focuses on deterministic extraction, metadata enrichment, and adaptive review to make downstream stages (rule units, typed decomposition, rule graph) safer and more accurate.

This is a living reference for the ingestion polish work, not a task list.

## Goal (Distilled)
Produce chunked content that is:
- Extracted with high-fidelity structure (Marker)
- Tagged with structured metadata to support hybrid search
- Structured to support graph traversal and rule unit extraction
- Deterministically reproducible
- Verified with adaptive, 99% coverage gates

## Scope and Boundaries
**In scope:**
- Deterministic extraction (Marker JSON + markdown)
- Deterministic metadata tagging (content kind, tags, traits, spell stats)
- Chunk graph enrichment (document → section → chunk)
- Adaptive review metrics (JSON counts vs markdown regex counts)

**Out of scope:**
- LLM-driven rule evaluation or conflict resolution
- Non-deterministic semantic inference at runtime

## Core Files
- `RulesIngestion/rules_ingestion_pipeline.py`: Marker + enrichment + graph + metrics
- `RulesIngestion/Rules/.../outputs/marker_eval/*.md`: Marker markdown output
- `RulesIngestion/Rules/.../outputs/marker_eval_chunks/*.json`: Marker chunks output
- `RulesIngestion/Rules/.../outputs/enriched/*.enriched.json`: enriched chunk store (RAG input)
- `RulesIngestion/Rules/.../outputs/enriched/*.graph.json`: enriched graph
- `RulesIngestion/Rules/.../outputs/enriched/*.metrics.json`: adaptive review metrics

## Output Layout (Recommended)
Keep `Rules/.../outputs/` clean by nesting per-run folders. The pipeline writes into
whatever `--output-dir` you pass, so point it at a run folder:
```
Rules/.../outputs/
  configs/
    <ruleset_id>/
      v001.config.json
  runs/
    2026-01-22_114-125/
      marker_raw/
      enriched/
        <doc_id>.enriched.json
        <doc_id>.coalesced.json
        <doc_id>.graph.json
        <doc_id>.evaluation_queries.json
        <doc_id>.llm_paragraphs.json
        <doc_id>.llm_review.json
        <doc_id>.metrics.json
  experiments/
```

## MongoDB Storage Layout (Canonical)
Rules ingestion records live in `rules_ingestion` (or `RULES_INGESTION_DB_NAME`):
- `ruleset_configs`
- `ruleset_profiles`
- `enrichment_runs`
- `run_inputs`
- `run_outputs`

Benchmark records live in `ruleslawyer` (or `RULESLAWYER_DB_NAME`):
- `embedding_runs`
- `embedding_chunks`
- `evaluation_runs`

## How to Run

**End-to-end (PDF → Marker → Enrich → Graph → Metrics):**
```
cd /media/drakosfire/Projects/DungeonOverMind/RulesIngestion
uv run python rules_ingestion_pipeline.py "path/to/input.pdf" \
  --output-dir "path/to/outputs" \
  --doc-id "YourDocId" \
  --markdown-source "path/to/marker.md"
```

**Enrich-only (use existing Marker chunks):**
```
cd /media/drakosfire/Projects/DungeonOverMind/RulesIngestion
uv run python rules_ingestion_pipeline.py --enrich-only "path/to/marker_chunks.json" \
  --output-dir "path/to/outputs" \
  --doc-id "YourDocId" \
  --markdown-source "path/to/marker.md"
```

**Optional: LLM-assisted tables**
```
uv run python rules_ingestion_pipeline.py "path/to/input.pdf" \
  --use-llm \
  --output-dir "path/to/outputs"
```

**Expected outputs:**
- `.../enriched/<doc_id>.enriched.json`
- `.../enriched/<doc_id>.coalesced.json`
- `.../enriched/<doc_id>.graph.json`
- `.../enriched/<doc_id>.evaluation_queries.json`
- `.../enriched/<doc_id>.llm_paragraphs.json` (when `--llm-pre-enrich`)
- `.../enriched/<doc_id>.llm_review.json` (when `--llm-review`)
- `.../enriched/<doc_id>.metrics.json` (fails if coverage < 99%)

## Metadata Taxonomy (Current)
**Enriched chunk fields (`*.enriched.json`):**
- `id`, `block_type`, `text`, `page`, `bbox`
- `section_path`, `section_hierarchy`
- `content_kind`: spell | feat | item | rule | narrative | table | image
- `is_rule_bearing`, `tags`, `traits`
- `spell_rank`, `traditions`, `spell_stats`

**Enriched graph nodes and edges (`*.graph.json`):**
- document -> section -> chunk
- sequential `next` edges between chunks

## Deterministic Extraction and Enrichment (Implemented)
### Marker Extraction
Marker is the canonical extractor for PDF → markdown/JSON. It preserves critical TTRPG metadata (e.g., spell rank, traditions, range/targets/defense).

### TTRPG Enrichment
Blocks are enriched deterministically using:
- Vocabularies (SECTION_TAGS, RULE_KEYWORDS, TRAIT_KEYWORDS, etc.)
- Content classification: spell/feat/item/rule/narrative/table
- Spell metadata extraction (rank, traditions, stats)
- Trait extraction from uppercase trait lines

### Spell Block Merging
Adjacent spell-related blocks are merged into a single spell entry. This produces complete spell chunks suitable for embedding and retrieval.

### Graph Construction
Graph nodes point to chunk IDs (no text duplication):
```
document -> section -> chunk
chunk -> chunk (next)
```

## Current Observations
- Enriched chunk store is the canonical RAG input (`chunks[].text`).
- Graph is structural metadata only (pointers to chunk IDs).
- Marker chunks are sufficient for RAG; custom chunking is not required.
- Evaluation queries are generated from enriched chunks; evaluation should use the same chunk source.

## Adaptive Review and Confidence Gates
The pipeline produces `*.metrics.json`, which drives a dynamic review config:
- JSON block counts vs markdown regex counts
- TOC titles (markdown headings) vs section titles (JSON SectionHeader)
- **Hard failure if coverage < 99%**

**Why this matters:** ensures extraction accuracy across unrelated PDFs with varying structure.

## Enhancements (Deterministic vs Non-Deterministic)
These are prioritized notes for pipeline evolution. Deterministic steps should happen before any LLM pass.

### Deterministic (Top Priority)
- Adaptive review metrics for additional structures (tables, lists, images)
- Expand TOC/section normalization to handle unusual headings

### Deterministic (Nice to Have)
- Header/footer suppression by repetition
- TOC + nav rail cleanup
- Section path continuity when headings are missing
- Table detection and structured extraction

### Non-Deterministic (LLM / Semantic)
- Rule atom extraction for downstream reasoning
- Semantic chunking refinement
- Cross-reference resolution and entity normalization

### Hybrid Opportunities (Deterministic + LLM)
- Pre-filter noise deterministically, then run LLM tagging / rule-bearing on clean content.
- Use deterministic section/heading extraction to provide stable context windows for the LLM (reduces hallucination).

## LLM Role (When Used)
LLMs may be used for:
- Structural classification where deterministic rules are insufficient
- Semantic extraction into typed fields
- Summarization or explanation
LLMs must not be used for runtime rule evaluation or conflict resolution.

## Quick Validation Targets
When re-running with the source PDF:
- `*.metrics.json` passes 99% coverage gates
- Enriched chunks include `text`, `content_kind`, and `section_path`
- Graph points to chunk IDs (no text duplication)

## Retrieval Quality Scale (Evaluation Benchmarks)
Use this scale to interpret evaluation reports (hit@k / MRR) across models.
These are targets for the **first-pass benchmark** on a single ruleset.

**Baseline (Investigate)**:
- Coverage < 0.90 or MRR < 0.05
- hit@1 < 0.05 or hit@5 < 0.15

**Acceptable (MVP)**:
- Coverage >= 0.95
- MRR >= 0.15
- hit@1 >= 0.15
- hit@5 >= 0.35

**Good (Stable)**:
- Coverage >= 0.98
- MRR >= 0.30
- hit@1 >= 0.30
- hit@5 >= 0.55

**Excellent (Target)**:
- Coverage >= 0.99
- MRR >= 0.45
- hit@1 >= 0.45
- hit@5 >= 0.70

**Notes**:
- If coverage is low, validate chunk ID alignment (enriched vs coalesced).
- Use the same chunk source for both query generation and evaluation.

## Evaluation Harness Learnings
- **Embedding run counts (from report headers, update as runs accrue)**:
  - Total reports: `101`
  - `bge-m3`: `83`
  - `qwen3-embedding-0.6b`: `6`
  - `nomic-embed-text-v2`: `6`
  - `gte-multilingual-base`: `3`
  - `embedding-gemma-300m`: `3`
  - Refresh: scan `RulesIngestion/Rules/**/outputs/runs/**/reports/**/*.md` and count the report header model names.

- **Strict vs Expanded Gold**: Expanded gold uses graph adjacency + section siblings to add acceptable answers.
- **Expanded Gold Validation**: Reports now include deltas and expansion stats (queries with additions, avg/max added).
- **Graph Namespacing**: Graph nodes are prefixed with `doc_id::` for merged multi-chapter evaluation.
- **Merged Evaluation**: You can evaluate a whole source directory by pointing at `--queries-dir` (combines all chapters).
- **Report Organization**: Reports are written to `reports/<model-id>/` and are timestamped; strict vs expanded are separate files.
- **Embedding Reuse**: `--reuse-embeddings` reuses stored vectors for the same `run_id + model_id` when available.
- **Baseline Delta Reporting**: Use `--baseline-report <report.json>` to add a delta section to evaluation reports.
- **Best-Practice Eval Shortcut**: Use `--best-practice-eval` to enable expanded gold + `--both`.
- **Current Best bge-m3 Baseline (Strict, no boost)**:
  - Intro slice (docs `014-029`, `058-073`, `098-113`): MRR `0.8460`, hit@1 `0.7951`, hit@3 `0.8716`, hit@5 `0.9012`, hit@10 `0.9531`.
- **Non-Oracle Graph Boost (Top-Seeded)**:
  - Best-performing defaults across Conditions/Class, Spells, and Intro slices:
    - `--graph-boost-source top`
    - `--graph-boost-seed-top-n 3`
    - `--graph-boost-depth 2`
    - `--graph-boost-top-k 50`
    - `--graph-boost-decay 0.4`
  - `seed_top_n=3` consistently outperformed or tied `seed_top_n=5` on MRR with less complexity.
  - `top_k=50` was consistently stronger than `top_k=20` on MRR for non-oracle boosting.
  - **Shortcut:** use `--best-practice-boost` to apply the defaults above.

- **LLM Chapter Summary Routing (Full-Query Sweep, 2026-01-24)**:
  - Run: `2026-01-23-full-source`, model `nomic-embed-text-v2`, embeddings reused.
  - Summary source: LLM map-reduce summaries (`chapter_summary_embeddings_llm.json`).
  - Results (Expanded Gold):
    - `top_n=3`: Coverage `0.3891`, MRR `0.8522`, hit@1 `0.8004`
      - Report: `.../reports/chapters-nomic/nomic-embed-text-v2/evaluation_expanded_queries_20260123-222656.md`
    - `top_n=5`: Coverage `0.4795`, MRR `0.8301`, hit@1 `0.7785`
      - Report: `.../reports/chapters-nomic/nomic-embed-text-v2/evaluation_expanded_queries_20260123-222916.md`
    - `top_n=8`: Coverage `0.5937`, MRR `0.8112`, hit@1 `0.7548`
      - Report: `.../reports/chapters-nomic/nomic-embed-text-v2/evaluation_expanded_queries_20260123-223148.md`
    - `top_n=12`: Coverage `0.7044`, MRR `0.7931`, hit@1 `0.7339`
      - Report: `.../reports/chapters-nomic/nomic-embed-text-v2/evaluation_expanded_queries_20260123-223434.md`
  - Tradeoff: higher `top_n` raises coverage but lowers MRR; expanded-gold deltas are small but positive (~0.004–0.007).

## Deterministic Edge Discovery + Traversal (New Learnings)
These were validated in recent runs with GMCore/PlayerCore outputs.

### Pipeline Refactor Learnings (2026-01-25)
- **Split enrichment + benchmark into modules** so orchestration is isolated from heavy logic.
- **Standard entrypoint**: use `ingest.py` for full runs (auto-config now tolerates config failures).
- **Traversal is core**: `--profile full` always runs edge-restricted evaluation for DEP/TCG.

### LLM Config Generation Guardrails
- Placeholder detection should **only scan values**, not keys (avoids false hits like `entity_aliases`).
- `Prompt with {label}` is considered a placeholder; when seen, validation fails and the run should continue if `--auto-config` is enabled.
- `ingest.py` now passes `--allow-config-failure` automatically when `--auto-config` is used.

### OCR/Spelling Gate (Pre-Edge Emission)
- Run OCR/spelling gates **before** edge emission to catch bad extractions.
- Metrics tracked per doc:
  - Unresolved strict reference rate (must be below threshold).
  - Suspect token rate (non-alpha noise).
  - Near-duplicate heading rate (edit distance ≤ 1).
- Gate failures should block edge emission **unless explicitly overridden**.

### Ambiguity Handling (Strict Emission Only)
- **Ambiguous targets (multi-resolved)** are never emitted as traversal edges.
- Only `resolution_count == 1` edges are merged into the graph.

### Deterministic Edges vs Hints (Do Not Conflate)
- **Traversal edges must be monotonic**: following them can add irrelevant info but must never add wrong info.
- **Hints are non-emitting**: `mentions_section` is a signal bucket, not a traversal edge.
- **Chapter references are boundary edges**: use them to restrict search scope, not as jump targets.

### Anchor Normalization (Required Before Edge Emission)
Resolution failures were caused by **aliasing**, not fuzziness. Authors reference human-friendly names.
Deterministic anchors must be generated per target:
- Exact heading/table/figure text
- De-numbered heading variants
- Simple canonical phrasings (e.g., "the <heading> section")

Resolution should be:
`cue -> anchor index -> chunk` (not `cue -> heading index`)

### Edge Classes to Emit (Strict)
- `references_chapter` (boundary only)
- `references_table` (traversal)
- `references_figure` (traversal)
- `references_named_section` (traversal, only with explicit numbering or exact heading match)
- `mentions_section` (hint only, never traversal)

### Edge Metrics to Track
- **DEP (Deterministic Edge Precision)** = unique / (unique + multi)
- **TCG (Traversal Coverage Gain)** = recall_with_edges - recall_without_edges
- **Reachability Monotonicity**: track chapter recall (pool + final), not rank MRR

### Graph Evaluation Metrics (Edge-Restricted)
These metrics are produced by `scripts/edge_restricted_retrieval_eval.py` and are tracked
per run (see `*.edge_eval.json`).
- **queries_total**: number of evaluation queries considered.
- **queries_with_edges**: queries whose seed chunk has at least one traversable edge.
- **edge_restricted_recall**: recall when retrieval is limited to traversable edges.
- **baseline_recall**: recall when edges exist but no traversal constraint is applied.
- **edge_restricted_tcg**: `edge_restricted_recall - baseline_recall` (gain from traversal).
- **avg_candidate_fraction**: average allowed chunk fraction per doc
  (`allowed_chunks / total_chunks_in_doc`); lower means tighter scope.
- **traversal_class_counts**: counts of edges by traversal policy class
  (`traversal`, `boundary`, `hint`).
- **dep_by_relation**: per-relation counts of `unique/multi/zero` resolutions and DEP.
- **soft_signal_usefulness**: sanity check for hint edges (e.g., `mentions_section`)
  showing how often hints align with section paths.

### Key Interpretation Notes
- Low `references_section` resolution is expected and correct; most section mentions are not deterministic.
- Routing can trade precision for recall; use hybrid rerank to recover precision, but accept remaining summary lossiness.

## Baselines Across Time (Full-Source / Merged)
Use these as the canonical full-source references for deltas.

- **2026-01-25 (GalaxyGuide, merged-full, dual-scope eval)**  
  - Run: `2026-01-25_13-30-10`  
  - Eval: `merged-full.dualscope.edge_eval.json`  
  - queries_total `268`, queries_with_edges `32`  
  - edge_restricted_recall `1.0`, baseline_recall `1.0`, TCG `0.0`  
  - avg_candidate_fraction `0.0112`  
  - Expanded MRR `0.7145` (same run, expanded-gold report below)  
  - dep_by_relation: mentions_term DEP `1.0`, defines_term DEP `1.0`,
    references_page DEP `0.0`  

- **2026-01-25 (GalaxyGuide, merged, expanded gold, rerun after pruning)**  
  - Run: `2026-01-25_18-37-56`  
  - Model: `nomic-embed-text-v2`  
  - Scope: merged evaluation  
  - Expanded MRR `0.8933`, hit@1 `0.8529`, hit@3 `0.9198`, hit@5 `0.9465`, hit@10 `0.9747`  
  - Report: `RulesIngestion/Rules/StarFinder2e/GalaxyGuide/outputs/runs/2026-01-25_18-37-56/enriched/reports/full-merged-nomic/nomic-embed-text-v2/evaluation_expanded_queries_20260125-185610.md`

- **2026-01-25 (GalaxyGuide, full pipeline, expanded gold)**  
  - Run: `2026-01-25_13-30-10`  
  - Model: `nomic-embed-text-v2`  
  - Scope: merged full-source evaluation  
  - Expanded MRR `0.7145`, hit@1 `0.4664`, hit@3 `0.9515`, hit@5 `0.9776`, hit@10 `0.9963`  
  - Report: `RulesIngestion/Rules/StarFinder2e/GalaxyGuide/outputs/runs/2026-01-25_13-30-10/reports/chapters-llm/nomic-embed-text-v2/evaluation_expanded_queries_20260125-135902.md`

- **2026-01-22 (Baseline, merged, expanded gold)**  
  - Run: `2026-01-22_21-59-56`  
  - Model: `bge-m3`  
  - Chunk source: `enriched`  
  - Scope: merged full-source evaluation  
  - Strict MRR `0.7065`, Expanded MRR `0.7083`  
  - Report: `RulesIngestion/Rules/StarFinder2e/PlayerCore/outputs/runs/2026-01-22_21-59-56/enriched/reports/bge-m3/evaluation_expanded_queries_20260123-085901.json`

- **2026-01-22 (Baseline, full-source, expanded gold)**  
  - Run: `2026-01-22_21-59-56`  
  - Model: `qwen3-embedding-0.6b`  
  - Chunk source: `enriched`  
  - Scope: full-source evaluation (queries_dir on run enriched)  
  - Strict MRR `0.6741`, Expanded MRR `0.6749`  
  - Report: `RulesIngestion/Rules/StarFinder2e/PlayerCore/outputs/runs/2026-01-22_21-59-56/reports/qwen3-embedding-0.6b/evaluation_expanded_queries_20260123-000915.json`

- **2026-01-22 (Baseline, full-source, expanded gold)**  
  - Run: `2026-01-22_21-59-56`  
  - Model: `nomic-embed-text-v2`  
  - Chunk source: `enriched`  
  - Scope: full-source evaluation (queries_dir on run enriched)  
  - Strict MRR `0.7067`, Expanded MRR `0.7078`  
  - Report: `RulesIngestion/Rules/StarFinder2e/PlayerCore/outputs/runs/2026-01-22_21-59-56/reports/nomic-embed-text-v2/evaluation_expanded_queries_20260123-002313.json`

- **2026-01-22 (Baseline, merged, expanded gold)**  
  - Run: `2026-01-22_21-59-56`  
  - Model: `embedding-gemma-300m`  
  - Chunk source: `enriched`  
  - Scope: merged full-source evaluation  
  - Strict MRR `0.5084`, Expanded MRR `0.5100`  
  - Report: `RulesIngestion/Rules/StarFinder2e/PlayerCore/outputs/runs/2026-01-22_21-59-56/enriched/reports/embedding-gemma-300m/evaluation_expanded_queries_20260123-103723.json`

- **2026-01-23 (Current, merged, best-practice boost)**  
  - Run: `2026-01-23-full-source`  
  - Model: `nomic-embed-text-v2` (uses `nomic-ai/nomic-embed-text-v2-moe`)  
  - Chunk source: `enriched`  
  - Scope: merged full-source evaluation  
  - Strict MRR `0.7099`  
  - Report: `RulesIngestion/Rules/StarFinder2e/PlayerCore/outputs/runs/2026-01-23-full-source/enriched/reports/full-merged-nomic/nomic-embed-text-v2/evaluation_strict_queries_20260123-194023.json`

- **2026-01-23 (Current, merged, best-practice boost + expanded gold)**  
  - Run: `2026-01-23-full-source`  
  - Model: `nomic-embed-text-v2` (uses `nomic-ai/nomic-embed-text-v2-moe`)  
  - Chunk source: `enriched`  
  - Scope: merged full-source evaluation  
  - Expanded MRR `0.7099`, hit@1 `0.6481`, hit@3 `0.7427`, hit@5 `0.7787`, hit@10 `0.8270`  
  - Estimated total time: `1,011,245 ms` (~16.85 min)  
  - Report: `RulesIngestion/Rules/StarFinder2e/PlayerCore/outputs/runs/2026-01-23-full-source/enriched/reports/full-merged-nomic/nomic-embed-text-v2/evaluation_expanded_queries_20260123-195715.md`

## Preferred Embedding Model (Current)
- **`nomic-embed-text-v2`** is the default going forward.
- Rationale: MRR comparable to `bge-m3` while running faster in practice.

## Future Lever: Embedding Fine-Tuning
- Add fine-tuning of `nomic-embed-text-v2` as a lever for full-book retrieval quality.
- We already generate evaluation queries, which can seed training pairs.
- Use the repo’s explicit fine-tuning instructions when ready.

## Best-Practice Eval Shortcut (Current)
```
uv run python -m ruleslawyer.evaluation_harness \
  --queries-dir "<run>/enriched" \
  --model-id nomic-embed-text-v2 \
  --document-prefix "<doc-prefix-1>" \
  --document-prefix "<doc-prefix-2>" \
  --query-limit 200 --query-seed 42 \
  --best-practice-eval \
  --best-practice-boost \
  --report-dir "<run>/enriched/reports/sample-boost-topn-3-nomic"
```

## Latest Spells Slice Result (Graph v2)
- Slice: `PZO22001 Starfinder Player Core 294-329` + `330-363`
- Run: `2026-01-23-alias-v2`
- Config: `--graph-boost-source top --graph-boost-seed-top-n 3 --graph-boost-depth 2 --graph-boost-top-k 50 --graph-boost-decay 0.4`
- MRR: `0.8576` (strict; expanded == strict)

## Instruction Set: Ingest + Evaluate a Source Directory
This instruction set exercises full ingestion + merged evaluation across all PDFs in a source directory.

1. Ensure env vars are set:
   - `MONGODB_URI` (optional; defaults to localhost)
   - `OPENAI_API_KEY` (required for `--auto-config` and LLM passes)
   - `EMBEDDING_MODEL_PATH` (optional, for local model cache)

2. Run the prebuilt script:
```
cd /media/drakosfire/Projects/DungeonOverMind/RulesIngestion
./run_ingest_and_evaluate_source.sh
```

3. The script will:
   - Run the pipeline on every PDF in the source directory
   - Store run snapshots in MongoDB
   - Run strict + expanded evaluation across `qwen`, `nomic`, and `gte` on merged enriched chunks

4. If you want to re-run the benchmark with another model:
```
cd /media/drakosfire/Projects/DungeonOverMind/DungeonMindServer
uv run python -m ruleslawyer.evaluation_harness \
  --queries-dir "path/to/run/enriched" \
  --model-id gte-multilingual-base \
  --chunk-source enriched \
  --both
```
