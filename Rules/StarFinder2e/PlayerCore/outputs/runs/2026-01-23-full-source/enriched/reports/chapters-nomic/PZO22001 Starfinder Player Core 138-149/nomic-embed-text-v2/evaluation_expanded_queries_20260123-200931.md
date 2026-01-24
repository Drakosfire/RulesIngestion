# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `600`
- Query count: `153`
- Evaluated queries: `153`
- Coverage: `1.0000`
- MRR: `0.9037`
- hit@1: `0.8562`
- hit@3: `0.9281`
- hit@5: `0.9673`
- hit@10: `1.0000`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

### Expanded Gold Metrics
- Coverage: `1.0000`
- MRR: `0.9069`
- hit@1: `0.8627`
- hit@3: `0.9281`
- hit@5: `0.9673`
- hit@10: `1.0000`

### Expanded Gold Expansion Stats
- Queries with additions: `153`
- Avg added per query: `2.08`
- Max added: `7`
- Addition reasons:
  - graph_depth_1: `318`

### Expanded Gold Delta (Expanded - Strict)
- Coverage Δ: `0.0000`
- MRR Δ: `0.0033`
- hit@1 Δ: `0.0065`
- hit@3 Δ: `0.0000`
- hit@5 Δ: `0.0000`
- hit@10 Δ: `0.0000`

## Timings (ms)
- Embedding (chunks): `8221`
- Embedding (queries): `2421`
- Evaluation (strict): `81`
- Evaluation (expanded): `48`
- Total: `15524`

### Timing Estimates (ms)
- Evaluation (strict): `397`
- Evaluation (expanded): `198`
- Total: `11237`

## Query Details
### Query 0
- Text: Summarize SOLARIAN
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/37', 'PZO22001 Starfinder Player Core 138-149::/page/5/Text/49']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/1` | 0.954773 | SOLARIAN |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/37` | 0.809947 | **Solarian** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/49` | 0.809947 | **Solarian** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/64` | 0.767947 | **Solarian** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/63` | 0.767947 | **Solarian** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/36` | 0.767947 | **Solarian** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/24` | 0.753944 | **SOLARIAN** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/4` | 0.753944 | **SOLARIAN** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/24` | 0.753944 | **SOLARIAN** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/53` | 0.753944 | **SOLARIAN** |

### Query 1
- Text: What is the rule about You're a conduit for the stellar forces of the cosmos—a solar knight. The powers of gravity and light  represent the extremes of these forces, and you can attune yourself between them. As an agent of this  cycle, you manifest an array of solar equipment and use your own connection to stellar forces to empower  them. Regardless of which extreme of the stellar spectrum you prefer, you can change your attunement  between them to take advantage of solar powers earned through meditation and practice.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/2', 'PZO22001 Starfinder Player Core 138-149::/page/2/Text/17', 'PZO22001 Starfinder Player Core 138-149::/page/2/Text/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/2', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/6', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/2` | 0.990963 | You're a conduit for the stellar forces of the cosmos—a solar knight. The powers of gravity and light  represent the extremes of these forces, and you can attune yourself between them. As an agent of |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/17` | 0.749923 | You steady your body and mind and attune yourself to the  stellar aspect of your choice. You become attuned to photon or  graviton. You can also manifest any of your solar manifestations  if they're c |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/11` | 0.709643 | As a solarian, your existence cycles between the aspects of  stars. You begin with two aspects: photon (the power of stars to |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/12` | 0.673223 | emit heat, light, and plasma) and graviton (the power of stars to  attract and imprison objects through gravity). At any time, you're  considered graviton-attuned, photon-attuned, or unattuned.  Many |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/29` | 0.651297 | You have absolute control and understanding of your  attunement with the stellar forces of the cosmos. If you  would become graviton- or photon-attuned, you instead  become perfectly-attuned. When you |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/13` | 0.635939 | You rush into the thick of things and attack with your solar manifestations. You  shift between battlefield control and heavy attacks, depending on your current  solar attunement. |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/20` | 0.629722 | Your deep understanding of the stellar forces of the universe  manifests in a variety of tangible ways. You can create and  maintain three different manifestations: a solar flare, solar  nimbus, and s |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/25` | 0.628961 | You reach true alignment with the cosmic cycle. You're  permanently quickened. You can use your extra action  only to Attune or make a Strike with your solar flare or  solar weapon. |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/4` | 0.628437 | **Cycle:** Actions with the cycle trait change your  current stellar attunement to its opposite state. When  you take such an action with this trait, you benefit  from the additional effect of your cu |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/19` | 0.622735 | You balance your downtime between meditation and other activities. You might  create your own dedicated following to train a new generation of solarians or use  your flashy solarian powers to earn cre |

### Query 2
- Text: Summarize **KEY ATTRIBUTE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/6', 'PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/1', 'PZO22001 Starfinder Player Core 138-149::/page/5/Text/62']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/6', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/2', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/6` | 0.948607 | **KEY ATTRIBUTE** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/1` | 0.665018 | **KEY TERMS** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/62` | 0.479617 | **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/50` | 0.437617 | **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/48` | 0.429512 | **CHARACTER ** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/74` | 0.407698 | **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/14` | 0.386976 | **ATTUNE **[one-action] |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/57` | 0.384082 | **ATTACKS** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/58` | 0.378905 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/58` | 0.378905 | **INTRODUCTION** |

### Query 3
- Text: Summarize **Strength**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/7', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/8', 'PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/7', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/6', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/7` | 0.952973 | **Strength** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/8` | 0.491381 | At 1st level, your class gives you  an attribute boost to Strength. |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/2` | 0.479096 | **ASCENDED STABILITY **[reaction] **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/555` | 0.401340 | Ascended Stability |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/41` | 0.383072 | **Failure** Your attack deals damage equal to your Strength  modifier. It doesn't count as a hit and doesn't trigger any  other special abilities. |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/25` | 0.383066 | **STELLAR RUSH **[two-actions] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/55` | 0.381376 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/41` | 0.381376 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/59` | 0.376954 | **DEFENSES** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/37` | 0.373291 | **CAREFUL STRIKE **[one-action] **FEAT 10** |

### Query 4
- Text: Summarize At 1st level, your class gives you  an attribute boost to Strength.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/8', 'PZO22001 Starfinder Player Core 138-149::/page/2/Text/6', 'PZO22001 Starfinder Player Core 138-149::/page/2/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/8', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/9', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/8` | 1.034391 | At 1st level, your class gives you  an attribute boost to Strength. |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/6` | 0.761160 | In addition to what you get from your class at 1st level, you have  four free boosts to different attribute modifiers. |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/9` | 0.667266 | At 1st level, you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start of  this class. |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/4` | 0.617905 | In addition to what you get from your class at 1st level, you  have the benefits of your selected ancestry and background, as  described in Chapter 2. |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/7` | 0.597112 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier is  already +4 or higher, it takes two boosts to increase it; you get a |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/11` | 0.578173 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/37` | 0.551893 | Similar to spells, some solarian abilities get more  powerful as you increase in level. These abilities ends  with one or more "Level" entries. This either lists the  levels at which the ability gets |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/29` | 0.543723 | You gain these abilities as a solarian. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/Table/2` | 0.540927 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, stellar attunement, solar manifestations, solarian feat2Skill feat, solarian feat3General feat, skill increas |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/49` | 0.532052 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use this increase either to increase your  proficiency rank to trained in one skill you're untrained in, or  to increase |

### Query 5
- Text: What is the rule about **HIT POINTS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/9', 'PZO22001 Starfinder Player Core 138-149::/page/11/Text/9', 'PZO22001 Starfinder Player Core 138-149::/page/6/Text/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/9', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/10', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/9` | 0.884304 | **HIT POINTS** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/9` | 0.428487 | Dissonance grants you some clarity and a brief second wind  in stressful situations. When you use an action with the  disharmony trait, you gain a number of temporary Hit Points  equal to half your le |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/20` | 0.426809 | **Graviton-Attuned** On a hit, the target takes a –10-foot status  penalty to Speed until the start of your next turn. |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/19` | 0.370275 | While the shield is raised, you can use the Shield Block  reaction (page 228) with your shield. The shield has Hit Points  equal to 5 plus twice your level and Hardness equal to half  your level, roun |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/62` | 0.354981 | **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/50` | 0.354981 | **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/41` | 0.354674 | **Failure** Your attack deals damage equal to your Strength  modifier. It doesn't count as a hit and doesn't trigger any  other special abilities. |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/11` | 0.348970 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/1` | 0.348413 | **KEY TERMS** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/72` | 0.333335 | **CONDITIONS ** |

### Query 6
- Text: What is the rule about **10 + Constitution modifier**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/10', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/408', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/568']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/10', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/11', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/10` | 0.865167 | **10 + Constitution modifier** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/408` | 0.490999 | 10 |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/568` | 0.490999 | 10 |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/570` | 0.448999 | 10 |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/638` | 0.448999 | 10 |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/628` | 0.448999 | 10 |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/7` | 0.434405 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier is  already +4 or higher, it takes two boosts to increase it; you get a |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/41` | 0.361331 | **Failure** Your attack deals damage equal to your Strength  modifier. It doesn't count as a hit and doesn't trigger any  other special abilities. |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/6` | 0.348647 | In addition to what you get from your class at 1st level, you have  four free boosts to different attribute modifiers. |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/56` | 0.338217 | Trained in Athletics Trained in a number of additional  skills equal to 4 plus your Intelligence  modifier |

### Query 7
- Text: Summarize You increase your maximum number  of HP by this number at 1st level and  every level thereafter.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/11', 'PZO22001 Starfinder Player Core 138-149::/page/3/Text/49', 'PZO22001 Starfinder Player Core 138-149::/page/2/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/11', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/10', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/11` | 1.031874 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/49` | 0.637439 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use this increase either to increase your  proficiency rank to trained in one skill you're untrained in, or  to increase |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/7` | 0.604495 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier is  already +4 or higher, it takes two boosts to increase it; you get a |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/8` | 0.555008 | At 1st level, your class gives you  an attribute boost to Strength. |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/50` | 0.543409 | At 7th level, you can use skill increases to increase your  proficiency rank to master in a skill in which you're already  an expert, and at 15th level, you can use them to increase  your proficiency |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/46` | 0.526529 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/28` | 0.524640 | **Level (+1)** Increase the damage by 1d6. |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/37` | 0.524430 | Similar to spells, some solarian abilities get more  powerful as you increase in level. These abilities ends  with one or more "Level" entries. This either lists the  levels at which the ability gets |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/6` | 0.520901 | In addition to what you get from your class at 1st level, you have  four free boosts to different attribute modifiers. |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/37` | 0.520391 | **Level (+2)** Increase the damage by 1d8. |

### Query 8
- Text: Summarize DURING COMBAT ENCOUNTERS...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/12', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/12', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/11', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/12` | 0.983036 | DURING COMBAT ENCOUNTERS... |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/14` | 0.745777 | DURING SOCIAL ENCOUNTERS... |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/16` | 0.434305 | WHILE EXPLORING... |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/18` | 0.337787 | IN DOWNTIME... |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/38` | 0.333292 | **Soldier** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/65` | 0.333292 | **Soldier** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/38` | 0.333292 | **Soldier** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/51` | 0.333292 | **Soldier** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/64` | 0.333292 | **Soldier** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/61` | 0.322069 | **Envoy** |

### Query 9
- Text: What is the rule about You rush into the thick of things and attack with your solar manifestations. You  shift between battlefield control and heavy attacks, depending on your current  solar attunement.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/13', 'PZO22001 Starfinder Player Core 138-149::/page/11/Text/25', 'PZO22001 Starfinder Player Core 138-149::/page/9/Text/28']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/13', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/13` | 0.959609 | You rush into the thick of things and attack with your solar manifestations. You  shift between battlefield control and heavy attacks, depending on your current  solar attunement. |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/25` | 0.646074 | You reach true alignment with the cosmic cycle. You're  permanently quickened. You can use your extra action  only to Attune or make a Strike with your solar flare or  solar weapon. |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/28` | 0.639751 | You fire blasts of solar energy through your raised shield,  harnessing its gravitational force to propel your attacks.  When you make a solar flare Strike while you have your solar |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/18` | 0.594392 | You pour all your effort into making a single attack with  your solar weapon that's so powerful it shatters the weapon. |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/17` | 0.594092 | You steady your body and mind and attune yourself to the  stellar aspect of your choice. You become attuned to photon or  graviton. You can also manifest any of your solar manifestations  if they're c |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/5` | 0.592559 | You can use your manifestations immediately upon  attuning yourself. When you Attune as a single action, you  can make a Strike with your solar flare or solar weapon as  a free action. |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/56` | 0.590789 | You raise one of your weapons to intercept a particularly  deadly attack. You gain resistance equal to your level against  the triggering attack. One of your solar weapons shatters and  is no longer m |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/14` | 0.590477 | With practice, you can make on-the-fly battlefield adjustments  to your weapon, letting you choose the perfect attack for a  situation. When you Attune, you can change the damage type  of your solar w |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/43` | 0.589652 | Your attacks create a brilliant eclipse that veil you from  the enemy's view. Make a Strike with your solar weapon or  your solar flare. On a hit, you create an impressive display of  solar energy bet |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/14` | 0.584917 | You extend your control of stellar forces to punish your foes.  Creatures that hit you with an attack suffer consequences  based on your attunement. |

### Query 10
- Text: Summarize DURING SOCIAL ENCOUNTERS...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/12', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/15', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/14` | 0.977694 | DURING SOCIAL ENCOUNTERS... |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/12` | 0.728104 | DURING COMBAT ENCOUNTERS... |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/16` | 0.408727 | WHILE EXPLORING... |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/18` | 0.315217 | IN DOWNTIME... |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/24` | 0.286287 | OTHERS PROBABLY... |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/20` | 0.285896 | YOU MIGHT... |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/34` | 0.282589 | **Envoy** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/61` | 0.282589 | **Envoy** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/35` | 0.282589 | **Envoy** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/61` | 0.282589 | **Envoy** |

### Query 11
- Text: What is the rule about Which solar aspect you prefer might influence how you act in social circles. You might  be a chatterbox who makes friends easily or a smooth manipulator who uses your  abilities to coerce people.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/15', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/13', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/15', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/16', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/15` | 1.011704 | Which solar aspect you prefer might influence how you act in social circles. You might  be a chatterbox who makes friends easily or a smooth manipulator who uses your  abilities to coerce people. |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/13` | 0.599378 | You rush into the thick of things and attack with your solar manifestations. You  shift between battlefield control and heavy attacks, depending on your current  solar attunement. |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/2` | 0.566802 | You're a conduit for the stellar forces of the cosmos—a solar knight. The powers of gravity and light  represent the extremes of these forces, and you can attune yourself between them. As an agent of |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/17` | 0.522786 | You steady your body and mind and attune yourself to the  stellar aspect of your choice. You become attuned to photon or  graviton. You can also manifest any of your solar manifestations  if they're c |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/26` | 0.516502 | You're a paragon among solarians, capable of shaping stellar  forces into powerful weapons that bend to your will. Your  proficiency ranks for your solar flare and solar weapon  increase to legendary. |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/7` | 0.499594 | **Manifestation:** Feats with this trait enhance or  alter your solar manifestations (flare, nimbus, and  weapon) or allow you to create a new type of solar  manifestation. |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/38` | 0.498340 | type (typically choosing between bludgeoning, piercing, or  slashing), selected traits, and weapon group. Your weapon  maintains your selections until the next time you Re-Forge  Solar Weapon. |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/43` | 0.495821 | Your attacks create a brilliant eclipse that veil you from  the enemy's view. Make a Strike with your solar weapon or  your solar flare. On a hit, you create an impressive display of  solar energy bet |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/11` | 0.489303 | As a solarian, your existence cycles between the aspects of  stars. You begin with two aspects: photon (the power of stars to |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/12` | 0.487477 | emit heat, light, and plasma) and graviton (the power of stars to  attract and imprison objects through gravity). At any time, you're  considered graviton-attuned, photon-attuned, or unattuned.  Many |

### Query 12
- Text: Summarize WHILE EXPLORING...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/16', 'PZO22001 Starfinder Player Core 138-149::/page/3/SectionHeader/34', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/16', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/15', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/16` | 0.945993 | WHILE EXPLORING... |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/3/SectionHeader/34` | 0.455893 | **CONCENTRATE** **EXPLORATION** **SOLARIAN** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/14` | 0.439598 | DURING SOCIAL ENCOUNTERS... |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/12` | 0.395469 | DURING COMBAT ENCOUNTERS... |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/18` | 0.348777 | IN DOWNTIME... |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/71` | 0.330508 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/45` | 0.330508 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/57` | 0.330508 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/44` | 0.330508 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/45` | 0.330508 | **PLAYING THE ** **GAME** |

### Query 13
- Text: Summarize You likely stick near the front of the group to quickly get into the fight. You use  your powers to overcome challenges, like moving debris or climbing strange terrain.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/17', 'PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/26', 'PZO22001 Starfinder Player Core 138-149::/page/5/Text/28']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/17', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/17` | 1.036782 | You likely stick near the front of the group to quickly get into the fight. You use  your powers to overcome challenges, like moving debris or climbing strange terrain. |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/26` | 0.618886 | Enjoy watching you fight or demonstrate your powers. |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/28` | 0.604751 | You rush forward with a blast of stellar energy, getting into  the thick of combat with ease. Stride twice. You gain a +10-foot  circumstance bonus to your Speed during these moves. |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/21` | 0.561823 | You use the momentum of your last attack to maneuver  around the battlefield, either by leaving photonic images or  making great gravity-assisted leaps. Step twice. |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/29` | 0.559360 | **Graviton-Attuned** When you finish your Strides, enemies  within 15 feet of you must attempt a Fortitude save against  your class DC. On a failure, they're pulled directly toward  you, ending in an |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/13` | 0.540769 | You rush into the thick of things and attack with your solar manifestations. You  shift between battlefield control and heavy attacks, depending on your current  solar attunement. |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/10` | 0.536751 | You attack a target with your solar weapon, harnessing the  collision's energy to attack another foe at the speed of light.  Make a Strike with your solar weapon. On a hit, you teleport  up to your Sp |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/14` | 0.530533 | You extend your control of stellar forces to punish your foes.  Creatures that hit you with an attack suffer consequences  based on your attunement. |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/35` | 0.528327 | **Failure** The creature takes full damage, is pulled 15 feet toward  you, and is off-guard against the next melee attack that you  attempt against it before the end of your current turn. |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/11` | 0.522883 | You focus on your flare, setting up a blast of energy to disorient  your foes. Make a ranged Strike with your solar flare. If this  attack hits, the target is off-guard until the start of your next  t |

### Query 14
- Text: Summarize IN DOWNTIME...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/20', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/19', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/18` | 0.786911 | IN DOWNTIME... |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/20` | 0.405938 | YOU MIGHT... |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/14` | 0.367088 | DURING SOCIAL ENCOUNTERS... |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/16` | 0.322232 | WHILE EXPLORING... |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/12` | 0.314851 | DURING COMBAT ENCOUNTERS... |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/24` | 0.302606 | OTHERS PROBABLY... |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/1` | 0.287179 | **KEY TERMS** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/71` | 0.281902 | **GAME** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/1` | 0.279634 | **SOLARIAN FEATS BY NAME** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/58` | 0.271423 | **INTRODUCTION** |

### Query 15
- Text: What is the rule about You balance your downtime between meditation and other activities. You might  create your own dedicated following to train a new generation of solarians or use  your flashy solarian powers to earn credits as a laborer or performer.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/19', 'PZO22001 Starfinder Player Core 138-149::/page/2/Text/11', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/19', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/19` | 0.972468 | You balance your downtime between meditation and other activities. You might  create your own dedicated following to train a new generation of solarians or use  your flashy solarian powers to earn cre |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/11` | 0.629652 | As a solarian, your existence cycles between the aspects of  stars. You begin with two aspects: photon (the power of stars to |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/2` | 0.622778 | You're a conduit for the stellar forces of the cosmos—a solar knight. The powers of gravity and light  represent the extremes of these forces, and you can attune yourself between them. As an agent of |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/17` | 0.557837 | You steady your body and mind and attune yourself to the  stellar aspect of your choice. You become attuned to photon or  graviton. You can also manifest any of your solar manifestations  if they're c |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/24` | 0.525859 | Your ability to manipulate stellar forces is unparalleled.  Your proficiency rank for your solarian class DC increases  to master. |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/13` | 0.523249 | You rush into the thick of things and attack with your solar manifestations. You  shift between battlefield control and heavy attacks, depending on your current  solar attunement. |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/26` | 0.517917 | You're a paragon among solarians, capable of shaping stellar  forces into powerful weapons that bend to your will. Your  proficiency ranks for your solar flare and solar weapon  increase to legendary. |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/15` | 0.515221 | You briefly meditate on the nature of your foe and their role  in the wider cosmos. Attempt a check to Recall Knowledge  about a creature. On a success, your next Strike with a solar  weapon against t |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/5` | 0.508845 | You can use your manifestations immediately upon  attuning yourself. When you Attune as a single action, you  can make a Strike with your solar flare or solar weapon as  a free action. |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/2` | 0.507487 | At each level that you gain a solarian feat, you can select one of  the following feats. You must satisfy any prerequisites before  taking the feat. |

### Query 16
- Text: Summarize YOU MIGHT...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/20', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/24', 'PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/20', 'PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/21', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/20` | 0.903204 | YOU MIGHT... |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/24` | 0.522471 | OTHERS PROBABLY... |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/11` | 0.387696 | **MUTABLE MANIFESTATION** **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/18` | 0.320798 | IN DOWNTIME... |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/16` | 0.315404 | WHILE EXPLORING... |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/12` | 0.303473 | DURING COMBAT ENCOUNTERS... |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/5` | 0.296888 | **Trigger **You would cycle or become unattuned. |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/22` | 0.291735 | Surprise others with cunning uses of your stellar abilities, performing acts that  others weren't expecting or didn't know you could do. |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/10` | 0.287086 | **10 + Constitution modifier** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/1` | 0.278501 | **KEY TERMS** |

### Query 17
- Text: What is the rule about Approach obstacles with caution or throw yourself headfirst at problems  depending upon which attunement you favor.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/21', 'PZO22001 Starfinder Player Core 138-149::/page/11/Text/14', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/21', 'PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/22', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/21` | 0.919029 | Approach obstacles with caution or throw yourself headfirst at problems  depending upon which attunement you favor. |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/14` | 0.496592 | You extend your control of stellar forces to punish your foes.  Creatures that hit you with an attack suffer consequences  based on your attunement. |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/13` | 0.491732 | You rush into the thick of things and attack with your solar manifestations. You  shift between battlefield control and heavy attacks, depending on your current  solar attunement. |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/3` | 0.434222 | **Attuned:** You can't use abilities with the attuned  trait while you're unattuned. Many attuned abilities  require you to be specifically graviton-attuned or  photon-attuned, while others can grant |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/29` | 0.431535 | You have absolute control and understanding of your  attunement with the stellar forces of the cosmos. If you  would become graviton- or photon-attuned, you instead  become perfectly-attuned. When you |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/16` | 0.429964 | **Graviton-Attuned** A creature beginning its turn adjacent  to a wormhole must succeed at a Fortitude save against  your class DC or be pulled into the wormhole. |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/4` | 0.422657 | **Cycle:** Actions with the cycle trait change your  current stellar attunement to its opposite state. When  you take such an action with this trait, you benefit  from the additional effect of your cu |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/29` | 0.421667 | **Graviton-Attuned** When you finish your Strides, enemies  within 15 feet of you must attempt a Fortitude save against  your class DC. On a failure, they're pulled directly toward  you, ending in an |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/12` | 0.417415 | emit heat, light, and plasma) and graviton (the power of stars to  attract and imprison objects through gravity). At any time, you're  considered graviton-attuned, photon-attuned, or unattuned.  Many |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/15` | 0.411032 | **Graviton-Attuned** The creature is clumsy 1 and off-guard for  1 round. This increases to clumsy 2 if this is the second  time it hit you this turn. |

### Query 18
- Text: What is the rule about Surprise others with cunning uses of your stellar abilities, performing acts that  others weren't expecting or didn't know you could do.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/22', 'PZO22001 Starfinder Player Core 138-149::/page/2/Text/17', 'PZO22001 Starfinder Player Core 138-149::/page/2/Text/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/22', 'PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/21', 'PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/22` | 0.902030 | Surprise others with cunning uses of your stellar abilities, performing acts that  others weren't expecting or didn't know you could do. |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/17` | 0.508392 | You steady your body and mind and attune yourself to the  stellar aspect of your choice. You become attuned to photon or  graviton. You can also manifest any of your solar manifestations  if they're c |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/12` | 0.494636 | emit heat, light, and plasma) and graviton (the power of stars to  attract and imprison objects through gravity). At any time, you're  considered graviton-attuned, photon-attuned, or unattuned.  Many |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/3` | 0.443593 | **Attuned:** You can't use abilities with the attuned  trait while you're unattuned. Many attuned abilities  require you to be specifically graviton-attuned or  photon-attuned, while others can grant |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/5` | 0.437459 | **Disharmony:** Actions with the disharmony trait  change your current stellar attunement to being  unattuned. When you take such an action with this  trait, you benefit from the additional effect of |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/5` | 0.432369 | You can use your manifestations immediately upon  attuning yourself. When you Attune as a single action, you  can make a Strike with your solar flare or solar weapon as  a free action. |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/4` | 0.426394 | **Cycle:** Actions with the cycle trait change your  current stellar attunement to its opposite state. When  you take such an action with this trait, you benefit  from the additional effect of your cu |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/14` | 0.425712 | You extend your control of stellar forces to punish your foes.  Creatures that hit you with an attack suffer consequences  based on your attunement. |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/2` | 0.420641 | You're a conduit for the stellar forces of the cosmos—a solar knight. The powers of gravity and light  represent the extremes of these forces, and you can attune yourself between them. As an agent of |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/5` | 0.415231 | Your careful training and honed senses give you increased  awareness of your surroundings. Your proficiency rank for  Perception increases to master. In addition, you gain a +2  circumstance bonus to |

### Query 19
- Text: Summarize Meditate or shadow spar constantly to perfect your techniques.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/23', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/19', 'PZO22001 Starfinder Player Core 138-149::/page/4/Text/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/23', 'PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/22', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/23` | 1.027295 | Meditate or shadow spar constantly to perfect your techniques. |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/19` | 0.562548 | You balance your downtime between meditation and other activities. You might  create your own dedicated following to train a new generation of solarians or use  your flashy solarian powers to earn cre |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/17` | 0.495820 | You avoid harm by manipulating gravitational forces to  protect your body. Your proficiency rank for Reflex saves  increases to master. When you roll a success on a Reflex save,  you get a critical su |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/43` | 0.421474 | Your attacks create a brilliant eclipse that veil you from  the enemy's view. Make a Strike with your solar weapon or  your solar flare. On a hit, you create an impressive display of  solar energy bet |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/6` | 0.418545 | You briefly enter a meditative state in which you re-center  yourself and remember the ever-shifting balance between  the violent extremes of the cycle. You don't become  unattuned or cycle, and you r |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/22` | 0.414048 | You deftly protect yourself in almost any situation. Your  proficiency ranks for light armor, medium armor, and  unarmored defense increase to master. |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/53` | 0.402944 | Stellar energy flows throughout your entire being like  an unstoppable tidal wave, strengthening both body and  mind. Your proficiency rank in Fortitude saves increases to  expert. When you roll a suc |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/17` | 0.402340 | You steady your body and mind and attune yourself to the  stellar aspect of your choice. You become attuned to photon or  graviton. You can also manifest any of your solar manifestations  if they're c |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/6` | 0.402315 | **Flourish:** Actions with the flourish trait are special  techniques that require too much exertion for you to  perform frequently. You can only use one action with  the flourish trait per round. |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/15` | 0.392726 | You briefly meditate on the nature of your foe and their role  in the wider cosmos. Attempt a check to Recall Knowledge  about a creature. On a success, your next Strike with a solar  weapon against t |

### Query 20
- Text: Summarize OTHERS PROBABLY...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/24', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/20', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/24', 'PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/25', 'PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/24` | 0.892334 | OTHERS PROBABLY... |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/20` | 0.536970 | YOU MIGHT... |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/16` | 0.348763 | WHILE EXPLORING... |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/59` | 0.304825 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/32` | 0.304825 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/59` | 0.304825 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/32` | 0.304825 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/22` | 0.296446 | Surprise others with cunning uses of your stellar abilities, performing acts that  others weren't expecting or didn't know you could do. |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/14` | 0.280939 | DURING SOCIAL ENCOUNTERS... |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/12` | 0.274839 | DURING COMBAT ENCOUNTERS... |

### Query 21
- Text: Summarize Expect you to bore them with constant talk of stars and cosmic phenomena.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/25', 'PZO22001 Starfinder Player Core 138-149::/page/2/Text/11', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/25', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/24', 'PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/25` | 1.013646 | Expect you to bore them with constant talk of stars and cosmic phenomena. |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/11` | 0.544018 | As a solarian, your existence cycles between the aspects of  stars. You begin with two aspects: photon (the power of stars to |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/19` | 0.500508 | You balance your downtime between meditation and other activities. You might  create your own dedicated following to train a new generation of solarians or use  your flashy solarian powers to earn cre |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/2` | 0.456856 | You're a conduit for the stellar forces of the cosmos—a solar knight. The powers of gravity and light  represent the extremes of these forces, and you can attune yourself between them. As an agent of |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/22` | 0.455618 | Surprise others with cunning uses of your stellar abilities, performing acts that  others weren't expecting or didn't know you could do. |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/17` | 0.451660 | You steady your body and mind and attune yourself to the  stellar aspect of your choice. You become attuned to photon or  graviton. You can also manifest any of your solar manifestations  if they're c |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/12` | 0.448039 | emit heat, light, and plasma) and graviton (the power of stars to  attract and imprison objects through gravity). At any time, you're  considered graviton-attuned, photon-attuned, or unattuned.  Many |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/14` | 0.438340 | You extend your control of stellar forces to punish your foes.  Creatures that hit you with an attack suffer consequences  based on your attunement. |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/20` | 0.435027 | Your deep understanding of the stellar forces of the universe  manifests in a variety of tangible ways. You can create and  maintain three different manifestations: a solar flare, solar  nimbus, and s |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/24` | 0.427448 | Your ability to manipulate stellar forces is unparalleled.  Your proficiency rank for your solarian class DC increases  to master. |

### Query 22
- Text: Summarize Enjoy watching you fight or demonstrate your powers.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/26', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/17', 'PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/22']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/26', 'PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/27', 'PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/25']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/26` | 1.018592 | Enjoy watching you fight or demonstrate your powers. |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/17` | 0.628997 | You likely stick near the front of the group to quickly get into the fight. You use  your powers to overcome challenges, like moving debris or climbing strange terrain. |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/22` | 0.499152 | Surprise others with cunning uses of your stellar abilities, performing acts that  others weren't expecting or didn't know you could do. |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/15` | 0.435933 | Your weapon becomes an extension of yourself.  Your proficiency ranks for simple weapons,  martial weapons, and unarmed attacks increases  to master. |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/14` | 0.425651 | You extend your control of stellar forces to punish your foes.  Creatures that hit you with an attack suffer consequences  based on your attunement. |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/28` | 0.424215 | You rush forward with a blast of stellar energy, getting into  the thick of combat with ease. Stride twice. You gain a +10-foot  circumstance bonus to your Speed during these moves. |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/43` | 0.423400 | Your attacks create a brilliant eclipse that veil you from  the enemy's view. Make a Strike with your solar weapon or  your solar flare. On a hit, you create an impressive display of  solar energy bet |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/17` | 0.419242 | You steady your body and mind and attune yourself to the  stellar aspect of your choice. You become attuned to photon or  graviton. You can also manifest any of your solar manifestations  if they're c |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/13` | 0.416219 | You rush into the thick of things and attack with your solar manifestations. You  shift between battlefield control and heavy attacks, depending on your current  solar attunement. |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/2` | 0.410071 | You're a conduit for the stellar forces of the cosmos—a solar knight. The powers of gravity and light  represent the extremes of these forces, and you can attune yourself between them. As an agent of |

### Query 23
- Text: Summarize Think you'll be the voice of reason in a group.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/27', 'PZO22001 Starfinder Player Core 138-149::/page/3/Text/20', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/27', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/28', 'PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/27` | 1.016992 | Think you'll be the voice of reason in a group. |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/20` | 0.484294 | You can select one of the following weapon groups for your  weapon to be a part of. |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/17` | 0.481444 | You likely stick near the front of the group to quickly get into the fight. You use  your powers to overcome challenges, like moving debris or climbing strange terrain. |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/15` | 0.391463 | Which solar aspect you prefer might influence how you act in social circles. You might  be a chatterbox who makes friends easily or a smooth manipulator who uses your  abilities to coerce people. |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/26` | 0.363691 | Enjoy watching you fight or demonstrate your powers. |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/19` | 0.346469 | You balance your downtime between meditation and other activities. You might  create your own dedicated following to train a new generation of solarians or use  your flashy solarian powers to earn cre |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/5` | 0.342832 | Your careful training and honed senses give you increased  awareness of your surroundings. Your proficiency rank for  Perception increases to master. In addition, you gain a +2  circumstance bonus to |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/22` | 0.340725 | Surprise others with cunning uses of your stellar abilities, performing acts that  others weren't expecting or didn't know you could do. |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/26` | 0.338406 | You're a paragon among solarians, capable of shaping stellar  forces into powerful weapons that bend to your will. Your  proficiency ranks for your solar flare and solar weapon  increase to legendary. |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/46` | 0.316598 | **Trigger** You would be damage by an attack, spell, or other effect. **Requirements** You're aware of the triggering effect and not offguard. |

### Query 24
- Text: What is the rule about CLASS FEATURES?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/28', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/389', 'PZO22001 Starfinder Player Core 138-149::/page/6/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/28', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/29', 'PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/ListItem/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/28` | 0.841653 | CLASS FEATURES |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/389` | 0.758361 | Class Features |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/2` | 0.539156 | You'll see the following key traits in many solarian  class features. |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/33` | 0.495843 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/60` | 0.495843 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/60` | 0.495843 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/34` | 0.495843 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/46` | 0.495843 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/33` | 0.495843 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/Table/2` | 0.421916 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, stellar attunement, solar manifestations, solarian feat2Skill feat, solarian feat3General feat, skill increas |

### Query 25
- Text: What is the rule about You gain these abilities as a solarian. Abilities gained at higher levels list the level at  which you gain them next to the features' names.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/29', 'PZO22001 Starfinder Player Core 138-149::/page/3/Text/37', 'PZO22001 Starfinder Player Core 138-149::/page/2/Table/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/29', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/31', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/28']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/29` | 0.975775 | You gain these abilities as a solarian. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/37` | 0.783815 | Similar to spells, some solarian abilities get more  powerful as you increase in level. These abilities ends  with one or more "Level" entries. This either lists the  levels at which the ability gets |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/Table/2` | 0.699535 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, stellar attunement, solar manifestations, solarian feat2Skill feat, solarian feat3General feat, skill increas |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/40` | 0.634718 | At 1st level and every even-numbered level, you gain a  solarian class feat. These begin on page 143. |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/2` | 0.621289 | At each level that you gain a solarian feat, you can select one of  the following feats. You must satisfy any prerequisites before  taking the feat. |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/2` | 0.601146 | You'll see the following key traits in many solarian  class features. |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409` | 0.599069 | Attribute boosts, skill feat, solarian feat |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429` | 0.599069 | Attribute boosts, skill feat, solarian feat |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/43` | 0.574499 | At 2nd level and every 2 levels thereafter, you gain a skill  feat. Skill feats can be found in Chapter 5 and have the skill  trait. You must be trained or better in the corresponding skill  to select |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/26` | 0.563806 | You're a paragon among solarians, capable of shaping stellar  forces into powerful weapons that bend to your will. Your  proficiency ranks for your solar flare and solar weapon  increase to legendary. |

