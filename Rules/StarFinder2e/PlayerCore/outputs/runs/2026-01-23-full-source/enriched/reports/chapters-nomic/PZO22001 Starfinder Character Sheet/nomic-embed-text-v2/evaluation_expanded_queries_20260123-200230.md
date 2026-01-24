# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `338`
- Query count: `100`
- Evaluated queries: `100`
- Coverage: `1.0000`
- MRR: `0.8061`
- hit@1: `0.7200`
- hit@3: `0.8700`
- hit@5: `0.9000`
- hit@10: `0.9800`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

### Expanded Gold Metrics
- Coverage: `1.0000`
- MRR: `0.8111`
- hit@1: `0.7300`
- hit@3: `0.8700`
- hit@5: `0.9000`
- hit@10: `0.9800`

### Expanded Gold Expansion Stats
- Queries with additions: `100`
- Avg added per query: `1.99`
- Max added: `2`
- Addition reasons:
  - graph_depth_1: `199`

### Expanded Gold Delta (Expanded - Strict)
- Coverage Δ: `0.0000`
- MRR Δ: `0.0050`
- hit@1 Δ: `0.0100`
- hit@3 Δ: `0.0000`
- hit@5 Δ: `0.0000`
- hit@10 Δ: `0.0000`

## Timings (ms)
- Embedding (chunks): `5360`
- Embedding (queries): `939`
- Evaluation (strict): `13`
- Evaluation (expanded): `13`
- Total: `10610`

### Timing Estimates (ms)
- Evaluation (strict): `10`
- Evaluation (expanded): `10`
- Total: `6319`

## Query Details
### Query 0
- Text: What is the rule about ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/Form/0']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/Form/0', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/9', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/21']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/Form/0', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.668879 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/9` | 0.603268 | Character Name = |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/21` | 0.534666 | Player Name |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/23` | 0.487440 | Gain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check. |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/12` | 0.472883 | Hero Points— |
| 6 | `PZO22001 Starfinder Character Sheet::/page/3/Form/0` | 0.469126 | Magical TraditionSpell SlotsArcane OccultPrepared CasterSpells per DayPrimal DivineSpontaneous CasterSpell Rank 12 345 67 8910Spell StatisticsSpells RemainingSpell AttackSpell DC TSpellsT + E M Key Pr |
| 7 | `PZO22001 Starfinder Character Sheet::/page/2/Form/0` | 0.451056 | Character SketchOrigin and AppearancePort of CallHome WorldAgeGender & PronounsHeightWeightAppearancePersonalityAttitudeDeity or PhilosophyEdictsAnathemaLikesDislikesCatchphrasesCampaign NotesNotesAll |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/11` | 0.406896 | Level ——— |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/Form/0` | 0.379655 | Ancestry and General FeatsClass AbilitiesInventoryLevel 1Ancestry and Heritage AbilitiesClass Feats and FeaturesHeld ItemsBulkAncestry FeatBackground Skill Feat2Skill FeatClass Feat3General FeatClass |
| 10 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/225` | 0.323674 | Spell Rank 1 |

### Query 1
- Text: Summarize ~~~~~°
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/8', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/128', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/78']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/8', 'PZO22001 Starfinder Character Sheet::/page/0/Form/0', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/Form/0` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/8` | 0.766615 | ~~~~~° |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/128` | 0.504594 | < |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/78` | 0.490046 | **→** □ r |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/147` | 0.417023 | • • • |
| 5 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/371` | 0.416235 | Page # |
| 6 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/396` | 0.416235 | Page # |
| 7 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/431` | 0.416235 | Page # |
| 8 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/336` | 0.416235 | Page # |
| 9 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/366` | 0.416235 | Page # |
| 10 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/426` | 0.416235 | Page # |

### Query 2
- Text: What is the rule about Character Name =?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/9', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/21', 'PZO22001 Starfinder Character Sheet::/page/3/TableCell/299']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/9', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/8', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/9` | 0.806861 | Character Name = |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/21` | 0.575559 | Player Name |
| 3 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/299` | 0.499570 | Name |
| 4 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/367` | 0.457570 | Name |
| 5 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/332` | 0.457570 | Name |
| 6 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/680` | 0.457570 | Name |
| 7 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/392` | 0.457570 | Name |
| 8 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/337` | 0.457570 | Name |
| 9 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/362` | 0.457570 | Name |
| 10 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/427` | 0.457570 | Name |

### Query 3
- Text: Summarize Level ———
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/11', 'PZO22001 Starfinder Character Sheet::/page/3/TableCell/520', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/283']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/11', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/9', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/11` | 0.804910 | Level ——— |
| 2 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/520` | 0.615108 | 1/2 your level rounded up |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/283` | 0.491632 | Level 1 |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/206` | 0.432466 | Expert 4 + level Master 6 + level |
| 5 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/289` | 0.415898 | Cantrip Rank 1/2 your level rounded up |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/200` | 0.383815 | Proficiency Untrained +0 Trained 2 + level |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.377382 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/26` | 0.362566 | Background —— |
| 9 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/431` | 0.355068 | Page # |
| 10 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/426` | 0.355068 | Page # |

### Query 4
- Text: Summarize Hero Points—
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/12', 'PZO22001 Starfinder Character Sheet::/page/0/Form/0', 'PZO22001 Starfinder Character Sheet::/page/3/TableCell/508']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/12', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/13', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/12` | 0.944573 | Hero Points— |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.564320 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 3 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/508` | 0.554602 | Focus Points |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/57` | 0.445761 | Hit Points Current |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/41` | 0.369884 | Attributes —— |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/9` | 0.336987 | Character Name = |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/Form/0` | 0.327304 | Ancestry and General FeatsClass AbilitiesInventoryLevel 1Ancestry and Heritage AbilitiesClass Feats and FeaturesHeld ItemsBulkAncestry FeatBackground Skill Feat2Skill FeatClass Feat3General FeatClass |
| 8 | `PZO22001 Starfinder Character Sheet::/page/2/Form/0` | 0.326814 | Character SketchOrigin and AppearancePort of CallHome WorldAgeGender & PronounsHeightWeightAppearancePersonalityAttitudeDeity or PhilosophyEdictsAnathemaLikesDislikesCatchphrasesCampaign NotesNotesAll |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/285` | 0.324351 | Class Feats and Features |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/181` | 0.317516 | Traits and Notes Weapon Proficiencies |

### Query 5
- Text: Summarize LJAK
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/13', 'PZO22001 Starfinder Character Sheet::/page/3/TableCell/266', 'PZO22001 Starfinder Character Sheet::/page/3/TableCell/267']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/13', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/14', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/13` | 0.895551 | LJAK |
| 2 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/266` | 0.426836 | L |
| 3 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/267` | 0.426836 | L |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/54` | 0.300643 | ld |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/14` | 0.287360 | ANDAK |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/188` | 0.263998 | lartial Advanced Other  T T T  JE JE JE  M M M  JL JL  L |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.245436 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 8 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/260` | 0.235276 | Rank |
| 9 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/678` | 0.235276 | Rank |
| 10 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/682` | 0.235276 | Rank |

### Query 6
- Text: Summarize ANDAK
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/14', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/89', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/14', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/13', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/14` | 0.938599 | ANDAK |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/89` | 0.371832 | Arcana ( |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/13` | 0.300315 | LJAK |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.257214 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 5 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/248` | 0.246460 | Anathema |
| 6 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/211` | 0.241301 | Arcane Occult |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/307` | 0.233410 | Bulk |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/332` | 0.233410 | Bulk |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/347` | 0.233410 | Bulk |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/287` | 0.233410 | Bulk |

### Query 7
- Text: Summarize XP
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/17', 'PZO22001 Starfinder Character Sheet::/page/0/Form/0', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/141']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/17', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/14', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/17` | 0.775309 | XP |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.430547 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/141` | 0.327748 | Mag/Ex |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/171` | 0.285748 | Mag/Ex |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/159` | 0.285748 | Mag/Ex |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/389` | 0.274522 | Skill Feat Boosts |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/339` | 0.274522 | Skill Feat Boosts |
| 8 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/520` | 0.273827 | 1/2 your level rounded up |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/Form/0` | 0.270380 | Ancestry and General FeatsClass AbilitiesInventoryLevel 1Ancestry and Heritage AbilitiesClass Feats and FeaturesHeld ItemsBulkAncestry FeatBackground Skill Feat2Skill FeatClass Feat3General FeatClass |
| 10 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/233` | 0.263885 | Spell Statistics |

### Query 8
- Text: What is the rule about Charact?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/19', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/9', 'PZO22001 Starfinder Character Sheet::/page/0/Form/0']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/19', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/17', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/19` | 0.845713 | Charact |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/9` | 0.414383 | Character Name = |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.361999 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 4 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/195` | 0.316947 | Character Sketch |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/35` | 0.307498 | Heritage and Traits |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/41` | 0.298852 | Attributes —— |
| 7 | `PZO22001 Starfinder Character Sheet::/page/2/Form/0` | 0.288343 | Character SketchOrigin and AppearancePort of CallHome WorldAgeGender & PronounsHeightWeightAppearancePersonalityAttitudeDeity or PhilosophyEdictsAnathemaLikesDislikesCatchphrasesCampaign NotesNotesAll |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/107` | 0.281169 | Crafting |
| 9 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/317` | 0.279999 | Faction |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/285` | 0.279735 | Class Feats and Features |

