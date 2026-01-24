# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `842`
- Query count: `144`
- Evaluated queries: `144`
- Coverage: `1.0000`
- MRR: `0.8546`
- hit@1: `0.7778`
- hit@3: `0.9097`
- hit@5: `0.9583`
- hit@10: `0.9931`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

### Expanded Gold Metrics
- Coverage: `1.0000`
- MRR: `0.8546`
- hit@1: `0.7778`
- hit@3: `0.9097`
- hit@5: `0.9583`
- hit@10: `0.9931`

### Expanded Gold Expansion Stats
- Queries with additions: `144`
- Avg added per query: `2.08`
- Max added: `7`
- Addition reasons:
  - graph_depth_1: `299`

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
- Embedding (chunks): `10139`
- Embedding (queries): `2137`
- Evaluation (strict): `100`
- Evaluation (expanded): `57`
- Total: `16718`

### Timing Estimates (ms)
- Evaluation (strict): `129`
- Evaluation (expanded): `43`
- Total: `12448`

## Query Details
### Query 0
- Text: Summarize MYSTIC
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/1']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/10/Text/7', 'PZO22001 Starfinder Player Core 114-125::/page/10/Text/25', 'PZO22001 Starfinder Player Core 114-125::/page/10/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/7` | 0.947410 | MYSTIC |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/25` | 0.947410 | MYSTIC |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/15` | 0.947410 | MYSTIC |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/3` | 0.905410 | MYSTIC |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/1` | 0.905410 | MYSTIC |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/35` | 0.905410 | MYSTIC |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/25` | 0.871254 | **MYSTIC** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/10` | 0.871254 | **MYSTIC** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/5` | 0.871254 | **MYSTIC** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/53` | 0.871254 | **MYSTIC** |

### Query 1
- Text: What is the rule about You're a conduit, channeling the fundamental forces that connect and bind everything in the cosmos.  You can draw upon this supernatural wellspring to form deep spiritual bonds with your allies,  empower them in combat, and restore their health should they become injured. Your powers take  unique shape based on the connection you choose, granting new and more powerful spells as you  explore your connection on a deeper level.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/2', 'PZO22001 Starfinder Player Core 114-125::/page/5/Text/11', 'PZO22001 Starfinder Player Core 114-125::/page/6/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/2', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/4', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/2` | 0.979544 | You're a conduit, channeling the fundamental forces that connect and bind everything in the cosmos.  You can draw upon this supernatural wellspring to form deep spiritual bonds with your allies,  empo |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/11` | 0.739448 | Your connection is a mystical force that grants you magic. It  could come from a divine patron, manifestation of a primeval  cosmic force, or some other mystery. Your connection  determines your spell |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/14` | 0.706615 | You're connected to the fount of vitality and void energy that  flows through all living things on every planet. You weave these  energies into spells that heal your allies and harm your enemies. |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/9` | 0.663379 | All mystics have a supernatural connection with a cosmic force  that grants magical powers. The exact nature of your connection  can vary widely—you might worship a god or pantheon, embody  a metaphys |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/35` | 0.640787 | Through dedication or serendipity, you've branched out to  explore other connections to the fundamental building blocks of  the cosmos. You learn the initial epiphany spell of a connection  that grant |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/7` | 0.634616 | You discover the ultimate truth of your connection and its  role as a foundation of the cosmos. You learn your chosen  connection's perfect harmony. |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/8` | 0.626432 | You see into the truth of the cosmos through your connection. You gain the greater epiphany spell for your chosen connection. |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/11` | 0.624026 | You cast powerful spells that blast enemies and empower allies. You heal allies you  share a bond with by drawing on your vitality network. |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/10` | 0.620239 | might interpret the source of their powers differently. At 1st level,  choose your connection. Your chosen connection determines the  type of spells you cast and the spell tradition you choose spells |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/7` | 0.616311 | Plumbing the depths of your own connection, you  understand how your piece of reality interconnects  with another. You learn the advanced epiphany spell of  the connection that grants training in the |

### Query 2
- Text: Summarize **KEY ATTRIBUTE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/4', 'PZO22001 Starfinder Player Core 114-125::/page/6/SectionHeader/1', 'PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/4', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/2', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/4` | 0.948607 | **KEY ATTRIBUTE** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/6/SectionHeader/1` | 0.665018 | **KEY TERMS** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/4` | 0.599101 | **Attributes** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/38` | 0.437617 | **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/50` | 0.437617 | **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/76` | 0.437617 | **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/49` | 0.437617 | **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/73` | 0.407698 | **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/2` | 0.400210 | You'll see the following key terms in many mystic class  features. |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/6` | 0.398872 | **Skills** |

### Query 3
- Text: Summarize **Wisdom**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/5', 'PZO22001 Starfinder Player Core 114-125::/page/8/Text/5', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/5', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/4', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/5` | 0.928886 | **Wisdom** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/5` | 0.446775 | Focus on Wisdom, followed by Dexterity. Add to  Constitution for more health and Strength to wield an  aucturnite chakram. |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/6` | 0.434199 | At 1st level, your class gives you  an attribute boost to Wisdom. |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/6` | 0.373961 | **Skills** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/73` | 0.359591 | **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/6/SectionHeader/1` | 0.357021 | **KEY TERMS** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/39` | 0.355925 | **GAME** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/6` | 0.350007 | Some of your spells require you to attempt a spell attack to  see how effective they are or have your enemies roll against  your spell DC (typically by attempting a saving throw). Since  your key attr |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/31` | 0.341226 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/34` | 0.341226 | **INTRODUCTION** |

### Query 4
- Text: Summarize At 1st level, your class gives you  an attribute boost to Wisdom.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/6', 'PZO22001 Starfinder Player Core 114-125::/page/2/Text/4', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/6', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/5', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/6` | 1.032734 | At 1st level, your class gives you  an attribute boost to Wisdom. |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/4` | 0.731405 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/29` | 0.624125 | In addition to what you get from your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/5` | 0.581865 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/7` | 0.581688 | At 1st level, you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start  of this class. |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/27` | 0.570566 | You gain these abilities as a mystic. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/Table/2` | 0.549706 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, connection, initial epiphany, mystic bond, vitality network, mystic spellcasting, spell repertoire2Mystic fea |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/9` | 0.538978 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/6` | 0.537328 | Some of your spells require you to attempt a spell attack to  see how effective they are or have your enemies roll against  your spell DC (typically by attempting a saving throw). Since  your key attr |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/9` | 0.526910 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use an increase to either become trained in  one skill you're untrained in or to increase your proficiency  in one skill |

### Query 5
- Text: What is the rule about **HIT POINTS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/7', 'PZO22001 Starfinder Player Core 114-125::/page/2/Text/22', 'PZO22001 Starfinder Player Core 114-125::/page/10/Text/32']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/7', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/8', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/7` | 0.884304 | **HIT POINTS** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/22` | 0.488337 | You can transfer up to 10 Hit Points (minimum 1) from your  vitality network into yourself or a bonded creature you can |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/32` | 0.486856 | With extreme concentration, you can sacrifice your own Hit Points to recharge your vitality network. Your vitality network regains Hit Points equal to the amount you sacrifice. |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/19` | 0.411145 | Life-and-death situations help strengthen your bonds with  your allies. At the start of each turn in combat, when you  regain actions, your vitality network regains 4 Hit Points; if  you're master in |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/23` | 0.403918 | With careful focus, you guarantee vital energy lost from a target  is caught by your vitality network. If the next action you use is  to Cast a Spell that deals void damage to a living creature, your |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/10/ListItem/45` | 0.396514 | If their spell deals damage or heals Hit Points and doesn't have a duration, you grant that spell a status bonus to damage or healing equal to its rank. |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/16` | 0.390462 | You always know the general distance and direction toward  other bonded creatures, their Hit Point totals, and if they're  conscious, unconscious, dying, or dead. This ability doesn't  work across pla |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/27` | 0.390338 | You understand the true nature of your connection and how  it stretches across the vast pillars of reality. Your vitality  network has a maximum capacity of 200 Hit Points and  regains 20 Hit Points a |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/18` | 0.378287 | Your vitality network absorbs the essence of the attack. Your vitality network regains 2 Hit Points per rank of the triggering spell or 4 Hit Points per weapon die of the triggering Strike. |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/13` | 0.377981 | Focus spells are automatically heightened to half your level  rounded up, much like cantrips. Focus spells don't require spell  slots, and you can't cast them using spell slots. Taking feats can  give |

### Query 6
- Text: What is the rule about **6 + Constitution modifier**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/8', 'PZO22001 Starfinder Player Core 114-125::/page/2/Text/5', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/58']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/8', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/9', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/8` | 0.867623 | **6 + Constitution modifier** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/5` | 0.500323 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/58` | 0.475634 | Trained in a number of additional  skills equal to 3 plus your Intelligence  modifier |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/576` | 0.414787 | 6 |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/580` | 0.414787 | 6 |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/582` | 0.414787 | 6 |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/398` | 0.414787 | 6 |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/586` | 0.414787 | 6 |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/935` | 0.414787 | 6 |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/4` | 0.377003 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |

### Query 7
- Text: Summarize You increase your maximum number  of HP by this number at 1st level and  every level thereafter.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/9', 'PZO22001 Starfinder Player Core 114-125::/page/4/Text/9', 'PZO22001 Starfinder Player Core 114-125::/page/2/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/9', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/9` | 1.031874 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/9` | 0.641938 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use an increase to either become trained in  one skill you're untrained in or to increase your proficiency  in one skill |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/5` | 0.604495 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/25` | 0.526529 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/4` | 0.520901 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/6` | 0.518215 | At 1st level, your class gives you  an attribute boost to Wisdom. |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/27` | 0.516808 | You gain these abilities as a mystic. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/14` | 0.516543 | When you gain access to a new rank of spells, your first new  spell is always the spell granted by your chosen connection,  but you can choose the other spells. At 2nd level, you select  another 1st-r |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/10` | 0.516332 | At 7th level, you can use skill increases to become a  master in a skill in which you're already an expert, and at  15th level, you can use them to become legendary in a skill  in which you're already |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/51` | 0.514252 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |

### Query 8
- Text: Summarize DURING COMBAT ENCOUNTERS...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/12', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/9', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/10` | 0.983036 | DURING COMBAT ENCOUNTERS... |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/12` | 0.745777 | DURING SOCIAL ENCOUNTERS... |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/14` | 0.434305 | WHILE EXPLORING... |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/16` | 0.337787 | IN DOWNTIME... |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/63` | 0.333292 | **Soldier** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/39` | 0.333292 | **Soldier** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/27` | 0.333292 | **Soldier** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/39` | 0.333292 | **Soldier** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/40` | 0.333292 | **Soldier** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/39` | 0.333292 | **Soldier** |

### Query 9
- Text: What is the rule about You cast powerful spells that blast enemies and empower allies. You heal allies you  share a bond with by drawing on your vitality network.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/11', 'PZO22001 Starfinder Player Core 114-125::/page/10/Text/50', 'PZO22001 Starfinder Player Core 114-125::/page/6/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/11', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/11` | 0.934739 | You cast powerful spells that blast enemies and empower allies. You heal allies you  share a bond with by drawing on your vitality network. |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/50` | 0.728192 | You infuse your magic with vital energy that empowers the target of your spell. Pick a spell and reduce your vitality network's total by a number equal to twice the spell's rank. If your next action i |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/14` | 0.705248 | You're connected to the fount of vitality and void energy that  flows through all living things on every planet. You weave these  energies into spells that heal your allies and harm your enemies. |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/44` | 0.653485 | You pulse energy through your bond as your ally casts a spell, empowering their spell in one of the following ways. |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/6` | 0.650671 | You prepare your vitality network to catch some of your  excess magic, allowing it to flow back and bolster your bond's  defenses. If the next action you use is to Cast a Spell that  deals damage, whe |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/18` | 0.647951 | Your soul supports a network of energy that connects and  heals those in your bond. Your vitality network has a maximum  capacity equal to 6 + 4 Hit Points per level. You gain the  Transfer Vitality a |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/11` | 0.643234 | You can manifest your bond as a web of vital energy between  your allies. You learn the *vitality* *web* epiphany spell  (page 377). |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/10` | 0.629023 | might interpret the source of their powers differently. At 1st level,  choose your connection. Your chosen connection determines the  type of spells you cast and the spell tradition you choose spells |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/40` | 0.607155 | You quickly expend energy from your vitality network toward  a bonded ally. Transfer Vitality to the triggering ally. |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/27` | 0.605276 | You understand the true nature of your connection and how  it stretches across the vast pillars of reality. Your vitality  network has a maximum capacity of 200 Hit Points and  regains 20 Hit Points a |

### Query 10
- Text: Summarize DURING SOCIAL ENCOUNTERS...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/12', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/12', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/13', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/12` | 0.977694 | DURING SOCIAL ENCOUNTERS... |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/10` | 0.728104 | DURING COMBAT ENCOUNTERS... |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/14` | 0.408727 | WHILE EXPLORING... |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/16` | 0.315217 | IN DOWNTIME... |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/22` | 0.286287 | OTHERS PROBABLY... |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/18` | 0.285896 | YOU MIGHT... |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/17` | 0.284776 | You reflect on your connection to deepen your understanding. You spend time  with your bonded allies, perhaps working on the same side hustle, going on a hike  together, or forming a guild in your fav |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/59` | 0.282589 | **Envoy** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/35` | 0.282589 | **Envoy** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/37` | 0.282589 | **Envoy** |

### Query 11
- Text: What is the rule about Your connection shapes your perspective on the world and the way you approach  problems. When a disagreement erupts between bonded members, you're often the  one to help them talk through their problems.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/13', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/17', 'PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/13', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/13` | 0.959114 | Your connection shapes your perspective on the world and the way you approach  problems. When a disagreement erupts between bonded members, you're often the  one to help them talk through their proble |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/17` | 0.685675 | You reflect on your connection to deepen your understanding. You spend time  with your bonded allies, perhaps working on the same side hustle, going on a hike  together, or forming a guild in your fav |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/20` | 0.646664 | Have insights into the nature of your connection that others find unorthodox. |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/7` | 0.586870 | You discover the ultimate truth of your connection and its  role as a foundation of the cosmos. You learn your chosen  connection's perfect harmony. |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/7` | 0.580947 | Plumbing the depths of your own connection, you  understand how your piece of reality interconnects  with another. You learn the advanced epiphany spell of  the connection that grants training in the |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/11` | 0.580421 | Your connection is a mystical force that grants you magic. It  could come from a divine patron, manifestation of a primeval  cosmic force, or some other mystery. Your connection  determines your spell |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/44` | 0.571642 | You gain a deeper understanding of your connection. You gain  the advanced epiphany spell for your chosen connection. |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/2` | 0.562551 | You're a conduit, channeling the fundamental forces that connect and bind everything in the cosmos.  You can draw upon this supernatural wellspring to form deep spiritual bonds with your allies,  empo |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/10` | 0.556735 | might interpret the source of their powers differently. At 1st level,  choose your connection. Your chosen connection determines the  type of spells you cast and the spell tradition you choose spells |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/25` | 0.551744 | Assume you view the universe through the lens of your connection. |

### Query 12
- Text: Summarize WHILE EXPLORING...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/12', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/13', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/14` | 0.945993 | WHILE EXPLORING... |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/12` | 0.439598 | DURING SOCIAL ENCOUNTERS... |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/10` | 0.437469 | DURING COMBAT ENCOUNTERS... |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/16` | 0.348777 | IN DOWNTIME... |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/33` | 0.333417 | **PLAYING THE ** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/45` | 0.330508 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/44` | 0.330508 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/46` | 0.330508 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/70` | 0.330508 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/46` | 0.330508 | **PLAYING THE ** **GAME** |

### Query 13
- Text: What is the rule about You search for traces of magic and notice details relevant to your connection.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/15', 'PZO22001 Starfinder Player Core 114-125::/page/5/Text/11', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/44']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/15', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/15` | 0.921793 | You search for traces of magic and notice details relevant to your connection. |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/11` | 0.574434 | Your connection is a mystical force that grants you magic. It  could come from a divine patron, manifestation of a primeval  cosmic force, or some other mystery. Your connection  determines your spell |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/44` | 0.528366 | You gain a deeper understanding of your connection. You gain  the advanced epiphany spell for your chosen connection. |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/31` | 0.480392 | You channel magic through your connection.  Your proficiency ranks for spell attack  modifiers and spell DCs increase to master. |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/16` | 0.478394 | **Connection Spells** cantrip: *scan* *environment*; 1st: *akashic* *download*; 2nd: *instant* *virus*; 3rd: *hypercognition*; 4th:  *clairvoyance*; 5th: *wave* of *warning*; 6th: *truesight*; 7th:  * |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/10` | 0.475137 | might interpret the source of their powers differently. At 1st level,  choose your connection. Your chosen connection determines the  type of spells you cast and the spell tradition you choose spells |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/16` | 0.458378 | You always know the general distance and direction toward  other bonded creatures, their Hit Point totals, and if they're  conscious, unconscious, dying, or dead. This ability doesn't  work across pla |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/29` | 0.457498 | **Connection Spells** cantrip: *figment*; 1st: *grim tendrils*; 2nd:  *invisibility*; 3rd: *slow*; 4th: *flicker*; 5th: *shadow blast*;  6th: *mislead*; 7th: *eclipse burst*; 8th: *disappearance*; 9th |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/28` | 0.456396 | **Tradition** divine; **Connection Skill** Stealth |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/17` | 0.455975 | You've formed a more powerful bond with your connection.  Your proficiency ranks for spell attack modifiers and spell  DCs increase to expert. |

### Query 14
- Text: Summarize IN DOWNTIME...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/16', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/16', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/15', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/16` | 0.786911 | IN DOWNTIME... |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/18` | 0.405938 | YOU MIGHT... |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/12` | 0.367088 | DURING SOCIAL ENCOUNTERS... |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/14` | 0.322232 | WHILE EXPLORING... |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/10/SectionHeader/33` | 0.319066 | CONVERT TEMPO ◆ TO ◆>> |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/10` | 0.314851 | DURING COMBAT ENCOUNTERS... |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/22` | 0.302606 | OTHERS PROBABLY... |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/549` | 0.295022 | Convert Tempo |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/6/SectionHeader/1` | 0.287179 | **KEY TERMS** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/39` | 0.281902 | **GAME** |

### Query 15
- Text: Summarize You reflect on your connection to deepen your understanding. You spend time  with your bonded allies, perhaps working on the same side hustle, going on a hike  together, or forming a guild in your favorite vidgame.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/17', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/13', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/17', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/17` | 1.028288 | You reflect on your connection to deepen your understanding. You spend time  with your bonded allies, perhaps working on the same side hustle, going on a hike  together, or forming a guild in your fav |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/13` | 0.739956 | Your connection shapes your perspective on the world and the way you approach  problems. When a disagreement erupts between bonded members, you're often the  one to help them talk through their proble |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/11` | 0.669724 | You cast powerful spells that blast enemies and empower allies. You heal allies you  share a bond with by drawing on your vitality network. |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/2` | 0.612468 | You're a conduit, channeling the fundamental forces that connect and bind everything in the cosmos.  You can draw upon this supernatural wellspring to form deep spiritual bonds with your allies,  empo |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/7` | 0.594630 | Plumbing the depths of your own connection, you  understand how your piece of reality interconnects  with another. You learn the advanced epiphany spell of  the connection that grants training in the |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/15` | 0.593263 | You form a bond between yourself and others, most typically  your closest companions. Forming bonds is different for every  mystic but always involves using a 10-minute activity related  to the mystic |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/44` | 0.587130 | You gain a deeper understanding of your connection. You gain  the advanced epiphany spell for your chosen connection. |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/20` | 0.580234 | Have insights into the nature of your connection that others find unorthodox. |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/35` | 0.568813 | Through dedication or serendipity, you've branched out to  explore other connections to the fundamental building blocks of  the cosmos. You learn the initial epiphany spell of a connection  that grant |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/11` | 0.562680 | You can manifest your bond as a web of vital energy between  your allies. You learn the *vitality* *web* epiphany spell  (page 377). |

