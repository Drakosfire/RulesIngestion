# HANDOFF — RLH-02 occupancy semantic pilot

**Status:** DEFERRED DRAFT  
**Repository:** `Drakosfire/RulesIngestion`  
**Authority:** `Drakosfire/DungeonOverMind/Docs/Plans/PLAN-rules-lawyer-graph-experiment.md`  
**Predecessor:** `RLH_01_JEV_DECISION_ADAPTER_ACCEPTED`  
**Primary question:** Can one bounded PHB occupancy slice become an auditable semantic candidate package whose claims remain tied to exact EvidenceUnits and whose adjudication can be compared against human gold?  
**Unlocks:** RLH-03

## Re-anchor before coding

Rebase onto the accepted RLH-01 head. Re-read:

- `Docs/Design/occupancy_vertical_slice_v0.md`;
- canonical Stage A/B and Retrieval Lab design docs;
- current EvidenceUnit schema;
- current answer-eval/structured-output model patterns.

Do not revive archived Stage C contracts as authority.

## Slice

Use the existing 2024 PHB occupancy vertical slice only.

Start from exact Stage B EvidenceUnits. If the full ingested corpus is not checked in, create a minimal fixture containing only the exact EvidenceUnits needed by the two existing occupancy grounding questions plus their provenance metadata.

## Pipeline

```text
EvidenceUnits
→ strong generative semantic proposal
→ typed adjudication treatment
→ SemanticCandidatePackage
→ comparison against human gold
```

The proposal model may generate candidate semantic structure. It does not publish truth.

Define only enough candidate structure to express this slice, for example:

- stable candidate ID;
- candidate kind;
- normalized subject/predicate/value or relationship;
- exact evidence-unit refs;
- proposal model/run identity;
- adjudication decisions;
- final disposition: accept / review / reject / unresolved.

Do **not** freeze a broad rules ontology.

## Treatments

Run the same proposed candidates through:

1. human gold;
2. a conventional structured-output generative adjudicator;
3. Jev typed judgments.

Keep the question contracts semantically equivalent across model treatments where possible.

Candidate judgments should stay narrow: rule/default/exception/definition/example classification, relationship choice, evidence sufficiency, identity equivalence, and accept/review/reject.

## Reproducibility

- require an explicit proposal-model ID for benchmark runs;
- record prompt/schema hashes;
- cache provider outputs by stable input + question/prompt + model identity;
- preserve raw provider receipts separately from normalized semantic results;
- never treat model confidence as source truth.

## Suggested lease

```text
semantic_lifting/
  proposal.py
  adjudication.py
  occupancy.py
  contracts.py          # extend only as needed
evals/semantic_lifting/occupancy_v0/
scripts/run_occupancy_semantic_pilot.py
tests/semantic_lifting/
```

## Do not

- write to DungeonMind;
- ingest a whole rulebook;
- change EvidenceUnit identity;
- cite model-generated text as evidence;
- tune retrieval in this PR;
- make Jev mandatory for the structured-LLM comparator.

## Acceptance evidence

Produce one checked-in experiment summary containing:

- human-gold decisions;
- both model-treatment decisions;
- per-decision correctness against gold;
- unresolved/review rate;
- exact EvidenceUnit coverage;
- provider/model identities and stable run/config digests;
- representative disagreement examples.

Every accepted semantic claim must resolve to at least one exact EvidenceUnit.

Acceptance token:

```text
RLH_02_OCCUPANCY_SEMANTIC_PILOT_ACCEPTED
```

## Stop conditions

Stop if the semantic vocabulary cannot stay small on this slice, if adjudication requires hidden outside-rules knowledge, or if evidence provenance is lost between proposal and decision.
