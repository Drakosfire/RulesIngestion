# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `919`
- Query count: `156`
- Evaluated queries: `156`
- Coverage: `1.0000`
- MRR: `0.7945`
- hit@1: `0.7051`
- hit@3: `0.8526`
- hit@5: `0.8974`
- hit@10: `0.9936`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

### Expanded Gold Metrics
- Coverage: `1.0000`
- MRR: `0.8167`
- hit@1: `0.7372`
- hit@3: `0.8654`
- hit@5: `0.9038`
- hit@10: `0.9936`

### Expanded Gold Expansion Stats
- Queries with additions: `156`
- Avg added per query: `2.51`
- Max added: `11`
- Addition reasons:
  - graph_depth_1: `392`

### Expanded Gold Delta (Expanded - Strict)
- Coverage Δ: `0.0000`
- MRR Δ: `0.0223`
- hit@1 Δ: `0.0321`
- hit@3 Δ: `0.0128`
- hit@5 Δ: `0.0064`
- hit@10 Δ: `0.0000`

## Timings (ms)
- Embedding (chunks): `17891`
- Embedding (queries): `2503`
- Evaluation (strict): `78`
- Evaluation (expanded): `69`
- Total: `24796`

### Timing Estimates (ms)
- Evaluation (strict): `62`
- Evaluation (expanded): `46`
- Total: `20502`

## Query Details
### Query 0
- Text: What does **SUGGESTION **[two-actions] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/1']
- Expected found: `True`
- Expected rank: `10`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/15/Text/12', 'PZO22001 Starfinder Player Core 364-387::/page/16/SectionHeader/13', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/79']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `10`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/15/Text/12` | 0.614317 | **FORGET **[two-actions] **FOCUS 4** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/16/SectionHeader/13` | 0.599167 | **ACCELERATE **[two-actions] **FOCUS 4** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.593494 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` | 0.551494 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/27` | 0.551494 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.551494 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.551494 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.551494 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.551494 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/1` | 0.545450 | **SUGGESTION **[two-actions] **SPELL 4**  **CONCENTRATE** **INCAPACITATION** **LINGUISTIC** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creatu |

### Query 1
- Text: What does **SUMMON ANIMAL **[three-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12', 'PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/25', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/43']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12` | 0.735104 | **SUMMON ANIMAL **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/25` | 0.614570 | **SUMMON UNDEAD **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, divine, occult  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/43` | 0.612486 | **SUMMON ELEMENTAL **[three-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/18` | 0.573249 | **SUMMON ROBOT **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51` | 0.549733 | **SUMMON ENTITY **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** occult **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/58` | 0.544294 | **SUMMON FEY **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** occult, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature th |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/27` | 0.536377 | **SUMMON CONSTRUCT **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/20` | 0.525702 | **SUMMON CELESTIAL **[three-actions] **SPELL 5**  **CONCENTRATE** **HOLY** **MANIPULATE** **SUMMON**  **Traditions** divine **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/11` | 0.523180 | **SUMMON PLANT OR FUNGUS **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** primal **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/34` | 0.516378 | **SUMMON DRAGON **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, divine, occult, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You s |

### Query 2
- Text: What does **SUMMON CELESTIAL **[three-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/20', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/43']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/20', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/20` | 0.709034 | **SUMMON CELESTIAL **[three-actions] **SPELL 5**  **CONCENTRATE** **HOLY** **MANIPULATE** **SUMMON**  **Traditions** divine **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51` | 0.614927 | **SUMMON ENTITY **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** occult **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/43` | 0.562363 | **SUMMON ELEMENTAL **[three-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/34` | 0.530781 | **SUMMON DRAGON **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, divine, occult, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You s |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/73` | 0.514592 | **SUMMON GIANT **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12` | 0.500731 | **SUMMON ANIMAL **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/68` | 0.499185 | **SYNAPTIC PULSE **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** occult **Area** 30-foot emanation **Defense** Will; **Duration** 1 round |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/25` | 0.492233 | **SUMMON UNDEAD **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, divine, occult  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/66` | 0.491599 | **SUMMON FIEND **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON** **UNHOLY**  **Traditions** divine  **Range **30 feet **Duration** sustained up to 1 minute  You summon a creatur |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/4` | 0.484401 | **SUMMON MONITOR **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** divine **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that ha |

### Query 3
- Text: What does **SUMMON CONSTRUCT **[three-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/27', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/43', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/27', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/20', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/34']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/34` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/27` | 0.723876 | **SUMMON CONSTRUCT **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/43` | 0.575467 | **SUMMON ELEMENTAL **[three-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12` | 0.575245 | **SUMMON ANIMAL **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/25` | 0.524468 | **SUMMON UNDEAD **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, divine, occult  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51` | 0.523243 | **SUMMON ENTITY **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** occult **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/18` | 0.523092 | **SUMMON ROBOT **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/58` | 0.497220 | **SUMMON FEY **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** occult, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature th |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/20` | 0.497132 | **SUMMON CELESTIAL **[three-actions] **SPELL 5**  **CONCENTRATE** **HOLY** **MANIPULATE** **SUMMON**  **Traditions** divine **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/34` | 0.492858 | **SUMMON DRAGON **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, divine, occult, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You s |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/11` | 0.492171 | **SUMMON PLANT OR FUNGUS **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** primal **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature |

### Query 4
- Text: What does **SUMMON DRAGON **[three-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/34', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/34', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/43', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/43` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/34` | 0.697947 | **SUMMON DRAGON **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, divine, occult, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You s |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51` | 0.593557 | **SUMMON ENTITY **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** occult **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/20` | 0.570052 | **SUMMON CELESTIAL **[three-actions] **SPELL 5**  **CONCENTRATE** **HOLY** **MANIPULATE** **SUMMON**  **Traditions** divine **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/73` | 0.511723 | **SUMMON GIANT **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/43` | 0.498499 | **SUMMON ELEMENTAL **[three-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12` | 0.492621 | **SUMMON ANIMAL **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/66` | 0.479413 | **SUMMON FIEND **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON** **UNHOLY**  **Traditions** divine  **Range **30 feet **Duration** sustained up to 1 minute  You summon a creatur |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/18` | 0.476846 | **SUMMON ROBOT **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/25` | 0.472688 | **SUMMON UNDEAD **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, divine, occult  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/4` | 0.471770 | **SUMMON MONITOR **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** divine **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that ha |

### Query 5
- Text: What does **SUMMON ELEMENTAL **[three-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/43', 'PZO22001 Starfinder Player Core 364-387::/page/11/SectionHeader/28', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/43', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/34']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/34` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/43` | 0.679674 | **SUMMON ELEMENTAL **[three-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/11/SectionHeader/28` | 0.576117 | **ELEMENTAL WEAPON **[three-actions] **FOCUS 1** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51` | 0.548514 | **SUMMON ENTITY **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** occult **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.505016 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.505016 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.505016 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/27` | 0.505016 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` | 0.505016 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.505016 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.505016 | **SPELLS** |

### Query 6
- Text: What does **SUMMON ENTITY **[three-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/20', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/73']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/43', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/58']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/43` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/58` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51` | 0.707991 | **SUMMON ENTITY **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** occult **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/20` | 0.580915 | **SUMMON CELESTIAL **[three-actions] **SPELL 5**  **CONCENTRATE** **HOLY** **MANIPULATE** **SUMMON**  **Traditions** divine **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/73` | 0.565416 | **SUMMON GIANT **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/43` | 0.525208 | **SUMMON ELEMENTAL **[three-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/34` | 0.504542 | **SUMMON DRAGON **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, divine, occult, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You s |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/66` | 0.499173 | **SUMMON FIEND **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON** **UNHOLY**  **Traditions** divine  **Range **30 feet **Duration** sustained up to 1 minute  You summon a creatur |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12` | 0.491952 | **SUMMON ANIMAL **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/4` | 0.488487 | **SUMMON MONITOR **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** divine **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that ha |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/25` | 0.485210 | **SUMMON UNDEAD **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, divine, occult  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/27` | 0.475549 | **SUMMON CONSTRUCT **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that |

### Query 7
- Text: What does **SUMMON FEY **[three-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/58']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/58', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/43']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/58', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/66']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/66` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/58` | 0.696602 | **SUMMON FEY **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** occult, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature th |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12` | 0.556464 | **SUMMON ANIMAL **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/43` | 0.550733 | **SUMMON ELEMENTAL **[three-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51` | 0.519305 | **SUMMON ENTITY **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** occult **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/27` | 0.504660 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.504660 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` | 0.504660 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.504660 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.504660 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.504660 | **SPELLS** |

### Query 8
- Text: What does **SUMMON FIEND **[three-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/66']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/66', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/66', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/73', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/58']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/73` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/58` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/66` | 0.671379 | **SUMMON FIEND **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON** **UNHOLY**  **Traditions** divine  **Range **30 feet **Duration** sustained up to 1 minute  You summon a creatur |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51` | 0.628594 | **SUMMON ENTITY **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** occult **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/20` | 0.588945 | **SUMMON CELESTIAL **[three-actions] **SPELL 5**  **CONCENTRATE** **HOLY** **MANIPULATE** **SUMMON**  **Traditions** divine **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/73` | 0.542918 | **SUMMON GIANT **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/34` | 0.537181 | **SUMMON DRAGON **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, divine, occult, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You s |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/43` | 0.524521 | **SUMMON ELEMENTAL **[three-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/58` | 0.515121 | **SUMMON FEY **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** occult, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature th |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12` | 0.511088 | **SUMMON ANIMAL **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/25` | 0.506774 | **SUMMON UNDEAD **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, divine, occult  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/4` | 0.499477 | **SUMMON MONITOR **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** divine **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that ha |

### Query 9
- Text: What does **SUMMON GIANT **[three-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/73']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/73', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/73', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/66', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/81']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/66` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/81` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/73` | 0.727077 | **SUMMON GIANT **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51` | 0.623025 | **SUMMON ENTITY **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** occult **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/20` | 0.578805 | **SUMMON CELESTIAL **[three-actions] **SPELL 5**  **CONCENTRATE** **HOLY** **MANIPULATE** **SUMMON**  **Traditions** divine **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/34` | 0.518255 | **SUMMON DRAGON **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, divine, occult, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You s |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/66` | 0.506811 | **SUMMON FIEND **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON** **UNHOLY**  **Traditions** divine  **Range **30 feet **Duration** sustained up to 1 minute  You summon a creatur |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/43` | 0.506099 | **SUMMON ELEMENTAL **[three-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12` | 0.502234 | **SUMMON ANIMAL **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/4` | 0.494388 | **SUMMON MONITOR **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** divine **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that ha |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/25` | 0.483204 | **SUMMON UNDEAD **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, divine, occult  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/68` | 0.483132 | **SYNAPTIC PULSE **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** occult **Area** 30-foot emanation **Defense** Will; **Duration** 1 round |

### Query 10
- Text: What does **SUMMON INSTRUMENT **[three-actions] **CANTRIP 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/81']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/81', 'PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/57', 'PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/34']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/81', 'PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/4', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/73']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/73` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/81` | 0.803099 | **SUMMON INSTRUMENT **[three-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Duration** 1 hour  You materialize a handheld musical instrume |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/57` | 0.559605 | **TELEKINETIC PROJECTILE **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** 1 creature  **Defense** AC |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/34` | 0.539043 | **TELEKINETIC HAND **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** 1 unattended object of light Bulk or  less |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/27` | 0.491357 | **SUMMON CONSTRUCT **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/11/SectionHeader/28` | 0.488518 | **ELEMENTAL WEAPON **[three-actions] **FOCUS 1** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/7/SectionHeader/22` | 0.479143 | **VOID WARP **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE** **VOID**  **Traditions** arcane, divine, occult  **Range **30 feet;** Targets** 1 living creature  **Defense** For |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/12/SectionHeader/2` | 0.474316 | **INFUSION **[one-action]** TO **[three-actions] **FOCUS 1** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/12/SectionHeader/47` | 0.473550 | **SHADOW SNAP **[two-actions] **FOCUS 1** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/18` | 0.469564 | **SUMMON ROBOT **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/4` | 0.466344 | **SUMMON MONITOR **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** divine **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that ha |

### Query 11
- Text: What does **SUMMON MONITOR **[three-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/4', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/4', 'PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/81']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/81` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/4` | 0.668302 | **SUMMON MONITOR **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** divine **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that ha |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51` | 0.572746 | **SUMMON ENTITY **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** occult **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/20` | 0.540115 | **SUMMON CELESTIAL **[three-actions] **SPELL 5**  **CONCENTRATE** **HOLY** **MANIPULATE** **SUMMON**  **Traditions** divine **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/73` | 0.485137 | **SUMMON GIANT **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12` | 0.479372 | **SUMMON ANIMAL **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/43` | 0.477074 | **SUMMON ELEMENTAL **[three-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/18` | 0.472595 | **SUMMON ROBOT **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/34` | 0.472594 | **SUMMON DRAGON **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, divine, occult, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You s |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/68` | 0.470213 | **SYNAPTIC PULSE **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** occult **Area** 30-foot emanation **Defense** Will; **Duration** 1 round |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/27` | 0.462537 | **SUMMON CONSTRUCT **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that |

### Query 12
- Text: What does **SUMMON PLANT OR FUNGUS **[three-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12', 'PZO22001 Starfinder Player Core 364-387::/page/12/SectionHeader/47']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/4', 'PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/11` | 0.756162 | **SUMMON PLANT OR FUNGUS **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** primal **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12` | 0.562256 | **SUMMON ANIMAL **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/12/SectionHeader/47` | 0.554257 | **SHADOW SNAP **[two-actions] **FOCUS 1** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/25` | 0.509240 | **SUMMON UNDEAD **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, divine, occult  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/43` | 0.508953 | **SUMMON ELEMENTAL **[three-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51` | 0.506966 | **SUMMON ENTITY **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** occult **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/27` | 0.503624 | **SUMMON CONSTRUCT **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/18` | 0.499862 | **SUMMON ROBOT **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/11/SectionHeader/28` | 0.499580 | **ELEMENTAL WEAPON **[three-actions] **FOCUS 1** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/12/SectionHeader/2` | 0.495431 | **INFUSION **[one-action]** TO **[three-actions] **FOCUS 1** |

### Query 13
- Text: What does **SUMMON ROBOT **[three-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12', 'PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/25']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/25']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/18` | 0.712500 | **SUMMON ROBOT **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12` | 0.583716 | **SUMMON ANIMAL **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/25` | 0.560384 | **SUMMON UNDEAD **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, divine, occult  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/43` | 0.510481 | **SUMMON ELEMENTAL **[three-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/27` | 0.504252 | **SUMMON CONSTRUCT **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/11/SectionHeader/28` | 0.500637 | **ELEMENTAL WEAPON **[three-actions] **FOCUS 1** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/12/SectionHeader/47` | 0.493402 | **SHADOW SNAP **[two-actions] **FOCUS 1** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51` | 0.491243 | **SUMMON ENTITY **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** occult **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/58` | 0.489994 | **SUMMON FEY **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** occult, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature th |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/20` | 0.489105 | **SUMMON CELESTIAL **[three-actions] **SPELL 5**  **CONCENTRATE** **HOLY** **MANIPULATE** **SUMMON**  **Traditions** divine **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |

### Query 14
- Text: What does **SUMMON UNDEAD **[three-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/25', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/25', 'PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/33', 'PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/25` | 0.704423 | **SUMMON UNDEAD **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, divine, occult  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12` | 0.558509 | **SUMMON ANIMAL **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51` | 0.558497 | **SUMMON ENTITY **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** occult **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/43` | 0.520333 | **SUMMON ELEMENTAL **[three-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/18` | 0.519115 | **SUMMON ROBOT **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/27` | 0.507954 | **SUMMON CONSTRUCT **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/58` | 0.487604 | **SUMMON FEY **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** occult, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature th |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/20` | 0.486498 | **SUMMON CELESTIAL **[three-actions] **SPELL 5**  **CONCENTRATE** **HOLY** **MANIPULATE** **SUMMON**  **Traditions** divine **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.482440 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` | 0.482440 | **SPELLS** |

### Query 15
- Text: What does **SUNBURST **[TWO-ACTIONS] **SPELL 7** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/33']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/33', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/59', 'PZO22001 Starfinder Player Core 364-387::/page/21/Text/54']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/33', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/40', 'PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/25']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/33` | 0.688401 | **SUNBURST **[TWO-ACTIONS] **SPELL 7**  **CONCENTRATE** **FIRE** **LIGHT** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **500 feet;** Area** 60-foot burst  **Defense** Reflex  A |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/59` | 0.513944 | **EQUIPMENT** **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/54` | 0.513944 | **EQUIPMENT** **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/57` | 0.471944 | **EQUIPMENT** **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` | 0.470894 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.470894 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.470894 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.470894 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.470894 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.470894 | **SPELLS** |

### Query 16
- Text: Summarize **Critical Success** The creature is unaffected.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/40']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/10/Text/27', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/40', 'PZO22001 Starfinder Player Core 364-387::/page/16/Text/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/40', 'PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/33', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/41']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/41` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/10/Text/27` | 1.018921 | **Critical Success** The creature is unaffected. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/40` | 1.018921 | **Critical Success** The creature is unaffected. |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/16/Text/23` | 1.018921 | **Critical Success** The creature is unaffected. |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/4/Text/10` | 0.976921 | **Critical Success** The creature is unaffected. |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/2/Text/2` | 0.976921 | **Critical Success** The creature is unaffected. |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/12` | 0.976921 | **Critical Success** The creature is unaffected. |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/2` | 0.960064 | **Critical** **Success** The creature is unaffected. |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/7/Text/3` | 0.960064 | **Critical** **Success** The creature is unaffected. |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/6/Text/18` | 0.887048 | **Success** The creature is unaffected. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/7` | 0.770139 | **Critical** **Success** The target is unaffected. |

### Query 17
- Text: What is the rule about **Success** The creature takes half damage.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/41', 'PZO22001 Starfinder Player Core 364-387::/page/7/Text/4', 'PZO22001 Starfinder Player Core 364-387::/page/4/Text/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/41', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/40', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/42']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/42` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/41` | 0.837732 | **Success** The creature takes half damage. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/7/Text/4` | 0.837732 | **Success** The creature takes half damage. |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/4/Text/11` | 0.837732 | **Success** The creature takes half damage. |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/13` | 0.704717 | **Success** The creature takes full damage. |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/42` | 0.683437 | **Failure** The creature takes full damage. |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/16/Text/9` | 0.681856 | **Success** The target takes half damage. |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/63` | 0.681856 | **Success** The target takes half damage. |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/23` | 0.617611 | **Success** The target takes half damage and is stupefied 1  until the end of your current turn. |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/7/Text/3` | 0.614927 | **Critical** **Success** The creature is unaffected. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/4/Text/12` | 0.608888 | **Failure** The creature takes full damage and is sickened 1. |

### Query 18
- Text: What is the rule about **Failure** The creature takes full damage.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/42']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/42', 'PZO22001 Starfinder Player Core 364-387::/page/4/Text/12', 'PZO22001 Starfinder Player Core 364-387::/page/8/Text/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/42', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/41', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/43']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/41` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/43` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/42` | 0.896288 | **Failure** The creature takes full damage. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/4/Text/12` | 0.779323 | **Failure** The creature takes full damage and is sickened 1. |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/13` | 0.751316 | **Success** The creature takes full damage. |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/14` | 0.698631 | **Failure** The creature takes full damage and is drained 1d4. **Critical Failure** The creature takes double damage and is  drained 4. |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/43` | 0.682309 | **Critical Failure** The creature takes full damage and becomes  blinded permanently. |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/7/Text/5` | 0.668409 | **Failure** The creature takes full damage and 1d6 persistent  void damage, and becomes drained 1. |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/40` | 0.624026 | **Failure** The wall stops the movement of the flying  creature, and any remaining movement from its  current action is wasted. |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/4/Text/13` | 0.623083 | **Critical Failure** The creature takes double damage and is  sickened 2. |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/24` | 0.620766 | **Failure** The target takes full damage and is stupefied 1 until the  end of your next turn. You Recall Knowledge about the target. **Critical** **Failure** As failure, except the target takes double |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/41` | 0.618313 | **Success** The creature takes half damage. |

### Query 19
- Text: What is the rule about **Critical Failure** The creature takes full damage and becomes  blinded permanently.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/43', 'PZO22001 Starfinder Player Core 364-387::/page/6/Text/20', 'PZO22001 Starfinder Player Core 364-387::/page/8/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/43', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/44', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/42']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/44` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/42` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/43` | 0.940484 | **Critical Failure** The creature takes full damage and becomes  blinded permanently. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/6/Text/20` | 0.789456 | **Critical Failure** The creature is blinded for 1 minute. |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/14` | 0.753404 | **Failure** The creature takes full damage and is drained 1d4. **Critical Failure** The creature takes double damage and is  drained 4. |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/10/Text/30` | 0.694582 | **Critical Failure** As failure, and the creature is automatically  slowed 1 for 1 minute. |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/18/Text/32` | 0.689251 | **Critical Failure** The creature offends your deity and is  permanently cast out from the faith. The creature can't  rejoin your religion without a more direct intervention. |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/5` | 0.685392 | **Critical Failure** As failure, except the target babbles  incoherently. Any creature that begins its turn within  20 feet of the target must attempt a Will saving throw.  On a failure, it must use i |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/42` | 0.684899 | **Failure** The creature takes full damage. |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/41` | 0.682863 | **Critical Failure** As failure, and the creature is  pushed 10 feet away from the wall. |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/15/Text/11` | 0.671882 | **Critical Failure** The triggering attack misses. You are  undetected to that creature for 1 minute. If you use a  hostile action, this effect ends after that hostile action  is completed. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/6/Text/19` | 0.655209 | **Failure** The creature is blinded by the pattern. If it exits  the pattern, it can attempt a new save to recover from  the blinded condition at the end of each of its turns, to  a maximum duration o |

### Query 20
- Text: What is the rule about If the globe overlaps with an area of magical darkness,  *sunburst* attempts to counteract the darkness effect.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/44', 'PZO22001 Starfinder Player Core 364-387::/page/12/ListItem/16', 'PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/33']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/44', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/43', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/45']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/43` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/45` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/44` | 0.972228 | If the globe overlaps with an area of magical darkness,  *sunburst* attempts to counteract the darkness effect. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/12/ListItem/16` | 0.596826 | If you spend 20 or more Hit Points and the spell was  cast in an area of magical darkness, vitality nova  attempts to counteract the darkness effect. |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/33` | 0.581338 | **SUNBURST **[TWO-ACTIONS] **SPELL 7**  **CONCENTRATE** **FIRE** **LIGHT** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **500 feet;** Area** 60-foot burst  **Defense** Reflex  A |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/14/ListItem/14` | 0.523690 | You suppress terrain in your field, turning any existing  difficult or greater difficult terrain in your quantum field  to normal terrain. This does not apply to effects that  cause a creature to coun |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/20/Text/1` | 0.507408 | decreases the crop yield for farms. If you cast this ritual in an  area affected by *plant growth*, *blight* attempts to counteract  *plant growth* instead of producing its usual effect. |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/15/Text/23` | 0.493794 | You reset reality within your quantum field, purging  the area of all forms of data. All written information and  computer data in the area is subject to the effects of *delete*.  You attempt to count |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/14/Text/15` | 0.445979 | **Heightened (3rd)** You can choose to have the quantum  field fill with fog, smoke, or another phenomenon that  obscures vision. This functions as *mist*. You can instead  suppress one of these effec |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/6/SectionHeader/48` | 0.441775 | **VOID SCOUR **[two-actions] **SPELL 7**  **CONCENTRATE** **DARKNESS** **MANIPULATE** **VOID**  **Traditions** divine, primal  **Range **500 feet; **Area** 60-foot burst  **Defense** Reflex  A well of |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/14/Text/12` | 0.439642 | You materialize terrain features from another reality within  your quantum field. Choose one of the following effects, which  lasts as long as your quantum field remains active, until you  cast *warp* |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/14/Text/6` | 0.437777 | You see the probability equations all around you, tracing each  variable to every possible conclusion. Creatures you target  during this spell's duration can't benefit from circumstance  bonuses to AC |

### Query 21
- Text: What is the rule about **Heightened (+1)** The fire damage increases by 1d10, and the  vitality damage against undead increases by 1d10.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/45']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/45', 'PZO22001 Starfinder Player Core 364-387::/page/14/Text/23', 'PZO22001 Starfinder Player Core 364-387::/page/15/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/45', 'PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/46', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/44']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/46` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/44` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/45` | 0.943888 | **Heightened (+1)** The fire damage increases by 1d10, and the  vitality damage against undead increases by 1d10. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/14/Text/23` | 0.768610 | **Heightened (+1)** Damage increases by 1d12, persistent  damage increases by 1d6. |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/15/Text/19` | 0.735795 | **Heightened (+1)** The damage increases by 2d8. |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/4/Text/14` | 0.691691 | **Heightened (+1)** The damage increases by 2d6. |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/52` | 0.688934 | **Heightened** **(+1) **The damage increases by 2d6. |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/55` | 0.684873 | **Heightened (+1)** The cold damage increases by 1d10. |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/10` | 0.681019 | **Heightened (+1)** The amount of healing increases by 1d6,  and the extra healing for the 2-action version increases  by 6. |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/16/Text/12` | 0.655838 | **Heightened (+2)** Increase the damage by 1d10 and the  temporary Hit Points by 5. |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/7/Text/7` | 0.652966 | **Heightened (+1)** Increase the initial void damage by 2d10.  The persistent void damage increases by 1d6 on a  failure, or by 2d6 on critical failure. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/4/Text/2` | 0.635763 | **Heightened (+1)** The damage increases by 1d12 electricity  and 1d4 sonic. |

### Query 22
- Text: What does **SUPERCHARGE WEAPON **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/46']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/46', 'PZO22001 Starfinder Player Core 364-387::/page/11/SectionHeader/28', 'PZO22001 Starfinder Player Core 364-387::/page/9/Text/57']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/46', 'PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/53', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/45']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/53` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/45` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/46` | 0.720003 | **SUPERCHARGE WEAPON **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane  **Range **30 feet; **Targets** 1 weapon held by you or a willing ally **Duration** 1 minute or |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/11/SectionHeader/28` | 0.558399 | **ELEMENTAL WEAPON **[three-actions] **FOCUS 1** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/57` | 0.554128 | **EQUIPMENT** **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/54` | 0.512128 | **EQUIPMENT** **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/59` | 0.512128 | **EQUIPMENT** **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/16/ListItem/52` | 0.507227 | **Charge** **Object** The object restores all its spent  charges if its item level is up to your level minus  2. If the object is powered by electrical means but  doesn't use charges, it instead becom |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/12/SectionHeader/47` | 0.484898 | **SHADOW SNAP **[two-actions] **FOCUS 1** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/16/ListItem/51` | 0.484791 | **Discharge** **Object** The object loses all its remaining  charges if its item level is up to your level minus 2. If the  object is powered by electrical means but doesn't use  charges, it instead l |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.478290 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.478290 | **SPELLS** |

### Query 23
- Text: What does **SURE FOOTING **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/53']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/53', 'PZO22001 Starfinder Player Core 364-387::/page/15/Text/12', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/79']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/53', 'PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/62', 'PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/46']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/62` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/46` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/53` | 0.601736 | **SURE FOOTING **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You free the target's li |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/15/Text/12` | 0.525474 | **FORGET **[two-actions] **FOCUS 4** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.519791 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.477791 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.477791 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.477791 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` | 0.477791 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.477791 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/27` | 0.477791 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/63` | 0.474895 | **Focus Spells** |

### Query 24
- Text: What does **SURE STRIKE **[one-action] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/62']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/62', 'PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/47', 'PZO22001 Starfinder Player Core 364-387::/page/15/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/62', 'PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/68', 'PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/53']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/68` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/53` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/62` | 0.702905 | **SURE STRIKE **[one-action] **SPELL 1**  **CONCENTRATE** **FORTUNE**  **Traditions** arcane, occult  **Duration** until the end of your turn  A glimpse into the future ensures your next blow strikes |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/47` | 0.553919 | **THUNDERSTRIKE **[two-actions] **SPELL 1**  **CONCENTRATE** **ELECTRICITY** **MANIPULATE** **SONIC**  **Traditions** arcane, primal  **Range **120 feet; **Targets** 1 creature  **Defense** basic Refl |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/15/Text/5` | 0.536807 | **Trigger** An enemy targets you with a Strike or spell attack. |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` | 0.473096 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.473096 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.473096 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/27` | 0.473096 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.473096 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.473096 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.473096 | **SPELLS** |

### Query 25
- Text: What does **SYNAPTIC PULSE **[two-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/68']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/68', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/59', 'PZO22001 Starfinder Player Core 364-387::/page/9/Text/57']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/68', 'PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/62', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/73']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/62` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/73` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/68` | 0.782669 | **SYNAPTIC PULSE **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** occult **Area** 30-foot emanation **Defense** Will; **Duration** 1 round |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/59` | 0.521619 | **EQUIPMENT** **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/57` | 0.521619 | **EQUIPMENT** **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/54` | 0.479619 | **EQUIPMENT** **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` | 0.474132 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.474132 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.474132 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.474132 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.474132 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.474132 | **SPELLS** |

### Query 26
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/73']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/73', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/54', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/66']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/73', 'PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/68', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/74']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/68` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/74` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/73` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/54` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/66` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/52` | 0.838541 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/54` | 0.838541 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/49` | 0.838541 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/47` | 0.838541 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/35` | 0.838541 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/21` | 0.838541 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/69` | 0.838541 | **INTRODUCTION** |

### Query 27
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/74']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/74', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/55', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/67']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/74', 'PZO22001 Starfinder Player Core 364-387::/page/9/Text/53', 'PZO22001 Starfinder Player Core 364-387::/page/17/Text/22', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/70', 'PZO22001 Starfinder Player Core 364-387::/page/21/Text/50', 'PZO22001 Starfinder Player Core 364-387::/page/19/Text/48', 'PZO22001 Starfinder Player Core 364-387::/page/11/Text/55', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/75', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/67', 'PZO22001 Starfinder Player Core 364-387::/page/23/Text/36', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/55', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/73']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/9/Text/53` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/17/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/13/Text/70` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/21/Text/50` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/19/Text/48` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/11/Text/55` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/75` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/67` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/23/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/55` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/73` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/74` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/55` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/67` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/53` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/22` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/70` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/50` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/55` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/48` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/36` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 28
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/75']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/75', 'PZO22001 Starfinder Player Core 364-387::/page/21/Text/51', 'PZO22001 Starfinder Player Core 364-387::/page/9/Text/54']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/75', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/68', 'PZO22001 Starfinder Player Core 364-387::/page/21/Text/51', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/76', 'PZO22001 Starfinder Player Core 364-387::/page/23/Text/37', 'PZO22001 Starfinder Player Core 364-387::/page/11/Text/56', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/56', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/71', 'PZO22001 Starfinder Player Core 364-387::/page/9/Text/54', 'PZO22001 Starfinder Player Core 364-387::/page/19/Text/49', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/74', 'PZO22001 Starfinder Player Core 364-387::/page/17/Text/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/68` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/21/Text/51` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/76` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/23/Text/37` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/11/Text/56` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/56` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/13/Text/71` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/9/Text/54` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/19/Text/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/74` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/17/Text/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/75` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/54` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/51` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/68` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/49` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/23` | 0.910061 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/71` | 0.910061 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/56` | 0.910061 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/56` | 0.910061 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/37` | 0.910061 | **CLASSES** |

### Query 29
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/76']
- Expected found: `True`
- Expected rank: `10`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/17/Text/24', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/57', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/69']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/76', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/77', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/75']
- Expanded expected found: `True`
- Expanded expected rank: `10`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/77` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/75` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/24` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/57` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/69` | 0.864442 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/72` | 0.822442 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/55` | 0.822442 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/57` | 0.822442 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/52` | 0.822442 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/50` | 0.822442 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/38` | 0.822442 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/76` | 0.822442 | **SKILLS** |

### Query 30
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/77']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/77', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/58', 'PZO22001 Starfinder Player Core 364-387::/page/19/Text/51']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/77', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/78', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/76']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/78` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/76` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/77` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/58` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/51` | 0.871817 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/39` | 0.829817 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/56` | 0.829817 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/70` | 0.829817 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/73` | 0.829817 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/53` | 0.829817 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/25` | 0.829817 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/58` | 0.829817 | **FEATS** |

### Query 31
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/78']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/78', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/71', 'PZO22001 Starfinder Player Core 364-387::/page/23/Text/40']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/78', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/79', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/77']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/77` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/78` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/71` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/40` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/59` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/74` | 0.902726 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/26` | 0.902726 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/52` | 0.902726 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/57` | 0.578761 | **EQUIPMENT** **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/59` | 0.578761 | **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/54` | 0.578761 | **EQUIPMENT** **SPELLS** |

### Query 32
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/79']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/23/Text/41', 'PZO22001 Starfinder Player Core 364-387::/page/17/Text/27', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/75']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/79', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/78', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/80']
- Expanded expected found: `True`
- Expanded expected rank: `7`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/78` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/80` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/27` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` | 0.847304 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.847304 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/57` | 0.759411 | **EQUIPMENT** **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/59` | 0.759411 | **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/54` | 0.759411 | **EQUIPMENT** **SPELLS** |

### Query 33
- Text: What is the rule about **Spell Lists**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/80']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/80', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/60', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/73']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/80', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/79', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/81']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/81` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/80` | 0.890837 | **Spell Lists** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/60` | 0.890837 | **Spell Lists** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/73` | 0.890837 | **Spell Lists** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/55` | 0.848837 | **Spell Lists** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/58` | 0.848837 | **Spell Lists** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/76` | 0.848837 | **Spell Lists** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/54` | 0.848837 | **Spell Lists** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/42` | 0.848837 | **Spell Lists** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/28` | 0.848837 | **Spell Lists** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/61` | 0.848837 | **Spell Lists** |

