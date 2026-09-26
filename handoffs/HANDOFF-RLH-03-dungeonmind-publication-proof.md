# HANDOFF — RLH-03 DungeonMind publication proof

**Status:** ACCEPTED — generic V3 publication and durable reopen proved
**Repository:** `Drakosfire/RulesIngestion`  
**Authority:** `Drakosfire/DungeonOverMind/Docs/Plans/PLAN-rules-lawyer-graph-experiment.md`  
**Predecessor:** `RLH_02_OCCUPANCY_SEMANTIC_PILOT_ACCEPTED`  
**Primary question:** Can the accepted occupancy package be durably represented in an isolated DungeonMind vNext KnowledgeSpace using generic contracts and a data/profile boundary, with exact evidence traceability and no DungeonMind kernel modification?  
**Unlocks:** RLH-04

## Architectural rule

This is a **consumer proof**. There is intentionally no planned DungeonMind code PR.

Use DungeonMind's current generic vNext contracts, governed write path, source/evidence model, Semantic Profile V3/open predicate namespaces, and durable repository implementation as they exist when this PR activates.

If a genuinely generic missing capability is discovered, stop. Record the smallest failing fixture and open a separate `RLH-03K` DungeonMind handoff from evidence. Do not patch around the gap in RulesIngestion and do not add D&D/rules meaning to the DungeonMind kernel.

WorldKeeper is not in this path. This is a batch/lab producer publishing governed knowledge, not Buddy interactive authoring.

## Re-anchor before coding

Pin the exact accepted DungeonMind revision used by the experiment and record it in the run manifest. Re-read DungeonMind's current vNext roadmap, contracts, V5 write path, V3 profile authority, and source/evidence contracts.

Activated after RulesIngestion PR #2 merged at `0ec3e3b59566a2ab06a3288026f8fa73569ce0cc`. The experimental DungeonMind dependency is pinned to `54a419f99057d96e0c4e7620d8bd8ccc6816fb62` (merged V3 authority PR #78).

## Build exactly this

Create an isolated rules KnowledgeSpace and a minimal domain/profile descriptor owned by the experiment.

Translate the RLH-02 accepted candidate package into:

- source artifact/revision identity derived from the corpus contract;
- evidence refs preserving RulesIngestion EvidenceUnit identity or an explicit reversible mapping;
- entities/assertions needed by the occupancy slice;
- only the predicates/value kinds actually exercised by that slice;
- a governed `KnowledgeContribution`;
- exact publication result/receipt.

Use a fresh V3-pinned space from genesis. Do not design profile transition for existing spaces.

Prove publication through DungeonMind's real application/repository boundary. Prefer a disposable PostgreSQL integration witness so the proof includes durable reopen, not only in-memory object construction.

## Suggested lease

```text
semantic_lifting/
  dungeonmind_export.py
  rules_profile.py
  publication.py
scripts/run_dungeonmind_rules_publish.py
tests/semantic_lifting/test_dungeonmind_publication.py
evals/semantic_lifting/occupancy_v0/  # add receipt/result fixtures only
pyproject.toml / uv.lock              # exact experimental DungeonMind pin if needed
```

## Invariants

- source prose remains outside model-generated authority;
- every semantic assertion resolves to exact evidence;
- rejected/unresolved RLH-02 candidates do not publish as accepted knowledge;
- publication uses expected-parent/CAS semantics and records exact revision identity;
- retry/replay semantics are the DungeonMind-owned ones;
- rules semantics live in the experiment profile/domain data, not generic Kernel code.

## Do not

- modify DungeonMind from this PR;
- add World/user/account semantics;
- bulk ingest the PHB;
- add WorldKeeper;
- create a rules-only persistence store;
- invent durable IDs client-side when DungeonMind owns their allocation.

## Acceptance evidence

One integration witness must prove:

```text
accepted occupancy package
→ fresh KnowledgeSpace
→ governed publication
→ exact child revision
→ process/repository reopen
→ same entities/assertions/evidence
→ exact source traceability
```

Also prove an unresolved/rejected semantic candidate remains absent.

Acceptance token:

```text
RLH_03_DUNGEONMIND_PUBLICATION_PROOF_ACCEPTED
```

## Acceptance witness

`evals/semantic_lifting/occupancy_v1/dungeonmind_publication_witness.json` records the exact PostgreSQL publication receipt, source artifact/revision descriptors, reversible EvidenceUnit mapping, V3 space and child revision IDs, and reopened assertions/evidence. Two accepted claims publish; the overbroad Prone consequence and unsupported ally-prone negative control are excluded. The child revision `rev:77293aef29dd5324f6b300da1ac970aa` reopens from a separate process and PostgreSQL repository with identical payload digest, assertions, and evidence. The full RulesIngestion suite passes (348 tests). No DungeonMind kernel change was needed.

## Stop conditions

Any required DungeonMind kernel change is a stop/split. Capture the failing generic fixture; do not broaden this consumer PR.