### Query 26
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/31', 'PZO22001 Starfinder Player Core 138-149::/page/11/Text/31', 'PZO22001 Starfinder Player Core 138-149::/page/9/Text/58']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/31', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/29', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/32']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/32` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/31` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/58` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/31` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/58` | 0.838541 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/62` | 0.569679 | **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/50` | 0.569679 | **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/74` | 0.524467 | **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/45` | 0.495539 | **INTRODUCTION** **ANCESTRIES & ** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/33` | 0.495539 | **INTRODUCTION** **ANCESTRIES & ** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/1` | 0.473765 | **KEY TERMS** |

### Query 27
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/32', 'PZO22001 Starfinder Player Core 138-149::/page/9/Text/59', 'PZO22001 Starfinder Player Core 138-149::/page/3/Text/59']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/32', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/33', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/31', 'PZO22001 Starfinder Player Core 138-149::/page/9/Text/59', 'PZO22001 Starfinder Player Core 138-149::/page/11/Text/32', 'PZO22001 Starfinder Player Core 138-149::/page/3/Text/59']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/9/Text/59` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/11/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/3/Text/59` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/32` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/59` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/59` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/32` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/3` | 0.726682 | ANCESTRY AND BACKGROUND |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/45` | 0.672101 | **INTRODUCTION** **ANCESTRIES & ** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/33` | 0.672101 | **INTRODUCTION** **ANCESTRIES & ** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/50` | 0.594354 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/62` | 0.594354 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/4` | 0.395462 | In addition to what you get from your class at 1st level, you  have the benefits of your selected ancestry and background, as  described in Chapter 2. |

### Query 28
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/33']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/33', 'PZO22001 Starfinder Player Core 138-149::/page/3/Text/60', 'PZO22001 Starfinder Player Core 138-149::/page/5/Text/46']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/33', 'PZO22001 Starfinder Player Core 138-149::/page/9/Text/60', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/34', 'PZO22001 Starfinder Player Core 138-149::/page/3/Text/60', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/32', 'PZO22001 Starfinder Player Core 138-149::/page/5/Text/46', 'PZO22001 Starfinder Player Core 138-149::/page/11/Text/33', 'PZO22001 Starfinder Player Core 138-149::/page/7/Text/34']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/9/Text/60` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/3/Text/60` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/5/Text/46` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/11/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/7/Text/34` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/33` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/60` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/46` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/34` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/60` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/33` | 0.910061 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/28` | 0.573477 | CLASS FEATURES |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/61` | 0.515930 | **CLASS DC** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/389` | 0.498036 | Class Features |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/74` | 0.463681 | **INDEX** |

### Query 29
- Text: Summarize **Envoy**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/34']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/9/Text/61', 'PZO22001 Starfinder Player Core 138-149::/page/5/Text/47', 'PZO22001 Starfinder Player Core 138-149::/page/3/Text/61']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/34', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/35', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/33']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/35` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/33` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/47` | 0.951326 | **Envoy** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/61` | 0.951326 | **Envoy** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/61` | 0.951326 | **Envoy** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/34` | 0.909326 | **Envoy** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/35` | 0.909326 | **Envoy** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/34` | 0.909326 | **Envoy** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/48` | 0.397750 | **CHARACTER ** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/74` | 0.382028 | **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/65` | 0.364330 | **Soldier** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/51` | 0.364330 | **Soldier** |

### Query 30
- Text: Summarize **Mystic**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/35', 'PZO22001 Starfinder Player Core 138-149::/page/3/Text/62', 'PZO22001 Starfinder Player Core 138-149::/page/11/Text/35']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/35', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/34', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/36']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/36` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/35` | 0.959378 | **Mystic** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/62` | 0.959378 | **Mystic** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/35` | 0.959378 | **Mystic** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/36` | 0.917378 | **Mystic** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/48` | 0.728194 | **Mystic** **Operative ** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/62` | 0.728194 | **Mystic** **Operative ** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/31` | 0.344700 | **ATTUNED** **DARKNESS** **DEATH** **DISHARMONY** **SOLARIAN** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/1` | 0.339324 | **KEY TERMS** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/14` | 0.322429 | **ATTUNED** **MANIFESTATION** **SOLARIAN** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/40` | 0.322429 | **ATTUNED** **MANIFESTATION** **SOLARIAN** |

### Query 31
- Text: Summarize **Operative **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/36']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/36', 'PZO22001 Starfinder Player Core 138-149::/page/3/Text/63', 'PZO22001 Starfinder Player Core 138-149::/page/5/Text/48']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/36', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/35', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/37']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/35` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/37` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/36` | 0.958402 | **Operative ** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/63` | 0.958402 | **Operative ** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/48` | 0.725410 | **Mystic** **Operative ** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/62` | 0.683410 | **Mystic** **Operative ** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/37` | 0.572748 | **Operative ** **Solarian** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/12` | 0.361709 | **MEDITATIVE ANALYSIS **[one-action] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/1` | 0.361666 | **KEY TERMS** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/51` | 0.345470 | **Soldier** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/38` | 0.345470 | **Soldier** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/38` | 0.345470 | **Soldier** |

### Query 32
- Text: Summarize **Solarian**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/37', 'PZO22001 Starfinder Player Core 138-149::/page/3/Text/64', 'PZO22001 Starfinder Player Core 138-149::/page/9/Text/63']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/37', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/38', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/36']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/38` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/36` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/37` | 0.974700 | **Solarian** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/64` | 0.974700 | **Solarian** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/63` | 0.974700 | **Solarian** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/49` | 0.932700 | **Solarian** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/36` | 0.932700 | **Solarian** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/24` | 0.855583 | **SOLARIAN** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/53` | 0.855583 | **SOLARIAN** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/8` | 0.855583 | **SOLARIAN** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/4` | 0.855583 | **SOLARIAN** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/24` | 0.855583 | **SOLARIAN** |