### Query 34
- Text: What is the rule about **Spells**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/81']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/23/Text/43', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/77', 'PZO22001 Starfinder Player Core 364-387::/page/19/Text/55']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/81', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/82', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/80']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/82` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/80` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/43` | 0.798799 | **Spells** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/77` | 0.798799 | **Spells** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/55` | 0.798799 | **Spells** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/62` | 0.756799 | **Spells** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/29` | 0.756799 | **Spells** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/81` | 0.756799 | **Spells** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/74` | 0.756799 | **Spells** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/59` | 0.756799 | **Spells** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/61` | 0.756799 | **Spells** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/56` | 0.756799 | **Spells** |

### Query 35
- Text: What is the rule about **Focus Spells**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/82']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/11/Text/63', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/78', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/82']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/82', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/83', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/81']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/83` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/81` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/63` | 0.926221 | **Focus Spells** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/78` | 0.926221 | **Focus Spells** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/82` | 0.926221 | **Focus Spells** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/56` | 0.884221 | **Focus Spells** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/44` | 0.884221 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/62` | 0.884221 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/30` | 0.884221 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/75` | 0.884221 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/60` | 0.884221 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/57` | 0.884221 | **Focus Spells** |

### Query 36
- Text: Summarize **Rituals**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/83']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/13/Text/79', 'PZO22001 Starfinder Player Core 364-387::/page/23/Text/45', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/76']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/83', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/82', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/84']
- Expanded expected found: `True`
- Expanded expected rank: `7`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/82` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/84` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/79` | 0.971114 | **Rituals** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/45` | 0.971114 | **Rituals** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/76` | 0.971114 | **Rituals** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/31` | 0.929114 | **Rituals** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/61` | 0.929114 | **Rituals** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/57` | 0.929114 | **Rituals** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/83` | 0.929114 | **Rituals** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/64` | 0.929114 | **Rituals** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/63` | 0.929114 | **Rituals** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/58` | 0.929114 | **Rituals** |

### Query 37
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/84']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/23/Text/46', 'PZO22001 Starfinder Player Core 364-387::/page/19/Text/58', 'PZO22001 Starfinder Player Core 364-387::/page/11/Text/65']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/84', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/83', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/85']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/83` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/85` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/46` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/58` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/65` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/84` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/77` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/32` | 0.923000 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/62` | 0.923000 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/80` | 0.923000 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/64` | 0.923000 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/59` | 0.923000 | **PLAYING THE ** **GAME** |

### Query 38
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/85']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/85', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/65', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/81']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/85', 'PZO22001 Starfinder Player Core 364-387::/page/21/Text/60', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/78', 'PZO22001 Starfinder Player Core 364-387::/page/23/Text/47', 'PZO22001 Starfinder Player Core 364-387::/page/19/Text/59', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/81', 'PZO22001 Starfinder Player Core 364-387::/page/17/Text/33', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/65', 'PZO22001 Starfinder Player Core 364-387::/page/11/Text/66', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/84', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/86', 'PZO22001 Starfinder Player Core 364-387::/page/9/Text/63']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/21/Text/60` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/78` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/23/Text/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/19/Text/59` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/13/Text/81` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/17/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/65` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/11/Text/66` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/84` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/86` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/9/Text/63` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/85` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/65` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/81` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/66` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/63` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/60` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/59` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/33` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/47` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/78` | 0.645203 | **CONDITIONS ** |

### Query 39
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/86']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/23/Text/48', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/86', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/66']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/86', 'PZO22001 Starfinder Player Core 364-387::/page/2/Text/1', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/85']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/2/Text/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/85` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/48` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/86` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/66` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/61` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/64` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/82` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/67` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/60` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/34` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/79` | 0.697531 | **APPENDIX** **GLOSSARY & ** |

### Query 40
- Text: What is the rule about You emit a pulsating mental blast that penetrates the minds  of all enemies in the area. Each enemy in the area must  attempt a Will save.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/2/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/2/Text/1', 'PZO22001 Starfinder Player Core 364-387::/page/16/Text/48', 'PZO22001 Starfinder Player Core 364-387::/page/10/SectionHeader/32']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/2/Text/1', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/86', 'PZO22001 Starfinder Player Core 364-387::/page/2/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/86` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/2/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/2/Text/1` | 0.938717 | You emit a pulsating mental blast that penetrates the minds  of all enemies in the area. Each enemy in the area must  attempt a Will save. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/16/Text/48` | 0.599848 | You briefly establish a mystical connection between your  mind and a piece of technology, allowing you to understand  the object or manipulate its power. Choose any one of the  following effects. An u |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/10/SectionHeader/32` | 0.585985 | **WAVE OF WARNING **[two-actions] **SPELL 5**  **CONCENTRATE** **EMOTION** **FEAR** **MANIPULATE** **MENTAL** **NONLETHAL**  **Traditions** divine, primal  **Range **120 feet; **Targets **1 creature, |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/10/SectionHeader/44` | 0.551110 | **WEIGHT OF AGES **[two-actions] **SPELL 4**  **ATTACK** **CONCENTRATE** **MANIPULATE**  **Traditions** divine, occult  **Range **120 feet; **Targets** 1 creature **Defense** Will; **Duration** 1 minu |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/59` | 0.525460 | **VIBE CHECK **[two-actions] **SPELL 2**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** occult  **Range **60 feet; **Targets** 1 creature **Defense** Will; **Duration** 1 round |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/15/Text/8` | 0.525107 | Your presence flickers in the target's mind as though you  had disappeared. The triggering creature attempts a Will  save. |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/6` | 0.522467 | You cause memories of the target's resentment, regret, and  other negative feelings to engorge its shadow until it grows  large enough to swallow them whole. The target attempts a  Will saving throw. |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/42` | 0.509712 | **WARP MIND **[two-actions] **SPELL 7**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **120 feet;** Targets** 1 creature  **Defense* |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/15/Text/18` | 0.499399 | The first time an enemy attempts to locate the target  (such as by Seeking) or uses Recall Knowledge to recall  information about the target, they take 8d8 mental damage  with a basic Will save as the |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/38` | 0.498879 | You shuffle the cosmic mix to repeat one creature's personal  anthem, further motivating and empowering them. The  target's Strikes deal an additional die of sonic damage and  the target gains a +1 st |

### Query 41
- Text: Summarize **Critical Success** The creature is unaffected.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/2/Text/2']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/10/Text/27', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/40', 'PZO22001 Starfinder Player Core 364-387::/page/16/Text/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/2/Text/2', 'PZO22001 Starfinder Player Core 364-387::/page/2/Text/1', 'PZO22001 Starfinder Player Core 364-387::/page/2/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/2/Text/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/2/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/10/Text/27` | 1.018921 | **Critical Success** The creature is unaffected. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/40` | 1.018921 | **Critical Success** The creature is unaffected. |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/16/Text/23` | 1.018921 | **Critical Success** The creature is unaffected. |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/4/Text/10` | 0.976921 | **Critical Success** The creature is unaffected. |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/2/Text/2` | 0.976921 | **Critical Success** The creature is unaffected. |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/12` | 0.976921 | **Critical Success** The creature is unaffected. |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/2` | 0.960064 | **Critical** **Success** The creature is unaffected. |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/7/Text/3` | 0.960064 | **Critical** **Success** The creature is unaffected. |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/6/Text/18` | 0.887048 | **Success** The creature is unaffected. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/7` | 0.770139 | **Critical** **Success** The target is unaffected. |