### Query 9
- Text: Summarize er Sheet
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/20', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/93', 'PZO22001 Starfinder Character Sheet::/page/0/Form/0']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/20', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/21', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/20` | 0.760188 | er Sheet |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/93` | 0.414730 | s Prof Item otes Spec |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.385679 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 4 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/195` | 0.336513 | Character Sketch |
| 5 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/371` | 0.319195 | Page # |
| 6 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/426` | 0.319195 | Page # |
| 7 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/366` | 0.319195 | Page # |
| 8 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/336` | 0.319195 | Page # |
| 9 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/396` | 0.319195 | Page # |
| 10 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/401` | 0.319195 | Page # |

### Query 10
- Text: Summarize Player Name
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/21', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/9', 'PZO22001 Starfinder Character Sheet::/page/3/TableCell/258']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/21', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/20', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/21` | 0.871066 | Player Name |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/9` | 0.641781 | Character Name = |
| 3 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/258` | 0.553318 | Name |
| 4 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/262` | 0.511318 | Name |
| 5 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/337` | 0.511318 | Name |
| 6 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/392` | 0.511318 | Name |
| 7 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/367` | 0.511318 | Name |
| 8 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/362` | 0.511318 | Name |
| 9 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/422` | 0.511318 | Name |
| 10 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/397` | 0.511318 | Name |

### Query 11
- Text: What is the rule about Gain 1 at the start of each session and when granted by the GM.?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/23', 'PZO22001 Starfinder Character Sheet::/page/0/Form/0', 'PZO22001 Starfinder Character Sheet::/page/3/TableCell/225']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/23', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/21', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/23` | 0.696007 | Gain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check. |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.428922 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 3 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/225` | 0.425342 | Spell Rank 1 |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/283` | 0.364110 | Level 1 |
| 5 | `PZO22001 Starfinder Character Sheet::/page/3/Form/0` | 0.336543 | Magical TraditionSpell SlotsArcane OccultPrepared CasterSpells per DayPrimal DivineSpontaneous CasterSpell Rank 12 345 67 8910Spell StatisticsSpells RemainingSpell AttackSpell DC TSpellsT + E M Key Pr |
| 6 | `PZO22001 Starfinder Character Sheet::/page/2/Form/0` | 0.275317 | Character SketchOrigin and AppearancePort of CallHome WorldAgeGender & PronounsHeightWeightAppearancePersonalityAttitudeDeity or PhilosophyEdictsAnathemaLikesDislikesCatchphrasesCampaign NotesNotesAll |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/339` | 0.264998 | Skill Feat Boosts |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/389` | 0.264998 | Skill Feat Boosts |
| 9 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/530` | 0.263047 | Refocus Spend 10 minutes to regain 1 Focus Point. Name |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/364` | 0.262268 | General Feat Boosts |

### Query 12
- Text: Summarize Ancestry ———
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/24', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/334', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/354']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/24', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/26', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/24` | 0.895114 | Ancestry ——— |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/354` | 0.645521 | Ancestry Feat |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/334` | 0.645521 | Ancestry Feat |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/289` | 0.603521 | Ancestry Feat |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/374` | 0.603521 | Ancestry Feat |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/279` | 0.586677 | Ancestry and General Feats |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/284` | 0.585121 | Ancestry and Heritage Abilities |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/314` | 0.549948 | Ancestry Feat Boosts |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/Form/0` | 0.463863 | Ancestry and General FeatsClass AbilitiesInventoryLevel 1Ancestry and Heritage AbilitiesClass Feats and FeaturesHeld ItemsBulkAncestry FeatBackground Skill Feat2Skill FeatClass Feat3General FeatClass |
| 10 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/198` | 0.394203 | Origin and Appearance |

### Query 13
- Text: What is the rule about Background ——?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/26', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/37', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/294']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/26', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/28', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/26` | 0.734290 | Background —— |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/37` | 0.595586 | Background Notes |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/294` | 0.509343 | Background Skill Feat |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/75` | 0.326517 | Conditions |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/24` | 0.311465 | Ancestry ——— |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/11` | 0.293990 | Level ——— |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.290429 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/41` | 0.284724 | Attributes —— |
| 9 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/8` | 0.275732 | ~~~~~° |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/12` | 0.264489 | Hero Points— |

### Query 14
- Text: Summarize Spend All to avoid death.
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/28', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/197', 'PZO22001 Starfinder Character Sheet::/page/0/Form/0']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/28', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/26', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/35']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/35` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/28` | 0.988843 | Spend All to avoid death. |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/197` | 0.400248 | Survival |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.375290 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 4 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/301` | 0.310046 | Actions Prep |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/64` | 0.297316 | Dying ( ) ( ) ( ) Wounded |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/23` | 0.293253 | Gain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check. |
| 7 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/257` | 0.282105 | + |
| 8 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/265` | 0.276558 | Prep |
| 9 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/261` | 0.276558 | Prep |
| 10 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/497` | 0.256005 | Focus Spells |

### Query 15
- Text: What is the rule about Heritage and Traits?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/35']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/35', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/284', 'PZO22001 Starfinder Character Sheet::/page/2/TableCell/429']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/35', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/28', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/36']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/36` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/35` | 0.881655 | Heritage and Traits |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/284` | 0.660579 | Ancestry and Heritage Abilities |
| 3 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/429` | 0.647860 | Traits |
| 4 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/394` | 0.605860 | Traits |
| 5 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/339` | 0.605860 | Traits |
| 6 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/369` | 0.605860 | Traits |
| 7 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/424` | 0.605860 | Traits |
| 8 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/364` | 0.605860 | Traits |
| 9 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/334` | 0.605860 | Traits |
| 10 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/399` | 0.605860 | Traits |

### Query 16
- Text: Summarize Size
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/36']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/36', 'PZO22001 Starfinder Character Sheet::/page/2/TableCell/214', 'PZO22001 Starfinder Character Sheet::/page/2/TableCell/213']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/36', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/37', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/35']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/37` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/35` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/36` | 0.748473 | Size |
| 2 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/214` | 0.407338 | Weight |
| 3 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/213` | 0.401284 | Height |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/371` | 0.344535 | Bulk Encumbered Bulk 5 + Str Maximum Bulk 10 + Str |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/140` | 0.342011 | Range (ft.) |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/170` | 0.342011 | Range (ft.) |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/158` | 0.342011 | Range (ft.) |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/70` | 0.322740 | S |
| 9 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/233` | 0.313869 | Spell Statistics |
| 10 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/266` | 0.298320 | L |

### Query 17
- Text: What is the rule about Background Notes?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/37', 'PZO22001 Starfinder Character Sheet::/page/2/TableCell/292', 'PZO22001 Starfinder Character Sheet::/page/2/TableCell/282']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/37', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/39', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/36']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/39` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/36` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/37` | 0.834526 | Background Notes |
| 2 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/292` | 0.534605 | Notes |
| 3 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/282` | 0.527462 | Campaign Notes |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/26` | 0.461710 | Background —— |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/151` | 0.433379 | Traits and Notes |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/133` | 0.433379 | Traits and Notes |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/163` | 0.433379 | Traits and Notes |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/294` | 0.411706 | Background Skill Feat |
| 9 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/39` | 0.405809 | Class Notes |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/74` | 0.372545 | tection Notes |

### Query 18
- Text: Summarize Class Notes
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/39', 'PZO22001 Starfinder Character Sheet::/page/2/TableCell/292', 'PZO22001 Starfinder Character Sheet::/page/2/TableCell/282']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/39', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/37', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/41']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/37` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/41` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/39` | 0.874224 | Class Notes |
| 2 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/292` | 0.623026 | Notes |
| 3 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/282` | 0.557442 | Campaign Notes |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/37` | 0.493613 | Background Notes |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/345` | 0.476516 | Class Feature |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/375` | 0.476516 | Class Feature |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/315` | 0.476516 | Class Feature |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/385` | 0.476516 | Class Feature |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/365` | 0.476516 | Class Feature |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/355` | 0.476516 | Class Feature |

### Query 19
- Text: Summarize Attributes ——
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/41', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/285', 'PZO22001 Starfinder Character Sheet::/page/0/Form/0']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/41', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/39', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/47']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/39` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/47` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/41` | 0.869988 | Attributes —— |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/285` | 0.489050 | Class Feats and Features |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.446504 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/Form/0` | 0.393229 | Ancestry and General FeatsClass AbilitiesInventoryLevel 1Ancestry and Heritage AbilitiesClass Feats and FeaturesHeld ItemsBulkAncestry FeatBackground Skill Feat2Skill FeatClass Feat3General FeatClass |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/163` | 0.385281 | Traits and Notes |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/151` | 0.385281 | Traits and Notes |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/133` | 0.385281 | Traits and Notes |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/26` | 0.377949 | Background —— |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/284` | 0.369326 | Ancestry and Heritage Abilities |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/279` | 0.367087 | Ancestry and General Feats |

### Query 20
- Text: Summarize Strength
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/47']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/47', 'PZO22001 Starfinder Character Sheet::/page/2/TableCell/214', 'PZO22001 Starfinder Character Sheet::/page/0/Form/0']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/47', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/48', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/41']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/48` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/41` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/47` | 0.517205 | Strength OPartial Boost |
| 2 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/214` | 0.445086 | Weight |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.436236 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/77` | 0.360924 | Skills — |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/55` | 0.359705 | Fortitude Refle |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/60` | 0.358088 | Hardness Max HP BT HP Armor Proficiencies |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/Form/0` | 0.327617 | Ancestry and General FeatsClass AbilitiesInventoryLevel 1Ancestry and Heritage AbilitiesClass Feats and FeaturesHeld ItemsBulkAncestry FeatBackground Skill Feat2Skill FeatClass Feat3General FeatClass |
| 8 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/233` | 0.327060 | Spell Statistics |
| 9 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/36` | 0.324705 | Size |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/167` | 0.324071 | Performance |

