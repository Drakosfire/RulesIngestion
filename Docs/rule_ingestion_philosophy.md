# Rule Ingestion Philosophy

## What This System Is (and Is Not)

This system is **not** Retrieval-Augmented Generation for rules.

It is a **Rule Ingestion and Compilation system**.

RAG is a projection layered on top of the ingestion artifacts, not the mechanism by which rules are understood, validated, or executed.

If a system can answer a question but cannot produce deterministic, replayable rule artifacts, it has failed its primary purpose.

---

## Ingestion Is a Compiler Front-End

Rule ingestion occupies the same architectural role as a compiler front-end:

- It consumes **unstructured source material** (PDFs, DOCX, HTML).
- It produces **structured intermediate representations** suitable for deterministic execution.
- It must preserve **source fidelity**, **scope**, and **intent** without inventing semantics.

Like a compiler front-end, ingestion:

- **May reject input** as ambiguous or malformed.
- **Must surface uncertainty explicitly**.
- **Must never guess to make progress**.

The output of ingestion is not executable logic.
It is a *compilable representation*.

---

## Where LLMs Are Allowed to Exist

LLMs are permitted only where non-determinism is acceptable **and bounded**.

Allowed:

- Structural classification (e.g., identifying candidate rule-bearing text)
- Semantic extraction into typed, inspectable fields
- Explanation, summarization, and citation assembly

Not allowed:

- Runtime rule evaluation
- Conflict resolution
- Ordering or precedence decisions
- Any operation that would affect deterministic replay

LLMs may propose structure.
They may not assert truth.

Every LLM-derived artifact must be:

- Inspectable
- Correctable
- Rejectable

---

## Ambiguity Is a First-Class Output

Ambiguity is not a failure state.

Silent resolution of ambiguity **is**.

When a rule is unclear, conditional, or underspecified, the system must:

- Represent the ambiguity explicitly
- Preserve competing interpretations if necessary
- Block compilation until ambiguity is resolved or scoped

Progress that hides uncertainty poisons downstream systems.

The ingestion pipeline must make uncertainty *visible, local, and actionable*.

---

## Determinism Is the End Constraint

All downstream systems—rules engines, replays, audits, projections—depend on a single invariant:

> Given the same inputs, the same rules must produce the same results.

Anything that compromises this invariant is out of scope for ingestion.

This includes:

- Probabilistic interpretation
- Heuristic conflict resolution
- Context-dependent rule meaning

If a rule cannot be made deterministic, it must not compile.

---

## Why This Document Exists

This document exists to be reread at moments of temptation:

- When a model produces a confident but unjustified answer
- When a demo "looks right" but cannot be replayed
- When speed pressures suggest "just letting the model decide"

This philosophy is the guardrail.

Everything else is implementation.