### Query 42
- Text: Summarize **Success** The creature is stunned 1. **Failure** The creature is stunned 2.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/2/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/2/Text/3', 'PZO22001 Starfinder Player Core 364-387::/page/16/Text/25', 'PZO22001 Starfinder Player Core 364-387::/page/16/Text/24']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/2/Text/3', 'PZO22001 Starfinder Player Core 364-387::/page/2/Text/2', 'PZO22001 Starfinder Player Core 364-387::/page/2/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/2/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/2/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/2/Text/3` | 1.024648 | **Success** The creature is stunned 1. **Failure** The creature is stunned 2. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/16/Text/25` | 0.909850 | **Failure** The creature is stunned 2. |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/16/Text/24` | 0.897210 | **Success** The creature is stunned 1. |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/16/Text/26` | 0.756199 | **Critical Failure** The creature is stunned 3 and slowed 1 for  1 minute. |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/2/Text/4` | 0.749767 | **Critical Failure** The creature is stunned for 1 round. |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/2` | 0.685581 | **Critical** **Success** The creature is unaffected. |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/7/Text/3` | 0.685581 | **Critical** **Success** The creature is unaffected. |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/10/Text/28` | 0.664708 | **Success** For 1 round, the creature can't use reactions and  must attempt another save at the start of its turn; on a  failure, it is slowed 1 for that turn as it sobs uncontrollably. |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/2/Text/2` | 0.659179 | **Critical Success** The creature is unaffected. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/16/Text/23` | 0.659179 | **Critical Success** The creature is unaffected. |

### Query 43
- Text: Summarize **Critical Failure** The creature is stunned for 1 round.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/2/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/2/Text/4', 'PZO22001 Starfinder Player Core 364-387::/page/16/Text/26', 'PZO22001 Starfinder Player Core 364-387::/page/16/Text/25']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/2/Text/4', 'PZO22001 Starfinder Player Core 364-387::/page/2/Text/3', 'PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/2/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/2/Text/4` | 1.036383 | **Critical Failure** The creature is stunned for 1 round. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/16/Text/26` | 0.894922 | **Critical Failure** The creature is stunned 3 and slowed 1 for  1 minute. |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/16/Text/25` | 0.830533 | **Failure** The creature is stunned 2. |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/16/Text/24` | 0.785906 | **Success** The creature is stunned 1. |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/2/Text/3` | 0.771159 | **Success** The creature is stunned 1. **Failure** The creature is stunned 2. |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/10/Text/28` | 0.706595 | **Success** For 1 round, the creature can't use reactions and  must attempt another save at the start of its turn; on a  failure, it is slowed 1 for that turn as it sobs uncontrollably. |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/10/Text/30` | 0.697949 | **Critical Failure** As failure, and the creature is automatically  slowed 1 for 1 minute. |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/6/Text/20` | 0.691859 | **Critical Failure** The creature is blinded for 1 minute. |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/14` | 0.683290 | **Failure** The creature takes full damage and is drained 1d4. **Critical Failure** The creature takes double damage and is  drained 4. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/4/Text/12` | 0.677151 | **Failure** The creature takes full damage and is sickened 1. |

### Query 44
- Text: What does **TAILWIND **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/5', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/79', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/72']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/5', 'PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/12', 'PZO22001 Starfinder Player Core 364-387::/page/2/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/2/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/5` | 0.675350 | **TAILWIND **[two-actions] **SPELL 1**  **AIR** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Duration** 1 hour  The wind at your back pushes you to find new horizons. You  gain a + |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.533801 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` | 0.533801 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/27` | 0.491801 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.491801 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.491801 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.491801 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.491801 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/54` | 0.466559 | **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/59` | 0.466559 | **EQUIPMENT** **SPELLS** |

### Query 45
- Text: What does **TALKING CORPSE** **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/12']
- Expected found: `True`
- Expected rank: `11`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/59', 'PZO22001 Starfinder Player Core 364-387::/page/21/Text/54', 'PZO22001 Starfinder Player Core 364-387::/page/9/Text/57']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/12', 'PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/23', 'PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/5']
- Expanded expected found: `True`
- Expanded expected rank: `11`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/59` | 0.606480 | **EQUIPMENT** **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/54` | 0.606480 | **EQUIPMENT** **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/57` | 0.606480 | **EQUIPMENT** **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` | 0.560773 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.560773 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/27` | 0.560773 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.560773 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.560773 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.560773 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.560773 | **SPELLS** |

### Query 46
- Text: What does **TANGLE VINE **[two-actions] **CANTRIP 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/23', 'PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/57', 'PZO22001 Starfinder Player Core 364-387::/page/7/SectionHeader/22']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/23', 'PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/12', 'PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/34']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/34` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/23` | 0.787353 | **TANGLE VINE **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE** **PLANT** **WOOD**  **Traditions** arcane, primal  **Range **30 feet; **Targets** 1 creature  **Defen |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/57` | 0.584547 | **TELEKINETIC PROJECTILE **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** 1 creature  **Defense** AC |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/7/SectionHeader/22` | 0.538135 | **VOID WARP **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE** **VOID**  **Traditions** arcane, divine, occult  **Range **30 feet;** Targets** 1 living creature  **Defense** For |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/34` | 0.498789 | **TELEKINETIC HAND **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** 1 unattended object of light Bulk or  less |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/81` | 0.491306 | **SUMMON INSTRUMENT **[three-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Duration** 1 hour  You materialize a handheld musical instrume |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/6/SectionHeader/40` | 0.466377 | **VITALITY LASH **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet; **Targets** 1 creature that is undead or  othe |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/23` | 0.457610 | **TRANSLATE **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult **Range **30 feet;** Targets** 1 creature  **Duration** 1 hour  The target can understand |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/47` | 0.442484 | **THUNDERSTRIKE **[two-actions] **SPELL 1**  **CONCENTRATE** **ELECTRICITY** **MANIPULATE** **SONIC**  **Traditions** arcane, primal  **Range **120 feet; **Targets** 1 creature  **Defense** basic Refl |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/12/SectionHeader/47` | 0.432112 | **SHADOW SNAP **[two-actions] **FOCUS 1** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/10/SectionHeader/55` | 0.426252 | **WISP ALLY **[two-actions] **SPELL 1**  **CONCENTRATE** **LIGHT** **MANIPULATE**  **Traditions** divine, primal  **Range **120 feet; **Target** one creature  **Defense** Will; **Duration** sustained |

### Query 47
- Text: What does **TELEKINETIC HAND **[two-actions] **CANTRIP 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/34', 'PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/57', 'PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/51']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/34', 'PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/23', 'PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/44']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/44` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/34` | 0.774023 | **TELEKINETIC HAND **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** 1 unattended object of light Bulk or  less |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/57` | 0.719549 | **TELEKINETIC PROJECTILE **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** 1 creature  **Defense** AC |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/51` | 0.614150 | **TELEKINETIC MANEUVER **[two-actions] **SPELL 2**  **ATTACK** **CONCENTRATE** **FORCE** **MANIPULATE**  **Traditions** arcane, occult  **Range **60 feet;** Targets** 1 creature  With a rush of teleki |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/81` | 0.556611 | **SUMMON INSTRUMENT **[three-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Duration** 1 hour  You materialize a handheld musical instrume |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/12` | 0.556364 | **TELEKINETIC TANTRUM **[three-actions] **SPELL 9**  **ATTACK** **CONCENTRATE** **FORCE** **MANIPULATE**  **Traditions** arcane, occult  **Range **500 feet;** Area** 100-foot burst  **Defense** see te |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/44` | 0.552117 | **TELEKINETIC HAUL **[two-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet; **Targets** 1 unattended object of up to 80 Bulk  with no dimension l |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/5` | 0.548423 | **TELEKINETIC STRANGULATION **[two-actions] **SPELL 6**  **ATTACK** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** divine, occult  **Range **30 feet;** Targets** 1 creature  **Defen |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/23` | 0.492739 | **TANGLE VINE **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE** **PLANT** **WOOD**  **Traditions** arcane, primal  **Range **30 feet; **Targets** 1 creature  **Defen |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/47` | 0.483720 | **THUNDERSTRIKE **[two-actions] **SPELL 1**  **CONCENTRATE** **ELECTRICITY** **MANIPULATE** **SONIC**  **Traditions** arcane, primal  **Range **120 feet; **Targets** 1 creature  **Defense** basic Refl |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/7/SectionHeader/22` | 0.472971 | **VOID WARP **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE** **VOID**  **Traditions** arcane, divine, occult  **Range **30 feet;** Targets** 1 living creature  **Defense** For |

### Query 48
- Text: What does **TELEKINETIC HAUL **[two-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/44', 'PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/51', 'PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/44', 'PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/34', 'PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/51']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/51` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/44` | 0.724091 | **TELEKINETIC HAUL **[two-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet; **Targets** 1 unattended object of up to 80 Bulk  with no dimension l |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/51` | 0.616033 | **TELEKINETIC MANEUVER **[two-actions] **SPELL 2**  **ATTACK** **CONCENTRATE** **FORCE** **MANIPULATE**  **Traditions** arcane, occult  **Range **60 feet;** Targets** 1 creature  With a rush of teleki |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/12` | 0.558416 | **TELEKINETIC TANTRUM **[three-actions] **SPELL 9**  **ATTACK** **CONCENTRATE** **FORCE** **MANIPULATE**  **Traditions** arcane, occult  **Range **500 feet;** Area** 100-foot burst  **Defense** see te |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/57` | 0.512989 | **TELEKINETIC PROJECTILE **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** 1 creature  **Defense** AC |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/34` | 0.497397 | **TELEKINETIC HAND **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** 1 unattended object of light Bulk or  less |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/5` | 0.496511 | **TELEKINETIC STRANGULATION **[two-actions] **SPELL 6**  **ATTACK** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** divine, occult  **Range **30 feet;** Targets** 1 creature  **Defen |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/68` | 0.490798 | **SYNAPTIC PULSE **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** occult **Area** 30-foot emanation **Defense** Will; **Duration** 1 round |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/59` | 0.478200 | **EQUIPMENT** **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/54` | 0.478200 | **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/57` | 0.478200 | **EQUIPMENT** **SPELLS** |

### Query 49
- Text: What does **TELEKINETIC MANEUVER **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/51']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/51', 'PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/44', 'PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/51', 'PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/57', 'PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/44']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/57` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/44` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/51` | 0.735059 | **TELEKINETIC MANEUVER **[two-actions] **SPELL 2**  **ATTACK** **CONCENTRATE** **FORCE** **MANIPULATE**  **Traditions** arcane, occult  **Range **60 feet;** Targets** 1 creature  With a rush of teleki |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/44` | 0.592976 | **TELEKINETIC HAUL **[two-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet; **Targets** 1 unattended object of up to 80 Bulk  with no dimension l |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/5` | 0.554537 | **TELEKINETIC STRANGULATION **[two-actions] **SPELL 6**  **ATTACK** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** divine, occult  **Range **30 feet;** Targets** 1 creature  **Defen |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/34` | 0.513720 | **TELEKINETIC HAND **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** 1 unattended object of light Bulk or  less |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/12` | 0.510243 | **TELEKINETIC TANTRUM **[three-actions] **SPELL 9**  **ATTACK** **CONCENTRATE** **FORCE** **MANIPULATE**  **Traditions** arcane, occult  **Range **500 feet;** Area** 100-foot burst  **Defense** see te |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/57` | 0.505605 | **TELEKINETIC PROJECTILE **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** 1 creature  **Defense** AC |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/59` | 0.503298 | **EQUIPMENT** **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/57` | 0.503298 | **EQUIPMENT** **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/54` | 0.503298 | **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/22` | 0.475966 | **TELEPATHY **[two-actions] **SPELL 4**  **CONCENTRATE** **LINGUISTIC** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Duration** 10 minutes  You can communicate telepathically with creat |

### Query 50
- Text: What does **TELEKINETIC PROJECTILE **[two-actions] **CANTRIP 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/57']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/57', 'PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/34', 'PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/51']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/57', 'PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/51', 'PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/51` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/57` | 0.777199 | **TELEKINETIC PROJECTILE **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** 1 creature  **Defense** AC |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/34` | 0.671933 | **TELEKINETIC HAND **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** 1 unattended object of light Bulk or  less |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/51` | 0.579443 | **TELEKINETIC MANEUVER **[two-actions] **SPELL 2**  **ATTACK** **CONCENTRATE** **FORCE** **MANIPULATE**  **Traditions** arcane, occult  **Range **60 feet;** Targets** 1 creature  With a rush of teleki |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/44` | 0.532750 | **TELEKINETIC HAUL **[two-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet; **Targets** 1 unattended object of up to 80 Bulk  with no dimension l |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/12` | 0.527487 | **TELEKINETIC TANTRUM **[three-actions] **SPELL 9**  **ATTACK** **CONCENTRATE** **FORCE** **MANIPULATE**  **Traditions** arcane, occult  **Range **500 feet;** Area** 100-foot burst  **Defense** see te |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/5` | 0.517213 | **TELEKINETIC STRANGULATION **[two-actions] **SPELL 6**  **ATTACK** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** divine, occult  **Range **30 feet;** Targets** 1 creature  **Defen |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/81` | 0.515992 | **SUMMON INSTRUMENT **[three-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Duration** 1 hour  You materialize a handheld musical instrume |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/47` | 0.501197 | **THUNDERSTRIKE **[two-actions] **SPELL 1**  **CONCENTRATE** **ELECTRICITY** **MANIPULATE** **SONIC**  **Traditions** arcane, primal  **Range **120 feet; **Targets** 1 creature  **Defense** basic Refl |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/23` | 0.487140 | **TANGLE VINE **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE** **PLANT** **WOOD**  **Traditions** arcane, primal  **Range **30 feet; **Targets** 1 creature  **Defen |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/6/SectionHeader/40` | 0.469947 | **VITALITY LASH **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet; **Targets** 1 creature that is undead or  othe |

### Query 51
- Text: What does **TELEKINETIC STRANGULATION **[two-actions] **SPELL 6** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/5', 'PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/51', 'PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/44']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/5', 'PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/12', 'PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/57']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/57` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/5` | 0.693023 | **TELEKINETIC STRANGULATION **[two-actions] **SPELL 6**  **ATTACK** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** divine, occult  **Range **30 feet;** Targets** 1 creature  **Defen |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/51` | 0.591274 | **TELEKINETIC MANEUVER **[two-actions] **SPELL 2**  **ATTACK** **CONCENTRATE** **FORCE** **MANIPULATE**  **Traditions** arcane, occult  **Range **60 feet;** Targets** 1 creature  With a rush of teleki |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/44` | 0.574831 | **TELEKINETIC HAUL **[two-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet; **Targets** 1 unattended object of up to 80 Bulk  with no dimension l |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/57` | 0.531110 | **TELEKINETIC PROJECTILE **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** 1 creature  **Defense** AC |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/12` | 0.529752 | **TELEKINETIC TANTRUM **[three-actions] **SPELL 9**  **ATTACK** **CONCENTRATE** **FORCE** **MANIPULATE**  **Traditions** arcane, occult  **Range **500 feet;** Area** 100-foot burst  **Defense** see te |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/14/SectionHeader/32` | 0.520926 | **PARALLEL FORMS **[two-actions] **FOCUS 6** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/34` | 0.503161 | **TELEKINETIC HAND **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** 1 unattended object of light Bulk or  less |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/11/SectionHeader/16` | 0.491330 | **DATA DRAIN **[two-actions] **FOCUS 6** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/22` | 0.487792 | **TELEPATHY **[two-actions] **SPELL 4**  **CONCENTRATE** **LINGUISTIC** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Duration** 10 minutes  You can communicate telepathically with creat |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/12/SectionHeader/39` | 0.482503 | **REMIX **[two-actions] **FOCUS 6** |

### Query 52
- Text: What does **TELEKINETIC TANTRUM **[three-actions] **SPELL 9** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/12', 'PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/51', 'PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/12', 'PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/5', 'PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/12` | 0.738690 | **TELEKINETIC TANTRUM **[three-actions] **SPELL 9**  **ATTACK** **CONCENTRATE** **FORCE** **MANIPULATE**  **Traditions** arcane, occult  **Range **500 feet;** Area** 100-foot burst  **Defense** see te |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/51` | 0.602913 | **TELEKINETIC MANEUVER **[two-actions] **SPELL 2**  **ATTACK** **CONCENTRATE** **FORCE** **MANIPULATE**  **Traditions** arcane, occult  **Range **60 feet;** Targets** 1 creature  With a rush of teleki |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/5` | 0.563175 | **TELEKINETIC STRANGULATION **[two-actions] **SPELL 6**  **ATTACK** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** divine, occult  **Range **30 feet;** Targets** 1 creature  **Defen |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/44` | 0.512719 | **TELEKINETIC HAUL **[two-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet; **Targets** 1 unattended object of up to 80 Bulk  with no dimension l |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/34` | 0.502826 | **TELEKINETIC HAND **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** 1 unattended object of light Bulk or  less |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/2/SectionHeader/57` | 0.502653 | **TELEKINETIC PROJECTILE **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** 1 creature  **Defense** AC |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/47` | 0.499498 | **THUNDERSTRIKE **[two-actions] **SPELL 1**  **CONCENTRATE** **ELECTRICITY** **MANIPULATE** **SONIC**  **Traditions** arcane, primal  **Range **120 feet; **Targets** 1 creature  **Defense** basic Refl |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/22` | 0.476130 | **TELEPATHY **[two-actions] **SPELL 4**  **CONCENTRATE** **LINGUISTIC** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Duration** 10 minutes  You can communicate telepathically with creat |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/68` | 0.452963 | **SYNAPTIC PULSE **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** occult **Area** 30-foot emanation **Defense** Will; **Duration** 1 round |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/23` | 0.445220 | **TRANSLATE **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult **Range **30 feet;** Targets** 1 creature  **Duration** 1 hour  The target can understand |

### Query 53
- Text: What does **TELEPATHY **[two-actions] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/22', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/79', 'PZO22001 Starfinder Player Core 364-387::/page/23/Text/41']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/22', 'PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/12', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/28']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/22` | 0.701305 | **TELEPATHY **[two-actions] **SPELL 4**  **CONCENTRATE** **LINGUISTIC** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Duration** 10 minutes  You can communicate telepathically with creat |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.538818 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.538818 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` | 0.496818 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.496818 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.496818 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.496818 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/27` | 0.496818 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/57` | 0.496454 | **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/54` | 0.496454 | **EQUIPMENT** **SPELLS** |

### Query 54
- Text: Summarize with a creature, the communication is two-way. You can  communicate with only creatures that share a language  with you.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/28', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/29', 'PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/22']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/28', 'PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/22', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/28` | 1.033429 | with a creature, the communication is two-way. You can  communicate with only creatures that share a language  with you. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/29` | 0.670430 | **Heightened (6th)** You can communicate telepathically with  creatures using shared mental imagery even if you don't  share a language; *telepathy* loses the linguistic trait. |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/22` | 0.611856 | **TELEPATHY **[two-actions] **SPELL 4**  **CONCENTRATE** **LINGUISTIC** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Duration** 10 minutes  You can communicate telepathically with creat |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/35` | 0.521781 | **Success** You call the extraplanar creature and must make  your case succinctly, after which the creature can return  home at any time. |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/2` | 0.507461 | **Critical** **Success** The creature is unaffected. |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/7/Text/3` | 0.507461 | **Critical** **Success** The creature is unaffected. |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/33` | 0.504705 | You can contact and negotiate with an extraplanar creature  using a computer and the infosphere if one of the secondary  casters is using Computers for their check. Some extraplanar  creatures only an |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/50` | 0.502109 | **TRUESPEECH **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Range **touch;** Targets** 1 creature  **Duration** 1 hour  The target c |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/23` | 0.498354 | **TRANSLATE **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult **Range **30 feet;** Targets** 1 creature  **Duration** 1 hour  The target can understand |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/18/Text/30` | 0.497675 | **Success** As critical success, but the creature gains no special  insight regarding its subsequent actions. |

### Query 55
- Text: What is the rule about **Heightened (6th)** You can communicate telepathically with  creatures using shared mental imagery even if you don't  share a language; *telepathy* loses the linguistic trait.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/29', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/28', 'PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/22']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/29', 'PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/30', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/28']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/29` | 0.990852 | **Heightened (6th)** You can communicate telepathically with  creatures using shared mental imagery even if you don't  share a language; *telepathy* loses the linguistic trait. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/28` | 0.628133 | with a creature, the communication is two-way. You can  communicate with only creatures that share a language  with you. |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/22` | 0.623707 | **TELEPATHY **[two-actions] **SPELL 4**  **CONCENTRATE** **LINGUISTIC** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Duration** 10 minutes  You can communicate telepathically with creat |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/50` | 0.563287 | **TRUESPEECH **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Range **touch;** Targets** 1 creature  **Duration** 1 hour  The target c |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/30` | 0.557051 | **TELEPORT** **SPELL 6**  **UNCOMMON** **CONCENTRATE** **MANIPULATE** **TELEPORTATION**  **Traditions** arcane, occult  **Cast** 10 minutes  **Range **100 miles;** Targets** you and up to 4 targets to |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/23` | 0.548723 | **TRANSLATE **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult **Range **30 feet;** Targets** 1 creature  **Duration** 1 hour  The target can understand |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/14/Text/16` | 0.536370 | **Heightened (6th)** You can choose to have the quantum  field become greater difficult terrain, or suppress greater  difficult terrain. |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/30` | 0.530505 | **TRANSLOCATE **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **TELEPORTATION**  **Traditions** arcane, occult  **Range **120 feet  You instantly transport yourself and any items you're  w |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/6/Text/9` | 0.515517 | **Heightened (4th)** The spell affects all creatures in a 20 foot burst. Each creature must be affected by the same  emotion. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/53` | 0.506582 | **SURE FOOTING **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You free the target's li |