### Query 21
- Text: Summarize **Dexterity**
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/48']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/48', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/113', 'PZO22001 Starfinder Character Sheet::/page/0/Form/0']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/48', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/49', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/47']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/47` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/48` | 0.637341 | **Dexterity** OPartial Boost |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/113` | 0.394154 | Deception |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.377998 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/191` | 0.330297 | Stealth |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/193` | 0.318137 | Class DC —— |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/128` | 0.303778 | < |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/184` | 0.301658 | Critical Specializations |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/8` | 0.295975 | ~~~~~° |
| 9 | `PZO22001 Starfinder Character Sheet::/page/2/Form/0` | 0.293288 | Character SketchOrigin and AppearancePort of CallHome WorldAgeGender & PronounsHeightWeightAppearancePersonalityAttitudeDeity or PhilosophyEdictsAnathemaLikesDislikesCatchphrasesCampaign NotesNotesAll |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/161` | 0.290298 | Occultism ( |

### Query 22
- Text: Summarize Constitution
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/49']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/49', 'PZO22001 Starfinder Character Sheet::/page/2/TableCell/431', 'PZO22001 Starfinder Character Sheet::/page/2/TableCell/371']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/49', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/48', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/50']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/48` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/50` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/49` | 0.461896 | Constitution OPartial Boost |
| 2 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/431` | 0.320988 | Page # |
| 3 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/371` | 0.320988 | Page # |
| 4 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/396` | 0.278988 | Page # |
| 5 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/426` | 0.278988 | Page # |
| 6 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/336` | 0.278988 | Page # |
| 7 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/366` | 0.278988 | Page # |
| 8 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/401` | 0.278988 | Page # |
| 9 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/341` | 0.278988 | Page # |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/185` | 0.268243 | Society |

### Query 23
- Text: Summarize Intelligence
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/50']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/50', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/77', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/281']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/50', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/49', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/51']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/51` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/50` | 0.468234 | Intelligence OPartial Boost |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/77` | 0.376018 | Skills — |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/281` | 0.367816 | Inventory |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.317642 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 5 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/233` | 0.316837 | Spell Statistics |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/Form/0` | 0.315881 | Ancestry and General FeatsClass AbilitiesInventoryLevel 1Ancestry and Heritage AbilitiesClass Feats and FeaturesHeld ItemsBulkAncestry FeatBackground Skill Feat2Skill FeatClass Feat3General FeatClass |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/81` | 0.306648 | ion — Spo |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/108` | 0.300299 | TE + + Int Prof Item |
| 9 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/90` | 0.300299 | TE + + Int Prof Item |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/162` | 0.300299 | TE + + Int Prof Item |

### Query 24
- Text: Summarize Wisdom
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/51']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/51', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/156', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/180']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/51', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/52', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/50']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/52` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/50` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/51` | 0.454877 | Wisdom OPartial Boost |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/156` | 0.420819 | Wis Prof Item |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/180` | 0.420819 | Wis Prof Item |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/77` | 0.326141 | Skills — |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/150` | 0.324324 | T + + H Wis Prof Item |
| 6 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/245` | 0.313944 | Edicts |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/Form/0` | 0.268346 | Ancestry and General FeatsClass AbilitiesInventoryLevel 1Ancestry and Heritage AbilitiesClass Feats and FeaturesHeld ItemsBulkAncestry FeatBackground Skill Feat2Skill FeatClass Feat3General FeatClass |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.268202 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 9 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/181` | 0.268147 | Traits and Notes Weapon Proficiencies |
| 10 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/233` | 0.267849 | Spell Statistics |

### Query 25
- Text: Summarize Charisma
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/52']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/52', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/19', 'PZO22001 Starfinder Character Sheet::/page/2/TableCell/228']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/52', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/53', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/51']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/53` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/51` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/52` | 0.596609 | Charisma OPartial Boost |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/19` | 0.492686 | Charact |
| 3 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/228` | 0.390935 | Personality |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/9` | 0.334991 | Character Name = |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.324950 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/161` | 0.302411 | Occultism ( |
| 7 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/195` | 0.296669 | Character Sketch |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/35` | 0.295695 | Heritage and Traits |
| 9 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/132` | 0.295255 | Cha Prof Item |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/168` | 0.295255 | Cha Prof Item |

### Query 26
- Text: What is the rule about Armor Class Shiel?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/53']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/53', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/97', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/85']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/53', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/52', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/54']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/52` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/54` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/53` | 0.890954 | Armor Class Shiel |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/97` | 0.459979 | Armor |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/85` | 0.459979 | Armor |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/205` | 0.389877 | 10 · · ·  Armor Base Key Prof Item |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/71` | 0.389427 | Base Dex* Prof Item * Use armor's Dex cap if lower |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/365` | 0.369541 | Class Feature |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/375` | 0.369541 | Class Feature |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/385` | 0.369541 | Class Feature |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/355` | 0.369541 | Class Feature |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/305` | 0.369541 | Class Feature |

### Query 27
- Text: Summarize ld
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/54']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/54', 'PZO22001 Starfinder Character Sheet::/page/3/TableCell/266', 'PZO22001 Starfinder Character Sheet::/page/3/TableCell/267']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/54', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/53', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/55']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/53` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/55` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/54` | 0.752861 | ld |
| 2 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/266` | 0.472406 | L |
| 3 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/267` | 0.472406 | L |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/13` | 0.278016 | LJAK |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/188` | 0.271559 | lartial Advanced Other  T T T  JE JE JE  M M M  JL JL  L |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.256421 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/366` | 0.252882 | Bulk Light Items 10 light Bulk items = 1 Bulk |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/137` | 0.251750 | Lore |
| 9 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/131` | 0.251750 | Lore |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/87` | 0.250149 | + + |

### Query 28
- Text: Summarize Fortitude Refle
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/55']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/55', 'PZO22001 Starfinder Character Sheet::/page/0/Form/0', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/379']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/55', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/56', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/54']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/56` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/54` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/55` | 0.976850 | Fortitude Refle |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.402882 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/379` | 0.398318 | Skill Feat |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/329` | 0.356318 | Skill Feat |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/369` | 0.356318 | Skill Feat |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/349` | 0.356318 | Skill Feat |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/309` | 0.356318 | Skill Feat |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/299` | 0.356318 | Skill Feat |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/359` | 0.356318 | Skill Feat |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/319` | 0.356318 | Skill Feat |

### Query 29
- Text: Summarize ex Will
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/56']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/56', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/141', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/159']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/56', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/55', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/57']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/55` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/57` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/56` | 0.824212 | ex Will |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/141` | 0.451505 | Mag/Ex |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/159` | 0.451505 | Mag/Ex |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/171` | 0.409505 | Mag/Ex |
| 5 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/233` | 0.298050 | Spell Statistics |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/156` | 0.288679 | Wis Prof Item |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/180` | 0.288679 | Wis Prof Item |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/150` | 0.274041 | T + + H Wis Prof Item |
| 9 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.263498 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 10 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/520` | 0.258338 | 1/2 your level rounded up |

### Query 30
- Text: What is the rule about Hit Points Current?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/57']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/57', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/12', 'PZO22001 Starfinder Character Sheet::/page/3/TableCell/508']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/57', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/56', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/58']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/56` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/58` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/57` | 0.864872 | Hit Points Current |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/12` | 0.478814 | Hero Points— |
| 3 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/508` | 0.468306 | Focus Points |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.303500 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 5 | `PZO22001 Starfinder Character Sheet::/page/3/Form/0` | 0.259781 | Magical TraditionSpell SlotsArcane OccultPrepared CasterSpells per DayPrimal DivineSpontaneous CasterSpell Rank 12 345 67 8910Spell StatisticsSpells RemainingSpell AttackSpell DC TSpellsT + E M Key Pr |
| 6 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/519` | 0.254027 | Focus Pool Equals the number of focus spells you have (maximum 3). |
| 7 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/275` | 0.251563 | Catchphrases |
| 8 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/292` | 0.246256 | Notes |
| 9 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/530` | 0.239788 | Refocus Spend 10 minutes to regain 1 Focus Point. Name |
| 10 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/497` | 0.238672 | Focus Spells |

### Query 31
- Text: Summarize HP Temporary HP
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/58']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/58', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/60', 'PZO22001 Starfinder Character Sheet::/page/0/Form/0']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/58', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/59', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/57']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/59` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/57` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/58` | 0.986583 | HP Temporary HP |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/60` | 0.522618 | Hardness Max HP BT HP Armor Proficiencies |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.397895 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/150` | 0.287309 | T + + H Wis Prof Item |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/57` | 0.280150 | Hit Points Current |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/20` | 0.266693 | er Sheet |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/35` | 0.263962 | Heritage and Traits |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/101` | 0.261203 | Computers |
| 9 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/429` | 0.242636 | Traits |
| 10 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/369` | 0.242636 | Traits |

### Query 32
- Text: Summarize 4 PE
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/59']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/59', 'PZO22001 Starfinder Character Sheet::/page/3/TableCell/228', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/308']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/59', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/60', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/58']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/60` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/58` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/59` | 0.885285 | 4 PE |
| 2 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/228` | 0.640827 | 4 |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/308` | 0.640827 | 4 |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/323` | 0.349055 | 7 |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/313` | 0.340734 | 5 |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/303` | 0.339961 | 3 |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/318` | 0.338430 | 6 |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/298` | 0.333627 | 2 |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/328` | 0.324668 | 8 |
| 10 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/230` | 0.306739 | 7 8 |

### Query 33
- Text: Summarize Hardness Max HP BT HP
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/60']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/60', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/58', 'PZO22001 Starfinder Character Sheet::/page/0/Form/0']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/60', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/63', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/59']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/63` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/59` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/60` | 0.874394 | Hardness Max HP BT HP Armor Proficiencies |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/58` | 0.530077 | HP Temporary HP |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.394097 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/371` | 0.293174 | Bulk Encumbered Bulk 5 + Str Maximum Bulk 10 + Str |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/142` | 0.289187 | p Damage |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/160` | 0.289187 | p Damage |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/172` | 0.289187 | p Damage |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/47` | 0.276358 | Strength OPartial Boost |
| 9 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/214` | 0.268938 | Weight |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/12` | 0.259790 | Hero Points— |