### Query 16
- Text: Summarize YOU MIGHT...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/22', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/19', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/18` | 0.903204 | YOU MIGHT... |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/22` | 0.522471 | OTHERS PROBABLY... |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/16` | 0.362798 | IN DOWNTIME... |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/14` | 0.315405 | WHILE EXPLORING... |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/10` | 0.303473 | DURING COMBAT ENCOUNTERS... |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/48` | 0.291340 | **Trigger** You would gain the confused, controlled, fleeing,  frightened, or stupefied condition. |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/1` | 0.288704 | **Sample Mystic** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/8` | 0.282268 | **6 + Constitution modifier** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/15` | 0.280053 | **CONCENTRATE** **MYSTIC** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/12` | 0.280053 | **CONCENTRATE** **MYSTIC** |

### Query 17
- Text: Summarize Know more about the other members of your party than anyone else.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/19', 'PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/23', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/19', 'PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/20', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/19` | 1.019820 | Know more about the other members of your party than anyone else. |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/23` | 0.611174 | Think of you as the heart of your party. |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/13` | 0.475975 | Your connection shapes your perspective on the world and the way you approach  problems. When a disagreement erupts between bonded members, you're often the  one to help them talk through their proble |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/17` | 0.425345 | You reflect on your connection to deepen your understanding. You spend time  with your bonded allies, perhaps working on the same side hustle, going on a hike  together, or forming a guild in your fav |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/20` | 0.420962 | Have insights into the nature of your connection that others find unorthodox. |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/32` | 0.415008 | Your understanding of your connection transcends the limits  of other mortals, granting you access to the most powerful  spells. You gain an additional 10th-rank spell slot. |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/44` | 0.393072 | You gain a deeper understanding of your connection. You gain  the advanced epiphany spell for your chosen connection. |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/16` | 0.390080 | You always know the general distance and direction toward  other bonded creatures, their Hit Point totals, and if they're  conscious, unconscious, dying, or dead. This ability doesn't  work across pla |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/28` | 0.369067 | You've learned to protect yourself and your allies with  your weapons. You deal 2 additional damage with  weapons and unarmed attacks in which you're an  expert. This damage increases to 3 if you're a |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/27` | 0.357311 | You gain these abilities as a mystic. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |

### Query 18
- Text: Summarize Have insights into the nature of your connection that others find unorthodox.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/20', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/44', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/20', 'PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/19', 'PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/20` | 1.019673 | Have insights into the nature of your connection that others find unorthodox. |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/44` | 0.641105 | You gain a deeper understanding of your connection. You gain  the advanced epiphany spell for your chosen connection. |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/7` | 0.636761 | Plumbing the depths of your own connection, you  understand how your piece of reality interconnects  with another. You learn the advanced epiphany spell of  the connection that grants training in the |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/25` | 0.593846 | Assume you view the universe through the lens of your connection. |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/13` | 0.591126 | Your connection shapes your perspective on the world and the way you approach  problems. When a disagreement erupts between bonded members, you're often the  one to help them talk through their proble |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/7` | 0.581033 | You discover the ultimate truth of your connection and its  role as a foundation of the cosmos. You learn your chosen  connection's perfect harmony. |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/6` | 0.560206 | **Prerequisites** master in a connection skill for a connection that  you've learned the initial epiphany for and that isn't your  chosen connection |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/17` | 0.551025 | You reflect on your connection to deepen your understanding. You spend time  with your bonded allies, perhaps working on the same side hustle, going on a hike  together, or forming a guild in your fav |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/34` | 0.547294 | **Prerequisites** expert in a connection skill other than that of  your chosen connection |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/8` | 0.543132 | You see into the truth of the cosmos through your connection. You gain the greater epiphany spell for your chosen connection. |

### Query 19
- Text: Summarize Have strange visions about fundamental forces.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/21', 'PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/20', 'PZO22001 Starfinder Player Core 114-125::/page/8/Text/35']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/21', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/22', 'PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/21` | 1.007101 | Have strange visions about fundamental forces. |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/20` | 0.460682 | Have insights into the nature of your connection that others find unorthodox. |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/35` | 0.429519 | You channel strange power from beyond this reality, granting  creatures in your bond the power to reform their bodies into  powerful, aberrant shapes. You gain the *eldritch* *bond* epiphany  spell (p |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/25` | 0.381930 | Assume you view the universe through the lens of your connection. |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/2` | 0.347848 | You're a conduit, channeling the fundamental forces that connect and bind everything in the cosmos.  You can draw upon this supernatural wellspring to form deep spiritual bonds with your allies,  empo |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/6` | 0.346412 | You channel the raw power of the primordial elements that  converge to create the Universe and everything in it. You might  have a strong affinity with one or more elements, or maybe you  visited one |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/9` | 0.338655 | All mystics have a supernatural connection with a cosmic force  that grants magical powers. The exact nature of your connection  can vary widely—you might worship a god or pantheon, embody  a metaphys |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/22` | 0.329170 | You remain alert to threats around you. Your proficiency  rank for Perception increases to expert. |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/24` | 0.327081 | You win battles with basic weapons. Your proficiency rank  for simple weapons and unarmed attacks increases to expert. |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/48` | 0.326144 | **Trigger** You would gain the confused, controlled, fleeing,  frightened, or stupefied condition. |

### Query 20
- Text: Summarize OTHERS PROBABLY...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/22', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/22', 'PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/21', 'PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/22` | 0.892334 | OTHERS PROBABLY... |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/18` | 0.536970 | YOU MIGHT... |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/19` | 0.351529 | Know more about the other members of your party than anyone else. |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/14` | 0.306763 | WHILE EXPLORING... |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/35` | 0.304825 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/32` | 0.304825 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/39` | 0.281109 | **Trigger** An adjacent bonded ally takes damage. |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/12` | 0.280939 | DURING SOCIAL ENCOUNTERS... |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/10` | 0.274839 | DURING COMBAT ENCOUNTERS... |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/20` | 0.269806 | Have insights into the nature of your connection that others find unorthodox. |

### Query 21
- Text: Summarize Think of you as the heart of your party.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/23', 'PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/19', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/23', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/22', 'PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/23` | 1.011474 | Think of you as the heart of your party. |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/19` | 0.627411 | Know more about the other members of your party than anyone else. |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/13` | 0.534245 | Your connection shapes your perspective on the world and the way you approach  problems. When a disagreement erupts between bonded members, you're often the  one to help them talk through their proble |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/17` | 0.485582 | You reflect on your connection to deepen your understanding. You spend time  with your bonded allies, perhaps working on the same side hustle, going on a hike  together, or forming a guild in your fav |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/20` | 0.410378 | Have insights into the nature of your connection that others find unorthodox. |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/44` | 0.401750 | You gain a deeper understanding of your connection. You gain  the advanced epiphany spell for your chosen connection. |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/8` | 0.397433 | You see into the truth of the cosmos through your connection. You gain the greater epiphany spell for your chosen connection. |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/7` | 0.395368 | You discover the ultimate truth of your connection and its  role as a foundation of the cosmos. You learn your chosen  connection's perfect harmony. |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/14` | 0.386001 | You're connected to the fount of vitality and void energy that  flows through all living things on every planet. You weave these  energies into spells that heal your allies and harm your enemies. |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/11` | 0.383647 | You cast powerful spells that blast enemies and empower allies. You heal allies you  share a bond with by drawing on your vitality network. |

### Query 22
- Text: Summarize View your bond as a closed clique or think you're trying to recruit them.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/24', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/13', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/24', 'PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/25', 'PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/24` | 1.032697 | View your bond as a closed clique or think you're trying to recruit them. |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/13` | 0.540524 | Your connection shapes your perspective on the world and the way you approach  problems. When a disagreement erupts between bonded members, you're often the  one to help them talk through their proble |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/17` | 0.523947 | You reflect on your connection to deepen your understanding. You spend time  with your bonded allies, perhaps working on the same side hustle, going on a hike  together, or forming a guild in your fav |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/15` | 0.455292 | You form a bond between yourself and others, most typically  your closest companions. Forming bonds is different for every  mystic but always involves using a 10-minute activity related  to the mystic |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/44` | 0.453957 | You pulse energy through your bond as your ally casts a spell, empowering their spell in one of the following ways. |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/16` | 0.439431 | **Target** any number of your bonded allies within 120 feet |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/17` | 0.429732 | You force link the target's mind to your bond and share a  confusing glimpse of your connection. Attempt a skill check  with your connection skill against the Will DC of a foe you  can see within 30 f |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/55` | 0.418240 | You can speak with computers. Any construct creatures you  summon are considered part of your bond and don't count  against the maximum number of creatures in your bond. During  your daily preparation |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/1` | 0.406041 | alter the genes of creatures in your bond. You gain the *wild* *bond* epiphany spell (page 377). |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/22` | 0.404147 | You channel a surge of energy through your bond, shielding  your ally's body and mind. Your ally gains a +1 status bonus  to the triggering saving throw. If they roll a success on the  saving throw ag |

### Query 23
- Text: Summarize Assume you view the universe through the lens of your connection.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/25', 'PZO22001 Starfinder Player Core 114-125::/page/10/Text/8', 'PZO22001 Starfinder Player Core 114-125::/page/5/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/25', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/26', 'PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/25` | 1.024264 | Assume you view the universe through the lens of your connection. |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/8` | 0.682058 | You see into the truth of the cosmos through your connection. You gain the greater epiphany spell for your chosen connection. |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/7` | 0.644081 | You discover the ultimate truth of your connection and its  role as a foundation of the cosmos. You learn your chosen  connection's perfect harmony. |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/20` | 0.599157 | Have insights into the nature of your connection that others find unorthodox. |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/35` | 0.556875 | Through dedication or serendipity, you've branched out to  explore other connections to the fundamental building blocks of  the cosmos. You learn the initial epiphany spell of a connection  that grant |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/44` | 0.554371 | You gain a deeper understanding of your connection. You gain  the advanced epiphany spell for your chosen connection. |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/7` | 0.553393 | Plumbing the depths of your own connection, you  understand how your piece of reality interconnects  with another. You learn the advanced epiphany spell of  the connection that grants training in the |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/2` | 0.552398 | You're a conduit, channeling the fundamental forces that connect and bind everything in the cosmos.  You can draw upon this supernatural wellspring to form deep spiritual bonds with your allies,  empo |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/13` | 0.526335 | Your connection shapes your perspective on the world and the way you approach  problems. When a disagreement erupts between bonded members, you're often the  one to help them talk through their proble |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/11` | 0.522653 | Your connection is a mystical force that grants you magic. It  could come from a divine patron, manifestation of a primeval  cosmic force, or some other mystery. Your connection  determines your spell |

### Query 24
- Text: What is the rule about CLASS FEATURES?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/26', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/387', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/33']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/26', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/27', 'PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/25']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/ListItem/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/26` | 0.841653 | CLASS FEATURES |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/387` | 0.758361 | Class Features |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/33` | 0.537843 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/34` | 0.507843 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/34` | 0.507843 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/58` | 0.507843 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/22` | 0.507843 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/36` | 0.507843 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/2` | 0.440904 | You'll see the following key terms in many mystic class  features. |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/4` | 0.440561 | **Attributes** |

### Query 25
- Text: What is the rule about You gain these abilities as a mystic. Abilities gained at higher levels list the level at  which you gain them next to the features' names.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/27', 'PZO22001 Starfinder Player Core 114-125::/page/6/Text/2', 'PZO22001 Starfinder Player Core 114-125::/page/2/Table/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/27', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/26', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/28']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/27` | 0.974952 | You gain these abilities as a mystic. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/2` | 0.683122 | You'll see the following key terms in many mystic class  features. |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/Table/2` | 0.675589 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, connection, initial epiphany, mystic bond, vitality network, mystic spellcasting, spell repertoire2Mystic fea |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/19` | 0.630176 | At 2nd level and every even-numbered level, you gain a mystic  class feat. These begin on page 121. |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/13` | 0.626887 | You add to this spell repertoire as you increase in level. Each  time you get a spell slot (see Mystic Spells per Day on page  119), you add a spell of the same rank to your spell repertoire. |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/11` | 0.613229 | At every level that you gain a mystic feat, you can select one  of the following feats. You must satisfy any prerequisites  before selecting the feat. |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/427` | 0.589151 | Attribute boosts, mystic feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/407` | 0.589151 | Attribute boosts, mystic feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/2` | 0.581921 | Use this table to look up mystic feats by name. |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/5` | 0.581666 | As you increase in level as a mystic, your number of spells  per day increases, as does the highest rank of spells you can  cast, as shown on the Mystic Spells per Day table on page 119. |

### Query 26
- Text: What is the rule about ANCESTRY AND BACKGROUND?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/28', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/32', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/35']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/28', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/27', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/28` | 0.928306 | ANCESTRY AND BACKGROUND |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/32` | 0.739658 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/35` | 0.739658 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/21` | 0.492053 | **INTRODUCTION** **ANCESTRIES & ** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/33` | 0.492053 | **INTRODUCTION** **ANCESTRIES & ** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/33` | 0.492053 | **INTRODUCTION** **ANCESTRIES & ** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/57` | 0.492053 | **INTRODUCTION** **ANCESTRIES & ** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/50` | 0.449777 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/38` | 0.449777 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/76` | 0.449777 | **BACKGROUNDS** |

### Query 27
- Text: What is the rule about In addition to what you get from your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/29', 'PZO22001 Starfinder Player Core 114-125::/page/4/Text/13', 'PZO22001 Starfinder Player Core 114-125::/page/2/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/29', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/28', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/31']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/29` | 0.963223 | In addition to what you get from your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/13` | 0.623303 | In addition to the initial ancestry feat you started with,  you gain an ancestry feat at 5th level and every 4 levels  thereafter. The list of ancestry feats available to you can be  found in your anc |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/7` | 0.598690 | At 1st level, you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start  of this class. |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/6` | 0.532424 | At 1st level, your class gives you  an attribute boost to Wisdom. |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/4` | 0.530786 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/2/Table/2` | 0.504675 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, connection, initial epiphany, mystic bond, vitality network, mystic spellcasting, spell repertoire2Mystic fea |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/51` | 0.494730 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/397` | 0.493127 | 3rd-rank spells, ancestry feat, attribute boosts, fortitude expertise, skill increase |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/14` | 0.479497 | When you gain access to a new rank of spells, your first new  spell is always the spell granted by your chosen connection,  but you can choose the other spells. At 2nd level, you select  another 1st-r |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/389` | 0.470952 | Ancestry and background, attribute boosts, initial proficiencies, connection, initial epiphany, mystic bond, vitality network, mystic spellcasting, spell repertoire |

### Query 28
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/31', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/34', 'PZO22001 Starfinder Player Core 114-125::/page/3/Text/50']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/31', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/29', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/32']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/32` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/31` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/34` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/50` | 0.611679 | **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/49` | 0.569679 | **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/38` | 0.569679 | **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/76` | 0.569679 | **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/73` | 0.524467 | **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/33` | 0.507539 | **INTRODUCTION** **ANCESTRIES & ** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/33` | 0.495539 | **INTRODUCTION** **ANCESTRIES & ** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/57` | 0.495539 | **INTRODUCTION** **ANCESTRIES & ** |

### Query 29
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/32', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/35', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/28']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/32', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/35', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/33', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/31']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/11/Text/35` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/32` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/35` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/28` | 0.768682 | ANCESTRY AND BACKGROUND |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/21` | 0.672101 | **INTRODUCTION** **ANCESTRIES & ** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/33` | 0.672101 | **INTRODUCTION** **ANCESTRIES & ** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/33` | 0.672101 | **INTRODUCTION** **ANCESTRIES & ** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/57` | 0.672101 | **INTRODUCTION** **ANCESTRIES & ** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/50` | 0.594354 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/49` | 0.594354 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/38` | 0.594354 | **BACKGROUNDS** |

### Query 30
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/33']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/33', 'PZO22001 Starfinder Player Core 114-125::/page/5/Text/22', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/58']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/33', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/36', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/58', 'PZO22001 Starfinder Player Core 114-125::/page/7/Text/34', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/32', 'PZO22001 Starfinder Player Core 114-125::/page/3/Text/34', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/34', 'PZO22001 Starfinder Player Core 114-125::/page/5/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/11/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/9/Text/58` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/7/Text/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/3/Text/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/5/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/33` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/58` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/22` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/34` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/34` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/36` | 0.910061 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/26` | 0.573477 | CLASS FEATURES |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/65` | 0.515930 | **CLASS DC** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/387` | 0.498036 | Class Features |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/6` | 0.476046 | **Skills** |