### Query 56
- Text: What does **TELEPORT** **SPELL 6** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/30']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/59', 'PZO22001 Starfinder Player Core 364-387::/page/9/Text/57', 'PZO22001 Starfinder Player Core 364-387::/page/21/Text/54']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/30', 'PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/41', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/41` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/59` | 0.555013 | **EQUIPMENT** **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/57` | 0.555013 | **EQUIPMENT** **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/54` | 0.555013 | **EQUIPMENT** **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/30` | 0.494288 | **TELEPORT** **SPELL 6**  **UNCOMMON** **CONCENTRATE** **MANIPULATE** **TELEPORTATION**  **Traditions** arcane, occult  **Cast** 10 minutes  **Range **100 miles;** Targets** you and up to 4 targets to |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.479374 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/27` | 0.479374 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.479374 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.479374 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.479374 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.479374 | **SPELLS** |

### Query 57
- Text: What does **TEMPORAL BULLETS **[reaction] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/41', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/79', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/72']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/41', 'PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/30', 'PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/47']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/47` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/41` | 0.638470 | **TEMPORAL BULLETS **[reaction] **SPELL 2**  **CONCENTRATE** **FORTUNE** **MANIPULATE**  **Traditions** occult  **Trigger** You fail (but not critically fail) an attack roll with a  weapon.  You rewin |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.596255 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` | 0.596255 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.554255 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.554255 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.554255 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/27` | 0.554255 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.554255 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/54` | 0.541236 | **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/59` | 0.541236 | **EQUIPMENT** **SPELLS** |

### Query 58
- Text: What does **THUNDERSTRIKE **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/47']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/47', 'PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/62', 'PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/44']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/47', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/54', 'PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/41']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/54` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/41` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/47` | 0.783194 | **THUNDERSTRIKE **[two-actions] **SPELL 1**  **CONCENTRATE** **ELECTRICITY** **MANIPULATE** **SONIC**  **Traditions** arcane, primal  **Range **120 feet; **Targets** 1 creature  **Defense** basic Refl |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/62` | 0.524414 | **SURE STRIKE **[one-action] **SPELL 1**  **CONCENTRATE** **FORTUNE**  **Traditions** arcane, occult  **Duration** until the end of your turn  A glimpse into the future ensures your next blow strikes |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/44` | 0.495632 | **TRUESIGHT **[two-actions] **SPELL 6**  **CONCENTRATE** **MANIPULATE** **REVELATION**  **Traditions** arcane, divine, occult, primal  **Duration** 10 minutes  You see things within 60 feet as they ac |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/37` | 0.464275 | **TRUE TARGET **[one-action] **SPELL 7**  **CONCENTRATE** **FORTUNE** **PREDICTION**  **Traditions** arcane, occult  **Range **60 feet;** Targets** 4 creatures  **Duration** until the start of your ne |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/68` | 0.455917 | **SYNAPTIC PULSE **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** occult **Area** 30-foot emanation **Defense** Will; **Duration** 1 round |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/41` | 0.450643 | **TEMPORAL BULLETS **[reaction] **SPELL 2**  **CONCENTRATE** **FORTUNE** **MANIPULATE**  **Traditions** occult  **Trigger** You fail (but not critically fail) an attack roll with a  weapon.  You rewin |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/12` | 0.449937 | **TELEKINETIC TANTRUM **[three-actions] **SPELL 9**  **ATTACK** **CONCENTRATE** **FORCE** **MANIPULATE**  **Traditions** arcane, occult  **Range **500 feet;** Area** 100-foot burst  **Defense** see te |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/15/Text/5` | 0.445491 | **Trigger** An enemy targets you with a Strike or spell attack. |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/13/SectionHeader/12` | 0.444932 | **ELDRITCH BOND **[two-actions] **FOCUS 1** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/39` | 0.443662 | **Cast** [two-actions] manipulate |

### Query 59
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/54']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/73', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/54', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/66']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/54', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/55', 'PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/47']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/55` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/47` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/73` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/54` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/66` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/52` | 0.838541 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/54` | 0.838541 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/49` | 0.838541 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/47` | 0.838541 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/35` | 0.838541 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/21` | 0.838541 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/69` | 0.838541 | **INTRODUCTION** |

### Query 60
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/55']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/74', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/55', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/67']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/55', 'PZO22001 Starfinder Player Core 364-387::/page/9/Text/53', 'PZO22001 Starfinder Player Core 364-387::/page/17/Text/22', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/54', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/70', 'PZO22001 Starfinder Player Core 364-387::/page/21/Text/50', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/56', 'PZO22001 Starfinder Player Core 364-387::/page/11/Text/55', 'PZO22001 Starfinder Player Core 364-387::/page/19/Text/48', 'PZO22001 Starfinder Player Core 364-387::/page/23/Text/36', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/74', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/67']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/9/Text/53` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/17/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/54` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/13/Text/70` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/21/Text/50` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/56` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/11/Text/55` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/19/Text/48` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/23/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/74` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/67` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/74` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/55` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/67` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/53` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/22` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/70` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/50` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/55` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/48` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/36` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 61
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/56']
- Expected found: `True`
- Expected rank: `9`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/75', 'PZO22001 Starfinder Player Core 364-387::/page/21/Text/51', 'PZO22001 Starfinder Player Core 364-387::/page/9/Text/54']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/56', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/68', 'PZO22001 Starfinder Player Core 364-387::/page/21/Text/51', 'PZO22001 Starfinder Player Core 364-387::/page/23/Text/37', 'PZO22001 Starfinder Player Core 364-387::/page/11/Text/56', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/75', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/71', 'PZO22001 Starfinder Player Core 364-387::/page/9/Text/54', 'PZO22001 Starfinder Player Core 364-387::/page/19/Text/49', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/57', 'PZO22001 Starfinder Player Core 364-387::/page/17/Text/23', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/55']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/68` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/21/Text/51` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/23/Text/37` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/11/Text/56` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/75` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/13/Text/71` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/9/Text/54` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/19/Text/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/57` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/17/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/55` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/75` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/54` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/51` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/68` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/49` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/23` | 0.910061 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/71` | 0.910061 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/56` | 0.910061 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/56` | 0.910061 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/37` | 0.910061 | **CLASSES** |

### Query 62
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/57']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/17/Text/24', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/57', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/69']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/57', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/56', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/58']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/56` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/58` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/24` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/57` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/69` | 0.864442 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/72` | 0.822442 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/55` | 0.822442 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/57` | 0.822442 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/52` | 0.822442 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/50` | 0.822442 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/38` | 0.822442 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/76` | 0.822442 | **SKILLS** |

### Query 63
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/58']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/77', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/58', 'PZO22001 Starfinder Player Core 364-387::/page/19/Text/51']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/58', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/57', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/59']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/57` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/59` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/77` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/58` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/51` | 0.871817 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/39` | 0.829817 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/56` | 0.829817 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/70` | 0.829817 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/73` | 0.829817 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/53` | 0.829817 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/25` | 0.829817 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/58` | 0.829817 | **FEATS** |

### Query 64
- Text: What is the rule about **EQUIPMENT** **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/59']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/59', 'PZO22001 Starfinder Player Core 364-387::/page/21/Text/54', 'PZO22001 Starfinder Player Core 364-387::/page/9/Text/57']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/59', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/60', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/58']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/60` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/58` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/59` | 0.887907 | **EQUIPMENT** **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/54` | 0.887907 | **EQUIPMENT** **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/57` | 0.887907 | **EQUIPMENT** **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.697854 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` | 0.697854 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/27` | 0.697854 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.697854 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.697854 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.697854 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.697854 | **SPELLS** |

### Query 65
- Text: What is the rule about **Spell Lists**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/60']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/80', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/60', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/73']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/60', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/61', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/59']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/61` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/59` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/80` | 0.890837 | **Spell Lists** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/60` | 0.890837 | **Spell Lists** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/73` | 0.890837 | **Spell Lists** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/55` | 0.848837 | **Spell Lists** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/58` | 0.848837 | **Spell Lists** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/76` | 0.848837 | **Spell Lists** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/54` | 0.848837 | **Spell Lists** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/42` | 0.848837 | **Spell Lists** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/28` | 0.848837 | **Spell Lists** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/61` | 0.848837 | **Spell Lists** |

### Query 66
- Text: What is the rule about **Spells**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/61']
- Expected found: `True`
- Expected rank: `9`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/23/Text/43', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/77', 'PZO22001 Starfinder Player Core 364-387::/page/19/Text/55']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/61', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/60', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/62']
- Expanded expected found: `True`
- Expanded expected rank: `9`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/60` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/62` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/43` | 0.798799 | **Spells** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/77` | 0.798799 | **Spells** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/55` | 0.798799 | **Spells** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/62` | 0.756799 | **Spells** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/29` | 0.756799 | **Spells** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/81` | 0.756799 | **Spells** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/74` | 0.756799 | **Spells** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/59` | 0.756799 | **Spells** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/61` | 0.756799 | **Spells** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/56` | 0.756799 | **Spells** |

### Query 67
- Text: What is the rule about **Focus Spells**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/62']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/11/Text/63', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/78', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/82']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/62', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/61', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/63']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/61` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/63` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/63` | 0.926221 | **Focus Spells** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/78` | 0.926221 | **Focus Spells** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/82` | 0.926221 | **Focus Spells** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/56` | 0.884221 | **Focus Spells** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/44` | 0.884221 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/62` | 0.884221 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/30` | 0.884221 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/75` | 0.884221 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/60` | 0.884221 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/57` | 0.884221 | **Focus Spells** |

### Query 68
- Text: Summarize **Rituals**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/63']
- Expected found: `True`
- Expected rank: `9`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/13/Text/79', 'PZO22001 Starfinder Player Core 364-387::/page/23/Text/45', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/76']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/63', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/62', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/64']
- Expanded expected found: `True`
- Expanded expected rank: `9`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/62` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/64` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/79` | 0.971114 | **Rituals** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/45` | 0.971114 | **Rituals** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/76` | 0.971114 | **Rituals** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/31` | 0.929114 | **Rituals** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/61` | 0.929114 | **Rituals** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/57` | 0.929114 | **Rituals** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/83` | 0.929114 | **Rituals** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/64` | 0.929114 | **Rituals** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/63` | 0.929114 | **Rituals** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/58` | 0.929114 | **Rituals** |

### Query 69
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/64']
- Expected found: `True`
- Expected rank: `9`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/23/Text/46', 'PZO22001 Starfinder Player Core 364-387::/page/19/Text/58', 'PZO22001 Starfinder Player Core 364-387::/page/11/Text/65']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/64', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/65', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/63']
- Expanded expected found: `True`
- Expanded expected rank: `9`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/65` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/63` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/46` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/58` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/65` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/84` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/77` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/32` | 0.923000 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/62` | 0.923000 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/80` | 0.923000 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/64` | 0.923000 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/59` | 0.923000 | **PLAYING THE ** **GAME** |

### Query 70
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/65']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/85', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/65', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/81']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/65', 'PZO22001 Starfinder Player Core 364-387::/page/21/Text/60', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/66', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/78', 'PZO22001 Starfinder Player Core 364-387::/page/23/Text/47', 'PZO22001 Starfinder Player Core 364-387::/page/19/Text/59', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/81', 'PZO22001 Starfinder Player Core 364-387::/page/17/Text/33', 'PZO22001 Starfinder Player Core 364-387::/page/11/Text/66', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/85', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/64', 'PZO22001 Starfinder Player Core 364-387::/page/9/Text/63']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/21/Text/60` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/66` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/78` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/23/Text/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/19/Text/59` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/13/Text/81` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/17/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/11/Text/66` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/85` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/64` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/9/Text/63` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/85` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/65` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/81` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/66` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/63` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/60` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/59` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/33` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/47` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/78` | 0.645203 | **CONDITIONS ** |

### Query 71
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/66']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/23/Text/48', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/86', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/66']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/3/Text/66', 'PZO22001 Starfinder Player Core 364-387::/page/4/Text/1', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/65']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/4/Text/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/65` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/48` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/86` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/66` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/61` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/64` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/82` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/67` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/60` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/34` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/79` | 0.697531 | **APPENDIX** **GLOSSARY & ** |

### Query 72
- Text: What is the rule about You call down a tendril of lightning that cracks with thunder,  dealing 1d12 electricity damage and 1d4 sonic damage to  the target with a basic Reflex save. A target wearing metal  armor or made of metal takes a –1 circumstance bonus to its  save, and if damaged by the spell is clumsy 1 for 1 round.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/4/Text/1', 'PZO22001 Starfinder Player Core 364-387::/page/11/Text/34', 'PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/47']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/Text/1', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/66', 'PZO22001 Starfinder Player Core 364-387::/page/4/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/66` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/4/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/4/Text/1` | 0.965333 | You call down a tendril of lightning that cracks with thunder,  dealing 1d12 electricity damage and 1d4 sonic damage to  the target with a basic Reflex save. A target wearing metal  armor or made of m |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/34` | 0.570950 | The weapon has one fewer upgrade slot but can be  upgraded with any upgrades you hold in your hands as a  locus when casting this spell, which become inert until the  spell ends. The weapon deals dama |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/47` | 0.558923 | **THUNDERSTRIKE **[two-actions] **SPELL 1**  **CONCENTRATE** **ELECTRICITY** **MANIPULATE** **SONIC**  **Traditions** arcane, primal  **Range **120 feet; **Targets** 1 creature  **Defense** basic Refl |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/10/Text/28` | 0.511613 | **Success** For 1 round, the creature can't use reactions and  must attempt another save at the start of its turn; on a  failure, it is slowed 1 for that turn as it sobs uncontrollably. |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/10/SectionHeader/32` | 0.499957 | **WAVE OF WARNING **[two-actions] **SPELL 5**  **CONCENTRATE** **EMOTION** **FEAR** **MANIPULATE** **MENTAL** **NONLETHAL**  **Traditions** divine, primal  **Range **120 feet; **Targets **1 creature, |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/6` | 0.499029 | You infuse the target's essence with healing energy. If the  target is a willing creature, you restore 1d6 Hit Points.  The target is then temporarily immune for 10 minutes.  The number of actions you |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/4/Text/2` | 0.497349 | **Heightened (+1)** The damage increases by 1d12 electricity  and 1d4 sonic. |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/8` | 0.493838 | **Success** The target resists the spell before it's completely  swallowed up, but shadowy tendrils cling to it, making  the target slowed 1 for 1 round. |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/52` | 0.492883 | **VERDANT CODE **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **PLANT** **WOOD**  **Traditions** arcane, primal  **Range **30 feet;** Targets** 1 unattended object with the tech trait  ** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/14/ListItem/29` | 0.491606 | 4 **Eldritch Storm:** A howling tempest of psychic  energy deals 4d12 sonic damage and 1d6 persistent  mental damage. On a critical failure, creatures take  double damage and are confused for 1 round. |

### Query 73
- Text: What is the rule about **Heightened (+1)** The damage increases by 1d12 electricity  and 1d4 sonic.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/4/Text/2', 'PZO22001 Starfinder Player Core 364-387::/page/14/Text/23', 'PZO22001 Starfinder Player Core 364-387::/page/15/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/Text/2', 'PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/3', 'PZO22001 Starfinder Player Core 364-387::/page/4/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/4/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/4/Text/2` | 0.927881 | **Heightened (+1)** The damage increases by 1d12 electricity  and 1d4 sonic. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/14/Text/23` | 0.802023 | **Heightened (+1)** Damage increases by 1d12, persistent  damage increases by 1d6. |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/15/Text/19` | 0.738300 | **Heightened (+1)** The damage increases by 2d8. |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/52` | 0.694791 | **Heightened** **(+1) **The damage increases by 2d6. |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/4/Text/14` | 0.690426 | **Heightened (+1)** The damage increases by 2d6. |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/45` | 0.683182 | **Heightened (+1)** The fire damage increases by 1d10, and the  vitality damage against undead increases by 1d10. |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/55` | 0.677490 | **Heightened (+1)** The cold damage increases by 1d10. |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/7/Text/7` | 0.645188 | **Heightened (+1)** Increase the initial void damage by 2d10.  The persistent void damage increases by 1d6 on a  failure, or by 2d6 on critical failure. |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/16/Text/12` | 0.632484 | **Heightened (+2)** Increase the damage by 1d10 and the  temporary Hit Points by 5. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/10` | 0.629855 | **Heightened (+1)** The amount of healing increases by 1d6,  and the extra healing for the 2-action version increases  by 6. |

### Query 74
- Text: What does **TIME'S EDGE **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/3', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/72', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/75']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/3', 'PZO22001 Starfinder Player Core 364-387::/page/4/Text/2', 'PZO22001 Starfinder Player Core 364-387::/page/4/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/4/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/4/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/3` | 0.684349 | **TIME'S EDGE **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** occult, primal  **Area** 60-foot line  **Defense** Fortitude  You refract latent energy from the Dimension of |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` | 0.559414 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.559414 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.517414 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.517414 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.517414 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.517414 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/27` | 0.517414 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/59` | 0.503288 | **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/54` | 0.503288 | **EQUIPMENT** **SPELLS** |

### Query 75
- Text: Summarize **Critical Success** The creature is unaffected.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/Text/10']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/10/Text/27', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/40', 'PZO22001 Starfinder Player Core 364-387::/page/16/Text/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/Text/10', 'PZO22001 Starfinder Player Core 364-387::/page/4/Text/11', 'PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/3']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/4/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/10/Text/27` | 1.018921 | **Critical Success** The creature is unaffected. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/40` | 1.018921 | **Critical Success** The creature is unaffected. |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/16/Text/23` | 1.018921 | **Critical Success** The creature is unaffected. |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/4/Text/10` | 0.976921 | **Critical Success** The creature is unaffected. |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/2/Text/2` | 0.976921 | **Critical Success** The creature is unaffected. |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/12` | 0.976921 | **Critical Success** The creature is unaffected. |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/2` | 0.960064 | **Critical** **Success** The creature is unaffected. |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/7/Text/3` | 0.960064 | **Critical** **Success** The creature is unaffected. |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/6/Text/18` | 0.887048 | **Success** The creature is unaffected. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/7` | 0.770139 | **Critical** **Success** The target is unaffected. |

### Query 76
- Text: What is the rule about **Success** The creature takes half damage.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/Text/11']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/41', 'PZO22001 Starfinder Player Core 364-387::/page/7/Text/4', 'PZO22001 Starfinder Player Core 364-387::/page/4/Text/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/Text/11', 'PZO22001 Starfinder Player Core 364-387::/page/4/Text/12', 'PZO22001 Starfinder Player Core 364-387::/page/4/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/4/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/4/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/41` | 0.837732 | **Success** The creature takes half damage. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/7/Text/4` | 0.837732 | **Success** The creature takes half damage. |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/4/Text/11` | 0.837732 | **Success** The creature takes half damage. |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/13` | 0.704717 | **Success** The creature takes full damage. |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/42` | 0.683437 | **Failure** The creature takes full damage. |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/16/Text/9` | 0.681856 | **Success** The target takes half damage. |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/63` | 0.681856 | **Success** The target takes half damage. |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/23` | 0.617611 | **Success** The target takes half damage and is stupefied 1  until the end of your current turn. |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/7/Text/3` | 0.614927 | **Critical** **Success** The creature is unaffected. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/4/Text/12` | 0.608888 | **Failure** The creature takes full damage and is sickened 1. |