### Query 34
- Text: Summarize \bigcirc
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/63']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/63', 'PZO22001 Starfinder Character Sheet::/page/2/TableCell/255', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/371']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/63', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/60', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/64']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/60` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/64` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/63` | 0.976704 | \bigcirc |
| 2 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/255` | 0.317987 | Likes |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/371` | 0.314112 | Bulk Encumbered Bulk 5 + Str Maximum Bulk 10 + Str |
| 4 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/257` | 0.263573 | + |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/36` | 0.262003 | Size |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/128` | 0.256919 | < |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/Form/0` | 0.247593 | Ancestry and General FeatsClass AbilitiesInventoryLevel 1Ancestry and Heritage AbilitiesClass Feats and FeaturesHeld ItemsBulkAncestry FeatBackground Skill Feat2Skill FeatClass Feat3General FeatClass |
| 8 | `PZO22001 Starfinder Character Sheet::/page/2/Form/0` | 0.245337 | Character SketchOrigin and AppearancePort of CallHome WorldAgeGender & PronounsHeightWeightAppearancePersonalityAttitudeDeity or PhilosophyEdictsAnathemaLikesDislikesCatchphrasesCampaign NotesNotesAll |
| 9 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/371` | 0.242711 | Page # |
| 10 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/431` | 0.242710 | Page # |

### Query 35
- Text: Summarize Dying ( ) ( ) ( ) Wounded
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/64']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/64', 'PZO22001 Starfinder Character Sheet::/page/0/Form/0', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/128']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/64', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/63', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/65']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/63` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/65` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/64` | 0.994747 | Dying ( ) ( ) ( ) Wounded |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.418247 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/128` | 0.399936 | < |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/87` | 0.357739 | + + |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/28` | 0.357311 | Spend All to avoid death. |
| 6 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/257` | 0.350870 | + |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/78` | 0.349404 | **→** □ r |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/124` | 0.341214 | Damage |
| 9 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/112` | 0.341214 | Damage |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/65` | 0.328930 | 10 · · · |

### Query 36
- Text: Summarize 10 · · ·
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/65']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/65', 'PZO22001 Starfinder Character Sheet::/page/3/TableCell/232', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/338']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/65', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/66', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/64']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/66` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/64` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/65` | 0.767045 | 10 · · · |
| 2 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/232` | 0.680523 | 10 |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/338` | 0.680523 | 10 |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/343` | 0.461414 | 11 |
| 5 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/231` | 0.451064 | 9 |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/366` | 0.441959 | Bulk Light Items 10 light Bulk items = 1 Bulk |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/333` | 0.439064 | 9 |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/328` | 0.410280 | 8 |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/318` | 0.404315 | 6 |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/368` | 0.387665 | 16 |

### Query 37
- Text: Summarize Unarmored Light Medium Heavy
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/66']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/66', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/97', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/85']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/66', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/67', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/65']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/67` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/65` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/66` | 0.992483 | Unarmored Light Medium Heavy |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/97` | 0.397106 | Armor |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/85` | 0.397106 | Armor |
| 4 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/214` | 0.326998 | Weight |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/366` | 0.307598 | Bulk Light Items 10 light Bulk items = 1 Bulk |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.289053 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 7 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/266` | 0.286960 | L |
| 8 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/267` | 0.286960 | L |
| 9 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/60` | 0.283793 | Hardness Max HP BT HP Armor Proficiencies |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/169` | 0.283268 | Weapon |

### Query 38
- Text: Summarize Con Prof Item Dex Prof
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/67']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/67', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/84', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/192']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/67', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/66', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/69']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/66` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/69` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/67` | 0.963242 | Con Prof Item Dex Prof |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/84` | 0.909998 | Dex Prof Item |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/192` | 0.909998 | Dex Prof Item |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/153` | 0.867998 | Dex Prof Item |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/165` | 0.867998 | Dex Prof Item |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/177` | 0.840332 | Dex Prof Item / |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/174` | 0.804971 | T E + + Dex Prof Item |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/71` | 0.657995 | Base Dex* Prof Item * Use armor's Dex cap if lower |
| 9 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/135` | 0.635126 | Str Prof Item |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/96` | 0.635126 | Str Prof Item |

### Query 39
- Text: Summarize Resistances and Immunities
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/69']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/69', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/197', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/181']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/69', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/67', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/70']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/67` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/70` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/69` | 0.973733 | Resistances and Immunities |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/197` | 0.404807 | Survival |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/181` | 0.385916 | Traits and Notes Weapon Proficiencies |
| 4 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/327` | 0.315466 | Free Actions and Reactions |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.313100 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/280` | 0.312854 | Class Abilities |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/184` | 0.302979 | Critical Specializations |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/284` | 0.297195 | Ancestry and Heritage Abilities |
| 9 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/121` | 0.296101 | Traits and Notes  Weapon |
| 10 | `PZO22001 Starfinder Character Sheet::/page/2/Form/0` | 0.291171 | Character SketchOrigin and AppearancePort of CallHome WorldAgeGender & PronounsHeightWeightAppearancePersonalityAttitudeDeity or PhilosophyEdictsAnathemaLikesDislikesCatchphrasesCampaign NotesNotesAll |

### Query 40
- Text: Summarize S
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/70']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/70', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/185', 'PZO22001 Starfinder Character Sheet::/page/2/TableCell/396']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/70', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/71', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/69']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/71` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/69` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/70` | 0.753265 | S |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/185` | 0.374480 | Society |
| 3 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/396` | 0.343699 | Page # |
| 4 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/371` | 0.301699 | Page # |
| 5 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/431` | 0.301699 | Page # |
| 6 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/426` | 0.301699 | Page # |
| 7 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/401` | 0.301699 | Page # |
| 8 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/336` | 0.301699 | Page # |
| 9 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/366` | 0.301699 | Page # |
| 10 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/341` | 0.301699 | Page # |

### Query 41
- Text: Summarize Base Dex* Prof Item
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/71']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/84', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/192', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/153']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/71', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/73', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/70']
- Expanded expected found: `True`
- Expanded expected rank: `8`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/73` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/70` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/84` | 0.818509 | Dex Prof Item |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/192` | 0.818509 | Dex Prof Item |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/153` | 0.818509 | Dex Prof Item |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/165` | 0.776509 | Dex Prof Item |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/177` | 0.769758 | Dex Prof Item / |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/67` | 0.764484 | Con Prof Item Dex Prof |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/174` | 0.734808 | T E + + Dex Prof Item |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/71` | 0.705908 | Base Dex* Prof Item * Use armor's Dex cap if lower |
| 9 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/135` | 0.546297 | Str Prof Item |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/96` | 0.546297 | Str Prof Item |

### Query 42
- Text: Summarize Defense & Environmental Pro
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/73']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/73', 'PZO22001 Starfinder Character Sheet::/page/0/Form/0', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/192']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/73', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/71', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/74']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/71` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/74` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/73` | 0.946073 | Defense & Environmental Pro |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.374278 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/192` | 0.362688 | Dex Prof Item |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/84` | 0.320688 | Dex Prof Item |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/165` | 0.320688 | Dex Prof Item |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/153` | 0.320688 | Dex Prof Item |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/177` | 0.314809 | Dex Prof Item / |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/155` | 0.308104 | Nature |
| 9 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/322` | 0.306044 | Actions and Activities |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/174` | 0.300624 | T E + + Dex Prof Item |

### Query 43
- Text: Summarize tection Notes
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/74']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/74', 'PZO22001 Starfinder Character Sheet::/page/2/TableCell/292', 'PZO22001 Starfinder Character Sheet::/page/2/TableCell/282']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/74', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/73', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/75']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/73` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/75` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/74` | 0.884529 | tection Notes |
| 2 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/292` | 0.620741 | Notes |
| 3 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/282` | 0.541134 | Campaign Notes |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/39` | 0.489454 | Class Notes |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/37` | 0.470966 | Background Notes |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/133` | 0.464726 | Traits and Notes |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/163` | 0.464726 | Traits and Notes |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/151` | 0.464726 | Traits and Notes |
| 9 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/121` | 0.375420 | Traits and Notes  Weapon |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/93` | 0.363016 | s Prof Item otes Spec |

### Query 44
- Text: Summarize Conditions
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/75']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/75', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/37', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/41']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/75', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/77', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/74']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/77` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/74` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/75` | 0.736828 | Conditions |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/37` | 0.360988 | Background Notes |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/41` | 0.337423 | Attributes —— |
| 4 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/292` | 0.272996 | Notes |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/184` | 0.264167 | Critical Specializations |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/26` | 0.258799 | Background —— |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.256825 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/Form/0` | 0.256270 | Ancestry and General FeatsClass AbilitiesInventoryLevel 1Ancestry and Heritage AbilitiesClass Feats and FeaturesHeld ItemsBulkAncestry FeatBackground Skill Feat2Skill FeatClass Feat3General FeatClass |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/285` | 0.254078 | Class Feats and Features |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/87` | 0.251393 | + + |

### Query 45
- Text: What is the rule about Skills —?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/77']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/77', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/319', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/309']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/77', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/78', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/75']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/78` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/75` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/77` | 0.820056 | Skills — |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/319` | 0.531288 | Skill Feat |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/309` | 0.531288 | Skill Feat |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/329` | 0.489288 | Skill Feat |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/359` | 0.489288 | Skill Feat |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/379` | 0.489288 | Skill Feat |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/299` | 0.489288 | Skill Feat |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/349` | 0.489288 | Skill Feat |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/369` | 0.489288 | Skill Feat |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/294` | 0.461580 | Background Skill Feat |