### Query 31
- Text: Summarize **Envoy**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/34']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/3/Text/35', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/34', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/37']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/34', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/33', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/35']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/35` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/35` | 0.951326 | **Envoy** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/34` | 0.951326 | **Envoy** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/37` | 0.951326 | **Envoy** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/23` | 0.909326 | **Envoy** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/59` | 0.909326 | **Envoy** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/35` | 0.909326 | **Envoy** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/73` | 0.382028 | **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/63` | 0.364330 | **Soldier** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/39` | 0.364330 | **Soldier** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/27` | 0.364330 | **Soldier** |

### Query 32
- Text: Summarize **Mystic**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/7/Text/36', 'PZO22001 Starfinder Player Core 114-125::/page/5/Text/24', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/60']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/35', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/36', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/34']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/34` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/36` | 0.959378 | **Mystic** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/24` | 0.959378 | **Mystic** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/60` | 0.959378 | **Mystic** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/35` | 0.917378 | **Mystic** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/38` | 0.917378 | **Mystic** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/36` | 0.917378 | **Mystic** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/1` | 0.844789 | **Sample Mystic** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/20` | 0.745497 | **MYSTIC** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/25` | 0.745497 | **MYSTIC** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/28` | 0.745497 | **MYSTIC** |

### Query 33
- Text: Summarize **Operative **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/36']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/7/Text/37', 'PZO22001 Starfinder Player Core 114-125::/page/5/Text/25', 'PZO22001 Starfinder Player Core 114-125::/page/3/Text/37']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/36', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/37', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/35']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/37` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/35` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/37` | 0.958402 | **Operative ** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/25` | 0.958402 | **Operative ** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/37` | 0.958402 | **Operative ** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/61` | 0.916402 | **Operative ** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/36` | 0.916402 | **Operative ** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/6/SectionHeader/1` | 0.361666 | **KEY TERMS** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/3` | 0.359222 | **ADAPTIVE DEFENSE **[one-action] **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/20` | 0.358452 | **WASTE NOT **[one-action] **FEAT 4** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/27` | 0.345470 | **Soldier** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/40` | 0.345470 | **Soldier** |

### Query 34
- Text: Summarize **Solarian**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/37']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/3/Text/38', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/37', 'PZO22001 Starfinder Player Core 114-125::/page/5/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/37', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/36', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/39']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/39` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/38` | 0.974700 | **Solarian** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/37` | 0.974700 | **Solarian** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/26` | 0.974700 | **Solarian** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/62` | 0.932700 | **Solarian** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/38` | 0.932700 | **Solarian** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/39` | 0.932700 | **Solarian** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/27` | 0.471086 | **Soldier** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/39` | 0.471086 | **Soldier** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/39` | 0.471086 | **Soldier** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/63` | 0.459086 | **Soldier** |

### Query 35
- Text: Summarize **Soldier**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/39', 'PZO22001 Starfinder Player Core 114-125::/page/3/Text/39', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/40']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/39', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/37', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/40']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/37` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/40` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/39` | 0.953061 | **Soldier** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/39` | 0.953061 | **Soldier** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/40` | 0.953061 | **Soldier** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/27` | 0.911061 | **Soldier** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/39` | 0.911061 | **Soldier** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/63` | 0.911061 | **Soldier** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/6` | 0.463308 | **Skills** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/39` | 0.454360 | **Solarian** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/37` | 0.454360 | **Solarian** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/38` | 0.454360 | **Solarian** |

### Query 36
- Text: Summarize **Witchwarper**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/40']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/5/Text/28', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/40', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/64']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/40', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/41', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/39']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/41` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/39` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/28` | 0.988715 | **Witchwarper** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/40` | 0.988715 | **Witchwarper** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/64` | 0.988715 | **Witchwarper** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/40` | 0.946715 | **Witchwarper** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/41` | 0.946715 | **Witchwarper** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/40` | 0.808939 | **Witchwarper** **Archetypes** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/11` | 0.356244 | **1st:** *heal*, *mind skewer*, *mystic armor*; **Cantrips** *daze*,  *eldritch lance*, *guidance*, *stabilize* |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/6` | 0.345863 | **Skills** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/39` | 0.342425 | **Soldier** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/27` | 0.342425 | **Soldier** |

### Query 37
- Text: Summarize **Archetypes**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/41', 'PZO22001 Starfinder Player Core 114-125::/page/3/Text/41', 'PZO22001 Starfinder Player Core 114-125::/page/5/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/41', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/42', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/40']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/40` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/41` | 0.973323 | **Archetypes** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/41` | 0.973323 | **Archetypes** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/29` | 0.973323 | **Archetypes** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/42` | 0.931323 | **Archetypes** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/65` | 0.931323 | **Archetypes** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/40` | 0.668054 | **Witchwarper** **Archetypes** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/4` | 0.431887 | **Attributes** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/15` | 0.399914 | **Order **Plant; **Skill** Plant Lore; **Spells** 1st: *summon* *plant* *or* *fungus*; 2nd: *verdant* *code*; 5th: *plant form* |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/11` | 0.393190 | **1st:** *heal*, *mind skewer*, *mystic armor*; **Cantrips** *daze*,  *eldritch lance*, *guidance*, *stabilize* |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/73` | 0.382400 | **INDEX** |

### Query 38
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/42']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/9/Text/66', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/56', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/42']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/42', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/43', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/41']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/43` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/41` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/66` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/56` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/42` | 0.864442 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/41` | 0.651094 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/42` | 0.651094 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/30` | 0.651094 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/6` | 0.640740 | **Skills** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/13` | 0.450539 | the listed skill, you instead become trained in another skill of  your choice. |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/22` | 0.446689 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/9` | 0.431076 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use an increase to either become trained in  one skill you're untrained in or to increase your proficiency  in one skill |

### Query 39
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/43']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/11/Text/43', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/67', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/43']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/43', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/42', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/44']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/44` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/43` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/67` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/43` | 0.871817 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/41` | 0.653037 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/42` | 0.653037 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/30` | 0.653037 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/569` | 0.619086 | Feat |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/525` | 0.619086 | Feat |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/8` | 0.515296 | **Connection and Feats** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/34` | 0.439647 | FEAT 12 |

### Query 40
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/44', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/68', 'PZO22001 Starfinder Player Core 114-125::/page/7/Text/42']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/44', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/43', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/45']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/43` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/45` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/44` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/68` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/42` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/43` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/31` | 0.902726 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/44` | 0.902726 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/73` | 0.421643 | **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/38` | 0.409329 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/49` | 0.409329 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/50` | 0.409329 | **BACKGROUNDS** |

### Query 41
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/45']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/45', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/63', 'PZO22001 Starfinder Player Core 114-125::/page/3/Text/44']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/45', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/46', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/44']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/46` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/44` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/45` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/63` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/44` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/45` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/43` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/32` | 0.847304 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/69` | 0.847304 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/10/SectionHeader/40` | 0.587542 | BOND SPELL ? |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/3/SectionHeader/29` | 0.585535 | **NETWORK SPELL **[one-action] |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/10/SectionHeader/47` | 0.574605 | INFUSED SPELL * |

### Query 42
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/46']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/46', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/46', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/70']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/46', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/45', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/47']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/45` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/47` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/46` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/46` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/70` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/45` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/44` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/33` | 0.811006 | **PLAYING THE ** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/39` | 0.663024 | **GAME** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/31` | 0.418586 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/34` | 0.418586 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/15` | 0.390371 | **Order **Plant; **Skill** Plant Lore; **Spells** 1st: *summon* *plant* *or* *fungus*; 2nd: *verdant* *code*; 5th: *plant form* |

### Query 43
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/47']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/47', 'PZO22001 Starfinder Player Core 114-125::/page/7/Text/45', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/71']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/47', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/47', 'PZO22001 Starfinder Player Core 114-125::/page/7/Text/45', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/46', 'PZO22001 Starfinder Player Core 114-125::/page/5/Text/34', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/48', 'PZO22001 Starfinder Player Core 114-125::/page/3/Text/46', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/71']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/11/Text/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/7/Text/45` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/46` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/5/Text/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/48` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/3/Text/46` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/9/Text/71` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/47` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/45` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/71` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/34` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/46` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/47` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/4` | 0.463693 | **Attributes** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/6/SectionHeader/1` | 0.439047 | **KEY TERMS** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/73` | 0.423722 | **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/35` | 0.416141 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 44
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/48']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/11/Text/48', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/48', 'PZO22001 Starfinder Player Core 114-125::/page/5/Text/35']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/48', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/49', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/47']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/47` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/48` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/48` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/35` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/47` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/46` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/72` | 0.804819 | **GLOSSARY & ** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/73` | 0.618357 | **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/34` | 0.385404 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/34` | 0.385404 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/22` | 0.385404 | **CLASSES** |

### Query 45
- Text: What is the rule about **CHARACTER ** **SHEET**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/49']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/49', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/41', 'PZO22001 Starfinder Player Core 114-125::/page/3/Text/41']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/49', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/50', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/48']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/50` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/48` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/49` | 0.859300 | **CHARACTER ** **SHEET** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/41` | 0.434353 | **Archetypes** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/41` | 0.434353 | **Archetypes** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/29` | 0.392353 | **Archetypes** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/42` | 0.392353 | **Archetypes** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/65` | 0.392353 | **Archetypes** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/39` | 0.380766 | **GAME** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/6` | 0.371280 | **Skills** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/42` | 0.369339 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/41` | 0.357339 | **SKILLS** **FEATS** |

### Query 46
- Text: Summarize **INITIAL PROFICIENCIES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/50']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/50', 'PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/6', 'PZO22001 Starfinder Player Core 114-125::/page/2/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/50', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/49', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/51']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/51` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/50` | 1.001056 | **INITIAL PROFICIENCIES** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/6` | 0.851001 | INITIAL PROFICIENCIES |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/7` | 0.516203 | At 1st level, you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start  of this class. |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/22` | 0.418278 | **Tradition** primal; **Connection Skill** Performance |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/31` | 0.400378 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/34` | 0.400378 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/6` | 0.396641 | **Skills** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/29` | 0.382691 | **Prerequisites** connection with primal spellcasting |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/4` | 0.382691 | **Prerequisites** connection with primal spellcasting |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/44` | 0.382691 | **Prerequisites** connection with primal spellcasting |

### Query 47
- Text: What is the rule about At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/51']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/51', 'PZO22001 Starfinder Player Core 114-125::/page/2/Text/7', 'PZO22001 Starfinder Player Core 114-125::/page/4/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/51', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/50', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/52']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/50` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/52` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/51` | 0.992024 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/7` | 0.706615 | At 1st level, you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start  of this class. |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/9` | 0.695602 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use an increase to either become trained in  one skill you're untrained in or to increase your proficiency  in one skill |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/22` | 0.579477 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/24` | 0.558981 | You win battles with basic weapons. Your proficiency rank  for simple weapons and unarmed attacks increases to expert. |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/13` | 0.538962 | the listed skill, you instead become trained in another skill of  your choice. |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/22` | 0.523184 | You remain alert to threats around you. Your proficiency  rank for Perception increases to expert. |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/10` | 0.508602 | At 7th level, you can use skill increases to become a  master in a skill in which you're already an expert, and at  15th level, you can use them to become legendary in a skill  in which you're already |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/31` | 0.503413 | You become trained in the listed skill associated with the  order and add the listed spells to your spell list and spell  repertoire as signature spells. If you were already trained in |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/14` | 0.498603 | When you gain access to a new rank of spells, your first new  spell is always the spell granted by your chosen connection,  but you can choose the other spells. At 2nd level, you select  another 1st-r |

### Query 48
- Text: Summarize **PERCEPTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/52']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/52', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/53', 'PZO22001 Starfinder Player Core 114-125::/page/4/SectionHeader/21']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/52', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/53', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/51']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/53` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/51` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/52` | 0.934058 | **PERCEPTION** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/53` | 0.583165 | Trained in Perception |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/4/SectionHeader/21` | 0.533791 | PERCEPTION EXPERTISE 11TH |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/31` | 0.443002 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/34` | 0.443002 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/38` | 0.438809 | **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/50` | 0.438809 | **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/49` | 0.438809 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/76` | 0.438809 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/22` | 0.431666 | You remain alert to threats around you. Your proficiency  rank for Perception increases to expert. |

### Query 49
- Text: Summarize Trained in Perception
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/53']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/53', 'PZO22001 Starfinder Player Core 114-125::/page/4/Text/22', 'PZO22001 Starfinder Player Core 114-125::/page/4/SectionHeader/21']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/53', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/52', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/54']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/52` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/54` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/53` | 0.944339 | Trained in Perception |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/22` | 0.582133 | You remain alert to threats around you. Your proficiency  rank for Perception increases to expert. |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/4/SectionHeader/21` | 0.516135 | PERCEPTION EXPERTISE 11TH |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/52` | 0.476849 | **PERCEPTION** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/55` | 0.454774 | Trained in Fortitude Trained in Reflex Expert in Will |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/57` | 0.438715 | Trained in one skill determined by  your connection |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/60` | 0.435404 | Trained in simple weapons Trained in unarmed attacks |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/62` | 0.434440 | Trained in light armor Trained in unarmored defense |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/13` | 0.416676 | the listed skill, you instead become trained in another skill of  your choice. |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/31` | 0.403520 | You become trained in the listed skill associated with the  order and add the listed spells to your spell list and spell  repertoire as signature spells. If you were already trained in |

### Query 50
- Text: What is the rule about **SAVING THROWS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/54']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/54', 'PZO22001 Starfinder Player Core 114-125::/page/8/Text/22', 'PZO22001 Starfinder Player Core 114-125::/page/8/Text/21']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/54', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/53', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/55']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/53` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/55` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/54` | 0.904955 | **SAVING THROWS** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/22` | 0.438626 | You channel a surge of energy through your bond, shielding  your ally's body and mind. Your ally gains a +1 status bonus  to the triggering saving throw. If they roll a success on the  saving throw ag |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/21` | 0.415586 | **Trigger** A bonded ally within 20 feet is about to roll a saving  throw. |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/25` | 0.341936 | **Perfect Harmony** The first time each round you Transfer  Vitality, the target who regained Hit Points can Stride as a  free action. This has the traversal trait. |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/19` | 0.277190 | **Success** As critical success, but the penalty to Will saves is –1. **Critical Failure** You become off-guard against the next attack  the target attempts against you before the end of your  next tu |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/18` | 0.276057 | **Critical Success** The target takes a –1 status penalty to attack  rolls and a –2 status penalty to Will saves for 1 minute.  This effect ends early if it uses a single action with the  concentrate |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/3/SectionHeader/16` | 0.267209 | Swapping Spells in Your Repertoire |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/21` | 0.265518 | **Prerequisites** shadow connection |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/31` | 0.260785 | **Harmony** When you Transfer Vitality, the target's shadow  darkens and swells, reducing bright light within a 10 foot emanation of the target to dim light. This is a form  of magical darkness and ca |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/20` | 0.258098 | The links to your connection and your bonded companions  bolster your soul against doubt. Your proficiency rank for  Will saves increases to master. When you roll a success on  a Will save, you get a |

### Query 51
- Text: Summarize Trained in Fortitude Trained in Reflex Expert in Will
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/55']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/55', 'PZO22001 Starfinder Player Core 114-125::/page/4/Text/3', 'PZO22001 Starfinder Player Core 114-125::/page/4/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/55', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/56', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/54']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/56` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/54` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/55` | 1.022599 | Trained in Fortitude Trained in Reflex Expert in Will |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/3` | 0.568701 | Your connection blesses you with insight that helps you  dodge danger. Your proficiency rank for Reflex saves  increases to expert. |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/15` | 0.534829 | Your physique has grown hardier from your adventures.  Your proficiency rank for Fortitude saves increases  to expert. |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/4/SectionHeader/1` | 0.488853 | REFLEX EXPERTISE 3RD |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/4/SectionHeader/14` | 0.466026 | FORTITUDE EXPERTISE 5TH |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/53` | 0.458539 | Trained in Perception |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/22` | 0.449646 | You remain alert to threats around you. Your proficiency  rank for Perception increases to expert. |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/397` | 0.446737 | 3rd-rank spells, ancestry feat, attribute boosts, fortitude expertise, skill increase |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/62` | 0.437578 | Trained in light armor Trained in unarmored defense |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/393` | 0.424781 | 2nd-rank spells, general feat, group chat, reflex expertise, signature spells, skill increase |

### Query 52
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/56']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/9/Text/66', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/56', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/42']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/56', 'PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/6', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/55', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/57']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/55` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/57` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/66` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/56` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/42` | 0.864442 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/41` | 0.651094 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/42` | 0.651094 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/30` | 0.651094 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/6` | 0.640740 | **Skills** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/13` | 0.450539 | the listed skill, you instead become trained in another skill of  your choice. |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/22` | 0.446689 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/9` | 0.431076 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use an increase to either become trained in  one skill you're untrained in or to increase your proficiency  in one skill |

### Query 53
- Text: What is the rule about Trained in one skill determined by  your connection?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/57']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/57', 'PZO22001 Starfinder Player Core 114-125::/page/8/Text/13', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/57', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/56', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/58']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/56` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/58` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/57` | 0.899740 | Trained in one skill determined by  your connection |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/13` | 0.654380 | the listed skill, you instead become trained in another skill of  your choice. |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/6` | 0.624519 | **Prerequisites** master in a connection skill for a connection that  you've learned the initial epiphany for and that isn't your  chosen connection |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/34` | 0.580586 | **Prerequisites** expert in a connection skill other than that of  your chosen connection |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/7` | 0.522658 | Plumbing the depths of your own connection, you  understand how your piece of reality interconnects  with another. You learn the advanced epiphany spell of  the connection that grants training in the |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/9` | 0.515153 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use an increase to either become trained in  one skill you're untrained in or to increase your proficiency  in one skill |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/10` | 0.513135 | might interpret the source of their powers differently. At 1st level,  choose your connection. Your chosen connection determines the  type of spells you cast and the spell tradition you choose spells |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/11` | 0.509414 | Your connection is a mystical force that grants you magic. It  could come from a divine patron, manifestation of a primeval  cosmic force, or some other mystery. Your connection  determines your spell |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/22` | 0.494853 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/51` | 0.486666 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |

### Query 54
- Text: What is the rule about Trained in a number of additional  skills equal to 3 plus your Intelligence  modifier?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/58']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/58', 'PZO22001 Starfinder Player Core 114-125::/page/4/Text/9', 'PZO22001 Starfinder Player Core 114-125::/page/8/Text/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/58', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/59', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/57']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/59` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/57` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/58` | 0.919891 | Trained in a number of additional  skills equal to 3 plus your Intelligence  modifier |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/9` | 0.631139 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use an increase to either become trained in  one skill you're untrained in or to increase your proficiency  in one skill |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/13` | 0.561868 | the listed skill, you instead become trained in another skill of  your choice. |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/10` | 0.499697 | At 7th level, you can use skill increases to become a  master in a skill in which you're already an expert, and at  15th level, you can use them to become legendary in a skill  in which you're already |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/22` | 0.495805 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/7` | 0.491607 | SKILL INCREASES 3RD |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/31` | 0.486686 | You become trained in the listed skill associated with the  order and add the listed spells to your spell list and spell  repertoire as signature spells. If you were already trained in |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/57` | 0.472959 | Trained in one skill determined by  your connection |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/5` | 0.463736 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/17` | 0.456778 | You've formed a more powerful bond with your connection.  Your proficiency ranks for spell attack modifiers and spell  DCs increase to expert. |

### Query 55
- Text: What is the rule about **ATTACKS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/59']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/59', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/29', 'PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/59', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/58', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/60']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/58` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/60` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/59` | 0.855189 | **ATTACKS** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/29` | 0.554998 | **Trigger** You're hit by an attack. |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/13` | 0.389454 | **NETWORK ATTUNEMENT **[one-action] **FEAT 18** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/60` | 0.353949 | Trained in simple weapons Trained in unarmed attacks |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/6` | 0.347430 | Some of your spells require you to attempt a spell attack to  see how effective they are or have your enemies roll against  your spell DC (typically by attempting a saving throw). Since  your key attr |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/17` | 0.346569 | **Trigger** An enemy targets a bonded creature with a Strike or spell with an attack roll that has an elemental trait and the roll fails or critically fails, or you roll a critical success on a save a |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/4` | 0.345033 | **KEY ATTRIBUTE** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/61` | 0.342350 | **DEFENSES** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/11` | 0.329458 | **Harmony** When you Transfer Vitality, choose an elemental  trait: air, earth, fire, metal, water, or wood. If one or more  of your elemental epiphanies are active, you must select  the elemental tra |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/39` | 0.329423 | **GAME** |

### Query 56
- Text: What is the rule about Trained in simple weapons Trained in unarmed attacks?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/60']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/60', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/62', 'PZO22001 Starfinder Player Core 114-125::/page/4/Text/24']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/60', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/61', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/59']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/61` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/59` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/60` | 0.914369 | Trained in simple weapons Trained in unarmed attacks |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/62` | 0.691830 | Trained in light armor Trained in unarmored defense |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/24` | 0.620360 | You win battles with basic weapons. Your proficiency rank  for simple weapons and unarmed attacks increases to expert. |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/13` | 0.484246 | the listed skill, you instead become trained in another skill of  your choice. |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/28` | 0.446465 | You've learned to protect yourself and your allies with  your weapons. You deal 2 additional damage with  weapons and unarmed attacks in which you're an  expert. This damage increases to 3 if you're a |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/64` | 0.440222 | Trained in spell attack modifier Trained in spell DC |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/57` | 0.432649 | Trained in one skill determined by  your connection |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/51` | 0.407431 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/26` | 0.401904 | The bonds you've forged protect you like supernatural  armor. Your proficiency rank in light armor and unarmored  defense increases to expert. |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/9` | 0.388275 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use an increase to either become trained in  one skill you're untrained in or to increase your proficiency  in one skill |

### Query 57
- Text: Summarize **DEFENSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/61']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/61', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/3', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/527']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/61', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/62', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/60']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/62` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/60` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/61` | 0.959826 | **DEFENSES** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/3` | 0.632700 | **ADAPTIVE DEFENSE **[one-action] **FEAT 4** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/527` | 0.546194 | Adaptive Defense |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/31` | 0.411981 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/34` | 0.411981 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/62` | 0.408873 | Trained in light armor Trained in unarmored defense |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/6` | 0.406384 | **Skills** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/49` | 0.400430 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/50` | 0.400430 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/76` | 0.400430 | **BACKGROUNDS** |

### Query 58
- Text: Summarize Trained in light armor Trained in unarmored defense
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/62']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/62', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/60', 'PZO22001 Starfinder Player Core 114-125::/page/4/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/62', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/61', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/63']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/61` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/63` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/62` | 1.027002 | Trained in light armor Trained in unarmored defense |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/60` | 0.779166 | Trained in simple weapons Trained in unarmed attacks |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/26` | 0.623810 | The bonds you've forged protect you like supernatural  armor. Your proficiency rank in light armor and unarmored  defense increases to expert. |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/13` | 0.477304 | the listed skill, you instead become trained in another skill of  your choice. |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/24` | 0.452756 | You win battles with basic weapons. Your proficiency rank  for simple weapons and unarmed attacks increases to expert. |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/28` | 0.441614 | You've learned to protect yourself and your allies with  your weapons. You deal 2 additional damage with  weapons and unarmed attacks in which you're an  expert. This damage increases to 3 if you're a |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/64` | 0.431980 | Trained in spell attack modifier Trained in spell DC |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/57` | 0.403678 | Trained in one skill determined by  your connection |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/51` | 0.403115 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/55` | 0.399383 | Trained in Fortitude Trained in Reflex Expert in Will |

### Query 59
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/63']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/45', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/63', 'PZO22001 Starfinder Player Core 114-125::/page/3/Text/44']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/63', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/64', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/62']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/64` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/62` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/45` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/63` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/44` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/45` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/43` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/32` | 0.847304 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/69` | 0.847304 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/10/SectionHeader/40` | 0.587542 | BOND SPELL ? |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/3/SectionHeader/29` | 0.585535 | **NETWORK SPELL **[one-action] |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/10/SectionHeader/47` | 0.574605 | INFUSED SPELL * |

### Query 60
- Text: What is the rule about Trained in spell attack modifier Trained in spell DC?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/64']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/64', 'PZO22001 Starfinder Player Core 114-125::/page/3/Text/6', 'PZO22001 Starfinder Player Core 114-125::/page/4/Text/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/64', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/63', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/65']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/63` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/65` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/64` | 0.929793 | Trained in spell attack modifier Trained in spell DC |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/6` | 0.685990 | Some of your spells require you to attempt a spell attack to  see how effective they are or have your enemies roll against  your spell DC (typically by attempting a saving throw). Since  your key attr |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/31` | 0.657392 | You channel magic through your connection.  Your proficiency ranks for spell attack  modifiers and spell DCs increase to master. |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/17` | 0.585577 | You've formed a more powerful bond with your connection.  Your proficiency ranks for spell attack modifiers and spell  DCs increase to expert. |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/5` | 0.569142 | Magic flows through your every pore. Your proficiency ranks  for spell attack modifiers and spell DCs increase to legendary. |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/66` | 0.511613 | Trained in mystic class DC |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/15` | 0.493962 | As a disciple of a god, you wield some of their divine power.  You become trained in the listed divine skill associated with  the deity and add the listed cleric spells (pages 35–39) to  your spell li |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/31` | 0.482491 | You become trained in the listed skill associated with the  order and add the listed spells to your spell list and spell  repertoire as signature spells. If you were already trained in |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/58` | 0.476915 | Trained in a number of additional  skills equal to 3 plus your Intelligence  modifier |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/60` | 0.465253 | Trained in simple weapons Trained in unarmed attacks |

### Query 61
- Text: What is the rule about **CLASS DC**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/65']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/65', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/33', 'PZO22001 Starfinder Player Core 114-125::/page/3/Text/34']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/65', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/66', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/64']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/66` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/64` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/65` | 0.881905 | **CLASS DC** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/33` | 0.521525 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/34` | 0.521525 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/58` | 0.491525 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/34` | 0.491525 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/22` | 0.491525 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/36` | 0.491525 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/66` | 0.408075 | Trained in mystic class DC |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/26` | 0.381301 | CLASS FEATURES |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/64` | 0.357379 | Trained in spell attack modifier Trained in spell DC |

### Query 62
- Text: What is the rule about Trained in mystic class DC?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/66']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/66', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/64', 'PZO22001 Starfinder Player Core 114-125::/page/3/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/66', 'PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/65']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/65` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/66` | 0.879985 | Trained in mystic class DC |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/64` | 0.586679 | Trained in spell attack modifier Trained in spell DC |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/19` | 0.540349 | At 2nd level and every even-numbered level, you gain a mystic  class feat. These begin on page 121. |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/15` | 0.490301 | As a disciple of a god, you wield some of their divine power.  You become trained in the listed divine skill associated with  the deity and add the listed cleric spells (pages 35–39) to  your spell li |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/2` | 0.483709 | You'll see the following key terms in many mystic class  features. |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/31` | 0.451108 | You channel magic through your connection.  Your proficiency ranks for spell attack  modifiers and spell DCs increase to master. |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/24` | 0.435049 | **Mystic** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/36` | 0.435049 | **Mystic** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/36` | 0.435049 | **Mystic** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/60` | 0.435049 | **Mystic** |

### Query 63
- Text: Summarize **MYSTIC ADVANCEMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/25', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/66', 'PZO22001 Starfinder Player Core 114-125::/page/2/Table/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/1/Text/66` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/Table/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/1` | 1.003068 | **MYSTIC ADVANCEMENT** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/25` | 0.740326 | **MYSTIC** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/5` | 0.740326 | **MYSTIC** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/10` | 0.698326 | **MYSTIC** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/20` | 0.698326 | **MYSTIC** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/33` | 0.698326 | **MYSTIC** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/43` | 0.698326 | **MYSTIC** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/30` | 0.698326 | **MYSTIC** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/28` | 0.698326 | **MYSTIC** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/38` | 0.698326 | **MYSTIC** |

### Query 64
- Text: Lookup values for Your LevelClass Features1Ancestry and background, attribute boosts,
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/Table/2']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/1/Text/29', 'PZO22001 Starfinder Player Core 114-125::/page/2/Table/2', 'PZO22001 Starfinder Player Core 114-125::/page/2/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/Table/2', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/386', 'PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/386` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/29` | 0.671822 | In addition to what you get from your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/Table/2` | 0.641388 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, connection, initial epiphany, mystic bond, vitality network, mystic spellcasting, spell repertoire2Mystic fea |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/4` | 0.624096 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/5` | 0.545659 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/6` | 0.531244 | At 1st level, your class gives you  an attribute boost to Wisdom. |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/387` | 0.528105 | Class Features |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/13` | 0.505494 | In addition to the initial ancestry feat you started with,  you gain an ancestry feat at 5th level and every 4 levels  thereafter. The list of ancestry feats available to you can be  found in your anc |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/397` | 0.489647 | 3rd-rank spells, ancestry feat, attribute boosts, fortitude expertise, skill increase |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/4` | 0.480214 | **Attributes** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/26` | 0.480165 | CLASS FEATURES |

### Query 65
- Text: Summarize Your Level
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/386']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/386', 'PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/863', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/570']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/386', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/387', 'PZO22001 Starfinder Player Core 114-125::/page/2/Table/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/387` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/Table/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/386` | 0.853813 | Your Level |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/863` | 0.853813 | Your Level |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/570` | 0.729099 | Level |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/526` | 0.687099 | Level |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/17` | 0.549996 | 2ND LEVEL |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/2` | 0.534036 | 4TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/12` | 0.523376 | 18TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/40` | 0.514596 | 8TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/10/SectionHeader/39` | 0.513306 | 14TH LEVEL |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/10/SectionHeader/51` | 0.501266 | 16TH LEVEL |

### Query 66
- Text: What is the rule about Class Features?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/387']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/387', 'PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/26', 'PZO22001 Starfinder Player Core 114-125::/page/6/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/387', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/386', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/388']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/386` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/388` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/387` | 0.835742 | Class Features |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/26` | 0.700239 | CLASS FEATURES |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/2` | 0.520204 | You'll see the following key terms in many mystic class  features. |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/4` | 0.414280 | **Attributes** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/22` | 0.407880 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/58` | 0.407880 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/34` | 0.407880 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/36` | 0.407880 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/33` | 0.407880 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/34` | 0.407880 | **CLASSES** |

### Query 67
- Text: Summarize 1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/388']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/608', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/588', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/604']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/388', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/387', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/389']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/387` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/389` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/604` | 0.669108 | 1 |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/608` | 0.669108 | 1 |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/588` | 0.669108 | 1 |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/875` | 0.627108 | 1 |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/554` | 0.627108 | 1 |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/388` | 0.627108 | 1 |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/532` | 0.513765 | 2 |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/887` | 0.513765 | 2 |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/536` | 0.513765 | 2 |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/592` | 0.513765 | 2 |

### Query 68
- Text: What is the rule about Ancestry and background, attribute boosts,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/389']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/397', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/29', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/389']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/389', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/390', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/388']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/390` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/388` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/397` | 0.590951 | 3rd-rank spells, ancestry feat, attribute boosts, fortitude expertise, skill increase |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/29` | 0.581688 | In addition to what you get from your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/389` | 0.581218 | Ancestry and background, attribute boosts, initial proficiencies, connection, initial epiphany, mystic bond, vitality network, mystic spellcasting, spell repertoire |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/5` | 0.509477 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/28` | 0.506753 | ANCESTRY AND BACKGROUND |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/32` | 0.496934 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/35` | 0.496934 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/13` | 0.489299 | In addition to the initial ancestry feat you started with,  you gain an ancestry feat at 5th level and every 4 levels  thereafter. The list of ancestry feats available to you can be  found in your anc |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/421` | 0.487480 | 9th-rank spells, ancestry feat, skill increase |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/427` | 0.481922 | Attribute boosts, mystic feat, skill feat |

### Query 69
- Text: Summarize 2
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/390']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/536', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/540', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/558']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/390', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/389', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/389` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/558` | 0.689465 | 2 |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/536` | 0.689465 | 2 |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/540` | 0.689465 | 2 |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/887` | 0.647465 | 2 |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/532` | 0.647465 | 2 |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/390` | 0.647465 | 2 |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/606` | 0.647465 | 2 |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/592` | 0.647465 | 2 |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/866` | 0.507646 | 2nd |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/588` | 0.459336 | 1 |

### Query 70
- Text: What is the rule about Mystic feat, skill feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/423', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/419', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/390', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/392']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/390` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/392` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391` | 0.916581 | Mystic feat, skill feat |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/423` | 0.916581 | Mystic feat, skill feat |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/419` | 0.916581 | Mystic feat, skill feat |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/411` | 0.874581 | Mystic feat, skill feat |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/399` | 0.874581 | Mystic feat, skill feat |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/403` | 0.874581 | Mystic feat, skill feat |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/415` | 0.874581 | Mystic feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/395` | 0.874581 | Mystic feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/427` | 0.761937 | Attribute boosts, mystic feat, skill feat |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/407` | 0.761937 | Attribute boosts, mystic feat, skill feat |

### Query 71
- Text: Summarize 3
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/392']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/1077', 'PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/902', 'PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/952']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/392', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/393']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/393` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/1077` | 0.731895 | 3 |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/902` | 0.731895 | 3 |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/952` | 0.731895 | 3 |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/1027` | 0.689895 | 3 |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/392` | 0.689895 | 3 |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/877` | 0.689895 | 3 |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/899` | 0.689895 | 3 |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/977` | 0.689895 | 3 |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/1002` | 0.689895 | 3 |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/927` | 0.689895 | 3 |

### Query 72
- Text: What is the rule about 2nd-rank spells, general feat, group chat,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/393']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/393', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/401', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/409']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/393', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/392', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/394']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/392` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/394` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/393` | 0.786430 | 2nd-rank spells, general feat, group chat, reflex expertise, signature spells, skill increase |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/401` | 0.598151 | 4th-rank spells, expert spellcaster, general feat, skill increase |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/409` | 0.592533 | 6th-rank spells, general feat, perception expertise, skill increase, weapon expertise |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/397` | 0.547658 | 3rd-rank spells, ancestry feat, attribute boosts, fortitude expertise, skill increase |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/417` | 0.514664 | 8th-rank spells, attribute boosts, general feat, master spellcaster, skill increase |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/421` | 0.510346 | 9th-rank spells, ancestry feat, skill increase |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/25` | 0.503184 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/14` | 0.488098 | When you gain access to a new rank of spells, your first new  spell is always the spell granted by your chosen connection,  but you can choose the other spells. At 2nd level, you select  another 1st-r |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/413` | 0.486870 | 7th-rank spells, ancestry feat, armor expertise, skill increase, weapon specialization |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/15` | 0.481017 | Though you gain them at the same rate, your spell slots and  the spells in your spell repertoire are separate. If a feat or other  ability adds a spell to your spell repertoire, it wouldn't give you |

### Query 73
- Text: Summarize 4
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/394']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/394', 'PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/889', 'PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/925']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/394', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/395', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/393']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/395` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/393` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/394` | 0.774878 | 4 |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/889` | 0.774878 | 4 |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/925` | 0.774878 | 4 |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/926` | 0.744878 | 4 |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/901` | 0.732878 | 4 |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/1021` | 0.732878 | 4 |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/1011` | 0.732878 | 4 |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/975` | 0.732878 | 4 |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/974` | 0.732878 | 4 |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/973` | 0.732878 | 4 |

### Query 74
- Text: What is the rule about Mystic feat, skill feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/395']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/423', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/419', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/395', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/396', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/394']
- Expanded expected found: `True`
- Expanded expected rank: `8`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/396` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/394` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391` | 0.916581 | Mystic feat, skill feat |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/423` | 0.916581 | Mystic feat, skill feat |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/419` | 0.916581 | Mystic feat, skill feat |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/411` | 0.874581 | Mystic feat, skill feat |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/399` | 0.874581 | Mystic feat, skill feat |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/403` | 0.874581 | Mystic feat, skill feat |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/415` | 0.874581 | Mystic feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/395` | 0.874581 | Mystic feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/427` | 0.761937 | Attribute boosts, mystic feat, skill feat |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/407` | 0.761937 | Attribute boosts, mystic feat, skill feat |

### Query 75
- Text: Summarize 5
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/396']
- Expected found: `True`
- Expected rank: `12`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/1104', 'PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/1080', 'PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/876']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/396', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/397', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/395']
- Expanded expected found: `True`
- Expanded expected rank: `12`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/397` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/395` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/1104` | 0.772788 | 5 |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/1080` | 0.772788 | 5 |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/876` | 0.772788 | 5 |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/900` | 0.730788 | 5 |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/888` | 0.730788 | 5 |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/960` | 0.730788 | 5 |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/972` | 0.730788 | 5 |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/984` | 0.730788 | 5 |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/1008` | 0.730788 | 5 |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/948` | 0.730788 | 5 |