### Query 77
- Text: What is the rule about **Failure** The creature takes full damage and is sickened 1.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/4/Text/12', 'PZO22001 Starfinder Player Core 364-387::/page/12/Text/64', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/42']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/Text/12', 'PZO22001 Starfinder Player Core 364-387::/page/4/Text/11', 'PZO22001 Starfinder Player Core 364-387::/page/4/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/4/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/4/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/4/Text/12` | 0.911692 | **Failure** The creature takes full damage and is sickened 1. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/64` | 0.795375 | **Failure** The target takes full damage and is sickened 1. |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/42` | 0.793384 | **Failure** The creature takes full damage. |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/4/Text/13` | 0.746510 | **Critical Failure** The creature takes double damage and is  sickened 2. |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/65` | 0.664689 | **Critical** **Failure** The target takes double damage and is  sickened 2. |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/14` | 0.663292 | **Failure** The creature takes full damage and is drained 1d4. **Critical Failure** The creature takes double damage and is  drained 4. |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/7/Text/5` | 0.661822 | **Failure** The creature takes full damage and 1d6 persistent  void damage, and becomes drained 1. |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/16/Text/25` | 0.629773 | **Failure** The creature is stunned 2. |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/43` | 0.628536 | **Critical Failure** The creature takes full damage and becomes  blinded permanently. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/6/Text/19` | 0.614633 | **Failure** The creature is blinded by the pattern. If it exits  the pattern, it can attempt a new save to recover from  the blinded condition at the end of each of its turns, to  a maximum duration o |

### Query 78
- Text: What is the rule about **Critical Failure** The creature takes double damage and is  sickened 2.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/4/Text/13', 'PZO22001 Starfinder Player Core 364-387::/page/12/Text/65', 'PZO22001 Starfinder Player Core 364-387::/page/4/Text/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/Text/13', 'PZO22001 Starfinder Player Core 364-387::/page/4/Text/12', 'PZO22001 Starfinder Player Core 364-387::/page/4/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/4/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/4/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/4/Text/13` | 0.910414 | **Critical Failure** The creature takes double damage and is  sickened 2. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/65` | 0.826698 | **Critical** **Failure** The target takes double damage and is  sickened 2. |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/4/Text/12` | 0.775525 | **Failure** The creature takes full damage and is sickened 1. |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/14` | 0.730749 | **Failure** The creature takes full damage and is drained 1d4. **Critical Failure** The creature takes double damage and is  drained 4. |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/7/Text/6` | 0.704458 | **Critical Failure** The creature takes double damage and 2d6  persistent void damage, and becomes drained 2. |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/64` | 0.651341 | **Failure** The target takes full damage and is sickened 1. |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/43` | 0.650121 | **Critical Failure** The creature takes full damage and becomes  blinded permanently. |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/41` | 0.648646 | **Critical Failure** As failure, and the creature is  pushed 10 feet away from the wall. |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/10/Text/30` | 0.646596 | **Critical Failure** As failure, and the creature is automatically  slowed 1 for 1 minute. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/24` | 0.645013 | **Failure** The target takes full damage and is stupefied 1 until the  end of your next turn. You Recall Knowledge about the target. **Critical** **Failure** As failure, except the target takes double |

### Query 79
- Text: What is the rule about **Heightened (+1)** The damage increases by 2d6.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/Text/14']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/11/Text/52', 'PZO22001 Starfinder Player Core 364-387::/page/4/Text/14', 'PZO22001 Starfinder Player Core 364-387::/page/15/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/Text/14', 'PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/15', 'PZO22001 Starfinder Player Core 364-387::/page/4/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/4/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/52` | 0.912625 | **Heightened** **(+1) **The damage increases by 2d6. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/4/Text/14` | 0.908182 | **Heightened (+1)** The damage increases by 2d6. |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/15/Text/19` | 0.855181 | **Heightened (+1)** The damage increases by 2d8. |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/14/Text/23` | 0.759104 | **Heightened (+1)** Damage increases by 1d12, persistent  damage increases by 1d6. |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/26` | 0.747373 | **Heightened (+1)** The mental damage increases by 2d6. |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/66` | 0.745555 | **Heightened (+1)** The cold damage increases by 2d6. |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/10` | 0.707366 | **Heightened (+1)** The amount of healing increases by 1d6,  and the extra healing for the 2-action version increases  by 6. |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/7/Text/7` | 0.701095 | **Heightened (+1)** Increase the initial void damage by 2d10.  The persistent void damage increases by 1d6 on a  failure, or by 2d6 on critical failure. |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/27` | 0.695872 | **Heightened (6th)** Increase the number of targets to 5 targets.  The damage dealt by the attacks increases to 3 dice. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/53` | 0.695872 | **Heightened (6th)** Increase the number of targets to 5  targets. The damage dealt by the attacks increases to  3 dice. |

### Query 80
- Text: What does **TOXIC CLOUD **[three-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/15', 'PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/68', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/79']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/15', 'PZO22001 Starfinder Player Core 364-387::/page/4/Text/14', 'PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/4/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/15` | 0.660149 | **TOXIC CLOUD **[three-actions] **SPELL 5**  **CONCENTRATE** **DEATH** **MANIPULATE** **POISON**  **Traditions** arcane, primal  **Range **120 feet;** Area** 20-foot burst  **Defense** basic Fortitude |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/68` | 0.474364 | **SYNAPTIC PULSE **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** occult **Area** 30-foot emanation **Defense** Will; **Duration** 1 round |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.471941 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.429941 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.429941 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.429941 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.429941 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/27` | 0.429941 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` | 0.429941 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/57` | 0.424428 | **EQUIPMENT** **SPELLS** |

### Query 81
- Text: What does **TRANSLATE **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/23', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/79', 'PZO22001 Starfinder Player Core 364-387::/page/11/Text/60']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/23', 'PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/30', 'PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/23` | 0.630204 | **TRANSLATE **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult **Range **30 feet;** Targets** 1 creature  **Duration** 1 hour  The target can understand |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.590846 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.590846 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` | 0.548846 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.548846 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.548846 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.548846 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/27` | 0.548846 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/57` | 0.504989 | **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/54` | 0.504989 | **EQUIPMENT** **SPELLS** |

### Query 82
- Text: What does **TRANSLOCATE **[two-actions] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/30', 'PZO22001 Starfinder Player Core 364-387::/page/16/SectionHeader/13', 'PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/30', 'PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/37', 'PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/37` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/30` | 0.572850 | **TRANSLOCATE **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **TELEPORTATION**  **Traditions** arcane, occult  **Range **120 feet  You instantly transport yourself and any items you're  w |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/16/SectionHeader/13` | 0.557640 | **ACCELERATE **[two-actions] **FOCUS 4** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/23` | 0.547268 | **TRANSLATE **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult **Range **30 feet;** Targets** 1 creature  **Duration** 1 hour  The target can understand |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/15/Text/12` | 0.498276 | **FORGET **[two-actions] **FOCUS 4** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` | 0.482373 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.482373 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.482373 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.482373 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.482373 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.482373 | **SPELLS** |

### Query 83
- Text: What does **TRUE TARGET **[one-action] **SPELL 7** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/37', 'PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/50', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/79']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/37', 'PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/30', 'PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/44']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/44` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/37` | 0.710453 | **TRUE TARGET **[one-action] **SPELL 7**  **CONCENTRATE** **FORTUNE** **PREDICTION**  **Traditions** arcane, occult  **Range **60 feet;** Targets** 4 creatures  **Duration** until the start of your ne |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/50` | 0.564246 | **TRUESPEECH **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Range **touch;** Targets** 1 creature  **Duration** 1 hour  The target c |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.520311 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` | 0.478311 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.478311 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/27` | 0.478311 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.478311 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.478311 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.478311 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/44` | 0.476879 | **TRUESIGHT **[two-actions] **SPELL 6**  **CONCENTRATE** **MANIPULATE** **REVELATION**  **Traditions** arcane, divine, occult, primal  **Duration** 10 minutes  You see things within 60 feet as they ac |

### Query 84
- Text: What does **TRUESIGHT **[two-actions] **SPELL 6** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/44', 'PZO22001 Starfinder Player Core 364-387::/page/12/SectionHeader/39', 'PZO22001 Starfinder Player Core 364-387::/page/11/SectionHeader/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/44', 'PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/37', 'PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/50']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/37` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/50` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/44` | 0.686351 | **TRUESIGHT **[two-actions] **SPELL 6**  **CONCENTRATE** **MANIPULATE** **REVELATION**  **Traditions** arcane, divine, occult, primal  **Duration** 10 minutes  You see things within 60 feet as they ac |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/12/SectionHeader/39` | 0.534927 | **REMIX **[two-actions] **FOCUS 6** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/11/SectionHeader/16` | 0.529588 | **DATA DRAIN **[two-actions] **FOCUS 6** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/50` | 0.490133 | **TRUESPEECH **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Range **touch;** Targets** 1 creature  **Duration** 1 hour  The target c |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/37` | 0.487655 | **TRUE TARGET **[one-action] **SPELL 7**  **CONCENTRATE** **FORTUNE** **PREDICTION**  **Traditions** arcane, occult  **Range **60 feet;** Targets** 4 creatures  **Duration** until the start of your ne |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/16/SectionHeader/18` | 0.484769 | **TIME LOOP **[two-actions] **FOCUS 6** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/13/SectionHeader/1` | 0.475310 | **SHADOW PRISON **[two-actions] **FOCUS 6** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/15/SectionHeader/20` | 0.472461 | **REALITY WIPE **[two-actions] **FOCUS 6** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/14/SectionHeader/32` | 0.469769 | **PARALLEL FORMS **[two-actions] **FOCUS 6** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/11/SectionHeader/46` | 0.461414 | **ELEMENTAL NOVA **[two-actions] **FOCUS 6** |

### Query 85
- Text: What does **TRUESPEECH **[two-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/50']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/50', 'PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/44', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/72']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/50', 'PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/44', 'PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/58']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/44` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/58` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/50` | 0.642122 | **TRUESPEECH **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Range **touch;** Targets** 1 creature  **Duration** 1 hour  The target c |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/44` | 0.533030 | **TRUESIGHT **[two-actions] **SPELL 6**  **CONCENTRATE** **MANIPULATE** **REVELATION**  **Traditions** arcane, divine, occult, primal  **Duration** 10 minutes  You see things within 60 feet as they ac |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` | 0.531311 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.489311 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/27` | 0.489311 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.489311 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.489311 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.489311 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.489311 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/54` | 0.487294 | **EQUIPMENT** **SPELLS** |

### Query 86
- Text: What does **UNCONTROLLABLE DANCE **[two-actions] **SPELL 8** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/58']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/58', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/72', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/79']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/58', 'PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/0', 'PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/50']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/0` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/50` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/58` | 0.807787 | **UNCONTROLLABLE DANCE **[two-actions] **SPELL 8**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **touch;** Targets** 1 creature **Defense** Will |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` | 0.536504 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.536504 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.494504 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/27` | 0.494504 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.494504 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.494504 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.494504 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/39` | 0.482809 | **Cast** [two-actions] manipulate |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/5` | 0.481955 | **UNFETTERED MOVEMENT **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, primal  **Range **touch;** Targets** 1 creature touched  **Duration** 10 minutes  You |

### Query 87
- Text: Summarize 7 PLAYER CORE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/0']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/0', 'PZO22001 Starfinder Player Core 364-387::/page/23/SectionHeader/0', 'PZO22001 Starfinder Player Core 364-387::/page/19/SectionHeader/0']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/0', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/1', 'PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/58']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/58` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/0` | 0.997217 | 7 PLAYER CORE |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/23/SectionHeader/0` | 0.997217 | 7 PLAYER CORE |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/19/SectionHeader/0` | 0.997217 | 7 PLAYER CORE |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/507` | 0.482795 | 7 |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/499` | 0.482795 | 7 |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/442` | 0.482795 | 7 |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/444` | 0.482795 | 7 |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/504` | 0.482795 | 7 |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/494` | 0.482795 | 7 |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/500` | 0.363250 | 7th |

### Query 88
- Text: What is the rule about can't use reactions. It also can't use move actions except to  dance, using the Stride action to move up to half its Speed. **Critical Success** The target is unaffected.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/1', 'PZO22001 Starfinder Player Core 364-387::/page/12/Text/62', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/1', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/2', 'PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/0']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/0` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/1` | 0.961017 | can't use reactions. It also can't use move actions except to  dance, using the Stride action to move up to half its Speed. **Critical Success** The target is unaffected. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/62` | 0.615996 | **Critical** **Success** The target is unaffected. |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/7` | 0.615996 | **Critical** **Success** The target is unaffected. |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/22` | 0.573996 | **Critical** **Success** The target is unaffected. |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/5` | 0.559541 | **UNFETTERED MOVEMENT **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, primal  **Range **touch;** Targets** 1 creature touched  **Duration** 10 minutes  You |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/16/Text/8` | 0.550029 | **Critical Success** The target is unaffected. |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/10/Text/28` | 0.512123 | **Success** For 1 round, the creature can't use reactions and  must attempt another save at the start of its turn; on a  failure, it is slowed 1 for that turn as it sobs uncontrollably. |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/6` | 0.512120 | **Joy** The target can't take any hostile actions. |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/4` | 0.502646 | **Critical Failure** The spell's duration is 1 minute, and the target  must spend all its actions each turn dancing. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/58` | 0.498769 | **UNCONTROLLABLE DANCE **[two-actions] **SPELL 8**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **touch;** Targets** 1 creature **Defense** Will |

### Query 89
- Text: What is the rule about **Success** The spell's duration is 3 rounds, and the target must?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/2', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/3', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/2', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/1', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/83']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/83` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/2` | 0.869941 | **Success** The spell's duration is 3 rounds, and the target must |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/3` | 0.668033 | **Failure** The spell's duration is 1 minute, and the target must  spend at least 2 actions each turn dancing. |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/4` | 0.636128 | **Critical Failure** The spell's duration is 1 minute, and the target  must spend all its actions each turn dancing. |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/10/Text/28` | 0.580530 | **Success** For 1 round, the creature can't use reactions and  must attempt another save at the start of its turn; on a  failure, it is slowed 1 for that turn as it sobs uncontrollably. |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/1` | 0.579515 | **SUGGESTION **[two-actions] **SPELL 4**  **CONCENTRATE** **INCAPACITATION** **LINGUISTIC** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creatu |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/4` | 0.568656 | **Failure** The target begins to wander aimlessly, using each  action to Step in a random direction. When it moves,  the target takes the safest route and doesn't enter  hazardous terrain. The spell h |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/14` | 0.564799 | **Critical Success** You resurrect the target. They return to life  with full Hit Points and the same spells prepared and points  in their pools they had when they died, and still suffering  from any |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/15` | 0.548347 | **Success** As critical success, except the target returns to life  with 1 Hit Point and no spells prepared or points in any  pools, and still is affected by any long-term debilitations  of the old bo |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/7` | 0.544301 | **Critical** **Success** The target is unaffected. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/22` | 0.544301 | **Critical** **Success** The target is unaffected. |

### Query 90
- Text: What is the rule about spend at least 1 action each turn dancing.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/83']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/83', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/3', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/83', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/2', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/83` | 0.887556 | spend at least 1 action each turn dancing. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/3` | 0.677345 | **Failure** The spell's duration is 1 minute, and the target must  spend at least 2 actions each turn dancing. |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/4` | 0.654077 | **Critical Failure** The spell's duration is 1 minute, and the target  must spend all its actions each turn dancing. |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/6/Text/17` | 0.422436 | In addition, a creature must attempt a Will saving  throw if it's inside the pattern when you cast it, enters the  pattern, ends its turn within the pattern, or uses a Seek or  Interact action on the |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/14/Text/35` | 0.421656 | You split yourself into two versions with different fates.  Each version of you Strides from your current space, then  takes a single action. If the actions are both attacks, they  must target a diffe |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/58` | 0.417318 | **UNCONTROLLABLE DANCE **[two-actions] **SPELL 8**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **touch;** Targets** 1 creature **Defense** Will |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/62` | 0.416037 | **SURE STRIKE **[one-action] **SPELL 1**  **CONCENTRATE** **FORTUNE**  **Traditions** arcane, occult  **Duration** until the end of your turn  A glimpse into the future ensures your next blow strikes |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/10/Text/28` | 0.402116 | **Success** For 1 round, the creature can't use reactions and  must attempt another save at the start of its turn; on a  failure, it is slowed 1 for that turn as it sobs uncontrollably. |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/1` | 0.395485 | can't use reactions. It also can't use move actions except to  dance, using the Stride action to move up to half its Speed. **Critical Success** The target is unaffected. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/37` | 0.391765 | **TRUE TARGET **[one-action] **SPELL 7**  **CONCENTRATE** **FORTUNE** **PREDICTION**  **Traditions** arcane, occult  **Range **60 feet;** Targets** 4 creatures  **Duration** until the start of your ne |

### Query 91
- Text: What is the rule about **Failure** The spell's duration is 1 minute, and the target must  spend at least 2 actions each turn dancing.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/3', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/4', 'PZO22001 Starfinder Player Core 364-387::/page/8/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/3', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/83', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/83` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/3` | 0.956552 | **Failure** The spell's duration is 1 minute, and the target must  spend at least 2 actions each turn dancing. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/4` | 0.896391 | **Critical Failure** The spell's duration is 1 minute, and the target  must spend all its actions each turn dancing. |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/4` | 0.734964 | **Failure** The target begins to wander aimlessly, using each  action to Step in a random direction. When it moves,  the target takes the safest route and doesn't enter  hazardous terrain. The spell h |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/10/Text/29` | 0.667523 | **Failure** As success, but the duration is 1 minute. |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/5` | 0.643528 | **Critical Failure** As failure, except the target babbles  incoherently. Any creature that begins its turn within  20 feet of the target must attempt a Will saving throw.  On a failure, it must use i |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/6/Text/19` | 0.636791 | **Failure** The creature is blinded by the pattern. If it exits  the pattern, it can attempt a new save to recover from  the blinded condition at the end of each of its turns, to  a maximum duration o |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/24` | 0.611922 | **Failure** The target takes full damage and is stupefied 1 until the  end of your next turn. You Recall Knowledge about the target. **Critical** **Failure** As failure, except the target takes double |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/9` | 0.598816 | **Failure** The target is swallowed by its own shadow until the  beginning of your next turn. The target is invisible and  paralyzed, cannot experience or interact with the outside  world, and cannot |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/83` | 0.596453 | spend at least 1 action each turn dancing. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/20` | 0.594257 | **Failure** You fail to awaken the target. |

### Query 92
- Text: What is the rule about **Critical Failure** The spell's duration is 1 minute, and the target  must spend all its actions each turn dancing.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/4', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/3', 'PZO22001 Starfinder Player Core 364-387::/page/8/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/4', 'PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/5', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/4` | 0.963715 | **Critical Failure** The spell's duration is 1 minute, and the target  must spend all its actions each turn dancing. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/3` | 0.870642 | **Failure** The spell's duration is 1 minute, and the target must  spend at least 2 actions each turn dancing. |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/5` | 0.769148 | **Critical Failure** As failure, except the target babbles  incoherently. Any creature that begins its turn within  20 feet of the target must attempt a Will saving throw.  On a failure, it must use i |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/10/Text/30` | 0.657595 | **Critical Failure** As failure, and the creature is automatically  slowed 1 for 1 minute. |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/4` | 0.650161 | **Failure** The target begins to wander aimlessly, using each  action to Step in a random direction. When it moves,  the target takes the safest route and doesn't enter  hazardous terrain. The spell h |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/10` | 0.640505 | **Critical Failure** As failure, except the target is swallowed  for 1 minute. |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/24` | 0.635769 | **Failure** The target takes full damage and is stupefied 1 until the  end of your next turn. You Recall Knowledge about the target. **Critical** **Failure** As failure, except the target takes double |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/15/Text/11` | 0.635405 | **Critical Failure** The triggering attack misses. You are  undetected to that creature for 1 minute. If you use a  hostile action, this effect ends after that hostile action  is completed. |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/18/Text/9` | 0.599671 | **Critical Failure** As failure, and you reduce the degree of  success of the primary skill check by one step. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/10/Text/29` | 0.584366 | **Failure** As success, but the duration is 1 minute. |

### Query 93
- Text: What does **UNFETTERED MOVEMENT **[two-actions] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/5', 'PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/12', 'PZO22001 Starfinder Player Core 364-387::/page/16/SectionHeader/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/5', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/4', 'PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/5` | 0.688238 | **UNFETTERED MOVEMENT **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, primal  **Range **touch;** Targets** 1 creature touched  **Duration** 10 minutes  You |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/12` | 0.573668 | **UNFETTERED PACK **[two-actions] **SPELL 7**  **CONCENTRATE** **MANIPULATE**  **Traditions** primal  **Range **30 feet; **Targets** up to 10 creatures  **Duration** 1 hour  You free those who travel |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/16/SectionHeader/13` | 0.564914 | **ACCELERATE **[two-actions] **FOCUS 4** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/15/Text/12` | 0.515898 | **FORGET **[two-actions] **FOCUS 4** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.494478 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/27` | 0.494478 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.494478 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.494478 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.494478 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.494478 | **SPELLS** |

