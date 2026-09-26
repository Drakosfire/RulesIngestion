# HANDOFF — RLH-09 reviewed rule artifact

**Status:** HOLD — implementation candidate exists, but review is blocked on the GenerationEngine migration and reconciled RLH-05  
**Repository:** `Drakosfire/RulesIngestion`  
**Authority:** `Drakosfire/DungeonOverMind/Docs/Plans/PLAN-rules-lawyer-graph-experiment.md`  
**Predecessors:** `RIGE_04_DIRECT_PROVIDER_DEMOLITION_ACCEPTED`; then a rebased/reviewed `RLH_05_GRAPH_REASONING_BENCHMARK_ACCEPTED` or explicit accepted no-promotion disposition; accepted RLH-02/03 occupancy semantics  
**Primary question:** Can the occupancy evidence/semantic package become one small reviewed formal rule artifact suitable for a deterministic consumer while preserving exact source traceability?  
**Unlocks:** RLH-10

## Mandatory stack/rebase gate

Cross-repo authority: `Drakosfire/DungeonOverMind/Docs/Plans/STACK-rules-ingestion-generationengine-sidequest.md`.

This branch is physically descended from the pre-migration RLH-05 branch. Its current head is not eligible for acceptance review.

Required sequence:

1. GEJ-01/02 accepted.
2. RIGE-01→04 accepted.
3. RLH-05 rebased/reconciled onto RIGE-04.
4. RLH-05 reviewed and settled with a decision-complete graph disposition.
5. Rebase/reconstruct RLH-09 onto that settled RLH-05 state.
6. Re-run formal-artifact tests and regenerate any compiler/run identity that depends on upstream experiment artifacts.
7. Refresh this handoff with exact base/head before review.

Do not preserve graph input merely because the old branch contains it. If the reconciled RLH-05 disposition remains no-promotion, RLH-09 must continue to compile from accepted semantic/evidence inputs without graph closure.

### Stack position

```text
GEJ-01 → GEJ-02
          ↓
RIGE-01 → RIGE-02 → RIGE-03 → RIGE-04
                                      ↓
                                   RLH-05
                                      ↓
                                   RLH-09  ← YOU ARE HERE
                                      ↓
                                   RLH-10 → RLH-11
```

## Important distinction

The graph does not become executable.

The output is a candidate formal artifact that becomes eligible for downstream consumption only after an explicit review/approval step recorded in the artifact/receipt.

If RLH-05 found no graph advantage, build from the accepted semantic/evidence package without graph closure. Do not force graph use.

## Target behavior

Only the existing occupancy vertical slice:

```text
Medium ordinary creature
attempts end_move_in_cell
occupied by Medium ordinary creature
→ reject by default
→ reject regardless of ally or Prone state; no sourced movement exception
```

Do not generalize to the entire movement system.

The historical ally-prone exception is superseded by the user's sourced-rule correction and the checked-in SRD 5.2.1 human gold. The source's Tiny/larger-than-other-creature clause concerns becoming Prone after somehow ending a turn in shared space; it does not permit willingly ending a move there. This artifact evaluates only the latter restriction. RLH-05 found no promotable graph value on the available fixture, so no graph closure enters the compiler.

## Artifact contract

Define deterministic versioned JSON containing at least:

- schema/version;
- rule ID/version;
- ruleset ID/version;
- reviewed semantic statement;
- typed required inputs;
- typed condition/decision representation;
- explicit empty exception set for this restriction;
- exact EvidenceUnit refs and DungeonMind knowledge refs where available;
- compiler/run identity;
- review disposition/approval metadata;
- canonical digest.

The executable representation must not require parsing natural-language prose.

## Compiler boundary

```text
accepted semantic package
+ optional bounded graph closure
+ explicit review decision
→ FormalRuleArtifact
```

Generative/Jev outputs may propose fields but cannot mark the artifact reviewed.

## Suggested lease

```text
semantic_lifting/formal_rule.py
semantic_lifting/review.py
schemas/formal_rule_artifact_v0.json
evals/semantic_lifting/occupancy_v0/
scripts/build_occupancy_rule_artifact.py
tests/semantic_lifting/test_formal_rule.py
```

If the repository has a more canonical schema home at activation, use it and amend this list.

## Determinism

Same accepted semantics + same review decision + same contract version must produce stable canonical artifact bytes/digest.

## Do not

- implement RulesEngine runtime;
- infer missing facts;
- encode free-form Python/Rust code in the artifact;
- make Jev confidence an approval;
- expand occupancy scope.

## Acceptance witness

Include one approved artifact, one rejected/unreviewed candidate, and exact evidence traceability for every executable condition.

Acceptance token:

```text
RLH_09_REVIEWED_RULE_ARTIFACT_ACCEPTED
```
