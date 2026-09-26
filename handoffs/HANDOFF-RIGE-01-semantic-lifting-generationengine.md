# HANDOFF — RIGE-01 Semantic lifting through GenerationEngine

**Status:** ACTIVE — implementation lease, pending acceptance
**Repository:** `Drakosfire/RulesIngestion`
**Creation anchor:** `main@b4a06e8b28ac34d40add64978a11116c6a24cf9c` (RLH-04 merged)
**Cross-repo authority:** `Drakosfire/DungeonOverMind/Docs/Plans/STACK-rules-ingestion-generationengine-sidequest.md`
**Primary question:** Can the current Phase-H semantic proposal and both adjudication treatments move from direct provider clients to GenerationEngine without moving experiment meaning into GenerationEngine or corrupting replay identity?
**Cross-repo predecessor:** `GEJ_02_TYPESAFE_JEV_PROVIDER_ACCEPTED`
**Unlocks:** RIGE-02

## Stack position

```text
GEJ-01 generic decision
→ GEJ-02 TypeSafe/Jev provider
→ RIGE-01  ← YOU ARE HERE
→ RIGE-02 retrieval/eval migration
→ RIGE-03 ingestion-time migration
→ RIGE-04 direct-provider demolition
→ RLH-05 rebase + resumed review
→ RLH-09 → RulesEngine bridge
```

The independent Buddy product lane RLH-06→08 may continue in parallel after RLH-04.

## Re-anchor before coding

At activation:

1. pin the exact accepted GenerationEngine GEJ-02 merge;
2. rebase onto current RulesIngestion `main`;
3. re-census RLH-05/RLH-09 and any provider-related PRs;
4. read the current occupancy semantic fixture and accepted RLH-01→04 artifacts;
5. do not modify historical direct-provider receipts in place.

Activation re-anchor (2026-09-26): RulesIngestion `main` remains `b4a06e8b28ac34d40add64978a11116c6a24cf9c`, the RLH-04 accepted anchor; this PR head contains only this handoff at `99897bda1e067a336888acbfd7d0cb6b906c6107`. GEJ-02 is accepted for review at unmerged PR #16 head `cf5bee24fa0a469a80c91c5e48992726eab8aa8d`, which includes the provider-neutral Choice-description amendment to GEJ-01. User instruction keeps these PRs unmerged; this branch will pin that exact GEJ-02 commit. RulesIngestion PRs #9-11 remain stacked handoff shells and RLH-05/#5 and RLH-09/#6 remain on hold. There is no active implementation-path collision. The checked-in occupancy source/evidence identity, human gold, candidate package, and direct-provider receipts remain immutable. This lease includes new GE-v2 receipts/report and focused tests under the named evaluation path; no historical receipt is rewritten.

The old opt-in `scripts/run_jev_smoke.py` imports the direct adapter, so this lease also migrates that smoke to `GenerationClient.decide()` and removes its direct SDK tests. The remaining direct OpenAI consumers require `openai` 2.x while this slice pins GEJ-02; constrain the package to `<3` until RIGE-02/03 retire those paths. These are necessary boundary/compatibility adjustments, not additional experiment treatments.

## Ownership boundary

RulesIngestion continues to own:

- semantic proposal prompts;
- Pydantic/domain schemas;
- Jev question meaning and treatment labels;
- evidence/candidate assembly;
- human gold;
- experiment comparison logic;
- run/request digests and receipt persistence;
- decisions about confidence thresholds and dispositions.

GenerationEngine owns:

- OpenAI/TypeSafe SDKs and endpoints;
- credentials;
- provider/model/transport execution;
- retries/deadlines;
- normalized provider failures;
- usage/model/transport observations.

No RulesIngestion semantic vocabulary moves into GenerationEngine.

## Migrate this slice

Replace direct provider execution in the Phase-H semantic path:

```text
semantic_lifting/jev.py
semantic_lifting/adjudication.py
semantic_lifting/proposal.py
scripts/run_occupancy_semantic_pilot.py
tests/semantic_lifting/*
```

Exact changes should result in:

```text
proposal
  → GenerationClient.generate_structured(...)

structured adjudication
  → GenerationClient.generate_structured(...)

Jev adjudication
  → GenerationClient.decide(...)
```

A small RulesIngestion-owned consumer adapter is allowed if it only translates experiment contracts to GE requests/results. It must not recreate provider retry/error/model logic.

## Dependency pin

Add GenerationEngine as an exact git revision/source matching accepted GEJ-02.

RulesIngestion must no longer import `typesafe_sdk` after this slice. Remove the direct TypeSafe dependency from RulesIngestion's dependency list; the GE TypeSafe extra owns it.

Do not remove all direct OpenAI support yet; RIGE-02/RIGE-03 still own remaining migrations.

## Experiment artifact versioning

Transport/provider ownership changes the experiment contract.

Do **not** overwrite or silently reinterpret RLH-01/RLH-02 direct-provider artifacts.

Introduce a new receipt/run schema or explicit execution-contract version that records at least:

- exact GenerationEngine commit/version;
- GE operation kind (`generate_structured` / `decide`);
- requested provider/model/profile fields;
- relevant `InferenceObservation` identity: provider, provider transport, requested/resolved/response model;
- usage and provider IDs where available;
- RulesIngestion prompt/schema/question hashes;
- exact state/evidence/candidate digest.

RulesIngestion owns the stable experiment digest. Hash deterministic configuration/input/result semantics; keep latency and other nondeterministic telemetry outside semantic identity.

## Jev correction carried from RLH-01 review

Do not preserve the old false meaning of `resolved_model`.

Use GE semantics:

- `resolved_model` = GE's selected/explicit target;
- `response_model` = provider-reported model, possibly the same floating alias;
- provider transport records Vercel AI Gateway;
- no concrete upstream Jev version is invented.

The old `semantic_lifting/jev.py` adapter should be deleted once no active code needs it.

## Live/eval witness

Re-run the bounded occupancy pilot through GE, producing **new** provider receipts.

Compare against the accepted human gold and report:

- proposal candidates/evidence refs unchanged or explicitly explain reviewed differences;
- structured adjudication metrics;
- Jev adjudication metrics;
- disagreement set;
- exact GE execution identity.

A change in model output is not automatically a failure. Silent change in evidence contract, treatment meaning, or replay identity is.

## Suggested lease

```text
semantic_lifting/adjudication.py
semantic_lifting/proposal.py
semantic_lifting/jev.py                 # delete/retire
semantic_lifting/contracts.py           # experiment receipt only
scripts/run_occupancy_semantic_pilot.py
tests/semantic_lifting/
evals/semantic_lifting/occupancy_v1/    # new versioned GE receipts/report only
pyproject.toml
uv.lock
handoffs/HANDOFF-RIGE-01-semantic-lifting-generationengine.md
```

## Do not

- migrate unrelated Retrieval Lab calls yet;
- migrate extraction-time LLM calls yet;
- modify DungeonMind publication/retrieval semantics;
- put human-gold/disposition logic in GE;
- keep a fallback direct TypeSafe path;
- relabel old receipts as GE-backed.

## Acceptance token

```text
RIGE_01_SEMANTIC_LIFTING_GENERATIONENGINE_ACCEPTED
```

## Stop conditions

Stop/split if:
- GEJ-02 cannot represent the needed Jev judgments;
- GE structured generation cannot preserve a required semantic contract;
- exact GE execution identity cannot be captured in experiment artifacts;
- migration requires changing human gold or evidence identity.