### Query 76
- Text: What is the rule about 3rd-rank spells, ancestry feat, attribute?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/397']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/397', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/421', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/413']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/397', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/396', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/398']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/396` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/398` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/397` | 0.826899 | 3rd-rank spells, ancestry feat, attribute boosts, fortitude expertise, skill increase |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/421` | 0.742464 | 9th-rank spells, ancestry feat, skill increase |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/413` | 0.672408 | 7th-rank spells, ancestry feat, armor expertise, skill increase, weapon specialization |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/405` | 0.621486 | 5th-rank spells, ancestry feat, resilient soul, skill increase |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/13` | 0.591919 | In addition to the initial ancestry feat you started with,  you gain an ancestry feat at 5th level and every 4 levels  thereafter. The list of ancestry feats available to you can be  found in your anc |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/2/Table/2` | 0.549901 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, connection, initial epiphany, mystic bond, vitality network, mystic spellcasting, spell repertoire2Mystic fea |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/417` | 0.548249 | 8th-rank spells, attribute boosts, general feat, master spellcaster, skill increase |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/401` | 0.542907 | 4th-rank spells, expert spellcaster, general feat, skill increase |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/409` | 0.541016 | 6th-rank spells, general feat, perception expertise, skill increase, weapon expertise |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/393` | 0.534661 | 2nd-rank spells, general feat, group chat, reflex expertise, signature spells, skill increase |

### Query 77
- Text: Summarize 6
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/398']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/935', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/576', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/582']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/398', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/397', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/399']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/397` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/399` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/935` | 0.783525 | 6 |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/576` | 0.783525 | 6 |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/582` | 0.783525 | 6 |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/398` | 0.741525 | 6 |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/586` | 0.741525 | 6 |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/580` | 0.741525 | 6 |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/870` | 0.627172 | 6th |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/25` | 0.508078 | 6TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/947` | 0.496931 | 7 |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/400` | 0.496931 | 7 |

### Query 78
- Text: What is the rule about Mystic feat, skill feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/399']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/423', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/419', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/399', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/400', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/398']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/400` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/398` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391` | 0.916581 | Mystic feat, skill feat |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/423` | 0.916581 | Mystic feat, skill feat |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/419` | 0.916581 | Mystic feat, skill feat |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/411` | 0.874581 | Mystic feat, skill feat |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/399` | 0.874581 | Mystic feat, skill feat |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/403` | 0.874581 | Mystic feat, skill feat |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/415` | 0.874581 | Mystic feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/395` | 0.874581 | Mystic feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/427` | 0.761937 | Attribute boosts, mystic feat, skill feat |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/407` | 0.761937 | Attribute boosts, mystic feat, skill feat |

### Query 79
- Text: Summarize 7
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/400']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/400', 'PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/947', 'PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/871']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/400', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/401', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/399']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/401` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/399` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/400` | 0.766039 | 7 |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/947` | 0.766039 | 7 |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/871` | 0.703809 | 7th |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/935` | 0.473241 | 6 |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/398` | 0.473241 | 6 |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/582` | 0.473241 | 6 |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/580` | 0.473241 | 6 |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/576` | 0.473241 | 6 |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/586` | 0.473241 | 6 |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/402` | 0.456129 | 8 |

### Query 80
- Text: What is the rule about 4th-rank spells, expert spellcaster, general?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/401']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/401', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/417', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/409']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/401', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/402', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/400']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/402` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/400` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/401` | 0.836421 | 4th-rank spells, expert spellcaster, general feat, skill increase |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/417` | 0.619852 | 8th-rank spells, attribute boosts, general feat, master spellcaster, skill increase |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/409` | 0.606642 | 6th-rank spells, general feat, perception expertise, skill increase, weapon expertise |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/393` | 0.540545 | 2nd-rank spells, general feat, group chat, reflex expertise, signature spells, skill increase |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/397` | 0.522110 | 3rd-rank spells, ancestry feat, attribute boosts, fortitude expertise, skill increase |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/4` | 0.508868 | Each day, you can cast up to three 1st-rank spells. You must  know spells to cast them, and you learn them via the spell  repertoire class feature. The number of spells you can cast  each day is calle |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/413` | 0.498310 | 7th-rank spells, ancestry feat, armor expertise, skill increase, weapon specialization |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/14` | 0.487539 | When you gain access to a new rank of spells, your first new  spell is always the spell granted by your chosen connection,  but you can choose the other spells. At 2nd level, you select  another 1st-r |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/2/Table/2` | 0.483124 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, connection, initial epiphany, mystic bond, vitality network, mystic spellcasting, spell repertoire2Mystic fea |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/862` | 0.480286 | Spell Rank |

### Query 81
- Text: Summarize 8
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/402']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/402', 'PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/959', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/598']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/402', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/401', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/403']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/401` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/403` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/402` | 0.787704 | 8 |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/959` | 0.787704 | 8 |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/598` | 0.787704 | 8 |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/530` | 0.745704 | 8 |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/872` | 0.670224 | 8th |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/40` | 0.546940 | 8TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/400` | 0.471909 | 7 |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/947` | 0.471909 | 7 |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/404` | 0.452855 | 9 |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/971` | 0.452855 | 9 |

### Query 82
- Text: What is the rule about Mystic feat, skill feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/403']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/423', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/419', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/403', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/402', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/404']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/402` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/404` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391` | 0.916581 | Mystic feat, skill feat |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/423` | 0.916581 | Mystic feat, skill feat |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/419` | 0.916581 | Mystic feat, skill feat |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/411` | 0.874581 | Mystic feat, skill feat |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/399` | 0.874581 | Mystic feat, skill feat |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/403` | 0.874581 | Mystic feat, skill feat |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/415` | 0.874581 | Mystic feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/395` | 0.874581 | Mystic feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/427` | 0.761937 | Attribute boosts, mystic feat, skill feat |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/407` | 0.761937 | Attribute boosts, mystic feat, skill feat |

### Query 83
- Text: Summarize 9
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/404']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/971', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/404', 'PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/873']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/404', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/405', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/403']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/405` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/403` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/971` | 0.770045 | 9 |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/404` | 0.770045 | 9 |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/873` | 0.699978 | 9th |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/4/SectionHeader/18` | 0.518515 | RESILIENT SOUL 9TH |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/402` | 0.455491 | 8 |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/530` | 0.455491 | 8 |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/598` | 0.455491 | 8 |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/959` | 0.455491 | 8 |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/406` | 0.446800 | 10 |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/983` | 0.446800 | 10 |

### Query 84
- Text: What is the rule about 5th-rank spells, ancestry feat, resilient soul,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/405']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/405', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/421', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/397']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/405', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/406', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/404']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/406` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/404` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/405` | 0.900498 | 5th-rank spells, ancestry feat, resilient soul, skill increase |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/421` | 0.708874 | 9th-rank spells, ancestry feat, skill increase |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/397` | 0.678403 | 3rd-rank spells, ancestry feat, attribute boosts, fortitude expertise, skill increase |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/13` | 0.598824 | In addition to the initial ancestry feat you started with,  you gain an ancestry feat at 5th level and every 4 levels  thereafter. The list of ancestry feats available to you can be  found in your anc |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/413` | 0.594420 | 7th-rank spells, ancestry feat, armor expertise, skill increase, weapon specialization |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/2/Table/2` | 0.546706 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, connection, initial epiphany, mystic bond, vitality network, mystic spellcasting, spell repertoire2Mystic fea |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/409` | 0.526070 | 6th-rank spells, general feat, perception expertise, skill increase, weapon expertise |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/393` | 0.524593 | 2nd-rank spells, general feat, group chat, reflex expertise, signature spells, skill increase |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/401` | 0.514685 | 4th-rank spells, expert spellcaster, general feat, skill increase |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/4/SectionHeader/11` | 0.496851 | ANCESTRY FEATS 5TH |

### Query 85
- Text: Summarize 10
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/406']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/406', 'PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/983', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/564']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/406', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/405', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/407']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/405` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/407` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/406` | 0.782219 | 10 |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/983` | 0.782219 | 10 |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/564` | 0.782219 | 10 |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/584` | 0.740219 | 10 |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/552` | 0.740219 | 10 |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/572` | 0.740219 | 10 |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/874` | 0.635691 | 10th |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/50` | 0.501945 | 10TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/2` | 0.499996 | LIFE BOND FEAT 10 |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/51` | 0.495199 | **DATA BOND** **FEAT 10** |

### Query 86
- Text: What is the rule about Attribute boosts, mystic feat, skill feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/407']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/427', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/407', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/395']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/407', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/408', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/406']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/408` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/406` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/427` | 0.902405 | Attribute boosts, mystic feat, skill feat |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/407` | 0.902405 | Attribute boosts, mystic feat, skill feat |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/395` | 0.742856 | Mystic feat, skill feat |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/399` | 0.700856 | Mystic feat, skill feat |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/415` | 0.700856 | Mystic feat, skill feat |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/423` | 0.700856 | Mystic feat, skill feat |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/411` | 0.700856 | Mystic feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/419` | 0.700856 | Mystic feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/403` | 0.700856 | Mystic feat, skill feat |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391` | 0.700856 | Mystic feat, skill feat |

### Query 87
- Text: Summarize 11
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/408']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/995', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/408', 'PZO22001 Starfinder Player Core 114-125::/page/4/SectionHeader/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/408', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/407', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/409']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/407` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/409` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/995` | 0.764621 | 11 |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/408` | 0.764621 | 11 |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/4/SectionHeader/23` | 0.554831 | WEAPON EXPERTISE 11TH |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/4/SectionHeader/21` | 0.500289 | PERCEPTION EXPERTISE 11TH |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/410` | 0.493902 | 12 |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/542` | 0.493902 | 12 |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/550` | 0.493902 | 12 |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/1007` | 0.493902 | 12 |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/544` | 0.493902 | 12 |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/546` | 0.493902 | 12 |

### Query 88
- Text: What is the rule about 6th-rank spells, general feat, perception?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/409']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/409', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/393', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/401']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/409', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/408', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/410']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/408` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/410` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/409` | 0.822135 | 6th-rank spells, general feat, perception expertise, skill increase, weapon expertise |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/393` | 0.605364 | 2nd-rank spells, general feat, group chat, reflex expertise, signature spells, skill increase |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/401` | 0.598241 | 4th-rank spells, expert spellcaster, general feat, skill increase |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/397` | 0.545418 | 3rd-rank spells, ancestry feat, attribute boosts, fortitude expertise, skill increase |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/421` | 0.543828 | 9th-rank spells, ancestry feat, skill increase |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/417` | 0.537228 | 8th-rank spells, attribute boosts, general feat, master spellcaster, skill increase |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/413` | 0.520455 | 7th-rank spells, ancestry feat, armor expertise, skill increase, weapon specialization |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/25` | 0.494847 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/405` | 0.493739 | 5th-rank spells, ancestry feat, resilient soul, skill increase |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/425` | 0.467250 | General feat, legendary spellcaster, perfect harmony, skill increase, transcendence |

### Query 89
- Text: What is the rule about Mystic feat, skill feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/411']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/423', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/419', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/411', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/412', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/410']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/412` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/410` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391` | 0.916581 | Mystic feat, skill feat |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/423` | 0.916581 | Mystic feat, skill feat |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/419` | 0.916581 | Mystic feat, skill feat |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/411` | 0.874581 | Mystic feat, skill feat |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/399` | 0.874581 | Mystic feat, skill feat |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/403` | 0.874581 | Mystic feat, skill feat |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/415` | 0.874581 | Mystic feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/395` | 0.874581 | Mystic feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/427` | 0.761937 | Attribute boosts, mystic feat, skill feat |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/407` | 0.761937 | Attribute boosts, mystic feat, skill feat |

### Query 90
- Text: What is the rule about 7th-rank spells, ancestry feat, armor expertise,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/413']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/413', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/397', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/421']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/413', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/412', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/414']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/412` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/414` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/413` | 0.870216 | 7th-rank spells, ancestry feat, armor expertise, skill increase, weapon specialization |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/397` | 0.724866 | 3rd-rank spells, ancestry feat, attribute boosts, fortitude expertise, skill increase |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/421` | 0.711962 | 9th-rank spells, ancestry feat, skill increase |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/409` | 0.624035 | 6th-rank spells, general feat, perception expertise, skill increase, weapon expertise |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/405` | 0.597463 | 5th-rank spells, ancestry feat, resilient soul, skill increase |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/401` | 0.571550 | 4th-rank spells, expert spellcaster, general feat, skill increase |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/Table/2` | 0.551989 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, connection, initial epiphany, mystic bond, vitality network, mystic spellcasting, spell repertoire2Mystic fea |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/13` | 0.545145 | In addition to the initial ancestry feat you started with,  you gain an ancestry feat at 5th level and every 4 levels  thereafter. The list of ancestry feats available to you can be  found in your anc |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/417` | 0.539430 | 8th-rank spells, attribute boosts, general feat, master spellcaster, skill increase |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/393` | 0.538201 | 2nd-rank spells, general feat, group chat, reflex expertise, signature spells, skill increase |

### Query 91
- Text: What is the rule about Mystic feat, skill feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/415']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/423', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/419', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/415', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/416', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/414']
- Expanded expected found: `True`
- Expanded expected rank: `7`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/416` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/414` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391` | 0.916581 | Mystic feat, skill feat |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/423` | 0.916581 | Mystic feat, skill feat |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/419` | 0.916581 | Mystic feat, skill feat |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/411` | 0.874581 | Mystic feat, skill feat |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/399` | 0.874581 | Mystic feat, skill feat |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/403` | 0.874581 | Mystic feat, skill feat |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/415` | 0.874581 | Mystic feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/395` | 0.874581 | Mystic feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/427` | 0.761937 | Attribute boosts, mystic feat, skill feat |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/407` | 0.761937 | Attribute boosts, mystic feat, skill feat |

### Query 92
- Text: What is the rule about 8th-rank spells, attribute boosts, general?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/417']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/417', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/397', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/421']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/417', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/416', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/418']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/416` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/418` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/417` | 0.772903 | 8th-rank spells, attribute boosts, general feat, master spellcaster, skill increase |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/397` | 0.615376 | 3rd-rank spells, ancestry feat, attribute boosts, fortitude expertise, skill increase |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/421` | 0.594638 | 9th-rank spells, ancestry feat, skill increase |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/409` | 0.538627 | 6th-rank spells, general feat, perception expertise, skill increase, weapon expertise |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/401` | 0.528813 | 4th-rank spells, expert spellcaster, general feat, skill increase |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/393` | 0.523006 | 2nd-rank spells, general feat, group chat, reflex expertise, signature spells, skill increase |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/413` | 0.520500 | 7th-rank spells, ancestry feat, armor expertise, skill increase, weapon specialization |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/5` | 0.512380 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/14` | 0.503596 | When you gain access to a new rank of spells, your first new  spell is always the spell granted by your chosen connection,  but you can choose the other spells. At 2nd level, you select  another 1st-r |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/8` | 0.501598 | When you get spell slots of 2nd rank and higher, you can fill those  slots with stronger versions of lower-rank spells. This increases  the spell's rank to match the spell slot. You must have a spell |

### Query 93
- Text: What is the rule about Mystic feat, skill feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/419']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/423', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/419', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/419', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/420', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/418']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/420` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/418` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391` | 0.916581 | Mystic feat, skill feat |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/423` | 0.916581 | Mystic feat, skill feat |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/419` | 0.916581 | Mystic feat, skill feat |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/411` | 0.874581 | Mystic feat, skill feat |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/399` | 0.874581 | Mystic feat, skill feat |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/403` | 0.874581 | Mystic feat, skill feat |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/415` | 0.874581 | Mystic feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/395` | 0.874581 | Mystic feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/427` | 0.761937 | Attribute boosts, mystic feat, skill feat |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/407` | 0.761937 | Attribute boosts, mystic feat, skill feat |

### Query 94
- Text: What is the rule about 9th-rank spells, ancestry feat, skill increase?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/421']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/421', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/397', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/413']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/421', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/422', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/420']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/422` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/420` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/421` | 0.923132 | 9th-rank spells, ancestry feat, skill increase |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/397` | 0.755121 | 3rd-rank spells, ancestry feat, attribute boosts, fortitude expertise, skill increase |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/413` | 0.714654 | 7th-rank spells, ancestry feat, armor expertise, skill increase, weapon specialization |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/405` | 0.665679 | 5th-rank spells, ancestry feat, resilient soul, skill increase |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/417` | 0.607022 | 8th-rank spells, attribute boosts, general feat, master spellcaster, skill increase |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/401` | 0.599857 | 4th-rank spells, expert spellcaster, general feat, skill increase |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/409` | 0.599832 | 6th-rank spells, general feat, perception expertise, skill increase, weapon expertise |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/13` | 0.573218 | In addition to the initial ancestry feat you started with,  you gain an ancestry feat at 5th level and every 4 levels  thereafter. The list of ancestry feats available to you can be  found in your anc |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/2/Table/2` | 0.572234 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, connection, initial epiphany, mystic bond, vitality network, mystic spellcasting, spell repertoire2Mystic fea |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/393` | 0.568944 | 2nd-rank spells, general feat, group chat, reflex expertise, signature spells, skill increase |

### Query 95
- Text: What is the rule about Mystic feat, skill feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/423']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/423', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/419', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/423', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/424', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/422']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/424` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/422` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391` | 0.916581 | Mystic feat, skill feat |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/423` | 0.916581 | Mystic feat, skill feat |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/419` | 0.916581 | Mystic feat, skill feat |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/411` | 0.874581 | Mystic feat, skill feat |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/399` | 0.874581 | Mystic feat, skill feat |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/403` | 0.874581 | Mystic feat, skill feat |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/415` | 0.874581 | Mystic feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/395` | 0.874581 | Mystic feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/427` | 0.761937 | Attribute boosts, mystic feat, skill feat |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/407` | 0.761937 | Attribute boosts, mystic feat, skill feat |

