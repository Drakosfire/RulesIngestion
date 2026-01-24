# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `648`
- Query count: `154`
- Evaluated queries: `154`
- Coverage: `1.0000`
- MRR: `0.8974`
- hit@1: `0.8442`
- hit@3: `0.9221`
- hit@5: `0.9805`
- hit@10: `1.0000`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

### Expanded Gold Metrics
- Coverage: `1.0000`
- MRR: `0.9038`
- hit@1: `0.8571`
- hit@3: `0.9221`
- hit@5: `0.9805`
- hit@10: `1.0000`

### Expanded Gold Expansion Stats
- Queries with additions: `154`
- Avg added per query: `2.08`
- Max added: `7`
- Addition reasons:
  - graph_depth_1: `320`

### Expanded Gold Delta (Expanded - Strict)
- Coverage Δ: `0.0000`
- MRR Δ: `0.0065`
- hit@1 Δ: `0.0130`
- hit@3 Δ: `0.0000`
- hit@5 Δ: `0.0000`
- hit@10 Δ: `0.0000`

## Timings (ms)
- Embedding (chunks): `9427`
- Embedding (queries): `2439`
- Evaluation (strict): `70`
- Evaluation (expanded): `52`
- Total: `16402`

### Timing Estimates (ms)
- Evaluation (strict): `354`
- Evaluation (expanded): `107`
- Total: `12327`

## Query Details
### Query 0
- Text: Summarize OPERATIVE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/34', 'PZO22001 Starfinder Player Core 126-137::/page/11/Text/32']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/1` | 0.899805 | OPERATIVE |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/34` | 0.829902 | **Operative ** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/32` | 0.829902 | **Operative ** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/15` | 0.642947 | OPERATIVE'S SPECIALIZATION |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/1` | 0.642781 | **Sample Operative** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/42` | 0.635268 | **OPERATIVE** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/33` | 0.635268 | **OPERATIVE** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/59` | 0.635268 | **OPERATIVE** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/41` | 0.635268 | **OPERATIVE** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/9` | 0.635268 | **OPERATIVE** |

### Query 1
- Text: What is the rule about You're a focused, quick-witted professional who thrives in high-stakes combat. Your deadly aim and  tactical training give you an edge over the competition—for you, even the most powerful enemy is just  another mark to take out. You have impressive prowess in your chosen field of specialization.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/2', 'PZO22001 Starfinder Player Core 126-137::/page/3/Text/23', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/2', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/4', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/2` | 0.971304 | You're a focused, quick-witted professional who thrives in high-stakes combat. Your deadly aim and  tactical training give you an edge over the competition—for you, even the most powerful enemy is jus |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/23` | 0.702014 | You specialize in hand-to-hand combat and prefer to fight  with your fists or lightweight melee weapons, rather than  guns. Whether you're a daredevil who lives for the thrill, a  martial artist who l |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/11` | 0.700206 | You attack and maneuver with tactical precision, whether you're lining up the  perfect headshot from a distance, dueling hand-to-hand, or trading shots at close  range. At higher levels, you master yo |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/23` | 0.624963 | You are a highly skilled sharpshooter and never go anywhere  without your gun. Your proficiency rank increases to master  with simple and martial guns, and increases to expert with  advanced guns. You |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/13` | 0.622961 | You're a local legend who's known for your prowess with  weaponry. Your proficiency rank increases to legendary  with simple and martial guns, and to master with advanced  guns. Your proficiency rank |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/19` | 0.616247 | You specialize in targeting foes from far away and attacking  while unseen. Whether you're peeking around a corner,  perching on a distant rooftop, or aiming from the back line  of a squad formation, |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/22` | 0.598082 | Your extensive training has transformed you into a living  weapon, ready to pull the trigger at a moment's notice. At the  start of each enemy's turn, you gain an additional reaction  during that turn |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/22` | 0.592766 | Rely on you for strategic advice and firepower in a fight but feel put off by your  talent for methodical violence. |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/47` | 0.586365 | You're rarely still, and you've learned to reliably hit your  targets even while moving. You Stride and then Aim with a  gun you're wielding. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/23` | 0.583074 | Your reputation as a shooter precedes you wherever you go  in the galaxy. Your proficiency rank increases to legendary  with advanced guns. Your proficiency rank for your  operative class DC increases |

### Query 2
- Text: Summarize **KEY ATTRIBUTE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/4', 'PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/1', 'PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/4', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/5', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/4` | 0.948607 | **KEY ATTRIBUTE** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/1` | 0.665018 | **KEY TERMS** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/4` | 0.599101 | **Attributes** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/10` | 0.471900 | **Feats** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/50` | 0.437617 | **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/44` | 0.437617 | **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/80` | 0.437617 | **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/2` | 0.410597 | You'll see the following key terms in many operative  class features. |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/8` | 0.408012 | **Specialization** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/77` | 0.407698 | **INDEX** |

### Query 3
- Text: Summarize **Dexterity**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/5', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/6', 'PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/5', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/6', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/5` | 0.967620 | **Dexterity** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/6` | 0.553902 | At 1st level, your class gives you  an attribute boost to Dexterity |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/8` | 0.452448 | **Specialization** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/8/Text/5` | 0.380851 | Make Dexterity highest, followed by Constitution and  Intelligence if you want more skills or Strength if you  plan to fight in melee. |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/29` | 0.379105 | **INTRODUCTION** **ANCESTRIES & ** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/62` | 0.379105 | **INTRODUCTION** **ANCESTRIES & ** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/33` | 0.379105 | **INTRODUCTION** **ANCESTRIES & ** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/49` | 0.364358 | **EXPLOSIVE DEFLECTION** **FEAT 16** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/29` | 0.353075 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/58` | 0.353075 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 4
- Text: Summarize At 1st level, your class gives you  an attribute boost to Dexterity
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/6', 'PZO22001 Starfinder Player Core 126-137::/page/2/Text/4', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/27']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/6', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/5', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/6` | 1.037960 | At 1st level, your class gives you  an attribute boost to Dexterity |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/4` | 0.714145 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/27` | 0.625573 | In addition to what you get from your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/8/Text/5` | 0.573346 | Make Dexterity highest, followed by Constitution and  Intelligence if you want more skills or Strength if you  plan to fight in melee. |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/5` | 0.564699 | At 5th level and every 5 levels thereafter, you get four  free boosts to different attribute modifiers. If an attribute  modifier is already +4 or higher, it takes two boosts to  increase it; you get |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/7` | 0.559497 | At 1st level, you gain a number of proficiencies that  represent your basic training. These proficiencies are noted  at the start of this class. |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/25` | 0.510843 | You gain these abilities as an operative. Abilities gained at higher levels list the level  at which you gain them next to the features' names. |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/Table/2` | 0.509120 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, sharpshooter, Aim 1d4, operative's specialization, operative feat2Operative feat, skill feat3Focused, general |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/5` | 0.500196 | **Dexterity** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/9` | 0.479034 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |

### Query 5
- Text: What is the rule about **HIT POINTS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/7', 'PZO22001 Starfinder Player Core 126-137::/page/10/Text/31', 'PZO22001 Starfinder Player Core 126-137::/page/10/Text/22']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/7', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/6', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/7` | 0.884304 | **HIT POINTS** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/31` | 0.474396 | As the old saying goes: hitting easy targets is like shooting fish  in a barrel. You Aim and then make a ranged Strike against a  prone or immobilized creature not benefiting from cover. Treat  a succ |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/22` | 0.445118 | When Bullet Fever ends, you lose any remaining temporary  Hit Points from Bullet Fever. |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/10` | 0.389076 | You aim your shots to unbalance your foe, pushing them back  or knocking them over. You Aim and then make a ranged Strike  against your mark. If the Strike hits, the target is knocked back  5 feet. If |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/1` | 0.378968 | the target of your last Strike; on a success, you're hidden  from the target or undetected on a critical success. |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/17` | 0.376021 | **Trigger** You take damage that would reduce you to 0 Hit Points. You fly into a frenzy instead of accepting defeat. Instead  of being knocked out, you're reduced to 1 Hit Point, gain a  number of te |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/3` | 0.365008 | **Aim:** An action used to focus on a target and deal  additional precision damage (page 128). |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/21` | 0.364250 | You hinder your target with a shot. You Aim and then make a  ranged Strike against your mark. If the Strike hits, the target  is slowed 1 until the end of its next turn. If the target is flying,  it a |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/12` | 0.356144 | You take careful aim at your mark and shoot to kill. You  Aim and then make a ranged Strike against your mark. If  this attack is a success (but not a critical success), you deal  maximum damage. Calc |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/8/Text/35` | 0.355724 | **Requirements** Your last ranged Strike this turn missed or hit  and failed to damage the target. |

### Query 6
- Text: What is the rule about **8 + Constitution modifier**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/8', 'PZO22001 Starfinder Player Core 126-137::/page/2/Text/5', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/652']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/8', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/9', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/8` | 0.865498 | **8 + Constitution modifier** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/5` | 0.478496 | At 5th level and every 5 levels thereafter, you get four  free boosts to different attribute modifiers. If an attribute  modifier is already +4 or higher, it takes two boosts to  increase it; you get |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/652` | 0.458298 | 8 |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/620` | 0.416298 | 8 |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/402` | 0.416298 | 8 |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/656` | 0.416298 | 8 |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/626` | 0.416298 | 8 |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/55` | 0.368330 | Trained in one skill determined by  your specialization Trained in a number of additional  skills equal to 3 plus your Intelligence  modifier |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/4` | 0.363675 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/6` | 0.329663 | **TOPPLING SHOT **[two-actions] **FEAT 8** |

### Query 7
- Text: Summarize You increase your maximum number  of HP by this number at 1st level and  every level thereafter.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/9', 'PZO22001 Starfinder Player Core 126-137::/page/4/Text/16', 'PZO22001 Starfinder Player Core 126-137::/page/2/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/9', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/9` | 1.031874 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/16` | 0.619588 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you're untrained in or to become an expert in one  skill in whi |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/5` | 0.604495 | At 5th level and every 5 levels thereafter, you get four  free boosts to different attribute modifiers. If an attribute  modifier is already +4 or higher, it takes two boosts to  increase it; you get |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/25` | 0.554042 | You gain these abilities as an operative. Abilities gained at higher levels list the level  at which you gain them next to the features' names. |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/6` | 0.537136 | At 1st level and every even-numbered level, you gain an  operative class feat. These begin on page 131. |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/14` | 0.537089 | At 3rd level and every 4 levels thereafter, you gain a  general feat. |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/4` | 0.520901 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/17` | 0.516332 | At 7th level, you can use skill increases to become a  master in a skill in which you're already an expert, and at  15th level, you can use them to become legendary in a skill  in which you're already |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/49` | 0.514252 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/10` | 0.510241 | At 2nd level and every 2 levels thereafter, you gain a skill  feat. You must be trained or better in the corresponding skill  to select a skill feat. |

### Query 8
- Text: Summarize DURING COMBAT ENCOUNTERS...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/12', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/9', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/10` | 0.983036 | DURING COMBAT ENCOUNTERS... |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/12` | 0.745777 | DURING SOCIAL ENCOUNTERS... |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/14` | 0.434305 | WHILE EXPLORING... |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/55` | 0.358920 | **Requirements** You aren't encumbered. |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/16` | 0.337787 | IN DOWNTIME... |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/67` | 0.333292 | **Soldier** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/63` | 0.333292 | **Soldier** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/38` | 0.333292 | **Soldier** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/34` | 0.333292 | **Soldier** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/36` | 0.333292 | **Soldier** |

### Query 9
- Text: What is the rule about You attack and maneuver with tactical precision, whether you're lining up the  perfect headshot from a distance, dueling hand-to-hand, or trading shots at close  range. At higher levels, you master your weapons of choice and rain calculated  destruction on foes.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/11', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/2', 'PZO22001 Starfinder Player Core 126-137::/page/5/Text/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/11', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/11` | 0.923073 | You attack and maneuver with tactical precision, whether you're lining up the  perfect headshot from a distance, dueling hand-to-hand, or trading shots at close  range. At higher levels, you master yo |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/2` | 0.641948 | You're a focused, quick-witted professional who thrives in high-stakes combat. Your deadly aim and  tactical training give you an edge over the competition—for you, even the most powerful enemy is jus |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/13` | 0.624680 | You're a local legend who's known for your prowess with  weaponry. Your proficiency rank increases to legendary  with simple and martial guns, and to master with advanced  guns. Your proficiency rank |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/19` | 0.571340 | You specialize in targeting foes from far away and attacking  while unseen. Whether you're peeking around a corner,  perching on a distant rooftop, or aiming from the back line  of a squad formation, |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/23` | 0.565760 | You are a highly skilled sharpshooter and never go anywhere  without your gun. Your proficiency rank increases to master  with simple and martial guns, and increases to expert with  advanced guns. You |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/5` | 0.561004 | You rush forward, firing a precisely aimed shot at your enemy  while you're on the move. Aim and then Stride up to your  Speed. At any point during this movement, you can make a  ranged Strike with th |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/24` | 0.559675 | **Exploit:** You have expert proficiency with one-handed  melee weapons and unarmed attacks with the agile or  finesse traits instead of with martial guns. Whenever you  increase your proficiency with |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/23` | 0.548593 | Your reputation as a shooter precedes you wherever you go  in the galaxy. Your proficiency rank increases to legendary  with advanced guns. Your proficiency rank for your  operative class DC increases |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/23` | 0.543071 | You specialize in hand-to-hand combat and prefer to fight  with your fists or lightweight melee weapons, rather than  guns. Whether you're a daredevil who lives for the thrill, a  martial artist who l |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/26` | 0.540381 | You fire two shots at the same target in quick succession.  You Aim and then make two Strikes against your mark.  Apply the multiple attack penalty normally. If both attacks  hit, combine their damage |

### Query 10
- Text: Summarize DURING SOCIAL ENCOUNTERS...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/12', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/12', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/13', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/12` | 0.977694 | DURING SOCIAL ENCOUNTERS... |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/10` | 0.728104 | DURING COMBAT ENCOUNTERS... |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/14` | 0.408727 | WHILE EXPLORING... |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/55` | 0.339718 | **Requirements** You aren't encumbered. |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/16` | 0.315217 | IN DOWNTIME... |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/21` | 0.286287 | OTHERS PROBABLY... |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/18` | 0.285896 | YOU MIGHT... |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/35` | 0.282589 | **Envoy** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/32` | 0.282589 | **Envoy** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/64` | 0.282589 | **Envoy** |

### Query 11
- Text: What is the rule about You might fall back on your training, speaking up to give strategic advice to your  allies while remaining alert for strangers' hidden agendas or take the lead about a  subject you know.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/13', 'PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/22', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/13', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/13` | 0.949568 | You might fall back on your training, speaking up to give strategic advice to your  allies while remaining alert for strangers' hidden agendas or take the lead about a  subject you know. |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/22` | 0.564102 | Rely on you for strategic advice and firepower in a fight but feel put off by your  talent for methodical violence. |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/2` | 0.550334 | You're a focused, quick-witted professional who thrives in high-stakes combat. Your deadly aim and  tactical training give you an edge over the competition—for you, even the most powerful enemy is jus |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/18` | 0.507157 | You specialize in slipping into a location, completing an  objective, and extricating yourself without being discovered.  You might use stealth tactics, cover identities, disguises, or  spy tech. Whet |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/30` | 0.479917 | You're able to move deftly around your foes, getting out of  tricky situations or managing to put yourself into a place  where you hold the advantage. You Step up to twice directly  toward the trigger |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/36` | 0.477929 | You've trained in close quarters combat and practiced how to  escape a hold, or similar situations. You attempt to Escape. If  you succeed or critically succeed, you can also Stand or Step. |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/22` | 0.474690 | Your extensive training has transformed you into a living  weapon, ready to pull the trigger at a moment's notice. At the  start of each enemy's turn, you gain an additional reaction  during that turn |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/1` | 0.473033 | the target of your last Strike; on a success, you're hidden  from the target or undetected on a critical success. |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/19` | 0.467691 | Have trained with a military organization or mercenary group that you remain  allied with or have defected from. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/19` | 0.464406 | You specialize in targeting foes from far away and attacking  while unseen. Whether you're peeking around a corner,  perching on a distant rooftop, or aiming from the back line  of a squad formation, |

### Query 12
- Text: Summarize WHILE EXPLORING...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/12', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/13', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/14` | 0.945993 | WHILE EXPLORING... |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/12` | 0.439598 | DURING SOCIAL ENCOUNTERS... |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/10` | 0.437469 | DURING COMBAT ENCOUNTERS... |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/4` | 0.350727 | **Exploit:** Your tinkering causes technological items and  creatures to experience glitches and malfunctions. You gain  the Sabotage action. |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/16` | 0.348777 | IN DOWNTIME... |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/31` | 0.339180 | **Enhanced Exploit:** You find yourself able to overwhelm  foes that you study. You gain the Overwhelming Strike  free action. |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/1` | 0.337585 | **Sample Operative** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/44` | 0.330508 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/45` | 0.330508 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/74` | 0.330508 | **PLAYING THE ** **GAME** |

### Query 13
- Text: What is the rule about You take a tactical position like point or rear guard and scan your surroundings,  keeping your weapon ready for action.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/15', 'PZO22001 Starfinder Player Core 126-137::/page/5/Text/39', 'PZO22001 Starfinder Player Core 126-137::/page/5/Text/43']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/15', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/15` | 0.942718 | You take a tactical position like point or rear guard and scan your surroundings,  keeping your weapon ready for action. |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/39` | 0.565270 | You draw your gun and take careful aim with the same  motion. You Interact to draw a ranged weapon or Switch  Hands and then Aim with that ranged weapon. |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/43` | 0.552001 | You always keep a target marked and in your sights, even if  they move. When you Aim, the benefits apply if your mark  is within your weapon's first or second range increment,  rather than only within |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/35` | 0.507663 | You shoot and then duck out of the way to avoid retaliation  and errant gunfire. Make a ranged Strike, then Take Cover. |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/47` | 0.501880 | You're rarely still, and you've learned to reliably hit your  targets even while moving. You Stride and then Aim with a  gun you're wielding. |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/27` | 0.495464 | You shoot a spray of bullets at a target. You Aim, make a  ranged Strike against your mark, and subtract three times  your weapon's expend from its magazine. Roll the attack twice,  and use the better |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/5` | 0.494960 | You rush forward, firing a precisely aimed shot at your enemy  while you're on the move. Aim and then Stride up to your  Speed. At any point during this movement, you can make a  ranged Strike with th |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/53` | 0.494295 | **Requirements** You're aware of the attack, wielding a gun, and  not off-guard. |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/11` | 0.492031 | You attack and maneuver with tactical precision, whether you're lining up the  perfect headshot from a distance, dueling hand-to-hand, or trading shots at close  range. At higher levels, you master yo |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/17` | 0.490392 | You train with your weapons, acquire and upgrade equipment, and practice tactical  drills for future engagements. |

### Query 14
- Text: Summarize IN DOWNTIME...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/16', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/16', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/17', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/16` | 0.786911 | IN DOWNTIME... |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/18` | 0.405938 | YOU MIGHT... |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/1` | 0.394200 | **Sample Operative** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/12` | 0.325088 | DURING SOCIAL ENCOUNTERS... |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/14` | 0.322232 | WHILE EXPLORING... |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/10` | 0.314851 | DURING COMBAT ENCOUNTERS... |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/21` | 0.302606 | OTHERS PROBABLY... |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/8` | 0.289874 | **Specialization** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/1` | 0.287179 | **KEY TERMS** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/10` | 0.282115 | **Feats** |

