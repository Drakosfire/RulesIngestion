# HANDOFF — RLH-01 Jev decision adapter

**Status:** ACTIVE — operator requested execution of the Phase H PR stack on 2026-09-25
**Repository:** `Drakosfire/RulesIngestion`
**Authority:** `Drakosfire/DungeonOverMind/Docs/Plans/PLAN-rules-lawyer-graph-experiment.md`
**Primary question:** Can RulesIngestion make one live Jev typed judgment through a provider-isolated adapter and persist a safe, replayable decision receipt?
**Unlocks:** RLH-02

## Re-anchor before coding

Activation anchor: `RulesIngestion main@f201d93ad854073565e6c0f88245d8c460cb78e2` after prerequisite policy repair PR #7; central stack authority merged as DungeonOverMind PR #8 at `1a09159452935191583b7a147c695df724951f46`.

Before implementation, refresh `main`, open PRs, current Jev SDK/API docs, and the canonical RulesIngestion design index. If another active PR owns the same provider/config files, stop and reconcile.

## Build exactly this

Add a small provider adapter for TypeSafe Jev through Vercel AI Gateway's TypeSafe-compatible endpoint. It is infrastructure for later semantic experiments; it is **not** Stage C semantics yet.

Required behavior:

- read the project credential from `TYPESAFE_JEV_API_KEY` (the existing value is a Vercel AI Gateway key);
- pass it explicitly to the official Python TypeSafe client rather than renaming/mutating process environment;
- set the TypeSafe-compatible Gateway base URL explicitly;
- keep the provider key server/script-side only and out of logs/receipts;
- support the typed Jev primitives needed by the experiment: Choice, Score, and Noul;
- expose explicit outcomes for missing key, authentication failure, rate limit, timeout, provider failure, and invalid response;
- emit a decision receipt containing stable input/question digests, requested and resolved model identity, typed answer payload, usage metadata when returned, and adapter/schema version;
- make any nondeterministic telemetry such as elapsed time separate from the stable decision digest;
- allow a mocked deterministic unit-test client and one opt-in live smoke command.

Use the official `typesafe-sdk` package. The upstream SDK normally reads `TYPESAFE_API_KEY`; this project intentionally keeps the operator-provided name `TYPESAFE_JEV_API_KEY` and supplies the Gateway key explicitly. Route through `https://ai-gateway.vercel.sh/typesafe` as documented by Vercel. The direct TypeSafe endpoint rejects this Gateway credential.

For Gateway connectivity, request `typesafe-ai/jev`. Any later benchmark run must record the model and routing identity returned by the service; do not infer a pinned model version from the alias.

## Suggested lease

Prefer a new bounded package rather than provider logic spread through retrieval code:

```text
semantic_lifting/
  __init__.py
  contracts.py
  jev.py
scripts/run_jev_smoke.py
tests/semantic_lifting/test_jev_adapter.py
pyproject.toml
uv.lock
```

Equivalent names are acceptable if current repository structure gives a clearly better home. Do not edit retrieval ranking behavior.

## Do not

- do semantic extraction;
- define rule predicates;
- call DungeonMind;
- add automatic fallback to an LLM;
- wrap the SDK in a second uncontrolled retry loop;
- persist secrets or raw Authorization headers;
- make live provider access required for ordinary unit tests.

## Acceptance evidence

Required before this PR can pass:

1. unit tests prove typed request/response normalization and every named failure class;
2. a redacted live smoke receipt proves the configured account can reach Jev;
3. the receipt contains no API key;
4. two identical mocked decisions produce the same stable digest;
5. `uv run pytest tests/ -v` remains green.

Acceptance token:

```text
RLH_01_JEV_DECISION_ADAPTER_ACCEPTED
```

## Stop conditions

Stop instead of widening the PR if the current TypeSafe SDK cannot represent the required typed questions, if provider configuration requires browser exposure, or if the experiment needs semantic policy to decide what the adapter means. Those are successor concerns.