### Query 96
- Text: What is the rule about General feat, legendary spellcaster, perfect?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/425']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/425', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/401', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/417']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/425', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/424', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/426']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/424` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/426` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/425` | 0.795634 | General feat, legendary spellcaster, perfect harmony, skill increase, transcendence |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/401` | 0.646174 | 4th-rank spells, expert spellcaster, general feat, skill increase |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/417` | 0.584032 | 8th-rank spells, attribute boosts, general feat, master spellcaster, skill increase |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/25` | 0.534203 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/393` | 0.510400 | 2nd-rank spells, general feat, group chat, reflex expertise, signature spells, skill increase |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/409` | 0.507617 | 6th-rank spells, general feat, perception expertise, skill increase, weapon expertise |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/397` | 0.493299 | 3rd-rank spells, ancestry feat, attribute boosts, fortitude expertise, skill increase |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/415` | 0.484339 | Mystic feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/395` | 0.484339 | Mystic feat, skill feat |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/423` | 0.484339 | Mystic feat, skill feat |

### Query 97
- Text: What is the rule about Attribute boosts, mystic feat, skill feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/427']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/427', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/407', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/395']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/427', 'PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/426', 'PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/426` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/427` | 0.902405 | Attribute boosts, mystic feat, skill feat |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/407` | 0.902405 | Attribute boosts, mystic feat, skill feat |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/395` | 0.742856 | Mystic feat, skill feat |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/399` | 0.700856 | Mystic feat, skill feat |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/415` | 0.700856 | Mystic feat, skill feat |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/423` | 0.700856 | Mystic feat, skill feat |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/411` | 0.700856 | Mystic feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/419` | 0.700856 | Mystic feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/403` | 0.700856 | Mystic feat, skill feat |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/391` | 0.700856 | Mystic feat, skill feat |

### Query 98
- Text: What is the rule about In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/Text/4', 'PZO22001 Starfinder Player Core 114-125::/page/2/Text/5', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/Text/4', 'PZO22001 Starfinder Player Core 114-125::/page/2/Text/5', 'PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/Text/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/4` | 0.943824 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/5` | 0.843002 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/6` | 0.673303 | At 1st level, your class gives you  an attribute boost to Wisdom. |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/29` | 0.530456 | In addition to what you get from your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/27` | 0.513914 | You gain these abilities as a mystic. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/9` | 0.505161 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/427` | 0.498346 | Attribute boosts, mystic feat, skill feat |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/407` | 0.498346 | Attribute boosts, mystic feat, skill feat |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/58` | 0.482799 | Trained in a number of additional  skills equal to 3 plus your Intelligence  modifier |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/Table/2` | 0.481890 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, connection, initial epiphany, mystic bond, vitality network, mystic spellcasting, spell repertoire2Mystic fea |

### Query 99
- Text: What is the rule about At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get a partial boost and must boost that attribute again at a  later level to increase it by 1.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/Text/5', 'PZO22001 Starfinder Player Core 114-125::/page/2/Text/4', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/Text/5', 'PZO22001 Starfinder Player Core 114-125::/page/2/Text/4', 'PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/5` | 0.966227 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/4` | 0.768876 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/9` | 0.601486 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/9` | 0.550930 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use an increase to either become trained in  one skill you're untrained in or to increase your proficiency  in one skill |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/6` | 0.515831 | At 1st level, your class gives you  an attribute boost to Wisdom. |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/13` | 0.503232 | In addition to the initial ancestry feat you started with,  you gain an ancestry feat at 5th level and every 4 levels  thereafter. The list of ancestry feats available to you can be  found in your anc |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/25` | 0.502212 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/10` | 0.501831 | At 7th level, you can use skill increases to become a  master in a skill in which you're already an expert, and at  15th level, you can use them to become legendary in a skill  in which you're already |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/27` | 0.500867 | You gain these abilities as a mystic. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/14` | 0.498597 | When you gain access to a new rank of spells, your first new  spell is always the spell granted by your chosen connection,  but you can choose the other spells. At 2nd level, you select  another 1st-r |

### Query 100
- Text: What is the rule about All mystics have a supernatural connection with a cosmic force  that grants magical powers. The exact nature of your connection  can vary widely—you might worship a god or pantheon, embody  a metaphysical concept, become a conduit for nature's wrath, or  something else. Even mystics who share the same connection?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/2/Text/9', 'PZO22001 Starfinder Player Core 114-125::/page/5/Text/11', 'PZO22001 Starfinder Player Core 114-125::/page/1/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/2/Text/9', 'PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/8', 'PZO22001 Starfinder Player Core 114-125::/page/2/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/2/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/9` | 0.997509 | All mystics have a supernatural connection with a cosmic force  that grants magical powers. The exact nature of your connection  can vary widely—you might worship a god or pantheon, embody  a metaphys |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/11` | 0.698736 | Your connection is a mystical force that grants you magic. It  could come from a divine patron, manifestation of a primeval  cosmic force, or some other mystery. Your connection  determines your spell |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/2` | 0.684236 | You're a conduit, channeling the fundamental forces that connect and bind everything in the cosmos.  You can draw upon this supernatural wellspring to form deep spiritual bonds with your allies,  empo |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/3` | 0.624900 | You are a spellcaster and can cast spells using the Cast a Spell  activity (see Casting Spells on page 298). As a mystic, when  you cast spells, you might intone a prayer or hum a song  inspired by yo |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/Text/15` | 0.574459 | You form a bond between yourself and others, most typically  your closest companions. Forming bonds is different for every  mystic but always involves using a 10-minute activity related  to the mystic |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/8` | 0.565726 | You see into the truth of the cosmos through your connection. You gain the greater epiphany spell for your chosen connection. |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/7` | 0.555851 | You discover the ultimate truth of your connection and its  role as a foundation of the cosmos. You learn your chosen  connection's perfect harmony. |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/35` | 0.546729 | Through dedication or serendipity, you've branched out to  explore other connections to the fundamental building blocks of  the cosmos. You learn the initial epiphany spell of a connection  that grant |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/14` | 0.543849 | You maintain a permanent psychic link to the Akashic  Record, the supernatural repository of all knowledge in the  multiverse. This connection allows you to access knowledge  that otherwise would rema |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/27` | 0.535246 | You gain these abilities as a mystic. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |

### Query 101
- Text: Lookup values for Spell RankYour LevelCantrips1st2nd3rd4th5th6th7th8th9th10th153—————————254—————————3543————————4544————————55443———————65444———————754443——————854444——————9544443—————10544444—————115444443————125444444————1354444443———1454444444———15544444443——16544444444——175444444443—185444444444—1954444444441*2054444444441*
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/5/Table/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/5/Table/2', 'PZO22001 Starfinder Player Core 114-125::/page/6/Text/8', 'PZO22001 Starfinder Player Core 114-125::/page/6/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/5/Table/2', 'PZO22001 Starfinder Player Core 114-125::/page/5/SectionHeader/1', 'PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/862']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/5/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/862` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/5/Table/2` | 1.019312 | Spell RankYour LevelCantrips1st2nd3rd4th5th6th7th8th9th10th153—————————254—————————3543————————4544————————55443———————65444———————754443——————854444——————9544443—————10544444—————115444443————1254444 |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/8` | 0.658742 | **Connection Spells** cantrip: *recharge* *weapon*; 1st: *shifting* *surge*; 2nd: *resist energy*; 3rd: *levitate*; 4th: *wall of fire**;  5th: *elemental form*; 6th: *promession*; 7th: *absolute zero |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/29` | 0.647395 | **Connection Spells** cantrip: *figment*; 1st: *grim tendrils*; 2nd:  *invisibility*; 3rd: *slow*; 4th: *flicker*; 5th: *shadow blast*;  6th: *mislead*; 7th: *eclipse burst*; 8th: *disappearance*; 9th |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/23` | 0.598938 | **Connection Spells** cantrip: *summon instrument*; 1st:  *motivating* *ringtone*; 2nd: *noise blast*; 3rd: *hypnotize*; 4th:  *battle* *sonata*; 5th: *synaptic pulse*; 6th: *vibrant pattern*; 7th:  * |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/Table/2` | 0.592259 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, connection, initial epiphany, mystic bond, vitality network, mystic spellcasting, spell repertoire2Mystic fea |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/Table/3` | 0.568968 | FeatLevelAdaptive Defense4Advanced Epiphany8Bond Boost2Bond Spell14Cantrip Expansion2Cloud Storage4Conceal Spell2Convert Elemental Essence12Convert Illumination12Convert Information12Convert Life Forc |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/16` | 0.567773 | **Connection Spells** cantrip: *scan* *environment*; 1st: *akashic* *download*; 2nd: *instant* *virus*; 3rd: *hypercognition*; 4th:  *clairvoyance*; 5th: *wave* of *warning*; 6th: *truesight*; 7th:  * |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/16` | 0.565113 | **Connection Spells** cantrip: *stabilize*; 1st: *heal*; 2nd: *false* *vitality*; 3rd: *entropy* *strike*; 4th: *genetic regeneration*; 5th:  *breath of life*; 6th: *vampiric exsanguination*; 7th: *ex |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/862` | 0.563108 | Spell Rank |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/12` | 0.537097 | The collection of spells you can cast is called your spell  repertoire. At 1st level, you learn two 1st-rank spells of your  choice and four cantrips of your choice as well as an additional  spell and |

### Query 102
- Text: Lookup values for FeatLevelAdaptive Defense4Advanced Epiphany8Bond Boost2Bond Spell14Cantrip Expansion2Cloud Storage4Conceal Spell2Convert Elemental Essence12Convert Illumination12Convert Information12Convert Life Force12Convert Tempo12Data Bond10Divine Bond1Effortless Concentration16Eldritch Bond2Enlightenment20Extended Vitality4Greater Epiphany10Infused Spell14
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/7/Table/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/7/Table/3', 'PZO22001 Starfinder Player Core 114-125::/page/7/Table/16', 'PZO22001 Starfinder Player Core 114-125::/page/2/Table/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/7/Table/3', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/525', 'PZO22001 Starfinder Player Core 114-125::/page/7/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/525` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/7/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/7/Table/3` | 0.989723 | FeatLevelAdaptive Defense4Advanced Epiphany8Bond Boost2Bond Spell14Cantrip Expansion2Cloud Storage4Conceal Spell2Convert Elemental Essence12Convert Illumination12Convert Information12Convert Life Forc |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/7/Table/16` | 0.781899 | FeatLevelLife Bond10Mental Interference4Mystic Luminary6Network Attunement18Network Shield6New Epiphany6Quickened Casting10Radiant Bond6Reach Spell1Realized Epiphany18Spot Healing2Syncretic Epiphany16 |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/Table/2` | 0.660475 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, connection, initial epiphany, mystic bond, vitality network, mystic spellcasting, spell repertoire2Mystic fea |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/5/Table/2` | 0.552498 | Spell RankYour LevelCantrips1st2nd3rd4th5th6th7th8th9th10th153—————————254—————————3543————————4544————————55443———————65444———————754443——————854444——————9544443—————10544444—————115444443————1254444 |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/12` | 0.549739 | feature. You gain the initial epiphany at 1st level and can  gain the advanced and greater epiphanies by selecting the  Advanced Epiphany (page 123) and Greater Epiphany (page  124) feats. You gain yo |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/17` | 0.523986 | **Epiphany Spells **initial: *akashic* *fount*; advanced: *akashic * *assistant*; greater: *data drain* |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/8` | 0.517490 | **Connection Spells** cantrip: *recharge* *weapon*; 1st: *shifting* *surge*; 2nd: *resist energy*; 3rd: *levitate*; 4th: *wall of fire**;  5th: *elemental form*; 6th: *promession*; 7th: *absolute zero |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/10` | 0.510994 | **Epiphany Spells **initial: *elemental weapon*; advanced:  *elemental barrier*; greater: *elemental nova* |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/2` | 0.510442 | Use this table to look up mystic feats by name. |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/25` | 0.505199 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |

### Query 103
- Text: What are the requirements for **DIVINE BOND** **FEAT 1** **MYSTIC**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/7/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/7/Text/13', 'PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/14', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/7/Text/13', 'PZO22001 Starfinder Player Core 114-125::/page/7/Text/14', 'PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/7/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/13` | 0.886238 | **DIVINE BOND** **FEAT 1** **MYSTIC** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/14` | 0.660053 | MYSTIC BOND |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/5` | 0.547372 | **MYSTIC** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/25` | 0.505372 | **MYSTIC** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/28` | 0.505372 | **MYSTIC** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/20` | 0.505372 | **MYSTIC** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/30` | 0.505372 | **MYSTIC** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/10` | 0.505372 | **MYSTIC** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/53` | 0.505372 | **MYSTIC** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/38` | 0.505372 | **MYSTIC** |

### Query 104
- Text: What are the requirements for **Prerequisites** connection with divine spellcasting, you  worship a deity?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/7/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/7/Text/14', 'PZO22001 Starfinder Player Core 114-125::/page/8/Text/34', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/54']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/7/Text/14', 'PZO22001 Starfinder Player Core 114-125::/page/7/Text/13', 'PZO22001 Starfinder Player Core 114-125::/page/7/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/7/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/7/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/14` | 0.966528 | **Prerequisites** connection with divine spellcasting, you  worship a deity |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/34` | 0.785638 | **Prerequisites** connection with occult spellcasting |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/54` | 0.785638 | **Prerequisites** connection with occult spellcasting |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/44` | 0.665335 | **Prerequisites** connection with primal spellcasting |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/29` | 0.665335 | **Prerequisites** connection with primal spellcasting |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/4` | 0.665335 | **Prerequisites** connection with primal spellcasting |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/15` | 0.531239 | As a disciple of a god, you wield some of their divine power.  You become trained in the listed divine skill associated with  the deity and add the listed cleric spells (pages 35–39) to  your spell li |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/21` | 0.515205 | **Prerequisites** shadow connection |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/3` | 0.510503 | You are a spellcaster and can cast spells using the Cast a Spell  activity (see Casting Spells on page 298). As a mystic, when  you cast spells, you might intone a prayer or hum a song  inspired by yo |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/26` | 0.506097 | Prerequisites akashic connection |

### Query 105
- Text: Lookup values for FeatLevelLife Bond10Mental Interference4Mystic Luminary6Network Attunement18Network Shield6New Epiphany6Quickened Casting10Radiant Bond6Reach Spell1Realized Epiphany18Spot Healing2Syncretic Epiphany16Transcended Existence20Tripartite Mind8Vitality Web16Waste Not4Widen Spell1Wild Bond2Xenodruid Bond1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/7/Table/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/7/Table/16', 'PZO22001 Starfinder Player Core 114-125::/page/7/Table/3', 'PZO22001 Starfinder Player Core 114-125::/page/2/Table/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/7/Table/16', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/569', 'PZO22001 Starfinder Player Core 114-125::/page/7/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/569` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/7/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/7/Table/16` | 0.989713 | FeatLevelLife Bond10Mental Interference4Mystic Luminary6Network Attunement18Network Shield6New Epiphany6Quickened Casting10Radiant Bond6Reach Spell1Realized Epiphany18Spot Healing2Syncretic Epiphany16 |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/7/Table/3` | 0.815457 | FeatLevelAdaptive Defense4Advanced Epiphany8Bond Boost2Bond Spell14Cantrip Expansion2Cloud Storage4Conceal Spell2Convert Elemental Essence12Convert Illumination12Convert Information12Convert Life Forc |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/2/Table/2` | 0.631037 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, connection, initial epiphany, mystic bond, vitality network, mystic spellcasting, spell repertoire2Mystic fea |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/11` | 0.568313 | You can manifest your bond as a web of vital energy between  your allies. You learn the *vitality* *web* epiphany spell  (page 377). |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/16` | 0.549975 | **Connection Spells** cantrip: *scan* *environment*; 1st: *akashic* *download*; 2nd: *instant* *virus*; 3rd: *hypercognition*; 4th:  *clairvoyance*; 5th: *wave* of *warning*; 6th: *truesight*; 7th:  * |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/17` | 0.541556 | **Epiphany Spells **initial: *akashic* *fount*; advanced: *akashic * *assistant*; greater: *data drain* |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/12` | 0.533859 | feature. You gain the initial epiphany at 1st level and can  gain the advanced and greater epiphanies by selecting the  Advanced Epiphany (page 123) and Greater Epiphany (page  124) feats. You gain yo |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/1` | 0.529301 | alter the genes of creatures in your bond. You gain the *wild* *bond* epiphany spell (page 377). |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/17` | 0.528133 | **Epiphany Spells **initial: *infusion*; advanced: *vitality nova*;  greater: *vital rebirth* |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/16` | 0.522808 | **Connection Spells** cantrip: *stabilize*; 1st: *heal*; 2nd: *false* *vitality*; 3rd: *entropy* *strike*; 4th: *genetic regeneration*; 5th:  *breath of life*; 6th: *vampiric exsanguination*; 7th: *ex |

### Query 106
- Text: What are the requirements for **REACH SPELL **[one-action] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/18', 'PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/22', 'PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/27']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/18', 'PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/20', 'PZO22001 Starfinder Player Core 114-125::/page/7/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/7/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/18` | 0.912330 | **REACH SPELL **[one-action] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/22` | 0.704854 | **WIDEN SPELL **[one-action] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/27` | 0.696623 | **CONCEAL SPELL **[one-action] **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/3/SectionHeader/29` | 0.634764 | **NETWORK SPELL **[one-action] |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/587` | 0.497331 | Reach Spell |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/45` | 0.471806 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/43` | 0.471806 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/44` | 0.471806 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/45` | 0.471806 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/32` | 0.471806 | **SPELLS** |

### Query 107
- Text: What are the requirements for **WIDEN SPELL **[one-action] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/22', 'PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/18', 'PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/27']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/22', 'PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/24', 'PZO22001 Starfinder Player Core 114-125::/page/7/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/7/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/22` | 0.901243 | **WIDEN SPELL **[one-action] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/18` | 0.714043 | **REACH SPELL **[one-action] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/27` | 0.698789 | **CONCEAL SPELL **[one-action] **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/3/SectionHeader/29` | 0.591565 | **NETWORK SPELL **[one-action] |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/20` | 0.473632 | **WASTE NOT **[one-action] **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/603` | 0.463077 | Widen Spell |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/14` | 0.458830 | **MENTAL INTERFERENCE **[one-action] **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/44` | 0.453433 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/63` | 0.453433 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/45` | 0.453433 | **SPELLS** |