### Query 15
- Text: What is the rule about You train with your weapons, acquire and upgrade equipment, and practice tactical  drills for future engagements.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/17', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/57', 'PZO22001 Starfinder Player Core 126-137::/page/3/Text/24']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/17', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/17` | 0.887535 | You train with your weapons, acquire and upgrade equipment, and practice tactical  drills for future engagements. |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/57` | 0.559026 | Expert in simple guns Expert in martial guns Trained in advanced guns Trained in simple weapons Trained in martial weapons Trained in unarmed attacks |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/24` | 0.548889 | **Exploit:** You have expert proficiency with one-handed  melee weapons and unarmed attacks with the agile or  finesse traits instead of with martial guns. Whenever you  increase your proficiency with |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/15` | 0.502166 | You take a tactical position like point or rear guard and scan your surroundings,  keeping your weapon ready for action. |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/11` | 0.500059 | You attack and maneuver with tactical precision, whether you're lining up the  perfect headshot from a distance, dueling hand-to-hand, or trading shots at close  range. At higher levels, you master yo |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/23` | 0.497929 | You specialize in hand-to-hand combat and prefer to fight  with your fists or lightweight melee weapons, rather than  guns. Whether you're a daredevil who lives for the thrill, a  martial artist who l |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/13` | 0.493950 | You're a local legend who's known for your prowess with  weaponry. Your proficiency rank increases to legendary  with simple and martial guns, and to master with advanced  guns. Your proficiency rank |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/40` | 0.489964 | **Prerequisites** Tactical Advance |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/23` | 0.480463 | You are a highly skilled sharpshooter and never go anywhere  without your gun. Your proficiency rank increases to master  with simple and martial guns, and increases to expert with  advanced guns. You |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/21` | 0.472440 | You've learned to defend yourself with only a gun, shielding  your body and deflecting blows with stock and barrel. Guns  you wield gain the parry trait. If an appropriate weapon  already has the parr |

### Query 16
- Text: Summarize YOU MIGHT...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/21', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/17', 'PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/18` | 0.903204 | YOU MIGHT... |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/21` | 0.522471 | OTHERS PROBABLY... |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/16` | 0.362798 | IN DOWNTIME... |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/14` | 0.315404 | WHILE EXPLORING... |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/49` | 0.304206 | **Requirements** You have a mark. |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/10` | 0.303473 | DURING COMBAT ENCOUNTERS... |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/55` | 0.284240 | **Requirements** You aren't encumbered. |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/8` | 0.279989 | **8 + Constitution modifier** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/27` | 0.278505 | **OPPORTUNE RETORT **[reaction] **FEAT 10** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/1` | 0.278501 | **KEY TERMS** |

### Query 17
- Text: Summarize Have trained with a military organization or mercenary group that you remain  allied with or have defected from.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/19', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/13', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/19', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/19` | 1.032939 | Have trained with a military organization or mercenary group that you remain  allied with or have defected from. |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/13` | 0.577889 | You might fall back on your training, speaking up to give strategic advice to your  allies while remaining alert for strangers' hidden agendas or take the lead about a  subject you know. |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/17` | 0.538492 | You train with your weapons, acquire and upgrade equipment, and practice tactical  drills for future engagements. |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/23` | 0.466036 | Want to hire you as a bodyguard or mercenary. |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/18` | 0.447917 | You specialize in slipping into a location, completing an  objective, and extricating yourself without being discovered.  You might use stealth tactics, cover identities, disguises, or  spy tech. Whet |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/57` | 0.445949 | Expert in simple guns Expert in martial guns Trained in advanced guns Trained in simple weapons Trained in martial weapons Trained in unarmed attacks |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/59` | 0.427734 | Trained in light armor Trained in unarmored defense |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/2` | 0.425934 | You're a focused, quick-witted professional who thrives in high-stakes combat. Your deadly aim and  tactical training give you an edge over the competition—for you, even the most powerful enemy is jus |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/47` | 0.425333 | You're rarely still, and you've learned to reliably hit your  targets even while moving. You Stride and then Aim with a  gun you're wielding. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/11` | 0.409007 | You've learned how to dodge while wearing light or no  armor. Your proficiency ranks for light armor and unarmored  defense increase to expert. |

### Query 18
- Text: Summarize Work as a gun for hire to the highest bidder, taking any job for enough credits.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/20', 'PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/23', 'PZO22001 Starfinder Player Core 126-137::/page/5/Text/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/20', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/21', 'PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/20` | 1.030840 | Work as a gun for hire to the highest bidder, taking any job for enough credits. |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/23` | 0.553649 | Want to hire you as a bodyguard or mercenary. |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/23` | 0.526609 | Your reputation as a shooter precedes you wherever you go  in the galaxy. Your proficiency rank increases to legendary  with advanced guns. Your proficiency rank for your  operative class DC increases |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/23` | 0.484154 | You are a highly skilled sharpshooter and never go anywhere  without your gun. Your proficiency rank increases to master  with simple and martial guns, and increases to expert with  advanced guns. You |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/2` | 0.481946 | You're a focused, quick-witted professional who thrives in high-stakes combat. Your deadly aim and  tactical training give you an edge over the competition—for you, even the most powerful enemy is jus |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/22` | 0.466229 | Your extensive training has transformed you into a living  weapon, ready to pull the trigger at a moment's notice. At the  start of each enemy's turn, you gain an additional reaction  during that turn |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/19` | 0.465301 | You specialize in targeting foes from far away and attacking  while unseen. Whether you're peeking around a corner,  perching on a distant rooftop, or aiming from the back line  of a squad formation, |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/23` | 0.462491 | You specialize in hand-to-hand combat and prefer to fight  with your fists or lightweight melee weapons, rather than  guns. Whether you're a daredevil who lives for the thrill, a  martial artist who l |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/18` | 0.461983 | **Requirements** You're wielding a gun. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/11` | 0.461983 | **Requirements** You're wielding a gun. |

### Query 19
- Text: Summarize OTHERS PROBABLY...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/21', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/21', 'PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/20', 'PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/21` | 0.892334 | OTHERS PROBABLY... |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/18` | 0.536970 | YOU MIGHT... |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/14` | 0.348763 | WHILE EXPLORING... |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/58` | 0.304825 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/29` | 0.304825 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/30` | 0.304825 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/12` | 0.280939 | DURING SOCIAL ENCOUNTERS... |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/10` | 0.274839 | DURING COMBAT ENCOUNTERS... |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/29` | 0.260114 | **INTRODUCTION** **ANCESTRIES & ** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/33` | 0.260114 | **INTRODUCTION** **ANCESTRIES & ** |

### Query 20
- Text: Summarize Rely on you for strategic advice and firepower in a fight but feel put off by your  talent for methodical violence.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/22', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/2', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/22', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/21', 'PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/22` | 1.029687 | Rely on you for strategic advice and firepower in a fight but feel put off by your  talent for methodical violence. |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/2` | 0.640087 | You're a focused, quick-witted professional who thrives in high-stakes combat. Your deadly aim and  tactical training give you an edge over the competition—for you, even the most powerful enemy is jus |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/13` | 0.617953 | You might fall back on your training, speaking up to give strategic advice to your  allies while remaining alert for strangers' hidden agendas or take the lead about a  subject you know. |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/23` | 0.544331 | You specialize in hand-to-hand combat and prefer to fight  with your fists or lightweight melee weapons, rather than  guns. Whether you're a daredevil who lives for the thrill, a  martial artist who l |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/11` | 0.499033 | You attack and maneuver with tactical precision, whether you're lining up the  perfect headshot from a distance, dueling hand-to-hand, or trading shots at close  range. At higher levels, you master yo |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/30` | 0.498136 | You're able to move deftly around your foes, getting out of  tricky situations or managing to put yourself into a place  where you hold the advantage. You Step up to twice directly  toward the trigger |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/22` | 0.491406 | Your extensive training has transformed you into a living  weapon, ready to pull the trigger at a moment's notice. At the  start of each enemy's turn, you gain an additional reaction  during that turn |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/21` | 0.491270 | You dash across the battlefield, tearing up your surroundings  and toppling nearby objects as you go to make it harder  for your foes to maneuver or to give chase. Stride up to  your Speed. The square |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/8/Text/5` | 0.476509 | Make Dexterity highest, followed by Constitution and  Intelligence if you want more skills or Strength if you  plan to fight in melee. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/47` | 0.462810 | You're rarely still, and you've learned to reliably hit your  targets even while moving. You Stride and then Aim with a  gun you're wielding. |

### Query 21
- Text: Summarize Want to hire you as a bodyguard or mercenary.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/23', 'PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/20', 'PZO22001 Starfinder Player Core 126-137::/page/3/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/23', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/24', 'PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/23` | 1.020781 | Want to hire you as a bodyguard or mercenary. |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/20` | 0.587031 | Work as a gun for hire to the highest bidder, taking any job for enough credits. |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/14` | 0.543110 | You specialize in close-quarters missions that require you to  operate in crowded or tight spaces, such as inside buildings  or vehicles, down narrow alleys, or in busy downtown streets.  Whether you' |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/19` | 0.491480 | Have trained with a military organization or mercenary group that you remain  allied with or have defected from. |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/23` | 0.466001 | You specialize in hand-to-hand combat and prefer to fight  with your fists or lightweight melee weapons, rather than  guns. Whether you're a daredevil who lives for the thrill, a  martial artist who l |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/53` | 0.441966 | **Requirements** You're aware of the attack, wielding a gun, and  not off-guard. |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/18` | 0.441486 | You specialize in slipping into a location, completing an  objective, and extricating yourself without being discovered.  You might use stealth tactics, cover identities, disguises, or  spy tech. Whet |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/15` | 0.423603 | You take a tactical position like point or rear guard and scan your surroundings,  keeping your weapon ready for action. |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/22` | 0.420679 | Rely on you for strategic advice and firepower in a fight but feel put off by your  talent for methodical violence. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/8/Text/46` | 0.419744 | **Requirements** You're wielding a gun and a melee weapon. |

### Query 22
- Text: What is the rule about CLASS FEATURES?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/24', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/387', 'PZO22001 Starfinder Player Core 126-137::/page/6/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/24', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/25', 'PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/24` | 0.841653 | CLASS FEATURES |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/387` | 0.758361 | Class Features |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/2` | 0.544408 | You'll see the following key terms in many operative  class features. |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/63` | 0.495843 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/31` | 0.495843 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/34` | 0.495843 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/59` | 0.495843 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/30` | 0.495843 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/30` | 0.495843 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/4` | 0.440561 | **Attributes** |

### Query 23
- Text: What is the rule about You gain these abilities as an operative. Abilities gained at higher levels list the level  at which you gain them next to the features' names.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/25', 'PZO22001 Starfinder Player Core 126-137::/page/4/Text/19', 'PZO22001 Starfinder Player Core 126-137::/page/6/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/25', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/24', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/25` | 0.975219 | You gain these abilities as an operative. Abilities gained at higher levels list the level  at which you gain them next to the features' names. |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/19` | 0.717872 | At 3rd level, 7th level, and 15th level, you gain a skill feat.  This feat must be for the trained skill from your operative's  specialization. |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/2` | 0.644484 | You'll see the following key terms in many operative  class features. |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/6` | 0.594712 | At 1st level and every even-numbered level, you gain an  operative class feat. These begin on page 131. |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/Table/2` | 0.592405 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, sharpshooter, Aim 1d4, operative's specialization, operative feat2Operative feat, skill feat3Focused, general |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/10` | 0.591025 | At 2nd level and every 2 levels thereafter, you gain a skill  feat. You must be trained or better in the corresponding skill  to select a skill feat. |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407` | 0.588338 | Attribute boosts, operative feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/427` | 0.588338 | Attribute boosts, operative feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/16` | 0.565910 | As an operative, you have a particular set of skills based  on your tactical style. These different specializations  help define your character and the approach you take to  most situations. Choose an |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/16` | 0.565021 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you're untrained in or to become an expert in one  skill in whi |

### Query 24
- Text: What is the rule about ANCESTRY AND BACKGROUND?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/26', 'PZO22001 Starfinder Player Core 126-137::/page/11/Text/29', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/30']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/26', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/27', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/25']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/26` | 0.928306 | ANCESTRY AND BACKGROUND |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/29` | 0.739658 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/30` | 0.739658 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/58` | 0.709658 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/33` | 0.492053 | **INTRODUCTION** **ANCESTRIES & ** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/62` | 0.492053 | **INTRODUCTION** **ANCESTRIES & ** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/29` | 0.492053 | **INTRODUCTION** **ANCESTRIES & ** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/44` | 0.449777 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/80` | 0.449777 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/50` | 0.449777 | **BACKGROUNDS** |

### Query 25
- Text: What is the rule about In addition to what you get from your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/27', 'PZO22001 Starfinder Player Core 126-137::/page/2/Text/7', 'PZO22001 Starfinder Player Core 126-137::/page/4/Text/21']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/27', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/26', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/27` | 0.963223 | In addition to what you get from your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/7` | 0.598690 | At 1st level, you gain a number of proficiencies that  represent your basic training. These proficiencies are noted  at the start of this class. |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/21` | 0.596668 | In addition to the initial ancestry feat you started with, you  gain an ancestry feat at 5th level and every 4 levels thereafter. |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/6` | 0.532928 | At 1st level, your class gives you  an attribute boost to Dexterity |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/4` | 0.530786 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/49` | 0.494730 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/10` | 0.470308 | At 2nd level and every 2 levels thereafter, you gain a skill  feat. You must be trained or better in the corresponding skill  to select a skill feat. |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/25` | 0.467259 | You gain these abilities as an operative. Abilities gained at higher levels list the level  at which you gain them next to the features' names. |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/389` | 0.462066 | Ancestry and background, attribute boosts, initial proficiencies, sharpshooter, Aim 1d4, operative's specialization, operative feat |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/2/Table/2` | 0.453320 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, sharpshooter, Aim 1d4, operative's specialization, operative feat2Operative feat, skill feat3Focused, general |

### Query 26
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/29', 'PZO22001 Starfinder Player Core 126-137::/page/11/Text/28', 'PZO22001 Starfinder Player Core 126-137::/page/5/Text/57']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/29', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/30', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/29` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/28` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/57` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/50` | 0.569679 | **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/44` | 0.569679 | **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/80` | 0.569679 | **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/77` | 0.524467 | **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/33` | 0.495539 | **INTRODUCTION** **ANCESTRIES & ** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/62` | 0.495539 | **INTRODUCTION** **ANCESTRIES & ** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/29` | 0.495539 | **INTRODUCTION** **ANCESTRIES & ** |

### Query 27
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/30']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/5/Text/58', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/30', 'PZO22001 Starfinder Player Core 126-137::/page/11/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/30', 'PZO22001 Starfinder Player Core 126-137::/page/11/Text/29', 'PZO22001 Starfinder Player Core 126-137::/page/5/Text/58', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/31', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/11/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/5/Text/58` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/58` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/30` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/29` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/26` | 0.726682 | ANCESTRY AND BACKGROUND |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/33` | 0.672101 | **INTRODUCTION** **ANCESTRIES & ** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/29` | 0.672101 | **INTRODUCTION** **ANCESTRIES & ** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/62` | 0.672101 | **INTRODUCTION** **ANCESTRIES & ** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/44` | 0.594354 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/80` | 0.594354 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/50` | 0.594354 | **BACKGROUNDS** |

### Query 28
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/31', 'PZO22001 Starfinder Player Core 126-137::/page/5/Text/59', 'PZO22001 Starfinder Player Core 126-137::/page/3/Text/34']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/31', 'PZO22001 Starfinder Player Core 126-137::/page/5/Text/59', 'PZO22001 Starfinder Player Core 126-137::/page/11/Text/30', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/32', 'PZO22001 Starfinder Player Core 126-137::/page/7/Text/30', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/63', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/30', 'PZO22001 Starfinder Player Core 126-137::/page/3/Text/34']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/5/Text/59` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/11/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/7/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/9/Text/63` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/3/Text/34` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/31` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/59` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/34` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/63` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/30` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/30` | 0.910061 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/24` | 0.573477 | CLASS FEATURES |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/60` | 0.515930 | **CLASS DC** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/387` | 0.498036 | Class Features |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/6` | 0.476046 | **Skills** |

### Query 29
- Text: Summarize **Envoy**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/32', 'PZO22001 Starfinder Player Core 126-137::/page/3/Text/35', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/64']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/32', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/33', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/31']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/32` | 0.951326 | **Envoy** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/35` | 0.951326 | **Envoy** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/64` | 0.951326 | **Envoy** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/60` | 0.909326 | **Envoy** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/31` | 0.909326 | **Envoy** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/31` | 0.671113 | **Envoy** **Mystic** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/77` | 0.382028 | **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/55` | 0.380728 | **Requirements** You aren't encumbered. |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/34` | 0.364330 | **Soldier** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/63` | 0.364330 | **Soldier** |

### Query 30
- Text: Summarize **Mystic**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/33']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/3/Text/36', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/33', 'PZO22001 Starfinder Player Core 126-137::/page/11/Text/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/33', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/34', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/32']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/32` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/36` | 0.959378 | **Mystic** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/33` | 0.959378 | **Mystic** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/31` | 0.802776 | **Envoy** **Mystic** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/61` | 0.728194 | **Mystic** **Operative ** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/65` | 0.728194 | **Mystic** **Operative ** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/32` | 0.728194 | **Mystic** **Operative ** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/17` | 0.339603 | Ghost |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/1` | 0.339324 | **KEY TERMS** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/5` | 0.327795 | **Dexterity** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/10` | 0.326924 | **Feats** |

### Query 31
- Text: Summarize **Operative **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/34', 'PZO22001 Starfinder Player Core 126-137::/page/11/Text/32', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/34', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/33', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/35']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/35` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/34` | 0.958402 | **Operative ** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/32` | 0.958402 | **Operative ** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/1` | 0.830647 | OPERATIVE |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/59` | 0.748621 | **OPERATIVE** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/41` | 0.748621 | **OPERATIVE** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/44` | 0.748621 | **OPERATIVE** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/20` | 0.748621 | **OPERATIVE** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/38` | 0.748621 | **OPERATIVE** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/29` | 0.748621 | **OPERATIVE** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/33` | 0.748621 | **OPERATIVE** |

### Query 32
- Text: Summarize **Solarian**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/35', 'PZO22001 Starfinder Player Core 126-137::/page/7/Text/33', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/66']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/35', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/34', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/36']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/36` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/35` | 0.974700 | **Solarian** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/33` | 0.974700 | **Solarian** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/66` | 0.974700 | **Solarian** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/62` | 0.932700 | **Solarian** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/37` | 0.828195 | **Operative ** **Solarian** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/33` | 0.787602 | **Solarian** **Soldier** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/36` | 0.471086 | **Soldier** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/34` | 0.471086 | **Soldier** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/67` | 0.471086 | **Soldier** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/63` | 0.459086 | **Soldier** |

### Query 33
- Text: Summarize **Soldier**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/36']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/3/Text/38', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/67', 'PZO22001 Starfinder Player Core 126-137::/page/7/Text/34']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/36', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/35', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/38']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/35` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/38` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/38` | 0.953061 | **Soldier** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/67` | 0.953061 | **Soldier** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/34` | 0.953061 | **Soldier** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/63` | 0.911061 | **Soldier** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/36` | 0.911061 | **Soldier** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/33` | 0.771063 | **Solarian** **Soldier** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/37` | 0.468437 | **Operative ** **Solarian** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/6` | 0.463308 | **Skills** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/66` | 0.454361 | **Solarian** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/33` | 0.454361 | **Solarian** |

### Query 34
- Text: Summarize **Witchwarper**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/38']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/38', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/68', 'PZO22001 Starfinder Player Core 126-137::/page/3/Text/39']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/38', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/39', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/36']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/39` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/36` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/38` | 0.988715 | **Witchwarper** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/68` | 0.988715 | **Witchwarper** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/39` | 0.988715 | **Witchwarper** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/64` | 0.946715 | **Witchwarper** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/34` | 0.946715 | **Witchwarper** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/35` | 0.808939 | **Witchwarper** **Archetypes** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/2` | 0.369244 | **SNIPER** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/36` | 0.348805 | **SWIFT REPOSITION **[reaction] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/6` | 0.345863 | **Skills** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/38` | 0.342425 | **Soldier** |

