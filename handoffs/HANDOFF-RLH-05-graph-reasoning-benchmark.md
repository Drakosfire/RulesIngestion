# HANDOFF — RLH-05 graph reasoning benchmark

**Status:** ACTIVE — bounded controller implemented; promotion blocked by substrate coverage  
**Repository:** `Drakosfire/RulesIngestion`  
**Authority:** `Drakosfire/DungeonOverMind/Docs/Plans/PLAN-rules-lawyer-graph-experiment.md`  
**Predecessor:** `RLH_04_DUNGEONMIND_RETRIEVAL_BENCHMARK_ACCEPTED`  
**Primary question:** Does bounded graph-assisted closure materially improve required-evidence assembly or answer support over retrieval-only under a fixed budget?  
**Parallel:** RLH-06 → RLH-08 product lane may proceed without waiting for this result.  
**Unlocks:** RLH-09 uses this result to decide whether graph closure belongs in formal-rule preparation.

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
D. C with edges retained only by structured-LLM adjudication;  
E. C with equivalent edges retained by Jev adjudication.

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