### Query 108
- Text: What are the requirements for **XENODRUID BOND** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/26', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/607', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/36']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/26', 'PZO22001 Starfinder Player Core 114-125::/page/7/Text/25', 'PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/28']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/7/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/26` | 0.892387 | **XENODRUID BOND** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/607` | 0.653145 | Xenodruid Bond |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/36` | 0.516816 | **RADIANT BOND** **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/41` | 0.471664 | **WILD BOND** **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/13` | 0.468719 | **DIVINE BOND** **FEAT 1** **MYSTIC** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/31` | 0.467058 | **ELDRITCH BOND** **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/51` | 0.434606 | **DATA BOND** **FEAT 10** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/30` | 0.426466 | You join a primal order of xenodruids with ties to nature and  the biodiversity of the Universe, such as the Xenowardens.  Choose one of the following xenodruid orders on page 122. |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/7/Table/16` | 0.413033 | FeatLevelLife Bond10Mental Interference4Mystic Luminary6Network Attunement18Network Shield6New Epiphany6Quickened Casting10Radiant Bond6Reach Spell1Realized Epiphany18Spot Healing2Syncretic Epiphany16 |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/18` | 0.389533 | **BOND BOOST **[reaction] **FEAT 2** |

### Query 109
- Text: What are the requirements for **Prerequisites** connection with primal spellcasting?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/7/Text/29']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/10/Text/4', 'PZO22001 Starfinder Player Core 114-125::/page/8/Text/44', 'PZO22001 Starfinder Player Core 114-125::/page/7/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/7/Text/29', 'PZO22001 Starfinder Player Core 114-125::/page/7/Text/30', 'PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/28']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/7/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/4` | 0.977786 | **Prerequisites** connection with primal spellcasting |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/44` | 0.977786 | **Prerequisites** connection with primal spellcasting |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/29` | 0.977786 | **Prerequisites** connection with primal spellcasting |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/34` | 0.711933 | **Prerequisites** connection with occult spellcasting |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/54` | 0.711933 | **Prerequisites** connection with occult spellcasting |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/14` | 0.626956 | **Prerequisites** connection with divine spellcasting, you  worship a deity |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/16` | 0.552485 | Prerequisites elemental connection |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/22` | 0.537314 | **Tradition** primal; **Connection Skill** Performance |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/7` | 0.517898 | **Tradition** primal; **Connection Skill** Nature |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/389` | 0.511687 | Ancestry and background, attribute boosts, initial proficiencies, connection, initial epiphany, mystic bond, vitality network, mystic spellcasting, spell repertoire |

### Query 110
- Text: What are the requirements for **BOND BOOST **[reaction] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/18', 'PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/41', 'PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/18', 'PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/20', 'PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/18` | 0.860549 | **BOND BOOST **[reaction] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/41` | 0.588088 | **WILD BOND** **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/31` | 0.527076 | **ELDRITCH BOND** **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/531` | 0.484266 | Bond Boost |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/51` | 0.480157 | **DATA BOND** **FEAT 10** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/36` | 0.473773 | **RADIANT BOND** **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/26` | 0.443053 | **XENODRUID BOND** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/23` | 0.407269 | **CANTRIP EXPANSION** **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/36` | 0.400626 | **SPOT HEALING **[reaction] **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/2` | 0.400282 | LIFE BOND FEAT 10 |

### Query 111
- Text: What are the requirements for **CANTRIP EXPANSION** **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/23', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/535', 'PZO22001 Starfinder Player Core 114-125::/page/7/Table/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/23', 'PZO22001 Starfinder Player Core 114-125::/page/8/Text/22', 'PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/25']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/8/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/23` | 0.912715 | **CANTRIP EXPANSION** **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/535` | 0.561950 | Cantrip Expansion |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/7/Table/3` | 0.455790 | FeatLevelAdaptive Defense4Advanced Epiphany8Bond Boost2Bond Spell14Cantrip Expansion2Cloud Storage4Conceal Spell2Convert Elemental Essence12Convert Illumination12Convert Information12Convert Life Forc |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/31` | 0.398449 | **Prerequisites** transcendence |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/3/SectionHeader/18` | 0.391618 | MYSTIC FEATS 2ND |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/3/SectionHeader/20` | 0.388703 | SKILL FEATS 2ND |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/4/Text/13` | 0.379232 | In addition to the initial ancestry feat you started with,  you gain an ancestry feat at 5th level and every 4 levels  thereafter. The list of ancestry feats available to you can be  found in your anc |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/28` | 0.378184 | **TRANSCENDED EXISTENCE** **FEAT 20** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/10` | 0.372064 | **EXTENDED VITALITY** **FEAT 4** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/23` | 0.371155 | **Connection Spells** cantrip: *summon instrument*; 1st:  *motivating* *ringtone*; 2nd: *noise blast*; 3rd: *hypnotize*; 4th:  *battle* *sonata*; 5th: *synaptic pulse*; 6th: *vibrant pattern*; 7th:  * |

### Query 112
- Text: What are the requirements for **CONCEAL SPELL **[one-action] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/27', 'PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/22', 'PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/27', 'PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/29', 'PZO22001 Starfinder Player Core 114-125::/page/8/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/8/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/27` | 0.904200 | **CONCEAL SPELL **[one-action] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/22` | 0.671951 | **WIDEN SPELL **[one-action] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/18` | 0.667761 | **REACH SPELL **[one-action] **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/3/SectionHeader/29` | 0.580763 | **NETWORK SPELL **[one-action] |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/539` | 0.477880 | Conceal Spell |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/45` | 0.453673 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/45` | 0.453673 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/63` | 0.453673 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/32` | 0.453673 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/43` | 0.453673 | **SPELLS** |

### Query 113
- Text: What are the requirements for **ELDRITCH BOND** **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/31', 'PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/41', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/557']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/31', 'PZO22001 Starfinder Player Core 114-125::/page/8/Text/30', 'PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/33']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/8/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/33` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/31` | 0.884336 | **ELDRITCH BOND** **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/41` | 0.646973 | **WILD BOND** **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/557` | 0.577383 | Eldritch Bond |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/36` | 0.482191 | **RADIANT BOND** **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/26` | 0.475606 | **XENODRUID BOND** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/18` | 0.452269 | **BOND BOOST **[reaction] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/7/Table/3` | 0.451970 | FeatLevelAdaptive Defense4Advanced Epiphany8Bond Boost2Bond Spell14Cantrip Expansion2Cloud Storage4Conceal Spell2Convert Elemental Essence12Convert Illumination12Convert Information12Convert Life Forc |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/13` | 0.445488 | **DIVINE BOND** **FEAT 1** **MYSTIC** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/51` | 0.431173 | **DATA BOND** **FEAT 10** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/3/SectionHeader/20` | 0.428997 | SKILL FEATS 2ND |

### Query 114
- Text: What are the requirements for **Prerequisites** connection with occult spellcasting?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/8/Text/34']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/9/Text/54', 'PZO22001 Starfinder Player Core 114-125::/page/8/Text/34', 'PZO22001 Starfinder Player Core 114-125::/page/8/Text/44']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/8/Text/34', 'PZO22001 Starfinder Player Core 114-125::/page/8/Text/35', 'PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/33']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/8/Text/35` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/33` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/54` | 0.974784 | **Prerequisites** connection with occult spellcasting |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/34` | 0.974784 | **Prerequisites** connection with occult spellcasting |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/44` | 0.766293 | **Prerequisites** connection with primal spellcasting |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/4` | 0.724293 | **Prerequisites** connection with primal spellcasting |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/29` | 0.724293 | **Prerequisites** connection with primal spellcasting |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/14` | 0.716404 | **Prerequisites** connection with divine spellcasting, you  worship a deity |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/15` | 0.554222 | **Tradition** occult; **Connection Skill** Occultism |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/26` | 0.543104 | Prerequisites akashic connection |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/21` | 0.532992 | **Prerequisites** shadow connection |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/16` | 0.523909 | Prerequisites elemental connection |

### Query 115
- Text: What are the requirements for **SPOT HEALING **[reaction] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/36']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/36', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/591', 'PZO22001 Starfinder Player Core 114-125::/page/10/Text/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/36', 'PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/38', 'PZO22001 Starfinder Player Core 114-125::/page/8/Text/35']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/38` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/8/Text/35` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/36` | 0.884960 | **SPOT HEALING **[reaction] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/591` | 0.586205 | Spot Healing |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/31` | 0.531242 | **Prerequisites** healing connection |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/6/SectionHeader/13` | 0.445579 | HEALING |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/18` | 0.432390 | **BOND BOOST **[reaction] **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/41` | 0.407928 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/42` | 0.407928 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/30` | 0.407928 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/27` | 0.399439 | **CONCEAL SPELL **[one-action] **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/3/SectionHeader/20` | 0.380021 | SKILL FEATS 2ND |

### Query 116
- Text: What are the requirements for **WILD BOND** **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/41', 'PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/31', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/36']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/41', 'PZO22001 Starfinder Player Core 114-125::/page/8/Text/40', 'PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/43']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/8/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/43` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/41` | 0.872366 | **WILD BOND** **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/31` | 0.657960 | **ELDRITCH BOND** **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/36` | 0.574911 | **RADIANT BOND** **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/18` | 0.522501 | **BOND BOOST **[reaction] **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/26` | 0.481056 | **XENODRUID BOND** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/51` | 0.479674 | **DATA BOND** **FEAT 10** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/605` | 0.478574 | Wild Bond |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/13` | 0.474355 | **DIVINE BOND** **FEAT 1** **MYSTIC** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/3/SectionHeader/20` | 0.469485 | SKILL FEATS 2ND |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/2` | 0.449105 | LIFE BOND FEAT 10 |

### Query 117
- Text: What are the requirements for **Prerequisites** connection with primal spellcasting?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/8/Text/44']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/10/Text/4', 'PZO22001 Starfinder Player Core 114-125::/page/8/Text/44', 'PZO22001 Starfinder Player Core 114-125::/page/7/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/8/Text/44', 'PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/43', 'PZO22001 Starfinder Player Core 114-125::/page/8/Text/45']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/43` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/8/Text/45` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/4` | 0.977786 | **Prerequisites** connection with primal spellcasting |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/44` | 0.977786 | **Prerequisites** connection with primal spellcasting |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/29` | 0.977786 | **Prerequisites** connection with primal spellcasting |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/34` | 0.711933 | **Prerequisites** connection with occult spellcasting |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/54` | 0.711933 | **Prerequisites** connection with occult spellcasting |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/14` | 0.626956 | **Prerequisites** connection with divine spellcasting, you  worship a deity |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/16` | 0.552485 | Prerequisites elemental connection |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/22` | 0.537314 | **Tradition** primal; **Connection Skill** Performance |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/7` | 0.517898 | **Tradition** primal; **Connection Skill** Nature |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/389` | 0.511687 | Ancestry and background, attribute boosts, initial proficiencies, connection, initial epiphany, mystic bond, vitality network, mystic spellcasting, spell repertoire |

### Query 118
- Text: What are the requirements for **ADAPTIVE DEFENSE **[one-action] **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/3', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/527', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/3', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/5', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/3` | 0.917323 | **ADAPTIVE DEFENSE **[one-action] **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/527` | 0.620654 | Adaptive Defense |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/14` | 0.533930 | **MENTAL INTERFERENCE **[one-action] **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/1/SectionHeader/61` | 0.477031 | **DEFENSES** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/20` | 0.472240 | **WASTE NOT **[one-action] **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/10` | 0.417593 | **EXTENDED VITALITY** **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/25` | 0.408425 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/42` | 0.397020 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/30` | 0.397020 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/41` | 0.397020 | **SKILLS** **FEATS** |

### Query 119
- Text: What are the requirements for **CLOUD STORAGE** **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/7', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/537', 'PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/1011']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/7', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/8', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/9/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/7` | 0.916971 | **CLOUD STORAGE** **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/537` | 0.582671 | Cloud Storage |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/1011` | 0.441247 | 4 |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/1012` | 0.411247 | 4 |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/538` | 0.411247 | 4 |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/939` | 0.399247 | 4 |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/963` | 0.399247 | 4 |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/964` | 0.399247 | 4 |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/989` | 0.399247 | 4 |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/937` | 0.399247 | 4 |

### Query 120
- Text: What are the requirements for **EXTENDED VITALITY** **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/10', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/561', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/10', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/12', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/9/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/10` | 0.894862 | **EXTENDED VITALITY** **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/561` | 0.652998 | Extended Vitality |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/8` | 0.473629 | **VITALITY WEB** **FEAT 16** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/20` | 0.422984 | **TRANSFER VITALITY **[one-action] |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/17` | 0.412145 | VITALITY NETWORK |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/28` | 0.408403 | **TRANSCENDED EXISTENCE** **FEAT 20** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/3` | 0.405626 | **ADAPTIVE DEFENSE **[one-action] **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/7/Table/3` | 0.403159 | FeatLevelAdaptive Defense4Advanced Epiphany8Bond Boost2Bond Spell14Cantrip Expansion2Cloud Storage4Conceal Spell2Convert Elemental Essence12Convert Illumination12Convert Information12Convert Life Forc |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/23` | 0.397506 | **CANTRIP EXPANSION** **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/1011` | 0.397353 | 4 |

### Query 121
- Text: What are the requirements for **MENTAL INTERFERENCE **[one-action] **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/14', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/573', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/14', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/13', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/9/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/14` | 0.921065 | **MENTAL INTERFERENCE **[one-action] **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/573` | 0.611557 | Mental Interference |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/20` | 0.584346 | **WASTE NOT **[one-action] **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/3` | 0.523081 | **ADAPTIVE DEFENSE **[one-action] **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/27` | 0.439109 | **CONCEAL SPELL **[one-action] **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/22` | 0.426007 | **WIDEN SPELL **[one-action] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/49` | 0.425018 | You create duplicates of your consciousness capable of fending  off mental intrusion. Attempt to counteract an effect of your  choice imposing one of the triggering conditions, using half  your level |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/13` | 0.412612 | **NETWORK ATTUNEMENT **[one-action] **FEAT 18** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/45` | 0.412086 | **TRIPARTITE MIND **[reaction] **FEAT 8** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/18` | 0.411597 | **REACH SPELL **[one-action] **FEAT 1** |

### Query 122
- Text: What are the requirements for **WASTE NOT **[one-action] **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/20', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/14', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/20', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/22', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/9/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/20` | 0.897643 | **WASTE NOT **[one-action] **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/14` | 0.584675 | **MENTAL INTERFERENCE **[one-action] **FEAT 4** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/3` | 0.527854 | **ADAPTIVE DEFENSE **[one-action] **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/601` | 0.445658 | Waste Not |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/22` | 0.433713 | **WIDEN SPELL **[one-action] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/18` | 0.431858 | **REACH SPELL **[one-action] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/27` | 0.417415 | **CONCEAL SPELL **[one-action] **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/3/Text/42` | 0.415844 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/30` | 0.415844 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/41` | 0.415844 | **SKILLS** **FEATS** |

### Query 123
- Text: What are the requirements for **NETWORK SHIELD **[reaction] **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/26', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/579', 'PZO22001 Starfinder Player Core 114-125::/page/3/SectionHeader/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/26', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/25', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/28']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/26` | 0.907036 | **NETWORK SHIELD **[reaction] **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/579` | 0.598034 | Network Shield |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/3/SectionHeader/29` | 0.525576 | **NETWORK SPELL **[one-action] |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/13` | 0.475070 | **NETWORK ATTUNEMENT **[one-action] **FEAT 18** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/36` | 0.408856 | **RADIANT BOND** **FEAT 6** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/Table/16` | 0.393155 | FeatLevelLife Bond10Mental Interference4Mystic Luminary6Network Attunement18Network Shield6New Epiphany6Quickened Casting10Radiant Bond6Reach Spell1Realized Epiphany18Spot Healing2Syncretic Epiphany16 |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/31` | 0.388489 | **NEW EPIPHANY** **FEAT 6** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/18` | 0.384990 | **REACH SPELL **[one-action] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/30` | 0.384328 | You condense the energy of your vitality network into a  shield. You gain resistance equal to twice your level against  all damage from the triggering attack or effect. Reduce your  vitality network's |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/21` | 0.380518 | **Prerequisites** shadow connection |

### Query 124
- Text: What are the requirements for **NEW EPIPHANY** **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/31', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/41', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/31', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/33', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/9/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/31` | 0.906213 | **NEW EPIPHANY** **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/41` | 0.670684 | **ADVANCED EPIPHANY** **FEAT 8** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/1` | 0.631012 | **SYNCRETIC EPIPHANY** **FEAT 16** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/6` | 0.559018 | GREATER EPIPHANY FEAT 10 |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/581` | 0.544563 | New Epiphany |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/18` | 0.535760 | **REALIZED EPIPHANY **[one-action] **FEAT 18** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/11` | 0.526242 | INITIAL EPIPHANY |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/10` | 0.459128 | **Epiphany Spells **initial: *elemental weapon*; advanced:  *elemental barrier*; greater: *elemental nova* |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/529` | 0.458361 | Advanced Epiphany |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/563` | 0.438110 | Greater Epiphany |

### Query 125
- Text: What are the requirements for **Prerequisites** expert in a connection skill other than that of  your chosen connection?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/9/Text/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/9/Text/34', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/6', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/9/Text/34', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/35', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/33']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/9/Text/35` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/33` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/34` | 0.962705 | **Prerequisites** expert in a connection skill other than that of  your chosen connection |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/6` | 0.839393 | **Prerequisites** master in a connection skill for a connection that  you've learned the initial epiphany for and that isn't your  chosen connection |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/26` | 0.699355 | **Prerequisites** legendary in your connection skill |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/19` | 0.657355 | **Prerequisites** legendary in your connection skill |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/7` | 0.612738 | Plumbing the depths of your own connection, you  understand how your piece of reality interconnects  with another. You learn the advanced epiphany spell of  the connection that grants training in the |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/21` | 0.589999 | **Prerequisites** shadow connection |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/31` | 0.587988 | **Prerequisites** healing connection |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/16` | 0.587753 | Prerequisites elemental connection |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/57` | 0.581043 | Trained in one skill determined by  your connection |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/22` | 0.552549 | **Tradition** primal; **Connection Skill** Performance |

### Query 126
- Text: What are the requirements for **RADIANT BOND** **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/36']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/36', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/585', 'PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/41']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/36', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/38', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/35']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/38` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/9/Text/35` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/36` | 0.912181 | **RADIANT BOND** **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/585` | 0.623056 | Radiant Bond |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/41` | 0.573839 | **WILD BOND** **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/51` | 0.503452 | **DATA BOND** **FEAT 10** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/26` | 0.488949 | **XENODRUID BOND** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/31` | 0.486537 | **ELDRITCH BOND** **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/2` | 0.454637 | LIFE BOND FEAT 10 |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/13` | 0.448661 | **DIVINE BOND** **FEAT 1** **MYSTIC** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/18` | 0.413814 | **BOND BOOST **[reaction] **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/31` | 0.410661 | **NEW EPIPHANY** **FEAT 6** |