### Query 35
- Text: Summarize **Archetypes**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/39']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/11/Text/35', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/39', 'PZO22001 Starfinder Player Core 126-137::/page/5/Text/65']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/39', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/40', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/38']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/38` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/35` | 0.973323 | **Archetypes** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/39` | 0.973323 | **Archetypes** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/65` | 0.973323 | **Archetypes** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/40` | 0.931323 | **Archetypes** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/69` | 0.931323 | **Archetypes** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/35` | 0.668054 | **Witchwarper** **Archetypes** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/4` | 0.431887 | **Attributes** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/77` | 0.382400 | **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/6` | 0.378068 | **Skills** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/29` | 0.376744 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 36
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/40']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/40', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/54', 'PZO22001 Starfinder Player Core 126-137::/page/3/Text/41']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/40', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/39', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/41']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/39` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/41` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/40` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/54` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/41` | 0.864442 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/70` | 0.822442 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/66` | 0.651094 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/36` | 0.651094 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/6` | 0.640740 | **Skills** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/55` | 0.456084 | Trained in one skill determined by  your specialization Trained in a number of additional  skills equal to 3 plus your Intelligence  modifier |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/10` | 0.446689 | At 2nd level and every 2 levels thereafter, you gain a skill  feat. You must be trained or better in the corresponding skill  to select a skill feat. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/16` | 0.430635 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you're untrained in or to become an expert in one  skill in whi |

### Query 37
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/41', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/71', 'PZO22001 Starfinder Player Core 126-137::/page/11/Text/36']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/41', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/40', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/42']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/42` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/41` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/71` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/36` | 0.871817 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/42` | 0.829817 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/36` | 0.653037 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/66` | 0.653037 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/545` | 0.619086 | Feat |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/605` | 0.619086 | Feat |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/4/SectionHeader/5` | 0.537568 | OPERATIVE FEATS |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/28` | 0.537568 | OPERATIVE FEATS |

### Query 38
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/42']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/11/Text/37', 'PZO22001 Starfinder Player Core 126-137::/page/7/Text/37', 'PZO22001 Starfinder Player Core 126-137::/page/5/Text/67']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/42', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/43', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/41']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/43` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/41` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/37` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/37` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/67` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/42` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/43` | 0.902726 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/72` | 0.902726 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/77` | 0.421643 | **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/80` | 0.409329 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/44` | 0.409329 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/50` | 0.409329 | **BACKGROUNDS** |

### Query 39
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/43']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/11/Text/38', 'PZO22001 Starfinder Player Core 126-137::/page/7/Text/38', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/73']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/43', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/44', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/42']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/44` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/42` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/38` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/38` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/73` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/43` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/44` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/68` | 0.847304 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/41` | 0.388254 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/70` | 0.388254 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/54` | 0.388254 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/40` | 0.388254 | **SKILLS** |

### Query 40
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/44', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/74', 'PZO22001 Starfinder Player Core 126-137::/page/11/Text/39']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/44', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/43', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/45']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/43` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/45` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/44` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/74` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/39` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/69` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/45` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/39` | 0.923000 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/29` | 0.418586 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/28` | 0.418586 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/57` | 0.418586 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/43` | 0.414297 | **OPENING VOLLEY **[one-action] **FEAT 8** |

### Query 41
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/45']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/11/Text/40', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/45', 'PZO22001 Starfinder Player Core 126-137::/page/7/Text/40']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/45', 'PZO22001 Starfinder Player Core 126-137::/page/11/Text/40', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/75', 'PZO22001 Starfinder Player Core 126-137::/page/7/Text/40', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/44', 'PZO22001 Starfinder Player Core 126-137::/page/5/Text/70', 'PZO22001 Starfinder Player Core 126-137::/page/3/Text/46', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/46']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/11/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/9/Text/75` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/7/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/44` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/5/Text/70` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/3/Text/46` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/46` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/40` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/45` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/40` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/46` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/70` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/75` | 0.645203 | **CONDITIONS ** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/76` | 0.573689 | **APPENDIX** **GLOSSARY & ** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/4` | 0.463693 | **Attributes** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/1` | 0.439047 | **KEY TERMS** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/77` | 0.423722 | **INDEX** |

### Query 42
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/46']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/11/Text/41', 'PZO22001 Starfinder Player Core 126-137::/page/7/Text/41', 'PZO22001 Starfinder Player Core 126-137::/page/5/Text/71']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/46', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/45', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/47']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/45` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/47` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/41` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/41` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/71` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/46` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/47` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/76` | 0.697531 | **APPENDIX** **GLOSSARY & ** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/77` | 0.618357 | **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/31` | 0.385404 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/59` | 0.385404 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/30` | 0.385404 | **CLASSES** |

### Query 43
- Text: What is the rule about **CHARACTER ** **SHEET**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/47']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/47', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/69', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/39']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/47', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/48', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/46']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/48` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/46` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/47` | 0.859300 | **CHARACTER ** **SHEET** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/69` | 0.434353 | **Archetypes** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/39` | 0.434353 | **Archetypes** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/40` | 0.392353 | **Archetypes** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/65` | 0.392353 | **Archetypes** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/35` | 0.392353 | **Archetypes** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/8` | 0.380071 | **KILL SHOT **[two-actions]** OR **[three-actions] **FEAT 18** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/75` | 0.378942 | **CONDITIONS ** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/50` | 0.376948 | **HAMPERING SHOT **[two-actions] **FEAT 4** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/48` | 0.375015 | **SCOPE SIGHT** **FEAT 1** |

### Query 44
- Text: Summarize **INITIAL PROFICIENCIES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/48']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/48', 'PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/6', 'PZO22001 Starfinder Player Core 126-137::/page/2/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/48', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/47', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/49']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/49` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/48` | 1.001056 | **INITIAL PROFICIENCIES** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/6` | 0.851001 | INITIAL PROFICIENCIES |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/7` | 0.516203 | At 1st level, you gain a number of proficiencies that  represent your basic training. These proficiencies are noted  at the start of this class. |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/389` | 0.416278 | Ancestry and background, attribute boosts, initial proficiencies, sharpshooter, Aim 1d4, operative's specialization, operative feat |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/36` | 0.415064 | **INSTINCTIVE AIM **[one-action] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/28` | 0.400378 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/57` | 0.400378 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/29` | 0.400378 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/6` | 0.396642 | **Skills** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/49` | 0.376597 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |

### Query 45
- Text: What is the rule about At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/49']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/49', 'PZO22001 Starfinder Player Core 126-137::/page/2/Text/7', 'PZO22001 Starfinder Player Core 126-137::/page/4/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/49', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/50', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/48']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/50` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/48` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/49` | 0.992024 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/7` | 0.706615 | At 1st level, you gain a number of proficiencies that  represent your basic training. These proficiencies are noted  at the start of this class. |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/16` | 0.663364 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you're untrained in or to become an expert in one  skill in whi |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/13` | 0.588220 | You're a local legend who's known for your prowess with  weaponry. Your proficiency rank increases to legendary  with simple and martial guns, and to master with advanced  guns. Your proficiency rank |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/10` | 0.579477 | At 2nd level and every 2 levels thereafter, you gain a skill  feat. You must be trained or better in the corresponding skill  to select a skill feat. |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/11` | 0.531049 | You've learned how to dodge while wearing light or no  armor. Your proficiency ranks for light armor and unarmored  defense increase to expert. |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/19` | 0.524578 | At 3rd level, 7th level, and 15th level, you gain a skill feat.  This feat must be for the trained skill from your operative's  specialization. |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/19` | 0.521420 | You've steeled your mind with resolve. Your proficiency  rank for Will saves increases to master. When you roll a  success on a Will save, you get a critical success instead. |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/17` | 0.508602 | At 7th level, you can use skill increases to become a  master in a skill in which you're already an expert, and at  15th level, you can use them to become legendary in a skill  in which you're already |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/23` | 0.507125 | You are a highly skilled sharpshooter and never go anywhere  without your gun. Your proficiency rank increases to master  with simple and martial guns, and increases to expert with  advanced guns. You |

### Query 46
- Text: Summarize **PERCEPTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/50']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/50', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/51', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/50', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/49', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/51']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/51` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/50` | 0.934058 | **PERCEPTION** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/51` | 0.581413 | Expert in Perception |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/29` | 0.485002 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/28` | 0.443002 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/57` | 0.443002 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/50` | 0.438809 | **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/80` | 0.438809 | **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/44` | 0.438809 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/77` | 0.414769 | **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/27` | 0.395891 | You've developed keen awareness and attention to detail.  Your proficiency rank for Perception increases to master.  In addition, you gain a +2 circumstance bonus to initiative  rolls, making you fast |

### Query 47
- Text: Summarize Expert in Perception
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/51']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/51', 'PZO22001 Starfinder Player Core 126-137::/page/5/Text/25', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/50']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/51', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/52', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/50']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/52` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/50` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/51` | 0.925572 | Expert in Perception |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/25` | 0.536180 | Your eyes are incredibly sharp even without a scope. Your  proficiency rank for Perception increases to legendary. |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/50` | 0.532067 | **PERCEPTION** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/27` | 0.482762 | You've developed keen awareness and attention to detail.  Your proficiency rank for Perception increases to master.  In addition, you gain a +2 circumstance bonus to initiative  rolls, making you fast |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/53` | 0.460649 | Trained in Fortitude Expert in Reflex Expert in Will |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/17` | 0.381573 | You have an intuitive sense that alerts you to danger and  allows you to discern the presence of hidden threats. You  gain a +1 circumstance bonus to Perception checks to find  traps and hidden, undet |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/401` | 0.346731 | General feat, operative's edge, reflex mastery, skill increase, specialized skill set, weapon specialization |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/57` | 0.346076 | Expert in simple guns Expert in martial guns Trained in advanced guns Trained in simple weapons Trained in martial weapons Trained in unarmed attacks |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/5` | 0.343801 | You have a hardy physique. Your proficiency rank for  Fortitude saves increases to expert. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/8` | 0.331970 | OPERATIVE EXPERTISE 11TH |

### Query 48
- Text: What is the rule about **SAVING THROWS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/52']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/52', 'PZO22001 Starfinder Player Core 126-137::/page/6/Text/39', 'PZO22001 Starfinder Player Core 126-137::/page/10/Text/58']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/52', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/53', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/51']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/53` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/51` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/52` | 0.904955 | **SAVING THROWS** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/39` | 0.463954 | **Trigger** You're about to roll a Reflex saving throw, but you  haven't rolled yet. |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/58` | 0.371214 | **Prerequisites** Keep Them in Your Sights |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/3/SectionHeader/5` | 0.317534 | **SABOTAGE **[one-action] |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/5` | 0.314350 | **Flourish:** Actions with this trait are special  techniques that require too much exertion for you to  perform frequently. You can use only one action with  the flourish trait per round. |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/1` | 0.303068 | increases to master. When you roll a success on a Reflex  save, you get a critical success instead. |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/19` | 0.296869 | You've steeled your mind with resolve. Your proficiency  rank for Will saves increases to master. When you roll a  success on a Will save, you get a critical success instead. |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/12` | 0.293783 | **Enhanced Exploit:** You can Sabotage as a free action  whenever you critically hit a tech creature with a melee  or ranged attack, targeting the triggering creature. You  can Sabotage as a reaction |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/10/ListItem/20` | 0.293218 | You take a –1 circumstance penalty to Will saves. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/55` | 0.285906 | **STOP THEM IN THEIR TRACKS **[one-action] **FEAT 4** |

### Query 49
- Text: Summarize Trained in Fortitude Expert in Reflex Expert in Will
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/53']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/53', 'PZO22001 Starfinder Player Core 126-137::/page/5/Text/5', 'PZO22001 Starfinder Player Core 126-137::/page/4/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/53', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/52', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/54']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/52` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/54` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/53` | 1.024915 | Trained in Fortitude Expert in Reflex Expert in Will |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/5` | 0.578916 | You have a hardy physique. Your proficiency rank for  Fortitude saves increases to expert. |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/29` | 0.527828 | You've learned to move quickly to avoid explosions, sentry  turrets, and worse. Your proficiency rank for Reflex saves |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/401` | 0.454929 | General feat, operative's edge, reflex mastery, skill increase, specialized skill set, weapon specialization |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/57` | 0.434042 | Expert in simple guns Expert in martial guns Trained in advanced guns Trained in simple weapons Trained in martial weapons Trained in unarmed attacks |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/51` | 0.432308 | Expert in Perception |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/19` | 0.431487 | You've steeled your mind with resolve. Your proficiency  rank for Will saves increases to master. When you roll a  success on a Will save, you get a critical success instead. |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/55` | 0.428553 | Trained in one skill determined by  your specialization Trained in a number of additional  skills equal to 3 plus your Intelligence  modifier |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/11` | 0.413747 | You've learned how to dodge while wearing light or no  armor. Your proficiency ranks for light armor and unarmored  defense increase to expert. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/561` | 0.412135 | Combat Reflexes |

### Query 50
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/54']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/40', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/54', 'PZO22001 Starfinder Player Core 126-137::/page/3/Text/41']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/54', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/53', 'PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/6', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/55']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/53` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/55` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/40` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/54` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/41` | 0.864442 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/70` | 0.822442 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/66` | 0.651094 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/36` | 0.651094 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/6` | 0.640740 | **Skills** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/55` | 0.456084 | Trained in one skill determined by  your specialization Trained in a number of additional  skills equal to 3 plus your Intelligence  modifier |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/10` | 0.446689 | At 2nd level and every 2 levels thereafter, you gain a skill  feat. You must be trained or better in the corresponding skill  to select a skill feat. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/16` | 0.430635 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you're untrained in or to become an expert in one  skill in whi |

### Query 51
- Text: What is the rule about Trained in one skill determined by  your specialization Trained in a number of additional  skills equal to 3 plus your Intelligence  modifier?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/55']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/55', 'PZO22001 Starfinder Player Core 126-137::/page/4/Text/16', 'PZO22001 Starfinder Player Core 126-137::/page/4/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/55', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/54', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/56']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/54` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/56` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/55` | 0.960041 | Trained in one skill determined by  your specialization Trained in a number of additional  skills equal to 3 plus your Intelligence  modifier |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/16` | 0.641312 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you're untrained in or to become an expert in one  skill in whi |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/19` | 0.588878 | At 3rd level, 7th level, and 15th level, you gain a skill feat.  This feat must be for the trained skill from your operative's  specialization. |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/4/SectionHeader/18` | 0.518991 | SPECIALIZED SKILL SET 3RD |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/10` | 0.506920 | At 2nd level and every 2 levels thereafter, you gain a skill  feat. You must be trained or better in the corresponding skill  to select a skill feat. |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/16` | 0.500675 | As an operative, you have a particular set of skills based  on your tactical style. These different specializations  help define your character and the approach you take to  most situations. Choose an |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/17` | 0.499457 | At 7th level, you can use skill increases to become a  master in a skill in which you're already an expert, and at  15th level, you can use them to become legendary in a skill  in which you're already |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/393` | 0.495862 | Focused, general feat, skill increase, specialized skill set |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/24` | 0.495346 | **Exploit:** You have expert proficiency with one-handed  melee weapons and unarmed attacks with the agile or  finesse traits instead of with martial guns. Whenever you  increase your proficiency with |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/49` | 0.487947 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |

### Query 52
- Text: What is the rule about **ATTACKS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/56']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/56', 'PZO22001 Starfinder Player Core 126-137::/page/8/Text/19', 'PZO22001 Starfinder Player Core 126-137::/page/6/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/56', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/57', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/55']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/57` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/55` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/56` | 0.855189 | **ATTACKS** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/8/Text/19` | 0.511311 | You attempt a ranged Strike against the triggering creature.  This Strike doesn't count toward your multiple attack penalty,  and your multiple attack penalty doesn't apply to this Strike. |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/26` | 0.494865 | You fire two shots at the same target in quick succession.  You Aim and then make two Strikes against your mark.  Apply the multiple attack penalty normally. If both attacks  hit, combine their damage |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/21` | 0.445905 | You unleash a devastating barrage of attacks upon your  mark. Your multiple attack penalty for attacks against your  mark is –3 (–2 with an agile weapon) on your second attack  of the turn instead of |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/8/Text/13` | 0.432137 | instead of attempting an Athletics check. A Disarming Shot  counts as two attacks for your multiple attack penalty,  but the penalty doesn't increase until after you've used  Disarming Shot. |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/56` | 0.425874 | You fire a single trick shot that passes through multiple foes.  Make a ranged Strike with your gun against a target within  your first range increment. Apply this attack against all  creatures in a s |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/10` | 0.420420 | You aim your shots to unbalance your foe, pushing them back  or knocking them over. You Aim and then make a ranged Strike  against your mark. If the Strike hits, the target is knocked back  5 feet. If |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/53` | 0.418420 | **Requirements** You're aware of the attack, wielding a gun, and  not off-guard. |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/27` | 0.415789 | You shoot a spray of bullets at a target. You Aim, make a  ranged Strike against your mark, and subtract three times  your weapon's expend from its magazine. Roll the attack twice,  and use the better |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/7` | 0.405328 | You dance across the battlefield while dispatching enemies  with precision and grace. Stride up to twice. You can make up  to three ranged Strikes during this movement. Each ranged  Strike you make mu |

### Query 53
- Text: What is the rule about Expert in simple guns Expert in martial guns Trained in advanced guns Trained in simple weapons Trained in martial weapons Trained in unarmed attacks?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/57']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/57', 'PZO22001 Starfinder Player Core 126-137::/page/3/Text/24', 'PZO22001 Starfinder Player Core 126-137::/page/5/Text/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/57', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/58', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/56']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/58` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/56` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/57` | 0.916566 | Expert in simple guns Expert in martial guns Trained in advanced guns Trained in simple weapons Trained in martial weapons Trained in unarmed attacks |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/24` | 0.696747 | **Exploit:** You have expert proficiency with one-handed  melee weapons and unarmed attacks with the agile or  finesse traits instead of with martial guns. Whenever you  increase your proficiency with |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/13` | 0.680981 | You're a local legend who's known for your prowess with  weaponry. Your proficiency rank increases to legendary  with simple and martial guns, and to master with advanced  guns. Your proficiency rank |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/23` | 0.617628 | You are a highly skilled sharpshooter and never go anywhere  without your gun. Your proficiency rank increases to master  with simple and martial guns, and increases to expert with  advanced guns. You |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/11` | 0.554812 | You've learned how to dodge while wearing light or no  armor. Your proficiency ranks for light armor and unarmored  defense increase to expert. |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/3` | 0.551870 | You've learned how to inflict greater injuries with the  weapons you know best. You deal 2 additional damage with  weapons and unarmed attacks in which you're an expert.  This damage increases to 3 if |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/17` | 0.542357 | Your damage from weapon specialization increases to 4 with  weapons and unarmed attacks in which you're an expert, 6  if you're a master, and 8 if you're legendary. |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/59` | 0.539290 | Trained in light armor Trained in unarmored defense |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/25` | 0.529653 | In addition, when you Aim, you can Aim with and apply  the benefits to a one-handed melee weapon or unarmed  attack with the agile or finesse trait rather than with a  ranged weapon. Treat any one-han |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/15` | 0.514921 | **Exploit:** You're trained to fight in close combat using pistols.  Your ranged Strikes with one-handed ranged weapons don't  trigger reactions that are triggered by a ranged attack. |

### Query 54
- Text: Summarize **DEFENSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/58']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/58', 'PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/18', 'PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/58', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/57', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/59']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/57` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/59` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/58` | 0.959826 | **DEFENSES** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/18` | 0.541716 | **DEFENSIVE GUNNER** **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/10` | 0.486403 | **Feats** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/14` | 0.438852 | **DANGER AWARENESS** **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/57` | 0.411981 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/29` | 0.411981 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/28` | 0.411981 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/59` | 0.408873 | Trained in light armor Trained in unarmored defense |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/6` | 0.406384 | **Skills** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/17` | 0.404851 | **DESTRUCTIVE DASH **[two-actions] **FEAT 6** |

