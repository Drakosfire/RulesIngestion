# RulesIngestion agent instructions

Start with the [README](README.md) for commands and the
[design index](Docs/Design/README.md) for active contracts. Read the owning
workflow before changing extraction, evidence binding, or retrieval evaluation.
Use archived designs for historical context.

Preserve source provenance and keep extraction changes separate from retrieval
benchmark changes when they can be reviewed independently. Use the committed
lockfile and run focused tests for the affected stage. For evaluation changes,
record the corpus, benchmark, configuration, run ID, and comparison baseline.
Keep generated run artifacts in the task-owned output location.