### Query 46
- Text: Summarize **→** □ r
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/78']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/78', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/8', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/147']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/78', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/77', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/79']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/77` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/79` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/78` | 0.943922 | **→** □ r |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/8` | 0.544165 | ~~~~~° |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/147` | 0.529713 | • • • |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/128` | 0.474016 | < |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/87` | 0.414686 | + + |
| 6 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/257` | 0.404208 | + |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/65` | 0.366823 | 10 · · · |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.365973 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 9 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/26` | 0.362782 | Background —— |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/9` | 0.352108 | Character Name = |

### Query 47
- Text: Summarize Languages —
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/79']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/79', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/77', 'PZO22001 Starfinder Character Sheet::/page/0/Form/0']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/79', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/80', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/78']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/80` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/78` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/79` | 0.807535 | Languages — |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/77` | 0.374693 | Skills — |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.353555 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 4 | `PZO22001 Starfinder Character Sheet::/page/2/Form/0` | 0.304813 | Character SketchOrigin and AppearancePort of CallHome WorldAgeGender & PronounsHeightWeightAppearancePersonalityAttitudeDeity or PhilosophyEdictsAnathemaLikesDislikesCatchphrasesCampaign NotesNotesAll |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/147` | 0.295016 | • • • |
| 6 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/275` | 0.294159 | Catchphrases |
| 7 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/257` | 0.292445 | + |
| 8 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/233` | 0.289074 | Spell Statistics |
| 9 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/26` | 0.288964 | Background —— |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/87` | 0.282358 | + + |

### Query 48
- Text: Summarize Percept
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/80']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/80', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/113', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/167']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/80', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/79', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/81']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/79` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/81` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/80` | 0.848590 | Percept |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/113` | 0.441824 | Deception |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/167` | 0.383513 | Performance |
| 4 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/342` | 0.327458 | Effects |
| 5 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/447` | 0.327458 | Effects |
| 6 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/417` | 0.327458 | Effects |
| 7 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/402` | 0.327458 | Effects |
| 8 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/372` | 0.327458 | Effects |
| 9 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/387` | 0.327458 | Effects |
| 10 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/432` | 0.327458 | Effects |

### Query 49
- Text: Summarize ion — Spo
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/81']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/81', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/70', 'PZO22001 Starfinder Character Sheet::/page/0/Form/0']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/81', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/80', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/83']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/80` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/83` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/81` | 0.921982 | ion — Spo |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/70` | 0.392847 | S |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.387998 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 4 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/233` | 0.322567 | Spell Statistics |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/Form/0` | 0.298802 | Ancestry and General FeatsClass AbilitiesInventoryLevel 1Ancestry and Heritage AbilitiesClass Feats and FeaturesHeld ItemsBulkAncestry FeatBackground Skill Feat2Skill FeatClass Feat3General FeatClass |
| 6 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/257` | 0.294935 | + |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/87` | 0.292011 | + + |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/93` | 0.283800 | s Prof Item otes Spec |
| 9 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/162` | 0.281524 | TE + + Int Prof Item |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/90` | 0.281524 | TE + + Int Prof Item |

### Query 50
- Text: What is the rule about Acrobatics?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/83']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/83', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/95', 'PZO22001 Starfinder Character Sheet::/page/3/TableCell/211']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/83', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/84', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/81']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/84` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/81` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/83` | 0.834082 | Acrobatics |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/95` | 0.473140 | Athletics |
| 3 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/211` | 0.344082 | Arcane Occult |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/107` | 0.276683 | Crafting |
| 5 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/264` | 0.276053 | Actions Rank |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/161` | 0.270184 | Occultism ( |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.266221 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 8 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/200` | 0.265725 | Magical Tradition |
| 9 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/665` | 0.264699 | Rituals |
| 10 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/423` | 0.263944 | Actions |

### Query 51
- Text: Summarize Dex Prof Item
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/84']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/192', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/84', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/165']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/84', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/83', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/85']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/83` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/85` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/192` | 0.947733 | Dex Prof Item |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/84` | 0.947733 | Dex Prof Item |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/165` | 0.947733 | Dex Prof Item |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/153` | 0.905733 | Dex Prof Item |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/67` | 0.881632 | Con Prof Item Dex Prof |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/177` | 0.873667 | Dex Prof Item / |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/174` | 0.812533 | T E + + Dex Prof Item |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/71` | 0.646574 | Base Dex* Prof Item * Use armor's Dex cap if lower |
| 9 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/135` | 0.593275 | Str Prof Item |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/117` | 0.593275 | Str Prof Item |

### Query 52
- Text: Summarize Armor
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/85']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/85', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/97', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/205']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/85', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/84', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/87']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/84` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/87` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/85` | 0.850262 | Armor |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/97` | 0.850262 | Armor |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/205` | 0.524360 | 10 · · ·  Armor Base Key Prof Item |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/71` | 0.463168 | Base Dex* Prof Item * Use armor's Dex cap if lower |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/60` | 0.422653 | Hardness Max HP BT HP Armor Proficiencies |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/53` | 0.411664 | Armor Class Shiel |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.400556 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/66` | 0.359444 | Unarmored Light Medium Heavy |
| 9 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/169` | 0.324104 | Weapon |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/157` | 0.324104 | Weapon |

### Query 53
- Text: Summarize + +
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/87']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/87', 'PZO22001 Starfinder Character Sheet::/page/3/TableCell/257', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/150']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/87', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/88', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/85']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/88` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/85` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/87` | 0.725023 | + + |
| 2 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/257` | 0.686054 | + |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/150` | 0.442627 | T + + H Wis Prof Item |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/128` | 0.362807 | < |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/108` | 0.362778 | TE + + Int Prof Item |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/90` | 0.362778 | TE + + Int Prof Item |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/162` | 0.362778 | TE + + Int Prof Item |
| 8 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/371` | 0.362060 | Page # |
| 9 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/426` | 0.362060 | Page # |
| 10 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/396` | 0.362060 | Page # |

### Query 54
- Text: Summarize feet
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/88']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/88', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/384', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/344']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/88', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/89', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/87']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/89` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/87` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/88` | 0.777833 | feet |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/384` | 0.529294 | General Feat |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/344` | 0.529294 | General Feat |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/304` | 0.487294 | General Feat |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/324` | 0.487294 | General Feat |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/320` | 0.485437 | Class Feat |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/360` | 0.485437 | Class Feat |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/300` | 0.485437 | Class Feat |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/390` | 0.485437 | Class Feat |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/370` | 0.485437 | Class Feat |

### Query 55
- Text: Summarize Arcana (
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/89']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/89', 'PZO22001 Starfinder Character Sheet::/page/3/TableCell/211', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/195']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/89', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/88', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/90']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/88` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/90` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/89` | 0.905184 | Arcana ( |
| 2 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/211` | 0.575315 | Arcane Occult |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/195` | 0.420665 | Action Icana |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.378108 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/161` | 0.288417 | Occultism ( |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/83` | 0.278826 | Acrobatics |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/Form/0` | 0.266616 | Ancestry and General FeatsClass AbilitiesInventoryLevel 1Ancestry and Heritage AbilitiesClass Feats and FeaturesHeld ItemsBulkAncestry FeatBackground Skill Feat2Skill FeatClass Feat3General FeatClass |
| 8 | `PZO22001 Starfinder Character Sheet::/page/3/Form/0` | 0.265104 | Magical TraditionSpell SlotsArcane OccultPrepared CasterSpells per DayPrimal DivineSpontaneous CasterSpell Rank 12 345 67 8910Spell StatisticsSpells RemainingSpell AttackSpell DC TSpellsT + E M Key Pr |
| 9 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/14` | 0.258679 | ANDAK |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/97` | 0.256789 | Armor |

### Query 56
- Text: Summarize TE + + Int Prof Item
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/90']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/90', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/108', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/162']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/90', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/92', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/89']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/92` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/89` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/90` | 0.966378 | TE + + Int Prof Item |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/108` | 0.966378 | TE + + Int Prof Item |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/162` | 0.966378 | TE + + Int Prof Item |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/174` | 0.718506 | T E + + Dex Prof Item |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/114` | 0.706784 | TE + + Cha Prof Item |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/186` | 0.691417 | Int Prof Item |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/138` | 0.691417 | Int Prof Item |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/102` | 0.691417 | Int Prof Item |
| 9 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/144` | 0.691417 | Int Prof Item |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/150` | 0.671687 | T + + H Wis Prof Item |