### Query 55
- Text: Summarize Trained in light armor Trained in unarmored defense
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/59']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/59', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/57', 'PZO22001 Starfinder Player Core 126-137::/page/5/Text/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/59', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/60', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/58']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/60` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/58` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/59` | 1.027001 | Trained in light armor Trained in unarmored defense |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/57` | 0.694225 | Expert in simple guns Expert in martial guns Trained in advanced guns Trained in simple weapons Trained in martial weapons Trained in unarmed attacks |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/11` | 0.691385 | You've learned how to dodge while wearing light or no  armor. Your proficiency ranks for light armor and unarmored  defense increase to expert. |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/27` | 0.606515 | Your skill with light armor improves, increasing your ability  to dodge blows. Your proficiency ranks for light armor and  unarmored defense increase to master. |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/10` | 0.489605 | LIGHT ARMOR EXPERTISE 13TH |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/19` | 0.460725 | You specialize in targeting foes from far away and attacking  while unseen. Whether you're peeking around a corner,  perching on a distant rooftop, or aiming from the back line  of a squad formation, |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/19` | 0.449428 | Have trained with a military organization or mercenary group that you remain  allied with or have defected from. |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/26` | 0.433714 | LIGHT ARMOR MASTERY 19TH |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/17` | 0.429854 | You train with your weapons, acquire and upgrade equipment, and practice tactical  drills for future engagements. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/24` | 0.416678 | **Exploit:** You have expert proficiency with one-handed  melee weapons and unarmed attacks with the agile or  finesse traits instead of with martial guns. Whenever you  increase your proficiency with |

### Query 56
- Text: What is the rule about **CLASS DC**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/60']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/60', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/61', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/60', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/61', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/59']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/61` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/59` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/60` | 0.881905 | **CLASS DC** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/61` | 0.542004 | Trained in operative class DC |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/31` | 0.521525 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/34` | 0.491525 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/63` | 0.491525 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/30` | 0.491525 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/30` | 0.491525 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/59` | 0.491525 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/24` | 0.381301 | CLASS FEATURES |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/9` | 0.360758 | Your techniques are now harder to resist. Your proficiency  rank for your operative class DC increases to expert. |

### Query 57
- Text: What is the rule about Trained in operative class DC?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/61']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/61', 'PZO22001 Starfinder Player Core 126-137::/page/5/Text/9', 'PZO22001 Starfinder Player Core 126-137::/page/6/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/61', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/60', 'PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/60` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/61` | 0.875542 | Trained in operative class DC |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/9` | 0.596886 | Your techniques are now harder to resist. Your proficiency  rank for your operative class DC increases to expert. |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/2` | 0.519287 | You'll see the following key terms in many operative  class features. |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/23` | 0.476516 | Your reputation as a shooter precedes you wherever you go  in the galaxy. Your proficiency rank increases to legendary  with advanced guns. Your proficiency rank for your  operative class DC increases |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/60` | 0.460491 | **CLASS DC** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/6` | 0.450381 | At 1st level and every even-numbered level, you gain an  operative class feat. These begin on page 131. |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/19` | 0.445260 | At 3rd level, 7th level, and 15th level, you gain a skill feat.  This feat must be for the trained skill from your operative's  specialization. |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/57` | 0.413263 | Expert in simple guns Expert in martial guns Trained in advanced guns Trained in simple weapons Trained in martial weapons Trained in unarmed attacks |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/1/ListItem/19` | 0.407739 | Have trained with a military organization or mercenary group that you remain  allied with or have defected from. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/1` | 0.400013 | OPERATIVE |

### Query 58
- Text: Summarize **OPERATIVE ADVANCEMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 126-137::/page/10/Text/41', 'PZO22001 Starfinder Player Core 126-137::/page/10/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/61', 'PZO22001 Starfinder Player Core 126-137::/page/2/Table/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/1/Text/61` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/Table/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/1` | 0.995488 | **OPERATIVE ADVANCEMENT** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/41` | 0.667731 | **OPERATIVE** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/9` | 0.667731 | **OPERATIVE** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/29` | 0.625731 | **OPERATIVE** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/20` | 0.625731 | **OPERATIVE** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/10` | 0.625731 | **OPERATIVE** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/25` | 0.625731 | **OPERATIVE** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/12` | 0.625731 | **OPERATIVE** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/7` | 0.625731 | **OPERATIVE** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/44` | 0.625731 | **OPERATIVE** |

### Query 59
- Text: Lookup values for Your LevelClass Features1Ancestry and background, attribute boosts,
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/Table/2']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/27', 'PZO22001 Starfinder Player Core 126-137::/page/2/Table/2', 'PZO22001 Starfinder Player Core 126-137::/page/2/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/Table/2', 'PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/386']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/386` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/27` | 0.671822 | In addition to what you get from your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/Table/2` | 0.643896 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, sharpshooter, Aim 1d4, operative's specialization, operative feat2Operative feat, skill feat3Focused, general |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/4` | 0.624096 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/5` | 0.545659 | At 5th level and every 5 levels thereafter, you get four  free boosts to different attribute modifiers. If an attribute  modifier is already +4 or higher, it takes two boosts to  increase it; you get |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/387` | 0.528105 | Class Features |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/25` | 0.515129 | You gain these abilities as an operative. Abilities gained at higher levels list the level  at which you gain them next to the features' names. |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/6` | 0.512742 | At 1st level, your class gives you  an attribute boost to Dexterity |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/389` | 0.511797 | Ancestry and background, attribute boosts, initial proficiencies, sharpshooter, Aim 1d4, operative's specialization, operative feat |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/427` | 0.491228 | Attribute boosts, operative feat, skill feat |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407` | 0.491228 | Attribute boosts, operative feat, skill feat |

### Query 60
- Text: Summarize Your Level
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/386']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/386', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/546', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/606']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/386', 'PZO22001 Starfinder Player Core 126-137::/page/2/Table/2', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/387']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/Table/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/387` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/386` | 0.853813 | Your Level |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/546` | 0.729099 | Level |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/606` | 0.729099 | Level |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/13` | 0.549996 | 2ND LEVEL |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/41` | 0.534036 | 4TH LEVEL |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/2` | 0.523376 | 18TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/42` | 0.514596 | 8TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/6` | 0.513306 | 14TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/38` | 0.501266 | 16TH LEVEL |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/11/SectionHeader/18` | 0.497936 | 20TH LEVEL |

### Query 61
- Text: What is the rule about Class Features?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/387']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/387', 'PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/24', 'PZO22001 Starfinder Player Core 126-137::/page/6/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/387', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/386', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/388']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/386` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/388` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/387` | 0.835742 | Class Features |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/24` | 0.700239 | CLASS FEATURES |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/2` | 0.605868 | You'll see the following key terms in many operative  class features. |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/25` | 0.437814 | You gain these abilities as an operative. Abilities gained at higher levels list the level  at which you gain them next to the features' names. |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/Table/2` | 0.427477 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, sharpshooter, Aim 1d4, operative's specialization, operative feat2Operative feat, skill feat3Focused, general |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/4` | 0.414280 | **Attributes** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/6` | 0.408853 | At 1st level and every even-numbered level, you gain an  operative class feat. These begin on page 131. |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/63` | 0.407880 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/30` | 0.407880 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/30` | 0.407880 | **CLASSES** |

### Query 62
- Text: Summarize 1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/388']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/578', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/388', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/598']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/388', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/389', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/387']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/389` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/387` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/578` | 0.669108 | 1 |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/388` | 0.669108 | 1 |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/598` | 0.669108 | 1 |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/648` | 0.627108 | 1 |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/660` | 0.627108 | 1 |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/636` | 0.627108 | 1 |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/616` | 0.627108 | 1 |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/612` | 0.513765 | 2 |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/390` | 0.513765 | 2 |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/628` | 0.513765 | 2 |

### Query 63
- Text: What is the rule about Ancestry and background, attribute boosts,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/389']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/1/Text/27', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/427']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/389', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/390', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/388']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/390` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/388` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/27` | 0.581688 | In addition to what you get from your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407` | 0.565335 | Attribute boosts, operative feat, skill feat |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/427` | 0.565335 | Attribute boosts, operative feat, skill feat |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/389` | 0.512235 | Ancestry and background, attribute boosts, initial proficiencies, sharpshooter, Aim 1d4, operative's specialization, operative feat |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/5` | 0.509477 | At 5th level and every 5 levels thereafter, you get four  free boosts to different attribute modifiers. If an attribute  modifier is already +4 or higher, it takes two boosts to  increase it; you get |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/26` | 0.506753 | ANCESTRY AND BACKGROUND |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/29` | 0.496934 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/58` | 0.496934 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/30` | 0.496934 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/405` | 0.482351 | Ancestry feat, enhanced exploit, operative resilience, skill increase |

### Query 64
- Text: Summarize 2
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/390']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/574', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/564', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/566']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/390', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/389', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/391']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/389` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/391` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/574` | 0.689465 | 2 |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/564` | 0.689465 | 2 |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/566` | 0.689465 | 2 |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/612` | 0.647465 | 2 |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/390` | 0.647465 | 2 |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/644` | 0.647465 | 2 |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/628` | 0.647465 | 2 |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/578` | 0.459336 | 1 |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/598` | 0.459336 | 1 |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/388` | 0.459336 | 1 |

### Query 65
- Text: What is the rule about Operative feat, skill feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/391']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/423', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/391', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/390', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/392']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/390` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/392` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411` | 0.932403 | Operative feat, skill feat |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/423` | 0.932403 | Operative feat, skill feat |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403` | 0.932403 | Operative feat, skill feat |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/391` | 0.890403 | Operative feat, skill feat |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/415` | 0.890403 | Operative feat, skill feat |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/399` | 0.890403 | Operative feat, skill feat |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/395` | 0.890403 | Operative feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407` | 0.742103 | Attribute boosts, operative feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/427` | 0.742103 | Attribute boosts, operative feat, skill feat |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/19` | 0.694313 | At 3rd level, 7th level, and 15th level, you gain a skill feat.  This feat must be for the trained skill from your operative's  specialization. |

### Query 66
- Text: Summarize 3
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/392']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/11/Text/27', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/392', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/390']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/392', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/393', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/391']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/393` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/391` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/27` | 0.731895 | 3 |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/392` | 0.731895 | 3 |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/390` | 0.558533 | 2 |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/564` | 0.516533 | 2 |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/628` | 0.516533 | 2 |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/574` | 0.516533 | 2 |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/644` | 0.516533 | 2 |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/612` | 0.516533 | 2 |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/566` | 0.516533 | 2 |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/4/SectionHeader/13` | 0.487018 | GENERAL FEATS 3RD |

### Query 67
- Text: What is the rule about Focused, general feat, skill increase,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/393']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/393', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/401', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/395']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/393', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/392', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/394']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/392` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/394` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/393` | 0.864663 | Focused, general feat, skill increase, specialized skill set |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/401` | 0.639093 | General feat, operative's edge, reflex mastery, skill increase, specialized skill set, weapon specialization |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/395` | 0.626237 | Operative feat, skill feat |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/399` | 0.584237 | Operative feat, skill feat |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411` | 0.584237 | Operative feat, skill feat |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403` | 0.584237 | Operative feat, skill feat |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/415` | 0.584237 | Operative feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/423` | 0.584237 | Operative feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/391` | 0.584237 | Operative feat, skill feat |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407` | 0.577097 | Attribute boosts, operative feat, skill feat |

### Query 68
- Text: Summarize 4
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/394']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/394', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/642', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/646']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/394', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/395', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/393']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/395` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/393` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/394` | 0.774878 | 4 |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/642` | 0.774878 | 4 |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/646` | 0.774878 | 4 |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/570` | 0.732877 | 4 |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/654` | 0.732877 | 4 |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/592` | 0.732877 | 4 |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/550` | 0.732877 | 4 |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/41` | 0.487593 | 4TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/392` | 0.459139 | 3 |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/27` | 0.459139 | 3 |

### Query 69
- Text: What is the rule about Operative feat, skill feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/395']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/423', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/395', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/396', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/394']
- Expanded expected found: `True`
- Expanded expected rank: `7`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/396` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/394` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411` | 0.932403 | Operative feat, skill feat |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/423` | 0.932403 | Operative feat, skill feat |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403` | 0.932403 | Operative feat, skill feat |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/391` | 0.890403 | Operative feat, skill feat |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/415` | 0.890403 | Operative feat, skill feat |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/399` | 0.890403 | Operative feat, skill feat |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/395` | 0.890403 | Operative feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407` | 0.742103 | Attribute boosts, operative feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/427` | 0.742103 | Attribute boosts, operative feat, skill feat |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/19` | 0.694313 | At 3rd level, 7th level, and 15th level, you gain a skill feat.  This feat must be for the trained skill from your operative's  specialization. |

### Query 70
- Text: Summarize 5
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/396']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/396', 'PZO22001 Starfinder Player Core 126-137::/page/4/SectionHeader/24', 'PZO22001 Starfinder Player Core 126-137::/page/4/SectionHeader/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/396', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/395', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/397']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/395` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/397` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/396` | 0.772788 | 5 |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/4/SectionHeader/24` | 0.521964 | URBAN OPERATOR 5TH |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/4/SectionHeader/20` | 0.521739 | ANCESTRY FEATS 5TH |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/650` | 0.467672 | 6 |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/398` | 0.467672 | 6 |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/608` | 0.467672 | 6 |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/590` | 0.467672 | 6 |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/658` | 0.467672 | 6 |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/638` | 0.467672 | 6 |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/572` | 0.467672 | 6 |

### Query 71
- Text: What is the rule about Aim 2d4, ancestry feat, attribute boosts,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/397']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/397', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/421', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/389']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/397', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/398', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/396']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/398` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/396` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/397` | 0.735637 | Aim 2d4, ancestry feat, attribute boosts, master gunner, skill increase, urban operator |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/421` | 0.642212 | Aim 4d4, ancestry feat, resolve, skill increase, tactical barrage |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/389` | 0.639220 | Ancestry and background, attribute boosts, initial proficiencies, sharpshooter, Aim 1d4, operative's specialization, operative feat |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/427` | 0.590182 | Attribute boosts, operative feat, skill feat |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407` | 0.590182 | Attribute boosts, operative feat, skill feat |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/2/Table/2` | 0.547928 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, sharpshooter, Aim 1d4, operative's specialization, operative feat2Operative feat, skill feat3Focused, general |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/21` | 0.531179 | In addition to the initial ancestry feat you started with, you  gain an ancestry feat at 5th level and every 4 levels thereafter. |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/417` | 0.524061 | Attribute boosts, critical aim, general feat, greater weapon specialization, skill increase, specialized skill set |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/405` | 0.518606 | Ancestry feat, enhanced exploit, operative resilience, skill increase |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/413` | 0.498367 | Ancestry feat, legendary gunner, light armor expertise, skill increase |

### Query 72
- Text: Summarize 6
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/398']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/638', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/650', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/398']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/398', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/397', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/399']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/397` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/399` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/638` | 0.783525 | 6 |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/650` | 0.783525 | 6 |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/398` | 0.783525 | 6 |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/590` | 0.741525 | 6 |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/608` | 0.741525 | 6 |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/658` | 0.741525 | 6 |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/572` | 0.741525 | 6 |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/568` | 0.741525 | 6 |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/16` | 0.508078 | 6TH LEVEL |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/400` | 0.496931 | 7 |

### Query 73
- Text: What is the rule about Operative feat, skill feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/399']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/423', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/399', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/400', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/398']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/400` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/398` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411` | 0.932403 | Operative feat, skill feat |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/423` | 0.932403 | Operative feat, skill feat |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403` | 0.932403 | Operative feat, skill feat |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/391` | 0.890403 | Operative feat, skill feat |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/415` | 0.890403 | Operative feat, skill feat |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/399` | 0.890403 | Operative feat, skill feat |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/395` | 0.890403 | Operative feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407` | 0.742103 | Attribute boosts, operative feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/427` | 0.742103 | Attribute boosts, operative feat, skill feat |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/19` | 0.694313 | At 3rd level, 7th level, and 15th level, you gain a skill feat.  This feat must be for the trained skill from your operative's  specialization. |

### Query 74
- Text: Summarize 7
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/400']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/400', 'PZO22001 Starfinder Player Core 126-137::/page/4/SectionHeader/26', 'PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/400', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/399', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/401']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/399` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/401` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/400` | 0.766039 | 7 |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/4/SectionHeader/26` | 0.601457 | OPERATIVE'S EDGE 7TH |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/2` | 0.585452 | WEAPON SPECIALIZATION 7TH |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/4/SectionHeader/28` | 0.477902 | REFLEX MASTERY 7TH |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/398` | 0.473241 | 6 |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/650` | 0.473241 | 6 |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/608` | 0.473241 | 6 |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/590` | 0.473241 | 6 |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/572` | 0.473241 | 6 |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/568` | 0.473241 | 6 |

### Query 75
- Text: What is the rule about General feat, operative's edge, reflex mastery,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/401']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/401', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/399']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/401', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/400', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/402']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/400` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/402` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/401` | 0.810911 | General feat, operative's edge, reflex mastery, skill increase, specialized skill set, weapon specialization |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403` | 0.684121 | Operative feat, skill feat |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/399` | 0.684121 | Operative feat, skill feat |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/423` | 0.642121 | Operative feat, skill feat |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411` | 0.642121 | Operative feat, skill feat |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/415` | 0.642121 | Operative feat, skill feat |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/395` | 0.642121 | Operative feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/391` | 0.642121 | Operative feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/19` | 0.591849 | At 3rd level, 7th level, and 15th level, you gain a skill feat.  This feat must be for the trained skill from your operative's  specialization. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/29` | 0.591316 | At every level that you gain an operative feat, you can  select one of the following feats. You must satisfy any  prerequisites before selecting the feat. |

### Query 76
- Text: Summarize 8
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/402']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/652', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/626', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/620']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/402', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/401']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/401` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/652` | 0.787704 | 8 |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/620` | 0.787704 | 8 |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/626` | 0.787704 | 8 |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/656` | 0.745704 | 8 |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/402` | 0.745704 | 8 |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/42` | 0.546940 | 8TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/400` | 0.471909 | 7 |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/404` | 0.452855 | 9 |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/658` | 0.445146 | 6 |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/638` | 0.445146 | 6 |

### Query 77
- Text: What is the rule about Operative feat, skill feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/423', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/404', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/402']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/404` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/402` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411` | 0.932403 | Operative feat, skill feat |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/423` | 0.932403 | Operative feat, skill feat |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403` | 0.932403 | Operative feat, skill feat |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/391` | 0.890403 | Operative feat, skill feat |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/415` | 0.890403 | Operative feat, skill feat |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/399` | 0.890403 | Operative feat, skill feat |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/395` | 0.890403 | Operative feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407` | 0.742103 | Attribute boosts, operative feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/427` | 0.742103 | Attribute boosts, operative feat, skill feat |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/19` | 0.694313 | At 3rd level, 7th level, and 15th level, you gain a skill feat.  This feat must be for the trained skill from your operative's  specialization. |

### Query 78
- Text: Summarize 9
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/404']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/404', 'PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/4', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/620']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/404', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/405']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/405` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/404` | 0.770045 | 9 |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/4` | 0.585748 | OPERATIVE RESILIENCE 9TH |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/620` | 0.497491 | 8 |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/652` | 0.455491 | 8 |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/626` | 0.455491 | 8 |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/656` | 0.455491 | 8 |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/402` | 0.455491 | 8 |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/622` | 0.446800 | 10 |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/618` | 0.446800 | 10 |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/594` | 0.446800 | 10 |

### Query 79
- Text: What is the rule about Ancestry feat, enhanced exploit, operative?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/405']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/405', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/427', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/405', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/404', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/406']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/404` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/406` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/405` | 0.805120 | Ancestry feat, enhanced exploit, operative resilience, skill increase |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/427` | 0.658618 | Attribute boosts, operative feat, skill feat |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407` | 0.658618 | Attribute boosts, operative feat, skill feat |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/399` | 0.612104 | Operative feat, skill feat |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/423` | 0.612104 | Operative feat, skill feat |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411` | 0.612104 | Operative feat, skill feat |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/395` | 0.612104 | Operative feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403` | 0.612104 | Operative feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/415` | 0.612104 | Operative feat, skill feat |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/391` | 0.612104 | Operative feat, skill feat |