### Query 33
- Text: Summarize **Soldier**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/38']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/38', 'PZO22001 Starfinder Player Core 138-149::/page/7/Text/38', 'PZO22001 Starfinder Player Core 138-149::/page/3/Text/65']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/38', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/40', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/37']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/37` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/38` | 0.953061 | **Soldier** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/65` | 0.953061 | **Soldier** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/38` | 0.953061 | **Soldier** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/51` | 0.911061 | **Soldier** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/64` | 0.911061 | **Soldier** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/48` | 0.500936 | **CHARACTER ** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/37` | 0.468437 | **Operative ** **Solarian** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/64` | 0.454361 | **Solarian** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/37` | 0.454361 | **Solarian** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/4` | 0.448013 | **SOLARIAN** |

### Query 34
- Text: Summarize **Witchwarper**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/40']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/3/Text/66', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/40', 'PZO22001 Starfinder Player Core 138-149::/page/5/Text/52']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/40', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/38', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/41']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/38` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/41` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/66` | 0.988715 | **Witchwarper** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/40` | 0.988715 | **Witchwarper** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/52` | 0.988715 | **Witchwarper** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/65` | 0.946715 | **Witchwarper** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/39` | 0.946715 | **Witchwarper** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/40` | 0.808939 | **Witchwarper** **Archetypes** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/48` | 0.371477 | **CHARACTER ** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/38` | 0.342425 | **Soldier** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/51` | 0.342425 | **Soldier** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/65` | 0.342425 | **Soldier** |

### Query 35
- Text: Summarize **Archetypes**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/41', 'PZO22001 Starfinder Player Core 138-149::/page/9/Text/66', 'PZO22001 Starfinder Player Core 138-149::/page/3/Text/67']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/41', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/42', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/40']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/40` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/41` | 0.973323 | **Archetypes** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/66` | 0.973323 | **Archetypes** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/67` | 0.973323 | **Archetypes** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/53` | 0.931323 | **Archetypes** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/40` | 0.931323 | **Archetypes** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/40` | 0.668054 | **Witchwarper** **Archetypes** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/48` | 0.393863 | **CHARACTER ** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/74` | 0.382400 | **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/59` | 0.376744 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/59` | 0.376744 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 36
- Text: What is the rule about **SKILLS** **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/42']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/3/Text/68', 'PZO22001 Starfinder Player Core 138-149::/page/9/Text/67', 'PZO22001 Starfinder Player Core 138-149::/page/5/Text/54']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/42', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/43', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/41']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/43` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/41` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/68` | 0.909736 | **SKILLS** **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/67` | 0.909736 | **SKILLS** **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/54` | 0.909736 | **SKILLS** **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/42` | 0.867736 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/41` | 0.656535 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/55` | 0.656535 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/42` | 0.613813 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/41` | 0.613813 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/43` | 0.558305 | At 2nd level and every 2 levels thereafter, you gain a skill  feat. Skill feats can be found in Chapter 5 and have the skill  trait. You must be trained or better in the corresponding skill  to select |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/3/SectionHeader/41` | 0.542737 | SKILL FEATS 2ND |

### Query 37
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/43']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/9/Text/69', 'PZO22001 Starfinder Player Core 138-149::/page/3/Text/69', 'PZO22001 Starfinder Player Core 138-149::/page/11/Text/42']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/43', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/44', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/42']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/44` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/42` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/69` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/69` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/42` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/43` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/55` | 0.902726 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/43` | 0.902726 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/74` | 0.421643 | **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/50` | 0.409329 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/62` | 0.409329 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/1` | 0.407120 | **KEY TERMS** |

### Query 38
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/44', 'PZO22001 Starfinder Player Core 138-149::/page/3/Text/70', 'PZO22001 Starfinder Player Core 138-149::/page/7/Text/44']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/44', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/45', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/43']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/45` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/43` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/44` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/70` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/44` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/56` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/43` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/70` | 0.740792 | **SPELLS** **PLAYING THE ** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/55` | 0.388254 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/41` | 0.388254 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/42` | 0.332025 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/68` | 0.332025 | **SKILLS** **FEATS** |

### Query 39
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/45']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/45', 'PZO22001 Starfinder Player Core 138-149::/page/5/Text/57', 'PZO22001 Starfinder Player Core 138-149::/page/3/Text/71']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/45', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/44', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/46']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/44` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/46` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/45` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/57` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/71` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/45` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/44` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/71` | 0.663024 | **GAME** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/70` | 0.576671 | **SPELLS** **PLAYING THE ** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/58` | 0.418586 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/58` | 0.418586 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/31` | 0.418586 | **INTRODUCTION** |

### Query 40
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/46']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/11/Text/45', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/46', 'PZO22001 Starfinder Player Core 138-149::/page/9/Text/72']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/46', 'PZO22001 Starfinder Player Core 138-149::/page/11/Text/45', 'PZO22001 Starfinder Player Core 138-149::/page/5/Text/58', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/45', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/47', 'PZO22001 Starfinder Player Core 138-149::/page/9/Text/72', 'PZO22001 Starfinder Player Core 138-149::/page/7/Text/46', 'PZO22001 Starfinder Player Core 138-149::/page/3/Text/72']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/11/Text/45` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/5/Text/58` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/45` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/9/Text/72` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/7/Text/46` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/3/Text/72` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/45` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/46` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/72` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/58` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/46` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/72` | 0.645203 | **CONDITIONS ** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/73` | 0.573689 | **APPENDIX** **GLOSSARY & ** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/1` | 0.439047 | **KEY TERMS** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/74` | 0.423722 | **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/59` | 0.416141 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 41
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/47']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/11/Text/46', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/47', 'PZO22001 Starfinder Player Core 138-149::/page/9/Text/73']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/47', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/48', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/46']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/48` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/46` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/46` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/47` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/73` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/59` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/47` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/73` | 0.697531 | **APPENDIX** **GLOSSARY & ** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/74` | 0.618357 | **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/9` | 0.388122 | **ATTUNED** **CYCLE** **FLOURISH** **SOLARIAN** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/10` | 0.388122 | **ATTUNED** **CYCLE** **FLOURISH** **SOLARIAN** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/42` | 0.388122 | **ATTUNED** **CYCLE** **FLOURISH** **SOLARIAN** |

### Query 42
- Text: What is the rule about **CHARACTER ** **SHEET**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/48']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/48', 'PZO22001 Starfinder Player Core 138-149::/page/7/Text/48', 'PZO22001 Starfinder Player Core 138-149::/page/7/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/48', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/47', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/49']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/49` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/48` | 0.859300 | **CHARACTER ** **SHEET** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/48` | 0.632820 | **CHARACTER ** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/4` | 0.445015 | **SHEET** of resistance when you use this action, depending on your  current attunement. |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/66` | 0.392353 | **Archetypes** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/53` | 0.392353 | **Archetypes** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/41` | 0.392353 | **Archetypes** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/67` | 0.392353 | **Archetypes** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/40` | 0.392353 | **Archetypes** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/71` | 0.380766 | **GAME** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/72` | 0.378942 | **CONDITIONS ** |

### Query 43
- Text: Summarize **INITIAL PROFICIENCIES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/49']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/49', 'PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/8', 'PZO22001 Starfinder Player Core 138-149::/page/2/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/49', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/48', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/50']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/48` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/50` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/49` | 1.001056 | **INITIAL PROFICIENCIES** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/8` | 0.851001 | INITIAL PROFICIENCIES |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/9` | 0.516203 | At 1st level, you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start of  this class. |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/58` | 0.400378 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/58` | 0.400378 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/31` | 0.400378 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/31` | 0.400378 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/50` | 0.376596 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/391` | 0.365501 | Ancestry and background, attribute boosts, initial proficiencies, stellar attunement, solar manifestations, solarian feat |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/62` | 0.353772 | **BACKGROUNDS** |

### Query 44
- Text: What is the rule about At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/50']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/50', 'PZO22001 Starfinder Player Core 138-149::/page/3/Text/49', 'PZO22001 Starfinder Player Core 138-149::/page/2/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/50', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/49', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/51']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/51` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/50` | 0.992024 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/49` | 0.743637 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use this increase either to increase your  proficiency rank to trained in one skill you're untrained in, or  to increase |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/9` | 0.706615 | At 1st level, you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start of  this class. |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/50` | 0.611362 | At 7th level, you can use skill increases to increase your  proficiency rank to master in a skill in which you're already  an expert, and at 15th level, you can use them to increase  your proficiency |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/13` | 0.538649 | You've spent so much time in armor that you know  how to make the most of its protection. Your  proficiency ranks for light armor, medium armor,  and unarmored defense increase to expert. |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/43` | 0.528757 | At 2nd level and every 2 levels thereafter, you gain a skill  feat. Skill feats can be found in Chapter 5 and have the skill  trait. You must be trained or better in the corresponding skill  to select |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/15` | 0.504513 | Your weapon becomes an extension of yourself.  Your proficiency ranks for simple weapons,  martial weapons, and unarmed attacks increases  to master. |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/22` | 0.500314 | You deftly protect yourself in almost any situation. Your  proficiency ranks for light armor, medium armor, and  unarmored defense increase to master. |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/29` | 0.474951 | You gain these abilities as a solarian. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/11` | 0.473065 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |

### Query 45
- Text: Summarize **PERCEPTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/51']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/51', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/52', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/51', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/52', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/50']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/52` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/50` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/51` | 0.934058 | **PERCEPTION** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/52` | 0.581413 | Expert in Perception |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/31` | 0.485002 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/58` | 0.443002 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/31` | 0.443002 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/58` | 0.443002 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/62` | 0.438809 | **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/50` | 0.438809 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/74` | 0.414769 | **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/5` | 0.406474 | Your careful training and honed senses give you increased  awareness of your surroundings. Your proficiency rank for  Perception increases to master. In addition, you gain a +2  circumstance bonus to |

### Query 46
- Text: Summarize Expert in Perception
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/52']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/52', 'PZO22001 Starfinder Player Core 138-149::/page/4/Text/5', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/51']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/52', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/53', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/51']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/53` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/51` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/52` | 0.925572 | Expert in Perception |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/5` | 0.536514 | Your careful training and honed senses give you increased  awareness of your surroundings. Your proficiency rank for  Perception increases to master. In addition, you gain a +2  circumstance bonus to |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/51` | 0.532067 | **PERCEPTION** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/54` | 0.460649 | Trained in Fortitude Expert in Reflex Expert in Will |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/411` | 0.359787 | Armor expertise, general feat, skill increase |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/13` | 0.346273 | You've spent so much time in armor that you know  how to make the most of its protection. Your  proficiency ranks for light armor, medium armor,  and unarmored defense increase to expert. |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/403` | 0.335872 | General feat, skill increase, stellar senses, weapon specialization |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/4/SectionHeader/4` | 0.325566 | STELLAR SENSES 7TH |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/4/SectionHeader/8` | 0.321593 | SOLARIAN EXPERTISE 9TH |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/4/SectionHeader/12` | 0.318743 | ARMOR EXPERTISE 11TH |

### Query 47
- Text: What is the rule about **SAVING THROWS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/53']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/53', 'PZO22001 Starfinder Player Core 138-149::/page/4/Text/17', 'PZO22001 Starfinder Player Core 138-149::/page/6/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/53', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/54', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/52']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/54` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/52` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/53` | 0.904955 | **SAVING THROWS** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/17` | 0.375591 | You avoid harm by manipulating gravitational forces to  protect your body. Your proficiency rank for Reflex saves  increases to master. When you roll a success on a Reflex save,  you get a critical su |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/6` | 0.358234 | **Flourish:** Actions with the flourish trait are special  techniques that require too much exertion for you to  perform frequently. You can only use one action with  the flourish trait per round. |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/50` | 0.297302 | Your soul becomes fuel, burning away your life force to purge  an affliction. Choose a disease or poison you're afflicted by.  Lose a number of Hit Points equal to the level of the affliction.  Attemp |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/11` | 0.294695 | **Graviton-Attuned** A creature that fails its save is knocked  prone. |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/23` | 0.293679 | save against your class DC or be suppressed for 1 round (2  rounds on a critical failure). |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/5` | 0.291301 | **Graviton-Attuned** If the Strike is a critical success, the target  must succeed at a Fortitude save against your class DC or  become enfeebled 1 until the end of its turn. |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/10` | 0.278915 | **Photon-Attuned** For the duration, if the target you struck  provides you cover against an enemy's attack, that enemy  takes a –1 circumstance penalty to their attack roll. |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/6` | 0.278901 | **Photon-Attuned** If the Strike is a critical success, the target  must succeed at a Fortitude save against your class DC or  become clumsy 1 until the start of its turn. |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/29` | 0.278194 | **Graviton-Attuned** When you finish your Strides, enemies  within 15 feet of you must attempt a Fortitude save against  your class DC. On a failure, they're pulled directly toward  you, ending in an |

### Query 48
- Text: Summarize Trained in Fortitude Expert in Reflex Expert in Will
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/54']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/54', 'PZO22001 Starfinder Player Core 138-149::/page/3/Text/53', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/52']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/54', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/55', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/53']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/55` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/53` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/54` | 1.024915 | Trained in Fortitude Expert in Reflex Expert in Will |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/53` | 0.530569 | Stellar energy flows throughout your entire being like  an unstoppable tidal wave, strengthening both body and  mind. Your proficiency rank in Fortitude saves increases to  expert. When you roll a suc |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/52` | 0.474308 | Expert in Perception |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/411` | 0.432149 | Armor expertise, general feat, skill increase |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/17` | 0.420056 | You avoid harm by manipulating gravitational forces to  protect your body. Your proficiency rank for Reflex saves  increases to master. When you roll a success on a Reflex save,  you get a critical su |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/56` | 0.410358 | Trained in Athletics Trained in a number of additional  skills equal to 4 plus your Intelligence  modifier |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/13` | 0.407282 | You've spent so much time in armor that you know  how to make the most of its protection. Your  proficiency ranks for light armor, medium armor,  and unarmored defense increase to expert. |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/60` | 0.393062 | Trained in light armor Trained in medium armor Trained in unarmored defense |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/11` | 0.387260 | Your solar nimbus protects you against mental intrusions. Your  proficiency rank for Will saves increases to master. When you  roll a success on a Will save against a mental or incapacitation  effect, |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/5` | 0.378139 | Your careful training and honed senses give you increased  awareness of your surroundings. Your proficiency rank for  Perception increases to master. In addition, you gain a +2  circumstance bonus to |

### Query 49
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/55']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/55', 'PZO22001 Starfinder Player Core 138-149::/page/7/Text/41', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/42']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/55', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/56', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/54']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/56` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/54` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/55` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/41` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/42` | 0.693094 | **SKILLS** **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/54` | 0.651094 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/67` | 0.651094 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/68` | 0.651094 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/3/SectionHeader/36` | 0.475137 | **SCALED ABILITIES** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/43` | 0.458870 | At 2nd level and every 2 levels thereafter, you gain a skill  feat. Skill feats can be found in Chapter 5 and have the skill  trait. You must be trained or better in the corresponding skill  to select |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/41` | 0.436424 | **Failure** Your attack deals damage equal to your Strength  modifier. It doesn't count as a hit and doesn't trigger any  other special abilities. |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/49` | 0.422118 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use this increase either to increase your  proficiency rank to trained in one skill you're untrained in, or  to increase |

### Query 50
- Text: What is the rule about Trained in Athletics Trained in a number of additional  skills equal to 4 plus your Intelligence  modifier?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/56']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/56', 'PZO22001 Starfinder Player Core 138-149::/page/3/Text/49', 'PZO22001 Starfinder Player Core 138-149::/page/3/Text/43']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/56', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/55', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/57']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/55` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/57` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/56` | 0.951853 | Trained in Athletics Trained in a number of additional  skills equal to 4 plus your Intelligence  modifier |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/49` | 0.560826 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use this increase either to increase your  proficiency rank to trained in one skill you're untrained in, or  to increase |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/43` | 0.511559 | At 2nd level and every 2 levels thereafter, you gain a skill  feat. Skill feats can be found in Chapter 5 and have the skill  trait. You must be trained or better in the corresponding skill  to select |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/50` | 0.471554 | At 7th level, you can use skill increases to increase your  proficiency rank to master in a skill in which you're already  an expert, and at 15th level, you can use them to increase  your proficiency |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/7` | 0.448773 | You've learned how to inflict greater injuries with the weapons  you've practiced with most. You deal 2 additional damage  with weapons and unarmed attacks in which you're an expert.  This damage incr |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/7` | 0.447301 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier is  already +4 or higher, it takes two boosts to increase it; you get a |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/50` | 0.444857 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/5` | 0.443890 | Your careful training and honed senses give you increased  awareness of your surroundings. Your proficiency rank for  Perception increases to master. In addition, you gain a +2  circumstance bonus to |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/25` | 0.439905 | Your training has helped you adapt to bulkier armor. You're  trained in heavy armor. Whenever you gain a class feature that  grants you expert or greater proficiency in medium armor, you  also gain th |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/6` | 0.417382 | In addition to what you get from your class at 1st level, you have  four free boosts to different attribute modifiers. |

### Query 51
- Text: What is the rule about **ATTACKS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/57']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/57', 'PZO22001 Starfinder Player Core 138-149::/page/6/Text/10', 'PZO22001 Starfinder Player Core 138-149::/page/10/Text/51']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/57', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/58', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/56']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/58` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/56` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/57` | 0.855189 | **ATTACKS** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/10` | 0.518049 | **Photon-Attuned** For the duration, if the target you struck  provides you cover against an enemy's attack, that enemy  takes a –1 circumstance penalty to their attack roll. |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/51` | 0.510589 | **Photon-Attuned** You're concealed to each target of this  attack until the start of your next turn. |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/7` | 0.452103 | You coordinate your attacks with both your solar flare and solar  weapon. Make two Strikes at the same target, one with your  solar weapon and one with your solar flare, each using your  current multi |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/11` | 0.439029 | **Graviton-Attuned** Increase the range to double your Speed. **Photon-Attuned** If a Strike made as part of this action is a  critical success, the struck target is dazzled until the end  of its next |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/9` | 0.417917 | **Graviton-Attuned** For the duration, if you don't have any  cover against an attack targeting you, you gain lesser cover  against that attack. |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/14` | 0.413599 | **ATTUNE **[one-action] |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/6` | 0.411859 | **Photon-Attuned** If the Strike is a critical success, the target  must succeed at a Fortitude save against your class DC or  become clumsy 1 until the start of its turn. |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/20` | 0.399869 | **Graviton-Attuned** If your shield is destroyed, it releases a  shock wave. Adjacent enemies must succeed at a Fortitude |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/4` | 0.398736 | Your nimbus surges with energy, forcing an opening in your foe's  defenses. Make a melee Strike against the triggering creature.  This Strike doesn't count toward your multiple attack penalty,  and yo |

### Query 52
- Text: What is the rule about Trained in simple weapons Trained in martial weapons Trained in unarmed attacks?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/58']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/58', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/60', 'PZO22001 Starfinder Player Core 138-149::/page/4/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/58', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/57', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/59']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/57` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/59` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/58` | 0.918604 | Trained in simple weapons Trained in martial weapons Trained in unarmed attacks |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/60` | 0.673197 | Trained in light armor Trained in medium armor Trained in unarmored defense |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/15` | 0.571189 | Your weapon becomes an extension of yourself.  Your proficiency ranks for simple weapons,  martial weapons, and unarmed attacks increases  to master. |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/7` | 0.444541 | You've learned how to inflict greater injuries with the weapons  you've practiced with most. You deal 2 additional damage  with weapons and unarmed attacks in which you're an expert.  This damage incr |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/25` | 0.434431 | Your training has helped you adapt to bulkier armor. You're  trained in heavy armor. Whenever you gain a class feature that  grants you expert or greater proficiency in medium armor, you  also gain th |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/22` | 0.431511 | You deftly protect yourself in almost any situation. Your  proficiency ranks for light armor, medium armor, and  unarmored defense increase to master. |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/3` | 0.428917 | Your connection to stellar forces make your weapons lethal.  Your proficiency ranks for simple weapons, martial weapons,  and unarmed attacks increase to expert. Whenever you get a  critical hit with |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/20` | 0.428772 | Your damage from weapon specialization increases to 4 with  weapons and unarmed attacks in which you're an expert, 6 if  you're a master, and 8 if you're legendary. |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/50` | 0.417411 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/7` | 0.395212 | You coordinate your attacks with both your solar flare and solar  weapon. Make two Strikes at the same target, one with your  solar weapon and one with your solar flare, each using your  current multi |

### Query 53
- Text: Summarize **DEFENSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/59']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/59', 'PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/16', 'PZO22001 Starfinder Player Core 138-149::/page/4/Text/22']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/59', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/58', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/60']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/58` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/60` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/59` | 0.959826 | **DEFENSES** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/16` | 0.473924 | **SOLAR SHIELD** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/22` | 0.454414 | You deftly protect yourself in almost any situation. Your  proficiency ranks for light armor, medium armor, and  unarmored defense increase to master. |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/58` | 0.411981 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/58` | 0.411981 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/31` | 0.411981 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/31` | 0.411981 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/62` | 0.400430 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/50` | 0.400430 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/51` | 0.397006 | **Soldier** |