### Query 94
- Text: What does **UNFETTERED PACK **[two-actions] **SPELL 7** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/12', 'PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/5', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/75']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/12', 'PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/5', 'PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/12` | 0.632568 | **UNFETTERED PACK **[two-actions] **SPELL 7**  **CONCENTRATE** **MANIPULATE**  **Traditions** primal  **Range **30 feet; **Targets** up to 10 creatures  **Duration** 1 hour  You free those who travel |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/5` | 0.548166 | **UNFETTERED MOVEMENT **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, primal  **Range **touch;** Targets** 1 creature touched  **Duration** 10 minutes  You |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.519200 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/27` | 0.477200 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.477200 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` | 0.477200 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.477200 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.477200 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.477200 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/59` | 0.469541 | **EQUIPMENT** **SPELLS** |

### Query 95
- Text: What does **VAMPIRIC EXSANGUINATION **[two-actions] **SPELL 6** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/20', 'PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/29', 'PZO22001 Starfinder Player Core 364-387::/page/6/SectionHeader/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/20', 'PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/29', 'PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/20` | 0.656285 | **VAMPIRIC EXSANGUINATION **[two-actions] **SPELL 6**  **CONCENTRATE** **DEATH** **MANIPULATE** **VOID**  **Traditions** arcane, divine, occult  **Area** 30-foot cone  **Defense** basic Fortitude  You |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/29` | 0.535678 | **VAMPIRIC FEAST **[two-actions] **SPELL 3**  **CONCENTRATE** **DEATH** **MANIPULATE** **VOID**  **Traditions** arcane, divine, occult **Range **touch;** Targets** 1 living creature  **Defense** basic |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/6/SectionHeader/10` | 0.528206 | **VIBRANT PATTERN **[two-actions] **SPELL 6**  **ILLUSION** **INCAPACITATION** **MANIPULATE** **SUBTLE** **VISUAL**  **Traditions** arcane, occult  **Range **120 feet; **Area** 10-foot burst  **Defens |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/11/SectionHeader/46` | 0.481158 | **ELEMENTAL NOVA **[two-actions] **FOCUS 6** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/12/SectionHeader/39` | 0.479649 | **REMIX **[two-actions] **FOCUS 6** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/14/SectionHeader/32` | 0.476510 | **PARALLEL FORMS **[two-actions] **FOCUS 6** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/13/SectionHeader/1` | 0.466107 | **SHADOW PRISON **[two-actions] **FOCUS 6** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/11/SectionHeader/16` | 0.462799 | **DATA DRAIN **[two-actions] **FOCUS 6** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/3/SectionHeader/5` | 0.462539 | **TELEKINETIC STRANGULATION **[two-actions] **SPELL 6**  **ATTACK** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** divine, occult  **Range **30 feet;** Targets** 1 creature  **Defen |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/68` | 0.460299 | **SYNAPTIC PULSE **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** occult **Area** 30-foot emanation **Defense** Will; **Duration** 1 round |

### Query 96
- Text: What does **VAMPIRIC FEAST **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/29', 'PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/37', 'PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/59']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/29', 'PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/37', 'PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/37` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/29` | 0.719647 | **VAMPIRIC FEAST **[two-actions] **SPELL 3**  **CONCENTRATE** **DEATH** **MANIPULATE** **VOID**  **Traditions** arcane, divine, occult **Range **touch;** Targets** 1 living creature  **Defense** basic |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/37` | 0.544634 | **VAPOR FORM **[two-actions] **SPELL 4**  **AIR** **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, occult, primal  **Range **touch;** Targets** 1 willing creature  **Duration** 5 m |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/59` | 0.528170 | **VIBE CHECK **[two-actions] **SPELL 2**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** occult  **Range **60 feet; **Targets** 1 creature **Defense** Will; **Duration** 1 round |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/54` | 0.482291 | **EQUIPMENT** **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/59` | 0.482291 | **EQUIPMENT** **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/57` | 0.482291 | **EQUIPMENT** **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/68` | 0.479626 | **SYNAPTIC PULSE **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** occult **Area** 30-foot emanation **Defense** Will; **Duration** 1 round |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/20` | 0.479483 | **VAMPIRIC EXSANGUINATION **[two-actions] **SPELL 6**  **CONCENTRATE** **DEATH** **MANIPULATE** **VOID**  **Traditions** arcane, divine, occult  **Area** 30-foot cone  **Defense** basic Fortitude  You |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/7/SectionHeader/16` | 0.474066 | **VOID VESSEL **[three-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **30 feet; **Targets** you and up to 10 willing creatures **Duration** 8 hou |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/7/SectionHeader/30` | 0.473133 | **VOID WHISPERS **[two-actions] **SPELL 3**  **AUDITORY** **CONCENTRATE** **INCAPACITATION** **LINGUISTIC** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **30 feet; **Targets** 1 c |

### Query 97
- Text: What does **VAPOR FORM **[two-actions] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/37', 'PZO22001 Starfinder Player Core 364-387::/page/14/SectionHeader/17', 'PZO22001 Starfinder Player Core 364-387::/page/16/SectionHeader/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/37', 'PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/29', 'PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/44']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/44` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/37` | 0.661915 | **VAPOR FORM **[two-actions] **SPELL 4**  **AIR** **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, occult, primal  **Range **touch;** Targets** 1 willing creature  **Duration** 5 m |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/14/SectionHeader/17` | 0.591152 | **WARP WORLD **[two-actions] **FOCUS 4** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/16/SectionHeader/13` | 0.551216 | **ACCELERATE **[two-actions] **FOCUS 4** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.504223 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` | 0.504223 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.504223 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.504223 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.504223 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/27` | 0.504223 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.504223 | **SPELLS** |

### Query 98
- Text: What does **VEIL OF PRIVACY** **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/44', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/59', 'PZO22001 Starfinder Player Core 364-387::/page/21/Text/54']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/44', 'PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/52', 'PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/37']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/52` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/37` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/44` | 0.686525 | **VEIL OF PRIVACY** **SPELL 3**  **UNCOMMON** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Cast** 10 minutes  **Range **touch;** Targets** 1 creature or object  **Duration* |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/59` | 0.550620 | **EQUIPMENT** **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/54` | 0.550620 | **EQUIPMENT** **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/57` | 0.508620 | **EQUIPMENT** **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.496614 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.496614 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.496614 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.496614 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.496614 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/27` | 0.496614 | **SPELLS** |

### Query 99
- Text: What does **VERDANT CODE **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/52']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/52', 'PZO22001 Starfinder Player Core 364-387::/page/23/Text/41', 'PZO22001 Starfinder Player Core 364-387::/page/11/Text/60']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/52', 'PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/44', 'PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/59']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/44` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/59` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/52` | 0.611814 | **VERDANT CODE **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **PLANT** **WOOD**  **Traditions** arcane, primal  **Range **30 feet;** Targets** 1 unattended object with the tech trait  ** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.565857 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.565857 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` | 0.523857 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.523857 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/27` | 0.523857 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.523857 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.523857 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/59` | 0.507909 | **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/57` | 0.507909 | **EQUIPMENT** **SPELLS** |

### Query 100
- Text: What does **VIBE CHECK **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/59']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/59', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/59', 'PZO22001 Starfinder Player Core 364-387::/page/21/Text/54']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/59', 'PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/52', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/66']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/52` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/66` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/59` | 0.696129 | **VIBE CHECK **[two-actions] **SPELL 2**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** occult  **Range **60 feet; **Targets** 1 creature **Defense** Will; **Duration** 1 round |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/59` | 0.522222 | **EQUIPMENT** **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/54` | 0.522222 | **EQUIPMENT** **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/57` | 0.480222 | **EQUIPMENT** **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` | 0.479763 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.479763 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.479763 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.479763 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/27` | 0.479763 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.479763 | **SPELLS** |

### Query 101
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/66']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/73', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/54', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/66']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/66', 'PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/59', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/67']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/SectionHeader/59` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/67` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/73` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/54` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/66` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/52` | 0.838541 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/54` | 0.838541 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/49` | 0.838541 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/47` | 0.838541 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/35` | 0.838541 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/21` | 0.838541 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/69` | 0.838541 | **INTRODUCTION** |

### Query 102
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/67']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/74', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/55', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/67']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/67', 'PZO22001 Starfinder Player Core 364-387::/page/9/Text/53', 'PZO22001 Starfinder Player Core 364-387::/page/17/Text/22', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/70', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/66', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/68', 'PZO22001 Starfinder Player Core 364-387::/page/21/Text/50', 'PZO22001 Starfinder Player Core 364-387::/page/19/Text/48', 'PZO22001 Starfinder Player Core 364-387::/page/11/Text/55', 'PZO22001 Starfinder Player Core 364-387::/page/23/Text/36', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/74', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/55']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/9/Text/53` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/17/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/13/Text/70` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/66` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/68` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/21/Text/50` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/19/Text/48` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/11/Text/55` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/23/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/74` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/55` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/74` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/55` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/67` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/53` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/22` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/70` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/50` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/55` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/48` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/36` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 103
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/68']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/75', 'PZO22001 Starfinder Player Core 364-387::/page/21/Text/51', 'PZO22001 Starfinder Player Core 364-387::/page/9/Text/54']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/68', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/69', 'PZO22001 Starfinder Player Core 364-387::/page/21/Text/51', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/56', 'PZO22001 Starfinder Player Core 364-387::/page/23/Text/37', 'PZO22001 Starfinder Player Core 364-387::/page/11/Text/56', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/75', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/71', 'PZO22001 Starfinder Player Core 364-387::/page/9/Text/54', 'PZO22001 Starfinder Player Core 364-387::/page/19/Text/49', 'PZO22001 Starfinder Player Core 364-387::/page/17/Text/23', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/67']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/69` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/21/Text/51` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/56` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/23/Text/37` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/11/Text/56` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/75` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/13/Text/71` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/9/Text/54` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/19/Text/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/17/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/67` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/75` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/54` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/51` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/68` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/49` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/23` | 0.910061 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/71` | 0.910061 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/56` | 0.910061 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/56` | 0.910061 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/37` | 0.910061 | **CLASSES** |

### Query 104
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/69']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/17/Text/24', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/57', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/72']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/69', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/70', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/68']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/70` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/68` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/24` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/57` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/72` | 0.864442 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/69` | 0.822442 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/38` | 0.822442 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/50` | 0.822442 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/55` | 0.822442 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/57` | 0.822442 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/52` | 0.822442 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/76` | 0.822442 | **SKILLS** |

### Query 105
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/70']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/77', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/58', 'PZO22001 Starfinder Player Core 364-387::/page/19/Text/51']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/70', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/69', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/71']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/69` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/71` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/77` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/58` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/51` | 0.871817 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/39` | 0.829817 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/56` | 0.829817 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/70` | 0.829817 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/73` | 0.829817 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/53` | 0.829817 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/25` | 0.829817 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/58` | 0.829817 | **FEATS** |

### Query 106
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/71']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/78', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/71', 'PZO22001 Starfinder Player Core 364-387::/page/23/Text/40']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/71', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/72', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/70']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/70` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/78` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/71` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/40` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/59` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/74` | 0.902726 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/26` | 0.902726 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/52` | 0.902726 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/57` | 0.578761 | **EQUIPMENT** **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/59` | 0.578761 | **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/54` | 0.578761 | **EQUIPMENT** **SPELLS** |

### Query 107
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/72']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/23/Text/41', 'PZO22001 Starfinder Player Core 364-387::/page/17/Text/27', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/75']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/72', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/71', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/73']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/71` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/73` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/41` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/27` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/75` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/60` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/53` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` | 0.847304 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/79` | 0.847304 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/57` | 0.759411 | **EQUIPMENT** **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/59` | 0.759411 | **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/54` | 0.759411 | **EQUIPMENT** **SPELLS** |

### Query 108
- Text: What is the rule about **Spell Lists**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/73']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/80', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/60', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/73']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/73', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/74', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/72']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/74` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/72` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/80` | 0.890837 | **Spell Lists** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/60` | 0.890837 | **Spell Lists** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/73` | 0.890837 | **Spell Lists** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/55` | 0.848837 | **Spell Lists** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/58` | 0.848837 | **Spell Lists** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/76` | 0.848837 | **Spell Lists** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/54` | 0.848837 | **Spell Lists** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/42` | 0.848837 | **Spell Lists** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/28` | 0.848837 | **Spell Lists** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/61` | 0.848837 | **Spell Lists** |

### Query 109
- Text: What is the rule about **Spells**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/74']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/23/Text/43', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/77', 'PZO22001 Starfinder Player Core 364-387::/page/19/Text/55']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/74', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/75', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/73']
- Expanded expected found: `True`
- Expanded expected rank: `7`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/75` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/73` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/43` | 0.798799 | **Spells** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/77` | 0.798799 | **Spells** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/55` | 0.798799 | **Spells** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/62` | 0.756799 | **Spells** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/29` | 0.756799 | **Spells** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/81` | 0.756799 | **Spells** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/74` | 0.756799 | **Spells** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/59` | 0.756799 | **Spells** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/61` | 0.756799 | **Spells** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/56` | 0.756799 | **Spells** |

### Query 110
- Text: What is the rule about **Focus Spells**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/75']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/11/Text/63', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/78', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/82']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/75', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/74', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/76']
- Expanded expected found: `True`
- Expanded expected rank: `8`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/74` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/76` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/63` | 0.926221 | **Focus Spells** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/78` | 0.926221 | **Focus Spells** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/82` | 0.926221 | **Focus Spells** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/56` | 0.884221 | **Focus Spells** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/44` | 0.884221 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/62` | 0.884221 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/30` | 0.884221 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/75` | 0.884221 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/60` | 0.884221 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/57` | 0.884221 | **Focus Spells** |

### Query 111
- Text: Summarize **Rituals**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/76']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/13/Text/79', 'PZO22001 Starfinder Player Core 364-387::/page/23/Text/45', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/76']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/76', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/77', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/75']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/77` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/75` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/79` | 0.971114 | **Rituals** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/45` | 0.971114 | **Rituals** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/76` | 0.971114 | **Rituals** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/31` | 0.929114 | **Rituals** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/61` | 0.929114 | **Rituals** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/57` | 0.929114 | **Rituals** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/83` | 0.929114 | **Rituals** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/64` | 0.929114 | **Rituals** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/63` | 0.929114 | **Rituals** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/58` | 0.929114 | **Rituals** |

### Query 112
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/77']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/23/Text/46', 'PZO22001 Starfinder Player Core 364-387::/page/19/Text/58', 'PZO22001 Starfinder Player Core 364-387::/page/11/Text/65']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/77', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/76', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/78']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/76` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/78` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/46` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/58` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/65` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/84` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/77` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/32` | 0.923000 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/62` | 0.923000 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/80` | 0.923000 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/64` | 0.923000 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/59` | 0.923000 | **PLAYING THE ** **GAME** |

### Query 113
- Text: Summarize **CONDITIONS **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/78']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/78', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/65', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/85']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/78', 'PZO22001 Starfinder Player Core 364-387::/page/21/Text/60', 'PZO22001 Starfinder Player Core 364-387::/page/23/Text/47', 'PZO22001 Starfinder Player Core 364-387::/page/19/Text/59', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/81', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/65', 'PZO22001 Starfinder Player Core 364-387::/page/11/Text/66', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/85', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/77', 'PZO22001 Starfinder Player Core 364-387::/page/17/Text/33', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/79', 'PZO22001 Starfinder Player Core 364-387::/page/9/Text/63']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/21/Text/60` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/23/Text/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/19/Text/59` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/13/Text/81` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/3/Text/65` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/11/Text/66` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/1/Text/85` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/77` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/17/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/79` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/9/Text/63` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/78` | 0.894175 | **CONDITIONS ** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/65` | 0.666199 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/85` | 0.666199 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/60` | 0.636199 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/81` | 0.636199 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/66` | 0.636199 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/63` | 0.636199 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/59` | 0.636199 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/33` | 0.636199 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/47` | 0.636199 | **CONDITIONS ** **APPENDIX** |

### Query 114
- Text: Summarize **APPENDIX** **GLOSSARY & **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/79']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/79', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/86', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/82']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/79', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/80', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/78']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/80` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/78` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/79` | 1.012230 | **APPENDIX** **GLOSSARY & ** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/86` | 0.756362 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/82` | 0.756362 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/67` | 0.714362 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/66` | 0.714362 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/34` | 0.714362 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/48` | 0.714362 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/61` | 0.714362 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/60` | 0.714362 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/64` | 0.714362 | **GLOSSARY & ** **INDEX** |

### Query 115
- Text: What is the rule about **INDEX** **CHARACTER **?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/80']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/80', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/66', 'PZO22001 Starfinder Player Core 364-387::/page/1/Text/86']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/80', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/82', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/79']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/82` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/79` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/80` | 0.814328 | **INDEX** **CHARACTER ** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/66` | 0.522867 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/86` | 0.522867 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/34` | 0.480867 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/82` | 0.480867 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/67` | 0.480867 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/64` | 0.480867 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/60` | 0.480867 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/61` | 0.480867 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/48` | 0.480867 | **GLOSSARY & ** **INDEX** |

### Query 116
- Text: Summarize **SHEET**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/82']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/82', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/73', 'PZO22001 Starfinder Player Core 364-387::/page/3/Text/58']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/5/Text/82', 'PZO22001 Starfinder Player Core 364-387::/page/6/SectionHeader/1', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/80']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/80` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/82` | 0.943034 | **SHEET** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/58` | 0.482549 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/73` | 0.482549 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/25` | 0.440549 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/70` | 0.440549 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/53` | 0.440549 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/56` | 0.440549 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/39` | 0.440549 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/77` | 0.440549 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/58` | 0.440549 | **FEATS** |

### Query 117
- Text: What is the rule about **THE SUMMON TRAIT**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/SectionHeader/1', 'PZO22001 Starfinder Player Core 364-387::/page/6/Text/2', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/34']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/SectionHeader/1', 'PZO22001 Starfinder Player Core 364-387::/page/6/Text/2', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/82']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/5/Text/82` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/SectionHeader/1` | 0.920298 | **THE SUMMON TRAIT** |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/6/Text/2` | 0.556498 | Spells with the summon trait can conjure creatures,  typically ones with a particular trait. Such creatures can  be found in *Alien Core* and similar books. Unless noted  otherwise, the creature must |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/34` | 0.505653 | **SUMMON DRAGON **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, divine, occult, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You s |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/20` | 0.459414 | **SUMMON CELESTIAL **[three-actions] **SPELL 5**  **CONCENTRATE** **HOLY** **MANIPULATE** **SUMMON**  **Traditions** divine **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/73` | 0.459030 | **SUMMON GIANT **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/66` | 0.455227 | **SUMMON FIEND **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON** **UNHOLY**  **Traditions** divine  **Range **30 feet **Duration** sustained up to 1 minute  You summon a creatur |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/4` | 0.452727 | **SUMMON MONITOR **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** divine **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that ha |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/43` | 0.448454 | **SUMMON ELEMENTAL **[three-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/18` | 0.447960 | **SUMMON ROBOT **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51` | 0.447087 | **SUMMON ENTITY **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** occult **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |

### Query 118
- Text: What is the rule about Spells with the summon trait can conjure creatures,  typically ones with a particular trait. Such creatures can  be found in *Alien Core* and similar books. Unless noted  otherwise, the creature must be common, it gains the  summoned trait (page 299), and it must appear in an  unoccupied space in range large enough to contain it.  The highest level of creature the spell can summon  depends on the rank of the spell, as listed below. The  spell can still summon a creature of a lower level if you  so choose. These rules apply only to spells that have  the summon trait; other spells that call or conjure items  or beings but that don't have the trait, like *summon * *instrument*, work as explained in the spell.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/Text/2', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/34', 'PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/Text/2', 'PZO22001 Starfinder Player Core 364-387::/page/6/Table/3', 'PZO22001 Starfinder Player Core 364-387::/page/6/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/Table/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/Text/2` | 1.013350 | Spells with the summon trait can conjure creatures,  typically ones with a particular trait. Such creatures can  be found in *Alien Core* and similar books. Unless noted  otherwise, the creature must |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/34` | 0.632698 | **SUMMON DRAGON **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, divine, occult, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You s |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/20` | 0.622652 | **SUMMON CELESTIAL **[three-actions] **SPELL 5**  **CONCENTRATE** **HOLY** **MANIPULATE** **SUMMON**  **Traditions** divine **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/43` | 0.589871 | **SUMMON ELEMENTAL **[three-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creat |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12` | 0.582926 | **SUMMON ANIMAL **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/66` | 0.576813 | **SUMMON FIEND **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON** **UNHOLY**  **Traditions** divine  **Range **30 feet **Duration** sustained up to 1 minute  You summon a creatur |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/51` | 0.573565 | **SUMMON ENTITY **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** occult **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/27` | 0.572093 | **SUMMON CONSTRUCT **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/73` | 0.566414 | **SUMMON GIANT **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature that has |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/11` | 0.560952 | **SUMMON PLANT OR FUNGUS **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** primal **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature |

### Query 119
- Text: Lookup values for Spell RankMaximum Creature Level1st–12nd13rd24th35th56th77th98th119th1310th15
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/Table/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/Table/3', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/487', 'PZO22001 Starfinder Player Core 364-387::/page/18/Table/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/Table/3', 'PZO22001 Starfinder Player Core 364-387::/page/6/Text/2', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/486']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/486` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/Table/3` | 1.008710 | Spell RankMaximum Creature Level1st–12nd13rd24th35th56th77th98th119th1310th15 |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/487` | 0.706255 | Maximum Creature Level |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/18/Table/2` | 0.704322 | Creature LevelRitual Rank RequiredCost–1 or 02150 credits12600 credits231,050 credits331,800 credits443,000 credits544,800 credits657,500 credits7510,800 credits8615,000 credits9621,000 credits10730,0 |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/486` | 0.610844 | Spell Rank |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/17/Table/9` | 0.574785 | RankRitual2Animate object2Consecrate2Create undead4Atone4Blight4Plant growth5Call spirit5Planar servitor5Resurrect6Awaken animal6Awaken computer6Binding circle6Commune6Primal call7Collective memories7 |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/470` | 0.574555 | Creature Level |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/6/Text/2` | 0.501037 | Spells with the summon trait can conjure creatures,  typically ones with a particular trait. Such creatures can  be found in *Alien Core* and similar books. Unless noted  otherwise, the creature must |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12` | 0.477984 | **SUMMON ANIMAL **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/11` | 0.476873 | **SUMMON PLANT OR FUNGUS **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** primal **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/16` | 0.467759 | **Range **10 feet; **Target** 1 computer or tech creature of up to the  level on the table |

