# HANDOFF — RIGE-04 Direct-provider demolition and boundary guard

**Status:** DEFERRED DRAFT — stacked on RIGE-03  
**Repository:** `Drakosfire/RulesIngestion`  
**Physical base:** `rige/03-ingestion-generationengine`  
**Cross-repo authority:** `Drakosfire/DungeonOverMind/Docs/Plans/STACK-rules-ingestion-generationengine-sidequest.md`  
**Primary question:** Can RulesIngestion finish the migration with one enforceable ownership rule: active generative/decision inference crosses GenerationEngine, while specialized OCR/embeddings remain explicit exceptions?  
**Predecessor:** `RIGE_03_INGESTION_GENERATIONENGINE_ACCEPTED`  
**Unlocks:** RLH-05 must rebase onto this accepted merge before review resumes

## Stack position

```text
GEJ-01 → GEJ-02
→ RIGE-01 → RIGE-02 → RIGE-03
→ RIGE-04  ← YOU ARE HERE
→ RLH-05 rebase/resume
→ RLH-09
```

## Boundary to enforce

After this PR, active RulesIngestion code must not own live generative/decision provider SDK execution.

Forbidden outside explicitly historical/archive code:

```text
from openai import OpenAI / AsyncOpenAI
OpenAI(...)
AsyncOpenAI(...)
from typesafe_sdk ...
TypeSafeClient(...)
direct OpenAI/TypeSafe HTTP endpoint calls
provider-specific retry/auth/error mapping
```

Allowed explicit exceptions:

- embedding models and sentence-transformers used by Retrieval Lab;
- DeepSeek OCR2 / OCR-specialized extraction runtime;
- other non-generative specialized ML only if current architecture already owns it and this PR documents it.

Do not opportunistically move embeddings/OCR into GenerationEngine.

## Dependency cleanup

- remove direct `typesafe-sdk` project dependency;
- remove direct OpenAI dependency only if no active non-provider reason remains; otherwise document why it is still required;
- depend on the exact accepted GenerationEngine revision with required extras;
- update lockfile.

Transitive SDK installation through GenerationEngine extras is acceptable. RulesIngestion code must not import/use those SDKs directly.

## Model/config ownership

RulesIngestion may keep experiment model IDs and task→target choices.

It must not keep copied provider capability/pricing catalogs or provider-error logic.

Review `MODEL_POLICY.json`, which currently carries old Buddy-transition wording. Either:

- replace it with a RulesIngestion-owned experiment/task mapping that correctly describes GE ownership; or
- delete it if no active consumer requires it.

Do not leave stale architecture commentary.

## Documentation

Update current RulesIngestion docs/workflows so they say:

```text
RulesIngestion owns
  evidence substrate
  prompts/schemas
  experiments/evaluation
  semantic interpretation
  run artifacts

GenerationEngine owns
  generative + typed-decision provider execution
  credentials/endpoints
  provider/model observations
  retry/timeout/failure normalization
```

Credential docs may still tell operators to set `OPENAI_API_KEY` and `TYPESAFE_JEV_API_KEY`; clarify that GenerationEngine consumes them.

## Regression guard

Add a focused architecture test/script that scans **active** code and fails if direct OpenAI/TypeSafe client ownership returns.

The guard must deliberately exclude:

- `Archive/`;
- generated/fixture text that merely contains provider names;
- approved OCR/embedding code.

Prefer semantic import/path checks over a fragile unrestricted grep.

## RLH re-entry proof

Before accepting this PR, compare current RLH-05 head against the new migration base and record:

- files that conflict;
- experiment artifacts that must be regenerated under GE;
- any handoff assumptions invalidated.

Do not silently merge RLH-05 on top.

Acceptance should leave a concrete rebase instruction for RLH-05.

## Acceptance token

```text
RIGE_04_DIRECT_PROVIDER_DEMOLITION_ACCEPTED
```

## Stop conditions

Stop if demolition reveals an active provider-specific control GenerationEngine still cannot express. That is evidence for a small GE capability successor, not permission to leave an undocumented direct path.
