# HANDOFF — RLH-05 graph reasoning benchmark

**Status:** HOLD — bounded controller exists, but acceptance/review is blocked on the GenerationEngine migration side quest  
**Repository:** `Drakosfire/RulesIngestion`  
**Authority:** `Drakosfire/DungeonOverMind/Docs/Plans/PLAN-rules-lawyer-graph-experiment.md`  
**Predecessors:** `RLH_04_DUNGEONMIND_RETRIEVAL_BENCHMARK_ACCEPTED` + `RIGE_04_DIRECT_PROVIDER_DEMOLITION_ACCEPTED`  
**Primary question:** Does bounded graph-assisted closure materially improve required-evidence assembly or answer support over retrieval-only under a fixed budget?  
**Parallel:** RLH-06 → RLH-08 product lane may proceed without waiting for this result.  
**Unlocks:** RLH-09 uses this result to decide whether graph closure belongs in formal-rule preparation.

## Mandatory side-quest re-entry gate

Cross-repo authority: `Drakosfire/DungeonOverMind/Docs/Plans/STACK-rules-ingestion-generationengine-sidequest.md`.

This branch was implemented before RulesIngestion inference ownership was moved behind GenerationEngine. Its current head is **not eligible for acceptance review**.

Before RLH-05 review resumes:

1. GEJ-01 and GEJ-02 must be accepted in GenerationEngine.
2. RIGE-01 → RIGE-04 must be accepted in RulesIngestion.
3. Rebase/reconstruct this branch onto the accepted RIGE-04 merge, not the historical direct-provider base.
4. Re-census every changed file against RIGE-04. Preserve the bounded graph controller only where it still applies cleanly.
5. Replace any direct structured-LLM/Jev execution with the accepted GenerationEngine consumer surfaces.
6. Regenerate any model-backed receipts, treatment outputs, manifests, or experiment summaries whose execution identity changed.
7. Preserve historical direct-provider artifacts as historical evidence; do not relabel them as GE-backed.
8. Refresh this handoff with the exact rebased base/head and the new execution-contract evidence before requesting review.

The existing substrate finding — available occupancy evidence is too small to support a valid multihop A–E comparison and therefore currently yields `GRAPH_ASSIST_NO_PROMOTION` — remains useful. It is **not** an acceptance token and does not bypass the migration gate.

After RIGE-04, all generative/decision inference in RLH-05 must cross GenerationEngine. Embedding retrieval remains an explicit RulesIngestion-owned exception.

### Side-quest stack position

```text
GEJ-01 → GEJ-02
          ↓
RIGE-01 → RIGE-02 → RIGE-03 → RIGE-04
                                      ↓
                                  RLH-05  ← YOU ARE HERE
                                      ↓
                                  RLH-09
```

## Experimental slice

Re-anchor finding: the checked-in PHB multihop working set has no available source EvidenceUnits in this checkout. The accepted SRD occupancy publication has two accepted assertions but only one exact EvidenceUnit. Its five grounding queries are already 5/5 for both retrieval treatments at top 1, so graph closure cannot add required evidence or test edge adjudication. This PR implements and tests the bounded closure controller and records a `GRAPH_ASSIST_NO_PROMOTION` decision for this available fixture. It does **not** claim RLH-05 acceptance, a valid multihop A–E comparison, or Jev/structured edge accuracy. A full comparison requires a source-grounded multihop publication and human-gold edges; do not fabricate those inputs from the historical chunk IDs.

Do not semantically lift a whole rulebook.

Select a small subset of the existing bounded multihop working set whose gold neighborhoods are already grounded and whose source EvidenceUnits are available. Prefer queries representing different failure families: base/exception, prerequisite, cross-rule interaction, and progression/relationship.

Publish only the required bounded neighborhoods into an isolated DungeonMind rules space using the accepted RLH-02/RLH-03 pipeline.

## Treatments

Keep the initial query and answer synthesizer fixed as far as practical.

Compare:

A. existing retrieval-only baseline;  
B. DungeonMind evidence retrieval only;  
C. DungeonMind retrieval + bounded structural/semantic neighborhood closure;  
D. C with edges retained only by structured-LLM adjudication executed through GenerationEngine;  
E. C with equivalent edges retained by GenerationEngine's TypeSafe/Jev decision provider.

Maximum graph expansion: two hops. Use explicit candidate/evidence budgets. No open-ended traversal.

## Required trace

Every graph-assisted answer context must record the actual path:

```text
query
→ seed result
→ traversed assertion/relationship
→ added evidence
→ final evidence packet
```

A graph edge is never itself a citation unless its underlying exact EvidenceUnit evidence is also returned.

## Metrics

At minimum:

- required-evidence coverage;
- rank of last required evidence;
- answer supported/completeness using existing answer-eval machinery;
- citation fidelity;
- added-evidence precision;
- graph-edge adjudication accuracy on human-gold edges;
- unresolved/review rate;
- latency/cost telemetry.

## Suggested lease

```text
semantic_lifting/graph_retrieval.py
retrieval_lab/                 # bounded controller/adapter seam only
evals/semantic_lifting/multihop_graph_v0/
scripts/run_graph_reasoning_benchmark.py
tests/semantic_lifting/test_graph_retrieval.py
```

## Decision artifact

End with one explicit disposition:

```text
GRAPH_ASSIST_VALUE_POSITIVE
GRAPH_ASSIST_VALUE_MIXED
GRAPH_ASSIST_NO_PROMOTION
```

Do not massage a negative result into a feature.

## Do not

- change Buddy product behavior;
- create recursive agent search;
- let hidden graph nodes authorize evidence;
- broaden predicate vocabulary to improve benchmark appearance;
- claim Jev calibration without measuring decision accuracy on this set.

Acceptance token:

```text
RLH_05_GRAPH_REASONING_BENCHMARK_ACCEPTED
```

Acceptance means the experiment is valid and decision-complete, not that graph assistance won.