### Query 80
- Text: Summarize 10
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/406']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/618', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/406', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/640']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/406', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/405']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/405` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/406` | 0.782219 | 10 |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/618` | 0.782219 | 10 |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/640` | 0.782219 | 10 |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/594` | 0.740219 | 10 |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/622` | 0.740219 | 10 |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/630` | 0.740219 | 10 |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/16` | 0.501945 | 10TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/408` | 0.492929 | 11 |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/404` | 0.454273 | 9 |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/32` | 0.415914 | **PRACTICED ESCAPE **[reaction] **FEAT 10** |

### Query 81
- Text: What is the rule about Attribute boosts, operative feat, skill feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/427', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/399']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/406', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/408']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/406` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/408` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407` | 0.914258 | Attribute boosts, operative feat, skill feat |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/427` | 0.914258 | Attribute boosts, operative feat, skill feat |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/399` | 0.754749 | Operative feat, skill feat |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/423` | 0.712749 | Operative feat, skill feat |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403` | 0.712749 | Operative feat, skill feat |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/395` | 0.712749 | Operative feat, skill feat |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411` | 0.712749 | Operative feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/415` | 0.712749 | Operative feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/391` | 0.712749 | Operative feat, skill feat |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/19` | 0.615385 | At 3rd level, 7th level, and 15th level, you gain a skill feat.  This feat must be for the trained skill from your operative's  specialization. |

### Query 82
- Text: Summarize 11
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/408']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/408', 'PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/6', 'PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/408', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/409']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/409` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/408` | 0.764621 | 11 |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/6` | 0.594985 | ON THE MOVE 11TH |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/8` | 0.591035 | OPERATIVE EXPERTISE 11TH |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/576` | 0.493902 | 12 |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/624` | 0.493902 | 12 |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/634` | 0.493902 | 12 |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/614` | 0.493902 | 12 |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/588` | 0.493902 | 12 |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/410` | 0.493902 | 12 |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/622` | 0.479429 | 10 |

### Query 83
- Text: What is the rule about Aim 3d4, general feat, on the move +5 feet,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/409']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/409', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/419', 'PZO22001 Starfinder Player Core 126-137::/page/4/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/409', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/408', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/410']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/408` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/410` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/409` | 0.814433 | Aim 3d4, general feat, on the move +5 feet, operative expertise, skill increase |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/419` | 0.647353 | On the move +10 feet, operative feat, skill feat |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/14` | 0.592592 | At 3rd level and every 4 levels thereafter, you gain a  general feat. |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403` | 0.487647 | Operative feat, skill feat |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/395` | 0.487647 | Operative feat, skill feat |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/423` | 0.487647 | Operative feat, skill feat |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/415` | 0.487647 | Operative feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/391` | 0.487647 | Operative feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/399` | 0.487647 | Operative feat, skill feat |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411` | 0.487647 | Operative feat, skill feat |

### Query 84
- Text: Summarize 12
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/410']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/614', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/624', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/410']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/410', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/409', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/409` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/410` | 0.783359 | 12 |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/624` | 0.783359 | 12 |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/614` | 0.783359 | 12 |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/588` | 0.741359 | 12 |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/576` | 0.741359 | 12 |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/634` | 0.741359 | 12 |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/412` | 0.524768 | 13 |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/41` | 0.516176 | 12TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/408` | 0.515039 | 11 |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/52` | 0.450637 | **LINE 'EM UP **[two-actions] **FEAT 12** |

### Query 85
- Text: What is the rule about Operative feat, skill feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/423', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/412', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/410']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/412` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/410` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411` | 0.932403 | Operative feat, skill feat |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/423` | 0.932403 | Operative feat, skill feat |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403` | 0.932403 | Operative feat, skill feat |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/391` | 0.890403 | Operative feat, skill feat |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/415` | 0.890403 | Operative feat, skill feat |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/399` | 0.890403 | Operative feat, skill feat |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/395` | 0.890403 | Operative feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407` | 0.742103 | Attribute boosts, operative feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/427` | 0.742103 | Attribute boosts, operative feat, skill feat |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/19` | 0.694313 | At 3rd level, 7th level, and 15th level, you gain a skill feat.  This feat must be for the trained skill from your operative's  specialization. |

### Query 86
- Text: Summarize 13
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/412']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/412', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/410', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/614']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/412', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/413', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/413` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/412` | 0.781589 | 13 |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/410` | 0.578297 | 12 |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/614` | 0.578297 | 12 |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/588` | 0.536297 | 12 |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/624` | 0.536297 | 12 |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/576` | 0.536297 | 12 |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/634` | 0.536297 | 12 |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/414` | 0.531543 | 14 |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/584` | 0.531543 | 14 |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/586` | 0.531543 | 14 |

### Query 87
- Text: What is the rule about Ancestry feat, legendary gunner, light armor?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/413']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/413', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/397', 'PZO22001 Starfinder Player Core 126-137::/page/4/Text/21']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/413', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/412', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/414']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/412` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/414` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/413` | 0.844701 | Ancestry feat, legendary gunner, light armor expertise, skill increase |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/397` | 0.591067 | Aim 2d4, ancestry feat, attribute boosts, master gunner, skill increase, urban operator |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/21` | 0.523275 | In addition to the initial ancestry feat you started with, you  gain an ancestry feat at 5th level and every 4 levels thereafter. |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/405` | 0.469932 | Ancestry feat, enhanced exploit, operative resilience, skill increase |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/Table/2` | 0.465411 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, sharpshooter, Aim 1d4, operative's specialization, operative feat2Operative feat, skill feat3Focused, general |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/13` | 0.443758 | You're a local legend who's known for your prowess with  weaponry. Your proficiency rank increases to legendary  with simple and martial guns, and to master with advanced  guns. Your proficiency rank |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/421` | 0.442571 | Aim 4d4, ancestry feat, resolve, skill increase, tactical barrage |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/425` | 0.432347 | Galaxy renowned, general feat, incredible senses, light armor mastery, skill increase |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/12` | 0.429545 | LEGENDARY GUNNER 13TH |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/423` | 0.414689 | Operative feat, skill feat |

### Query 88
- Text: Summarize 14
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/414']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/554', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/548', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/560']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/414', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/413', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/415']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/413` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/415` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/554` | 0.770535 | 14 |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/548` | 0.770535 | 14 |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/560` | 0.770535 | 14 |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/586` | 0.728535 | 14 |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/584` | 0.728535 | 14 |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/414` | 0.728535 | 14 |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/6` | 0.572466 | 14TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/416` | 0.517382 | 15 |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/412` | 0.509591 | 13 |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/558` | 0.467370 | 16 |

### Query 89
- Text: What is the rule about Operative feat, skill feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/415']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/423', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/415', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/416', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/414']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/416` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/414` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411` | 0.932403 | Operative feat, skill feat |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/423` | 0.932403 | Operative feat, skill feat |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403` | 0.932403 | Operative feat, skill feat |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/391` | 0.890403 | Operative feat, skill feat |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/415` | 0.890403 | Operative feat, skill feat |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/399` | 0.890403 | Operative feat, skill feat |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/395` | 0.890403 | Operative feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407` | 0.742103 | Attribute boosts, operative feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/427` | 0.742103 | Attribute boosts, operative feat, skill feat |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/19` | 0.694313 | At 3rd level, 7th level, and 15th level, you gain a skill feat.  This feat must be for the trained skill from your operative's  specialization. |

### Query 90
- Text: What is the rule about Attribute boosts, critical aim, general feat,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/417']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/417', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/427', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/417', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/418', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/416']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/418` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/416` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/417` | 0.760483 | Attribute boosts, critical aim, general feat, greater weapon specialization, skill increase, specialized skill set |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/427` | 0.729912 | Attribute boosts, operative feat, skill feat |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407` | 0.729912 | Attribute boosts, operative feat, skill feat |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/389` | 0.547722 | Ancestry and background, attribute boosts, initial proficiencies, sharpshooter, Aim 1d4, operative's specialization, operative feat |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/393` | 0.537565 | Focused, general feat, skill increase, specialized skill set |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/5` | 0.534783 | At 5th level and every 5 levels thereafter, you get four  free boosts to different attribute modifiers. If an attribute  modifier is already +4 or higher, it takes two boosts to  increase it; you get |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/15` | 0.518222 | The first time in each round when you Aim and successfully  make a ranged Strike against your mark, add your weapon's  critical specialization effect to the attack even if you didn't  score a critical |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/Table/2` | 0.514868 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, sharpshooter, Aim 1d4, operative's specialization, operative feat2Operative feat, skill feat3Focused, general |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/423` | 0.501756 | Operative feat, skill feat |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411` | 0.501756 | Operative feat, skill feat |

### Query 91
- Text: What is the rule about On the move +10 feet, operative feat, skill?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/419']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/419', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/399', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/391']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/419', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/418', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/420']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/418` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/420` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/419` | 0.924471 | On the move +10 feet, operative feat, skill feat |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/399` | 0.689565 | Operative feat, skill feat |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/391` | 0.689565 | Operative feat, skill feat |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/395` | 0.647565 | Operative feat, skill feat |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/415` | 0.647565 | Operative feat, skill feat |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403` | 0.647565 | Operative feat, skill feat |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411` | 0.647565 | Operative feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/423` | 0.647565 | Operative feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/409` | 0.646755 | Aim 3d4, general feat, on the move +5 feet, operative expertise, skill increase |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407` | 0.575952 | Attribute boosts, operative feat, skill feat |

### Query 92
- Text: What is the rule about Aim 4d4, ancestry feat, resolve, skill increase,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/421']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/421', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/397', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/389']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/421', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/422', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/420']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/422` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/420` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/421` | 0.798370 | Aim 4d4, ancestry feat, resolve, skill increase, tactical barrage |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/397` | 0.666987 | Aim 2d4, ancestry feat, attribute boosts, master gunner, skill increase, urban operator |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/389` | 0.631372 | Ancestry and background, attribute boosts, initial proficiencies, sharpshooter, Aim 1d4, operative's specialization, operative feat |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/405` | 0.560778 | Ancestry feat, enhanced exploit, operative resilience, skill increase |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/409` | 0.547498 | Aim 3d4, general feat, on the move +5 feet, operative expertise, skill increase |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/2/Table/2` | 0.539656 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, sharpshooter, Aim 1d4, operative's specialization, operative feat2Operative feat, skill feat3Focused, general |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/21` | 0.536033 | In addition to the initial ancestry feat you started with, you  gain an ancestry feat at 5th level and every 4 levels thereafter. |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/413` | 0.509942 | Ancestry feat, legendary gunner, light armor expertise, skill increase |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/59` | 0.506509 | When you Aim, the benefits apply if your mark is within range  up to your weapon's fourth range increment. Additionally, you |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407` | 0.489395 | Attribute boosts, operative feat, skill feat |

### Query 93
- Text: What is the rule about Operative feat, skill feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/423']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/423', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/423', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/424', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/422']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/424` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/422` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411` | 0.932403 | Operative feat, skill feat |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/423` | 0.932403 | Operative feat, skill feat |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403` | 0.932403 | Operative feat, skill feat |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/391` | 0.890403 | Operative feat, skill feat |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/415` | 0.890403 | Operative feat, skill feat |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/399` | 0.890403 | Operative feat, skill feat |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/395` | 0.890403 | Operative feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407` | 0.742103 | Attribute boosts, operative feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/427` | 0.742103 | Attribute boosts, operative feat, skill feat |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/19` | 0.694313 | At 3rd level, 7th level, and 15th level, you gain a skill feat.  This feat must be for the trained skill from your operative's  specialization. |

### Query 94
- Text: What is the rule about Galaxy renowned, general feat, incredible?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/425']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/425', 'PZO22001 Starfinder Player Core 126-137::/page/5/Text/23', 'PZO22001 Starfinder Player Core 126-137::/page/4/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/425', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/424', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/426']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/424` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/426` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/425` | 0.757588 | Galaxy renowned, general feat, incredible senses, light armor mastery, skill increase |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/23` | 0.486376 | Your reputation as a shooter precedes you wherever you go  in the galaxy. Your proficiency rank increases to legendary  with advanced guns. Your proficiency rank for your  operative class DC increases |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/14` | 0.481682 | At 3rd level and every 4 levels thereafter, you gain a  general feat. |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/391` | 0.434638 | Operative feat, skill feat |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411` | 0.434638 | Operative feat, skill feat |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/423` | 0.434638 | Operative feat, skill feat |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/395` | 0.434638 | Operative feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/399` | 0.434638 | Operative feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403` | 0.434638 | Operative feat, skill feat |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/415` | 0.434638 | Operative feat, skill feat |

### Query 95
- Text: What is the rule about Attribute boosts, operative feat, skill feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/427']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/427', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/399']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/427', 'PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/426', 'PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/3']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/426` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407` | 0.914258 | Attribute boosts, operative feat, skill feat |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/427` | 0.914258 | Attribute boosts, operative feat, skill feat |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/399` | 0.754749 | Operative feat, skill feat |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/423` | 0.712749 | Operative feat, skill feat |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/403` | 0.712749 | Operative feat, skill feat |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/395` | 0.712749 | Operative feat, skill feat |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/411` | 0.712749 | Operative feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/415` | 0.712749 | Operative feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/391` | 0.712749 | Operative feat, skill feat |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/19` | 0.615385 | At 3rd level, 7th level, and 15th level, you gain a skill feat.  This feat must be for the trained skill from your operative's  specialization. |

### Query 96
- Text: What is the rule about In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/Text/4', 'PZO22001 Starfinder Player Core 126-137::/page/2/Text/5', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/Text/4', 'PZO22001 Starfinder Player Core 126-137::/page/2/Text/5', 'PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/Text/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/4` | 0.943824 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/5` | 0.843002 | At 5th level and every 5 levels thereafter, you get four  free boosts to different attribute modifiers. If an attribute  modifier is already +4 or higher, it takes two boosts to  increase it; you get |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/6` | 0.656825 | At 1st level, your class gives you  an attribute boost to Dexterity |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/25` | 0.540393 | You gain these abilities as an operative. Abilities gained at higher levels list the level  at which you gain them next to the features' names. |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/27` | 0.530456 | In addition to what you get from your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/427` | 0.529312 | Attribute boosts, operative feat, skill feat |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407` | 0.529312 | Attribute boosts, operative feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/9` | 0.505161 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/Table/2` | 0.470364 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, sharpshooter, Aim 1d4, operative's specialization, operative feat2Operative feat, skill feat3Focused, general |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/417` | 0.469761 | Attribute boosts, critical aim, general feat, greater weapon specialization, skill increase, specialized skill set |

### Query 97
- Text: What is the rule about At 5th level and every 5 levels thereafter, you get four  free boosts to different attribute modifiers. If an attribute  modifier is already +4 or higher, it takes two boosts to  increase it; you get a partial boost and must boost that  attribute again at a later level to increase it by 1.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/Text/5', 'PZO22001 Starfinder Player Core 126-137::/page/2/Text/4', 'PZO22001 Starfinder Player Core 126-137::/page/1/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/Text/5', 'PZO22001 Starfinder Player Core 126-137::/page/2/Text/4', 'PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/5` | 0.966227 | At 5th level and every 5 levels thereafter, you get four  free boosts to different attribute modifiers. If an attribute  modifier is already +4 or higher, it takes two boosts to  increase it; you get |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/4` | 0.768876 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/9` | 0.601486 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/25` | 0.543680 | You gain these abilities as an operative. Abilities gained at higher levels list the level  at which you gain them next to the features' names. |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/21` | 0.541149 | In addition to the initial ancestry feat you started with, you  gain an ancestry feat at 5th level and every 4 levels thereafter. |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/16` | 0.530004 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you're untrained in or to become an expert in one  skill in whi |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/427` | 0.514526 | Attribute boosts, operative feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/407` | 0.514526 | Attribute boosts, operative feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/7` | 0.508837 | You gain a +5-foot status bonus to your Speed. This increases  to a +10-foot status bonus to your Speed at 16th level. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/4/Text/14` | 0.507553 | At 3rd level and every 4 levels thereafter, you gain a  general feat. |

### Query 98
- Text: What is the rule about You can spot a target's weak points, letting you deal  additional precision damage with most types of ranged  weapons. You gain the Aim action.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/Text/9', 'PZO22001 Starfinder Player Core 126-137::/page/2/Text/13', 'PZO22001 Starfinder Player Core 126-137::/page/10/Text/59']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/Text/9', 'PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/10', 'PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/9` | 0.942400 | You can spot a target's weak points, letting you deal  additional precision damage with most types of ranged  weapons. You gain the Aim action. |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/13` | 0.678955 | You take careful aim at a single creature that you're aware  of, designating it as your mark. Until the end of your turn,  your ranged Strikes against your mark using the required  ranged weapon deal |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/59` | 0.670409 | When you Aim, the benefits apply if your mark is within range  up to your weapon's fourth range increment. Additionally, you |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/15` | 0.627248 | The first time in each round when you Aim and successfully  make a ranged Strike against your mark, add your weapon's  critical specialization effect to the attack even if you didn't  score a critical |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/27` | 0.626195 | You shoot a spray of bullets at a target. You Aim, make a  ranged Strike against your mark, and subtract three times  your weapon's expend from its magazine. Roll the attack twice,  and use the better |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/43` | 0.625861 | You always keep a target marked and in your sights, even if  they move. When you Aim, the benefits apply if your mark  is within your weapon's first or second range increment,  rather than only within |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/3` | 0.624650 | **Aim:** An action used to focus on a target and deal  additional precision damage (page 128). |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/39` | 0.608912 | You draw your gun and take careful aim with the same  motion. You Interact to draw a ranged weapon or Switch  Hands and then Aim with that ranged weapon. |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/26` | 0.604172 | You fire two shots at the same target in quick succession.  You Aim and then make two Strikes against your mark.  Apply the multiple attack penalty normally. If both attacks  hit, combine their damage |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/10` | 0.601901 | You aim your shots to unbalance your foe, pushing them back  or knocking them over. You Aim and then make a ranged Strike  against your mark. If the Strike hits, the target is knocked back  5 feet. If |

### Query 99
- Text: What is the rule about **AIM **[one-action]?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/10', 'PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/44', 'PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/36']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/10', 'PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/11', 'PZO22001 Starfinder Player Core 126-137::/page/2/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/10` | 0.909094 | **AIM **[one-action] |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/44` | 0.719334 | **MOBILE AIM **[one-action] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/36` | 0.717730 | **INSTINCTIVE AIM **[one-action] **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/575` | 0.531600 | Dual Aim |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/595` | 0.521622 | Infinite Aim |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/42` | 0.517136 | **DUAL AIM** **FEAT 12** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/597` | 0.503407 | Instinctive Aim |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/25` | 0.477222 | In addition, when you Aim, you can Aim with and apply  the benefits to a one-handed melee weapon or unarmed  attack with the agile or finesse trait rather than with a  ranged weapon. Treat any one-han |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/14` | 0.475257 | You've practiced smoothly drawing and taking aim with  two weapons. Draw up to two one-handed weapons  and Aim. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/615` | 0.474796 | Mobile Aim |

### Query 100
- Text: What is the rule about **Requirements** You're wielding a ranged weapon that doesn't  have the area trait.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/2/Text/12', 'PZO22001 Starfinder Player Core 126-137::/page/11/Text/6', 'PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/2/Text/12', 'PZO22001 Starfinder Player Core 126-137::/page/2/Text/13', 'PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/2/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/12` | 0.896399 | **Requirements** You're wielding a ranged weapon that doesn't  have the area trait. |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/9` | 0.672062 | **Requirements** You're wielding a gun. |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/6` | 0.672062 | **Requirements** You're wielding a gun. |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/11` | 0.630062 | **Requirements** You're wielding a gun. |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/31` | 0.630062 | **Requirements** You're wielding a gun. |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/11` | 0.630062 | **Requirements** You're wielding a gun. |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/25` | 0.630062 | **Requirements** You're wielding a gun. |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/4` | 0.630062 | **Requirements** You're wielding a gun. |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/53` | 0.630062 | **Requirements** You're wielding a gun. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/11` | 0.630062 | **Requirements** You're wielding a gun. |

### Query 101
- Text: What are the requirements for **ELUSIVE TARGET **[reaction] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/31', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/577', 'PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/31', 'PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/30', 'PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/33']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/33` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/31` | 0.893222 | **ELUSIVE TARGET **[reaction] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/577` | 0.603020 | Elusive Target |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/6` | 0.543339 | **SWITCH TARGET **[free-action] **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/603` | 0.498547 | Requirements You've Aimed at a target. |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/7/Table/4` | 0.498547 | Requirements You've Aimed at a target. |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/36` | 0.463606 | **INSTINCTIVE AIM **[one-action] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/52` | 0.443636 | **TACTICAL ADVANCE **[one-action] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/3/SectionHeader/27` | 0.436952 | **REACTIVE STEP **[reaction] |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/44` | 0.435001 | **MOBILE AIM **[one-action] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/27` | 0.418043 | **KILL STEAL **[reaction] **FEAT 2** |

