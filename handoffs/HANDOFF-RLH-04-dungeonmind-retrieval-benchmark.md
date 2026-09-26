# HANDOFF — RLH-04 DungeonMind retrieval benchmark

**Status:** DEFERRED DRAFT  
**Repository:** `Drakosfire/RulesIngestion`  
**Authority:** `Drakosfire/DungeonOverMind/Docs/Plans/PLAN-rules-lawyer-graph-experiment.md`  
**Predecessor:** `RLH_03_DUNGEONMIND_PUBLICATION_PROOF_ACCEPTED`  
**Primary question:** Can DungeonMind retrieve the exact admitted evidence needed for the bounded rules questions well enough to support a useful cited Rules Lawyer path, and how does that compare with the existing RulesIngestion retrieval baseline?  
**Unlocks:** RLH-05 and RLH-06 may proceed independently after acceptance.

## Scope

Do not add graph reasoning yet.

Use the exact RLH-03 published occupancy space plus a small bounded query set that includes:

- both occupancy grounding questions;
- narrow paraphrases/negative controls sufficient to expose exact-match-only behavior;
- the same required/supporting EvidenceUnit gold used by the pilot.

Run two comparable retrieval paths:

1. current RulesIngestion baseline;
2. DungeonMind read/search/evidence path over the published rules space.

Measure the same evidence identities after mapping.

## Build

Add a Retrieval-Lab-compatible adapter or experiment runner that turns DungeonMind results into the same scored evidence surface used by existing evaluation code.

Record:

- DungeonMind commit/profile/revision identity;
- query;
- returned entity/assertion/evidence IDs;
- mapped EvidenceUnit IDs;
- rank/order;
- admission/failure reason;
- latency as telemetry, not semantic identity.

No LLM answer synthesis in this PR.

## Suggested lease

```text
semantic_lifting/dungeonmind_retrieval.py
retrieval_lab/                 # smallest adapter seam only
evals/semantic_lifting/occupancy_v0/
scripts/run_dungeonmind_retrieval_compare.py
tests/semantic_lifting/test_dungeonmind_retrieval.py
```

## Product gate

Buddy does not require DungeonMind to beat the mature baseline on MRR to proceed.

It **does** require the bounded product witness to retrieve the exact required occupancy evidence with stable source/evidence identity and truthful no-result behavior.

Report both:

- comparative metrics versus baseline;
- a binary product-readiness verdict for this bounded cited-retrieval use.

## Do not

- tune semantic edges;
- add graph expansion;
- generate an answer;
- change DungeonMind authorization/admission rules;
- hide evidence misses behind generative completion.

## Acceptance evidence

Produce a contract-valid comparison artifact and report.

Minimum acceptance:

- both canonical occupancy grounding questions recover all required evidence inside the agreed top-k;
- returned citations map exactly to source EvidenceUnits;
- repeated run on the frozen revision is deterministic in membership/order;
- missing evidence remains an explicit miss.

Acceptance token:

```text
RLH_04_DUNGEONMIND_RETRIEVAL_BENCHMARK_ACCEPTED
```

If comparative ranking is materially worse than baseline, record that honestly; it does not block the product lane if the bounded exact-evidence gate passes.