### Query 54
- Text: Summarize Trained in light armor Trained in medium armor Trained in unarmored defense
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/60']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/60', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/58', 'PZO22001 Starfinder Player Core 138-149::/page/4/Text/22']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/60', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/61', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/59']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/61` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/59` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/60` | 1.029022 | Trained in light armor Trained in medium armor Trained in unarmored defense |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/58` | 0.774155 | Trained in simple weapons Trained in martial weapons Trained in unarmed attacks |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/22` | 0.695276 | You deftly protect yourself in almost any situation. Your  proficiency ranks for light armor, medium armor, and  unarmored defense increase to master. |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/13` | 0.639611 | You've spent so much time in armor that you know  how to make the most of its protection. Your  proficiency ranks for light armor, medium armor,  and unarmored defense increase to expert. |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/25` | 0.629267 | Your training has helped you adapt to bulkier armor. You're  trained in heavy armor. Whenever you gain a class feature that  grants you expert or greater proficiency in medium armor, you  also gain th |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/411` | 0.434050 | Armor expertise, general feat, skill increase |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/15` | 0.431828 | Your weapon becomes an extension of yourself.  Your proficiency ranks for simple weapons,  martial weapons, and unarmed attacks increases  to master. |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/7` | 0.426993 | You've learned how to inflict greater injuries with the weapons  you've practiced with most. You deal 2 additional damage  with weapons and unarmed attacks in which you're an expert.  This damage incr |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/50` | 0.423201 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/20` | 0.413710 | Your damage from weapon specialization increases to 4 with  weapons and unarmed attacks in which you're an expert, 6 if  you're a master, and 8 if you're legendary. |

### Query 55
- Text: What is the rule about **CLASS DC**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/61']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/61', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/33', 'PZO22001 Starfinder Player Core 138-149::/page/11/Text/33']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/61', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/62', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/60']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/62` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/60` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/61` | 0.881905 | **CLASS DC** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/33` | 0.521525 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/33` | 0.521525 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/60` | 0.491525 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/46` | 0.491525 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/60` | 0.491525 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/34` | 0.491525 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/62` | 0.449699 | Trained in solarian class DC |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/23` | 0.444425 | save against your class DC or be suppressed for 1 round (2  rounds on a critical failure). |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/28` | 0.381301 | CLASS FEATURES |

### Query 56
- Text: What is the rule about Trained in solarian class DC?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/62']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/62', 'PZO22001 Starfinder Player Core 138-149::/page/4/Text/24', 'PZO22001 Starfinder Player Core 138-149::/page/4/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/1/Text/62', 'PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/61']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/61` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/62` | 0.905344 | Trained in solarian class DC |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/24` | 0.673637 | Your ability to manipulate stellar forces is unparalleled.  Your proficiency rank for your solarian class DC increases  to master. |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/9` | 0.630162 | Your ability to manipulate stellar forces has improved. Your  proficiency rank for your solarian class DC increases to expert. |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/40` | 0.536006 | At 1st level and every even-numbered level, you gain a  solarian class feat. These begin on page 143. |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/2` | 0.508471 | You'll see the following key traits in many solarian  class features. |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/421` | 0.479806 | Skill feat, solarian feat |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/417` | 0.479806 | Skill feat, solarian feat |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/425` | 0.479806 | Skill feat, solarian feat |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/413` | 0.479806 | Skill feat, solarian feat |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/401` | 0.479806 | Skill feat, solarian feat |

### Query 57
- Text: Summarize **SOLARIAN ADVANCEMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/37', 'PZO22001 Starfinder Player Core 138-149::/page/11/Text/36']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/62', 'PZO22001 Starfinder Player Core 138-149::/page/2/Table/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/1/Text/62` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/Table/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/1` | 1.009234 | **SOLARIAN ADVANCEMENT** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/37` | 0.737117 | **Solarian** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/36` | 0.737117 | **Solarian** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/64` | 0.695117 | **Solarian** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/49` | 0.695117 | **Solarian** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/63` | 0.695117 | **Solarian** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/24` | 0.685352 | **SOLARIAN** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/24` | 0.685352 | **SOLARIAN** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/53` | 0.685352 | **SOLARIAN** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/8` | 0.685352 | **SOLARIAN** |

### Query 58
- Text: Lookup values for Your LevelClass Features1Ancestry and background, attribute boosts,
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/Table/2']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/Text/4', 'PZO22001 Starfinder Player Core 138-149::/page/2/Table/2', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/Table/2', 'PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/388']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/388` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/4` | 0.671822 | In addition to what you get from your class at 1st level, you  have the benefits of your selected ancestry and background, as  described in Chapter 2. |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/Table/2` | 0.641573 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, stellar attunement, solar manifestations, solarian feat2Skill feat, solarian feat3General feat, skill increas |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/8` | 0.628016 | At 1st level, your class gives you  an attribute boost to Strength. |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/6` | 0.582096 | In addition to what you get from your class at 1st level, you have  four free boosts to different attribute modifiers. |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/7` | 0.533659 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier is  already +4 or higher, it takes two boosts to increase it; you get a |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/1` | 0.533214 | thereafter. The list of ancestry feats available to you can be  found in your ancestry's entry in Chapter 2. |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/389` | 0.528105 | Class Features |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/399` | 0.504091 | Ancestry feat, attribute boosts, skill increase, solar weapon expertise |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/391` | 0.503923 | Ancestry and background, attribute boosts, initial proficiencies, stellar attunement, solar manifestations, solarian feat |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/29` | 0.480840 | You gain these abilities as a solarian. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |

### Query 59
- Text: Summarize Your Level
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/388']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/388', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/600', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/554']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/388', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/389', 'PZO22001 Starfinder Player Core 138-149::/page/2/Table/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/389` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/Table/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/388` | 0.853813 | Your Level |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/600` | 0.729099 | Level |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/554` | 0.729099 | Level |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/35` | 0.549996 | 2ND LEVEL |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/26` | 0.534036 | 4TH LEVEL |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/10` | 0.523376 | 18TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/2` | 0.514596 | 8TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/18` | 0.513306 | 14TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/1` | 0.501266 | 16TH LEVEL |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/21` | 0.497936 | 20TH LEVEL |

### Query 60
- Text: What is the rule about Class Features?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/389']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/389', 'PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/28', 'PZO22001 Starfinder Player Core 138-149::/page/6/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/389', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/390', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/388']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/390` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/388` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/389` | 0.835742 | Class Features |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/1/SectionHeader/28` | 0.700239 | CLASS FEATURES |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/2` | 0.560356 | You'll see the following key traits in many solarian  class features. |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/Table/2` | 0.435434 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, stellar attunement, solar manifestations, solarian feat2Skill feat, solarian feat3General feat, skill increas |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/8` | 0.410975 | At 1st level, your class gives you  an attribute boost to Strength. |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/46` | 0.407880 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/60` | 0.407880 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/33` | 0.407880 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/34` | 0.407880 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/60` | 0.407880 | **CLASSES** |

### Query 61
- Text: Summarize 1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/390']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/390', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/590', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/632']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/390', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/391', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/389']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/391` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/389` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/390` | 0.669108 | 1 |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/632` | 0.669108 | 1 |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/590` | 0.669108 | 1 |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/564` | 0.627108 | 1 |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/640` | 0.627108 | 1 |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/596` | 0.627108 | 1 |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/624` | 0.627108 | 1 |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/584` | 0.513765 | 2 |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/622` | 0.513765 | 2 |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/392` | 0.513765 | 2 |

### Query 62
- Text: What is the rule about Ancestry and background, attribute boosts,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/391']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/391', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/399', 'PZO22001 Starfinder Player Core 138-149::/page/2/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/391', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/390', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/392']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/390` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/392` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/391` | 0.645194 | Ancestry and background, attribute boosts, initial proficiencies, stellar attunement, solar manifestations, solarian feat |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/399` | 0.617882 | Ancestry feat, attribute boosts, skill increase, solar weapon expertise |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/4` | 0.581688 | In addition to what you get from your class at 1st level, you  have the benefits of your selected ancestry and background, as  described in Chapter 2. |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/1` | 0.512047 | thereafter. The list of ancestry feats available to you can be  found in your ancestry's entry in Chapter 2. |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/7` | 0.509477 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier is  already +4 or higher, it takes two boosts to increase it; you get a |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/3` | 0.506753 | ANCESTRY AND BACKGROUND |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/59` | 0.496934 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/59` | 0.496934 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/32` | 0.496934 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/32` | 0.496934 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 63
- Text: Summarize 2
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/392']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/584', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/392', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/586']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/392', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/391', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/391` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/584` | 0.689465 | 2 |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/392` | 0.689465 | 2 |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/586` | 0.689465 | 2 |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/604` | 0.647465 | 2 |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/622` | 0.647465 | 2 |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/616` | 0.647465 | 2 |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/624` | 0.459336 | 1 |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/390` | 0.459336 | 1 |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/596` | 0.459336 | 1 |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/590` | 0.459336 | 1 |

### Query 64
- Text: What is the rule about Skill feat, solarian feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/425']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/394', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/392']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/394` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/392` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393` | 0.931260 | Skill feat, solarian feat |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397` | 0.931260 | Skill feat, solarian feat |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/425` | 0.931260 | Skill feat, solarian feat |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/421` | 0.889260 | Skill feat, solarian feat |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/401` | 0.889260 | Skill feat, solarian feat |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/413` | 0.889260 | Skill feat, solarian feat |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/405` | 0.889260 | Skill feat, solarian feat |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/417` | 0.889260 | Skill feat, solarian feat |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409` | 0.775088 | Attribute boosts, skill feat, solarian feat |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429` | 0.775088 | Attribute boosts, skill feat, solarian feat |

### Query 65
- Text: Summarize 3
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/394']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/394', 'PZO22001 Starfinder Player Core 138-149::/page/11/Text/30', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/584']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/394', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/395', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/395` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/394` | 0.731895 | 3 |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/30` | 0.731895 | 3 |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/584` | 0.558533 | 2 |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/622` | 0.516533 | 2 |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/616` | 0.516533 | 2 |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/604` | 0.516533 | 2 |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/586` | 0.516533 | 2 |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/392` | 0.516533 | 2 |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/3/SectionHeader/44` | 0.487018 | GENERAL FEATS 3RD |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/390` | 0.435144 | 1 |

### Query 66
- Text: What is the rule about General feat, skill increase, stellar resilience?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/395']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/395', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/403', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/427']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/395', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/394', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/396']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/394` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/396` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/395` | 0.913478 | General feat, skill increase, stellar resilience |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/403` | 0.738081 | General feat, skill increase, stellar senses, weapon specialization |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/427` | 0.722285 | General feat, skill increase, stellar paragon |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/411` | 0.636866 | Armor expertise, general feat, skill increase |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/407` | 0.595609 | Ancestry feat, skill increase, solarian expertise, stellar partition |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/46` | 0.588636 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/Table/2` | 0.565211 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, stellar attunement, solar manifestations, solarian feat2Skill feat, solarian feat3General feat, skill increas |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/419` | 0.563643 | Attribute boosts, general feat, gravitas, greater weapon specialization, skill increase |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409` | 0.563061 | Attribute boosts, skill feat, solarian feat |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429` | 0.563061 | Attribute boosts, skill feat, solarian feat |

### Query 67
- Text: Summarize 4
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/396']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/566', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/578', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/612']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/396', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/395', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/395` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/566` | 0.774878 | 4 |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/578` | 0.774878 | 4 |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/612` | 0.774878 | 4 |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/608` | 0.732878 | 4 |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/396` | 0.732877 | 4 |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/636` | 0.732877 | 4 |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/26` | 0.487593 | 4TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/394` | 0.459139 | 3 |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/30` | 0.459139 | 3 |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/584` | 0.438507 | 2 |

### Query 68
- Text: What is the rule about Skill feat, solarian feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/425']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/396', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/398']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/396` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/398` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393` | 0.931260 | Skill feat, solarian feat |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397` | 0.931260 | Skill feat, solarian feat |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/425` | 0.931260 | Skill feat, solarian feat |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/421` | 0.889260 | Skill feat, solarian feat |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/401` | 0.889260 | Skill feat, solarian feat |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/413` | 0.889260 | Skill feat, solarian feat |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/405` | 0.889260 | Skill feat, solarian feat |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/417` | 0.889260 | Skill feat, solarian feat |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409` | 0.775088 | Attribute boosts, skill feat, solarian feat |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429` | 0.775088 | Attribute boosts, skill feat, solarian feat |

### Query 69
- Text: Summarize 5
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/398']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/398', 'PZO22001 Starfinder Player Core 138-149::/page/3/SectionHeader/54', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/400']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/398', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/399', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/399` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/398` | 0.772788 | 5 |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/3/SectionHeader/54` | 0.521739 | ANCESTRY FEATS 5TH |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/400` | 0.509672 | 6 |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/606` | 0.467672 | 6 |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/620` | 0.467672 | 6 |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/572` | 0.467672 | 6 |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/630` | 0.467672 | 6 |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/574` | 0.467672 | 6 |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/566` | 0.446968 | 4 |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/636` | 0.446968 | 4 |

### Query 70
- Text: What is the rule about Ancestry feat, attribute boosts, skill increase,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/399']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/399', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/415', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/407']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/399', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/400', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/398']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/400` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/398` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/399` | 0.782748 | Ancestry feat, attribute boosts, skill increase, solar weapon expertise |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/415` | 0.705987 | Ancestry feat, skill increase, solarian weapon mastery |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/407` | 0.698787 | Ancestry feat, skill increase, solarian expertise, stellar partition |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/423` | 0.653739 | Ancestry feat, armor mastery, skill increase, solarian mastery |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/391` | 0.632103 | Ancestry and background, attribute boosts, initial proficiencies, stellar attunement, solar manifestations, solarian feat |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429` | 0.632013 | Attribute boosts, skill feat, solarian feat |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409` | 0.632013 | Attribute boosts, skill feat, solarian feat |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/56` | 0.613974 | In addition to the initial ancestry feat you started with,  you gain an ancestry feat at 5th level and every 4 levels |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/1` | 0.611586 | thereafter. The list of ancestry feats available to you can be  found in your ancestry's entry in Chapter 2. |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/419` | 0.566771 | Attribute boosts, general feat, gravitas, greater weapon specialization, skill increase |

### Query 71
- Text: Summarize 6
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/400']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/400', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/606', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/620']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/400', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/401', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/399']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/401` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/399` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/400` | 0.783525 | 6 |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/606` | 0.783525 | 6 |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/620` | 0.783525 | 6 |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/574` | 0.741525 | 6 |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/572` | 0.741525 | 6 |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/630` | 0.741525 | 6 |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/27` | 0.508078 | 6TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/402` | 0.496931 | 7 |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/558` | 0.468373 | 16 |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/592` | 0.468373 | 16 |

### Query 72
- Text: What is the rule about Skill feat, solarian feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/401']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/425']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/401', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/402', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/400']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/402` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/400` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393` | 0.931260 | Skill feat, solarian feat |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397` | 0.931260 | Skill feat, solarian feat |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/425` | 0.931260 | Skill feat, solarian feat |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/421` | 0.889260 | Skill feat, solarian feat |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/401` | 0.889260 | Skill feat, solarian feat |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/413` | 0.889260 | Skill feat, solarian feat |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/405` | 0.889260 | Skill feat, solarian feat |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/417` | 0.889260 | Skill feat, solarian feat |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409` | 0.775088 | Attribute boosts, skill feat, solarian feat |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429` | 0.775088 | Attribute boosts, skill feat, solarian feat |

### Query 73
- Text: Summarize 7
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/402']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/402', 'PZO22001 Starfinder Player Core 138-149::/page/4/SectionHeader/4', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/574']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/402', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/401', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/403']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/401` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/403` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/402` | 0.766039 | 7 |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/4/SectionHeader/4` | 0.539451 | STELLAR SENSES 7TH |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/574` | 0.515241 | 6 |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/630` | 0.473241 | 6 |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/572` | 0.473241 | 6 |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/400` | 0.473241 | 6 |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/606` | 0.473241 | 6 |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/620` | 0.473241 | 6 |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/588` | 0.456129 | 8 |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/598` | 0.456129 | 8 |

### Query 74
- Text: What is the rule about General feat, skill increase, stellar senses,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/403']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/403', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/395', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/427']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/403', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/402', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/404']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/402` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/404` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/403` | 0.827996 | General feat, skill increase, stellar senses, weapon specialization |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/395` | 0.781292 | General feat, skill increase, stellar resilience |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/427` | 0.739408 | General feat, skill increase, stellar paragon |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/411` | 0.650866 | Armor expertise, general feat, skill increase |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/407` | 0.614967 | Ancestry feat, skill increase, solarian expertise, stellar partition |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/46` | 0.602127 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/419` | 0.591284 | Attribute boosts, general feat, gravitas, greater weapon specialization, skill increase |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409` | 0.574749 | Attribute boosts, skill feat, solarian feat |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429` | 0.574749 | Attribute boosts, skill feat, solarian feat |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/Table/2` | 0.557783 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, stellar attunement, solar manifestations, solarian feat2Skill feat, solarian feat3General feat, skill increas |

### Query 75
- Text: Summarize 8
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/404']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/588', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/602', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/598']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/404', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/405', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/403']
- Expanded expected found: `True`
- Expanded expected rank: `7`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/405` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/403` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/588` | 0.787704 | 8 |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/598` | 0.787704 | 8 |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/602` | 0.787704 | 8 |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/582` | 0.745704 | 8 |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/614` | 0.745704 | 8 |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/626` | 0.745704 | 8 |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/404` | 0.745704 | 8 |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/2` | 0.546940 | 8TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/402` | 0.471909 | 7 |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/24` | 0.457647 | **PROPULSIVE SHIELD** **FEAT 8** |

### Query 76
- Text: What is the rule about Skill feat, solarian feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/405']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/425']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/405', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/404', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/406']
- Expanded expected found: `True`
- Expanded expected rank: `7`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/404` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/406` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393` | 0.931260 | Skill feat, solarian feat |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397` | 0.931260 | Skill feat, solarian feat |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/425` | 0.931260 | Skill feat, solarian feat |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/421` | 0.889260 | Skill feat, solarian feat |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/401` | 0.889260 | Skill feat, solarian feat |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/413` | 0.889260 | Skill feat, solarian feat |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/405` | 0.889260 | Skill feat, solarian feat |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/417` | 0.889260 | Skill feat, solarian feat |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409` | 0.775088 | Attribute boosts, skill feat, solarian feat |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429` | 0.775088 | Attribute boosts, skill feat, solarian feat |

### Query 77
- Text: Summarize 9
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/406']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/406', 'PZO22001 Starfinder Player Core 138-149::/page/4/SectionHeader/10', 'PZO22001 Starfinder Player Core 138-149::/page/4/SectionHeader/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/406', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/405', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/407']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/405` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/407` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/406` | 0.770045 | 9 |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/4/SectionHeader/10` | 0.607156 | STELLAR PARTITION 9TH |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/4/SectionHeader/8` | 0.579779 | SOLARIAN EXPERTISE 9TH |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/582` | 0.455491 | 8 |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/602` | 0.455491 | 8 |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/404` | 0.455491 | 8 |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/588` | 0.455491 | 8 |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/626` | 0.455491 | 8 |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/614` | 0.455491 | 8 |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/598` | 0.455491 | 8 |

### Query 78
- Text: What is the rule about Ancestry feat, skill increase, solarian?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/407']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/415', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/407', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/423']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/407', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/408', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/406']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/408` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/406` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/415` | 0.878224 | Ancestry feat, skill increase, solarian weapon mastery |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/407` | 0.847968 | Ancestry feat, skill increase, solarian expertise, stellar partition |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/423` | 0.830872 | Ancestry feat, armor mastery, skill increase, solarian mastery |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/399` | 0.753677 | Ancestry feat, attribute boosts, skill increase, solar weapon expertise |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429` | 0.719881 | Attribute boosts, skill feat, solarian feat |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409` | 0.719881 | Attribute boosts, skill feat, solarian feat |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393` | 0.696272 | Skill feat, solarian feat |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/401` | 0.696272 | Skill feat, solarian feat |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/413` | 0.696272 | Skill feat, solarian feat |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/405` | 0.696272 | Skill feat, solarian feat |

### Query 79
- Text: Summarize 10
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/408']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/570', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/638', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/628']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/408', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/407']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/407` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/570` | 0.782219 | 10 |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/638` | 0.782219 | 10 |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/628` | 0.782219 | 10 |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/568` | 0.740219 | 10 |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/408` | 0.740219 | 10 |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/36` | 0.501945 | 10TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/410` | 0.492929 | 11 |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/406` | 0.454273 | 9 |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/10` | 0.444192 | **10 + Constitution modifier** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/3/ListItem/19` | 0.405996 | Two-Hand 1d10 (counts as two traits) |