### Query 102
- Text: What are the requirements for **INSTINCTIVE AIM **[one-action] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/36']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/36', 'PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/44', 'PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/36', 'PZO22001 Starfinder Player Core 126-137::/page/5/Text/35', 'PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/38']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/5/Text/35` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/38` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/36` | 0.924285 | **INSTINCTIVE AIM **[one-action] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/44` | 0.734973 | **MOBILE AIM **[one-action] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/10` | 0.694337 | **AIM **[one-action] |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/597` | 0.601351 | Instinctive Aim |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/52` | 0.560529 | **TACTICAL ADVANCE **[one-action] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/11/SectionHeader/23` | 0.551251 | **INFINITE AIM** **FEAT 20** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/595` | 0.496534 | Infinite Aim |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/33` | 0.488149 | **PEEK **[one-action] **FEAT 2** **OPERATIVE** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/42` | 0.481255 | **DUAL AIM** **FEAT 12** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/11` | 0.481178 | **TWIN DRAW **[one-action] **FEAT 4** |

### Query 103
- Text: What are the requirements for **KEEP THEM IN YOUR SIGHTS** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/40']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/40', 'PZO22001 Starfinder Player Core 126-137::/page/10/Text/58', 'PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/48']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/40', 'PZO22001 Starfinder Player Core 126-137::/page/5/Text/39', 'PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/42']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/5/Text/39` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/42` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/40` | 0.851825 | **KEEP THEM IN YOUR SIGHTS** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/58` | 0.698128 | **Prerequisites** Keep Them in Your Sights |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/48` | 0.604537 | **SCOPE SIGHT** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/55` | 0.499990 | **STOP THEM IN THEIR TRACKS **[one-action] **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/36` | 0.463426 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/66` | 0.463426 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/20` | 0.428450 | **Exploit:** You ignore the unwieldy and volley trait of guns  you wield belonging to the sniper group. You gain one of the  following operative feats as a bonus feat: Keep Them in Your  Sights or Sco |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/8/Text/11` | 0.416600 | Keep Them in Your Sights (1st), Scope Sight (1st),  Devastating Aim (4th), Hair Trigger (6th), Parkour (8th) |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/55` | 0.394388 | **Requirements** You aren't encumbered. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/36` | 0.391205 | **FEATS** |

### Query 104
- Text: What are the requirements for **MOBILE AIM **[one-action] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/44', 'PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/36', 'PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/44', 'PZO22001 Starfinder Player Core 126-137::/page/5/Text/43', 'PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/46']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/5/Text/43` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/46` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/44` | 0.916178 | **MOBILE AIM **[one-action] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/36` | 0.711203 | **INSTINCTIVE AIM **[one-action] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/10` | 0.696453 | **AIM **[one-action] |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/52` | 0.559670 | **TACTICAL ADVANCE **[one-action] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/615` | 0.547190 | Mobile Aim |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/42` | 0.530839 | **DUAL AIM** **FEAT 12** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/25` | 0.493263 | In addition, when you Aim, you can Aim with and apply  the benefits to a one-handed melee weapon or unarmed  attack with the agile or finesse trait rather than with a  ranged weapon. Treat any one-han |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/11/SectionHeader/14` | 0.487409 | **RELENTLESS AIM** **FEAT 18** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/33` | 0.480457 | **PEEK **[one-action] **FEAT 2** **OPERATIVE** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/11/SectionHeader/23` | 0.477296 | **INFINITE AIM** **FEAT 20** |

### Query 105
- Text: What are the requirements for **SCOPE SIGHT** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/48']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/48', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/635', 'PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/40']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/48', 'PZO22001 Starfinder Player Core 126-137::/page/5/Text/47', 'PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/50']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/5/Text/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/50` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/48` | 0.888963 | **SCOPE SIGHT** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/635` | 0.609353 | Scope Sight |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/40` | 0.521854 | **KEEP THEM IN YOUR SIGHTS** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/7` | 0.443590 | **360 NO SCOPE **[two-actions] **FEAT 14** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/58` | 0.426426 | **Prerequisites** Keep Them in Your Sights |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/8/Text/11` | 0.425053 | Keep Them in Your Sights (1st), Scope Sight (1st),  Devastating Aim (4th), Hair Trigger (6th), Parkour (8th) |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/20` | 0.413068 | **Exploit:** You ignore the unwieldy and volley trait of guns  you wield belonging to the sniper group. You gain one of the  following operative feats as a bonus feat: Keep Them in Your  Sights or Sco |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/66` | 0.406204 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/36` | 0.406204 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/547` | 0.390534 | 360 No Scope |

### Query 106
- Text: What are the requirements for **TACTICAL ADVANCE **[one-action] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/52']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/52', 'PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/40', 'PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/52', 'PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/54', 'PZO22001 Starfinder Player Core 126-137::/page/5/Text/51']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/54` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/5/Text/51` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/52` | 0.913652 | **TACTICAL ADVANCE **[one-action] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/40` | 0.731907 | **Prerequisites** Tactical Advance |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/31` | 0.600793 | **TACTICAL SWAP **[one-action] **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/44` | 0.553127 | **MOBILE AIM **[one-action] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/647` | 0.543422 | Tactical Advance |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/36` | 0.517659 | **INSTINCTIVE AIM **[one-action] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/8/Text/41` | 0.490499 | When you use Tactical Advance, you ignore difficult terrain  and greater difficult terrain. |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/22` | 0.488056 | **DOUBLE TAP **[two-actions] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/Table/2` | 0.477045 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, sharpshooter, Aim 1d4, operative's specialization, operative feat2Operative feat, skill feat3Focused, general |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/1` | 0.463325 | **OPERATIVE ADVANCEMENT** |

### Query 107
- Text: What are the requirements for **WEAKENING SHOT **[two-actions] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/6/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/6/Text/8', 'PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/50', 'PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/6/Text/8', 'PZO22001 Starfinder Player Core 126-137::/page/6/Text/7', 'PZO22001 Starfinder Player Core 126-137::/page/6/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/6/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/6/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/8` | 0.886866 | **WEAKENING SHOT **[two-actions] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/50` | 0.644726 | **HAMPERING SHOT **[two-actions] **FEAT 4** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/17` | 0.636562 | **IMPEDING SHOT **[two-actions] **FEAT 10** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/8` | 0.589033 | **KILL SHOT **[two-actions]** OR **[three-actions] **FEAT 18** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/1` | 0.577180 | **RUNNING SHOT **[two-actions] **FEAT 12** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/6` | 0.550794 | **TOPPLING SHOT **[two-actions] **FEAT 8** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/46` | 0.544893 | **GRAZING SHOT **[one-action] **FEAT 12** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/57` | 0.538763 | **OVERWHELMING SHOT **[two-actions] **FEAT 12** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/659` | 0.526608 | Weakening Shot |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/23` | 0.521723 | **DISARMING SHOT **[two-actions] **FEAT 6** |

### Query 108
- Text: What are the requirements for **DANGER AWARENESS** **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/14', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/563', 'PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/14', 'PZO22001 Starfinder Player Core 126-137::/page/6/Text/16', 'PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/6/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/14` | 0.887408 | **DANGER AWARENESS** **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/563` | 0.635779 | Danger Awareness |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/18` | 0.542287 | **DEFENSIVE GUNNER** **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/4/SectionHeader/8` | 0.473093 | SKILL FEATS 2ND |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/53` | 0.448623 | **Requirements** You're aware of the attack, wielding a gun, and  not off-guard. |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/22` | 0.445695 | **DOUBLE TAP **[two-actions] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/66` | 0.436301 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/36` | 0.436301 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/42` | 0.431804 | **DUAL AIM** **FEAT 12** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/52` | 0.425751 | **TACTICAL ADVANCE **[one-action] **FEAT 1** |

### Query 109
- Text: What are the requirements for **DEFENSIVE GUNNER** **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/18', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/565', 'PZO22001 Starfinder Player Core 126-137::/page/11/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/18', 'PZO22001 Starfinder Player Core 126-137::/page/6/Text/20', 'PZO22001 Starfinder Player Core 126-137::/page/6/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/6/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/6/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/18` | 0.880335 | **DEFENSIVE GUNNER** **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/565` | 0.594822 | Defensive Gunner |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/6` | 0.519820 | **Requirements** You're wielding a gun. |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/4` | 0.477820 | **Requirements** You're wielding a gun. |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/55` | 0.477820 | **Requirements** You're wielding a gun. |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/53` | 0.477820 | **Requirements** You're wielding a gun. |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/9` | 0.477820 | **Requirements** You're wielding a gun. |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/31` | 0.477820 | **Requirements** You're wielding a gun. |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/25` | 0.477820 | **Requirements** You're wielding a gun. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/11` | 0.477820 | **Requirements** You're wielding a gun. |

### Query 110
- Text: What are the requirements for **DOUBLE TAP **[two-actions] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/6/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/6/Text/22', 'PZO22001 Starfinder Player Core 126-137::/page/10/Text/42', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/573']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/6/Text/22', 'PZO22001 Starfinder Player Core 126-137::/page/6/Text/21', 'PZO22001 Starfinder Player Core 126-137::/page/6/Text/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/6/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/6/Text/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/22` | 0.919514 | **DOUBLE TAP **[two-actions] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/42` | 0.755238 | **Prerequisites** Double Tap |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/573` | 0.632625 | Double Tap |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/43` | 0.528925 | You squeeze the trigger and release a calculated burst of fire. If  you make your second Strike from Double Tap with the same  gun, Double Tap counts as one attack when calculating your  multiple atta |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/52` | 0.513811 | **TACTICAL ADVANCE **[one-action] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/42` | 0.506878 | **DUAL AIM** **FEAT 12** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/37` | 0.496571 | **SPRINT **[two-actions]** OR **[three-actions] **FEAT 10** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/21` | 0.496534 | **GHOST TAP **[free-action] |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/6` | 0.489262 | **TOPPLING SHOT **[two-actions] **FEAT 8** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/33` | 0.480093 | **PEEK **[one-action] **FEAT 2** **OPERATIVE** |

### Query 111
- Text: What are the requirements for **KILL STEAL **[reaction] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/27', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/611', 'PZO22001 Starfinder Player Core 126-137::/page/11/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/27', 'PZO22001 Starfinder Player Core 126-137::/page/6/Text/26', 'PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/6/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/27` | 0.871750 | **KILL STEAL **[reaction] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/611` | 0.621194 | Kill Steal |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/8` | 0.598235 | **KILL SHOT **[two-actions]** OR **[three-actions] **FEAT 18** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/36` | 0.485330 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/66` | 0.485330 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/14` | 0.471846 | **DANGER AWARENESS** **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/8` | 0.453982 | **WEAKENING SHOT **[two-actions] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/4/SectionHeader/8` | 0.452285 | SKILL FEATS 2ND |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/18` | 0.446868 | **DEFENSIVE GUNNER** **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/53` | 0.444966 | **Requirements** You're aware of the attack, wielding a gun, and  not off-guard. |

### Query 112
- Text: What are the requirements for **PEEK **[one-action] **FEAT 2** **OPERATIVE**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/6/Text/33']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/6/Text/33', 'PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/44', 'PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/6/Text/33', 'PZO22001 Starfinder Player Core 126-137::/page/6/Text/35', 'PZO22001 Starfinder Player Core 126-137::/page/6/Text/32']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/6/Text/35` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/6/Text/32` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/33` | 0.896762 | **PEEK **[one-action] **FEAT 2** **OPERATIVE** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/44` | 0.548739 | **MOBILE AIM **[one-action] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/1` | 0.534201 | **OPERATIVE FEATS BY NAME** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/37` | 0.486693 | **SPRINT **[two-actions]** OR **[three-actions] **FEAT 10** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/52` | 0.486538 | **TACTICAL ADVANCE **[one-action] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/36` | 0.482477 | **INSTINCTIVE AIM **[one-action] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/22` | 0.481924 | **DOUBLE TAP **[two-actions] **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/29` | 0.475907 | **OPERATIVE** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/20` | 0.475907 | **OPERATIVE** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/44` | 0.475907 | **OPERATIVE** |

### Query 113
- Text: What are the requirements for **SWIFT REPOSITION **[reaction] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/36']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/36', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/643', 'PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/36', 'PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/38', 'PZO22001 Starfinder Player Core 126-137::/page/6/Text/35']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/38` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/6/Text/35` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/36` | 0.908755 | **SWIFT REPOSITION **[reaction] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/643` | 0.542000 | Swift Reposition |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/6` | 0.535545 | **SWITCH TARGET **[free-action] **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/31` | 0.447607 | **TACTICAL SWAP **[one-action] **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/3/SectionHeader/27` | 0.442421 | **REACTIVE STEP **[reaction] |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/27` | 0.441463 | **KILL STEAL **[reaction] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/37` | 0.434886 | **SPRINT **[two-actions]** OR **[three-actions] **FEAT 10** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/17` | 0.424788 | **IMPEDING SHOT **[two-actions] **FEAT 10** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/27` | 0.403727 | **OPPORTUNE RETORT **[reaction] **FEAT 10** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/8` | 0.395649 | **KILL SHOT **[two-actions]** OR **[three-actions] **FEAT 18** |

### Query 114
- Text: What are the requirements for **BLOODY WOUNDS** **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/42']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/42', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/549', 'PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/42', 'PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/41', 'PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/44']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/41` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/44` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/42` | 0.867483 | **BLOODY WOUNDS** **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/549` | 0.535044 | Bloody Wounds |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/11` | 0.510378 | **TWIN DRAW **[one-action] **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/66` | 0.413883 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/36` | 0.413883 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/550` | 0.397332 | 4 |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/646` | 0.385332 | 4 |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/642` | 0.385332 | 4 |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/394` | 0.385332 | 4 |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/654` | 0.385332 | 4 |

### Query 115
- Text: What are the requirements for **DEVASTATING AIM** **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/46']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/46', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/569', 'PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/42']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/46', 'PZO22001 Starfinder Player Core 126-137::/page/6/Text/45', 'PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/48']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/6/Text/45` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/48` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/46` | 0.869998 | **DEVASTATING AIM** **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/569` | 0.521882 | Devastating Aim |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/42` | 0.519812 | **DUAL AIM** **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/6` | 0.457914 | **SWITCH TARGET **[free-action] **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/44` | 0.453088 | **MOBILE AIM **[one-action] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/11/SectionHeader/23` | 0.451530 | **INFINITE AIM** **FEAT 20** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/11/SectionHeader/14` | 0.447508 | **RELENTLESS AIM** **FEAT 18** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/11` | 0.445083 | **TWIN DRAW **[one-action] **FEAT 4** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/36` | 0.439285 | **INSTINCTIVE AIM **[one-action] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/603` | 0.428522 | Requirements You've Aimed at a target. |

### Query 116
- Text: What are the requirements for **HAMPERING SHOT **[two-actions] **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/50']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/50', 'PZO22001 Starfinder Player Core 126-137::/page/6/Text/8', 'PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/50', 'PZO22001 Starfinder Player Core 126-137::/page/6/Text/49', 'PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/52']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/6/Text/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/52` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/50` | 0.896239 | **HAMPERING SHOT **[two-actions] **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/8` | 0.629974 | **WEAKENING SHOT **[two-actions] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/17` | 0.618842 | **IMPEDING SHOT **[two-actions] **FEAT 10** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/8` | 0.574922 | **KILL SHOT **[two-actions]** OR **[three-actions] **FEAT 18** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/23` | 0.570062 | **DISARMING SHOT **[two-actions] **FEAT 6** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/6` | 0.567598 | **TOPPLING SHOT **[two-actions] **FEAT 8** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/1` | 0.556858 | **RUNNING SHOT **[two-actions] **FEAT 12** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/591` | 0.546783 | Hampering Shot |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/46` | 0.540160 | **GRAZING SHOT **[one-action] **FEAT 12** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/57` | 0.530166 | **OVERWHELMING SHOT **[two-actions] **FEAT 12** |

### Query 117
- Text: What are the requirements for **STOP THEM IN THEIR TRACKS **[one-action] **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/55']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/55', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/641', 'PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/55', 'PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/57', 'PZO22001 Starfinder Player Core 126-137::/page/6/Text/54']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/57` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/6/Text/54` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/55` | 0.905689 | **STOP THEM IN THEIR TRACKS **[one-action] **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/641` | 0.625075 | Stop Them In Their Tracks |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/11` | 0.583879 | **TWIN DRAW **[one-action] **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/6` | 0.504529 | **SWITCH TARGET **[free-action] **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/40` | 0.474110 | **KEEP THEM IN YOUR SIGHTS** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/50` | 0.464939 | **HAMPERING SHOT **[two-actions] **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/36` | 0.447029 | **INSTINCTIVE AIM **[one-action] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/2` | 0.444685 | **PARKOUR **[one-action] **FEAT 8** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/7/Table/15` | 0.444580 | FeatLevelKick it into Overdrive6Kill Shot18Kill Steal2Line 'Em Up12Mobile Aim1Muzzle Flash10Opening Volley8Opportune Retort10Overwhelming Shot12Parkour8Peek2Practiced Escape10Relentless Aim18Running S |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/5` | 0.441037 | With a deadly authority, you order your target to halt  in their tracks, drop their weapons, and surrender. You  attempt to Demoralize your mark. This check doesn't take  the –4 circumstance penalty i |

### Query 118
- Text: What are the requirements for **Prerequisites** trained in Intimidation?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/6/Text/58']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/6/Text/58', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/603', 'PZO22001 Starfinder Player Core 126-137::/page/7/Table/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/6/Text/58', 'PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/57', 'PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/57` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/58` | 0.969563 | **Prerequisites** trained in Intimidation |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/603` | 0.476508 | Requirements You've Aimed at a target. |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/Table/4` | 0.476508 | Requirements You've Aimed at a target. |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/55` | 0.415343 | **Requirements** You aren't encumbered. |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/1/SectionHeader/48` | 0.372592 | **INITIAL PROFICIENCIES** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/58` | 0.371697 | **Prerequisites** Keep Them in Your Sights |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/53` | 0.366434 | **Requirements** You're aware of the attack, wielding a gun, and  not off-guard. |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/6` | 0.365624 | **Skills** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/31` | 0.359025 | **Requirements** You're wielding a gun. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/11` | 0.359025 | **Requirements** You're wielding a gun. |

### Query 119
- Text: Lookup values for FeatLevel360 No Scope14Bloody Wounds4Bullet Dance18Bullet Fever14Burst Fire16Cloaking Field16Clustered Shots14Combat Reflexes20Danger Awareness2Defensive Gunner2Destructive Dash6Devastating Aim4Disarming Shot6Double Tap2Dual Aim12Elusive Target1Explosive Deflection16Extreme Accuracy16Fish in a Barrel14Follow-Up Fire14Grazing Shot12Hair Trigger6Hampering Shot4Impeding Shot10Infinite Aim20Instinctive Aim1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/7/Table/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/7/Table/3', 'PZO22001 Starfinder Player Core 126-137::/page/7/Table/15', 'PZO22001 Starfinder Player Core 126-137::/page/2/Table/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/7/Table/3', 'PZO22001 Starfinder Player Core 126-137::/page/7/Text/2', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/545']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/7/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/545` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/7/Table/3` | 0.997772 | FeatLevel360 No Scope14Bloody Wounds4Bullet Dance18Bullet Fever14Burst Fire16Cloaking Field16Clustered Shots14Combat Reflexes20Danger Awareness2Defensive Gunner2Destructive Dash6Devastating Aim4Disarm |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/Table/15` | 0.760469 | FeatLevelKick it into Overdrive6Kill Shot18Kill Steal2Line 'Em Up12Mobile Aim1Muzzle Flash10Opening Volley8Opportune Retort10Overwhelming Shot12Parkour8Peek2Practiced Escape10Relentless Aim18Running S |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/2/Table/2` | 0.681984 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, sharpshooter, Aim 1d4, operative's specialization, operative feat2Operative feat, skill feat3Focused, general |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/2` | 0.535123 | Use this table to look up operative feats by name. |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/7` | 0.503479 | **360 NO SCOPE **[two-actions] **FEAT 14** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/8/Text/11` | 0.493135 | Keep Them in Your Sights (1st), Scope Sight (1st),  Devastating Aim (4th), Hair Trigger (6th), Parkour (8th) |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/16` | 0.484652 | **Enhanced Exploit:** Your point-blank shots are particularly  deadly. When you make a successful Strike against an  adjacent enemy with a one-handed ranged weapon, you  calculate the damage as if the |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/401` | 0.478838 | General feat, operative's edge, reflex mastery, skill increase, specialized skill set, weapon specialization |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/11` | 0.476910 | You attack and maneuver with tactical precision, whether you're lining up the  perfect headshot from a distance, dueling hand-to-hand, or trading shots at close  range. At higher levels, you master yo |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/20` | 0.475381 | **Exploit:** You ignore the unwieldy and volley trait of guns  you wield belonging to the sniper group. You gain one of the  following operative feats as a bonus feat: Keep Them in Your  Sights or Sco |

