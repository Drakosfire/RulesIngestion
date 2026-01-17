# Rule Ingestion Pipeline Overview

## Purpose

This document describes the **rule ingestion pipeline** as a staged, tool-agnostic process.

It exists to:

- Make boundaries explicit
- Prevent capability creep
- Provide a shared mental model for experimentation

This is **not** an implementation plan. This is a statement of responsibilities and prohibitions.

---

## Pipeline at a Glance

```
Unstructured Docs
      │
      ▼
[A] Structural Ingestion
      │
      ▼
[B] Rule Unit Extraction
      │
      ▼
[C] Typed Rule Decomposition
      │
      ▼
[D] Rule Graph Construction
      │
      ▼
[E] Compiler Feasibility Gate
      │
      ├──► Deterministic Rules Engine
      │
      └──► Projections (RulesLawyer, Audit, Docs)
```

Each stage consumes the artifacts of the previous stage. No stage may reach backward or shortcut downstream concerns.

---

## Stage A — Structural Ingestion

### Responsibility

Convert raw documents into a stable structural representation.

Typical outputs include:

- Sections and headings
- Paragraphs
- Lists
- Tables
- Page and offset metadata

This stage establishes **source fidelity**.

### Inputs

- PDFs
- DOCX
- HTML
- Other document formats

### Outputs

- Document tree
- Block-level text units
- Layout and position metadata

### This Stage Does *Not* Do

- Semantic interpretation
- Rule identification
- Cross-section reasoning
- Any form of inference

This stage answers only:

> “What text exists, and where did it come from?”

---

## Stage B — Rule Unit Extraction

### Responsibility

Identify **candidate rule-bearing units** from structural blocks.

A Rule Unit is a *container*, not an executable rule.

Examples:

- A paragraph describing a spell effect
- A table defining costs or modifiers
- A section defining a condition

### Inputs

- Structural blocks from Stage A

### Outputs

```
RuleUnit {
  id
  source_block_ids[]
  kind (Rule | Definition | Constraint | Table | Glossary)
  raw_text
}
```

### This Stage Does *Not* Do

- Interpret rule meaning
- Decide precedence
- Resolve ambiguity
- Split rules into executable parts

This stage answers only:

> “Which pieces of text are worth treating as rules?”

---

## Stage C — Typed Rule Decomposition

### Responsibility

Decompose Rule Units into **typed, semantic fragments** aligned with the rules engine vocabulary.

Fragments make intent explicit without asserting execution order.

### Inputs

- RuleUnits

### Outputs

```
RuleFragment {
  rule_id
  fragment_type (Precondition | Effect | Cost | Constraint | Selector)
  subject
  predicate
  object
  qualifiers[]
}
```

### This Stage Does *Not* Do

- Decide evaluation order
- Resolve conflicts
- Invent missing semantics
- Hide uncertainty

Ambiguity must be preserved explicitly.

This stage answers:

> “What *claims* does this rule make about the world?”

---

## Stage D — Rule Graph Construction

### Responsibility

Connect fragments into a **typed rule graph** that exposes dependencies, scope, and impact.

### Inputs

- RuleFragments

### Outputs

- Nodes: Rules, Fragments, Entities, Resources, Attributes
- Edges: REQUIRES, MODIFIES, CONSUMES, PRODUCES, CONSTRAINS, REFERENCES

The graph is inspectable and queryable.

### This Stage Does *Not* Do

- Execute rules
- Resolve precedence
- Perform dynamic traversal at runtime

This stage answers:

> “How are rule components related?”

---

## Stage E — Compiler Feasibility Gate

### Responsibility

Determine whether a rule graph **can be compiled** into a deterministic rules engine.

This is a hard gate.

### Inputs

- Rule graph

### Outputs

```
CompilationReport {
  rule_id
  status (OK | NeedsHuman | Impossible)
  reasons[]
}
```

### Checks Performed

- Bounded reads and writes
- Explicit costs and effects
- Derivable evaluation order
- Absence of hidden global state

### This Stage Does *Not* Do

- Execute rules
- Repair rules
- Guess intent

If a rule does not pass, it does not compile.

---

## Projections (Downstream Consumers)

Once artifacts pass the feasibility gate, they may feed multiple projections:

- Deterministic rules engine
- RulesLawyer (explanation and citation)
- CharacterGenerator
- Audit logs
- Documentation views

Projections **never modify ingestion artifacts**.

---

## Non-Negotiable Invariants

Across all stages:

- No hidden inference
- No silent ambiguity resolution
- No runtime LLM involvement
- No backdoors around the compiler gate

Violating these invariants invalidates the pipeline.

---

## Why This Document Exists

This document exists to:

- Stop stage leakage
- Prevent premature optimization
- Anchor experiments to shared constraints

If a proposed change cannot be placed cleanly into one stage, it is likely wrong.