### Query 80
- Text: What is the rule about Attribute boosts, skill feat, solarian feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/408', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/410']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/408` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/410` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409` | 0.912263 | Attribute boosts, skill feat, solarian feat |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429` | 0.912263 | Attribute boosts, skill feat, solarian feat |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393` | 0.750242 | Skill feat, solarian feat |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397` | 0.708242 | Skill feat, solarian feat |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/405` | 0.708242 | Skill feat, solarian feat |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/413` | 0.708242 | Skill feat, solarian feat |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/417` | 0.708242 | Skill feat, solarian feat |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/401` | 0.708242 | Skill feat, solarian feat |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/421` | 0.708242 | Skill feat, solarian feat |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/425` | 0.708242 | Skill feat, solarian feat |

### Query 81
- Text: Summarize 11
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/410']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/410', 'PZO22001 Starfinder Player Core 138-149::/page/4/SectionHeader/12', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/580']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/410', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/411', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/411` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/410` | 0.764621 | 11 |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/4/SectionHeader/12` | 0.560241 | ARMOR EXPERTISE 11TH |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/580` | 0.535902 | 12 |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/556` | 0.493902 | 12 |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/412` | 0.493902 | 12 |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/644` | 0.493902 | 12 |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/568` | 0.479429 | 10 |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/570` | 0.479429 | 10 |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/628` | 0.479429 | 10 |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/408` | 0.479429 | 10 |

### Query 82
- Text: What is the rule about Armor expertise, general feat, skill increase?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/411']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/411', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/403', 'PZO22001 Starfinder Player Core 138-149::/page/4/Text/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/411', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/412', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/410']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/412` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/410` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/411` | 0.919718 | Armor expertise, general feat, skill increase |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/403` | 0.672973 | General feat, skill increase, stellar senses, weapon specialization |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/13` | 0.665106 | You've spent so much time in armor that you know  how to make the most of its protection. Your  proficiency ranks for light armor, medium armor,  and unarmored defense increase to expert. |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/423` | 0.606688 | Ancestry feat, armor mastery, skill increase, solarian mastery |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/395` | 0.584593 | General feat, skill increase, stellar resilience |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/419` | 0.569345 | Attribute boosts, general feat, gravitas, greater weapon specialization, skill increase |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/427` | 0.562643 | General feat, skill increase, stellar paragon |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/43` | 0.560031 | At 2nd level and every 2 levels thereafter, you gain a skill  feat. Skill feats can be found in Chapter 5 and have the skill  trait. You must be trained or better in the corresponding skill  to select |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/399` | 0.556897 | Ancestry feat, attribute boosts, skill increase, solar weapon expertise |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/46` | 0.554154 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |

### Query 83
- Text: Summarize 12
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/412']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/580', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/644', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/412']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/412', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/413', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/411']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/413` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/411` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/580` | 0.783359 | 12 |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/644` | 0.783359 | 12 |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/412` | 0.783359 | 12 |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/556` | 0.741359 | 12 |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/414` | 0.524768 | 13 |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/1` | 0.516176 | 12TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/410` | 0.515039 | 11 |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/11` | 0.434755 | **WORMHOLE **[two-actions] **FEAT 12** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/558` | 0.423140 | 16 |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/592` | 0.423140 | 16 |

### Query 84
- Text: What is the rule about Skill feat, solarian feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/413']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/425']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/413', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/414', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/412']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/414` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/412` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393` | 0.931260 | Skill feat, solarian feat |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397` | 0.931260 | Skill feat, solarian feat |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/425` | 0.931260 | Skill feat, solarian feat |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/421` | 0.889260 | Skill feat, solarian feat |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/401` | 0.889260 | Skill feat, solarian feat |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/413` | 0.889260 | Skill feat, solarian feat |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/405` | 0.889260 | Skill feat, solarian feat |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/417` | 0.889260 | Skill feat, solarian feat |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409` | 0.775088 | Attribute boosts, skill feat, solarian feat |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429` | 0.775088 | Attribute boosts, skill feat, solarian feat |

### Query 85
- Text: Summarize 13
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/414']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/414', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/412', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/580']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/414', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/413', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/415']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/413` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/415` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/414` | 0.781589 | 13 |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/412` | 0.578297 | 12 |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/580` | 0.578297 | 12 |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/556` | 0.536297 | 12 |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/644` | 0.536297 | 12 |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/562` | 0.531543 | 14 |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/634` | 0.531543 | 14 |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/642` | 0.531543 | 14 |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/618` | 0.531543 | 14 |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/416` | 0.531543 | 14 |

### Query 86
- Text: What is the rule about Ancestry feat, skill increase, solarian weapon?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/415']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/415', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/399', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/423']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/415', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/414', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/416']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/414` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/416` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/415` | 0.911820 | Ancestry feat, skill increase, solarian weapon mastery |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/399` | 0.834752 | Ancestry feat, attribute boosts, skill increase, solar weapon expertise |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/423` | 0.828376 | Ancestry feat, armor mastery, skill increase, solarian mastery |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/407` | 0.774110 | Ancestry feat, skill increase, solarian expertise, stellar partition |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429` | 0.686190 | Attribute boosts, skill feat, solarian feat |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409` | 0.686190 | Attribute boosts, skill feat, solarian feat |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/Table/2` | 0.663772 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, stellar attunement, solar manifestations, solarian feat2Skill feat, solarian feat3General feat, skill increas |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/401` | 0.654953 | Skill feat, solarian feat |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/413` | 0.654953 | Skill feat, solarian feat |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397` | 0.654953 | Skill feat, solarian feat |

### Query 87
- Text: What is the rule about Skill feat, solarian feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/417']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/425']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/417', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/418', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/416']
- Expanded expected found: `True`
- Expanded expected rank: `8`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/418` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/416` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393` | 0.931260 | Skill feat, solarian feat |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397` | 0.931260 | Skill feat, solarian feat |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/425` | 0.931260 | Skill feat, solarian feat |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/421` | 0.889260 | Skill feat, solarian feat |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/401` | 0.889260 | Skill feat, solarian feat |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/413` | 0.889260 | Skill feat, solarian feat |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/405` | 0.889260 | Skill feat, solarian feat |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/417` | 0.889260 | Skill feat, solarian feat |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409` | 0.775088 | Attribute boosts, skill feat, solarian feat |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429` | 0.775088 | Attribute boosts, skill feat, solarian feat |

### Query 88
- Text: What is the rule about Attribute boosts, general feat, gravitas,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/419']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/419', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/419', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/418', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/420']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/418` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/420` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/419` | 0.770580 | Attribute boosts, general feat, gravitas, greater weapon specialization, skill increase |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409` | 0.679375 | Attribute boosts, skill feat, solarian feat |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429` | 0.679375 | Attribute boosts, skill feat, solarian feat |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/391` | 0.564784 | Ancestry and background, attribute boosts, initial proficiencies, stellar attunement, solar manifestations, solarian feat |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/46` | 0.546181 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/399` | 0.529875 | Ancestry feat, attribute boosts, skill increase, solar weapon expertise |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/7` | 0.529646 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier is  already +4 or higher, it takes two boosts to increase it; you get a |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/403` | 0.528733 | General feat, skill increase, stellar senses, weapon specialization |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/Table/2` | 0.518082 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, stellar attunement, solar manifestations, solarian feat2Skill feat, solarian feat3General feat, skill increas |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/395` | 0.504631 | General feat, skill increase, stellar resilience |

### Query 89
- Text: What is the rule about Skill feat, solarian feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/421']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/425']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/421', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/422', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/420']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/422` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/420` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393` | 0.931260 | Skill feat, solarian feat |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397` | 0.931260 | Skill feat, solarian feat |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/425` | 0.931260 | Skill feat, solarian feat |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/421` | 0.889260 | Skill feat, solarian feat |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/401` | 0.889260 | Skill feat, solarian feat |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/413` | 0.889260 | Skill feat, solarian feat |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/405` | 0.889260 | Skill feat, solarian feat |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/417` | 0.889260 | Skill feat, solarian feat |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409` | 0.775088 | Attribute boosts, skill feat, solarian feat |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429` | 0.775088 | Attribute boosts, skill feat, solarian feat |

### Query 90
- Text: What is the rule about Ancestry feat, armor mastery, skill increase,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/423']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/423', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/415', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/411']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/423', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/422', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/424']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/422` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/424` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/423` | 0.844117 | Ancestry feat, armor mastery, skill increase, solarian mastery |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/415` | 0.753051 | Ancestry feat, skill increase, solarian weapon mastery |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/411` | 0.701114 | Armor expertise, general feat, skill increase |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/399` | 0.658406 | Ancestry feat, attribute boosts, skill increase, solar weapon expertise |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/407` | 0.641308 | Ancestry feat, skill increase, solarian expertise, stellar partition |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/56` | 0.592624 | In addition to the initial ancestry feat you started with,  you gain an ancestry feat at 5th level and every 4 levels |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/1` | 0.579671 | thereafter. The list of ancestry feats available to you can be  found in your ancestry's entry in Chapter 2. |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/Table/2` | 0.555786 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, stellar attunement, solar manifestations, solarian feat2Skill feat, solarian feat3General feat, skill increas |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/403` | 0.540227 | General feat, skill increase, stellar senses, weapon specialization |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/391` | 0.522590 | Ancestry and background, attribute boosts, initial proficiencies, stellar attunement, solar manifestations, solarian feat |

### Query 91
- Text: What is the rule about Skill feat, solarian feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/425']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/425']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/425', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/426', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/424']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/426` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/424` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393` | 0.931260 | Skill feat, solarian feat |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397` | 0.931260 | Skill feat, solarian feat |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/425` | 0.931260 | Skill feat, solarian feat |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/421` | 0.889260 | Skill feat, solarian feat |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/401` | 0.889260 | Skill feat, solarian feat |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/413` | 0.889260 | Skill feat, solarian feat |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/405` | 0.889260 | Skill feat, solarian feat |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/417` | 0.889260 | Skill feat, solarian feat |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409` | 0.775088 | Attribute boosts, skill feat, solarian feat |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429` | 0.775088 | Attribute boosts, skill feat, solarian feat |

### Query 92
- Text: What is the rule about General feat, skill increase, stellar paragon?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/427']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/427', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/395', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/403']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/427', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/426', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/428']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/426` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/428` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/427` | 0.909702 | General feat, skill increase, stellar paragon |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/395` | 0.744397 | General feat, skill increase, stellar resilience |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/403` | 0.730136 | General feat, skill increase, stellar senses, weapon specialization |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/411` | 0.625650 | Armor expertise, general feat, skill increase |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/407` | 0.609175 | Ancestry feat, skill increase, solarian expertise, stellar partition |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/2/Table/2` | 0.590958 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, stellar attunement, solar manifestations, solarian feat2Skill feat, solarian feat3General feat, skill increas |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409` | 0.588022 | Attribute boosts, skill feat, solarian feat |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429` | 0.588022 | Attribute boosts, skill feat, solarian feat |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/46` | 0.583511 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/419` | 0.579429 | Attribute boosts, general feat, gravitas, greater weapon specialization, skill increase |

### Query 93
- Text: What is the rule about Attribute boosts, skill feat, solarian feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429', 'PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/3', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/428']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/428` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409` | 0.912263 | Attribute boosts, skill feat, solarian feat |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429` | 0.912263 | Attribute boosts, skill feat, solarian feat |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/393` | 0.750242 | Skill feat, solarian feat |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/397` | 0.708242 | Skill feat, solarian feat |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/405` | 0.708242 | Skill feat, solarian feat |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/413` | 0.708242 | Skill feat, solarian feat |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/417` | 0.708242 | Skill feat, solarian feat |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/401` | 0.708242 | Skill feat, solarian feat |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/421` | 0.708242 | Skill feat, solarian feat |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/425` | 0.708242 | Skill feat, solarian feat |

### Query 94
- Text: What is the rule about ANCESTRY AND BACKGROUND?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/3', 'PZO22001 Starfinder Player Core 138-149::/page/3/Text/59', 'PZO22001 Starfinder Player Core 138-149::/page/11/Text/32']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/3', 'PZO22001 Starfinder Player Core 138-149::/page/2/Text/4', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/3` | 0.928306 | ANCESTRY AND BACKGROUND |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/59` | 0.739658 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/32` | 0.739658 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/59` | 0.709658 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/32` | 0.709658 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/33` | 0.492053 | **INTRODUCTION** **ANCESTRIES & ** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/45` | 0.492053 | **INTRODUCTION** **ANCESTRIES & ** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/62` | 0.449777 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/50` | 0.449777 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/3/SectionHeader/54` | 0.404594 | ANCESTRY FEATS 5TH |

### Query 95
- Text: What is the rule about In addition to what you get from your class at 1st level, you  have the benefits of your selected ancestry and background, as  described in Chapter 2.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/Text/4', 'PZO22001 Starfinder Player Core 138-149::/page/4/Text/1', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/Text/4', 'PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/5', 'PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/4` | 0.963223 | In addition to what you get from your class at 1st level, you  have the benefits of your selected ancestry and background, as  described in Chapter 2. |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/4/Text/1` | 0.648554 | thereafter. The list of ancestry feats available to you can be  found in your ancestry's entry in Chapter 2. |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/8` | 0.603962 | At 1st level, your class gives you  an attribute boost to Strength. |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/9` | 0.556690 | At 1st level, you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start of  this class. |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/56` | 0.555359 | In addition to the initial ancestry feat you started with,  you gain an ancestry feat at 5th level and every 4 levels |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/6` | 0.530786 | In addition to what you get from your class at 1st level, you have  four free boosts to different attribute modifiers. |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/50` | 0.494730 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/Table/2` | 0.492264 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, stellar attunement, solar manifestations, solarian feat2Skill feat, solarian feat3General feat, skill increas |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/391` | 0.477638 | Ancestry and background, attribute boosts, initial proficiencies, stellar attunement, solar manifestations, solarian feat |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/43` | 0.476847 | At 2nd level and every 2 levels thereafter, you gain a skill  feat. Skill feats can be found in Chapter 5 and have the skill  trait. You must be trained or better in the corresponding skill  to select |

### Query 96
- Text: What is the rule about In addition to what you get from your class at 1st level, you have  four free boosts to different attribute modifiers.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/Text/6', 'PZO22001 Starfinder Player Core 138-149::/page/2/Text/7', 'PZO22001 Starfinder Player Core 138-149::/page/1/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/Text/6', 'PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/5', 'PZO22001 Starfinder Player Core 138-149::/page/2/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/6` | 0.943824 | In addition to what you get from your class at 1st level, you have  four free boosts to different attribute modifiers. |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/7` | 0.843002 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier is  already +4 or higher, it takes two boosts to increase it; you get a |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/8` | 0.694753 | At 1st level, your class gives you  an attribute boost to Strength. |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/4` | 0.530456 | In addition to what you get from your class at 1st level, you  have the benefits of your selected ancestry and background, as  described in Chapter 2. |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/29` | 0.521368 | You gain these abilities as a solarian. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/11` | 0.505161 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/2/Table/2` | 0.497204 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, stellar attunement, solar manifestations, solarian feat2Skill feat, solarian feat3General feat, skill increas |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/37` | 0.496361 | Similar to spells, some solarian abilities get more  powerful as you increase in level. These abilities ends  with one or more "Level" entries. This either lists the  levels at which the ability gets |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/409` | 0.483040 | Attribute boosts, skill feat, solarian feat |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/429` | 0.483040 | Attribute boosts, skill feat, solarian feat |

### Query 97
- Text: What is the rule about At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier is  already +4 or higher, it takes two boosts to increase it; you get a  partial boost and must boost that attribute again at a later level  to increase it by 1.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/Text/7', 'PZO22001 Starfinder Player Core 138-149::/page/2/Text/6', 'PZO22001 Starfinder Player Core 138-149::/page/3/Text/37']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/Text/7', 'PZO22001 Starfinder Player Core 138-149::/page/2/Text/6', 'PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/7` | 0.966227 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier is  already +4 or higher, it takes two boosts to increase it; you get a |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/6` | 0.768876 | In addition to what you get from your class at 1st level, you have  four free boosts to different attribute modifiers. |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/37` | 0.601933 | Similar to spells, some solarian abilities get more  powerful as you increase in level. These abilities ends  with one or more "Level" entries. This either lists the  levels at which the ability gets |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/11` | 0.559486 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/49` | 0.540230 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use this increase either to increase your  proficiency rank to trained in one skill you're untrained in, or  to increase |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/56` | 0.532248 | In addition to the initial ancestry feat you started with,  you gain an ancestry feat at 5th level and every 4 levels |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/8` | 0.521283 | At 1st level, your class gives you  an attribute boost to Strength. |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/50` | 0.514247 | At 7th level, you can use skill increases to increase your  proficiency rank to master in a skill in which you're already  an expert, and at 15th level, you can use them to increase  your proficiency |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/46` | 0.502212 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/29` | 0.500016 | You gain these abilities as a solarian. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |

### Query 98
- Text: What is the rule about emit heat, light, and plasma) and graviton (the power of stars to  attract and imprison objects through gravity). At any time, you're  considered graviton-attuned, photon-attuned, or unattuned.  Many of your abilities have additional effects based on your  current attunement, and some abilities swap your current state  of attunement to another state.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/Text/12', 'PZO22001 Starfinder Player Core 138-149::/page/11/Text/29', 'PZO22001 Starfinder Player Core 138-149::/page/6/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/Text/12', 'PZO22001 Starfinder Player Core 138-149::/page/2/Text/11', 'PZO22001 Starfinder Player Core 138-149::/page/2/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/12` | 0.982402 | emit heat, light, and plasma) and graviton (the power of stars to  attract and imprison objects through gravity). At any time, you're  considered graviton-attuned, photon-attuned, or unattuned.  Many |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/29` | 0.819628 | You have absolute control and understanding of your  attunement with the stellar forces of the cosmos. If you  would become graviton- or photon-attuned, you instead  become perfectly-attuned. When you |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/3` | 0.767429 | **Attuned:** You can't use abilities with the attuned  trait while you're unattuned. Many attuned abilities  require you to be specifically graviton-attuned or  photon-attuned, while others can grant |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/17` | 0.695842 | You steady your body and mind and attune yourself to the  stellar aspect of your choice. You become attuned to photon or  graviton. You can also manifest any of your solar manifestations  if they're c |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/4` | 0.684842 | **Cycle:** Actions with the cycle trait change your  current stellar attunement to its opposite state. When  you take such an action with this trait, you benefit  from the additional effect of your cu |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/8/Text/8` | 0.615247 | You unleash a corona of stellar energy in a 10-foot emanation,  which lasts until the end of your next turn. You can Sustain  your Corona for up to 1 minute. If your attunement changes,  your Corona's |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/33` | 0.615077 | **Requirements** You're graviton-attuned. |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/31` | 0.615077 | **Requirements** You're graviton-attuned. |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/2` | 0.594843 | You're a conduit for the stellar forces of the cosmos—a solar knight. The powers of gravity and light  represent the extremes of these forces, and you can attune yourself between them. As an agent of |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/6` | 0.584533 | You break the bonds of gravity. While graviton-attuned, you  gain a fly Speed equal to your Speed. |

### Query 99
- Text: What is the rule about You gain the Attune action.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/Text/13', 'PZO22001 Starfinder Player Core 138-149::/page/2/Text/18', 'PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/Text/13', 'PZO22001 Starfinder Player Core 138-149::/page/2/Text/12', 'PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/13` | 0.912421 | You gain the Attune action. |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/18` | 0.690428 | **Special** In addition to the above usage, you can also Attune as a  free action when you roll initiative. |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/14` | 0.655722 | **ATTUNE **[one-action] |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/5` | 0.608215 | You can use your manifestations immediately upon  attuning yourself. When you Attune as a single action, you  can make a Strike with your solar flare or solar weapon as  a free action. |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/4` | 0.562469 | **Cycle:** Actions with the cycle trait change your  current stellar attunement to its opposite state. When  you take such an action with this trait, you benefit  from the additional effect of your cu |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/29` | 0.557239 | You have absolute control and understanding of your  attunement with the stellar forces of the cosmos. If you  would become graviton- or photon-attuned, you instead  become perfectly-attuned. When you |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/5` | 0.548674 | **Disharmony:** Actions with the disharmony trait  change your current stellar attunement to being  unattuned. When you take such an action with this  trait, you benefit from the additional effect of |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/3` | 0.545310 | **Attuned:** You can't use abilities with the attuned  trait while you're unattuned. Many attuned abilities  require you to be specifically graviton-attuned or  photon-attuned, while others can grant |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/12` | 0.523458 | emit heat, light, and plasma) and graviton (the power of stars to  attract and imprison objects through gravity). At any time, you're  considered graviton-attuned, photon-attuned, or unattuned.  Many |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/25` | 0.517040 | You reach true alignment with the cosmic cycle. You're  permanently quickened. You can use your extra action  only to Attune or make a Strike with your solar flare or  solar weapon. |