### Query 120
- Text: Lookup values for Requirements You've Aimed at a target.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/7/Table/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/7/Table/4', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/603', 'PZO22001 Starfinder Player Core 126-137::/page/7/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/7/Table/4', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/598', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/603']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/598` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/603` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/7/Table/4` | 0.866135 | Requirements You've Aimed at a target. |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/603` | 0.866135 | Requirements You've Aimed at a target. |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/2` | 0.489376 | Use this table to look up operative feats by name. |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/17` | 0.428053 | You take careful aim with your shots so that your bullets  ricochet off solid surfaces. When determining if you have line  of effect to a target you've aimed at, you can choose one solid  surface with |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/9` | 0.427410 | You can spot a target's weak points, letting you deal  additional precision damage with most types of ranged  weapons. You gain the Aim action. |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/10` | 0.422465 | As your target falls, you immediately home in on the next.  You Aim at a different creature. |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/23` | 0.416030 | **Requirements** Your last action this round was a successful  Strike against a target you were hidden from or  undetected by. |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/59` | 0.413417 | When you Aim, the benefits apply if your mark is within range  up to your weapon's fourth range increment. Additionally, you |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/21` | 0.409675 | You hinder your target with a shot. You Aim and then make a  ranged Strike against your mark. If the Strike hits, the target  is slowed 1 until the end of its next turn. If the target is flying,  it a |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/43` | 0.404365 | You always keep a target marked and in your sights, even if  they move. When you Aim, the benefits apply if your mark  is within your weapon's first or second range increment,  rather than only within |

### Query 121
- Text: What are the requirements for **SWITCH TARGET **[free-action] **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/6', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/645', 'PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/55']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/6', 'PZO22001 Starfinder Player Core 126-137::/page/7/Text/5', 'PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/7/Text/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/6` | 0.916569 | **SWITCH TARGET **[free-action] **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/645` | 0.560144 | Switch Target |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/55` | 0.535546 | **STOP THEM IN THEIR TRACKS **[one-action] **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/11` | 0.490014 | **TWIN DRAW **[one-action] **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/31` | 0.482956 | **TACTICAL SWAP **[one-action] **FEAT 6** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/31` | 0.477197 | **ELUSIVE TARGET **[reaction] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/603` | 0.457957 | Requirements You've Aimed at a target. |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/Table/4` | 0.457957 | Requirements You've Aimed at a target. |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/32` | 0.456800 | **FOLLOW-UP FIRE **[free-action] **FEAT 14** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/8/Text/36` | 0.455874 | You swap weapons with a practiced motion. You Switch  Hands or Interact to swap your current weapon for another.  Make a Strike against the required target with your newly  drawn weapon. |

### Query 122
- Text: What are the requirements for **TWIN DRAW **[one-action] **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/11', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/14', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/11', 'PZO22001 Starfinder Player Core 126-137::/page/7/Text/10', 'PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/7/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/11` | 0.886209 | **TWIN DRAW **[one-action] **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/14` | 0.625704 | **Prerequisites** Twin Draw |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/11` | 0.570016 | **TWIN SHOOTER** **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/50` | 0.496325 | **HAMPERING SHOT **[two-actions] **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/55` | 0.493285 | **STOP THEM IN THEIR TRACKS **[one-action] **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/44` | 0.464456 | **MOBILE AIM **[one-action] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/52` | 0.460449 | **TACTICAL ADVANCE **[one-action] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/653` | 0.455825 | Twin Draw |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/46` | 0.454272 | **GRAZING SHOT **[one-action] **FEAT 12** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/22` | 0.452680 | **DOUBLE TAP **[two-actions] **FEAT 2** |

### Query 123
- Text: Lookup values for FeatLevelKick it into Overdrive6Kill Shot18Kill Steal2Line 'Em Up12Mobile Aim1Muzzle Flash10Opening Volley8Opportune Retort10Overwhelming Shot12Parkour8Peek2Practiced Escape10Relentless Aim18Running Shot12Scope Sight1Skirmish Strike6Sprint10Stop Them In Their Tracks4Swift Reposition2Switch Target4Tactical Advance1Tactical Swap6Toppling Shot8Twin Draw4Twin Shooter8Unhindered Advance6Weakening Shot1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/7/Table/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/7/Table/15', 'PZO22001 Starfinder Player Core 126-137::/page/7/Table/3', 'PZO22001 Starfinder Player Core 126-137::/page/2/Table/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/7/Table/15', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/605', 'PZO22001 Starfinder Player Core 126-137::/page/7/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/605` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/7/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/7/Table/15` | 0.981706 | FeatLevelKick it into Overdrive6Kill Shot18Kill Steal2Line 'Em Up12Mobile Aim1Muzzle Flash10Opening Volley8Opportune Retort10Overwhelming Shot12Parkour8Peek2Practiced Escape10Relentless Aim18Running S |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/Table/3` | 0.755910 | FeatLevel360 No Scope14Bloody Wounds4Bullet Dance18Bullet Fever14Burst Fire16Cloaking Field16Clustered Shots14Combat Reflexes20Danger Awareness2Defensive Gunner2Destructive Dash6Devastating Aim4Disarm |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/2/Table/2` | 0.678946 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, sharpshooter, Aim 1d4, operative's specialization, operative feat2Operative feat, skill feat3Focused, general |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/2` | 0.587649 | Use this table to look up operative feats by name. |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/8/Text/11` | 0.496781 | Keep Them in Your Sights (1st), Scope Sight (1st),  Devastating Aim (4th), Hair Trigger (6th), Parkour (8th) |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/16` | 0.475782 | **Enhanced Exploit:** Your point-blank shots are particularly  deadly. When you make a successful Strike against an  adjacent enemy with a one-handed ranged weapon, you  calculate the damage as if the |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/3/Text/20` | 0.474526 | **Exploit:** You ignore the unwieldy and volley trait of guns  you wield belonging to the sniper group. You gain one of the  following operative feats as a bonus feat: Keep Them in Your  Sights or Sco |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/25` | 0.473302 | You gain these abilities as an operative. Abilities gained at higher levels list the level  at which you gain them next to the features' names. |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/11` | 0.472218 | You attack and maneuver with tactical precision, whether you're lining up the  perfect headshot from a distance, dueling hand-to-hand, or trading shots at close  range. At higher levels, you master yo |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/20` | 0.466575 | **KICK IT INTO OVERDRIVE **[free-action] **FEAT 6** |

### Query 124
- Text: What are the requirements for **DESTRUCTIVE DASH **[two-actions] **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/17', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/567', 'PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/17', 'PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/19', 'PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/17` | 0.933816 | **DESTRUCTIVE DASH **[two-actions] **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/567` | 0.686072 | Destructive Dash |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/23` | 0.603310 | **DISARMING SHOT **[two-actions] **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/31` | 0.501082 | **TACTICAL SWAP **[one-action] **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/22` | 0.484347 | **DOUBLE TAP **[two-actions] **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/27` | 0.474628 | **SKIRMISH STRIKE **[one-action] **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/8` | 0.451315 | **KILL SHOT **[two-actions]** OR **[three-actions] **FEAT 18** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/11` | 0.445163 | **TWIN DRAW **[one-action] **FEAT 4** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/37` | 0.439107 | **SPRINT **[two-actions]** OR **[three-actions] **FEAT 10** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/52` | 0.438128 | **TACTICAL ADVANCE **[one-action] **FEAT 1** |

### Query 125
- Text: What are the requirements for **DISARMING SHOT **[two-actions] **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/23', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/571', 'PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/50']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/23', 'PZO22001 Starfinder Player Core 126-137::/page/7/Text/22', 'PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/25']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/7/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/23` | 0.925669 | **DISARMING SHOT **[two-actions] **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/571` | 0.625725 | Disarming Shot |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/50` | 0.624904 | **HAMPERING SHOT **[two-actions] **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/17` | 0.578480 | **IMPEDING SHOT **[two-actions] **FEAT 10** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/8/Text/13` | 0.549497 | instead of attempting an Athletics check. A Disarming Shot  counts as two attacks for your multiple attack penalty,  but the penalty doesn't increase until after you've used  Disarming Shot. |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/57` | 0.537762 | **OVERWHELMING SHOT **[two-actions] **FEAT 12** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/17` | 0.537024 | **DESTRUCTIVE DASH **[two-actions] **FEAT 6** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/31` | 0.536396 | **TACTICAL SWAP **[one-action] **FEAT 6** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/8` | 0.535602 | **KILL SHOT **[two-actions]** OR **[three-actions] **FEAT 18** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/46` | 0.531967 | **GRAZING SHOT **[one-action] **FEAT 12** |

### Query 126
- Text: What are the requirements for **HAIR TRIGGER **[reaction] **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/14', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/589', 'PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/27']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/14', 'PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/16', 'PZO22001 Starfinder Player Core 126-137::/page/8/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/8/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/14` | 0.910695 | **HAIR TRIGGER **[reaction] **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/589` | 0.673716 | Hair Trigger |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/27` | 0.514628 | **SKIRMISH STRIKE **[one-action] **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/23` | 0.440673 | **DISARMING SHOT **[two-actions] **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/20` | 0.435091 | **KICK IT INTO OVERDRIVE **[free-action] **FEAT 6** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/35` | 0.426178 | **Trigger** A creature grabs, immobilizes, or restrains you. |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/8/Text/24` | 0.423292 | **Trigger** Your turn begins. |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/31` | 0.421744 | **ELUSIVE TARGET **[reaction] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/34` | 0.415284 | **Trigger** A Strike targeting you fails. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/31` | 0.415038 | **TACTICAL SWAP **[one-action] **FEAT 6** |

### Query 127
- Text: What are the requirements for **KICK IT INTO OVERDRIVE **[free-action] **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/20', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/607', 'PZO22001 Starfinder Player Core 126-137::/page/7/Table/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/20', 'PZO22001 Starfinder Player Core 126-137::/page/8/Text/19', 'PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/8/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/20` | 0.908326 | **KICK IT INTO OVERDRIVE **[free-action] **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/607` | 0.589197 | Kick it into Overdrive |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/Table/15` | 0.562872 | FeatLevelKick it into Overdrive6Kill Shot18Kill Steal2Line 'Em Up12Mobile Aim1Muzzle Flash10Opening Volley8Opportune Retort10Overwhelming Shot12Parkour8Peek2Practiced Escape10Relentless Aim18Running S |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/31` | 0.480024 | **TACTICAL SWAP **[one-action] **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/6` | 0.473974 | **SWITCH TARGET **[free-action] **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/37` | 0.471672 | **UNHINDERED ADVANCE** **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/4/SectionHeader/1` | 0.470674 | **OVERWHELMING STRIKE **[free-action] |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/23` | 0.462836 | **DISARMING SHOT **[two-actions] **FEAT 6** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/27` | 0.457584 | **SKIRMISH STRIKE **[one-action] **FEAT 6** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/32` | 0.446708 | **FOLLOW-UP FIRE **[free-action] **FEAT 14** |

### Query 128
- Text: What are the requirements for **SKIRMISH STRIKE **[one-action] **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/27', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/637', 'PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/27', 'PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/29', 'PZO22001 Starfinder Player Core 126-137::/page/8/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/8/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/27` | 0.908138 | **SKIRMISH STRIKE **[one-action] **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/637` | 0.594239 | Skirmish Strike |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/31` | 0.587527 | **TACTICAL SWAP **[one-action] **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/23` | 0.527707 | **DISARMING SHOT **[two-actions] **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/4/SectionHeader/1` | 0.496189 | **OVERWHELMING STRIKE **[free-action] |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/14` | 0.478582 | **HAIR TRIGGER **[reaction] **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/52` | 0.474095 | **TACTICAL ADVANCE **[one-action] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/46` | 0.472349 | **GRAZING SHOT **[one-action] **FEAT 12** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/17` | 0.465166 | **DESTRUCTIVE DASH **[two-actions] **FEAT 6** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/20` | 0.462112 | **KICK IT INTO OVERDRIVE **[free-action] **FEAT 6** |

### Query 129
- Text: What are the requirements for **TACTICAL SWAP **[one-action] **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/31', 'PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/52', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/649']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/31', 'PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/33', 'PZO22001 Starfinder Player Core 126-137::/page/8/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/8/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/31` | 0.924132 | **TACTICAL SWAP **[one-action] **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/52` | 0.661762 | **TACTICAL ADVANCE **[one-action] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/649` | 0.638524 | Tactical Swap |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/27` | 0.520422 | **SKIRMISH STRIKE **[one-action] **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/23` | 0.506919 | **DISARMING SHOT **[two-actions] **FEAT 6** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/8/Text/36` | 0.482894 | You swap weapons with a practiced motion. You Switch  Hands or Interact to swap your current weapon for another.  Make a Strike against the required target with your newly  drawn weapon. |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/40` | 0.480251 | **Prerequisites** Tactical Advance |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/6` | 0.478408 | **SWITCH TARGET **[free-action] **FEAT 4** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/44` | 0.477300 | **MOBILE AIM **[one-action] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/22` | 0.464707 | **DOUBLE TAP **[two-actions] **FEAT 2** |

### Query 130
- Text: What are the requirements for **UNHINDERED ADVANCE** **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/37', 'PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/40', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/657']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/37', 'PZO22001 Starfinder Player Core 126-137::/page/8/Text/36', 'PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/39']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/8/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/39` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/37` | 0.876947 | **UNHINDERED ADVANCE** **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/40` | 0.495865 | **Prerequisites** Tactical Advance |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/657` | 0.492191 | Unhindered Advance |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/20` | 0.445195 | **KICK IT INTO OVERDRIVE **[free-action] **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/52` | 0.444448 | **TACTICAL ADVANCE **[one-action] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/11/SectionHeader/23` | 0.423362 | **INFINITE AIM** **FEAT 20** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/55` | 0.405788 | **EXTREME ACCURACY** **FEAT 16** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/31` | 0.394852 | **TACTICAL SWAP **[one-action] **FEAT 6** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/36` | 0.387735 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/66` | 0.387735 | **SKILLS** **FEATS** |

### Query 131
- Text: What are the requirements for **Prerequisites** Tactical Advance?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/40']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/40', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/647', 'PZO22001 Starfinder Player Core 126-137::/page/8/Text/41']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/40', 'PZO22001 Starfinder Player Core 126-137::/page/8/Text/41', 'PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/39']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/8/Text/41` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/39` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/40` | 0.960846 | **Prerequisites** Tactical Advance |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/647` | 0.766744 | Tactical Advance |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/8/Text/41` | 0.633550 | When you use Tactical Advance, you ignore difficult terrain  and greater difficult terrain. |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/52` | 0.549706 | **TACTICAL ADVANCE **[one-action] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/1/Text/17` | 0.474562 | You train with your weapons, acquire and upgrade equipment, and practice tactical  drills for future engagements. |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/1` | 0.443247 | **OPERATIVE ADVANCEMENT** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/657` | 0.430486 | Unhindered Advance |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/Text/12` | 0.420156 | **Requirements** You're wielding a ranged weapon that doesn't  have the area trait. |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/4` | 0.412567 | **Requirements** You're wielding a gun. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/6` | 0.412567 | **Requirements** You're wielding a gun. |

### Query 132
- Text: What are the requirements for **OPENING VOLLEY **[one-action] **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/43', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/619', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/43', 'PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/45', 'PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/42']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/45` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/42` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/43` | 0.915547 | **OPENING VOLLEY **[one-action] **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/619` | 0.629328 | Opening Volley |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/6` | 0.562409 | **TOPPLING SHOT **[two-actions] **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/2` | 0.473555 | **PARKOUR **[one-action] **FEAT 8** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/44` | 0.455077 | **MOBILE AIM **[one-action] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/33` | 0.453090 | **PEEK **[one-action] **FEAT 2** **OPERATIVE** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/11` | 0.448731 | **TWIN SHOOTER** **FEAT 8** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/11` | 0.442016 | **TWIN DRAW **[one-action] **FEAT 4** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/3` | 0.433252 | **BULLET DANCE **[three-actions] **FEAT 18** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/46` | 0.432698 | **GRAZING SHOT **[one-action] **FEAT 12** |

### Query 133
- Text: What are the requirements for **PARKOUR **[one-action] **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/9/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/9/Text/2', 'PZO22001 Starfinder Player Core 126-137::/page/10/Text/10', 'PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/43']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/9/Text/2', 'PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/4', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/9/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/2` | 0.903014 | **PARKOUR **[one-action] **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/10` | 0.637766 | **Prerequisites** Parkour |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/43` | 0.554722 | **OPENING VOLLEY **[one-action] **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/6` | 0.503186 | **TOPPLING SHOT **[two-actions] **FEAT 8** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/625` | 0.497645 | Parkour |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/11` | 0.485424 | **TWIN DRAW **[one-action] **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/11` | 0.478020 | **TWIN SHOOTER** **FEAT 8** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/52` | 0.476911 | **TACTICAL ADVANCE **[one-action] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/44` | 0.467742 | **MOBILE AIM **[one-action] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/55` | 0.453420 | **STOP THEM IN THEIR TRACKS **[one-action] **FEAT 4** |

### Query 134
- Text: What are the requirements for **TOPPLING SHOT **[two-actions] **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/9/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/9/Text/6', 'PZO22001 Starfinder Player Core 126-137::/page/11/Text/8', 'PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/50']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/9/Text/6', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/5', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/9/Text/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/9/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/6` | 0.899457 | **TOPPLING SHOT **[two-actions] **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/8` | 0.644759 | **KILL SHOT **[two-actions]** OR **[three-actions] **FEAT 18** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/50` | 0.625791 | **HAMPERING SHOT **[two-actions] **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/11` | 0.583316 | **TWIN SHOOTER** **FEAT 8** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/17` | 0.562406 | **IMPEDING SHOT **[two-actions] **FEAT 10** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/651` | 0.554317 | Toppling Shot |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/1` | 0.552589 | **RUNNING SHOT **[two-actions] **FEAT 12** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/8` | 0.549672 | **WEAKENING SHOT **[two-actions] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/46` | 0.543603 | **GRAZING SHOT **[one-action] **FEAT 12** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/43` | 0.535715 | **OPENING VOLLEY **[one-action] **FEAT 8** |