### Query 57
- Text: Summarize Senses and No
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/92']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/92', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/163', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/151']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/92', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/93', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/90']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/93` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/90` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/92` | 0.932293 | Senses and No |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/151` | 0.441004 | Traits and Notes |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/163` | 0.441004 | Traits and Notes |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/133` | 0.399004 | Traits and Notes |
| 5 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/292` | 0.387162 | Notes |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/121` | 0.329325 | Traits and Notes  Weapon |
| 7 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/327` | 0.319209 | Free Actions and Reactions |
| 8 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/282` | 0.312750 | Campaign Notes |
| 9 | `PZO22001 Starfinder Character Sheet::/page/2/Form/0` | 0.312464 | Character SketchOrigin and AppearancePort of CallHome WorldAgeGender & PronounsHeightWeightAppearancePersonalityAttitudeDeity or PhilosophyEdictsAnathemaLikesDislikesCatchphrasesCampaign NotesNotesAll |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/39` | 0.308848 | Class Notes |

### Query 58
- Text: Summarize s Prof Item
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/93']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/93', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/102', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/138']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/93', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/94', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/92']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/94` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/92` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/93` | 0.745859 | s Prof Item otes Spec |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/102` | 0.717883 | Int Prof Item |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/138` | 0.717883 | Int Prof Item |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/144` | 0.675883 | Int Prof Item |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/186` | 0.675883 | Int Prof Item |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/96` | 0.666089 | Str Prof Item |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/117` | 0.666089 | Str Prof Item |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/135` | 0.666089 | Str Prof Item |
| 9 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/156` | 0.650753 | Wis Prof Item |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/180` | 0.650753 | Wis Prof Item |

### Query 59
- Text: Summarize ial Movement
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/94']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/94', 'PZO22001 Starfinder Character Sheet::/page/2/TableCell/423', 'PZO22001 Starfinder Character Sheet::/page/2/TableCell/393']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/94', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/93', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/95']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/93` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/95` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/94` | 0.909492 | ial Movement |
| 2 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/423` | 0.382915 | Actions |
| 3 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/393` | 0.382915 | Actions |
| 4 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/363` | 0.340915 | Actions |
| 5 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/532` | 0.340915 | Actions |
| 6 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/333` | 0.340915 | Actions |
| 7 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/259` | 0.340915 | Actions |
| 8 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/652` | 0.340915 | Actions |
| 9 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/327` | 0.329787 | Free Actions and Reactions |
| 10 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/322` | 0.329098 | Actions and Activities |

### Query 60
- Text: Summarize Athletics
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/95']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/95', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/83', 'PZO22001 Starfinder Character Sheet::/page/2/TableCell/238']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/95', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/94', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/96']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/94` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/96` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/95` | 0.853437 | Athletics |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/83` | 0.529693 | Acrobatics |
| 3 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/238` | 0.327182 | Attitude |
| 4 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/423` | 0.275816 | Actions |
| 5 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/393` | 0.275816 | Actions |
| 6 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/363` | 0.275816 | Actions |
| 7 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/333` | 0.275816 | Actions |
| 8 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/259` | 0.275816 | Actions |
| 9 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/532` | 0.275816 | Actions |
| 10 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/652` | 0.275816 | Actions |

### Query 61
- Text: What is the rule about Damage?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/112']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/112', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/124', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/142']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/112', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/109', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/113']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/109` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/113` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/112` | 0.772400 | Damage |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/124` | 0.772400 | Damage |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/142` | 0.669151 | p Damage |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/160` | 0.627151 | p Damage |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/172` | 0.627151 | p Damage |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/64` | 0.327012 | Dying ( ) ( ) ( ) Wounded |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.315429 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 8 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/244` | 0.271483 | Spell Attack |
| 9 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/69` | 0.259891 | Resistances and Immunities |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/109` | 0.256731 | Melee Strikes Weapon |

### Query 62
- Text: What is the rule about Diplomacy?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/119']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/119', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/69', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/79']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/119', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/120', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/117']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/120` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/117` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/119` | 0.814591 | Diplomacy |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/69` | 0.298391 | Resistances and Immunities |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/79` | 0.290430 | Languages — |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/77` | 0.241714 | Skills — |
| 5 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/200` | 0.241299 | Magical Tradition |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/181` | 0.237267 | Traits and Notes Weapon Proficiencies |
| 7 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/247` | 0.233384 | Spells |
| 8 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/297` | 0.231844 | Allies |
| 9 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/241` | 0.230433 | Deity or Philosophy |
| 10 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/665` | 0.228926 | Rituals |

### Query 63
- Text: What is the rule about Traits and Notes?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/121']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/151', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/163', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/133']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/121', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/124', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/120']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/124` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/120` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/151` | 0.878191 | Traits and Notes |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/163` | 0.878191 | Traits and Notes |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/133` | 0.878191 | Traits and Notes |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/121` | 0.639121 | Traits and Notes  Weapon |
| 5 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/394` | 0.596178 | Traits |
| 6 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/334` | 0.596178 | Traits |
| 7 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/339` | 0.596178 | Traits |
| 8 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/429` | 0.596178 | Traits |
| 9 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/424` | 0.596178 | Traits |
| 10 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/364` | 0.596178 | Traits |

### Query 64
- Text: What is the rule about Damage?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/124']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/112', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/124', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/142']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/124', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/121', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/125']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/121` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/125` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/112` | 0.772400 | Damage |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/124` | 0.772400 | Damage |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/142` | 0.669151 | p Damage |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/160` | 0.627151 | p Damage |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/172` | 0.627151 | p Damage |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/64` | 0.327012 | Dying ( ) ( ) ( ) Wounded |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.315429 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 8 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/244` | 0.271483 | Spell Attack |
| 9 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/69` | 0.259891 | Resistances and Immunities |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/109` | 0.256731 | Melee Strikes Weapon |

### Query 65
- Text: What is the rule about Traits and Notes?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/133']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/151', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/163', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/133']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/133', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/132', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/135']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/132` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/135` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/151` | 0.878191 | Traits and Notes |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/163` | 0.878191 | Traits and Notes |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/133` | 0.878191 | Traits and Notes |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/121` | 0.639121 | Traits and Notes  Weapon |
| 5 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/394` | 0.596178 | Traits |
| 6 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/334` | 0.596178 | Traits |
| 7 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/339` | 0.596178 | Traits |
| 8 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/429` | 0.596178 | Traits |
| 9 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/424` | 0.596178 | Traits |
| 10 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/364` | 0.596178 | Traits |

### Query 66
- Text: What is the rule about p Damage?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/142']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/160', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/142', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/172']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/142', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/141', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/144']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/141` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/144` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/160` | 0.865703 | p Damage |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/142` | 0.865703 | p Damage |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/172` | 0.865703 | p Damage |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/124` | 0.651876 | Damage |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/112` | 0.651876 | Damage |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.352447 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/64` | 0.330717 | Dying ( ) ( ) ( ) Wounded |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/12` | 0.273267 | Hero Points— |
| 9 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/244` | 0.272708 | Spell Attack |
| 10 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/387` | 0.265243 | Effects |

### Query 67
- Text: What is the rule about Traits and Notes?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/151']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/151', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/163', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/133']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/151', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/153', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/150']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/153` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/150` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/151` | 0.878191 | Traits and Notes |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/163` | 0.878191 | Traits and Notes |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/133` | 0.878191 | Traits and Notes |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/121` | 0.639121 | Traits and Notes  Weapon |
| 5 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/394` | 0.596178 | Traits |
| 6 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/334` | 0.596178 | Traits |
| 7 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/339` | 0.596178 | Traits |
| 8 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/429` | 0.596178 | Traits |
| 9 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/424` | 0.596178 | Traits |
| 10 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/364` | 0.596178 | Traits |

### Query 68
- Text: What is the rule about p Damage?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/160']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/160', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/142', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/172']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/160', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/161', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/159']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/161` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/159` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/160` | 0.865703 | p Damage |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/142` | 0.865703 | p Damage |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/172` | 0.865703 | p Damage |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/124` | 0.651876 | Damage |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/112` | 0.651876 | Damage |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.352447 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/64` | 0.330717 | Dying ( ) ( ) ( ) Wounded |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/12` | 0.273267 | Hero Points— |
| 9 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/244` | 0.272708 | Spell Attack |
| 10 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/387` | 0.265243 | Effects |

### Query 69
- Text: What is the rule about Traits and Notes?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/163']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/151', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/163', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/133']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/163', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/165', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/162']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/165` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/162` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/151` | 0.878191 | Traits and Notes |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/163` | 0.878191 | Traits and Notes |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/133` | 0.878191 | Traits and Notes |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/121` | 0.639121 | Traits and Notes  Weapon |
| 5 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/394` | 0.596178 | Traits |
| 6 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/334` | 0.596178 | Traits |
| 7 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/339` | 0.596178 | Traits |
| 8 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/364` | 0.596178 | Traits |
| 9 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/399` | 0.596178 | Traits |
| 10 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/429` | 0.596178 | Traits |

