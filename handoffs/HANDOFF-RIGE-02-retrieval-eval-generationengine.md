# HANDOFF — RIGE-02 Retrieval/evaluation through GenerationEngine

**Status:** DEFERRED DRAFT — stacked on RIGE-01  
**Repository:** `Drakosfire/RulesIngestion`  
**Physical base:** `rige/01-semantic-lifting-generationengine`  
**Cross-repo authority:** `Drakosfire/DungeonOverMind/Docs/Plans/STACK-rules-ingestion-generationengine-sidequest.md`  
**Primary question:** Can active Retrieval Lab generative inference move to GenerationEngine without changing retrieval/evaluation meaning or weakening contract-aware run artifacts?  
**Predecessor:** `RIGE_01_SEMANTIC_LIFTING_GENERATIONENGINE_ACCEPTED`  
**Unlocks:** RIGE-03

## Stack position

```text
GEJ-01 → GEJ-02
→ RIGE-01
→ RIGE-02  ← YOU ARE HERE
→ RIGE-03
→ RIGE-04
→ RLH-05
```

## Scope

Migrate the active retrieval/evaluation inference family, not extraction.

At re-anchor, search active non-Archive code again. Expected owners include:

```text
retrieval_lab/query_enhancement/enhancer.py
retrieval_lab/query_enhancement/decomposition.py
retrieval_lab/llm_reranker.py
retrieval_lab/answer_eval/openai_generator.py
retrieval_lab/auto_gold_review/openai_reviewer.py
retrieval_lab/run_experiment.py
associated focused tests/config/docs
```

Provider-specific class/file names may be renamed when they become misleading, but avoid broad cosmetic churn.

## Mapping

Use:

- ordinary rewrite/decomposition text → `GenerationClient.generate_text` or `generate_structured` according to the existing output contract;
- listwise/typed reranker → `generate_structured`;
- answer synthesis → `generate_text` or structured only if the current contract requires structure;
- auto-gold structured reviewer → `generate_structured`.

RulesIngestion owns prompts, schemas, parsing of domain meaning, fallback policy, benchmark semantics, and evaluation.

## Exact targets and experimental controls

Retrieval Lab may continue to choose explicit provider/model targets. Model identifiers in experiment config are consumer configuration, not a copied provider catalog.

Map only controls GenerationEngine currently expresses. If an active experiment needs a provider-specific control GE cannot represent, stop and record the exact call/control. Do not smuggle direct SDK usage through a helper to make this PR green.

## Run-manifest requirements

Every live generative Retrieval Lab run must record:

- exact GenerationEngine revision;
- operation kind;
- provider/model/profile request;
- provider transport;
- requested/resolved/response model;
- usage/provider IDs/failure code when available.

Keep corpus/benchmark contract identity unchanged.

Inference observations supplement run truth; they do not replace corpus/benchmark manifests.

## Baseline preservation

Use representative frozen tests/fixtures for each migrated family.

Required proof is semantic contract parity, not byte-identical provider wire calls:

- same prompt content/schema intent;
- same query/benchmark inputs;
- same accepted parser/schema constraints;
- same failure visibility;
- no hidden extra model calls.

If GE structured conformance can issue one repair call where the old direct path could not, record that as an intentional execution-contract change and ensure attempt counts are visible.

## Suggested lease

```text
retrieval_lab/query_enhancement/**
retrieval_lab/llm_reranker.py
retrieval_lab/answer_eval/**
retrieval_lab/auto_gold_review/**
retrieval_lab/run_experiment.py
retrieval_lab/run_manifest.py
tests/retrieval_lab/**
Docs/Design/RETRIEVAL_LAB.md and workflow docs only where provider ownership is stated
handoffs/HANDOFF-RIGE-02-retrieval-eval-generationengine.md
```

## Do not

- touch Stage A/B extraction/provider paths;
- change retrieval scoring/ranking algorithms while migrating execution;
- change benchmark gold;
- move embeddings into GE;
- turn GE observations into benchmark authority.

## Acceptance proof

1. No direct `OpenAI`/provider client construction remains in active `retrieval_lab/`.
2. Focused tests cover each migrated family and normalized failures.
3. Representative eval runs retain valid corpus/benchmark contracts.
4. Run artifacts identify exact GE execution.
5. Full RulesIngestion suite remains green.

Acceptance token:

```text
RIGE_02_RETRIEVAL_EVAL_GENERATIONENGINE_ACCEPTED
```