### Query 100
- Text: What is the rule about **ATTUNE **[one-action]?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/14', 'PZO22001 Starfinder Player Core 138-149::/page/2/Text/13', 'PZO22001 Starfinder Player Core 138-149::/page/2/Text/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/14', 'PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/15', 'PZO22001 Starfinder Player Core 138-149::/page/2/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/2/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/14` | 0.928141 | **ATTUNE **[one-action] |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/13` | 0.736545 | You gain the Attune action. |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/18` | 0.656324 | **Special** In addition to the above usage, you can also Attune as a  free action when you roll initiative. |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/4` | 0.554086 | **Cycle:** Actions with the cycle trait change your  current stellar attunement to its opposite state. When  you take such an action with this trait, you benefit  from the additional effect of your cu |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/5` | 0.541277 | You can use your manifestations immediately upon  attuning yourself. When you Attune as a single action, you  can make a Strike with your solar flare or solar weapon as  a free action. |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/3` | 0.538029 | **Attuned:** You can't use abilities with the attuned  trait while you're unattuned. Many attuned abilities  require you to be specifically graviton-attuned or  photon-attuned, while others can grant |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/5` | 0.516877 | **Disharmony:** Actions with the disharmony trait  change your current stellar attunement to being  unattuned. When you take such an action with this  trait, you benefit from the additional effect of |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/14` | 0.502957 | With practice, you can make on-the-fly battlefield adjustments  to your weapon, letting you choose the perfect attack for a  situation. When you Attune, you can change the damage type  of your solar w |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/12` | 0.499073 | emit heat, light, and plasma) and graviton (the power of stars to  attract and imprison objects through gravity). At any time, you're  considered graviton-attuned, photon-attuned, or unattuned.  Many |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/29` | 0.497140 | You have absolute control and understanding of your  attunement with the stellar forces of the cosmos. If you  would become graviton- or photon-attuned, you instead  become perfectly-attuned. When you |

### Query 101
- Text: What are the requirements for **BINARIC ASSAULT **[two-actions] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/4', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/563', 'PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/4', 'PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/3', 'PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/4` | 0.920011 | **BINARIC ASSAULT **[two-actions] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/563` | 0.658522 | Binaric Assault |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/15` | 0.540103 | **SHATTERING IMPACT **[two-actions] **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/7` | 0.492238 | You coordinate your attacks with both your solar flare and solar  weapon. Make two Strikes at the same target, one with your  solar weapon and one with your solar flare, each using your  current multi |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/5` | 0.470780 | **CORONA **[two-actions] **FEAT 6** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/31` | 0.456092 | **TWIN WEAPONS** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/27` | 0.454610 | **BLACK HOLE **[two-actions] **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/12` | 0.450039 | **MEDITATIVE ANALYSIS **[one-action] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/25` | 0.444790 | **STELLAR RUSH **[two-actions] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/54` | 0.442160 | **Prerequisites** Twin Weapons |

### Query 102
- Text: What are the requirements for **HAMPERING FLARE **[one-action] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/8', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/42', 'PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/8', 'PZO22001 Starfinder Player Core 138-149::/page/5/Text/7', 'PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/5/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/8` | 0.900340 | **HAMPERING FLARE **[one-action] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/42` | 0.644595 | **CLINGING FLARE **[one-action] **FEAT 10** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/7` | 0.632090 | **COVERING FLARE **[two-actions] **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/589` | 0.524941 | Hampering Flare |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/45` | 0.518825 | **UNSTABLE FLARE **[two-actions] **FEAT 14** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/36` | 0.501580 | **DISTANT FLARE** **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/12` | 0.466266 | **MEDITATIVE ANALYSIS **[one-action] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/37` | 0.447810 | **CAREFUL STRIKE **[one-action] **FEAT 10** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/46` | 0.430792 | **SOUL FURNACE **[one-action] **FEAT 10** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/8/Text/23` | 0.427369 | **Requirements** Your last action was a successful solar flare or  solar weapon Strike against a creature. |

### Query 103
- Text: What are the requirements for **MEDITATIVE ANALYSIS **[one-action] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/12', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/595', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/12', 'PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/14', 'PZO22001 Starfinder Player Core 138-149::/page/5/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/5/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/12` | 0.917045 | **MEDITATIVE ANALYSIS **[one-action] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/595` | 0.684825 | Meditative Analysis |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/17` | 0.502657 | **MOMENTUM **[one-action] **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/29` | 0.445927 | **SINGULARITY **[three-actions] **FEAT 14** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/15` | 0.437592 | You briefly meditate on the nature of your foe and their role  in the wider cosmos. Attempt a check to Recall Knowledge  about a creature. On a success, your next Strike with a solar  weapon against t |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/46` | 0.431453 | **SOUL FURNACE **[one-action] **FEAT 10** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/8` | 0.425112 | **HAMPERING FLARE **[one-action] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/4` | 0.418958 | **BINARIC ASSAULT **[two-actions] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/40` | 0.412104 | **ECLIPSE STRIKE **[one-action] **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/27` | 0.405993 | **BLACK HOLE **[two-actions] **FEAT 4** |

### Query 104
- Text: What are the requirements for **SOLAR SHIELD** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/16', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/27', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/16', 'PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/17', 'PZO22001 Starfinder Player Core 138-149::/page/5/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/5/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/16` | 0.902114 | **SOLAR SHIELD** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/27` | 0.776259 | **Prerequisites** Solar Shield |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/15` | 0.776259 | **Prerequisites** Solar Shield |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/39` | 0.637104 | **Prerequisites** Solar Shield plus either Black Hole or  Supernova |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/623` | 0.595877 | Solar Shield |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/8/Text/14` | 0.552699 | **Prerequisites** Nimbus Ward and Solar Shield |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/24` | 0.532562 | **PROPULSIVE SHIELD** **FEAT 8** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/48` | 0.518020 | **Prerequisites** Solar Barrage |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/32` | 0.502236 | **SOLAR WIND** **FEAT 8** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/2` | 0.501333 | At each level that you gain a solarian feat, you can select one of  the following feats. You must satisfy any prerequisites before  taking the feat. |

### Query 105
- Text: What are the requirements for **STELLAR RUSH **[two-actions] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/25', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/631', 'PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/395']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/25', 'PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/27', 'PZO22001 Starfinder Player Core 138-149::/page/5/Text/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/5/Text/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/25` | 0.901907 | **STELLAR RUSH **[two-actions] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/631` | 0.593283 | Stellar Rush |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/395` | 0.533268 | General feat, skill increase, stellar resilience |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/427` | 0.476623 | General feat, skill increase, stellar paragon |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/16` | 0.476244 | **SOLAR BARRAGE **[two-actions] **FEAT 6** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/40` | 0.474054 | **ECLIPSE STRIKE **[one-action] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/28` | 0.469157 | You rush forward with a blast of stellar energy, getting into  the thick of combat with ease. Stride twice. You gain a +10-foot  circumstance bonus to your Speed during these moves. |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/2` | 0.467198 | At each level that you gain a solarian feat, you can select one of  the following feats. You must satisfy any prerequisites before  taking the feat. |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/Table/2` | 0.466190 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, stellar attunement, solar manifestations, solarian feat2Skill feat, solarian feat3General feat, skill increas |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/7` | 0.460915 | **PLASMA EJECTION **[two-actions] **FEAT 4** |

### Query 106
- Text: What are the requirements for **TWIN WEAPONS** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/31', 'PZO22001 Starfinder Player Core 138-149::/page/9/Text/54', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/639']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/31', 'PZO22001 Starfinder Player Core 138-149::/page/5/Text/30', 'PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/33']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/5/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/33` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/31` | 0.866726 | **TWIN WEAPONS** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/54` | 0.795294 | **Prerequisites** Twin Weapons |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/639` | 0.670437 | Twin Weapons |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/51` | 0.507660 | **TWIN GUARD **[reaction] **FEAT 10** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/34` | 0.449341 | You have a second solar weapon. When you take this feat  or Re-Forge Solar Weapon, choose its traits separately from  your first weapon. You can select a different damage type,  traits, and weapon gro |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/16` | 0.434026 | **SOLAR SHIELD** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/68` | 0.420431 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/67` | 0.420431 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/54` | 0.420431 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/42` | 0.420431 | **SKILLS** **FEATS** |

### Query 107
- Text: What are the requirements for **DISTANT FLARE** **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/36']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/36', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/583', 'PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/45']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/36', 'PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/35', 'PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/38']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/35` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/38` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/36` | 0.876072 | **DISTANT FLARE** **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/583` | 0.632997 | Distant Flare |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/45` | 0.543050 | **UNSTABLE FLARE **[two-actions] **FEAT 14** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/7` | 0.496302 | **COVERING FLARE **[two-actions] **FEAT 12** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/8` | 0.471261 | **HAMPERING FLARE **[one-action] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/42` | 0.439954 | **CLINGING FLARE **[one-action] **FEAT 10** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/3/SectionHeader/41` | 0.434137 | SKILL FEATS 2ND |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/21` | 0.431045 | Solar Flare |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/589` | 0.419501 | Hampering Flare |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/8/Text/23` | 0.413339 | **Requirements** Your last action was a successful solar flare or  solar weapon Strike against a creature. |

### Query 108
- Text: What are the requirements for **ECLIPSE STRIKE **[one-action] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/40']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/40', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/37', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/40', 'PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/42', 'PZO22001 Starfinder Player Core 138-149::/page/5/Text/39']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/5/Text/39` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/40` | 0.912621 | **ECLIPSE STRIKE **[one-action] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/37` | 0.630320 | **CAREFUL STRIKE **[one-action] **FEAT 10** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/7` | 0.625829 | **FLICKER STRIKE **[two-actions] **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/585` | 0.558237 | Eclipse Strike |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/20` | 0.477003 | **Requirements** Your last action was a successful solar weapon  Strike. |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/6` | 0.461982 | **Photon-Attuned** If the Strike is a critical success, the target  must succeed at a Fortitude save against your class DC or  become clumsy 1 until the start of its turn. |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/15` | 0.461149 | **SHATTERING IMPACT **[two-actions] **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/25` | 0.438938 | **STELLAR RUSH **[two-actions] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/8/Text/23` | 0.434748 | **Requirements** Your last action was a successful solar flare or  solar weapon Strike against a creature. |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/1/Text/42` | 0.433408 | **SKILLS** **FEATS** |

### Query 109
- Text: What are the requirements for **MUTABLE MANIFESTATION** **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/11', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/603', 'PZO22001 Starfinder Player Core 138-149::/page/3/SectionHeader/41']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/11', 'PZO22001 Starfinder Player Core 138-149::/page/6/Text/10', 'PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/6/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/11` | 0.922304 | **MUTABLE MANIFESTATION** **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/603` | 0.573846 | Mutable Manifestation |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/3/SectionHeader/41` | 0.457021 | SKILL FEATS 2ND |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/13` | 0.414346 | **SOLARIAN** **MANIFESTATION** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/7` | 0.412462 | **Manifestation:** Feats with this trait enhance or  alter your solar manifestations (flare, nimbus, and  weapon) or allow you to create a new type of solar  manifestation. |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/38` | 0.402346 | **SOLARIAN** **MANIFESTATION** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/15` | 0.395983 | **SHATTERING IMPACT **[two-actions] **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/17` | 0.373934 | **MANIFESTATION** **SOLARIAN** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/33` | 0.373934 | **MANIFESTATION** **SOLARIAN** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/19` | 0.373934 | **MANIFESTATION** **SOLARIAN** |

### Query 110
- Text: What are the requirements for **SHATTERING IMPACT **[two-actions] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/15', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/615', 'PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/15', 'PZO22001 Starfinder Player Core 138-149::/page/6/Text/14', 'PZO22001 Starfinder Player Core 138-149::/page/6/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/6/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/6/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/15` | 0.928878 | **SHATTERING IMPACT **[two-actions] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/615` | 0.613255 | Shattering Impact |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/4` | 0.540584 | **BINARIC ASSAULT **[two-actions] **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/40` | 0.483122 | **ECLIPSE STRIKE **[one-action] **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/7` | 0.469859 | **FLICKER STRIKE **[two-actions] **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/5` | 0.465560 | **CORONA **[two-actions] **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/14` | 0.460862 | **SUPERNOVA **[two-actions] **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/25` | 0.454122 | **STELLAR RUSH **[two-actions] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/7` | 0.439039 | **PLASMA EJECTION **[two-actions] **FEAT 4** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/29` | 0.434637 | **SINGULARITY **[three-actions] **FEAT 14** |

### Query 111
- Text: What are the requirements for **SOLAR RAMPART** **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/22', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/621', 'PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/22', 'PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/24', 'PZO22001 Starfinder Player Core 138-149::/page/6/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/6/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/22` | 0.905217 | **SOLAR RAMPART** **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/621` | 0.698409 | Solar Rampart |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/16` | 0.575777 | **SOLAR SHIELD** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/16` | 0.522954 | **SOLAR BARRAGE **[two-actions] **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/48` | 0.511022 | **Prerequisites** Solar Barrage |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/27` | 0.510200 | **Prerequisites** Solar Shield |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/15` | 0.510200 | **Prerequisites** Solar Shield |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/32` | 0.470555 | **SOLAR WIND** **FEAT 8** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/39` | 0.463100 | **Prerequisites** Solar Shield plus either Black Hole or  Supernova |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/2` | 0.452873 | At each level that you gain a solarian feat, you can select one of  the following feats. You must satisfy any prerequisites before  taking the feat. |

### Query 112
- Text: What are the requirements for **BLACK HOLE **[two-actions] **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/27', 'PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/11', 'PZO22001 Starfinder Player Core 138-149::/page/10/Text/43']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/27', 'PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/26', 'PZO22001 Starfinder Player Core 138-149::/page/6/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/6/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/27` | 0.893813 | **BLACK HOLE **[two-actions] **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/11` | 0.589683 | **WORMHOLE **[two-actions] **FEAT 12** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/43` | 0.556166 | **Graviton-Attuned** Immediately use Black Hole as a free  action (if you have the Black Hole feat). |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/14` | 0.484036 | **SUPERNOVA **[two-actions] **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/7` | 0.478730 | **PLASMA EJECTION **[two-actions] **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/41` | 0.456980 | **Requirements** You haven't used Black Hole or Supernova  within the last 10 minutes. |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/29` | 0.452463 | **SINGULARITY **[three-actions] **FEAT 14** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/565` | 0.449007 | Black Hole |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/19` | 0.441060 | **BIG BANG **[three-actions] **FEAT 14** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/4` | 0.432086 | **BINARIC ASSAULT **[two-actions] **FEAT 1** |

### Query 113
- Text: What are the requirements for **COSMIC INFUSION** **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/38']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/38', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/577', 'PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/22']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/38', 'PZO22001 Starfinder Player Core 138-149::/page/6/Text/37', 'PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/40']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/6/Text/37` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/40` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/38` | 0.925210 | **COSMIC INFUSION** **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/577` | 0.696432 | Cosmic Infusion |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/22` | 0.474633 | **COSMIC ALIGNMENT** **FEAT 20** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/Table/3` | 0.414186 | FeatLevelAscended Stability12Attuned Blow16Attuned Wards18Big Bang14Binaric Assault1Black Hole4Careful Strike10Clinging Flare10Constellation Vortex6Corona6Cosmic Alignment20Cosmic Infusion4Covering Fl |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/7` | 0.405352 | **PLASMA EJECTION **[two-actions] **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/578` | 0.395441 | 4 |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/2` | 0.389480 | At each level that you gain a solarian feat, you can select one of  the following feats. You must satisfy any prerequisites before  taking the feat. |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/41` | 0.388670 | **Requirements** You haven't used Black Hole or Supernova  within the last 10 minutes. |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/39` | 0.383988 | **Prerequisites** Solar Shield plus either Black Hole or  Supernova |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/608` | 0.383441 | 4 |

### Query 114
- Text: What are the requirements for **NIMBUS WARD **[reaction]** OR **[one-action] **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/43', 'PZO22001 Starfinder Player Core 138-149::/page/7/Text/5', 'PZO22001 Starfinder Player Core 138-149::/page/8/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/43', 'PZO22001 Starfinder Player Core 138-149::/page/6/Text/42', 'PZO22001 Starfinder Player Core 138-149::/page/6/Text/45']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/6/Text/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/6/Text/45` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/43` | 0.929060 | **NIMBUS WARD **[reaction]** OR **[one-action] **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/5` | 0.667615 | You can use Nimbus Ward as a reaction only when the  requirements and trigger are met, but you can use it as a  1-action activity without the requirements or trigger being met. **Graviton-Attuned** Yo |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/8/Text/14` | 0.556047 | **Prerequisites** Nimbus Ward and Solar Shield |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/2/Text/27` | 0.497606 | You gain the Nimbus Surge reaction. |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/607` | 0.491048 | Nimbus Ward |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/3/SectionHeader/1` | 0.487276 | **NIMBUS SURGE **[reaction] |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/11` | 0.469378 | **NIMBUS BLOCK** **FEAT 6** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/14` | 0.464348 | **SUPERNOVA **[two-actions] **FEAT 4** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/17` | 0.446362 | **MOMENTUM **[one-action] **FEAT 8** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/4` | 0.445651 | Your nimbus surges with energy, forcing an opening in your foe's  defenses. Make a melee Strike against the triggering creature.  This Strike doesn't count toward your multiple attack penalty,  and yo |

