# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `2`
- Query count: `2`
- Evaluated queries: `2`
- Coverage: `1.0000`
- MRR: `1.0000`
- hit@1: `1.0000`
- hit@3: `1.0000`
- hit@5: `1.0000`
- hit@10: `1.0000`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

### Expanded Gold Metrics
- Coverage: `1.0000`
- MRR: `1.0000`
- hit@1: `1.0000`
- hit@3: `1.0000`
- hit@5: `1.0000`
- hit@10: `1.0000`

### Expanded Gold Expansion Stats
- Queries with additions: `2`
- Avg added per query: `1.00`
- Max added: `1`
- Addition reasons:
  - graph_depth_1: `2`

### Expanded Gold Delta (Expanded - Strict)
- Coverage Δ: `0.0000`
- MRR Δ: `0.0000`
- hit@1 Δ: `0.0000`
- hit@3 Δ: `0.0000`
- hit@5 Δ: `0.0000`
- hit@10 Δ: `0.0000`

### Expanded Gold Note
- Expanded gold metrics match strict metrics (no change).

## Timings (ms)
- Embedding (chunks): `72`
- Embedding (queries): `69`
- Evaluation (strict): `0`
- Evaluation (expanded): `0`
- Total: `4724`

### Timing Estimates (ms)
- Evaluation (strict): `None`
- Evaluation (expanded): `None`
- Total: `None`

## Query Details
### Query 0
- Text: Summarize PZ022001-HC Printed
- Expected chunk IDs: ['PZO22001-HC Player Core 000::/page/0/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `2`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001-HC Player Core 000::/page/0/Text/5', 'PZO22001-HC Player Core 000::/page/0/Text/6']
- Expanded expected chunk IDs: ['PZO22001-HC Player Core 000::/page/0/Text/5', 'PZO22001-HC Player Core 000::/page/0/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001-HC Player Core 000::/page/0/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001-HC Player Core 000::/page/0/Text/5` | 0.955130 | PZ022001-HC Printed |
| 2 | `PZO22001-HC Player Core 000::/page/0/Text/6` | 0.251589 | Printed in China. |

### Query 1
- Text: Summarize Printed in China.
- Expected chunk IDs: ['PZO22001-HC Player Core 000::/page/0/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `2`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001-HC Player Core 000::/page/0/Text/6', 'PZO22001-HC Player Core 000::/page/0/Text/5']
- Expanded expected chunk IDs: ['PZO22001-HC Player Core 000::/page/0/Text/6', 'PZO22001-HC Player Core 000::/page/0/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001-HC Player Core 000::/page/0/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001-HC Player Core 000::/page/0/Text/6` | 0.866812 | Printed in China. |
| 2 | `PZO22001-HC Player Core 000::/page/0/Text/5` | 0.257258 | PZ022001-HC Printed |