### Query 127
- Text: What are the requirements for **ADVANCED EPIPHANY** **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/41', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/31', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/41', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/43', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/40']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/43` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/40` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/41` | 0.912847 | **ADVANCED EPIPHANY** **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/31` | 0.663091 | **NEW EPIPHANY** **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/18` | 0.594665 | **REALIZED EPIPHANY **[one-action] **FEAT 18** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/1` | 0.533371 | **SYNCRETIC EPIPHANY** **FEAT 16** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/6` | 0.532628 | GREATER EPIPHANY FEAT 10 |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/529` | 0.516079 | Advanced Epiphany |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/11` | 0.505626 | INITIAL EPIPHANY |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/17` | 0.434749 | **Epiphany Spells **initial: *akashic* *fount*; advanced: *akashic * *assistant*; greater: *data drain* |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/581` | 0.429729 | New Epiphany |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/10` | 0.423461 | **Epiphany Spells **initial: *elemental weapon*; advanced:  *elemental barrier*; greater: *elemental nova* |

### Query 128
- Text: What are the requirements for **TRIPARTITE MIND **[reaction] **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/45']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/45', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/597', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/45', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/47', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/44']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/9/Text/44` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/45` | 0.899090 | **TRIPARTITE MIND **[reaction] **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/597` | 0.618695 | Tripartite Mind |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/14` | 0.456114 | **MENTAL INTERFERENCE **[one-action] **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/41` | 0.393856 | **ADVANCED EPIPHANY** **FEAT 8** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/598` | 0.385054 | 8 |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/13` | 0.379403 | **NETWORK ATTUNEMENT **[one-action] **FEAT 18** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/402` | 0.373054 | 8 |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/530` | 0.373054 | 8 |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/959` | 0.373054 | 8 |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/26` | 0.361146 | **NETWORK SHIELD **[reaction] **FEAT 6** |

### Query 129
- Text: What are the requirements for **DATA BOND** **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/51']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/51', 'PZO22001 Starfinder Player Core 114-125::/page/10/Text/2', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/551']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/51', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/50', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/53']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/50` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/53` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/51` | 0.902886 | **DATA BOND** **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/2` | 0.663937 | LIFE BOND FEAT 10 |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/551` | 0.555230 | Data Bond |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/36` | 0.507971 | **RADIANT BOND** **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/41` | 0.482738 | **WILD BOND** **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/26` | 0.467258 | **XENODRUID BOND** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/13` | 0.447351 | **DIVINE BOND** **FEAT 1** **MYSTIC** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/31` | 0.439488 | **ELDRITCH BOND** **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/9` | 0.421173 | QUICKENED CASTING ♦ FEAT 10 |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/8/SectionHeader/18` | 0.408469 | **BOND BOOST **[reaction] **FEAT 2** |

### Query 130
- Text: What are the requirements for **Prerequisites** connection with occult spellcasting?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/9/Text/54']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/9/Text/54', 'PZO22001 Starfinder Player Core 114-125::/page/8/Text/34', 'PZO22001 Starfinder Player Core 114-125::/page/8/Text/44']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/9/Text/54', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/55', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/53']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/9/Text/55` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/53` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/54` | 0.974784 | **Prerequisites** connection with occult spellcasting |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/34` | 0.974784 | **Prerequisites** connection with occult spellcasting |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/44` | 0.766293 | **Prerequisites** connection with primal spellcasting |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/4` | 0.724293 | **Prerequisites** connection with primal spellcasting |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/29` | 0.724293 | **Prerequisites** connection with primal spellcasting |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/14` | 0.716404 | **Prerequisites** connection with divine spellcasting, you  worship a deity |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/15` | 0.554222 | **Tradition** occult; **Connection Skill** Occultism |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/26` | 0.543104 | Prerequisites akashic connection |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/21` | 0.532992 | **Prerequisites** shadow connection |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/16` | 0.523909 | Prerequisites elemental connection |

### Query 131
- Text: What are the requirements for **Prerequisites** connection with primal spellcasting?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/10/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/10/Text/4', 'PZO22001 Starfinder Player Core 114-125::/page/8/Text/44', 'PZO22001 Starfinder Player Core 114-125::/page/7/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/10/Text/4', 'PZO22001 Starfinder Player Core 114-125::/page/10/Text/5', 'PZO22001 Starfinder Player Core 114-125::/page/10/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/10/Text/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/10/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/4` | 0.977786 | **Prerequisites** connection with primal spellcasting |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/44` | 0.977786 | **Prerequisites** connection with primal spellcasting |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/29` | 0.977786 | **Prerequisites** connection with primal spellcasting |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/34` | 0.711933 | **Prerequisites** connection with occult spellcasting |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/54` | 0.711933 | **Prerequisites** connection with occult spellcasting |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/14` | 0.626956 | **Prerequisites** connection with divine spellcasting, you  worship a deity |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/16` | 0.552485 | Prerequisites elemental connection |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/22` | 0.537314 | **Tradition** primal; **Connection Skill** Performance |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/7` | 0.517898 | **Tradition** primal; **Connection Skill** Nature |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/389` | 0.511687 | Ancestry and background, attribute boosts, initial proficiencies, connection, initial epiphany, mystic bond, vitality network, mystic spellcasting, spell repertoire |

### Query 132
- Text: What are the requirements for **Prerequisites** shadow connection?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/10/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/10/Text/21', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/34', 'PZO22001 Starfinder Player Core 114-125::/page/10/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/10/Text/21', 'PZO22001 Starfinder Player Core 114-125::/page/10/Text/20', 'PZO22001 Starfinder Player Core 114-125::/page/10/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/10/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/10/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/21` | 0.955333 | **Prerequisites** shadow connection |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/34` | 0.623458 | **Prerequisites** expert in a connection skill other than that of  your chosen connection |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/26` | 0.619112 | Prerequisites akashic connection |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/16` | 0.573945 | Prerequisites elemental connection |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/31` | 0.548275 | **Prerequisites** healing connection |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/6` | 0.546260 | **Prerequisites** master in a connection skill for a connection that  you've learned the initial epiphany for and that isn't your  chosen connection |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/19` | 0.526010 | **Prerequisites** legendary in your connection skill |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/26` | 0.526010 | **Prerequisites** legendary in your connection skill |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/36` | 0.509050 | Prerequisites rhythm connection |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/34` | 0.500678 | **Prerequisites** connection with occult spellcasting |

### Query 133
- Text: What are the requirements for **Prerequisites** healing connection?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/10/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/10/Text/31', 'PZO22001 Starfinder Player Core 114-125::/page/10/Text/16', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/34']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/10/Text/31', 'PZO22001 Starfinder Player Core 114-125::/page/10/Text/32', 'PZO22001 Starfinder Player Core 114-125::/page/10/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/10/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/10/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/31` | 0.938436 | **Prerequisites** healing connection |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/16` | 0.684286 | Prerequisites elemental connection |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/34` | 0.657517 | **Prerequisites** expert in a connection skill other than that of  your chosen connection |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/26` | 0.613071 | Prerequisites akashic connection |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/6` | 0.590694 | **Prerequisites** master in a connection skill for a connection that  you've learned the initial epiphany for and that isn't your  chosen connection |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/21` | 0.588716 | **Prerequisites** shadow connection |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/19` | 0.557547 | **Prerequisites** legendary in your connection skill |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/26` | 0.557547 | **Prerequisites** legendary in your connection skill |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/36` | 0.554106 | Prerequisites rhythm connection |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/8` | 0.477570 | CONNECTION |

### Query 134
- Text: What are the requirements for **SYNCRETIC EPIPHANY** **FEAT 16**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/11/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/11/Text/1', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/31', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/41']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/11/Text/1', 'PZO22001 Starfinder Player Core 114-125::/page/10/Text/56', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/10/Text/56` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/11/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/1` | 0.894992 | **SYNCRETIC EPIPHANY** **FEAT 16** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/31` | 0.651684 | **NEW EPIPHANY** **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/41` | 0.607247 | **ADVANCED EPIPHANY** **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/18` | 0.542500 | **REALIZED EPIPHANY **[one-action] **FEAT 18** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/53` | 0.527417 | FEAT 16 |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/593` | 0.524886 | Syncretic Epiphany |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/6` | 0.510528 | GREATER EPIPHANY FEAT 10 |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/11` | 0.484821 | INITIAL EPIPHANY |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/8` | 0.449065 | **VITALITY WEB** **FEAT 16** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/529` | 0.445481 | Advanced Epiphany |

### Query 135
- Text: What are the requirements for **Prerequisites** master in a connection skill for a connection that  you've learned the initial epiphany for and that isn't your  chosen connection?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/11/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/11/Text/6', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/34', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/11/Text/6', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/7', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/11/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/11/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/6` | 0.971354 | **Prerequisites** master in a connection skill for a connection that  you've learned the initial epiphany for and that isn't your  chosen connection |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/34` | 0.845208 | **Prerequisites** expert in a connection skill other than that of  your chosen connection |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/7` | 0.751905 | Plumbing the depths of your own connection, you  understand how your piece of reality interconnects  with another. You learn the advanced epiphany spell of  the connection that grants training in the |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/35` | 0.661915 | Through dedication or serendipity, you've branched out to  explore other connections to the fundamental building blocks of  the cosmos. You learn the initial epiphany spell of a connection  that grant |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/44` | 0.630647 | You gain a deeper understanding of your connection. You gain  the advanced epiphany spell for your chosen connection. |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/19` | 0.620601 | **Prerequisites** legendary in your connection skill |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/26` | 0.620601 | **Prerequisites** legendary in your connection skill |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/1/Text/57` | 0.585912 | Trained in one skill determined by  your connection |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/16` | 0.582037 | Prerequisites elemental connection |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/21` | 0.581860 | **Prerequisites** shadow connection |

### Query 136
- Text: What are the requirements for **VITALITY WEB** **FEAT 16**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/11/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/11/Text/8', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/599', 'PZO22001 Starfinder Player Core 114-125::/page/10/Text/53']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/11/Text/8', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/10', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/11/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/11/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/8` | 0.882201 | **VITALITY WEB** **FEAT 16** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/599` | 0.603681 | Vitality Web |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/53` | 0.580205 | FEAT 16 |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/17` | 0.508586 | VITALITY NETWORK |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/10` | 0.425426 | **EXTENDED VITALITY** **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/600` | 0.425158 | 16 |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/418` | 0.413158 | 16 |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/1055` | 0.413157 | 16 |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/594` | 0.413157 | 16 |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/556` | 0.413157 | 16 |

### Query 137
- Text: What are the requirements for **NETWORK ATTUNEMENT **[one-action] **FEAT 18**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/13', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/577', 'PZO22001 Starfinder Player Core 114-125::/page/3/SectionHeader/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/13', 'PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/12', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/11/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/13` | 0.924448 | **NETWORK ATTUNEMENT **[one-action] **FEAT 18** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/577` | 0.631648 | Network Attunement |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/3/SectionHeader/29` | 0.525438 | **NETWORK SPELL **[one-action] |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/18` | 0.459459 | **REALIZED EPIPHANY **[one-action] **FEAT 18** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/26` | 0.434264 | **NETWORK SHIELD **[reaction] **FEAT 6** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/14` | 0.398975 | **MENTAL INTERFERENCE **[one-action] **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/3` | 0.391842 | **ADAPTIVE DEFENSE **[one-action] **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/7/SectionHeader/18` | 0.382932 | **REACH SPELL **[one-action] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/23` | 0.381824 | **ENLIGHTENMENT** **FEAT 20** |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/20` | 0.371488 | **WASTE NOT **[one-action] **FEAT 4** |

### Query 138
- Text: What are the requirements for **REALIZED EPIPHANY **[one-action] **FEAT 18**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/11/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/11/Text/18', 'PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/41', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/11/Text/18', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/19', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/11/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/11/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/18` | 0.917528 | **REALIZED EPIPHANY **[one-action] **FEAT 18** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/41` | 0.646920 | **ADVANCED EPIPHANY** **FEAT 8** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/1` | 0.601503 | **SYNCRETIC EPIPHANY** **FEAT 16** |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/31` | 0.539092 | **NEW EPIPHANY** **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/13` | 0.512122 | **NETWORK ATTUNEMENT **[one-action] **FEAT 18** |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/2/SectionHeader/11` | 0.487732 | INITIAL EPIPHANY |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/6` | 0.466912 | GREATER EPIPHANY FEAT 10 |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/589` | 0.459482 | Realized Epiphany |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/6/Text/10` | 0.425609 | **Epiphany Spells **initial: *elemental weapon*; advanced:  *elemental barrier*; greater: *elemental nova* |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/12` | 0.420609 | feature. You gain the initial epiphany at 1st level and can  gain the advanced and greater epiphanies by selecting the  Advanced Epiphany (page 123) and Greater Epiphany (page  124) feats. You gain yo |

### Query 139
- Text: What are the requirements for **Prerequisites** legendary in your connection skill?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/11/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/11/Text/19', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/26', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/34']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/11/Text/19', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/20', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/11/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/11/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/19` | 0.948717 | **Prerequisites** legendary in your connection skill |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/26` | 0.948717 | **Prerequisites** legendary in your connection skill |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/34` | 0.743345 | **Prerequisites** expert in a connection skill other than that of  your chosen connection |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/6` | 0.653277 | **Prerequisites** master in a connection skill for a connection that  you've learned the initial epiphany for and that isn't your  chosen connection |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/31` | 0.589437 | **Prerequisites** healing connection |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/16` | 0.587120 | Prerequisites elemental connection |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/21` | 0.571917 | **Prerequisites** shadow connection |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/26` | 0.566727 | Prerequisites akashic connection |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/36` | 0.515457 | Prerequisites rhythm connection |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/7` | 0.513741 | Plumbing the depths of your own connection, you  understand how your piece of reality interconnects  with another. You learn the advanced epiphany spell of  the connection that grants training in the |

### Query 140
- Text: What are the requirements for **ENLIGHTENMENT** **FEAT 20**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/23', 'PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/28', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/559']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/23', 'PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/22', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/25']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/11/Text/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/23` | 0.899580 | **ENLIGHTENMENT** **FEAT 20** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/28` | 0.615164 | **TRANSCENDED EXISTENCE** **FEAT 20** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/559` | 0.527735 | Enlightenment |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/22` | 0.483669 | 20TH LEVEL |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/560` | 0.469626 | 20 |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/10/SectionHeader/19` | 0.462011 | CONVERT ILLUMINATION → FEAT 12 |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/596` | 0.457626 | 20 |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/426` | 0.457626 | 20 |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/1103` | 0.457626 | 20 |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/8` | 0.404691 | **Requirements** You're in dim light or darkness. |

### Query 141
- Text: What are the requirements for **Prerequisites** legendary in your connection skill?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/11/Text/26']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/11/Text/19', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/26', 'PZO22001 Starfinder Player Core 114-125::/page/9/Text/34']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/11/Text/26', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/25', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/11/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/11/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/19` | 0.948717 | **Prerequisites** legendary in your connection skill |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/26` | 0.948717 | **Prerequisites** legendary in your connection skill |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/9/Text/34` | 0.743345 | **Prerequisites** expert in a connection skill other than that of  your chosen connection |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/6` | 0.653277 | **Prerequisites** master in a connection skill for a connection that  you've learned the initial epiphany for and that isn't your  chosen connection |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/31` | 0.589437 | **Prerequisites** healing connection |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/16` | 0.587120 | Prerequisites elemental connection |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/21` | 0.571917 | **Prerequisites** shadow connection |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/26` | 0.566727 | Prerequisites akashic connection |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/36` | 0.515457 | Prerequisites rhythm connection |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/7` | 0.513741 | Plumbing the depths of your own connection, you  understand how your piece of reality interconnects  with another. You learn the advanced epiphany spell of  the connection that grants training in the |

### Query 142
- Text: What are the requirements for **TRANSCENDED EXISTENCE** **FEAT 20**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/28', 'PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/23', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/28', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/30', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/11/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/11/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/28` | 0.912654 | **TRANSCENDED EXISTENCE** **FEAT 20** |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/11/SectionHeader/23` | 0.625412 | **ENLIGHTENMENT** **FEAT 20** |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/31` | 0.557189 | **Prerequisites** transcendence |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/595` | 0.514653 | Transcended Existence |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/5/SectionHeader/8` | 0.436404 | TRANSCENDENCE 19TH |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/5/TableCell/1103` | 0.418301 | 20 |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/560` | 0.418301 | 20 |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/2/TableCell/426` | 0.418301 | 20 |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/596` | 0.418301 | 20 |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/9/SectionHeader/10` | 0.411268 | **EXTENDED VITALITY** **FEAT 4** |

### Query 143
- Text: What are the requirements for **Prerequisites** transcendence?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/11/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 114-125::/page/11/Text/31', 'PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/595', 'PZO22001 Starfinder Player Core 114-125::/page/5/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 114-125::/page/11/Text/31', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/30', 'PZO22001 Starfinder Player Core 114-125::/page/11/Text/32']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 114-125::/page/11/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 114-125::/page/11/Text/32` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/31` | 0.953325 | **Prerequisites** transcendence |
| 2 | `PZO22001 Starfinder Player Core 114-125::/page/7/TableCell/595` | 0.506388 | Transcended Existence |
| 3 | `PZO22001 Starfinder Player Core 114-125::/page/5/Text/3` | 0.498800 | *The transcendence class feature gives you a 10th-rank spell slot that works a bit differently from other spell slots. |
| 4 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/44` | 0.456336 | **Prerequisites** connection with primal spellcasting |
| 5 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/4` | 0.456336 | **Prerequisites** connection with primal spellcasting |
| 6 | `PZO22001 Starfinder Player Core 114-125::/page/7/Text/29` | 0.456336 | **Prerequisites** connection with primal spellcasting |
| 7 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/16` | 0.451480 | Prerequisites elemental connection |
| 8 | `PZO22001 Starfinder Player Core 114-125::/page/10/Text/26` | 0.437914 | Prerequisites akashic connection |
| 9 | `PZO22001 Starfinder Player Core 114-125::/page/11/Text/6` | 0.427905 | **Prerequisites** master in a connection skill for a connection that  you've learned the initial epiphany for and that isn't your  chosen connection |
| 10 | `PZO22001 Starfinder Player Core 114-125::/page/8/Text/34` | 0.422653 | **Prerequisites** connection with occult spellcasting |