### Query 70
- Text: What is the rule about p Damage?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/172']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/160', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/142', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/172']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/172', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/171', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/173']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/171` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/173` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/160` | 0.865703 | p Damage |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/142` | 0.865703 | p Damage |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/172` | 0.865703 | p Damage |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/124` | 0.651876 | Damage |
| 5 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/112` | 0.651876 | Damage |
| 6 | `PZO22001 Starfinder Character Sheet::/page/0/Form/0` | 0.352447 | ~~~~~°Character Name =Level ———Hero Points—LJAKANDAKXPCharacter SheetPlayer NameGain 1 at the start of each session and when granted by the GM.  Spend 1 to reroll a check.Ancestry ———Background ——Spen |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/64` | 0.330717 | Dying ( ) ( ) ( ) Wounded |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/12` | 0.273267 | Hero Points— |
| 9 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/244` | 0.272708 | Spell Attack |
| 10 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/387` | 0.265243 | Effects |

### Query 71
- Text: What is the rule about Traits and Notes?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/181']
- Expected found: `True`
- Expected rank: `15`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/151', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/163', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/133']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/181', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/180', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/184']
- Expanded expected found: `True`
- Expanded expected rank: `15`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/180` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/184` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/151` | 0.878191 | Traits and Notes |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/163` | 0.878191 | Traits and Notes |
| 3 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/133` | 0.878191 | Traits and Notes |
| 4 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/121` | 0.639121 | Traits and Notes  Weapon |
| 5 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/394` | 0.596178 | Traits |
| 6 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/334` | 0.596178 | Traits |
| 7 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/339` | 0.596178 | Traits |
| 8 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/429` | 0.596178 | Traits |
| 9 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/424` | 0.596178 | Traits |
| 10 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/364` | 0.596178 | Traits |

### Query 72
- Text: What is the rule about Class DC ——?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/193']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/193', 'PZO22001 Starfinder Character Sheet::/page/3/TableCell/245', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/355']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/193', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/194', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/192']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/194` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/192` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/193` | 0.833037 | Class DC —— |
| 2 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/245` | 0.547063 | Spell DC T |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/355` | 0.534899 | Class Feature |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/315` | 0.492899 | Class Feature |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/345` | 0.492899 | Class Feature |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/305` | 0.492899 | Class Feature |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/365` | 0.492899 | Class Feature |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/375` | 0.492899 | Class Feature |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/385` | 0.492899 | Class Feature |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/335` | 0.492899 | Class Feature |

### Query 73
- Text: What is the rule about Action Icana?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/195']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/195', 'PZO22001 Starfinder Character Sheet::/page/3/TableCell/259', 'PZO22001 Starfinder Character Sheet::/page/3/TableCell/652']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/195', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/194', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/197']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/194` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/197` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/195` | 0.843975 | Action Icana |
| 2 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/259` | 0.498999 | Actions |
| 3 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/652` | 0.498999 | Actions |
| 4 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/393` | 0.456999 | Actions |
| 5 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/423` | 0.456999 | Actions |
| 6 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/363` | 0.456999 | Actions |
| 7 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/333` | 0.456999 | Actions |
| 8 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/532` | 0.456999 | Actions |
| 9 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/201` | 0.417278 | Action Icons  ❖ Single Action  ❖ Two-Action Activity |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/207` | 0.392263 | Two-Action Activity Three-Action Activity Free Action Reaction |

### Query 74
- Text: What is the rule about Proficiency?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/200']
- Expected found: `True`
- Expected rank: `12`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/181', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/77', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/294']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/200', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/199', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/201']
- Expanded expected found: `True`
- Expanded expected rank: `12`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/199` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/201` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/181` | 0.543434 | Traits and Notes Weapon Proficiencies |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/77` | 0.456052 | Skills — |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/294` | 0.447682 | Background Skill Feat |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/319` | 0.385083 | Skill Feat |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/379` | 0.385083 | Skill Feat |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/299` | 0.385083 | Skill Feat |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/359` | 0.385083 | Skill Feat |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/329` | 0.385083 | Skill Feat |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/309` | 0.385083 | Skill Feat |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/349` | 0.385083 | Skill Feat |

### Query 75
- Text: What is the rule about Action Icons?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/201']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/201', 'PZO22001 Starfinder Character Sheet::/page/3/TableCell/264', 'PZO22001 Starfinder Character Sheet::/page/2/TableCell/423']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/201', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/203', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/200']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/203` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/200` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/201` | 0.667186 | Action Icons  ❖ Single Action  ❖ Two-Action Activity |
| 2 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/264` | 0.477401 | Actions Rank |
| 3 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/423` | 0.455664 | Actions |
| 4 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/259` | 0.413664 | Actions |
| 5 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/652` | 0.413664 | Actions |
| 6 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/393` | 0.413664 | Actions |
| 7 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/333` | 0.413664 | Actions |
| 8 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/363` | 0.413664 | Actions |
| 9 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/532` | 0.413664 | Actions |
| 10 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/207` | 0.372332 | Two-Action Activity Three-Action Activity Free Action Reaction |

### Query 76
- Text: What is the rule about Two-Action Activity?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/207']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/201', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/207', 'PZO22001 Starfinder Character Sheet::/page/2/TableCell/322']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/0/TableCell/207', 'PZO22001 Starfinder Character Sheet::/page/1/Form/0', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/206']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/1/Form/0` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/206` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/201` | 0.703393 | Action Icons  ❖ Single Action  ❖ Two-Action Activity |
| 2 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/207` | 0.699171 | Two-Action Activity Three-Action Activity Free Action Reaction |
| 3 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/322` | 0.595622 | Actions and Activities |
| 4 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/259` | 0.533813 | Actions |
| 5 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/363` | 0.533813 | Actions |
| 6 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/532` | 0.533813 | Actions |
| 7 | `PZO22001 Starfinder Character Sheet::/page/3/TableCell/652` | 0.533813 | Actions |
| 8 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/333` | 0.533813 | Actions |
| 9 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/393` | 0.533813 | Actions |
| 10 | `PZO22001 Starfinder Character Sheet::/page/2/TableCell/423` | 0.533813 | Actions |

### Query 77
- Text: What is the rule about Ancestry and General FeatsClass AbilitiesInventoryLevel?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/Form/0']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/279', 'PZO22001 Starfinder Character Sheet::/page/1/Form/0', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/284']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/Form/0', 'PZO22001 Starfinder Character Sheet::/page/0/TableCell/207', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/279']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/0/TableCell/207` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/279` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/279` | 0.723971 | Ancestry and General Feats |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/Form/0` | 0.651058 | Ancestry and General FeatsClass AbilitiesInventoryLevel 1Ancestry and Heritage AbilitiesClass Feats and FeaturesHeld ItemsBulkAncestry FeatBackground Skill Feat2Skill FeatClass Feat3General FeatClass |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/284` | 0.631367 | Ancestry and Heritage Abilities |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/334` | 0.567611 | Ancestry Feat |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/289` | 0.567611 | Ancestry Feat |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/354` | 0.567611 | Ancestry Feat |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/374` | 0.567611 | Ancestry Feat |
| 8 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/24` | 0.526739 | Ancestry ——— |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/314` | 0.509593 | Ancestry Feat Boosts |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/280` | 0.498278 | Class Abilities |

### Query 78
- Text: What is the rule about Ancestry and General Feats?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/279']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/279', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/289', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/354']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/279', 'PZO22001 Starfinder Character Sheet::/page/1/Form/0', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/280']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/1/Form/0` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/280` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/279` | 0.907787 | Ancestry and General Feats |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/289` | 0.779696 | Ancestry Feat |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/354` | 0.779696 | Ancestry Feat |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/334` | 0.737696 | Ancestry Feat |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/374` | 0.737696 | Ancestry Feat |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/314` | 0.622093 | Ancestry Feat Boosts |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/344` | 0.596036 | General Feat |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/304` | 0.596036 | General Feat |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/324` | 0.596036 | General Feat |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/384` | 0.596036 | General Feat |

### Query 79
- Text: What is the rule about Class Feats and Features?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/285']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/285', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/330', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/310']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/285', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/286', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/284']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/286` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/284` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/285` | 0.850856 | Class Feats and Features |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/310` | 0.717109 | Class Feat |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/330` | 0.717109 | Class Feat |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/300` | 0.675109 | Class Feat |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/360` | 0.675109 | Class Feat |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/370` | 0.675109 | Class Feat |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/350` | 0.675109 | Class Feat |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/340` | 0.675109 | Class Feat |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/380` | 0.675109 | Class Feat |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/390` | 0.675109 | Class Feat |

### Query 80
- Text: What is the rule about Ancestry Feat?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/289']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/354', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/289', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/334']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/289', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/294', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/287']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/294` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/287` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/354` | 0.888677 | Ancestry Feat |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/289` | 0.888677 | Ancestry Feat |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/334` | 0.888677 | Ancestry Feat |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/374` | 0.846677 | Ancestry Feat |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/279` | 0.720776 | Ancestry and General Feats |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/314` | 0.698027 | Ancestry Feat Boosts |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/24` | 0.587890 | Ancestry ——— |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/384` | 0.534833 | General Feat |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/304` | 0.534833 | General Feat |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/324` | 0.534833 | General Feat |

### Query 81
- Text: What is the rule about Background Skill Feat?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/294']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/294', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/299', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/319']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/294', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/298', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/289']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/298` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/289` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/294` | 0.891325 | Background Skill Feat |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/299` | 0.693223 | Skill Feat |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/319` | 0.693223 | Skill Feat |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/309` | 0.651223 | Skill Feat |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/329` | 0.651223 | Skill Feat |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/349` | 0.651223 | Skill Feat |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/369` | 0.651223 | Skill Feat |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/379` | 0.651223 | Skill Feat |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/359` | 0.651223 | Skill Feat |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/389` | 0.550940 | Skill Feat Boosts |

### Query 82
- Text: What is the rule about Skill Feat?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/299']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/319', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/309', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/329']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/299', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/300', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/298']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/300` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/298` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/319` | 0.860776 | Skill Feat |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/309` | 0.860776 | Skill Feat |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/329` | 0.860776 | Skill Feat |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/379` | 0.818776 | Skill Feat |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/359` | 0.818776 | Skill Feat |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/299` | 0.818776 | Skill Feat |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/369` | 0.818776 | Skill Feat |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/349` | 0.818776 | Skill Feat |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/294` | 0.728123 | Background Skill Feat |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/339` | 0.651706 | Skill Feat Boosts |

### Query 83
- Text: What is the rule about Class Feat?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/300']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/340', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/350', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/370']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/300', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/299', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/303']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/299` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/303` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/370` | 0.864068 | Class Feat |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/340` | 0.864068 | Class Feat |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/350` | 0.864068 | Class Feat |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/390` | 0.822068 | Class Feat |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/310` | 0.822068 | Class Feat |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/300` | 0.822068 | Class Feat |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/330` | 0.822068 | Class Feat |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/360` | 0.822068 | Class Feat |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/380` | 0.822068 | Class Feat |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/320` | 0.822068 | Class Feat |

### Query 84
- Text: What is the rule about General Feat?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/304']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/304', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/384', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/344']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/304', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/305', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/303']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/305` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/303` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/304` | 0.855928 | General Feat |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/344` | 0.855928 | General Feat |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/384` | 0.855928 | General Feat |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/324` | 0.813928 | General Feat |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/279` | 0.636012 | Ancestry and General Feats |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/364` | 0.541149 | General Feat Boosts |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/334` | 0.514873 | Ancestry Feat |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/354` | 0.514873 | Ancestry Feat |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/289` | 0.514873 | Ancestry Feat |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/374` | 0.514873 | Ancestry Feat |

### Query 85
- Text: What is the rule about Class Feature?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/305']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/315', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/305', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/325']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/305', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/306', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/304']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/306` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/304` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/315` | 0.825723 | Class Feature |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/305` | 0.825723 | Class Feature |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/325` | 0.825723 | Class Feature |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/355` | 0.783723 | Class Feature |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/385` | 0.783723 | Class Feature |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/375` | 0.783723 | Class Feature |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/365` | 0.783723 | Class Feature |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/335` | 0.783723 | Class Feature |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/345` | 0.783723 | Class Feature |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/285` | 0.715955 | Class Feats and Features |

### Query 86
- Text: What is the rule about Skill Feat?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/309']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/319', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/309', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/329']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/309', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/310', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/308']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/310` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/308` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/319` | 0.860776 | Skill Feat |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/309` | 0.860776 | Skill Feat |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/329` | 0.860776 | Skill Feat |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/379` | 0.818776 | Skill Feat |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/359` | 0.818776 | Skill Feat |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/299` | 0.818776 | Skill Feat |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/369` | 0.818776 | Skill Feat |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/349` | 0.818776 | Skill Feat |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/294` | 0.728123 | Background Skill Feat |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/339` | 0.651706 | Skill Feat Boosts |

### Query 87
- Text: What is the rule about Class Feat?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/310']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/340', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/350', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/370']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/310', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/309', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/313']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/309` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/313` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/370` | 0.864068 | Class Feat |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/340` | 0.864068 | Class Feat |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/350` | 0.864068 | Class Feat |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/390` | 0.822068 | Class Feat |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/310` | 0.822068 | Class Feat |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/300` | 0.822068 | Class Feat |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/330` | 0.822068 | Class Feat |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/360` | 0.822068 | Class Feat |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/380` | 0.822068 | Class Feat |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/320` | 0.822068 | Class Feat |

### Query 88
- Text: What is the rule about Ancestry Feat?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/314']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/354', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/289', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/334']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/314', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/315', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/313']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/315` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/313` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/354` | 0.888677 | Ancestry Feat |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/289` | 0.888677 | Ancestry Feat |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/334` | 0.888677 | Ancestry Feat |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/374` | 0.846677 | Ancestry Feat |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/279` | 0.720776 | Ancestry and General Feats |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/314` | 0.698027 | Ancestry Feat Boosts |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/24` | 0.587890 | Ancestry ——— |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/384` | 0.534833 | General Feat |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/304` | 0.534833 | General Feat |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/324` | 0.534833 | General Feat |

### Query 89
- Text: What is the rule about Class Feature?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/315']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/315', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/305', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/325']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/315', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/314', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/318']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/314` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/318` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/315` | 0.825723 | Class Feature |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/305` | 0.825723 | Class Feature |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/325` | 0.825723 | Class Feature |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/355` | 0.783723 | Class Feature |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/385` | 0.783723 | Class Feature |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/375` | 0.783723 | Class Feature |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/365` | 0.783723 | Class Feature |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/335` | 0.783723 | Class Feature |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/345` | 0.783723 | Class Feature |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/285` | 0.715955 | Class Feats and Features |

### Query 90
- Text: What is the rule about Skill Feat?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/319']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/319', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/309', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/329']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/319', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/320', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/318']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/320` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/318` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/319` | 0.860776 | Skill Feat |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/309` | 0.860776 | Skill Feat |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/329` | 0.860776 | Skill Feat |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/379` | 0.818776 | Skill Feat |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/359` | 0.818776 | Skill Feat |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/299` | 0.818776 | Skill Feat |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/369` | 0.818776 | Skill Feat |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/349` | 0.818776 | Skill Feat |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/294` | 0.728123 | Background Skill Feat |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/339` | 0.651706 | Skill Feat Boosts |

### Query 91
- Text: What is the rule about Class Feat?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/320']
- Expected found: `True`
- Expected rank: `10`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/340', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/350', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/370']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/320', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/319', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/323']
- Expanded expected found: `True`
- Expanded expected rank: `10`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/319` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/323` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/370` | 0.864068 | Class Feat |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/340` | 0.864068 | Class Feat |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/350` | 0.864068 | Class Feat |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/390` | 0.822068 | Class Feat |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/310` | 0.822068 | Class Feat |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/300` | 0.822068 | Class Feat |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/330` | 0.822068 | Class Feat |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/360` | 0.822068 | Class Feat |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/380` | 0.822068 | Class Feat |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/320` | 0.822068 | Class Feat |

### Query 92
- Text: What is the rule about General Feat?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/324']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/304', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/384', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/344']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/324', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/325', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/323']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/325` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/323` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/304` | 0.855928 | General Feat |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/344` | 0.855928 | General Feat |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/384` | 0.855928 | General Feat |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/324` | 0.813928 | General Feat |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/279` | 0.636012 | Ancestry and General Feats |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/364` | 0.541149 | General Feat Boosts |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/334` | 0.514873 | Ancestry Feat |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/354` | 0.514873 | Ancestry Feat |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/289` | 0.514873 | Ancestry Feat |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/374` | 0.514873 | Ancestry Feat |

### Query 93
- Text: What is the rule about Class Feature?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/325']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/315', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/305', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/325']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/325', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/328', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/324']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/328` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/324` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/315` | 0.825723 | Class Feature |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/305` | 0.825723 | Class Feature |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/325` | 0.825723 | Class Feature |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/355` | 0.783723 | Class Feature |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/385` | 0.783723 | Class Feature |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/375` | 0.783723 | Class Feature |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/365` | 0.783723 | Class Feature |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/335` | 0.783723 | Class Feature |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/345` | 0.783723 | Class Feature |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/285` | 0.715955 | Class Feats and Features |

### Query 94
- Text: What is the rule about Skill Feat?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/329']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/319', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/309', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/329']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/329', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/328', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/330']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/328` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/330` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/319` | 0.860776 | Skill Feat |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/309` | 0.860776 | Skill Feat |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/329` | 0.860776 | Skill Feat |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/379` | 0.818776 | Skill Feat |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/359` | 0.818776 | Skill Feat |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/299` | 0.818776 | Skill Feat |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/369` | 0.818776 | Skill Feat |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/349` | 0.818776 | Skill Feat |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/294` | 0.728123 | Background Skill Feat |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/339` | 0.651706 | Skill Feat Boosts |

### Query 95
- Text: What is the rule about Class Feat?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/330']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/340', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/350', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/370']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/330', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/331', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/329']
- Expanded expected found: `True`
- Expanded expected rank: `7`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/331` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/329` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/370` | 0.864068 | Class Feat |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/340` | 0.864068 | Class Feat |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/350` | 0.864068 | Class Feat |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/390` | 0.822068 | Class Feat |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/310` | 0.822068 | Class Feat |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/300` | 0.822068 | Class Feat |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/330` | 0.822068 | Class Feat |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/360` | 0.822068 | Class Feat |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/380` | 0.822068 | Class Feat |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/320` | 0.822068 | Class Feat |

### Query 96
- Text: What is the rule about Ancestry Feat?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/334']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/354', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/289', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/334']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/334', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/335', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/333']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/335` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/333` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/354` | 0.888677 | Ancestry Feat |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/289` | 0.888677 | Ancestry Feat |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/334` | 0.888677 | Ancestry Feat |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/374` | 0.846677 | Ancestry Feat |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/279` | 0.720776 | Ancestry and General Feats |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/314` | 0.698027 | Ancestry Feat Boosts |
| 7 | `PZO22001 Starfinder Character Sheet::/page/0/TableCell/24` | 0.587890 | Ancestry ——— |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/384` | 0.534833 | General Feat |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/304` | 0.534833 | General Feat |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/324` | 0.534833 | General Feat |