### Query 115
- Text: Lookup values for FeatLevelAscended Stability12Attuned Blow16Attuned Wards18Big Bang14Binaric Assault1Black Hole4Careful Strike10Clinging Flare10Constellation Vortex6Corona6Cosmic Alignment20Cosmic Infusion4Covering Flare12Defy Gravity8Distant Flare2Eclipse Strike2Flicker Strike8Hampering Flare1Harmonic Convergence16Homing Mote18Meditative Analysis1Mindward Shield8
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/7/Table/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/7/Table/3', 'PZO22001 Starfinder Player Core 138-149::/page/7/Table/20', 'PZO22001 Starfinder Player Core 138-149::/page/2/Table/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/7/Table/3', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/553', 'PZO22001 Starfinder Player Core 138-149::/page/7/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/553` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/7/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/7/Table/3` | 0.997119 | FeatLevelAscended Stability12Attuned Blow16Attuned Wards18Big Bang14Binaric Assault1Black Hole4Careful Strike10Clinging Flare10Constellation Vortex6Corona6Cosmic Alignment20Cosmic Infusion4Covering Fl |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/Table/20` | 0.732609 | FeatLevelMomentum8Mutable Manifestation2Nimbus Block6Nimbus Ward4Perfectly-Attuned20Plasma Ejection4Propulsive Shield8Shattering Impact2Singularity14Solar Barrage6Solar Rampart2Solar Shield1Solar Wind |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/Table/2` | 0.628453 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, stellar attunement, solar manifestations, solarian feat2Skill feat, solarian feat3General feat, skill increas |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/2` | 0.531664 | Use this table to look up solarian feats by name. |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/24` | 0.502403 | You manifest a fragment of the cosmic forces from the  Universe's first moments, unleashing a blast of scouring  cosmic fire that reverts all things to their basic components  and overcomes even magic |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/37` | 0.494403 | Similar to spells, some solarian abilities get more  powerful as you increase in level. These abilities ends  with one or more "Level" entries. This either lists the  levels at which the ability gets |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/32` | 0.476090 | You concentrate on the gravitational forces around you, pulling  matter toward you in emulation of a black hole. Select any  number of creatures within 30 feet. Each affected creature  takes 2d8 bludg |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/29` | 0.465707 | **Graviton-Attuned** When you finish your Strides, enemies  within 15 feet of you must attempt a Fortitude save against  your class DC. On a failure, they're pulled directly toward  you, ending in an |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/11` | 0.459902 | **Graviton-Attuned** Increase the range to double your Speed. **Photon-Attuned** If a Strike made as part of this action is a  critical success, the struck target is dazzled until the end  of its next |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/6` | 0.452819 | **Photon-Attuned** If the Strike is a critical success, the target  must succeed at a Fortitude save against your class DC or  become clumsy 1 until the start of its turn. |

### Query 116
- Text: What are the requirements for **PLASMA EJECTION **[two-actions] **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/7', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/611', 'PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/7', 'PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/9', 'PZO22001 Starfinder Player Core 138-149::/page/7/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/7/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/7` | 0.918789 | **PLASMA EJECTION **[two-actions] **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/611` | 0.657289 | Plasma Ejection |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/14` | 0.542484 | **SUPERNOVA **[two-actions] **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/27` | 0.495096 | **BLACK HOLE **[two-actions] **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/10` | 0.473308 | You unleash an ejection of plasma, hitting every creature in  your choice of a 10-foot emanation or in a 30-foot line. Each  creature in the area takes 3d6 fire damage with a basic Reflex  save agains |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/38` | 0.430342 | **COSMIC INFUSION** **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/16` | 0.428061 | **SOLAR BARRAGE **[two-actions] **FEAT 6** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/15` | 0.421641 | **SHATTERING IMPACT **[two-actions] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/25` | 0.415559 | **STELLAR RUSH **[two-actions] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/29` | 0.415503 | **SINGULARITY **[three-actions] **FEAT 14** |

### Query 117
- Text: What are the requirements for **SUPERNOVA **[two-actions] **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/14', 'PZO22001 Starfinder Player Core 138-149::/page/10/Text/44', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/635']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/14', 'PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/16', 'PZO22001 Starfinder Player Core 138-149::/page/7/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/7/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/14` | 0.914220 | **SUPERNOVA **[two-actions] **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/44` | 0.570994 | **Photon-Attuned** Immediately use Supernova as a free action  (if you have the Supernova feat). |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/635` | 0.556377 | Supernova |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/7` | 0.490751 | **PLASMA EJECTION **[two-actions] **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/27` | 0.486935 | **BLACK HOLE **[two-actions] **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/41` | 0.469976 | **Requirements** You haven't used Black Hole or Supernova  within the last 10 minutes. |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/5` | 0.457841 | **CORONA **[two-actions] **FEAT 6** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/29` | 0.442279 | **SINGULARITY **[three-actions] **FEAT 14** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/43` | 0.441405 | **NIMBUS WARD **[reaction]** OR **[one-action] **FEAT 4** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/15` | 0.437819 | **SHATTERING IMPACT **[two-actions] **FEAT 2** |

### Query 118
- Text: Lookup values for FeatLevelMomentum8Mutable Manifestation2Nimbus Block6Nimbus Ward4Perfectly-Attuned20Plasma Ejection4Propulsive Shield8Shattering Impact2Singularity14Solar Barrage6Solar Rampart2Solar Shield1Solar Wind8Soul Furnace10Star Brand6Stellar Rush1Stellar Shield Collapse14Supernova4Twin Guard10Twin Weapons1Unstable Flare14Wormhole12
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/7/Table/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/7/Table/20', 'PZO22001 Starfinder Player Core 138-149::/page/7/Table/3', 'PZO22001 Starfinder Player Core 138-149::/page/2/Table/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/7/Table/20', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/599', 'PZO22001 Starfinder Player Core 138-149::/page/7/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/599` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/7/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/7/Table/20` | 1.006200 | FeatLevelMomentum8Mutable Manifestation2Nimbus Block6Nimbus Ward4Perfectly-Attuned20Plasma Ejection4Propulsive Shield8Shattering Impact2Singularity14Solar Barrage6Solar Rampart2Solar Shield1Solar Wind |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/Table/3` | 0.763778 | FeatLevelAscended Stability12Attuned Blow16Attuned Wards18Big Bang14Binaric Assault1Black Hole4Careful Strike10Clinging Flare10Constellation Vortex6Corona6Cosmic Alignment20Cosmic Infusion4Covering Fl |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/2/Table/2` | 0.654170 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, stellar attunement, solar manifestations, solarian feat2Skill feat, solarian feat3General feat, skill increas |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/7` | 0.519179 | **Manifestation:** Feats with this trait enhance or  alter your solar manifestations (flare, nimbus, and  weapon) or allow you to create a new type of solar  manifestation. |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/2` | 0.514358 | Use this table to look up solarian feats by name. |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/37` | 0.478121 | Similar to spells, some solarian abilities get more  powerful as you increase in level. These abilities ends  with one or more "Level" entries. This either lists the  levels at which the ability gets |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/5` | 0.474984 | You can use Nimbus Ward as a reaction only when the  requirements and trigger are met, but you can use it as a  1-action activity without the requirements or trigger being met. **Graviton-Attuned** Yo |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/16` | 0.473359 | **SOLAR SHIELD** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/43` | 0.470374 | Your attacks create a brilliant eclipse that veil you from  the enemy's view. Make a Strike with your solar weapon or  your solar flare. On a hit, you create an impressive display of  solar energy bet |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/24` | 0.458867 | **Photon-Attuned** If your shield is destroyed, it releases a flash  of light. Adjacent enemies must succeed at a Fortitude save  against your class DC or be dazzled for 1 round (blinded for  1 round |

### Query 119
- Text: What are the requirements for **CONSTELLATION VORTEX **[one-action] **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/28', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/571', 'PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/28', 'PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/30', 'PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/28` | 0.935752 | **CONSTELLATION VORTEX **[one-action] **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/571` | 0.571989 | Constellation Vortex |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/20` | 0.543978 | **STAR BRAND **[one-action] **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/5` | 0.501859 | **CORONA **[two-actions] **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/31` | 0.490270 | You manifest a copy of your solar weapon, causing it to circle  around you in a vortex, leaving constellation patterns in its wake.  A creature that starts its turn adjacent to you takes damage of  an |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/16` | 0.464688 | **SOLAR BARRAGE **[two-actions] **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/17` | 0.446733 | **MOMENTUM **[one-action] **FEAT 8** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/6` | 0.441135 | **HARMONIC CONVERGENCE** **FEAT 16** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/42` | 0.436723 | **CLINGING FLARE **[one-action] **FEAT 10** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/7/Table/3` | 0.430990 | FeatLevelAscended Stability12Attuned Blow16Attuned Wards18Big Bang14Binaric Assault1Black Hole4Careful Strike10Clinging Flare10Constellation Vortex6Corona6Cosmic Alignment20Cosmic Infusion4Covering Fl |

### Query 120
- Text: What are the requirements for **CORONA **[two-actions] **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/5', 'PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/16', 'PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/5', 'PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/7', 'PZO22001 Starfinder Player Core 138-149::/page/8/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/8/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/5` | 0.891447 | **CORONA **[two-actions] **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/16` | 0.569744 | **SOLAR BARRAGE **[two-actions] **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/20` | 0.542997 | **STAR BRAND **[one-action] **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/14` | 0.496581 | **SUPERNOVA **[two-actions] **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/15` | 0.476285 | **SHATTERING IMPACT **[two-actions] **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/28` | 0.473938 | **CONSTELLATION VORTEX **[one-action] **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/4` | 0.456364 | **BINARIC ASSAULT **[two-actions] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/11` | 0.443723 | **WORMHOLE **[two-actions] **FEAT 12** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/573` | 0.436200 | Corona |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/29` | 0.427437 | **SINGULARITY **[three-actions] **FEAT 14** |

### Query 121
- Text: What are the requirements for **NIMBUS BLOCK** **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/11', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/605', 'PZO22001 Starfinder Player Core 138-149::/page/8/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/11', 'PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/13', 'PZO22001 Starfinder Player Core 138-149::/page/8/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/8/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/11` | 0.924152 | **NIMBUS BLOCK** **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/605` | 0.649175 | Nimbus Block |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/8/Text/14` | 0.506237 | **Prerequisites** Nimbus Ward and Solar Shield |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/43` | 0.461369 | **NIMBUS WARD **[reaction]** OR **[one-action] **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/25` | 0.444308 | Solar Nimbus |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/3/SectionHeader/1` | 0.428684 | **NIMBUS SURGE **[reaction] |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/606` | 0.404256 | 6 |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/16` | 0.396927 | **SOLAR BARRAGE **[two-actions] **FEAT 6** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/620` | 0.392256 | 6 |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/400` | 0.392256 | 6 |

### Query 122
- Text: What are the requirements for **Prerequisites** Nimbus Ward and Solar Shield?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/8/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/8/Text/14', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/27', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/8/Text/14', 'PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/13', 'PZO22001 Starfinder Player Core 138-149::/page/8/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/8/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/8/Text/14` | 0.988502 | **Prerequisites** Nimbus Ward and Solar Shield |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/27` | 0.747117 | **Prerequisites** Solar Shield |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/15` | 0.747117 | **Prerequisites** Solar Shield |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/8/Text/15` | 0.667210 | You've combined the strength of your defensive powers such  that your solar nimbus bolsters your solar shield. When you  Shield Block a melee attack with your solar shield, as long as  either you or y |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/2/SectionHeader/25` | 0.630398 | Solar Nimbus |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/39` | 0.605519 | **Prerequisites** Solar Shield plus either Black Hole or  Supernova |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/607` | 0.593113 | Nimbus Ward |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/47` | 0.540068 | You harness your solar nimbus to protect yourself from  harm. You gain resistance equal to half your level (rounded  up) until the start of your next turn. You choose the type |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/48` | 0.531357 | **Prerequisites** Solar Barrage |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/5` | 0.526412 | You can use Nimbus Ward as a reaction only when the  requirements and trigger are met, but you can use it as a  1-action activity without the requirements or trigger being met. **Graviton-Attuned** Yo |

### Query 123
- Text: What are the requirements for **SOLAR BARRAGE **[two-actions] **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/16', 'PZO22001 Starfinder Player Core 138-149::/page/10/Text/48', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/619']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/16', 'PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/18', 'PZO22001 Starfinder Player Core 138-149::/page/8/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/8/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/16` | 0.932710 | **SOLAR BARRAGE **[two-actions] **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/48` | 0.719370 | **Prerequisites** Solar Barrage |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/619` | 0.594007 | Solar Barrage |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/5` | 0.541509 | **CORONA **[two-actions] **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/27` | 0.537955 | **Prerequisites** Solar Shield |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/15` | 0.537955 | **Prerequisites** Solar Shield |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/22` | 0.534079 | **SOLAR RAMPART** **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/16` | 0.528172 | **SOLAR SHIELD** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/39` | 0.514314 | **Prerequisites** Solar Shield plus either Black Hole or  Supernova |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/20` | 0.507390 | **STAR BRAND **[one-action] **FEAT 6** |

### Query 124
- Text: What are the requirements for **STAR BRAND **[one-action] **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/20', 'PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/5', 'PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/20', 'PZO22001 Starfinder Player Core 138-149::/page/8/Text/19', 'PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/8/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/20` | 0.881097 | **STAR BRAND **[one-action] **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/5` | 0.545510 | **CORONA **[two-actions] **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/16` | 0.543866 | **SOLAR BARRAGE **[two-actions] **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/28` | 0.492722 | **CONSTELLATION VORTEX **[one-action] **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/17` | 0.468014 | **MOMENTUM **[one-action] **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/46` | 0.449484 | **SOUL FURNACE **[one-action] **FEAT 10** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/25` | 0.432844 | **STELLAR RUSH **[two-actions] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/43` | 0.429995 | **NIMBUS WARD **[reaction]** OR **[one-action] **FEAT 4** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/14` | 0.422872 | **SUPERNOVA **[two-actions] **FEAT 4** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/11` | 0.421069 | **NIMBUS BLOCK** **FEAT 6** |

### Query 125
- Text: What are the requirements for **DEFY GRAVITY** **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/3', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/581', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/24']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/3', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/5', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/3` | 0.909542 | **DEFY GRAVITY** **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/581` | 0.651873 | Defy Gravity |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/24` | 0.531816 | **PROPULSIVE SHIELD** **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/32` | 0.482999 | **SOLAR WIND** **FEAT 8** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/33` | 0.441125 | **Requirements** You're graviton-attuned. |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/31` | 0.441125 | **Requirements** You're graviton-attuned. |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/12` | 0.432948 | **MINDWARD SHIELD** **FEAT 8** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/17` | 0.419984 | **MOMENTUM **[one-action] **FEAT 8** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/582` | 0.416769 | 8 |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/602` | 0.404769 | 8 |

### Query 126
- Text: What are the requirements for **FLICKER STRIKE **[two-actions] **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/7', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/587', 'PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/40']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/7', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/9', 'PZO22001 Starfinder Player Core 138-149::/page/9/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/9/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/7` | 0.923504 | **FLICKER STRIKE **[two-actions] **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/587` | 0.662660 | Flicker Strike |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/40` | 0.638976 | **ECLIPSE STRIKE **[one-action] **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/37` | 0.552408 | **CAREFUL STRIKE **[one-action] **FEAT 10** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/6` | 0.464562 | **Photon-Attuned** If the Strike is a critical success, the target  must succeed at a Fortitude save against your class DC or  become clumsy 1 until the start of its turn. |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/15` | 0.459521 | **SHATTERING IMPACT **[two-actions] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/17` | 0.456105 | **MOMENTUM **[one-action] **FEAT 8** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/5` | 0.456045 | **Graviton-Attuned** If the Strike is a critical success, the target  must succeed at a Fortitude save against your class DC or  become enfeebled 1 until the end of its turn. |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/20` | 0.454807 | **Requirements** Your last action was a successful solar weapon  Strike. |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/7` | 0.439517 | You coordinate your attacks with both your solar flare and solar  weapon. Make two Strikes at the same target, one with your  solar weapon and one with your solar flare, each using your  current multi |

### Query 127
- Text: What are the requirements for **MINDWARD SHIELD** **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/12', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/24', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/32']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/12', 'PZO22001 Starfinder Player Core 138-149::/page/9/Text/11', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/9/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/12` | 0.891270 | **MINDWARD SHIELD** **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/24` | 0.693607 | **PROPULSIVE SHIELD** **FEAT 8** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/32` | 0.567382 | **SOLAR WIND** **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/597` | 0.513769 | Mindward Shield |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/16` | 0.513679 | **SOLAR SHIELD** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/3` | 0.456165 | **DEFY GRAVITY** **FEAT 8** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/15` | 0.453772 | **Prerequisites** Solar Shield |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/27` | 0.453772 | **Prerequisites** Solar Shield |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/17` | 0.439916 | **MOMENTUM **[one-action] **FEAT 8** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/8/Text/14` | 0.434856 | **Prerequisites** Nimbus Ward and Solar Shield |

### Query 128
- Text: What are the requirements for **Prerequisites** Solar Shield?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/15']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/27', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/15', 'PZO22001 Starfinder Player Core 138-149::/page/10/Text/39']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/15', 'PZO22001 Starfinder Player Core 138-149::/page/9/Text/16', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/14']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/9/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/27` | 0.976354 | **Prerequisites** Solar Shield |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/15` | 0.976354 | **Prerequisites** Solar Shield |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/39` | 0.806642 | **Prerequisites** Solar Shield plus either Black Hole or  Supernova |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/623` | 0.744849 | Solar Shield |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/8/Text/14` | 0.655475 | **Prerequisites** Nimbus Ward and Solar Shield |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/48` | 0.651590 | **Prerequisites** Solar Barrage |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/16` | 0.609024 | **SOLAR SHIELD** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/40` | 0.559689 | **Trigger** Your Solar Shield is destroyed while you have it  raised. |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/16` | 0.551899 | Your solar shield acts as an anchor for your mind as much as  your body. When your Raise your solar Shield, you gain the  shield's circumstance bonus to Will saves. In addition, while  you have your s |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/18` | 0.534426 | You've developed a new solar manifestation—a small shield  of stellar energy that orbits you. This energy shield has the  attuned and solarian traits and doesn't require a hand to use.  You can Raise |

### Query 129
- Text: What are the requirements for **MOMENTUM **[one-action] **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/17', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/601', 'PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/17', 'PZO22001 Starfinder Player Core 138-149::/page/9/Text/16', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/9/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/17` | 0.918855 | **MOMENTUM **[one-action] **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/601` | 0.567801 | Momentum |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/12` | 0.517639 | **MEDITATIVE ANALYSIS **[one-action] **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/20` | 0.461694 | **STAR BRAND **[one-action] **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/24` | 0.460596 | **PROPULSIVE SHIELD** **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/12` | 0.453437 | **MINDWARD SHIELD** **FEAT 8** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/32` | 0.452383 | **SOLAR WIND** **FEAT 8** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/7` | 0.450702 | **FLICKER STRIKE **[two-actions] **FEAT 8** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/28` | 0.441720 | **CONSTELLATION VORTEX **[one-action] **FEAT 6** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/29` | 0.440886 | **SINGULARITY **[three-actions] **FEAT 14** |

### Query 130
- Text: What are the requirements for **PROPULSIVE SHIELD** **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/24', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/613', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/24', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/26', 'PZO22001 Starfinder Player Core 138-149::/page/9/Text/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/9/Text/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/24` | 0.923477 | **PROPULSIVE SHIELD** **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/613` | 0.648092 | Propulsive Shield |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/12` | 0.647133 | **MINDWARD SHIELD** **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/16` | 0.525496 | **SOLAR SHIELD** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/27` | 0.490041 | **Prerequisites** Solar Shield |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/15` | 0.490041 | **Prerequisites** Solar Shield |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/32` | 0.487809 | **SOLAR WIND** **FEAT 8** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/3` | 0.469660 | **DEFY GRAVITY** **FEAT 8** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/39` | 0.432093 | **Prerequisites** Solar Shield plus either Black Hole or  Supernova |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/614` | 0.424773 | 8 |

### Query 131
- Text: What are the requirements for **Prerequisites** Solar Shield?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/27', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/15', 'PZO22001 Starfinder Player Core 138-149::/page/10/Text/39']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/27', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/26', 'PZO22001 Starfinder Player Core 138-149::/page/9/Text/28']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/9/Text/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/27` | 0.976354 | **Prerequisites** Solar Shield |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/15` | 0.976354 | **Prerequisites** Solar Shield |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/39` | 0.806642 | **Prerequisites** Solar Shield plus either Black Hole or  Supernova |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/623` | 0.744849 | Solar Shield |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/8/Text/14` | 0.655475 | **Prerequisites** Nimbus Ward and Solar Shield |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/48` | 0.651590 | **Prerequisites** Solar Barrage |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/16` | 0.609024 | **SOLAR SHIELD** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/40` | 0.559689 | **Trigger** Your Solar Shield is destroyed while you have it  raised. |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/16` | 0.551899 | Your solar shield acts as an anchor for your mind as much as  your body. When your Raise your solar Shield, you gain the  shield's circumstance bonus to Will saves. In addition, while  you have your s |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/18` | 0.534426 | You've developed a new solar manifestation—a small shield  of stellar energy that orbits you. This energy shield has the  attuned and solarian traits and doesn't require a hand to use.  You can Raise |

### Query 132
- Text: What are the requirements for **SOLAR WIND** **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/32', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/625', 'PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/32', 'PZO22001 Starfinder Player Core 138-149::/page/9/Text/31', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/34']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/9/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/34` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/32` | 0.910872 | **SOLAR WIND** **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/625` | 0.602313 | Solar Wind |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/16` | 0.569045 | **SOLAR SHIELD** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/15` | 0.522692 | **Prerequisites** Solar Shield |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/27` | 0.522692 | **Prerequisites** Solar Shield |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/24` | 0.510503 | **PROPULSIVE SHIELD** **FEAT 8** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/12` | 0.500825 | **MINDWARD SHIELD** **FEAT 8** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/39` | 0.488053 | **Prerequisites** Solar Shield plus either Black Hole or  Supernova |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/48` | 0.479784 | **Prerequisites** Solar Barrage |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/3` | 0.472899 | **DEFY GRAVITY** **FEAT 8** |