### Query 135
- Text: What are the requirements for **TWIN SHOOTER** **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/9/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/9/Text/11', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/655', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/9/Text/11', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/10', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/9/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/9/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/11` | 0.898852 | **TWIN SHOOTER** **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/655` | 0.644338 | Twin Shooter |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/6` | 0.575695 | **TOPPLING SHOT **[two-actions] **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/11` | 0.530921 | **TWIN DRAW **[one-action] **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/14` | 0.468551 | **Prerequisites** Twin Draw |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/8` | 0.455173 | **KILL SHOT **[two-actions]** OR **[three-actions] **FEAT 18** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/11` | 0.426125 | **Requirements** You're wielding a gun. |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/55` | 0.426125 | **Requirements** You're wielding a gun. |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/6` | 0.426125 | **Requirements** You're wielding a gun. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/18` | 0.426125 | **Requirements** You're wielding a gun. |

### Query 136
- Text: What are the requirements for **Prerequisites** Twin Draw?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/9/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/9/Text/14', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/653', 'PZO22001 Starfinder Player Core 126-137::/page/10/Text/42']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/9/Text/14', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/13', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/9/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/9/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/14` | 0.954890 | **Prerequisites** Twin Draw |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/653` | 0.784000 | Twin Draw |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/42` | 0.524157 | **Prerequisites** Double Tap |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/11` | 0.441531 | **TWIN DRAW **[one-action] **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/655` | 0.406907 | Twin Shooter |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/13` | 0.391572 | **Requirements** You have two free hands. |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/58` | 0.373054 | **Prerequisites** Keep Them in Your Sights |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/49` | 0.366832 | **Requirements** You have a mark. |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/58` | 0.353948 | **Prerequisites** trained in Intimidation |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/7/Text/14` | 0.345691 | You've practiced smoothly drawing and taking aim with  two weapons. Draw up to two one-handed weapons  and Aim. |

### Query 137
- Text: What are the requirements for **IMPEDING SHOT **[two-actions] **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/17', 'PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/37', 'PZO22001 Starfinder Player Core 126-137::/page/11/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/17', 'PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/16', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/9/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/17` | 0.908843 | **IMPEDING SHOT **[two-actions] **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/37` | 0.654532 | **SPRINT **[two-actions]** OR **[three-actions] **FEAT 10** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/8` | 0.634259 | **KILL SHOT **[two-actions]** OR **[three-actions] **FEAT 18** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/8` | 0.591344 | **WEAKENING SHOT **[two-actions] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/50` | 0.589022 | **HAMPERING SHOT **[two-actions] **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/1` | 0.579903 | **RUNNING SHOT **[two-actions] **FEAT 12** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/22` | 0.579520 | **MUZZLE FLASH **[two-actions] **FEAT 10** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/23` | 0.577026 | **DISARMING SHOT **[two-actions] **FEAT 6** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/57` | 0.567121 | **OVERWHELMING SHOT **[two-actions] **FEAT 12** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/6` | 0.553203 | **TOPPLING SHOT **[two-actions] **FEAT 8** |

### Query 138
- Text: What are the requirements for **MUZZLE FLASH **[two-actions] **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/9/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/9/Text/22', 'PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/37', 'PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/9/Text/22', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/21', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/9/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/9/Text/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/22` | 0.922253 | **MUZZLE FLASH **[two-actions] **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/37` | 0.606324 | **SPRINT **[two-actions]** OR **[three-actions] **FEAT 10** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/17` | 0.604146 | **IMPEDING SHOT **[two-actions] **FEAT 10** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/617` | 0.517089 | Muzzle Flash |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/8` | 0.467062 | **KILL SHOT **[two-actions]** OR **[three-actions] **FEAT 18** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/23` | 0.460792 | **CLUSTERED SHOTS **[two-actions] **FEAT 14** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/22` | 0.460184 | **DOUBLE TAP **[two-actions] **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/1` | 0.456059 | **RUNNING SHOT **[two-actions] **FEAT 12** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/6` | 0.447745 | **TOPPLING SHOT **[two-actions] **FEAT 8** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/8` | 0.446410 | **WEAKENING SHOT **[two-actions] **FEAT 1** |

### Query 139
- Text: What are the requirements for **OPPORTUNE RETORT **[reaction] **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/27', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/621', 'PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/32']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/27', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/26', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/9/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/9/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/27` | 0.901926 | **OPPORTUNE RETORT **[reaction] **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/621` | 0.573968 | Opportune Retort |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/32` | 0.543018 | **PRACTICED ESCAPE **[reaction] **FEAT 10** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/37` | 0.456926 | **SPRINT **[two-actions]** OR **[three-actions] **FEAT 10** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/17` | 0.449226 | **IMPEDING SHOT **[two-actions] **FEAT 10** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/22` | 0.438015 | **MUZZLE FLASH **[two-actions] **FEAT 10** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/14` | 0.414072 | **HAIR TRIGGER **[reaction] **FEAT 6** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/75` | 0.394445 | **CONDITIONS ** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/31` | 0.393392 | **ELUSIVE TARGET **[reaction] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/36` | 0.392363 | **SWIFT REPOSITION **[reaction] **FEAT 2** |

### Query 140
- Text: What are the requirements for **PRACTICED ESCAPE **[reaction] **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/32', 'PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/17', 'PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/27']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/32', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/31', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/34']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/9/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/9/Text/34` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/32` | 0.903925 | **PRACTICED ESCAPE **[reaction] **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/17` | 0.552841 | **IMPEDING SHOT **[two-actions] **FEAT 10** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/27` | 0.535552 | **OPPORTUNE RETORT **[reaction] **FEAT 10** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/629` | 0.491218 | Practiced Escape |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/37` | 0.470953 | **SPRINT **[two-actions]** OR **[three-actions] **FEAT 10** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/22` | 0.452599 | **MUZZLE FLASH **[two-actions] **FEAT 10** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/31` | 0.452258 | **TACTICAL SWAP **[one-action] **FEAT 6** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/3/SectionHeader/27` | 0.430618 | **REACTIVE STEP **[reaction] |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/36` | 0.420365 | You've trained in close quarters combat and practiced how to  escape a hold, or similar situations. You attempt to Escape. If  you succeed or critically succeed, you can also Stand or Step. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/2/TableCell/419` | 0.418654 | On the move +10 feet, operative feat, skill feat |

### Query 141
- Text: What are the requirements for **SPRINT **[two-actions]** OR **[three-actions] **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/37', 'PZO22001 Starfinder Player Core 126-137::/page/11/Text/8', 'PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/37', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/39', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/36']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/9/Text/39` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/9/Text/36` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/37` | 0.945866 | **SPRINT **[two-actions]** OR **[three-actions] **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/8` | 0.641516 | **KILL SHOT **[two-actions]** OR **[three-actions] **FEAT 18** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/17` | 0.624202 | **IMPEDING SHOT **[two-actions] **FEAT 10** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/22` | 0.560311 | **MUZZLE FLASH **[two-actions] **FEAT 10** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/1` | 0.495635 | **RUNNING SHOT **[two-actions] **FEAT 12** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/22` | 0.468830 | **DOUBLE TAP **[two-actions] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/6` | 0.464564 | **TOPPLING SHOT **[two-actions] **FEAT 8** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/8` | 0.459623 | **WEAKENING SHOT **[two-actions] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/50` | 0.459589 | **HAMPERING SHOT **[two-actions] **FEAT 4** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/3` | 0.458003 | **BULLET DANCE **[three-actions] **FEAT 18** |

### Query 142
- Text: What are the requirements for **DUAL AIM** **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/42']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/42', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/575', 'PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/42', 'PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/41', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/44']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/41` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/9/Text/44` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/42` | 0.912145 | **DUAL AIM** **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/575` | 0.634769 | Dual Aim |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/1` | 0.564366 | **RUNNING SHOT **[two-actions] **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/52` | 0.515550 | **LINE 'EM UP **[two-actions] **FEAT 12** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/11/SectionHeader/23` | 0.508614 | **INFINITE AIM** **FEAT 20** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/11/SectionHeader/14` | 0.496627 | **RELENTLESS AIM** **FEAT 18** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/44` | 0.495596 | **MOBILE AIM **[one-action] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/2/SectionHeader/10` | 0.485699 | **AIM **[one-action] |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/46` | 0.477314 | **GRAZING SHOT **[one-action] **FEAT 12** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/22` | 0.466830 | **DOUBLE TAP **[two-actions] **FEAT 2** |

### Query 143
- Text: What are the requirements for **GRAZING SHOT **[one-action] **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/46']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/46', 'PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/1', 'PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/57']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/46', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/45', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/48']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/9/Text/45` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/9/Text/48` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/46` | 0.892685 | **GRAZING SHOT **[one-action] **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/1` | 0.664006 | **RUNNING SHOT **[two-actions] **FEAT 12** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/57` | 0.635660 | **OVERWHELMING SHOT **[two-actions] **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/587` | 0.564226 | Grazing Shot |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/50` | 0.536381 | **HAMPERING SHOT **[two-actions] **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/6` | 0.526746 | **TOPPLING SHOT **[two-actions] **FEAT 8** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/8` | 0.520660 | **KILL SHOT **[two-actions]** OR **[three-actions] **FEAT 18** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/17` | 0.520263 | **IMPEDING SHOT **[two-actions] **FEAT 10** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/23` | 0.508510 | **DISARMING SHOT **[two-actions] **FEAT 6** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/8` | 0.505177 | **WEAKENING SHOT **[two-actions] **FEAT 1** |

### Query 144
- Text: What are the requirements for **LINE 'EM UP **[two-actions] **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/52']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/52', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/613', 'PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/42']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/52', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/51', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/54']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/9/Text/51` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/9/Text/54` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/52` | 0.908150 | **LINE 'EM UP **[two-actions] **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/613` | 0.618302 | Line 'Em Up |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/42` | 0.612642 | **DUAL AIM** **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/1` | 0.554282 | **RUNNING SHOT **[two-actions] **FEAT 12** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/46` | 0.497819 | **GRAZING SHOT **[one-action] **FEAT 12** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/57` | 0.491262 | **OVERWHELMING SHOT **[two-actions] **FEAT 12** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/37` | 0.490146 | **SPRINT **[two-actions]** OR **[three-actions] **FEAT 10** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/17` | 0.483782 | **IMPEDING SHOT **[two-actions] **FEAT 10** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/22` | 0.474244 | **MUZZLE FLASH **[two-actions] **FEAT 10** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/44` | 0.468351 | **MOBILE AIM **[one-action] **FEAT 1** |

### Query 145
- Text: What are the requirements for **OVERWHELMING SHOT **[two-actions] **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/57']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/57', 'PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/1', 'PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/46']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/57', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/56', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/59']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/9/Text/56` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/9/Text/59` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/57` | 0.904713 | **OVERWHELMING SHOT **[two-actions] **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/1` | 0.715416 | **RUNNING SHOT **[two-actions] **FEAT 12** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/46` | 0.685827 | **GRAZING SHOT **[one-action] **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/17` | 0.587592 | **IMPEDING SHOT **[two-actions] **FEAT 10** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/8` | 0.552705 | **WEAKENING SHOT **[two-actions] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/50` | 0.551928 | **HAMPERING SHOT **[two-actions] **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/23` | 0.549762 | **DISARMING SHOT **[two-actions] **FEAT 6** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/8` | 0.549250 | **KILL SHOT **[two-actions]** OR **[three-actions] **FEAT 18** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/42` | 0.543264 | **DUAL AIM** **FEAT 12** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/623` | 0.542067 | Overwhelming Shot |

### Query 146
- Text: What are the requirements for **RUNNING SHOT **[two-actions] **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/1', 'PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/57', 'PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/46']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/1', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/77', 'PZO22001 Starfinder Player Core 126-137::/page/10/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/9/Text/77` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/10/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/1` | 0.903927 | **RUNNING SHOT **[two-actions] **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/57` | 0.681940 | **OVERWHELMING SHOT **[two-actions] **FEAT 12** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/46` | 0.668300 | **GRAZING SHOT **[one-action] **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/8` | 0.598542 | **KILL SHOT **[two-actions]** OR **[three-actions] **FEAT 18** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/17` | 0.582848 | **IMPEDING SHOT **[two-actions] **FEAT 10** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/8` | 0.569620 | **WEAKENING SHOT **[two-actions] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/6/SectionHeader/50` | 0.557060 | **HAMPERING SHOT **[two-actions] **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/42` | 0.554435 | **DUAL AIM** **FEAT 12** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/52` | 0.547911 | **LINE 'EM UP **[two-actions] **FEAT 12** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/633` | 0.546104 | Running Shot |

### Query 147
- Text: What are the requirements for **360 NO SCOPE **[two-actions] **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/7', 'PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/23', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/547']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/7', 'PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/6', 'PZO22001 Starfinder Player Core 126-137::/page/10/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/10/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/7` | 0.907568 | **360 NO SCOPE **[two-actions] **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/23` | 0.615211 | **CLUSTERED SHOTS **[two-actions] **FEAT 14** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/547` | 0.613817 | 360 No Scope |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/Table/3` | 0.507552 | FeatLevel360 No Scope14Bloody Wounds4Bullet Dance18Bullet Fever14Burst Fire16Cloaking Field16Clustered Shots14Combat Reflexes20Danger Awareness2Defensive Gunner2Destructive Dash6Devastating Aim4Disarm |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/28` | 0.493465 | **FISH IN A BARREL **[two-actions] **FEAT 14** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/32` | 0.478962 | **FOLLOW-UP FIRE **[free-action] **FEAT 14** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/8` | 0.476998 | **KILL SHOT **[two-actions]** OR **[three-actions] **FEAT 18** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/44` | 0.463505 | **CLOAKING FIELD **[two-actions] **FEAT 16** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/37` | 0.451714 | **SPRINT **[two-actions]** OR **[three-actions] **FEAT 10** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/1` | 0.446574 | **RUNNING SHOT **[two-actions] **FEAT 12** |

### Query 148
- Text: What are the requirements for **Prerequisites** Parkour?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/10/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/10/Text/10', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/625', 'PZO22001 Starfinder Player Core 126-137::/page/9/Text/49']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/10/Text/10', 'PZO22001 Starfinder Player Core 126-137::/page/10/Text/11', 'PZO22001 Starfinder Player Core 126-137::/page/10/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/10/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/10/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/10` | 0.932742 | **Prerequisites** Parkour |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/625` | 0.732828 | Parkour |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/49` | 0.490763 | **Requirements** You have a mark. |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/12` | 0.437247 | You fire a trick shot as part of a daredevil maneuver. You Parkour.  You can Aim and then make a ranged Strike with the gun you're  wielding during this movement, including when you're falling. |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/2` | 0.433678 | **PARKOUR **[one-action] **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/58` | 0.394545 | **Prerequisites** Keep Them in Your Sights |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/40` | 0.391973 | **Prerequisites** Tactical Advance |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/5/Text/55` | 0.380400 | **Requirements** You aren't encumbered. |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/10/Text/11` | 0.357689 | **Requirements** You're wielding a gun. |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/6/Text/58` | 0.355168 | **Prerequisites** trained in Intimidation |

### Query 149
- Text: What are the requirements for **BULLET FEVER **[reaction] **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/13', 'PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/32', 'PZO22001 Starfinder Player Core 126-137::/page/11/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/13', 'PZO22001 Starfinder Player Core 126-137::/page/10/Text/12', 'PZO22001 Starfinder Player Core 126-137::/page/10/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/10/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/10/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/13` | 0.890825 | **BULLET FEVER **[reaction] **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/32` | 0.565999 | **FOLLOW-UP FIRE **[free-action] **FEAT 14** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/3` | 0.556004 | **BULLET DANCE **[three-actions] **FEAT 18** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/553` | 0.513572 | Bullet Fever |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/23` | 0.494625 | **CLUSTERED SHOTS **[two-actions] **FEAT 14** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/28` | 0.479701 | **FISH IN A BARREL **[two-actions] **FEAT 14** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/39` | 0.455791 | **BURST FIRE** **FEAT 16** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/7` | 0.455154 | **360 NO SCOPE **[two-actions] **FEAT 14** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/7/Table/3` | 0.423847 | FeatLevel360 No Scope14Bloody Wounds4Bullet Dance18Bullet Fever14Burst Fire16Cloaking Field16Clustered Shots14Combat Reflexes20Danger Awareness2Defensive Gunner2Destructive Dash6Devastating Aim4Disarm |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/5/SectionHeader/31` | 0.414261 | **ELUSIVE TARGET **[reaction] **FEAT 1** |

### Query 150
- Text: What are the requirements for **CLUSTERED SHOTS **[two-actions] **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/23', 'PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/7', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/559']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/23', 'PZO22001 Starfinder Player Core 126-137::/page/10/Text/22', 'PZO22001 Starfinder Player Core 126-137::/page/10/Text/25']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/10/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/10/Text/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/23` | 0.928468 | **CLUSTERED SHOTS **[two-actions] **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/7` | 0.625041 | **360 NO SCOPE **[two-actions] **FEAT 14** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/559` | 0.617678 | Clustered Shots |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/8` | 0.544133 | **KILL SHOT **[two-actions]** OR **[three-actions] **FEAT 18** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/1` | 0.543640 | **RUNNING SHOT **[two-actions] **FEAT 12** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/28` | 0.542509 | **FISH IN A BARREL **[two-actions] **FEAT 14** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/17` | 0.519880 | **IMPEDING SHOT **[two-actions] **FEAT 10** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/57` | 0.511969 | **OVERWHELMING SHOT **[two-actions] **FEAT 12** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/46` | 0.505064 | **GRAZING SHOT **[one-action] **FEAT 12** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/32` | 0.504649 | **FOLLOW-UP FIRE **[free-action] **FEAT 14** |

### Query 151
- Text: What are the requirements for **FISH IN A BARREL **[two-actions] **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/28', 'PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/23', 'PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/28', 'PZO22001 Starfinder Player Core 126-137::/page/10/Text/30', 'PZO22001 Starfinder Player Core 126-137::/page/10/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/10/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/10/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/28` | 0.919471 | **FISH IN A BARREL **[two-actions] **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/23` | 0.609967 | **CLUSTERED SHOTS **[two-actions] **FEAT 14** |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/7` | 0.567965 | **360 NO SCOPE **[two-actions] **FEAT 14** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/583` | 0.498502 | Fish in a Barrel |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/37` | 0.481665 | **SPRINT **[two-actions]** OR **[three-actions] **FEAT 10** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/11/Text/8` | 0.479526 | **KILL SHOT **[two-actions]** OR **[three-actions] **FEAT 18** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/9/Text/22` | 0.478442 | **MUZZLE FLASH **[two-actions] **FEAT 10** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/17` | 0.471319 | **IMPEDING SHOT **[two-actions] **FEAT 10** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/32` | 0.461575 | **FOLLOW-UP FIRE **[free-action] **FEAT 14** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/1` | 0.459240 | **RUNNING SHOT **[two-actions] **FEAT 12** |

### Query 152
- Text: What are the requirements for **FOLLOW-UP FIRE **[free-action] **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/32', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/585', 'PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/32', 'PZO22001 Starfinder Player Core 126-137::/page/10/Text/34', 'PZO22001 Starfinder Player Core 126-137::/page/10/Text/31']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/10/Text/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/10/Text/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/32` | 0.924904 | **FOLLOW-UP FIRE **[free-action] **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/585` | 0.608524 | Follow-Up Fire |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/23` | 0.534276 | **CLUSTERED SHOTS **[two-actions] **FEAT 14** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/7` | 0.483344 | **360 NO SCOPE **[two-actions] **FEAT 14** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/13` | 0.473837 | **BULLET FEVER **[reaction] **FEAT 14** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/39` | 0.464938 | **BURST FIRE** **FEAT 16** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/7/SectionHeader/6` | 0.457720 | **SWITCH TARGET **[free-action] **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/8/SectionHeader/20` | 0.456352 | **KICK IT INTO OVERDRIVE **[free-action] **FEAT 6** |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/9/SectionHeader/52` | 0.452693 | **LINE 'EM UP **[two-actions] **FEAT 12** |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/44` | 0.450059 | **CLOAKING FIELD **[two-actions] **FEAT 16** |

### Query 153
- Text: What are the requirements for **BURST FIRE** **FEAT 16**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/39', 'PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/555', 'PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/55']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/39', 'PZO22001 Starfinder Player Core 126-137::/page/10/Text/41', 'PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/38']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 126-137::/page/10/Text/41` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/38` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/39` | 0.914072 | **BURST FIRE** **FEAT 16** |
| 2 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/555` | 0.620008 | Burst Fire |
| 3 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/55` | 0.521178 | **EXTREME ACCURACY** **FEAT 16** |
| 4 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/32` | 0.470141 | **FOLLOW-UP FIRE **[free-action] **FEAT 14** |
| 5 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/49` | 0.449288 | **EXPLOSIVE DEFLECTION** **FEAT 16** |
| 6 | `PZO22001 Starfinder Player Core 126-137::/page/10/SectionHeader/13` | 0.444810 | **BULLET FEVER **[reaction] **FEAT 14** |
| 7 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/556` | 0.420141 | 16 |
| 8 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/585` | 0.416395 | Follow-Up Fire |
| 9 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/582` | 0.408141 | 16 |
| 10 | `PZO22001 Starfinder Player Core 126-137::/page/7/TableCell/558` | 0.408141 | 16 |