### Query 97
- Text: What is the rule about Class Feature?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/335']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/315', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/305', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/325']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/335', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/334', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/338']
- Expanded expected found: `True`
- Expanded expected rank: `8`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/334` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/338` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/315` | 0.825723 | Class Feature |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/305` | 0.825723 | Class Feature |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/325` | 0.825723 | Class Feature |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/355` | 0.783723 | Class Feature |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/385` | 0.783723 | Class Feature |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/375` | 0.783723 | Class Feature |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/365` | 0.783723 | Class Feature |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/335` | 0.783723 | Class Feature |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/345` | 0.783723 | Class Feature |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/285` | 0.715955 | Class Feats and Features |

### Query 98
- Text: What is the rule about Skill Feat?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/339']
- Expected found: `True`
- Expected rank: `10`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/319', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/309', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/329']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/339', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/340', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/338']
- Expanded expected found: `True`
- Expanded expected rank: `10`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/340` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/338` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/319` | 0.860776 | Skill Feat |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/309` | 0.860776 | Skill Feat |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/329` | 0.860776 | Skill Feat |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/379` | 0.818776 | Skill Feat |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/359` | 0.818776 | Skill Feat |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/299` | 0.818776 | Skill Feat |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/369` | 0.818776 | Skill Feat |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/349` | 0.818776 | Skill Feat |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/294` | 0.728123 | Background Skill Feat |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/339` | 0.651706 | Skill Feat Boosts |

### Query 99
- Text: What is the rule about Class Feat?
- Expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/340']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/340', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/350', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/370']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Character Sheet::/page/1/TableCell/340', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/343', 'PZO22001 Starfinder Character Sheet::/page/1/TableCell/339']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/343` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Character Sheet::/page/1/TableCell/339` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/370` | 0.864068 | Class Feat |
| 2 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/340` | 0.864068 | Class Feat |
| 3 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/350` | 0.864068 | Class Feat |
| 4 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/390` | 0.822068 | Class Feat |
| 5 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/310` | 0.822068 | Class Feat |
| 6 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/300` | 0.822068 | Class Feat |
| 7 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/330` | 0.822068 | Class Feat |
| 8 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/360` | 0.822068 | Class Feat |
| 9 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/380` | 0.822068 | Class Feat |
| 10 | `PZO22001 Starfinder Character Sheet::/page/1/TableCell/320` | 0.822068 | Class Feat |