### Query 120
- Text: What is the rule about Spell Rank?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/486']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/486', 'PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/471', 'PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/448']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/486', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/487', 'PZO22001 Starfinder Player Core 364-387::/page/6/Table/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/487` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/Table/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/486` | 0.855858 | Spell Rank |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/471` | 0.620446 | Ritual Rank Required |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/448` | 0.585264 | Rank |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/412` | 0.543264 | Rank |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/6/Table/3` | 0.542110 | Spell RankMaximum Creature Level1st–12nd13rd24th35th56th77th98th119th1310th15 |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/17/Text/6` | 0.503834 | When you take charge of a ritual, you are its primary caster,  and others assisting you are secondary casters. You can be  a primary caster for a ritual even if you can't cast spells. You  must know t |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/54` | 0.482266 | **Spell Lists** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/73` | 0.482266 | **Spell Lists** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/9/Text/58` | 0.482266 | **Spell Lists** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/76` | 0.482266 | **Spell Lists** |

### Query 121
- Text: Summarize Maximum Creature Level
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/487']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/487', 'PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/470', 'PZO22001 Starfinder Player Core 364-387::/page/6/Table/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/487', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/486', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/488']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/486` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/488` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/487` | 0.989661 | Maximum Creature Level |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/470` | 0.856818 | Creature Level |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/6/Table/3` | 0.771756 | Spell RankMaximum Creature Level1st–12nd13rd24th35th56th77th98th119th1310th15 |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/18/Table/2` | 0.626937 | Creature LevelRitual Rank RequiredCost–1 or 02150 credits12600 credits231,050 credits331,800 credits443,000 credits544,800 credits657,500 credits7510,800 credits8615,000 credits9621,000 credits10730,0 |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/13/ListItem/19` | 0.573392 | Mental resistance equal to half the creature's level  (minimum 1) |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/16` | 0.524431 | **Range **10 feet; **Target** 1 computer or tech creature of up to the  level on the table |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/12` | 0.522910 | **Range **10 feet; **Targets** 1 dead creature of up to 10th level |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/7` | 0.512558 | **Range **10 feet; **Target** 1 animal of up to the level on the table You grant intelligence to the target, transforming it into a  beast. If it was previously an animal companion or minion, it  can |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/18/Text/27` | 0.485488 | **Range **10 feet; **Targets** another creature of up to 8th level who  is a worshipper of the same deity or philosophy as you |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12` | 0.481232 | **SUMMON ANIMAL **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature |

### Query 122
- Text: Summarize 1st
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/488']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/488', 'PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/476', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/491']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/488', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/487', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/489']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/487` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/489` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/488` | 0.640923 | 1st |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/476` | 0.581124 | 1 |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/491` | 0.581124 | 1 |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/489` | 0.525205 | –1 |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/477` | 0.493746 | 2 |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/418` | 0.481745 | 2 |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/416` | 0.481745 | 2 |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/414` | 0.481745 | 2 |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/474` | 0.481745 | 2 |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/479` | 0.481745 | 2 |

### Query 123
- Text: Summarize –1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/489']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/489', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/491', 'PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/476']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/489', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/490', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/488']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/490` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/488` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/489` | 0.738680 | –1 |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/491` | 0.564189 | 1 |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/476` | 0.564189 | 1 |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/477` | 0.441670 | 2 |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/418` | 0.429670 | 2 |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/474` | 0.429670 | 2 |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/479` | 0.429670 | 2 |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/493` | 0.429670 | 2 |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/414` | 0.429670 | 2 |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/416` | 0.429670 | 2 |

### Query 124
- Text: Summarize 2nd
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/490']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/490', 'PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/477', 'PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/418']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/490', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/491', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/489']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/491` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/489` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/490` | 0.723063 | 2nd |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/477` | 0.565593 | 2 |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/418` | 0.565593 | 2 |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/479` | 0.523593 | 2 |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/474` | 0.523593 | 2 |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/493` | 0.523593 | 2 |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/416` | 0.523593 | 2 |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/414` | 0.523593 | 2 |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/492` | 0.421716 | 3rd |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/21/SectionHeader/1` | 0.399730 | **CONSECRATE** **RITUAL 2** |

### Query 125
- Text: Summarize 1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/491']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/476', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/491', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/489']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/491', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/492', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/490']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/492` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/490` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/476` | 0.669108 | 1 |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/491` | 0.669108 | 1 |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/489` | 0.633488 | –1 |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/477` | 0.525765 | 2 |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/418` | 0.513765 | 2 |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/479` | 0.513765 | 2 |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/474` | 0.513765 | 2 |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/414` | 0.513765 | 2 |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/493` | 0.513765 | 2 |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/416` | 0.513765 | 2 |

### Query 126
- Text: Summarize 3rd
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/492']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/492', 'PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/483', 'PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/482']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/492', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/493', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/491']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/493` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/491` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/492` | 0.794516 | 3rd |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/483` | 0.580890 | 3 |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/482` | 0.580890 | 3 |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/480` | 0.538890 | 3 |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/495` | 0.538890 | 3 |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/490` | 0.460646 | 2nd |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/25` | 0.414078 | **Heightened (3rd)** The damage dealt by the attacks increases  to 2 dice. |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/51` | 0.414078 | **Heightened (3rd)** The damage dealt by the attacks  increases to 2 dice. |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/493` | 0.393601 | 2 |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/494` | 0.391617 | 4th |

### Query 127
- Text: Summarize 2
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/493']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/418', 'PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/477', 'PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/416']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/493', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/492', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/494']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/492` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/494` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/418` | 0.689465 | 2 |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/477` | 0.689465 | 2 |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/416` | 0.689465 | 2 |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/479` | 0.647465 | 2 |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/414` | 0.647465 | 2 |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/493` | 0.647465 | 2 |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/474` | 0.647465 | 2 |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/490` | 0.507646 | 2nd |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/476` | 0.471336 | 1 |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/491` | 0.459336 | 1 |

### Query 128
- Text: Summarize 4th
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/494']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/494', 'PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/420', 'PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/489']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/494', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/493', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/495']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/493` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/495` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/494` | 0.830106 | 4th |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/420` | 0.648322 | 4 |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/489` | 0.648322 | 4 |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/424` | 0.606322 | 4 |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/485` | 0.606322 | 4 |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/486` | 0.606322 | 4 |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/422` | 0.606322 | 4 |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/496` | 0.435651 | 5th |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/492` | 0.434068 | 3rd |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/6/Text/9` | 0.406614 | **Heightened (4th)** The spell affects all creatures in a 20 foot burst. Each creature must be affected by the same  emotion. |

### Query 129
- Text: Summarize 3
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/495']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/495', 'PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/483', 'PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/482']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/495', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/496', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/494']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/496` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/494` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/495` | 0.731895 | 3 |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/482` | 0.731895 | 3 |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/483` | 0.731895 | 3 |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/480` | 0.689895 | 3 |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/492` | 0.536050 | 3rd |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/477` | 0.516533 | 2 |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/418` | 0.516533 | 2 |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/493` | 0.516533 | 2 |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/474` | 0.516533 | 2 |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/416` | 0.516533 | 2 |

### Query 130
- Text: Summarize 5th
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/496']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/496', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/497', 'PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/428']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/496', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/497', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/495']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/497` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/495` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/496` | 0.828489 | 5th |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/497` | 0.640791 | 5 |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/428` | 0.640791 | 5 |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/426` | 0.598791 | 5 |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/492` | 0.598791 | 5 |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/488` | 0.598791 | 5 |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/495` | 0.598791 | 5 |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/430` | 0.598791 | 5 |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/498` | 0.503063 | 6th |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/494` | 0.485219 | 4th |

### Query 131
- Text: Summarize 5
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/497']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/497', 'PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/430', 'PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/428']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/497', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/496', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/498']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/496` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/498` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/497` | 0.772788 | 5 |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/430` | 0.772788 | 5 |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/428` | 0.772788 | 5 |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/492` | 0.730788 | 5 |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/426` | 0.730788 | 5 |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/495` | 0.730788 | 5 |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/488` | 0.730788 | 5 |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/496` | 0.609137 | 5th |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/432` | 0.467672 | 6 |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/440` | 0.467672 | 6 |

### Query 132
- Text: Summarize 6th
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/498']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/498', 'PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/436', 'PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/434']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/498', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/499', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/497']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/499` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/497` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/498` | 0.848854 | 6th |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/436` | 0.647621 | 6 |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/434` | 0.647621 | 6 |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/498` | 0.605621 | 6 |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/438` | 0.605621 | 6 |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/491` | 0.605621 | 6 |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/501` | 0.605621 | 6 |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/440` | 0.605621 | 6 |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/432` | 0.605621 | 6 |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/500` | 0.508216 | 7th |

### Query 133
- Text: Summarize 7
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/499']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/499', 'PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/444', 'PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/442']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/499', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/498', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/500']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/498` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/500` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/499` | 0.766039 | 7 |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/444` | 0.766039 | 7 |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/442` | 0.766039 | 7 |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/504` | 0.724039 | 7 |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/494` | 0.724039 | 7 |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/507` | 0.724039 | 7 |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/500` | 0.673809 | 7th |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/432` | 0.473241 | 6 |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/436` | 0.473241 | 6 |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/440` | 0.473241 | 6 |

### Query 134
- Text: Summarize 7th
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/500']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/500', 'PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/442', 'PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/444']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/500', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/499', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/501']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/499` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/501` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/500` | 0.848591 | 7th |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/442` | 0.651346 | 7 |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/444` | 0.651346 | 7 |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/499` | 0.621346 | 7 |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/494` | 0.609346 | 7 |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/507` | 0.609346 | 7 |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/504` | 0.609346 | 7 |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/502` | 0.501446 | 8th |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/498` | 0.495836 | 6th |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/10/Text/31` | 0.453687 | **Heightened (7th)** The area increases to a 60-foot cone. |

### Query 135
- Text: Summarize 9
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/501']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/501', 'PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/519', 'PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/516']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/501', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/502', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/500']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/502` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/500` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/501` | 0.770045 | 9 |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/516` | 0.770045 | 9 |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/519` | 0.770045 | 9 |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/500` | 0.728045 | 9 |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/450` | 0.728045 | 9 |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/504` | 0.657978 | 9th |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/510` | 0.455491 | 8 |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/446` | 0.455491 | 8 |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/513` | 0.455491 | 8 |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/497` | 0.455491 | 8 |

### Query 136
- Text: Summarize 8th
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/502']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/502', 'PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/513', 'PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/510']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/502', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/503', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/501']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/503` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/501` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/502` | 0.857094 | 8th |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/513` | 0.666071 | 8 |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/510` | 0.666071 | 8 |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/446` | 0.624071 | 8 |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/497` | 0.624071 | 8 |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/504` | 0.511312 | 9th |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/500` | 0.507894 | 7th |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/498` | 0.437676 | 6th |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/14/Text/36` | 0.432774 | **Heightened (8th)** Your parallel forms are quickened and can  use the extra action to Step, Stride, or Strike. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/494` | 0.385223 | 4th |

### Query 137
- Text: Summarize 11
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/503']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/506', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/503', 'PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/509']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/503', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/504', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/502']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/504` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/502` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/506` | 0.764621 | 11 |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/503` | 0.764621 | 11 |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/509` | 0.535902 | 12 |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/503` | 0.479429 | 10 |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/522` | 0.479429 | 10 |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/452` | 0.479429 | 10 |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/525` | 0.479429 | 10 |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/521` | 0.435902 | 16 |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/524` | 0.433307 | 17 |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/505` | 0.419468 | 13 |

### Query 138
- Text: Summarize 9th
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/504']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/504', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/501', 'PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/516']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/504', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/503', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/505']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/503` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/505` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/504` | 0.843315 | 9th |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/501` | 0.660144 | 9 |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/516` | 0.660144 | 9 |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/500` | 0.618144 | 9 |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/519` | 0.618144 | 9 |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/450` | 0.618144 | 9 |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/502` | 0.488375 | 8th |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/506` | 0.472604 | 10th |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/28` | 0.443815 | **Heightened (9th)** Increase the number of targets to 5 targets.  The damage dealt by the attacks increases to 4 dice. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/54` | 0.443815 | **Heightened (9th)** Increase the number of targets to 5  targets. The damage dealt by the attacks increases to  4 dice. |

### Query 139
- Text: Summarize 13
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/505']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/512', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/505', 'PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/509']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/505', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/506', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/504']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/506` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/504` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/512` | 0.781589 | 13 |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/505` | 0.781589 | 13 |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/509` | 0.578297 | 12 |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/515` | 0.531543 | 14 |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/517` | 0.473679 | 135,000 credits |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/521` | 0.468047 | 16 |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/506` | 0.455605 | 11 |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/503` | 0.455605 | 11 |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/507` | 0.441952 | 15 |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/518` | 0.441952 | 15 |

### Query 140
- Text: Summarize 10th
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/506']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/506', 'PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/503', 'PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/522']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/506', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/507', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/505']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/507` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/505` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/506` | 0.847502 | 10th |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/503` | 0.679157 | 10 |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/522` | 0.679157 | 10 |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/452` | 0.637157 | 10 |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/525` | 0.637157 | 10 |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/504` | 0.507377 | 9th |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/11/SectionHeader/32` | 0.466888 | **Duration** 10 minutes |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/15/Text/16` | 0.466888 | **Duration** 10 minutes |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/20/SectionHeader/11` | 0.430799 | **Duration** up to 10 minutes |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/20/SectionHeader/33` | 0.430799 | **Duration** up to 10 minutes |

### Query 141
- Text: Summarize 15
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/507']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/518', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/507', 'PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/521']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/507', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/506', 'PZO22001 Starfinder Player Core 364-387::/page/6/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/506` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/518` | 0.777005 | 15 |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/507` | 0.777005 | 15 |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/521` | 0.614131 | 16 |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/515` | 0.530304 | 14 |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/524` | 0.501762 | 17 |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/499` | 0.451578 | 15,000 credits |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/505` | 0.438149 | 13 |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/512` | 0.438149 | 13 |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/475` | 0.408570 | 150 credits |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/13/ListItem/43` | 0.397881 | A burrow Speed of 15 feet |

### Query 142
- Text: What is the rule about following emotions, but if you pick anger or joy this spell  gains the incapacitation trait.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/Text/4', 'PZO22001 Starfinder Player Core 364-387::/page/8/Text/5', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/Text/4', 'PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/507', 'PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/507` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/Text/4` | 0.970297 | following emotions, but if you pick anger or joy this spell  gains the incapacitation trait. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/5` | 0.538178 | **Critical Failure** As failure, except the target babbles  incoherently. Any creature that begins its turn within  20 feet of the target must attempt a Will saving throw.  On a failure, it must use i |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/6` | 0.529980 | You cause memories of the target's resentment, regret, and  other negative feelings to engorge its shadow until it grows  large enough to swallow them whole. The target attempts a  Will saving throw. |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/14/Text/7` | 0.487698 | The first time after casting this spell when you make an  attack roll against a creature within your quantum field  during *quantum* *analysis'* duration, you roll twice and use  the better result. Th |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/5` | 0.459974 | **Anger** On its next turn, the target spends its first  action to attack the nearest creature, even if it's an  ally. |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/1` | 0.458778 | **SUGGESTION **[two-actions] **SPELL 4**  **CONCENTRATE** **INCAPACITATION** **LINGUISTIC** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creatu |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/4` | 0.453399 | **Failure** The target begins to wander aimlessly, using each  action to Step in a random direction. When it moves,  the target takes the safest route and doesn't enter  hazardous terrain. The spell h |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/10/Text/28` | 0.445644 | **Success** For 1 round, the creature can't use reactions and  must attempt another save at the start of its turn; on a  failure, it is slowed 1 for that turn as it sobs uncontrollably. |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/16/Text/48` | 0.440558 | You briefly establish a mystical connection between your  mind and a piece of technology, allowing you to understand  the object or manipulate its power. Choose any one of the  following effects. An u |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/20/Text/12` | 0.438804 | You tear the veil to the afterlife and call a spirit from its final  resting place. You must call the spirit by name, and you must  provide a connection to the spirit, such as a possession, a  garment |

### Query 143
- Text: What is the rule about **Anger** On its next turn, the target spends its first  action to attack the nearest creature, even if it's an  ally.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/5', 'PZO22001 Starfinder Player Core 364-387::/page/15/Text/5', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/67']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/5', 'PZO22001 Starfinder Player Core 364-387::/page/6/Text/4', 'PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/5` | 0.938809 | **Anger** On its next turn, the target spends its first  action to attack the nearest creature, even if it's an  ally. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/15/Text/5` | 0.559725 | **Trigger** An enemy targets you with a Strike or spell attack. |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/67` | 0.555068 | **Range **within your quantum field;** Targets** the triggering  creature |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/4` | 0.508588 | **Failure** The target begins to wander aimlessly, using each  action to Step in a random direction. When it moves,  the target takes the safest route and doesn't enter  hazardous terrain. The spell h |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/37` | 0.506803 | **TRUE TARGET **[one-action] **SPELL 7**  **CONCENTRATE** **FORTUNE** **PREDICTION**  **Traditions** arcane, occult  **Range **60 feet;** Targets** 4 creatures  **Duration** until the start of your ne |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/16/Text/31` | 0.502805 | **Range **within your quantum field;** Targets** 1 creature **Defense** basic Will |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/14/Text/7` | 0.502384 | The first time after casting this spell when you make an  attack roll against a creature within your quantum field  during *quantum* *analysis'* duration, you roll twice and use  the better result. Th |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/15/Text/6` | 0.499560 | **Range **120 feet; **Target **the triggering enemy |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/10/Text/28` | 0.498241 | **Success** For 1 round, the creature can't use reactions and  must attempt another save at the start of its turn; on a  failure, it is slowed 1 for that turn as it sobs uncontrollably. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/23` | 0.489055 | **Range **60 feet;** Target **the triggering creature |

### Query 144
- Text: What is the rule about **Joy** The target can't take any hostile actions.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/6', 'PZO22001 Starfinder Player Core 364-387::/page/5/Text/1', 'PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/6', 'PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/7', 'PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/6` | 0.935727 | **Joy** The target can't take any hostile actions. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/1` | 0.547007 | can't use reactions. It also can't use move actions except to  dance, using the Stride action to move up to half its Speed. **Critical Success** The target is unaffected. |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/7` | 0.536288 | **Fear** The target becomes frightened 2. |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/5` | 0.489938 | **Anger** On its next turn, the target spends its first  action to attack the nearest creature, even if it's an  ally. |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/10/SectionHeader/32` | 0.480321 | **WAVE OF WARNING **[two-actions] **SPELL 5**  **CONCENTRATE** **EMOTION** **FEAR** **MANIPULATE** **MENTAL** **NONLETHAL**  **Traditions** divine, primal  **Range **120 feet; **Targets **1 creature, |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/4` | 0.476262 | **Failure** The target begins to wander aimlessly, using each  action to Step in a random direction. When it moves,  the target takes the safest route and doesn't enter  hazardous terrain. The spell h |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/22` | 0.474433 | **Critical** **Success** The target is unaffected. |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/7` | 0.474433 | **Critical** **Success** The target is unaffected. |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/62` | 0.474433 | **Critical** **Success** The target is unaffected. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/21` | 0.473973 | **Critical Failure** You accidentally awaken the target with  a pure homicidal hatred toward you. The target's  Intelligence, Wisdom, and Charisma modifiers increase to  –2 if they were lower. It beco |

