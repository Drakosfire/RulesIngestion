# HANDOFF — RLH-02 occupancy semantic pilot

**Status:** ACTIVE — operator approved correction to the sourced 2024 rule
**Repository:** `Drakosfire/RulesIngestion`
**Authority:** `Drakosfire/DungeonOverMind/Docs/Plans/PLAN-rules-lawyer-graph-experiment.md`
**Predecessor:** `RLH_01_JEV_DECISION_ADAPTER_ACCEPTED`
**Primary question:** Can one bounded source-grounded 2024 occupancy slice become an auditable semantic candidate package whose claims remain tied to exact EvidenceUnits and whose adjudication can be compared against human gold?
**Unlocks:** RLH-03

## Re-anchor before coding

Rebased onto `RulesIngestion main@175f03e6a9adf95d423dbff24ff46eef4c17015f` after RLH-01 merged. Central source-rule correction merged in DungeonOverMind PR #9 at `823c6aa5c0a87090d8d83562691a6a98924bbe7b`.

Re-read:

- `Docs/Design/occupancy_vertical_slice_v1.md` (which supersedes the incorrect v0 ally-prone branch);
- canonical Stage A/B and Retrieval Lab design docs;
- current EvidenceUnit schema;
- current answer-eval/structured-output model patterns.

Do not revive archived Stage C contracts as authority.

### Activation correction

The v0 design expects an ally-prone allowance for willingly ending movement in an occupied space. The official [2024 Basic Rules, Moving around Other Creatures](https://www.dndbeyond.com/sources/dnd/br-2024/playing-the-game) and [SRD 5.2.1, page 14](https://media.dndbeyond.com/compendium-images/srd/5.2/SRD_CC_v5.2.1.pdf) instead prohibit willingly ending a move in another creature's space. They describe Prone as a consequence if a turn somehow ends in a shared space, not as an allowance for a prone ally. The operator chose to revise to the sourced rule. No PHB Stage B EvidenceUnits or the referenced occupancy retrieval benchmark are checked in here or available in the local owner checkout.

The RLH-02 fixture therefore uses the official CC-licensed SRD 5.2.1 page as its source and runs its exact paragraph through Stage B. It must never be labeled a PHB ingestion result. The semantic pilot compares default prohibition, separate shared-space Prone consequence, and rejection of the unsupported ally-prone exception. Later PHB-specific publication still requires PHB EvidenceUnits.

## Slice

Use the corrected 2024 occupancy vertical slice only (`Docs/Design/occupancy_vertical_slice_v1.md`).

Start from exact Stage B EvidenceUnits. The full PHB corpus is not checked in, so use the minimal SRD 5.2.1 fixture containing the exact EvidenceUnit needed by both corrected occupancy grounding questions plus its provenance metadata.

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
evals/semantic_lifting/occupancy_v1/
scripts/run_occupancy_semantic_pilot.py
scripts/build_occupancy_source_fixture.py
tests/semantic_lifting/
Docs/Design/occupancy_vertical_slice_v0.md       # supersession notice only
Docs/Design/occupancy_vertical_slice_v1.md
Docs/Design/README.md                             # design index update
Docs/Design/decision_lock_in_and_next_spec.md    # historical correction note only
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