### Query 133
- Text: What are the requirements for **CAREFUL STRIKE **[one-action] **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/37', 'PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/40', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/37', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/36', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/39']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/39` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/37` | 0.917136 | **CAREFUL STRIKE **[one-action] **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/40` | 0.646631 | **ECLIPSE STRIKE **[one-action] **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/7` | 0.596647 | **FLICKER STRIKE **[two-actions] **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/42` | 0.517964 | **CLINGING FLARE **[one-action] **FEAT 10** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/46` | 0.510569 | **SOUL FURNACE **[one-action] **FEAT 10** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/567` | 0.477623 | Careful Strike |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/20` | 0.464431 | **Requirements** Your last action was a successful solar weapon  Strike. |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/5` | 0.456268 | **Graviton-Attuned** If the Strike is a critical success, the target  must succeed at a Fortitude save against your class DC or  become enfeebled 1 until the end of its turn. |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/6` | 0.448294 | **Photon-Attuned** If the Strike is a critical success, the target  must succeed at a Fortitude save against your class DC or  become clumsy 1 until the start of its turn. |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/8` | 0.424987 | **HAMPERING FLARE **[one-action] **FEAT 1** |

### Query 134
- Text: What are the requirements for **CLINGING FLARE **[one-action] **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/42']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/42', 'PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/8', 'PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/42', 'PZO22001 Starfinder Player Core 138-149::/page/9/Text/41', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/44']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/9/Text/41` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/44` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/42` | 0.908255 | **CLINGING FLARE **[one-action] **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/8` | 0.654251 | **HAMPERING FLARE **[one-action] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/7` | 0.627504 | **COVERING FLARE **[two-actions] **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/569` | 0.583274 | Clinging Flare |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/37` | 0.533965 | **CAREFUL STRIKE **[one-action] **FEAT 10** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/46` | 0.515388 | **SOUL FURNACE **[one-action] **FEAT 10** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/45` | 0.504489 | **UNSTABLE FLARE **[two-actions] **FEAT 14** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/36` | 0.465258 | **DISTANT FLARE** **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/28` | 0.441872 | **CONSTELLATION VORTEX **[one-action] **FEAT 6** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/40` | 0.437660 | **ECLIPSE STRIKE **[one-action] **FEAT 2** |

### Query 135
- Text: What are the requirements for **SOUL FURNACE **[one-action] **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/46']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/46', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/627', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/37']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/46', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/48', 'PZO22001 Starfinder Player Core 138-149::/page/9/Text/45']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/48` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/9/Text/45` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/46` | 0.907334 | **SOUL FURNACE **[one-action] **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/627` | 0.564557 | Soul Furnace |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/37` | 0.543498 | **CAREFUL STRIKE **[one-action] **FEAT 10** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/42` | 0.490471 | **CLINGING FLARE **[one-action] **FEAT 10** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/12` | 0.443696 | **MEDITATIVE ANALYSIS **[one-action] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/16` | 0.436758 | **SOLAR BARRAGE **[two-actions] **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/20` | 0.434347 | **STAR BRAND **[one-action] **FEAT 6** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/29` | 0.429959 | **SINGULARITY **[three-actions] **FEAT 14** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/51` | 0.420931 | **TWIN GUARD **[reaction] **FEAT 10** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/16` | 0.412811 | **SOLAR SHIELD** **FEAT 1** |

### Query 136
- Text: What are the requirements for **TWIN GUARD **[reaction] **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/51']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/51', 'PZO22001 Starfinder Player Core 138-149::/page/9/Text/54', 'PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/51', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/53', 'PZO22001 Starfinder Player Core 138-149::/page/9/Text/50']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/53` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/9/Text/50` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/51` | 0.881166 | **TWIN GUARD **[reaction] **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/54` | 0.612180 | **Prerequisites** Twin Weapons |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/31` | 0.579418 | **TWIN WEAPONS** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/637` | 0.457912 | Twin Guard |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/46` | 0.441480 | **SOUL FURNACE **[one-action] **FEAT 10** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/43` | 0.437925 | **NIMBUS WARD **[reaction]** OR **[one-action] **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/37` | 0.426647 | **CAREFUL STRIKE **[one-action] **FEAT 10** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/42` | 0.412832 | **CLINGING FLARE **[one-action] **FEAT 10** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/3/ListItem/19` | 0.404942 | Two-Hand 1d10 (counts as two traits) |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/68` | 0.398985 | **SKILLS** **FEATS** |

### Query 137
- Text: What are the requirements for **Prerequisites** Twin Weapons?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/9/Text/54']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/9/Text/54', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/639', 'PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/9/Text/54', 'PZO22001 Starfinder Player Core 138-149::/page/9/Text/55', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/53']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/9/Text/55` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/53` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/54` | 0.950488 | **Prerequisites** Twin Weapons |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/639` | 0.744864 | Twin Weapons |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/31` | 0.631486 | **TWIN WEAPONS** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/637` | 0.418700 | Twin Guard |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/34` | 0.413542 | You have a second solar weapon. When you take this feat  or Re-Forge Solar Weapon, choose its traits separately from  your first weapon. You can select a different damage type,  traits, and weapon gro |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/51` | 0.388127 | **TWIN GUARD **[reaction] **FEAT 10** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/27` | 0.372204 | **Prerequisites** Solar Shield |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/15` | 0.372204 | **Prerequisites** Solar Shield |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/8/Text/14` | 0.363422 | **Prerequisites** Nimbus Ward and Solar Shield |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/3/Text/9` | 0.362568 | At first level, choose up to two of the following traits for  your weapon. Alternatively, you can select the reach or twohand 1d10 trait for your weapon instead of selecting two of  the following trai |

### Query 138
- Text: What are the requirements for **ASCENDED STABILITY **[reaction] **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/2', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/555', 'PZO22001 Starfinder Player Core 138-149::/page/7/Table/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/2', 'PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/1', 'PZO22001 Starfinder Player Core 138-149::/page/10/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/10/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/2` | 0.914439 | **ASCENDED STABILITY **[reaction] **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/555` | 0.538264 | Ascended Stability |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/7/Table/3` | 0.470343 | FeatLevelAscended Stability12Attuned Blow16Attuned Wards18Big Bang14Binaric Assault1Black Hole4Careful Strike10Clinging Flare10Constellation Vortex6Corona6Cosmic Alignment20Cosmic Infusion4Covering Fl |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/45` | 0.403155 | **UNSTABLE FLARE **[two-actions] **FEAT 14** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/36` | 0.398915 | **STELLAR SHIELD COLLAPSE **[reaction] **FEAT 14** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/11` | 0.390340 | **WORMHOLE **[two-actions] **FEAT 12** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/556` | 0.390134 | 12 |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/15` | 0.380865 | **SHATTERING IMPACT **[two-actions] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/28` | 0.379964 | **CONSTELLATION VORTEX **[one-action] **FEAT 6** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/7` | 0.379251 | **COVERING FLARE **[two-actions] **FEAT 12** |

### Query 139
- Text: What are the requirements for **COVERING FLARE **[two-actions] **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/7', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/579', 'PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/45']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/7', 'PZO22001 Starfinder Player Core 138-149::/page/10/Text/9', 'PZO22001 Starfinder Player Core 138-149::/page/10/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/10/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/10/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/7` | 0.931046 | **COVERING FLARE **[two-actions] **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/579` | 0.648033 | Covering Flare |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/45` | 0.645253 | **UNSTABLE FLARE **[two-actions] **FEAT 14** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/8` | 0.595236 | **HAMPERING FLARE **[one-action] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/42` | 0.577260 | **CLINGING FLARE **[one-action] **FEAT 10** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/11` | 0.526161 | **WORMHOLE **[two-actions] **FEAT 12** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/36` | 0.508755 | **DISTANT FLARE** **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/16` | 0.471802 | **SOLAR BARRAGE **[two-actions] **FEAT 6** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/10` | 0.453402 | You use your solar flare to cover yourself as you close in  on your foes. You Stride twice; at any point during this  movement, you can make a solar flare Strike. On a hit, the  target is also suppres |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/589` | 0.450186 | Hampering Flare |

### Query 140
- Text: What are the requirements for **WORMHOLE **[two-actions] **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/11', 'PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/27', 'PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/11', 'PZO22001 Starfinder Player Core 138-149::/page/10/Text/13', 'PZO22001 Starfinder Player Core 138-149::/page/10/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/10/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/10/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/11` | 0.927238 | **WORMHOLE **[two-actions] **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/27` | 0.611252 | **BLACK HOLE **[two-actions] **FEAT 4** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/7` | 0.559280 | **COVERING FLARE **[two-actions] **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/643` | 0.503296 | Wormhole |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/15` | 0.454212 | You force a rip in space that acts as a tunnel to a nearby  location. Create two wormholes in unoccupied squares in  line of effect that are within 100 feet, visible to you, and at  least 15 feet apar |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/5` | 0.447876 | **CORONA **[two-actions] **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/43` | 0.436544 | **Graviton-Attuned** Immediately use Black Hole as a free  action (if you have the Black Hole feat). |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/16` | 0.435730 | **Graviton-Attuned** A creature beginning its turn adjacent  to a wormhole must succeed at a Fortitude save against  your class DC or be pulled into the wormhole. |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/15` | 0.426456 | **SHATTERING IMPACT **[two-actions] **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/7` | 0.423071 | **PLASMA EJECTION **[two-actions] **FEAT 4** |

### Query 141
- Text: What are the requirements for **BIG BANG **[three-actions] **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/19', 'PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/29', 'PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/45']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/19', 'PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/18', 'PZO22001 Starfinder Player Core 138-149::/page/10/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/10/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/19` | 0.906102 | **BIG BANG **[three-actions] **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/29` | 0.650521 | **SINGULARITY **[three-actions] **FEAT 14** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/45` | 0.522664 | **UNSTABLE FLARE **[two-actions] **FEAT 14** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/27` | 0.451802 | **BLACK HOLE **[two-actions] **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/14` | 0.420670 | **SUPERNOVA **[two-actions] **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/20` | 0.397088 | **STAR BRAND **[one-action] **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/16` | 0.390594 | **SOLAR BARRAGE **[two-actions] **FEAT 6** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/43` | 0.389122 | **NIMBUS WARD **[reaction]** OR **[one-action] **FEAT 4** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/561` | 0.384846 | Big Bang |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/25` | 0.380388 | **STELLAR RUSH **[two-actions] **FEAT 1** |

### Query 142
- Text: What are the requirements for **SINGULARITY **[three-actions] **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/29', 'PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/19', 'PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/45']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/29', 'PZO22001 Starfinder Player Core 138-149::/page/10/Text/28', 'PZO22001 Starfinder Player Core 138-149::/page/10/Text/31']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/10/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/10/Text/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/29` | 0.943014 | **SINGULARITY **[three-actions] **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/19` | 0.618060 | **BIG BANG **[three-actions] **FEAT 14** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/45` | 0.544215 | **UNSTABLE FLARE **[two-actions] **FEAT 14** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/617` | 0.500654 | Singularity |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/36` | 0.436791 | **STELLAR SHIELD COLLAPSE **[reaction] **FEAT 14** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/27` | 0.434164 | **BLACK HOLE **[two-actions] **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/12` | 0.427587 | **MEDITATIVE ANALYSIS **[one-action] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/14` | 0.419183 | **SUPERNOVA **[two-actions] **FEAT 4** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/46` | 0.406650 | **SOUL FURNACE **[one-action] **FEAT 10** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/17` | 0.402439 | **MOMENTUM **[one-action] **FEAT 8** |

### Query 143
- Text: What are the requirements for **STELLAR SHIELD COLLAPSE **[reaction] **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/36']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/36', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/633', 'PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/36', 'PZO22001 Starfinder Player Core 138-149::/page/10/Text/35', 'PZO22001 Starfinder Player Core 138-149::/page/10/Text/38']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/10/Text/35` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/10/Text/38` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/36` | 0.919186 | **STELLAR SHIELD COLLAPSE **[reaction] **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/633` | 0.672544 | Stellar Shield Collapse |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/16` | 0.559023 | **SOLAR SHIELD** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/29` | 0.491683 | **SINGULARITY **[three-actions] **FEAT 14** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/25` | 0.480573 | **STELLAR RUSH **[two-actions] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/45` | 0.478693 | **UNSTABLE FLARE **[two-actions] **FEAT 14** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/39` | 0.476773 | **Prerequisites** Solar Shield plus either Black Hole or  Supernova |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/27` | 0.472273 | **Prerequisites** Solar Shield |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/15` | 0.472273 | **Prerequisites** Solar Shield |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/7/Table/20` | 0.464379 | FeatLevelMomentum8Mutable Manifestation2Nimbus Block6Nimbus Ward4Perfectly-Attuned20Plasma Ejection4Propulsive Shield8Shattering Impact2Singularity14Solar Barrage6Solar Rampart2Solar Shield1Solar Wind |

### Query 144
- Text: What are the requirements for **Prerequisites** Solar Shield plus either Black Hole or  Supernova?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/10/Text/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/10/Text/39', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/27', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/10/Text/39', 'PZO22001 Starfinder Player Core 138-149::/page/10/Text/40', 'PZO22001 Starfinder Player Core 138-149::/page/10/Text/38']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/10/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/10/Text/38` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/39` | 0.982693 | **Prerequisites** Solar Shield plus either Black Hole or  Supernova |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/27` | 0.859432 | **Prerequisites** Solar Shield |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/15` | 0.859432 | **Prerequisites** Solar Shield |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/623` | 0.637219 | Solar Shield |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/41` | 0.612749 | **Requirements** You haven't used Black Hole or Supernova  within the last 10 minutes. |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/8/Text/14` | 0.602810 | **Prerequisites** Nimbus Ward and Solar Shield |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/48` | 0.580704 | **Prerequisites** Solar Barrage |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/16` | 0.542165 | **SOLAR SHIELD** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/5/Text/18` | 0.503792 | You've developed a new solar manifestation—a small shield  of stellar energy that orbits you. This energy shield has the  attuned and solarian traits and doesn't require a hand to use.  You can Raise |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/40` | 0.483752 | **Trigger** Your Solar Shield is destroyed while you have it  raised. |

### Query 145
- Text: What are the requirements for **UNSTABLE FLARE **[two-actions] **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/45']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/45', 'PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/7', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/641']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/45', 'PZO22001 Starfinder Player Core 138-149::/page/10/Text/47', 'PZO22001 Starfinder Player Core 138-149::/page/10/Text/44']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/10/Text/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/10/Text/44` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/45` | 0.928193 | **UNSTABLE FLARE **[two-actions] **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/7` | 0.671624 | **COVERING FLARE **[two-actions] **FEAT 12** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/641` | 0.593557 | Unstable Flare |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/29` | 0.550139 | **SINGULARITY **[three-actions] **FEAT 14** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/8` | 0.541429 | **HAMPERING FLARE **[one-action] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/5/SectionHeader/36` | 0.525990 | **DISTANT FLARE** **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/42` | 0.519405 | **CLINGING FLARE **[one-action] **FEAT 10** |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/19` | 0.506832 | **BIG BANG **[three-actions] **FEAT 14** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/27` | 0.457054 | **BLACK HOLE **[two-actions] **FEAT 4** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/10/SectionHeader/2` | 0.451140 | **ASCENDED STABILITY **[reaction] **FEAT 12** |

### Query 146
- Text: What are the requirements for **Prerequisites** Solar Barrage?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/10/Text/48']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/10/Text/48', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/619', 'PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/10/Text/48', 'PZO22001 Starfinder Player Core 138-149::/page/10/Text/47', 'PZO22001 Starfinder Player Core 138-149::/page/10/Text/49']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/10/Text/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/10/Text/49` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/48` | 0.980000 | **Prerequisites** Solar Barrage |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/619` | 0.806789 | Solar Barrage |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/15` | 0.698076 | **Prerequisites** Solar Shield |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/27` | 0.656076 | **Prerequisites** Solar Shield |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/39` | 0.562195 | **Prerequisites** Solar Shield plus either Black Hole or  Supernova |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/8/SectionHeader/16` | 0.539206 | **SOLAR BARRAGE **[two-actions] **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/8/Text/14` | 0.501288 | **Prerequisites** Nimbus Ward and Solar Shield |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/623` | 0.454691 | Solar Shield |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/8/Text/23` | 0.437006 | **Requirements** Your last action was a successful solar flare or  solar weapon Strike against a creature. |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/9/Text/20` | 0.436266 | **Requirements** Your last action was a successful solar weapon  Strike. |

### Query 147
- Text: What are the requirements for **ATTUNED BLOW** **FEAT 16**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/2', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/557', 'PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/2', 'PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/4', 'PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/2` | 0.907073 | **ATTUNED BLOW** **FEAT 16** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/557` | 0.644085 | Attuned Blow |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/11` | 0.558139 | **ATTUNED WARDS** **FEAT 18** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/26` | 0.474525 | **PERFECTLY-ATTUNED** **FEAT 20** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/6` | 0.453425 | **HARMONIC CONVERGENCE** **FEAT 16** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/1` | 0.446162 | 16TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/23` | 0.424459 | **Requirements** You're photon-attuned. |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/18` | 0.424459 | **Requirements** You're photon-attuned. |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/44` | 0.413016 | **Photon-Attuned** Immediately use Supernova as a free action  (if you have the Supernova feat). |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/13` | 0.397501 | **ATTUNED** **SOLARIAN** |

### Query 148
- Text: What are the requirements for **HARMONIC CONVERGENCE** **FEAT 16**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/6', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/591', 'PZO22001 Starfinder Player Core 138-149::/page/7/Table/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/6', 'PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/8', 'PZO22001 Starfinder Player Core 138-149::/page/11/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/11/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/6` | 0.927305 | **HARMONIC CONVERGENCE** **FEAT 16** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/591` | 0.680558 | Harmonic Convergence |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/7/Table/3` | 0.483588 | FeatLevelAscended Stability12Attuned Blow16Attuned Wards18Big Bang14Binaric Assault1Black Hole4Careful Strike10Clinging Flare10Constellation Vortex6Corona6Cosmic Alignment20Cosmic Infusion4Covering Fl |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/2` | 0.426105 | **ATTUNED BLOW** **FEAT 16** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/592` | 0.415542 | 16 |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/1` | 0.415366 | 16TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/558` | 0.403542 | 16 |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/420` | 0.403542 | 16 |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/SectionHeader/28` | 0.395399 | **CONSTELLATION VORTEX **[one-action] **FEAT 6** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/22` | 0.381722 | **COSMIC ALIGNMENT** **FEAT 20** |

### Query 149
- Text: What are the requirements for **ATTUNED WARDS** **FEAT 18**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/11', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/559', 'PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/11', 'PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/13', 'PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/11` | 0.899378 | **ATTUNED WARDS** **FEAT 18** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/559` | 0.575432 | Attuned Wards |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/2` | 0.568203 | **ATTUNED BLOW** **FEAT 16** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/26` | 0.474703 | **PERFECTLY-ATTUNED** **FEAT 20** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/17` | 0.463177 | **HOMING MOTE** **FEAT 18** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/23` | 0.455791 | **Requirements** You're photon-attuned. |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/18` | 0.455791 | **Requirements** You're photon-attuned. |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/560` | 0.412251 | 18 |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/6/Text/3` | 0.407138 | **Attuned:** You can't use abilities with the attuned  trait while you're unattuned. Many attuned abilities  require you to be specifically graviton-attuned or  photon-attuned, while others can grant |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/13` | 0.405873 | **ATTUNED** **SOLARIAN** |

### Query 150
- Text: What are the requirements for **HOMING MOTE** **FEAT 18**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/17', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/593', 'PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/17', 'PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/19', 'PZO22001 Starfinder Player Core 138-149::/page/11/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/11/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/17` | 0.900741 | **HOMING MOTE** **FEAT 18** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/593` | 0.581864 | Homing Mote |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/10` | 0.480346 | 18TH LEVEL |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/594` | 0.443991 | 18 |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/11` | 0.439672 | **ATTUNED WARDS** **FEAT 18** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/424` | 0.431991 | 18 |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/560` | 0.431991 | 18 |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/6` | 0.392220 | **HARMONIC CONVERGENCE** **FEAT 16** |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/9/SectionHeader/17` | 0.357318 | **MOMENTUM **[one-action] **FEAT 8** |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/41` | 0.354541 | **FEATS** |

### Query 151
- Text: What are the requirements for **COSMIC ALIGNMENT** **FEAT 20**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/22', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/575', 'PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/22', 'PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/24', 'PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/22` | 0.928298 | **COSMIC ALIGNMENT** **FEAT 20** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/575` | 0.672083 | Cosmic Alignment |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/26` | 0.572665 | **PERFECTLY-ATTUNED** **FEAT 20** |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/7/Table/3` | 0.454885 | FeatLevelAscended Stability12Attuned Blow16Attuned Wards18Big Bang14Binaric Assault1Black Hole4Careful Strike10Clinging Flare10Constellation Vortex6Corona6Cosmic Alignment20Cosmic Infusion4Covering Fl |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/11/Text/25` | 0.449646 | You reach true alignment with the cosmic cycle. You're  permanently quickened. You can use your extra action  only to Attune or make a Strike with your solar flare or  solar weapon. |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/6/SectionHeader/38` | 0.446175 | **COSMIC INFUSION** **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/21` | 0.440431 | 20TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/39` | 0.424442 | **Prerequisites** Solar Shield plus either Black Hole or  Supernova |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/576` | 0.422505 | 20 |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/428` | 0.410505 | 20 |

### Query 152
- Text: What are the requirements for **PERFECTLY-ATTUNED** **FEAT 20**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/26', 'PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/22', 'PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/609']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/26', 'PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/28', 'PZO22001 Starfinder Player Core 138-149::/page/11/Text/25']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 138-149::/page/11/Text/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/26` | 0.894086 | **PERFECTLY-ATTUNED** **FEAT 20** |
| 2 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/22` | 0.582552 | **COSMIC ALIGNMENT** **FEAT 20** |
| 3 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/609` | 0.559922 | Perfectly-Attuned |
| 4 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/11` | 0.470071 | **ATTUNED WARDS** **FEAT 18** |
| 5 | `PZO22001 Starfinder Player Core 138-149::/page/11/SectionHeader/2` | 0.463374 | **ATTUNED BLOW** **FEAT 16** |
| 6 | `PZO22001 Starfinder Player Core 138-149::/page/7/Text/18` | 0.454647 | **Requirements** You're photon-attuned. |
| 7 | `PZO22001 Starfinder Player Core 138-149::/page/10/Text/23` | 0.454647 | **Requirements** You're photon-attuned. |
| 8 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/610` | 0.438634 | 20 |
| 9 | `PZO22001 Starfinder Player Core 138-149::/page/2/TableCell/428` | 0.426634 | 20 |
| 10 | `PZO22001 Starfinder Player Core 138-149::/page/7/TableCell/576` | 0.426634 | 20 |