### Query 145
- Text: Summarize **Fear** The target becomes frightened 2.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/7', 'PZO22001 Starfinder Player Core 364-387::/page/16/Text/10', 'PZO22001 Starfinder Player Core 364-387::/page/12/Text/64']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/7', 'PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/8', 'PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/7` | 1.019163 | **Fear** The target becomes frightened 2. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/16/Text/10` | 0.661665 | **Failure** The target takes full damage and is enfeebled 1  for 1 round. |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/64` | 0.651419 | **Failure** The target takes full damage and is sickened 1. |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/65` | 0.614242 | **Critical** **Failure** The target takes double damage and is  sickened 2. |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/6` | 0.597714 | **Joy** The target can't take any hostile actions. |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/16/Text/11` | 0.579247 | **Critical Failure** The target takes double damage and is  enfeebled 1 for 1 minute. |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/10/SectionHeader/32` | 0.576351 | **WAVE OF WARNING **[two-actions] **SPELL 5**  **CONCENTRATE** **EMOTION** **FEAR** **MANIPULATE** **MENTAL** **NONLETHAL**  **Traditions** divine, primal  **Range **120 feet; **Targets **1 creature, |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/24` | 0.568832 | **Failure** The target takes full damage and is stupefied 1 until the  end of your next turn. You Recall Knowledge about the target. **Critical** **Failure** As failure, except the target takes double |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/3` | 0.562009 | **Success** The target hears the strange whispers, becoming  stupefied 1 for 1 round. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/62` | 0.558663 | **Critical** **Success** The target is unaffected. |

### Query 146
- Text: What is the rule about **Heightened (4th)** The spell affects all creatures in a 20 foot burst. Each creature must be affected by the same  emotion.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/Text/9', 'PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/53', 'PZO22001 Starfinder Player Core 364-387::/page/13/Text/54']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/Text/9', 'PZO22001 Starfinder Player Core 364-387::/page/6/SectionHeader/10', 'PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/SectionHeader/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/ListItem/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/Text/9` | 0.984520 | **Heightened (4th)** The spell affects all creatures in a 20 foot burst. Each creature must be affected by the same  emotion. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/53` | 0.630877 | **SURE FOOTING **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You free the target's li |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/54` | 0.615226 | **Heightened (9th)** Increase the number of targets to 5  targets. The damage dealt by the attacks increases to  4 dice. |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/53` | 0.583872 | **Heightened (6th)** Increase the number of targets to 5  targets. The damage dealt by the attacks increases to  3 dice. |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/28` | 0.573226 | **Heightened (9th)** Increase the number of targets to 5 targets.  The damage dealt by the attacks increases to 4 dice. |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/27` | 0.571872 | **Heightened (6th)** Increase the number of targets to 5 targets.  The damage dealt by the attacks increases to 3 dice. |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/52` | 0.569213 | **Heightened (5th)** Increase the number of targets to 5  targets. The damage dealt by the attacks increases to  2 dice. |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/26` | 0.569213 | **Heightened (5th)** Increase the number of targets to 5 targets.  The damage dealt by the attacks increases to 2 dice. |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/23` | 0.568592 | **Heightened (10th)** As 9th rank, except it doesn't matter how  long ago the target died. The ritual requires 16 secondary  casters, each of whom must be at least half the target's  level. The target |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/14` | 0.552612 | **Heightened (7th)** The consecrated area also gains the effects  of the *planar seal* spell, but the effect doesn't attempt to  counteract teleportation by worshippers of your deity. The  cost increa |

### Query 147
- Text: What does **VIBRANT PATTERN **[two-actions] **SPELL 6** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/SectionHeader/10', 'PZO22001 Starfinder Player Core 364-387::/page/14/SectionHeader/32', 'PZO22001 Starfinder Player Core 364-387::/page/11/SectionHeader/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/SectionHeader/10', 'PZO22001 Starfinder Player Core 364-387::/page/6/Text/9', 'PZO22001 Starfinder Player Core 364-387::/page/6/Text/54']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/Text/54` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/SectionHeader/10` | 0.748640 | **VIBRANT PATTERN **[two-actions] **SPELL 6**  **ILLUSION** **INCAPACITATION** **MANIPULATE** **SUBTLE** **VISUAL**  **Traditions** arcane, occult  **Range **120 feet; **Area** 10-foot burst  **Defens |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/14/SectionHeader/32` | 0.565979 | **PARALLEL FORMS **[two-actions] **FOCUS 6** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/11/SectionHeader/16` | 0.538736 | **DATA DRAIN **[two-actions] **FOCUS 6** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/14/Text/2` | 0.493966 | **QUANTUM ANALYSIS **[one-action] **FOCUS 6** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/11/SectionHeader/46` | 0.489770 | **ELEMENTAL NOVA **[two-actions] **FOCUS 6** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/13/SectionHeader/1` | 0.489575 | **SHADOW PRISON **[two-actions] **FOCUS 6** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/12/SectionHeader/39` | 0.486584 | **REMIX **[two-actions] **FOCUS 6** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/1/SectionHeader/68` | 0.477469 | **SYNAPTIC PULSE **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** occult **Area** 30-foot emanation **Defense** Will; **Duration** 1 round |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/21/Text/54` | 0.468011 | **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/3/Text/59` | 0.468011 | **EQUIPMENT** **SPELLS** |

### Query 148
- Text: What is the rule about In addition, a creature must attempt a Will saving  throw if it's inside the pattern when you cast it, enters the  pattern, ends its turn within the pattern, or uses a Seek or  Interact action on the pattern. A creature currently blinded  by the pattern doesn't need to attempt new saving throws.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/Text/17', 'PZO22001 Starfinder Player Core 364-387::/page/6/Text/19', 'PZO22001 Starfinder Player Core 364-387::/page/8/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/Text/17', 'PZO22001 Starfinder Player Core 364-387::/page/6/Text/16', 'PZO22001 Starfinder Player Core 364-387::/page/6/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/Text/17` | 0.996337 | In addition, a creature must attempt a Will saving  throw if it's inside the pattern when you cast it, enters the  pattern, ends its turn within the pattern, or uses a Seek or  Interact action on the |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/6/Text/19` | 0.700172 | **Failure** The creature is blinded by the pattern. If it exits  the pattern, it can attempt a new save to recover from  the blinded condition at the end of each of its turns, to  a maximum duration o |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/5` | 0.628773 | **Critical Failure** As failure, except the target babbles  incoherently. Any creature that begins its turn within  20 feet of the target must attempt a Will saving throw.  On a failure, it must use i |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/10/Text/28` | 0.558946 | **Success** For 1 round, the creature can't use reactions and  must attempt another save at the start of its turn; on a  failure, it is slowed 1 for that turn as it sobs uncontrollably. |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/16/Text/48` | 0.553762 | You briefly establish a mystical connection between your  mind and a piece of technology, allowing you to understand  the object or manipulate its power. Choose any one of the  following effects. An u |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/16/Text/22` | 0.525455 | You trap a creature in a time loop of your creation. The  target sees and reacts to a repeating loop of events, based  on the result of a Will save. |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/15/Text/10` | 0.514547 | **Failure** The triggering attack misses. You are undetected  to the triggering creature for 1 round. If you use a  hostile action, this effect ends after that hostile action  is completed. |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/66` | 0.511017 | **Trigger** A creature in your quantum field would succeed (but  not critically succeed) a saving throw. |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/6` | 0.509913 | You cause memories of the target's resentment, regret, and  other negative feelings to engorge its shadow until it grows  large enough to swallow them whole. The target attempts a  Will saving throw. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/4` | 0.498676 | **Failure** The target begins to wander aimlessly, using each  action to Step in a random direction. When it moves,  the target takes the safest route and doesn't enter  hazardous terrain. The spell h |

### Query 149
- Text: What is the rule about **Failure** The creature is blinded by the pattern. If it exits  the pattern, it can attempt a new save to recover from  the blinded condition at the end of each of its turns, to  a maximum duration of 1 minute.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/Text/19', 'PZO22001 Starfinder Player Core 364-387::/page/6/Text/17', 'PZO22001 Starfinder Player Core 364-387::/page/10/Text/28']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/6/Text/19', 'PZO22001 Starfinder Player Core 364-387::/page/6/Text/18', 'PZO22001 Starfinder Player Core 364-387::/page/6/Text/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/6/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/6/Text/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/Text/19` | 0.972617 | **Failure** The creature is blinded by the pattern. If it exits  the pattern, it can attempt a new save to recover from  the blinded condition at the end of each of its turns, to  a maximum duration o |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/6/Text/17` | 0.708505 | In addition, a creature must attempt a Will saving  throw if it's inside the pattern when you cast it, enters the  pattern, ends its turn within the pattern, or uses a Seek or  Interact action on the |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/10/Text/28` | 0.706289 | **Success** For 1 round, the creature can't use reactions and  must attempt another save at the start of its turn; on a  failure, it is slowed 1 for that turn as it sobs uncontrollably. |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/6/Text/20` | 0.659861 | **Critical Failure** The creature is blinded for 1 minute. |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/13/Text/9` | 0.636098 | **Failure** The target is swallowed by its own shadow until the  beginning of your next turn. The target is invisible and  paralyzed, cannot experience or interact with the outside  world, and cannot |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/5` | 0.628975 | **Critical Failure** As failure, except the target babbles  incoherently. Any creature that begins its turn within  20 feet of the target must attempt a Will saving throw.  On a failure, it must use i |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/15/Text/10` | 0.626773 | **Failure** The triggering attack misses. You are undetected  to the triggering creature for 1 round. If you use a  hostile action, this effect ends after that hostile action  is completed. |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/4` | 0.624950 | **Failure** The target begins to wander aimlessly, using each  action to Step in a random direction. When it moves,  the target takes the safest route and doesn't enter  hazardous terrain. The spell h |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/43` | 0.622415 | **Critical Failure** The creature takes full damage and becomes  blinded permanently. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/5/Text/3` | 0.602291 | **Failure** The spell's duration is 1 minute, and the target must  spend at least 2 actions each turn dancing. |

### Query 150
- Text: What is the rule about **Success** The creature takes half damage.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/7/Text/4']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/1/Text/41', 'PZO22001 Starfinder Player Core 364-387::/page/7/Text/4', 'PZO22001 Starfinder Player Core 364-387::/page/4/Text/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/7/Text/4', 'PZO22001 Starfinder Player Core 364-387::/page/7/Text/3', 'PZO22001 Starfinder Player Core 364-387::/page/7/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/7/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/7/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/41` | 0.837732 | **Success** The creature takes half damage. |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/7/Text/4` | 0.837732 | **Success** The creature takes half damage. |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/4/Text/11` | 0.837732 | **Success** The creature takes half damage. |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/8/Text/13` | 0.704717 | **Success** The creature takes full damage. |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/1/Text/42` | 0.683437 | **Failure** The creature takes full damage. |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/16/Text/9` | 0.681856 | **Success** The target takes half damage. |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/63` | 0.681856 | **Success** The target takes half damage. |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/23` | 0.617611 | **Success** The target takes half damage and is stupefied 1  until the end of your current turn. |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/7/Text/3` | 0.614927 | **Critical** **Success** The creature is unaffected. |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/4/Text/12` | 0.608888 | **Failure** The creature takes full damage and is sickened 1. |

### Query 151
- Text: Lookup values for UNCOMMONCONCENTRATEEMOTIONFOCUSINCAPACITATIONMANIPULATEMENTALMYSTICSHADOW
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/13/Table/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/13/Table/3', 'PZO22001 Starfinder Player Core 364-387::/page/12/Text/41', 'PZO22001 Starfinder Player Core 364-387::/page/12/Text/35']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/13/Table/3', 'PZO22001 Starfinder Player Core 364-387::/page/13/TableCell/616', 'PZO22001 Starfinder Player Core 364-387::/page/13/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/13/TableCell/616` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/13/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/13/Table/3` | 0.973098 | UNCOMMONCONCENTRATEEMOTIONFOCUSINCAPACITATIONMANIPULATEMENTALMYSTICSHADOW |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/41` | 0.779201 | **UNCOMMON** **CONCENTRATE** **EMOTION** **FOCUS** **MANIPULATE** **MENTAL** **MYSTIC** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/35` | 0.779201 | **UNCOMMON** **CONCENTRATE** **EMOTION** **FOCUS** **MANIPULATE** **MENTAL** **MYSTIC** |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/28` | 0.737201 | **UNCOMMON** **CONCENTRATE** **EMOTION** **FOCUS** **MANIPULATE** **MENTAL** **MYSTIC** |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/58` | 0.680585 | **UNCOMMON** **CONCENTRATE** **FOCUS** **MANIPULATE** **MYSTIC** **SHADOW** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/49` | 0.680585 | **UNCOMMON** **CONCENTRATE** **FOCUS** **MANIPULATE** **MYSTIC** **SHADOW** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/16/Text/20` | 0.667148 | **UNCOMMON** **ANCHORING** **CONCENTRATE** **FOCUS** **INCAPACITATION** **MANIPULATE** **WITCHWARPER** |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/18` | 0.661798 | **UNCOMMON** **CONCENTRATE** **FOCUS** **MANIPULATE** **MYSTIC** |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/48` | 0.661798 | **UNCOMMON** **CONCENTRATE** **FOCUS** **MANIPULATE** **MYSTIC** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/11/Text/12` | 0.661798 | **UNCOMMON** **CONCENTRATE** **FOCUS** **MANIPULATE** **MYSTIC** |

### Query 152
- Text: Lookup values for D6Effect
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/14/Table/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/14/Table/25', 'PZO22001 Starfinder Player Core 364-387::/page/14/TableCell/464', 'PZO22001 Starfinder Player Core 364-387::/page/18/SectionHeader/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/14/Table/25', 'PZO22001 Starfinder Player Core 364-387::/page/14/SectionHeader/24', 'PZO22001 Starfinder Player Core 364-387::/page/14/TableCell/464']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/14/SectionHeader/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/14/TableCell/464` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/14/Table/25` | 0.880741 | D6Effect |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/14/TableCell/464` | 0.659651 | D6 |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/18/SectionHeader/10` | 0.529191 | EFFECT |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/14/TableCell/465` | 0.473510 | Effect |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/11/SectionHeader/16` | 0.448872 | **DATA DRAIN **[two-actions] **FOCUS 6** |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/491` | 0.438720 | 6 |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/498` | 0.438720 | 6 |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/434` | 0.438720 | 6 |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/436` | 0.438720 | 6 |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/438` | 0.438720 | 6 |

### Query 153
- Text: Lookup values for RankRitual2Animate object2Consecrate2Create undead4Atone4Blight4Plant growth5Call spirit5Planar servitor5Resurrect6Awaken animal6Awaken computer6Binding circle6Commune6Primal call7Collective memories7Planar displacement8Control weather
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/17/Table/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/17/Table/9', 'PZO22001 Starfinder Player Core 364-387::/page/18/Table/2', 'PZO22001 Starfinder Player Core 364-387::/page/6/Table/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/17/Table/9', 'PZO22001 Starfinder Player Core 364-387::/page/17/SectionHeader/8', 'PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/412']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/17/SectionHeader/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/412` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/17/Table/9` | 0.990310 | RankRitual2Animate object2Consecrate2Create undead4Atone4Blight4Plant growth5Call spirit5Planar servitor5Resurrect6Awaken animal6Awaken computer6Binding circle6Commune6Primal call7Collective memories7 |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/18/Table/2` | 0.629091 | Creature LevelRitual Rank RequiredCost–1 or 02150 credits12600 credits231,050 credits331,800 credits443,000 credits544,800 credits657,500 credits7510,800 credits8615,000 credits9621,000 credits10730,0 |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/6/Table/3` | 0.598444 | Spell RankMaximum Creature Level1st–12nd13rd24th35th56th77th98th119th1310th15 |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/471` | 0.511154 | Ritual Rank Required |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/17/Table/10` | 0.498685 | RankRitual9Forge Drift beacon10Wish |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/1` | 0.497086 | **SUGGESTION **[two-actions] **SPELL 4**  **CONCENTRATE** **INCAPACITATION** **LINGUISTIC** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creatu |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/0/SectionHeader/12` | 0.490861 | **SUMMON ANIMAL **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SUMMON**  **Traditions** arcane, primal  **Range **30 feet  **Duration** sustained up to 1 minute  You summon a creature |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/6/Text/2` | 0.482571 | Spells with the summon trait can conjure creatures,  typically ones with a particular trait. Such creatures can  be found in *Alien Core* and similar books. Unless noted  otherwise, the creature must |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/15` | 0.481198 | **Cast** 1 day; **Cost** UPBs or digital media, 1/5 the value on  Creature Creation Rituals (page 382); **Secondary Casters** 3 **Primary Check** Computers (master); **Secondary Checks** Lore  (any), |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/4/SectionHeader/23` | 0.480861 | **TRANSLATE **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult **Range **30 feet;** Targets** 1 creature  **Duration** 1 hour  The target can understand |

### Query 154
- Text: Lookup values for RankRitual9Forge Drift beacon10Wish
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/17/Table/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/17/Table/10', 'PZO22001 Starfinder Player Core 364-387::/page/21/SectionHeader/42', 'PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/451']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/17/Table/10', 'PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/447', 'PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/448']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/447` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/448` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/17/Table/10` | 0.933238 | RankRitual9Forge Drift beacon10Wish |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/21/SectionHeader/42` | 0.700024 | **FORGE DRIFT BEACON** **RITUAL 9** |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/17/TableCell/451` | 0.670500 | Forge Drift beacon |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/17/Table/9` | 0.519901 | RankRitual2Animate object2Consecrate2Create undead4Atone4Blight4Plant growth5Call spirit5Planar servitor5Resurrect6Awaken animal6Awaken computer6Binding circle6Commune6Primal call7Collective memories7 |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/471` | 0.466694 | Ritual Rank Required |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/24` | 0.462409 | **WISH** **RITUAL 10** |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/18/Table/2` | 0.439839 | Creature LevelRitual Rank RequiredCost–1 or 02150 credits12600 credits231,050 credits331,800 credits443,000 credits544,800 credits657,500 credits7510,800 credits8615,000 credits9621,000 credits10730,0 |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/22/Text/6` | 0.438619 | **Critical Failure** The forging fails spectacularly and causes a  glitch in Triune's code, which might have tangible effects  on the space station, like glitch gremlin infestations, a  visit from a s |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/17/SectionHeader/8` | 0.414077 | **RITUALS BY RANK** |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/22/Text/1` | 0.397526 | You consecrate a space station to the deity Triune by installing  sacred hardware and syncing it to the hyperspace plane of  the Drift. It becomes a Drift beacon that allows swifter travel  to the sur |

### Query 155
- Text: Lookup values for Creature
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/18/Table/2']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/487', 'PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/470', 'PZO22001 Starfinder Player Core 364-387::/page/18/Table/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 364-387::/page/18/Table/2', 'PZO22001 Starfinder Player Core 364-387::/page/18/SectionHeader/1', 'PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/470']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 364-387::/page/18/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/470` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 364-387::/page/6/TableCell/487` | 0.636569 | Maximum Creature Level |
| 2 | `PZO22001 Starfinder Player Core 364-387::/page/18/TableCell/470` | 0.634935 | Creature Level |
| 3 | `PZO22001 Starfinder Player Core 364-387::/page/18/Table/2` | 0.568382 | Creature LevelRitual Rank RequiredCost–1 or 02150 credits12600 credits231,050 credits331,800 credits443,000 credits544,800 credits657,500 credits7510,800 credits8615,000 credits9621,000 credits10730,0 |
| 4 | `PZO22001 Starfinder Player Core 364-387::/page/6/Table/3` | 0.498566 | Spell RankMaximum Creature Level1st–12nd13rd24th35th56th77th98th119th1310th15 |
| 5 | `PZO22001 Starfinder Player Core 364-387::/page/23/Text/28` | 0.456744 | **Range **10 feet; **Targets** 1 creature |
| 6 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/16` | 0.455786 | **Range **10 feet; **Target** 1 computer or tech creature of up to the  level on the table |
| 7 | `PZO22001 Starfinder Player Core 364-387::/page/12/Text/50` | 0.455181 | **Range **30 feet; **Target **1 creature |
| 8 | `PZO22001 Starfinder Player Core 364-387::/page/16/Text/47` | 0.444734 | **Range **120 feet; **Target** one creature or object with the tech  trait |
| 9 | `PZO22001 Starfinder Player Core 364-387::/page/19/Text/27` | 0.441945 | **Range **interplanar; **Targets** 1 extraplanar creature |
| 10 | `PZO22001 Starfinder Player Core 364-387::/page/17/Table/9` | 0.441231 | RankRitual2Animate object2Consecrate2Create undead4Atone4Blight4Plant growth5Call spirit5Planar servitor5Resurrect6Awaken animal6Awaken computer6Binding circle6Commune6Primal call7Collective memories7 |
