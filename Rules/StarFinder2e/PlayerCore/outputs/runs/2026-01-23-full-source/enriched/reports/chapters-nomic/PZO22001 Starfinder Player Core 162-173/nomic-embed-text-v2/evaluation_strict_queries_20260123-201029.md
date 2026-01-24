# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `837`
- Query count: `149`
- Evaluated queries: `149`
- Coverage: `1.0000`
- MRR: `0.8764`
- hit@1: `0.8121`
- hit@3: `0.9195`
- hit@5: `0.9664`
- hit@10: `1.0000`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

## Timings (ms)
- Embedding (chunks): `10602`
- Embedding (queries): `2269`
- Evaluation (strict): `85`
- Evaluation (expanded): `0`
- Total: `17359`

### Timing Estimates (ms)
- Evaluation (strict): `342`
- Evaluation (expanded): `None`
- Total: `13213`

## Query Details
### Query 0
- Text: Summarize WITCHWARPER
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 162-173::/page/10/Text/56', 'PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/1` | 0.962389 | WITCHWARPER |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/56` | 0.954526 | **WITCHWARPER** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/4` | 0.954526 | **WITCHWARPER** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/29` | 0.912526 | **WITCHWARPER** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/26` | 0.912526 | **WITCHWARPER** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/52` | 0.912526 | **WITCHWARPER** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/9` | 0.912526 | **WITCHWARPER** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/32` | 0.912526 | **WITCHWARPER** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/56` | 0.912526 | **WITCHWARPER** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/61` | 0.912526 | **WITCHWARPER** |

### Query 1
- Text: What is the rule about A strange paradoxical event forever altered your existence, and now you can manipulate reality. You  explore the infinite possibilities of the multiverse, possibly visualizing variant timelines or parallel  worlds. You create fields that subvert space and time, allowing you to cast powerful magic. You've  learned to focus on an anchoring memory, concept, or object to help you identify reality.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/2', 'PZO22001 Starfinder Player Core 162-173::/page/2/Text/10', 'PZO22001 Starfinder Player Core 162-173::/page/2/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/2` | 0.986285 | A strange paradoxical event forever altered your existence, and now you can manipulate reality. You  explore the infinite possibilities of the multiverse, possibly visualizing variant timelines or par |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/10` | 0.760049 | from an alternate reality or a different timeline, or perhaps  you experienced an unnatural phenomenon that altered your  path, discovered a time-glitching alien device, or wrote a  treatise on quantu |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/15` | 0.733817 | You can draw on paradoxical forces to create a reality-warping  quantum field. It might manifest as a haze in the air that shows  shimmers of alternate realities, appear as walls of glowing  magical e |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/20` | 0.668747 | Some event has unstuck you in time. You might come  from the distant past or a far-flung future. Perhaps you've  traveled from some forsaken timeline to stop a cataclysmic  event. Whatever the reason, |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/13` | 0.646730 | You reshape terrain and manipulate events to match other realities. You cast powerful  spells and recenter yourself through your anchor when pushed to your limits. |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/53` | 0.630624 | You spend 10 minutes opening yourself to the mysteries of the  multiverse by peering across different timelines or analyzing  probability simulations. You gain the effects of *augury*, except  you lea |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/11` | 0.629630 | At 1st level, choose your paradox. Your chosen paradox  determines the tradition of your spells, additional trained  skills, additional spells you learn, and the effects of your  quantum field. You al |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/8/Text/3` | 0.629464 | Your connection to a temporal anomaly allows you to  manipulate time using magic. |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/3` | 0.622041 | Your paradox grants you magical power. You can cast spells  using the Cast a Spell activity. As a witchwarper, when you  cast spells, you might describe your revelations about other  realities aloud, |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/16` | 0.620104 | Your paradox represents an event or force that forever altered  you. Your chosen paradox determines your spellcasting  tradition and grants you trained proficiency in the listed  paradox skill. You au |

### Query 2
- Text: Summarize **KEY ATTRIBUTE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/6', 'PZO22001 Starfinder Player Core 162-173::/page/6/SectionHeader/1', 'PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/6` | 0.948607 | **KEY ATTRIBUTE** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/6/SectionHeader/1` | 0.665018 | **KEY TERMS** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/4` | 0.599101 | **Attributes** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/10` | 0.471900 | **Feats** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/48` | 0.437617 | **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/39` | 0.437617 | **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/84` | 0.407698 | **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/6` | 0.398872 | **Skills** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/60` | 0.384082 | **ATTACKS** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/33` | 0.378905 | **INTRODUCTION** |

### Query 3
- Text: Summarize **Charisma or Intelligence**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/7', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/8', 'PZO22001 Starfinder Player Core 162-173::/page/8/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/7` | 1.010290 | **Charisma or Intelligence** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/8` | 0.715203 | At 1st level, your class gives you  an attribute boost to your choice  of Charisma or Intelligence. |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/8/Text/5` | 0.555471 | Prioritize Intelligence, then Dexterity and Wisdom to  improve your defenses. |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/6` | 0.499811 | Some of your spells require you to attempt a spell attack to  see how effective they are or have your enemies roll against  your spell DC (typically by attempting a saving throw). Your spell  attack m |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/59` | 0.465753 | Trained in a number of additional  skills equal to 3 plus your Intelligence  modifier |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/6` | 0.423745 | **Skills** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/5` | 0.383064 | **Prerequisites** master in a paradox skill for a paradox other  than your chosen paradox |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/57` | 0.377890 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/43` | 0.377890 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/58` | 0.362225 | Trained in one skill determined by  your paradox |

### Query 4
- Text: Summarize At 1st level, your class gives you  an attribute boost to your choice  of Charisma or Intelligence.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/8', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/31', 'PZO22001 Starfinder Player Core 162-173::/page/2/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/8` | 1.037529 | At 1st level, your class gives you  an attribute boost to your choice  of Charisma or Intelligence. |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/31` | 0.716195 | In addition to the abilities provided by your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/4` | 0.697131 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/7` | 0.666912 | **Charisma or Intelligence** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/7` | 0.593198 | At 1st level you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start  of this class. |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/5` | 0.528815 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/9` | 0.527319 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use this increase either to increase your  proficiency rank to trained in one skill you're untrained in or  to increase |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/6` | 0.526337 | Some of your spells require you to attempt a spell attack to  see how effective they are or have your enemies roll against  your spell DC (typically by attempting a saving throw). Your spell  attack m |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/29` | 0.522402 | You gain these abilities as a witchwarper. Abilities gained at higher levels list the  levels next to their names. |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/11` | 0.519130 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |

### Query 5
- Text: What is the rule about **HIT POINTS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/9', 'PZO22001 Starfinder Player Core 162-173::/page/6/SectionHeader/31', 'PZO22001 Starfinder Player Core 162-173::/page/3/Text/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/9` | 0.884304 | **HIT POINTS** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/6/SectionHeader/31` | 0.449886 | FOCAL POINT |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/13` | 0.422510 | Focus spells are automatically heightened to half your level  rounded up, much like cantrips. Focus spells don't require spell  slots, and you can't cast them using spell slots. Taking feats can  give |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/8/Text/24` | 0.373244 | You concentrate more deeply on your anchor to soothe yourself.  You gain temporary Hit Points equal to your witchwarper level  that last for 1 round. |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/48` | 0.354981 | **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/39` | 0.354981 | **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/11` | 0.348970 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/6/SectionHeader/1` | 0.348413 | **KEY TERMS** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/82` | 0.333335 | **CONDITIONS ** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/60` | 0.327885 | **ATTACKS** |

### Query 6
- Text: What is the rule about **8 + Constitution modifier**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 162-173::/page/2/Text/5', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/59']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/10` | 0.865498 | **8 + Constitution modifier** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/5` | 0.478496 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/59` | 0.460375 | Trained in a number of additional  skills equal to 3 plus your Intelligence  modifier |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/575` | 0.416298 | 8 |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/541` | 0.416298 | 8 |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/952` | 0.416298 | 8 |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/408` | 0.416298 | 8 |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/529` | 0.416298 | 8 |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/4` | 0.363675 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/423` | 0.355423 | 8th-rank spells, attribute boosts, general feat, master spellcaster, skill increase |

### Query 7
- Text: Summarize You increase your maximum number  of HP by this number at 1st level and  every level thereafter.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/11', 'PZO22001 Starfinder Player Core 162-173::/page/4/Text/9', 'PZO22001 Starfinder Player Core 162-173::/page/2/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/11` | 1.031874 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/9` | 0.635112 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use this increase either to increase your  proficiency rank to trained in one skill you're untrained in or  to increase |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/5` | 0.604495 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/29` | 0.544411 | You gain these abilities as a witchwarper. Abilities gained at higher levels list the  levels next to their names. |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/10` | 0.543409 | At 7th level, you can use skill increases to increase your  proficiency rank to master in a skill in which you're already  an expert, and at 15th level, you can use them to increase  your proficiency |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/3` | 0.526529 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/4` | 0.520901 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/18` | 0.514353 | You add to this spell repertoire as you increase in level.  Each time you get a spell slot (see Witchwarper Spells per  Day on page 167), you add a spell to your spell repertoire of  the same rank. At |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/52` | 0.514252 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/7` | 0.511936 | At 1st level you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start  of this class. |

### Query 8
- Text: Summarize DURING COMBAT ENCOUNTERS...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/12', 'PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/12` | 0.983036 | DURING COMBAT ENCOUNTERS... |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/14` | 0.745777 | DURING SOCIAL ENCOUNTERS... |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/16` | 0.434305 | WHILE EXPLORING... |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/18` | 0.337787 | IN DOWNTIME... |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/75` | 0.333292 | **Soldier** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/40` | 0.333292 | **Soldier** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/38` | 0.333292 | **Soldier** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/4` | 0.326510 | **ANCHORING** **CONCENTRATE** **WITCHWARPER** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/47` | 0.326510 | **ANCHORING** **CONCENTRATE** **WITCHWARPER** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/18` | 0.323311 | **ANCHORING** **CONCENTRATE** **MANIPULATE** **WITCHWARPER** **ZONE** |

### Query 9
- Text: What is the rule about You reshape terrain and manipulate events to match other realities. You cast powerful  spells and recenter yourself through your anchor when pushed to your limits.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/13', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/2', 'PZO22001 Starfinder Player Core 162-173::/page/3/Text/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/13` | 0.917532 | You reshape terrain and manipulate events to match other realities. You cast powerful  spells and recenter yourself through your anchor when pushed to your limits. |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/2` | 0.613612 | A strange paradoxical event forever altered your existence, and now you can manipulate reality. You  explore the infinite possibilities of the multiverse, possibly visualizing variant timelines or par |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/3` | 0.602339 | Your paradox grants you magical power. You can cast spells  using the Cast a Spell activity. As a witchwarper, when you  cast spells, you might describe your revelations about other  realities aloud, |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/49` | 0.540352 | By reaching across both time and space, you can borrow the  use of a spell from a version of yourself inhabiting another  reality. During this turn, you can cast one spell without  spending a spell sl |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/19` | 0.538282 | You craft magic items for your party. You might travel to other dimensions or distant  star systems as part of your training or embark on such journeys by accident. |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/26` | 0.537886 | Your anchor keeps you centered, reminding you what's  real, and helps counter the disorienting effects one might  experience by causing paradoxes. You select your anchor at 1st  level. Your anchor gra |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/32` | 0.522913 | You become a true embodiment of your paradox and surpass  what mortals can achieve in your reality. You gain an additional  10th-rank spell slot. |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/3` | 0.522458 | **Anchoring:** You can use abilities with the anchoring  trait only while your quantum field is activated. If you  use the ability on your turn, in addition to their stated  effects, they automaticall |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/4` | 0.518566 | **Spellshape:** Actions with the spellshape trait tweak  the properties of your spells. These actions usually  come from spellshape feats. You must use a spellshape  action directly before Casting the |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/9` | 0.516280 | Your existence is contrary to the status quo of the universe,  causing quantum ripples that empower your spellcasting  talent and open doorways to other worlds. Perhaps you're |

### Query 10
- Text: Summarize DURING SOCIAL ENCOUNTERS...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/12', 'PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/14` | 0.977694 | DURING SOCIAL ENCOUNTERS... |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/12` | 0.728104 | DURING COMBAT ENCOUNTERS... |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/16` | 0.408727 | WHILE EXPLORING... |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/18` | 0.315217 | IN DOWNTIME... |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/24` | 0.286287 | OTHERS PROBABLY... |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/20` | 0.285896 | YOU MIGHT... |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/71` | 0.282589 | **Envoy** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/34` | 0.282589 | **Envoy** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/36` | 0.282589 | **Envoy** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/25` | 0.282589 | **Envoy** |

### Query 11
- Text: Summarize You might solve problems with deductive reasoning or by determining mathematic  probabilities, drawing on your deep knowledge of the multiverse.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/15', 'PZO22001 Starfinder Player Core 162-173::/page/11/Text/17', 'PZO22001 Starfinder Player Core 162-173::/page/9/Text/53']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/15` | 1.037244 | You might solve problems with deductive reasoning or by determining mathematic  probabilities, drawing on your deep knowledge of the multiverse. |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/17` | 0.614644 | The multiverse is a complex game—you use alternate realities to |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/53` | 0.608321 | You spend 10 minutes opening yourself to the mysteries of the  multiverse by peering across different timelines or analyzing  probability simulations. You gain the effects of *augury*, except  you lea |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/2` | 0.552701 | A strange paradoxical event forever altered your existence, and now you can manipulate reality. You  explore the infinite possibilities of the multiverse, possibly visualizing variant timelines or par |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/10` | 0.482758 | from an alternate reality or a different timeline, or perhaps  you experienced an unnatural phenomenon that altered your  path, discovered a time-glitching alien device, or wrote a  treatise on quantu |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/6` | 0.479096 | Your paradoxical nature has become multifaceted. During daily  preparations, you can replace one of your paradox spells with a  spell of another paradox that grants training in the prerequisite  parad |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/11` | 0.469516 | At 1st level, choose your paradox. Your chosen paradox  determines the tradition of your spells, additional trained  skills, additional spells you learn, and the effects of your  quantum field. You al |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/15` | 0.467216 | Your awareness of possible dangers, through incredible  analysis or an understanding of the wider multiverse,  increases your reflexes. Your proficiency rank for Reflex  saves increases to expert. |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/10` | 0.460439 | You breach the veil of paradoxical understanding. You gain  the greater warp spell for your paradox. |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/18` | 0.460262 | There's a hidden code that powers the Universe and realms  beyond, and by focusing your intellect, you can tap into it and  see the equations. |

### Query 12
- Text: Summarize WHILE EXPLORING...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/16', 'PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/16` | 0.945993 | WHILE EXPLORING... |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/14` | 0.439598 | DURING SOCIAL ENCOUNTERS... |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/12` | 0.437469 | DURING COMBAT ENCOUNTERS... |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/18` | 0.348777 | IN DOWNTIME... |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/44` | 0.330508 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/45` | 0.330508 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/43` | 0.330508 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/81` | 0.330508 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/34` | 0.330508 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/47` | 0.330508 | **PLAYING THE ** **GAME** |

### Query 13
- Text: What is the rule about You seek magical auras and provide guidance regarding supernatural phenomena you  encounter while analyzing the environment around you. You might use *spell gems* to  bypass obstacles and protect yourself from dangerous environments.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/17', 'PZO22001 Starfinder Player Core 162-173::/page/10/Text/42', 'PZO22001 Starfinder Player Core 162-173::/page/3/Text/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/17` | 0.960448 | You seek magical auras and provide guidance regarding supernatural phenomena you  encounter while analyzing the environment around you. You might use *spell gems* to  bypass obstacles and protect your |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/42` | 0.654264 | You possess an uncanny sixth sense for ambient magic. You  can sense the presence of magic auras as though you were  always using a 1st-rank *detect magic* spell. This detects magic  in your field of |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/3` | 0.594448 | Your paradox grants you magical power. You can cast spells  using the Cast a Spell activity. As a witchwarper, when you  cast spells, you might describe your revelations about other  realities aloud, |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/19` | 0.551993 | You craft magic items for your party. You might travel to other dimensions or distant  star systems as part of your training or embark on such journeys by accident. |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/9` | 0.541877 | Your existence is contrary to the status quo of the universe,  causing quantum ripples that empower your spellcasting  talent and open doorways to other worlds. Perhaps you're |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/13` | 0.518298 | You reshape terrain and manipulate events to match other realities. You cast powerful  spells and recenter yourself through your anchor when pushed to your limits. |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/18` | 0.505217 | **Quantum Field** Supernatural static obscures you from sight.  You're concealed to creatures within your quantum field.  When a creature within your quantum field hits you with  an attack, you lose t |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/15` | 0.501791 | You can draw on paradoxical forces to create a reality-warping  quantum field. It might manifest as a haze in the air that shows  shimmers of alternate realities, appear as walls of glowing  magical e |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/30` | 0.498614 | You allow your mind to wander to things you find pleasant,  briefly shutting out all realities and protecting you from harm.  You gain a +2 status bonus to saving throws against mental  effects until |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/35` | 0.498572 | **Trigger** You cast a 2nd-rank or higher spell, and the spell  targets a creature or area within your quantum field. |

### Query 14
- Text: Summarize IN DOWNTIME...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/20', 'PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/18` | 0.786911 | IN DOWNTIME... |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/20` | 0.405938 | YOU MIGHT... |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/14` | 0.367088 | DURING SOCIAL ENCOUNTERS... |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/16` | 0.322232 | WHILE EXPLORING... |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/12` | 0.314851 | DURING COMBAT ENCOUNTERS... |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/24` | 0.302606 | OTHERS PROBABLY... |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/6/SectionHeader/1` | 0.287179 | **KEY TERMS** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/10` | 0.282115 | **Feats** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/SectionHeader/22` | 0.272339 | **QUANTUM PULSE **[free-action] |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/33` | 0.271423 | **INTRODUCTION** |

### Query 15
- Text: What is the rule about You craft magic items for your party. You might travel to other dimensions or distant  star systems as part of your training or embark on such journeys by accident.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/19', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/17', 'PZO22001 Starfinder Player Core 162-173::/page/3/Text/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/19` | 0.920364 | You craft magic items for your party. You might travel to other dimensions or distant  star systems as part of your training or embark on such journeys by accident. |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/17` | 0.540809 | You seek magical auras and provide guidance regarding supernatural phenomena you  encounter while analyzing the environment around you. You might use *spell gems* to  bypass obstacles and protect your |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/3` | 0.538148 | Your paradox grants you magical power. You can cast spells  using the Cast a Spell activity. As a witchwarper, when you  cast spells, you might describe your revelations about other  realities aloud, |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/49` | 0.484939 | By reaching across both time and space, you can borrow the  use of a spell from a version of yourself inhabiting another  reality. During this turn, you can cast one spell without  spending a spell sl |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/13` | 0.481419 | You reshape terrain and manipulate events to match other realities. You cast powerful  spells and recenter yourself through your anchor when pushed to your limits. |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/11` | 0.461732 | At 1st level, choose your paradox. Your chosen paradox  determines the tradition of your spells, additional trained  skills, additional spells you learn, and the effects of your  quantum field. You al |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/9` | 0.460160 | Your existence is contrary to the status quo of the universe,  causing quantum ripples that empower your spellcasting  talent and open doorways to other worlds. Perhaps you're |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/2` | 0.459796 | A strange paradoxical event forever altered your existence, and now you can manipulate reality. You  explore the infinite possibilities of the multiverse, possibly visualizing variant timelines or par |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/8/Text/42` | 0.457152 | **Trigger** A creature, trap, or similar object within your quantum  field casts a spell that you don't have in your spell repertoire,  and you're aware of the casting. |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/21` | 0.455265 | You temporarily share your quantum field with an ally. You  cause your quantum field to emanate from an ally you can  see instead of yourself. The ally gains all the benefits of your  quantum field, a |

### Query 16
- Text: Summarize YOU MIGHT...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/20', 'PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/24', 'PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/20` | 0.903204 | YOU MIGHT... |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/24` | 0.522471 | OTHERS PROBABLY... |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/18` | 0.362798 | IN DOWNTIME... |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/49` | 0.318160 | **PREDICT OUTCOME** **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/16` | 0.315404 | WHILE EXPLORING... |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/12` | 0.303473 | DURING COMBAT ENCOUNTERS... |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/10` | 0.279989 | **8 + Constitution modifier** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/17` | 0.278624 | You seek magical auras and provide guidance regarding supernatural phenomena you  encounter while analyzing the environment around you. You might use *spell gems* to  bypass obstacles and protect your |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/6/SectionHeader/1` | 0.278501 | **KEY TERMS** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/72` | 0.275093 | **Mystic** |

### Query 17
- Text: Summarize Travel to distant destinations and hunt for secret knowledge.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/ListItem/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/ListItem/21', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/19', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/ListItem/21` | 0.997888 | Travel to distant destinations and hunt for secret knowledge. |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/19` | 0.584555 | You craft magic items for your party. You might travel to other dimensions or distant  star systems as part of your training or embark on such journeys by accident. |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/17` | 0.493098 | You seek magical auras and provide guidance regarding supernatural phenomena you  encounter while analyzing the environment around you. You might use *spell gems* to  bypass obstacles and protect your |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/4` | 0.432935 | paradoxes and alternate realities. Your focal point might be  a field of study, an abstract concept, a hobby, or even your  favorite media. |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/28` | 0.431456 | No matter where you travel, precious memories keep you  tethered to reality. Whatever the nature and number of your  memories, you can focus on them to remind yourself which of  the infinite possible |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/2` | 0.391225 | A strange paradoxical event forever altered your existence, and now you can manipulate reality. You  explore the infinite possibilities of the multiverse, possibly visualizing variant timelines or par |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/10` | 0.387553 | from an alternate reality or a different timeline, or perhaps  you experienced an unnatural phenomenon that altered your  path, discovered a time-glitching alien device, or wrote a  treatise on quantu |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/18` | 0.381103 | There's a hidden code that powers the Universe and realms  beyond, and by focusing your intellect, you can tap into it and  see the equations. |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/49` | 0.378603 | By reaching across both time and space, you can borrow the  use of a spell from a version of yourself inhabiting another  reality. During this turn, you can cast one spell without  spending a spell sl |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/20` | 0.376039 | **Paradox Spells** cantrip: *analyze* *target*; 1st: *sure strike*; 2nd:  *sift* *the* *sphere*; 3rd: *hypercognition*; 4th: *translocate*; 5th:  *subjective reality*; 6th: *truesight*; 7th: *retrocog |

### Query 18
- Text: What is the rule about Struggle to remain present without being distracted by all the possibilities.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/ListItem/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/ListItem/22', 'PZO22001 Starfinder Player Core 162-173::/page/10/Text/48', 'PZO22001 Starfinder Player Core 162-173::/page/9/Text/30']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/ListItem/22` | 0.893486 | Struggle to remain present without being distracted by all the possibilities. |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/48` | 0.450152 | **Trigger** You use an action that Sustains your quantum field,  and the quantum field is still active. |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/30` | 0.422839 | You allow your mind to wander to things you find pleasant,  briefly shutting out all realities and protecting you from harm.  You gain a +2 status bonus to saving throws against mental  effects until |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/5` | 0.379892 | You prevent creatures from leaving your quantum field and  returning to reality. Until the start of your next turn, any  creature who begins its turn inside your quantum field must  succeed at a Will |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/25` | 0.369220 | You expose this reality to a realm of pure darkness filled with  gibbering voices and otherworldly entities. The area of your  quantum field functions as though it were an area of 2ndrank *darkness*. |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/17` | 0.363389 | **Trigger** You or an ally fail a save against a mental effect while  within your quantum field. |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/20` | 0.358156 | Your quantum field activates and lasts as long as you  Sustain it (up to 10 minutes) or until the end of your next  turn. Your quantum field is a 20-foot burst centered on a  point you choose within 1 |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/8` | 0.356043 | Your existence is an anomaly that defies the normal  parameters of your current reality. You might have  encountered something that disrupted your core existence,  or you crossed the veil from an alte |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/49` | 0.348191 | By reaching across both time and space, you can borrow the  use of a spell from a version of yourself inhabiting another  reality. During this turn, you can cast one spell without  spending a spell sl |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/13` | 0.343968 | Whatever paradox altered the course of your existence,  something helps keep you anchored to reality. This might be  a physical object you carry, memories of your home, or loved  ones. At 1st level, s |

### Query 19
- Text: Summarize Remember an encounter with bizarre forces that changed you.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/ListItem/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/ListItem/23', 'PZO22001 Starfinder Player Core 162-173::/page/2/Text/10', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/ListItem/23` | 1.018428 | Remember an encounter with bizarre forces that changed you. |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/10` | 0.559924 | from an alternate reality or a different timeline, or perhaps  you experienced an unnatural phenomenon that altered your  path, discovered a time-glitching alien device, or wrote a  treatise on quantu |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/2` | 0.551382 | A strange paradoxical event forever altered your existence, and now you can manipulate reality. You  explore the infinite possibilities of the multiverse, possibly visualizing variant timelines or par |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/13` | 0.488624 | You reshape terrain and manipulate events to match other realities. You cast powerful  spells and recenter yourself through your anchor when pushed to your limits. |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/20` | 0.472659 | Some event has unstuck you in time. You might come  from the distant past or a far-flung future. Perhaps you've  traveled from some forsaken timeline to stop a cataclysmic  event. Whatever the reason, |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/18` | 0.450808 | **Quantum Field** Supernatural static obscures you from sight.  You're concealed to creatures within your quantum field.  When a creature within your quantum field hits you with  an attack, you lose t |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/23` | 0.443839 | **Trigger** An enemy damages you. |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/10` | 0.443839 | **Trigger** An enemy damages you. |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/17` | 0.440975 | **Trigger** You or an ally fail a save against a mental effect while  within your quantum field. |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/16` | 0.436949 | Your paradox represents an event or force that forever altered  you. Your chosen paradox determines your spellcasting  tradition and grants you trained proficiency in the listed  paradox skill. You au |

### Query 20
- Text: Summarize OTHERS PROBABLY...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/24', 'PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/20', 'PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/24` | 0.892334 | OTHERS PROBABLY... |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/20` | 0.536970 | YOU MIGHT... |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/16` | 0.348763 | WHILE EXPLORING... |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/34` | 0.304825 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/69` | 0.304825 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/34` | 0.304825 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/33` | 0.304825 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/22` | 0.298501 | **Prerequisites** anomaly paradox |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/27` | 0.293356 | **OTHERWORLDLY SPELL **[one-action] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/49` | 0.287481 | **PREDICT OUTCOME** **FEAT 6** |

### Query 21
- Text: Summarize Fear your abilities or worry your warps might be dangerous.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/ListItem/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/ListItem/25', 'PZO22001 Starfinder Player Core 162-173::/page/3/Text/15', 'PZO22001 Starfinder Player Core 162-173::/page/3/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/ListItem/25` | 1.031367 | Fear your abilities or worry your warps might be dangerous. |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/15` | 0.566644 | You learn warp spells based on your paradox. |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/1` | 0.563533 | You're always ready to let loose with your paradoxical  abilities, and when imperiled, you instinctively release a pulse  of quantum energy. As combat begins, you Warp Reality. |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/62` | 0.497041 | Your paradox begins to cement itself across your life. You  gain the advanced warp spell for your paradox. |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/12` | 0.465679 | You can create powerful magical phenomena known as warp  spells. Warp spells are a type of focus spell. It costs 1 Focus  Point to cast a warp spell, and you start with a focus pool  of 1 Focus Point. |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/528` | 0.462873 | Advanced Warp |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/10` | 0.460991 | You breach the veil of paradoxical understanding. You gain  the greater warp spell for your paradox. |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/20` | 0.448075 | Magical power has improved your body's  resiliency. Your proficiency rank for Fortitude  saves increases to expert. |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/2` | 0.446265 | You'll see the following key terms in many witchwarper  abilities. |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/21` | 0.442412 | You temporarily share your quantum field with an ally. You  cause your quantum field to emanate from an ally you can  see instead of yourself. The ally gains all the benefits of your  quantum field, a |

### Query 22
- Text: Summarize Dismiss your precognition or doubt your grip on your current reality.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/ListItem/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/ListItem/26', 'PZO22001 Starfinder Player Core 162-173::/page/6/Text/8', 'PZO22001 Starfinder Player Core 162-173::/page/3/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/ListItem/26` | 1.022173 | Dismiss your precognition or doubt your grip on your current reality. |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/8` | 0.488514 | Your existence is an anomaly that defies the normal  parameters of your current reality. You might have  encountered something that disrupted your core existence,  or you crossed the veil from an alte |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/1` | 0.468910 | You're always ready to let loose with your paradoxical  abilities, and when imperiled, you instinctively release a pulse  of quantum energy. As combat begins, you Warp Reality. |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/10` | 0.419952 | from an alternate reality or a different timeline, or perhaps  you experienced an unnatural phenomenon that altered your  path, discovered a time-glitching alien device, or wrote a  treatise on quantu |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/1/ListItem/27` | 0.415817 | Hope you can solve their problems by rewriting reality. |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/9` | 0.406201 | Your existence is contrary to the status quo of the universe,  causing quantum ripples that empower your spellcasting  talent and open doorways to other worlds. Perhaps you're |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/20` | 0.405063 | Some event has unstuck you in time. You might come  from the distant past or a far-flung future. Perhaps you've  traveled from some forsaken timeline to stop a cataclysmic  event. Whatever the reason, |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/6` | 0.403936 | Your paradoxical nature has become multifaceted. During daily  preparations, you can replace one of your paradox spells with a  spell of another paradox that grants training in the prerequisite  parad |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/4` | 0.403820 | paradoxes and alternate realities. Your focal point might be  a field of study, an abstract concept, a hobby, or even your  favorite media. |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/13` | 0.403764 | You reshape terrain and manipulate events to match other realities. You cast powerful  spells and recenter yourself through your anchor when pushed to your limits. |

### Query 23
- Text: Summarize Hope you can solve their problems by rewriting reality.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/ListItem/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/ListItem/27', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/15', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/ListItem/27` | 1.000076 | Hope you can solve their problems by rewriting reality. |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/15` | 0.464753 | You might solve problems with deductive reasoning or by determining mathematic  probabilities, drawing on your deep knowledge of the multiverse. |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/2` | 0.441910 | A strange paradoxical event forever altered your existence, and now you can manipulate reality. You  explore the infinite possibilities of the multiverse, possibly visualizing variant timelines or par |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/1/ListItem/26` | 0.403328 | Dismiss your precognition or doubt your grip on your current reality. |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/10` | 0.390569 | from an alternate reality or a different timeline, or perhaps  you experienced an unnatural phenomenon that altered your  path, discovered a time-glitching alien device, or wrote a  treatise on quantu |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/15` | 0.367898 | You can draw on paradoxical forces to create a reality-warping  quantum field. It might manifest as a haze in the air that shows  shimmers of alternate realities, appear as walls of glowing  magical e |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/4` | 0.359807 | paradoxes and alternate realities. Your focal point might be  a field of study, an abstract concept, a hobby, or even your  favorite media. |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/6` | 0.357627 | Your paradoxical nature has become multifaceted. During daily  preparations, you can replace one of your paradox spells with a  spell of another paradox that grants training in the prerequisite  parad |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/8` | 0.356208 | Your existence is an anomaly that defies the normal  parameters of your current reality. You might have  encountered something that disrupted your core existence,  or you crossed the veil from an alte |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/13` | 0.354079 | Whatever paradox altered the course of your existence,  something helps keep you anchored to reality. This might be  a physical object you carry, memories of your home, or loved  ones. At 1st level, s |

### Query 24
- Text: What is the rule about CLASS FEATURES?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/28', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/393', 'PZO22001 Starfinder Player Core 162-173::/page/9/Text/70']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/28` | 0.841653 | CLASS FEATURES |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/393` | 0.758361 | Class Features |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/70` | 0.537843 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/35` | 0.507843 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/24` | 0.507843 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/33` | 0.507843 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/35` | 0.507843 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/34` | 0.507843 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/4` | 0.440561 | **Attributes** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/31` | 0.426093 | In addition to the abilities provided by your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |

### Query 25
- Text: Summarize You gain these abilities as a witchwarper. Abilities gained at higher levels list the  levels next to their names.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/29', 'PZO22001 Starfinder Player Core 162-173::/page/6/Text/2', 'PZO22001 Starfinder Player Core 162-173::/page/3/Text/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/29` | 1.040828 | You gain these abilities as a witchwarper. Abilities gained at higher levels list the  levels next to their names. |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/2` | 0.810352 | You'll see the following key terms in many witchwarper  abilities. |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/26` | 0.767616 | At 2nd level and every even-numbered level thereafter, you  gain a witchwarper class feat. These feats begin on page 169. |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/2` | 0.691631 | Use this table to look up witchwarper feats by name. |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/12` | 0.690082 | At each level that you gain a witchwarper feat, you can select |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/5` | 0.661627 | As you increase in level as a witchwarper, your number of  spells per day increases, as does the highest rank of spells  you can cast, as shown on the table on page 167. |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/Table/2` | 0.652154 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, paradox, anchor, quantum field, witchwarper spellcasting, spell repertoire2Skill feat, witchwarper feat32nd-r |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/18` | 0.625517 | You add to this spell repertoire as you increase in level.  Each time you get a spell slot (see Witchwarper Spells per  Day on page 167), you add a spell to your spell repertoire of  the same rank. At |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/433` | 0.618134 | Attribute boosts, skill feat, witchwarper feat |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/413` | 0.618134 | Attribute boosts, skill feat, witchwarper feat |

### Query 26
- Text: What is the rule about ANCESTRY AND BACKGROUND?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/30', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/34', 'PZO22001 Starfinder Player Core 162-173::/page/3/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/30` | 0.928306 | ANCESTRY AND BACKGROUND |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/34` | 0.739658 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/34` | 0.739658 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/69` | 0.709658 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/33` | 0.709658 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/23` | 0.492053 | **INTRODUCTION** **ANCESTRIES & ** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/32` | 0.492053 | **INTRODUCTION** **ANCESTRIES & ** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/39` | 0.449777 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/48` | 0.449777 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/4/SectionHeader/11` | 0.404594 | ANCESTRY FEATS 5TH |

### Query 27
- Text: What is the rule about In addition to the abilities provided by your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/31', 'PZO22001 Starfinder Player Core 162-173::/page/4/Text/13', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/31` | 0.966171 | In addition to the abilities provided by your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/13` | 0.655915 | In addition to the ancestry feat you started with, you gain an  ancestry feat at 5th level and every 4 levels thereafter. The  list of ancestry feats available to you can be found in your  ancestry's |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/8` | 0.651892 | At 1st level, your class gives you  an attribute boost to your choice  of Charisma or Intelligence. |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/7` | 0.570999 | At 1st level you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start  of this class. |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/31` | 0.556002 | in other realities. During your daily preparations, select  one ancestry feat for your ancestry that you meet the  prerequisites for and don't already have. You gain that feat  until your next daily p |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/403` | 0.527699 | 3rd-rank spells, ancestry feat, attribute boosts, reflex expertise, skill increase |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/4` | 0.524161 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/Table/2` | 0.522915 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, paradox, anchor, quantum field, witchwarper spellcasting, spell repertoire2Skill feat, witchwarper feat32nd-r |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/24` | 0.522265 | At 2nd level and every even-numbered level thereafter, you  gain a skill feat. Skill feats can be found in Chapter 5 and  have the skill trait. You must be trained or better in the  corresponding skil |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/52` | 0.509986 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |

### Query 28
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/33']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/33', 'PZO22001 Starfinder Player Core 162-173::/page/3/Text/33', 'PZO22001 Starfinder Player Core 162-173::/page/9/Text/68']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/33` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/33` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/68` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/48` | 0.569679 | **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/39` | 0.569679 | **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/84` | 0.524467 | **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/32` | 0.495539 | **INTRODUCTION** **ANCESTRIES & ** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/23` | 0.495539 | **INTRODUCTION** **ANCESTRIES & ** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/6/SectionHeader/1` | 0.473765 | **KEY TERMS** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/4` | 0.463676 | **Attributes** |

### Query 29
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/34']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/3/Text/34', 'PZO22001 Starfinder Player Core 162-173::/page/9/Text/69', 'PZO22001 Starfinder Player Core 162-173::/page/11/Text/33']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/34` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/69` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/33` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/34` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/30` | 0.726682 | ANCESTRY AND BACKGROUND |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/23` | 0.672101 | **INTRODUCTION** **ANCESTRIES & ** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/32` | 0.672101 | **INTRODUCTION** **ANCESTRIES & ** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/39` | 0.594354 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/48` | 0.594354 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/31` | 0.404713 | In addition to the abilities provided by your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |

### Query 30
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/5/Text/24', 'PZO22001 Starfinder Player Core 162-173::/page/7/Text/33', 'PZO22001 Starfinder Player Core 162-173::/page/9/Text/70']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/24` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/33` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/70` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/35` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/34` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/35` | 0.910061 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/28` | 0.573477 | CLASS FEATURES |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/66` | 0.515930 | **CLASS DC** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/393` | 0.498036 | Class Features |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/6` | 0.476046 | **Skills** |

### Query 31
- Text: Summarize **Envoy**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/36']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/7/Text/34', 'PZO22001 Starfinder Player Core 162-173::/page/9/Text/71', 'PZO22001 Starfinder Player Core 162-173::/page/3/Text/36']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/34` | 0.951326 | **Envoy** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/71` | 0.951326 | **Envoy** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/36` | 0.951326 | **Envoy** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/36` | 0.909326 | **Envoy** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/25` | 0.909326 | **Envoy** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/35` | 0.909326 | **Envoy** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/84` | 0.382028 | **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/75` | 0.364330 | **Soldier** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/38` | 0.364330 | **Soldier** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/40` | 0.364330 | **Soldier** |

### Query 32
- Text: Summarize **Mystic**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/37']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/9/Text/72', 'PZO22001 Starfinder Player Core 162-173::/page/7/Text/35', 'PZO22001 Starfinder Player Core 162-173::/page/5/Text/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/72` | 0.959378 | **Mystic** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/35` | 0.959378 | **Mystic** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/26` | 0.959378 | **Mystic** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/37` | 0.917378 | **Mystic** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/37` | 0.917378 | **Mystic** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/36` | 0.728194 | **Mystic** **Operative ** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/10` | 0.358421 | **Paradox Spells** cantrip: *stumble*; 1st: *shifting* *surge*; 2nd:  *dispel magic*; 3rd: *void* *whispers*; 4th: *eldritch* *wrath*; 5th:  *wall of stone*; 6th: *slice reality*; 7th: *death sentence |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/17` | 0.352188 | You seek magical auras and provide guidance regarding supernatural phenomena you  encounter while analyzing the environment around you. You might use *spell gems* to  bypass obstacles and protect your |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/19` | 0.347612 | **INFINITE MAGIC** **FEAT 18** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/6/SectionHeader/1` | 0.339324 | **KEY TERMS** |

### Query 33
- Text: Summarize **Operative **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/38']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/38', 'PZO22001 Starfinder Player Core 162-173::/page/5/Text/27', 'PZO22001 Starfinder Player Core 162-173::/page/7/Text/36']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/38` | 0.958402 | **Operative ** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/27` | 0.958402 | **Operative ** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/36` | 0.958402 | **Operative ** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/73` | 0.916402 | **Operative ** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/38` | 0.916402 | **Operative ** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/36` | 0.683410 | **Mystic** **Operative ** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/6/SectionHeader/1` | 0.361666 | **KEY TERMS** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/SectionHeader/17` | 0.347645 | **WARP REALITY **[one-action] |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/38` | 0.345470 | **Soldier** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/75` | 0.345470 | **Soldier** |

### Query 34
- Text: Summarize **Solarian**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/39']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/9/Text/74', 'PZO22001 Starfinder Player Core 162-173::/page/11/Text/37', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/39']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/74` | 0.974700 | **Solarian** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/37` | 0.974700 | **Solarian** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/39` | 0.974700 | **Solarian** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/37` | 0.787602 | **Solarian** **Soldier** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/28` | 0.787602 | **Solarian** **Soldier** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/39` | 0.787602 | **Solarian** **Soldier** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/40` | 0.471086 | **Soldier** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/38` | 0.471086 | **Soldier** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/75` | 0.471086 | **Soldier** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/47` | 0.359014 | **GLOSSARY & ** **INDEX** |

### Query 35
- Text: Summarize **Soldier**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/40']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/11/Text/38', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/40', 'PZO22001 Starfinder Player Core 162-173::/page/9/Text/75']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/38` | 0.953061 | **Soldier** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/40` | 0.953061 | **Soldier** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/75` | 0.953061 | **Soldier** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/28` | 0.771063 | **Solarian** **Soldier** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/37` | 0.771063 | **Solarian** **Soldier** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/39` | 0.771063 | **Solarian** **Soldier** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/6` | 0.463308 | **Skills** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/39` | 0.454361 | **Solarian** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/37` | 0.454361 | **Solarian** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/74` | 0.454361 | **Solarian** |

### Query 36
- Text: Summarize **Witchwarper**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/41']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/11/Text/39', 'PZO22001 Starfinder Player Core 162-173::/page/5/Text/29', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/39` | 0.988715 | **Witchwarper** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/29` | 0.988715 | **Witchwarper** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/41` | 0.988715 | **Witchwarper** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/38` | 0.946715 | **Witchwarper** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/76` | 0.946715 | **Witchwarper** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/40` | 0.946715 | **Witchwarper** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/26` | 0.864874 | **WITCHWARPER** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/52` | 0.864874 | **WITCHWARPER** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/56` | 0.864874 | **WITCHWARPER** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/21` | 0.864874 | **WITCHWARPER** |

### Query 37
- Text: Summarize **Archetypes**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/42']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/11/Text/40', 'PZO22001 Starfinder Player Core 162-173::/page/3/Text/41', 'PZO22001 Starfinder Player Core 162-173::/page/5/Text/30']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/40` | 0.973323 | **Archetypes** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/41` | 0.973323 | **Archetypes** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/30` | 0.973323 | **Archetypes** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/39` | 0.931323 | **Archetypes** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/77` | 0.931323 | **Archetypes** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/42` | 0.931323 | **Archetypes** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/4` | 0.431887 | **Attributes** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/19` | 0.398905 | **Tradition** arcane; **Paradox Skill **Computers |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/20` | 0.382994 | **Paradox Spells** cantrip: *analyze* *target*; 1st: *sure strike*; 2nd:  *sift* *the* *sphere*; 3rd: *hypercognition*; 4th: *translocate*; 5th:  *subjective reality*; 6th: *truesight*; 7th: *retrocog |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/8/Text/13` | 0.382777 | **1st ***akashic download*, *mind skewer*, *fleet step*;  **Cantrips ***analyze target, injury echo,* *measure*,* seek * *the stars*, *telekinetic projectile* |

### Query 38
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/43']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/57', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/43', 'PZO22001 Starfinder Player Core 162-173::/page/9/Text/78']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/57` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/43` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/78` | 0.693094 | **SKILLS** **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/31` | 0.651094 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/40` | 0.651094 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/42` | 0.651094 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/6` | 0.640740 | **Skills** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/29` | 0.461596 | **Anchor Benefit** During your daily preparations, choose a skill  you're trained in. You gain Assurance in that skill. If you're  expert in that skill, and the skill has the Recall Knowledge  action, |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/24` | 0.461059 | At 2nd level and every even-numbered level thereafter, you  gain a skill feat. Skill feats can be found in Chapter 5 and  have the skill trait. You must be trained or better in the  corresponding skil |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/58` | 0.441812 | Trained in one skill determined by  your paradox |

### Query 39
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/44', 'PZO22001 Starfinder Player Core 162-173::/page/11/Text/41', 'PZO22001 Starfinder Player Core 162-173::/page/3/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/44` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/41` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/42` | 0.695037 | **SKILLS** **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/40` | 0.653037 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/78` | 0.653037 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/31` | 0.653037 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/526` | 0.619086 | Feat |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/566` | 0.619086 | Feat |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/14` | 0.506428 | one of the following feats. You must satisfy any prerequisites  before taking the feat. |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/10` | 0.496910 | **Feats** |

### Query 40
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/45']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/45', 'PZO22001 Starfinder Player Core 162-173::/page/9/Text/79', 'PZO22001 Starfinder Player Core 162-173::/page/7/Text/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/45` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/79` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/41` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/32` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/43` | 0.902726 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/42` | 0.902726 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/84` | 0.421643 | **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/39` | 0.409329 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/48` | 0.409329 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/6` | 0.408837 | **Skills** |

### Query 41
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/46']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/46', 'PZO22001 Starfinder Player Core 162-173::/page/5/Text/33', 'PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/64']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/46` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/33` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/64` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/42` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/44` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/80` | 0.847304 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/43` | 0.847304 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/3/SectionHeader/16` | 0.536072 | SPELL REPERTOIRE |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/4/SectionHeader/4` | 0.533616 | SIGNATURE SPELLS 3RD |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/34` | 0.531732 | **CONCEAL SPELL **[one-action] **FEAT 2** |

### Query 42
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/47']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/5/Text/34', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/47', 'PZO22001 Starfinder Player Core 162-173::/page/7/Text/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/34` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/47` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/43` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/45` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/81` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/44` | 0.923000 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/33` | 0.418586 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/68` | 0.418586 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/33` | 0.418586 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/17` | 0.390655 | The multiverse is a complex game—you use alternate realities to |

### Query 43
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/48']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/11/Text/45', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/48', 'PZO22001 Starfinder Player Core 162-173::/page/3/Text/46']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/45` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/48` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/46` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/35` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/44` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/82` | 0.645203 | **CONDITIONS ** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/83` | 0.573689 | **APPENDIX** **GLOSSARY & ** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/4` | 0.463693 | **Attributes** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/6/SectionHeader/1` | 0.439047 | **KEY TERMS** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/84` | 0.423722 | **INDEX** |

### Query 44
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/49']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/11/Text/46', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/49', 'PZO22001 Starfinder Player Core 162-173::/page/5/Text/36']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/46` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/49` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/36` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/47` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/45` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/83` | 0.697531 | **APPENDIX** **GLOSSARY & ** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/84` | 0.618357 | **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/70` | 0.385404 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/35` | 0.385404 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/34` | 0.385404 | **CLASSES** |

### Query 45
- Text: What is the rule about **CHARACTER ** **SHEET**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/50']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/50', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/42', 'PZO22001 Starfinder Player Core 162-173::/page/9/Text/77']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/50` | 0.859300 | **CHARACTER ** **SHEET** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/42` | 0.434353 | **Archetypes** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/77` | 0.434353 | **Archetypes** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/41` | 0.392353 | **Archetypes** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/39` | 0.392353 | **Archetypes** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/30` | 0.392353 | **Archetypes** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/40` | 0.392353 | **Archetypes** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/82` | 0.378942 | **CONDITIONS ** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/6` | 0.371280 | **Skills** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/78` | 0.369339 | **SKILLS** **FEATS** |

### Query 46
- Text: Summarize **INITIAL PROFICIENCIES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/51']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/51', 'PZO22001 Starfinder Player Core 162-173::/page/2/SectionHeader/6', 'PZO22001 Starfinder Player Core 162-173::/page/2/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/51` | 1.001056 | **INITIAL PROFICIENCIES** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/SectionHeader/6` | 0.851001 | INITIAL PROFICIENCIES |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/7` | 0.511438 | At 1st level you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start  of this class. |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/33` | 0.400378 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/68` | 0.400378 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/33` | 0.400378 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/6` | 0.396642 | **Skills** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/6` | 0.379965 | **PREDICTIVE POSITIONING **[reaction] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/52` | 0.376597 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/48` | 0.353772 | **BACKGROUNDS** |

### Query 47
- Text: What is the rule about At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/52']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/52', 'PZO22001 Starfinder Player Core 162-173::/page/4/Text/9', 'PZO22001 Starfinder Player Core 162-173::/page/2/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/52` | 0.992024 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/9` | 0.747954 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use this increase either to increase your  proficiency rank to trained in one skill you're untrained in or  to increase |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/7` | 0.702241 | At 1st level you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start  of this class. |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/10` | 0.611362 | At 7th level, you can use skill increases to increase your  proficiency rank to master in a skill in which you're already  an expert, and at 15th level, you can use them to increase  your proficiency |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/24` | 0.529877 | At 2nd level and every even-numbered level thereafter, you  gain a skill feat. Skill feats can be found in Chapter 5 and  have the skill trait. You must be trained or better in the  corresponding skil |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/22` | 0.528930 | You remain alert to threats. Your proficiency  rank for Perception increases to expert. |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/24` | 0.527181 | You've gained a broader understanding of  conventional weaponry to augment your  unconventional spellcasting. Your proficiency rank |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/28` | 0.493558 | combine to help you avoid attacks. Your proficiency ranks in  light armor and unarmored defense increase to expert. |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/31` | 0.479746 | In addition to the abilities provided by your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/17` | 0.477742 | Extended practice of magic has improved your capabilities.  Your proficiency ranks for class DC, spell attack  modifier, and spell DC increase to expert. |

### Query 48
- Text: Summarize **PERCEPTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/53']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/53', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/54', 'PZO22001 Starfinder Player Core 162-173::/page/4/SectionHeader/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/53` | 0.934058 | **PERCEPTION** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/54` | 0.583165 | Trained in Perception |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/4/SectionHeader/21` | 0.533791 | PERCEPTION EXPERTISE 11TH |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/33` | 0.443002 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/33` | 0.443002 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/68` | 0.443002 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/39` | 0.438809 | **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/48` | 0.438809 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/22` | 0.437558 | You remain alert to threats. Your proficiency  rank for Perception increases to expert. |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/38` | 0.437106 | **FUNDAMENTAL UNDERSTANDING **[reaction] **FEAT 2** |

### Query 49
- Text: Summarize Trained in Perception
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/54']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/54', 'PZO22001 Starfinder Player Core 162-173::/page/4/Text/22', 'PZO22001 Starfinder Player Core 162-173::/page/4/SectionHeader/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/54` | 0.944339 | Trained in Perception |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/22` | 0.583480 | You remain alert to threats. Your proficiency  rank for Perception increases to expert. |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/4/SectionHeader/21` | 0.516135 | PERCEPTION EXPERTISE 11TH |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/53` | 0.476849 | **PERCEPTION** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/56` | 0.454774 | Trained in Fortitude Trained in Reflex Expert in Will |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/61` | 0.435404 | Trained in simple weapons Trained in unarmed attacks |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/63` | 0.434440 | Trained in light armor Trained in unarmored defense |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/415` | 0.397413 | 6th-rank spells, general feat, perception expertise, skill increase, weapon expertise |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/58` | 0.396746 | Trained in one skill determined by  your paradox |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/7` | 0.362883 | At 1st level you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start  of this class. |

### Query 50
- Text: What is the rule about **SAVING THROWS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/55']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/55', 'PZO22001 Starfinder Player Core 162-173::/page/9/Text/1', 'PZO22001 Starfinder Player Core 162-173::/page/9/Text/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/55` | 0.904955 | **SAVING THROWS** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/1` | 0.511143 | saving throw or your AC against it (or a +2 circumstance bonus  if you rolled a critical success). |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/18` | 0.482258 | You scrub all traces of the triggering effect from the target's  mind. The target rerolls their saving throw against the triggering  effect and must use the second result, even if it's worse. |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/30` | 0.361248 | You allow your mind to wander to things you find pleasant,  briefly shutting out all realities and protecting you from harm.  You gain a +2 status bonus to saving throws against mental  effects until |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/5` | 0.337260 | You prevent creatures from leaving your quantum field and  returning to reality. Until the start of your next turn, any  creature who begins its turn inside your quantum field must  succeed at a Will |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/18` | 0.324909 | move creatures on the board. When you use the Sustain action  to move your quantum field, you can teleport any number of  creatures within the quantum field's original area to squares  of your choice |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/532` | 0.310262 | Borrow Spell |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/3` | 0.297028 | **Anchoring:** You can use abilities with the anchoring  trait only while your quantum field is activated. If you  use the ability on your turn, in addition to their stated  effects, they automaticall |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/17` | 0.292938 | **Trigger** You or an ally fail a save against a mental effect while  within your quantum field. |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/24` | 0.284649 | **Trigger** You roll initiative. |

### Query 51
- Text: Summarize Trained in Fortitude Trained in Reflex Expert in Will
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/56']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/56', 'PZO22001 Starfinder Player Core 162-173::/page/4/Text/15', 'PZO22001 Starfinder Player Core 162-173::/page/5/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/56` | 1.022599 | Trained in Fortitude Trained in Reflex Expert in Will |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/15` | 0.551395 | Your awareness of possible dangers, through incredible  analysis or an understanding of the wider multiverse,  increases your reflexes. Your proficiency rank for Reflex  saves increases to expert. |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/7` | 0.539338 | The intense experiences you've accumulated through your  studies or travels have strengthened your mental fortitude.  Your proficiency rank for Will saves increases to master.  When you roll a success |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/20` | 0.491511 | Magical power has improved your body's  resiliency. Your proficiency rank for Fortitude  saves increases to expert. |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/54` | 0.458539 | Trained in Perception |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/22` | 0.450863 | You remain alert to threats. Your proficiency  rank for Perception increases to expert. |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/4/SectionHeader/14` | 0.448810 | REFLEX EXPERTISE 5TH |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/63` | 0.437578 | Trained in light armor Trained in unarmored defense |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/403` | 0.436219 | 3rd-rank spells, ancestry feat, attribute boosts, reflex expertise, skill increase |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/59` | 0.420064 | Trained in a number of additional  skills equal to 3 plus your Intelligence  modifier |

### Query 52
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/57']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/57', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/43', 'PZO22001 Starfinder Player Core 162-173::/page/9/Text/78']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/57` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/43` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/78` | 0.693094 | **SKILLS** **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/31` | 0.651094 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/40` | 0.651094 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/42` | 0.651094 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/6` | 0.640740 | **Skills** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/29` | 0.461596 | **Anchor Benefit** During your daily preparations, choose a skill  you're trained in. You gain Assurance in that skill. If you're  expert in that skill, and the skill has the Recall Knowledge  action, |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/24` | 0.461059 | At 2nd level and every even-numbered level thereafter, you  gain a skill feat. Skill feats can be found in Chapter 5 and  have the skill trait. You must be trained or better in the  corresponding skil |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/58` | 0.441812 | Trained in one skill determined by  your paradox |

### Query 53
- Text: What is the rule about Trained in one skill determined by  your paradox?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/58']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/58', 'PZO22001 Starfinder Player Core 162-173::/page/11/Text/5', 'PZO22001 Starfinder Player Core 162-173::/page/2/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/58` | 0.919500 | Trained in one skill determined by  your paradox |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/5` | 0.701841 | **Prerequisites** master in a paradox skill for a paradox other  than your chosen paradox |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/11` | 0.664419 | At 1st level, choose your paradox. Your chosen paradox  determines the tradition of your spells, additional trained  skills, additional spells you learn, and the effects of your  quantum field. You al |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/6` | 0.620082 | Your paradoxical nature has become multifaceted. During daily  preparations, you can replace one of your paradox spells with a  spell of another paradox that grants training in the prerequisite  parad |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/16` | 0.582696 | Your paradox represents an event or force that forever altered  you. Your chosen paradox determines your spellcasting  tradition and grants you trained proficiency in the listed  paradox skill. You au |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/15` | 0.568326 | You learn warp spells based on your paradox. |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/62` | 0.529994 | Your paradox begins to cement itself across your life. You  gain the advanced warp spell for your paradox. |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/10` | 0.507788 | You breach the veil of paradoxical understanding. You gain  the greater warp spell for your paradox. |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/9` | 0.505672 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use this increase either to increase your  proficiency rank to trained in one skill you're untrained in or  to increase |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/59` | 0.500309 | Trained in a number of additional  skills equal to 3 plus your Intelligence  modifier |

### Query 54
- Text: What is the rule about Trained in a number of additional  skills equal to 3 plus your Intelligence  modifier?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/59']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/59', 'PZO22001 Starfinder Player Core 162-173::/page/4/Text/9', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/58']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/59` | 0.919891 | Trained in a number of additional  skills equal to 3 plus your Intelligence  modifier |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/9` | 0.623130 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use this increase either to increase your  proficiency rank to trained in one skill you're untrained in or  to increase |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/58` | 0.547399 | Trained in one skill determined by  your paradox |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/10` | 0.499547 | At 7th level, you can use skill increases to increase your  proficiency rank to master in a skill in which you're already  an expert, and at 15th level, you can use them to increase  your proficiency |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/24` | 0.498273 | At 2nd level and every even-numbered level thereafter, you  gain a skill feat. Skill feats can be found in Chapter 5 and  have the skill trait. You must be trained or better in the  corresponding skil |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/4/SectionHeader/7` | 0.491607 | SKILL INCREASES 3RD |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/30` | 0.479283 | You've learned how to inflict greater injuries with the weapons  you know best. You deal 2 additional damage with weapons  and unarmed attacks in which you're an expert. This damage  increases to 3 if |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/5` | 0.463736 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/8` | 0.461034 | At 1st level, your class gives you  an attribute boost to your choice  of Charisma or Intelligence. |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/6` | 0.449481 | Some of your spells require you to attempt a spell attack to  see how effective they are or have your enemies roll against  your spell DC (typically by attempting a saving throw). Your spell  attack m |

### Query 55
- Text: What is the rule about **ATTACKS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/60']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/60', 'PZO22001 Starfinder Player Core 162-173::/page/9/Text/23', 'PZO22001 Starfinder Player Core 162-173::/page/9/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/60` | 0.855189 | **ATTACKS** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/23` | 0.423197 | **Trigger** An enemy damages you. |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/10` | 0.423197 | **Trigger** An enemy damages you. |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/21` | 0.379163 | **Critical Success** The Strike gains the anchoring trait. You can  reroll the damage dice rolled for this strike, but you must  use the second result, even if it's worse. |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/16` | 0.354860 | **ANCHORING STRIKE **[one-action] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/61` | 0.353949 | Trained in simple weapons Trained in unarmed attacks |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/20` | 0.352512 | Battle can be disorienting, but for you, the intense mental  effort of striking your targets lends you additional clarity and  focus. Make a Strike. The Strike gains the following success  and critica |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/6` | 0.345033 | **KEY ATTRIBUTE** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/6` | 0.343876 | Some of your spells require you to attempt a spell attack to  see how effective they are or have your enemies roll against  your spell DC (typically by attempting a saving throw). Your spell  attack m |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/62` | 0.342350 | **DEFENSES** |

### Query 56
- Text: What is the rule about Trained in simple weapons Trained in unarmed attacks?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/61']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/61', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/63', 'PZO22001 Starfinder Player Core 162-173::/page/4/Text/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/61` | 0.914369 | Trained in simple weapons Trained in unarmed attacks |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/63` | 0.691830 | Trained in light armor Trained in unarmored defense |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/25` | 0.580869 | for simple weapons and unarmed attacks increases to  expert. |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/28` | 0.455630 | combine to help you avoid attacks. Your proficiency ranks in  light armor and unarmored defense increase to expert. |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/65` | 0.440222 | Trained in spell attack modifier Trained in spell DC |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/30` | 0.428574 | You've learned how to inflict greater injuries with the weapons  you know best. You deal 2 additional damage with weapons  and unarmed attacks in which you're an expert. This damage  increases to 3 if |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/52` | 0.407431 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/58` | 0.403028 | Trained in one skill determined by  your paradox |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/24` | 0.392659 | You've gained a broader understanding of  conventional weaponry to augment your  unconventional spellcasting. Your proficiency rank |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/9` | 0.382090 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use this increase either to increase your  proficiency rank to trained in one skill you're untrained in or  to increase |

### Query 57
- Text: Summarize **DEFENSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/62']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/62', 'PZO22001 Starfinder Player Core 162-173::/page/4/SectionHeader/26', 'PZO22001 Starfinder Player Core 162-173::/page/8/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/62` | 0.959826 | **DEFENSES** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/4/SectionHeader/26` | 0.560957 | QUANTUM DEFENSES 13TH |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/8/Text/5` | 0.492029 | Prioritize Intelligence, then Dexterity and Wisdom to  improve your defenses. |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/10` | 0.444403 | **Feats** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/6` | 0.418384 | **Skills** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/63` | 0.415012 | **DANGER ZONE **[one-action] **FEAT 8** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/33` | 0.411981 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/68` | 0.411981 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/33` | 0.411981 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/63` | 0.408873 | Trained in light armor Trained in unarmored defense |

### Query 58
- Text: Summarize Trained in light armor Trained in unarmored defense
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/63']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/63', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/61', 'PZO22001 Starfinder Player Core 162-173::/page/4/Text/28']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/63` | 1.027002 | Trained in light armor Trained in unarmored defense |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/61` | 0.779166 | Trained in simple weapons Trained in unarmed attacks |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/28` | 0.662768 | combine to help you avoid attacks. Your proficiency ranks in  light armor and unarmored defense increase to expert. |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/65` | 0.431980 | Trained in spell attack modifier Trained in spell DC |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/25` | 0.416484 | for simple weapons and unarmed attacks increases to  expert. |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/27` | 0.406514 | The flow of your spellcasting and your defensive training |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/52` | 0.403115 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/30` | 0.401338 | You've learned how to inflict greater injuries with the weapons  you know best. You deal 2 additional damage with weapons  and unarmed attacks in which you're an expert. This damage  increases to 3 if |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/56` | 0.399383 | Trained in Fortitude Trained in Reflex Expert in Will |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/67` | 0.399314 | Trained in witchwarper class DC |

### Query 59
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/64']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/46', 'PZO22001 Starfinder Player Core 162-173::/page/5/Text/33', 'PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/64']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/46` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/33` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/64` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/42` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/44` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/80` | 0.847304 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/43` | 0.847304 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/3/SectionHeader/16` | 0.536072 | SPELL REPERTOIRE |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/4/SectionHeader/4` | 0.533616 | SIGNATURE SPELLS 3RD |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/34` | 0.531732 | **CONCEAL SPELL **[one-action] **FEAT 2** |

### Query 60
- Text: What is the rule about Trained in spell attack modifier Trained in spell DC?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/65']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/65', 'PZO22001 Starfinder Player Core 162-173::/page/3/Text/6', 'PZO22001 Starfinder Player Core 162-173::/page/5/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/65` | 0.929793 | Trained in spell attack modifier Trained in spell DC |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/6` | 0.688068 | Some of your spells require you to attempt a spell attack to  see how effective they are or have your enemies roll against  your spell DC (typically by attempting a saving throw). Your spell  attack m |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/9` | 0.634159 | You push way past the boundaries of magical theory to  embody the pinnacle of spellcasting. Your proficiency  ranks for spell attack modifier and spell DC increase to  legendary. |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/5` | 0.574303 | Your spells are among the most potent across all possible  worlds. Your proficiency ranks for class DC, spell attack  modifier, and spell DC increase to master. |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/17` | 0.571636 | Extended practice of magic has improved your capabilities.  Your proficiency ranks for class DC, spell attack  modifier, and spell DC increase to expert. |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/67` | 0.535424 | Trained in witchwarper class DC |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/59` | 0.476915 | Trained in a number of additional  skills equal to 3 plus your Intelligence  modifier |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/27` | 0.470400 | The flow of your spellcasting and your defensive training |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/61` | 0.465253 | Trained in simple weapons Trained in unarmed attacks |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/5` | 0.449639 | You can alter offensive spells to be less deadly. If your next  action is to Cast a Spell that deals damage and doesn't have the  death or void trait, that spell gains the nonlethal trait (page 256). |

### Query 61
- Text: What is the rule about **CLASS DC**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/66']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/66', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/35', 'PZO22001 Starfinder Player Core 162-173::/page/3/Text/35']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/66` | 0.881905 | **CLASS DC** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/35` | 0.521525 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/35` | 0.521525 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/34` | 0.491525 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/70` | 0.491525 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/24` | 0.491525 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/33` | 0.491525 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/28` | 0.381301 | CLASS FEATURES |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/6` | 0.362036 | Some of your spells require you to attempt a spell attack to  see how effective they are or have your enemies roll against  your spell DC (typically by attempting a saving throw). Your spell  attack m |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/65` | 0.357379 | Trained in spell attack modifier Trained in spell DC |

### Query 62
- Text: What is the rule about Trained in witchwarper class DC?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/67']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/67', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/65', 'PZO22001 Starfinder Player Core 162-173::/page/3/Text/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/67` | 0.884018 | Trained in witchwarper class DC |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/65` | 0.601481 | Trained in spell attack modifier Trained in spell DC |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/26` | 0.592949 | At 2nd level and every even-numbered level thereafter, you  gain a witchwarper class feat. These feats begin on page 169. |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/417` | 0.499295 | Skill feat, witchwarper feat |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/421` | 0.499295 | Skill feat, witchwarper feat |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/409` | 0.499295 | Skill feat, witchwarper feat |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/401` | 0.499295 | Skill feat, witchwarper feat |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/425` | 0.499295 | Skill feat, witchwarper feat |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/397` | 0.499295 | Skill feat, witchwarper feat |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/405` | 0.499295 | Skill feat, witchwarper feat |

### Query 63
- Text: Summarize **WITCHWARPER ADVANCEMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 162-173::/page/10/Text/56', 'PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/SectionHeader/1` | 1.020134 | **WITCHWARPER ADVANCEMENT** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/56` | 0.869759 | **WITCHWARPER** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/21` | 0.869759 | **WITCHWARPER** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/26` | 0.827759 | **WITCHWARPER** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/52` | 0.827759 | **WITCHWARPER** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/29` | 0.827759 | **WITCHWARPER** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/40` | 0.827759 | **WITCHWARPER** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/51` | 0.827759 | **WITCHWARPER** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/33` | 0.827759 | **WITCHWARPER** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/56` | 0.827759 | **WITCHWARPER** |

### Query 64
- Text: Lookup values for Your LevelClass Features1Ancestry and background, attribute boosts,
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/Table/2']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/1/Text/31', 'PZO22001 Starfinder Player Core 162-173::/page/2/Text/4', 'PZO22001 Starfinder Player Core 162-173::/page/2/Table/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/31` | 0.670773 | In addition to the abilities provided by your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/4` | 0.624096 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/Table/2` | 0.623774 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, paradox, anchor, quantum field, witchwarper spellcasting, spell repertoire2Skill feat, witchwarper feat32nd-r |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/5` | 0.545659 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/8` | 0.544884 | At 1st level, your class gives you  an attribute boost to your choice  of Charisma or Intelligence. |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/393` | 0.528105 | Class Features |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/13` | 0.517895 | In addition to the ancestry feat you started with, you gain an  ancestry feat at 5th level and every 4 levels thereafter. The  list of ancestry feats available to you can be found in your  ancestry's |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/395` | 0.492770 | Ancestry and background, attribute boosts, initial proficiencies, paradox, anchor, quantum field, witchwarper spellcasting, spell repertoire |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/403` | 0.489965 | 3rd-rank spells, ancestry feat, attribute boosts, reflex expertise, skill increase |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/4` | 0.480214 | **Attributes** |

### Query 65
- Text: Summarize Your Level
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/392']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/856', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/392', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/527']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/856` | 0.853813 | Your Level |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/392` | 0.853813 | Your Level |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/527` | 0.729099 | Level |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/567` | 0.687099 | Level |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/29` | 0.549996 | 2ND LEVEL |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/25` | 0.534036 | 4TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/13` | 0.523376 | 18TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/58` | 0.514596 | 8TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/43` | 0.513306 | 14TH LEVEL |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/1` | 0.501266 | 16TH LEVEL |

### Query 66
- Text: What is the rule about Class Features?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/393']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/393', 'PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/28', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/393` | 0.835742 | Class Features |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/28` | 0.700239 | CLASS FEATURES |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/31` | 0.477963 | In addition to the abilities provided by your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/4` | 0.414280 | **Attributes** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/34` | 0.407880 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/70` | 0.407880 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/35` | 0.407880 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/35` | 0.407880 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/24` | 0.407879 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/33` | 0.407879 | **CLASSES** |

### Query 67
- Text: Summarize 1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/394']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/868', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/595', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/603']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/868` | 0.669108 | 1 |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/595` | 0.669108 | 1 |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/603` | 0.669108 | 1 |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/394` | 0.627108 | 1 |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/563` | 0.627108 | 1 |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/543` | 0.627108 | 1 |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/587` | 0.627108 | 1 |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/531` | 0.627108 | 1 |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/571` | 0.513765 | 2 |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/549` | 0.513765 | 2 |

### Query 68
- Text: What is the rule about Ancestry and background, attribute boosts,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/395']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/395', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/31', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/403']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/395` | 0.628211 | Ancestry and background, attribute boosts, initial proficiencies, paradox, anchor, quantum field, witchwarper spellcasting, spell repertoire |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/31` | 0.591532 | In addition to the abilities provided by your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/403` | 0.582925 | 3rd-rank spells, ancestry feat, attribute boosts, reflex expertise, skill increase |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/5` | 0.509477 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/30` | 0.506753 | ANCESTRY AND BACKGROUND |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/13` | 0.501055 | In addition to the ancestry feat you started with, you gain an  ancestry feat at 5th level and every 4 levels thereafter. The  list of ancestry feats available to you can be found in your  ancestry's |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/33` | 0.496934 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/69` | 0.496934 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/34` | 0.496934 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/34` | 0.496934 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 69
- Text: Summarize 2
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/396']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/396', 'PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/880', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/535']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/396` | 0.689465 | 2 |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/880` | 0.689465 | 2 |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/535` | 0.689465 | 2 |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/571` | 0.647465 | 2 |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/589` | 0.647465 | 2 |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/539` | 0.647465 | 2 |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/601` | 0.647465 | 2 |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/549` | 0.647465 | 2 |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/561` | 0.647465 | 2 |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/859` | 0.507646 | 2nd |

### Query 70
- Text: What is the rule about Skill feat, witchwarper feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/397']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/425', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/429', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/417']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/425` | 0.919131 | Skill feat, witchwarper feat |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/429` | 0.919131 | Skill feat, witchwarper feat |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/417` | 0.919131 | Skill feat, witchwarper feat |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/409` | 0.877131 | Skill feat, witchwarper feat |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/405` | 0.877131 | Skill feat, witchwarper feat |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/421` | 0.877131 | Skill feat, witchwarper feat |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/397` | 0.877131 | Skill feat, witchwarper feat |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/401` | 0.877131 | Skill feat, witchwarper feat |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/413` | 0.764002 | Attribute boosts, skill feat, witchwarper feat |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/433` | 0.764002 | Attribute boosts, skill feat, witchwarper feat |

### Query 71
- Text: Summarize 3
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/398']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/398', 'PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/995', 'PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/892']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/398` | 0.731895 | 3 |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/995` | 0.731895 | 3 |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/892` | 0.731895 | 3 |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/895` | 0.689895 | 3 |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/920` | 0.689895 | 3 |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/1045` | 0.689895 | 3 |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/970` | 0.689895 | 3 |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/1070` | 0.689895 | 3 |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/1020` | 0.689895 | 3 |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/945` | 0.689895 | 3 |

### Query 72
- Text: What is the rule about 2nd-rank spells, general feat, isolated spell?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/399']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/399', 'PZO22001 Starfinder Player Core 162-173::/page/11/Text/22', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/407']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/399` | 0.808316 | 2nd-rank spells, general feat, isolated spell matrix, signature spells, skill increase |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/22` | 0.594437 | You borrow spells from other realities. Twice per day, you can  cast a 9th-rank or lower spell after you've run out of spell slots  of the appropriate spell rank; the two spells you cast with this  fe |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/407` | 0.588177 | 4th-rank spells, expert spellcaster, general feat, skill increase |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/411` | 0.540193 | 5th-rank spells, ancestry feat, magical fortitude, skill increase |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/415` | 0.539164 | 6th-rank spells, general feat, perception expertise, skill increase, weapon expertise |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/3` | 0.512333 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/19` | 0.506531 | Though you gain them at the same rate, your spell slots  and the spells in your spell repertoire are separate. If a feat or  other ability adds a spell to your spell repertoire, it wouldn't  give you |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/403` | 0.501786 | 3rd-rank spells, ancestry feat, attribute boosts, reflex expertise, skill increase |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/423` | 0.497456 | 8th-rank spells, attribute boosts, general feat, master spellcaster, skill increase |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/8` | 0.493063 | When you get spell slots of 2nd rank and higher, you can fill  those slots with stronger versions of lower-rank spells. This  increases the spell's rank, heightening it to match the spell  slot. You m |

### Query 73
- Text: Summarize 4
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/400']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/400', 'PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/919', 'PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/918']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/400` | 0.774878 | 4 |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/919` | 0.774878 | 4 |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/918` | 0.774878 | 4 |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/969` | 0.732878 | 4 |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/968` | 0.732878 | 4 |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/967` | 0.732878 | 4 |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/944` | 0.732878 | 4 |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/932` | 0.732878 | 4 |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/942` | 0.732878 | 4 |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/907` | 0.732878 | 4 |

### Query 74
- Text: What is the rule about Skill feat, witchwarper feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/401']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/425', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/429', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/417']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/425` | 0.919131 | Skill feat, witchwarper feat |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/429` | 0.919131 | Skill feat, witchwarper feat |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/417` | 0.919131 | Skill feat, witchwarper feat |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/409` | 0.877131 | Skill feat, witchwarper feat |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/405` | 0.877131 | Skill feat, witchwarper feat |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/421` | 0.877131 | Skill feat, witchwarper feat |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/397` | 0.877131 | Skill feat, witchwarper feat |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/401` | 0.877131 | Skill feat, witchwarper feat |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/413` | 0.764002 | Attribute boosts, skill feat, witchwarper feat |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/433` | 0.764002 | Attribute boosts, skill feat, witchwarper feat |

### Query 75
- Text: Summarize 5
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/402']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/402', 'PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/869', 'PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/881']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/402` | 0.772788 | 5 |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/869` | 0.772788 | 5 |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/881` | 0.772788 | 5 |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/917` | 0.730788 | 5 |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/916` | 0.730788 | 5 |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/905` | 0.730788 | 5 |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/893` | 0.730788 | 5 |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/941` | 0.730788 | 5 |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/953` | 0.730788 | 5 |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/965` | 0.730788 | 5 |

### Query 76
- Text: What is the rule about 3rd-rank spells, ancestry feat, attribute?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/403']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/403', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/411', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/427']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/403` | 0.805734 | 3rd-rank spells, ancestry feat, attribute boosts, reflex expertise, skill increase |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/411` | 0.732170 | 5th-rank spells, ancestry feat, magical fortitude, skill increase |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/427` | 0.684351 | 9th-rank spells, ancestry feat, quantum will, skill increase |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/13` | 0.611031 | In addition to the ancestry feat you started with, you gain an  ancestry feat at 5th level and every 4 levels thereafter. The  list of ancestry feats available to you can be found in your  ancestry's |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/419` | 0.607915 | 7th-rank spells, ancestry feat, quantum defenses, skill increase, weapon specialization |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/399` | 0.552897 | 2nd-rank spells, general feat, isolated spell matrix, signature spells, skill increase |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/423` | 0.548249 | 8th-rank spells, attribute boosts, general feat, master spellcaster, skill increase |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/407` | 0.542907 | 4th-rank spells, expert spellcaster, general feat, skill increase |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/31` | 0.542403 | in other realities. During your daily preparations, select  one ancestry feat for your ancestry that you meet the  prerequisites for and don't already have. You gain that feat  until your next daily p |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/415` | 0.541016 | 6th-rank spells, general feat, perception expertise, skill increase, weapon expertise |

### Query 77
- Text: Summarize 6
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/404']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/545', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/569', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/573']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/545` | 0.783525 | 6 |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/569` | 0.783525 | 6 |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/573` | 0.783525 | 6 |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/404` | 0.741525 | 6 |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/928` | 0.741525 | 6 |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/863` | 0.627172 | 6th |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/44` | 0.508078 | 6TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/940` | 0.496931 | 7 |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/406` | 0.496931 | 7 |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/49` | 0.485213 | **PREDICT OUTCOME** **FEAT 6** |

### Query 78
- Text: What is the rule about Skill feat, witchwarper feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/405']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/425', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/429', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/417']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/425` | 0.919131 | Skill feat, witchwarper feat |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/429` | 0.919131 | Skill feat, witchwarper feat |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/417` | 0.919131 | Skill feat, witchwarper feat |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/409` | 0.877131 | Skill feat, witchwarper feat |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/405` | 0.877131 | Skill feat, witchwarper feat |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/421` | 0.877131 | Skill feat, witchwarper feat |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/397` | 0.877131 | Skill feat, witchwarper feat |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/401` | 0.877131 | Skill feat, witchwarper feat |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/413` | 0.764002 | Attribute boosts, skill feat, witchwarper feat |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/433` | 0.764002 | Attribute boosts, skill feat, witchwarper feat |

### Query 79
- Text: Summarize 7
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/406']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/940', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/406', 'PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/864']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/940` | 0.766039 | 7 |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/406` | 0.766039 | 7 |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/864` | 0.703809 | 7th |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/569` | 0.473241 | 6 |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/545` | 0.473241 | 6 |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/573` | 0.473241 | 6 |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/404` | 0.473241 | 6 |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/928` | 0.473241 | 6 |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/541` | 0.456129 | 8 |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/575` | 0.456129 | 8 |

### Query 80
- Text: What is the rule about 4th-rank spells, expert spellcaster, general?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/407']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/407', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/423', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/415']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/407` | 0.836421 | 4th-rank spells, expert spellcaster, general feat, skill increase |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/423` | 0.619852 | 8th-rank spells, attribute boosts, general feat, master spellcaster, skill increase |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/415` | 0.606642 | 6th-rank spells, general feat, perception expertise, skill increase, weapon expertise |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/4` | 0.508868 | Each day, you can cast up to three 1st-rank spells. You  must know spells to cast them, and you learn them via the  spell repertoire class feature. The number of spells you can  cast each day is calle |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/403` | 0.503097 | 3rd-rank spells, ancestry feat, attribute boosts, reflex expertise, skill increase |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/399` | 0.501379 | 2nd-rank spells, general feat, isolated spell matrix, signature spells, skill increase |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/24` | 0.500413 | You've gained a broader understanding of  conventional weaponry to augment your  unconventional spellcasting. Your proficiency rank |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/411` | 0.499142 | 5th-rank spells, ancestry feat, magical fortitude, skill increase |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/8` | 0.486713 | When you get spell slots of 2nd rank and higher, you can fill  those slots with stronger versions of lower-rank spells. This  increases the spell's rank, heightening it to match the spell  slot. You m |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/17` | 0.483295 | Extended practice of magic has improved your capabilities.  Your proficiency ranks for class DC, spell attack  modifier, and spell DC increase to expert. |

### Query 81
- Text: Summarize 8
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/408']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/408', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/529', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/575']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/408` | 0.787704 | 8 |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/575` | 0.787704 | 8 |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/529` | 0.787704 | 8 |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/541` | 0.745704 | 8 |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/952` | 0.745704 | 8 |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/865` | 0.670223 | 8th |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/58` | 0.546940 | 8TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/406` | 0.471909 | 7 |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/940` | 0.471909 | 7 |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/410` | 0.452855 | 9 |

### Query 82
- Text: What is the rule about Skill feat, witchwarper feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/409']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/425', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/429', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/417']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/425` | 0.919131 | Skill feat, witchwarper feat |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/429` | 0.919131 | Skill feat, witchwarper feat |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/417` | 0.919131 | Skill feat, witchwarper feat |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/409` | 0.877131 | Skill feat, witchwarper feat |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/405` | 0.877131 | Skill feat, witchwarper feat |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/421` | 0.877131 | Skill feat, witchwarper feat |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/397` | 0.877131 | Skill feat, witchwarper feat |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/401` | 0.877131 | Skill feat, witchwarper feat |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/413` | 0.764002 | Attribute boosts, skill feat, witchwarper feat |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/433` | 0.764002 | Attribute boosts, skill feat, witchwarper feat |

### Query 83
- Text: Summarize 9
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/410']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/964', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/410', 'PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/866']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/964` | 0.770045 | 9 |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/410` | 0.770045 | 9 |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/866` | 0.699978 | 9th |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/19` | 0.630795 | 9TH |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/408` | 0.455491 | 8 |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/529` | 0.455491 | 8 |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/575` | 0.455491 | 8 |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/952` | 0.455491 | 8 |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/541` | 0.455491 | 8 |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/551` | 0.446800 | 10 |

### Query 84
- Text: What is the rule about 5th-rank spells, ancestry feat, magical?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/411']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/411', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/427', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/403']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/411` | 0.860478 | 5th-rank spells, ancestry feat, magical fortitude, skill increase |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/427` | 0.695108 | 9th-rank spells, ancestry feat, quantum will, skill increase |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/403` | 0.691290 | 3rd-rank spells, ancestry feat, attribute boosts, reflex expertise, skill increase |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/13` | 0.627252 | In addition to the ancestry feat you started with, you gain an  ancestry feat at 5th level and every 4 levels thereafter. The  list of ancestry feats available to you can be found in your  ancestry's |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/419` | 0.622195 | 7th-rank spells, ancestry feat, quantum defenses, skill increase, weapon specialization |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/407` | 0.564269 | 4th-rank spells, expert spellcaster, general feat, skill increase |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/399` | 0.562904 | 2nd-rank spells, general feat, isolated spell matrix, signature spells, skill increase |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/415` | 0.555239 | 6th-rank spells, general feat, perception expertise, skill increase, weapon expertise |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/423` | 0.526686 | 8th-rank spells, attribute boosts, general feat, master spellcaster, skill increase |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/Table/2` | 0.526343 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, paradox, anchor, quantum field, witchwarper spellcasting, spell repertoire2Skill feat, witchwarper feat32nd-r |

### Query 85
- Text: Summarize 10
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/412']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/412', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/551', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/593']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/412` | 0.782219 | 10 |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/593` | 0.782219 | 10 |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/551` | 0.782219 | 10 |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/583` | 0.740219 | 10 |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/976` | 0.740219 | 10 |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/599` | 0.740219 | 10 |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/867` | 0.635691 | 10th |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/6` | 0.501945 | 10TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/414` | 0.492929 | 11 |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/988` | 0.492929 | 11 |

### Query 86
- Text: What is the rule about Attribute boosts, skill feat, witchwarper feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/413']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/413', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/433', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/405']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/413` | 0.902772 | Attribute boosts, skill feat, witchwarper feat |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/433` | 0.902772 | Attribute boosts, skill feat, witchwarper feat |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/405` | 0.736553 | Skill feat, witchwarper feat |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/421` | 0.694553 | Skill feat, witchwarper feat |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/425` | 0.694553 | Skill feat, witchwarper feat |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/417` | 0.694553 | Skill feat, witchwarper feat |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/409` | 0.694553 | Skill feat, witchwarper feat |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/429` | 0.694553 | Skill feat, witchwarper feat |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/401` | 0.694553 | Skill feat, witchwarper feat |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/397` | 0.694553 | Skill feat, witchwarper feat |

### Query 87
- Text: Summarize 11
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/414']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/988', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/414', 'PZO22001 Starfinder Player Core 162-173::/page/4/SectionHeader/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/988` | 0.764621 | 11 |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/414` | 0.764621 | 11 |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/4/SectionHeader/23` | 0.554831 | WEAPON EXPERTISE 11TH |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/4/SectionHeader/21` | 0.500289 | PERCEPTION EXPERTISE 11TH |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/1000` | 0.493902 | 12 |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/591` | 0.493902 | 12 |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/553` | 0.493902 | 12 |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/585` | 0.493902 | 12 |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/416` | 0.493902 | 12 |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/593` | 0.479429 | 10 |

### Query 88
- Text: What is the rule about 6th-rank spells, general feat, perception?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/415']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/415', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/411', 'PZO22001 Starfinder Player Core 162-173::/page/10/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/415` | 0.822135 | 6th-rank spells, general feat, perception expertise, skill increase, weapon expertise |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/411` | 0.615178 | 5th-rank spells, ancestry feat, magical fortitude, skill increase |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/42` | 0.608116 | You possess an uncanny sixth sense for ambient magic. You  can sense the presence of magic auras as though you were  always using a 1st-rank *detect magic* spell. This detects magic  in your field of |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/399` | 0.557317 | 2nd-rank spells, general feat, isolated spell matrix, signature spells, skill increase |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/407` | 0.556241 | 4th-rank spells, expert spellcaster, general feat, skill increase |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/423` | 0.537228 | 8th-rank spells, attribute boosts, general feat, master spellcaster, skill increase |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/403` | 0.522959 | 3rd-rank spells, ancestry feat, attribute boosts, reflex expertise, skill increase |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/22` | 0.513313 | You borrow spells from other realities. Twice per day, you can  cast a 9th-rank or lower spell after you've run out of spell slots  of the appropriate spell rank; the two spells you cast with this  fe |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/419` | 0.511696 | 7th-rank spells, ancestry feat, quantum defenses, skill increase, weapon specialization |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/427` | 0.505679 | 9th-rank spells, ancestry feat, quantum will, skill increase |

### Query 89
- Text: What is the rule about Skill feat, witchwarper feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/417']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/425', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/429', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/417']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/425` | 0.919131 | Skill feat, witchwarper feat |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/429` | 0.919131 | Skill feat, witchwarper feat |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/417` | 0.919131 | Skill feat, witchwarper feat |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/409` | 0.877131 | Skill feat, witchwarper feat |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/405` | 0.877131 | Skill feat, witchwarper feat |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/421` | 0.877131 | Skill feat, witchwarper feat |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/397` | 0.877131 | Skill feat, witchwarper feat |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/401` | 0.877131 | Skill feat, witchwarper feat |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/413` | 0.764002 | Attribute boosts, skill feat, witchwarper feat |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/433` | 0.764002 | Attribute boosts, skill feat, witchwarper feat |

### Query 90
- Text: What is the rule about 7th-rank spells, ancestry feat, quantum?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/419']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/419', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/427', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/411']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/419` | 0.812784 | 7th-rank spells, ancestry feat, quantum defenses, skill increase, weapon specialization |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/427` | 0.766318 | 9th-rank spells, ancestry feat, quantum will, skill increase |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/411` | 0.719441 | 5th-rank spells, ancestry feat, magical fortitude, skill increase |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/403` | 0.636523 | 3rd-rank spells, ancestry feat, attribute boosts, reflex expertise, skill increase |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/Table/2` | 0.558512 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, paradox, anchor, quantum field, witchwarper spellcasting, spell repertoire2Skill feat, witchwarper feat32nd-r |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/11` | 0.553864 | You command the most potent magic and can cast spells  of truly incredible power. Add two common 10th-rank  spells of your tradition to your repertoire. You gain a single  10th-rank spell slot you can |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/13` | 0.553152 | In addition to the ancestry feat you started with, you gain an  ancestry feat at 5th level and every 4 levels thereafter. The  list of ancestry feats available to you can be found in your  ancestry's |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/395` | 0.546894 | Ancestry and background, attribute boosts, initial proficiencies, paradox, anchor, quantum field, witchwarper spellcasting, spell repertoire |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/415` | 0.540137 | 6th-rank spells, general feat, perception expertise, skill increase, weapon expertise |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/399` | 0.528328 | 2nd-rank spells, general feat, isolated spell matrix, signature spells, skill increase |

### Query 91
- Text: What is the rule about Skill feat, witchwarper feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/421']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/425', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/429', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/417']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/425` | 0.919131 | Skill feat, witchwarper feat |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/429` | 0.919131 | Skill feat, witchwarper feat |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/417` | 0.919131 | Skill feat, witchwarper feat |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/409` | 0.877131 | Skill feat, witchwarper feat |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/405` | 0.877131 | Skill feat, witchwarper feat |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/421` | 0.877131 | Skill feat, witchwarper feat |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/397` | 0.877131 | Skill feat, witchwarper feat |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/401` | 0.877131 | Skill feat, witchwarper feat |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/413` | 0.764002 | Attribute boosts, skill feat, witchwarper feat |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/433` | 0.764002 | Attribute boosts, skill feat, witchwarper feat |

### Query 92
- Text: What is the rule about 8th-rank spells, attribute boosts, general?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/423']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/423', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/403', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/415']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/423` | 0.772903 | 8th-rank spells, attribute boosts, general feat, master spellcaster, skill increase |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/403` | 0.607070 | 3rd-rank spells, ancestry feat, attribute boosts, reflex expertise, skill increase |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/415` | 0.580627 | 6th-rank spells, general feat, perception expertise, skill increase, weapon expertise |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/407` | 0.528813 | 4th-rank spells, expert spellcaster, general feat, skill increase |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/427` | 0.525126 | 9th-rank spells, ancestry feat, quantum will, skill increase |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/399` | 0.524873 | 2nd-rank spells, general feat, isolated spell matrix, signature spells, skill increase |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/411` | 0.524693 | 5th-rank spells, ancestry feat, magical fortitude, skill increase |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/8` | 0.519515 | When you get spell slots of 2nd rank and higher, you can fill  those slots with stronger versions of lower-rank spells. This  increases the spell's rank, heightening it to match the spell  slot. You m |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/419` | 0.516018 | 7th-rank spells, ancestry feat, quantum defenses, skill increase, weapon specialization |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/5` | 0.512380 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |

### Query 93
- Text: What is the rule about Skill feat, witchwarper feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/425']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/425', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/429', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/417']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/425` | 0.919131 | Skill feat, witchwarper feat |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/429` | 0.919131 | Skill feat, witchwarper feat |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/417` | 0.919131 | Skill feat, witchwarper feat |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/409` | 0.877131 | Skill feat, witchwarper feat |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/405` | 0.877131 | Skill feat, witchwarper feat |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/421` | 0.877131 | Skill feat, witchwarper feat |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/397` | 0.877131 | Skill feat, witchwarper feat |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/401` | 0.877131 | Skill feat, witchwarper feat |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/413` | 0.764002 | Attribute boosts, skill feat, witchwarper feat |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/433` | 0.764002 | Attribute boosts, skill feat, witchwarper feat |

### Query 94
- Text: What is the rule about 9th-rank spells, ancestry feat, quantum will,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/427']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/427', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/411', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/419']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/427` | 0.903531 | 9th-rank spells, ancestry feat, quantum will, skill increase |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/411` | 0.705686 | 5th-rank spells, ancestry feat, magical fortitude, skill increase |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/419` | 0.698689 | 7th-rank spells, ancestry feat, quantum defenses, skill increase, weapon specialization |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/403` | 0.627413 | 3rd-rank spells, ancestry feat, attribute boosts, reflex expertise, skill increase |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/22` | 0.572937 | You borrow spells from other realities. Twice per day, you can  cast a 9th-rank or lower spell after you've run out of spell slots  of the appropriate spell rank; the two spells you cast with this  fe |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/11` | 0.566563 | You command the most potent magic and can cast spells  of truly incredible power. Add two common 10th-rank  spells of your tradition to your repertoire. You gain a single  10th-rank spell slot you can |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/Table/2` | 0.551336 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, paradox, anchor, quantum field, witchwarper spellcasting, spell repertoire2Skill feat, witchwarper feat32nd-r |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/395` | 0.530184 | Ancestry and background, attribute boosts, initial proficiencies, paradox, anchor, quantum field, witchwarper spellcasting, spell repertoire |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/399` | 0.526490 | 2nd-rank spells, general feat, isolated spell matrix, signature spells, skill increase |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/13` | 0.526478 | In addition to the ancestry feat you started with, you gain an  ancestry feat at 5th level and every 4 levels thereafter. The  list of ancestry feats available to you can be found in your  ancestry's |

### Query 95
- Text: What is the rule about Skill feat, witchwarper feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/429']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/425', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/429', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/417']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/425` | 0.919131 | Skill feat, witchwarper feat |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/429` | 0.919131 | Skill feat, witchwarper feat |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/417` | 0.919131 | Skill feat, witchwarper feat |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/409` | 0.877131 | Skill feat, witchwarper feat |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/405` | 0.877131 | Skill feat, witchwarper feat |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/421` | 0.877131 | Skill feat, witchwarper feat |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/397` | 0.877131 | Skill feat, witchwarper feat |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/401` | 0.877131 | Skill feat, witchwarper feat |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/413` | 0.764002 | Attribute boosts, skill feat, witchwarper feat |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/433` | 0.764002 | Attribute boosts, skill feat, witchwarper feat |

### Query 96
- Text: What is the rule about General feat, legendary spellcaster, quantum?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/431']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/431', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/407', 'PZO22001 Starfinder Player Core 162-173::/page/5/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/431` | 0.748557 | General feat, legendary spellcaster, quantum thesis, skill increase, warped infinities |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/407` | 0.603360 | 4th-rank spells, expert spellcaster, general feat, skill increase |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/11` | 0.573239 | You command the most potent magic and can cast spells  of truly incredible power. Add two common 10th-rank  spells of your tradition to your repertoire. You gain a single  10th-rank spell slot you can |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/419` | 0.527995 | 7th-rank spells, ancestry feat, quantum defenses, skill increase, weapon specialization |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/Table/2` | 0.526471 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, paradox, anchor, quantum field, witchwarper spellcasting, spell repertoire2Skill feat, witchwarper feat32nd-r |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/427` | 0.521080 | 9th-rank spells, ancestry feat, quantum will, skill increase |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/399` | 0.513375 | 2nd-rank spells, general feat, isolated spell matrix, signature spells, skill increase |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/423` | 0.508446 | 8th-rank spells, attribute boosts, general feat, master spellcaster, skill increase |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/3` | 0.506053 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/395` | 0.500564 | Ancestry and background, attribute boosts, initial proficiencies, paradox, anchor, quantum field, witchwarper spellcasting, spell repertoire |

### Query 97
- Text: What is the rule about Attribute boosts, skill feat, witchwarper feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/433']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/413', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/433', 'PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/405']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/413` | 0.902772 | Attribute boosts, skill feat, witchwarper feat |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/433` | 0.902772 | Attribute boosts, skill feat, witchwarper feat |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/405` | 0.736553 | Skill feat, witchwarper feat |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/421` | 0.694553 | Skill feat, witchwarper feat |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/425` | 0.694553 | Skill feat, witchwarper feat |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/417` | 0.694553 | Skill feat, witchwarper feat |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/409` | 0.694553 | Skill feat, witchwarper feat |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/429` | 0.694553 | Skill feat, witchwarper feat |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/401` | 0.694553 | Skill feat, witchwarper feat |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/397` | 0.694553 | Skill feat, witchwarper feat |

### Query 98
- Text: What is the rule about In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/Text/4', 'PZO22001 Starfinder Player Core 162-173::/page/2/Text/5', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/4` | 0.943824 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/5` | 0.843002 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/8` | 0.624984 | At 1st level, your class gives you  an attribute boost to your choice  of Charisma or Intelligence. |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/31` | 0.533965 | In addition to the abilities provided by your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/11` | 0.505161 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/59` | 0.482799 | Trained in a number of additional  skills equal to 3 plus your Intelligence  modifier |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/413` | 0.482616 | Attribute boosts, skill feat, witchwarper feat |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/433` | 0.482616 | Attribute boosts, skill feat, witchwarper feat |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/3` | 0.469559 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/29` | 0.468913 | You gain these abilities as a witchwarper. Abilities gained at higher levels list the  levels next to their names. |

### Query 99
- Text: What is the rule about At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get a partial boost and must boost that attribute again at a  later level to increase it by 1.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/Text/5', 'PZO22001 Starfinder Player Core 162-173::/page/2/Text/4', 'PZO22001 Starfinder Player Core 162-173::/page/1/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/5` | 0.966227 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/4` | 0.768876 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/11` | 0.601486 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/9` | 0.536168 | At 3rd level and every 2 levels thereafter, you gain a skill  increase. You can use this increase either to increase your  proficiency rank to trained in one skill you're untrained in or  to increase |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/10` | 0.514247 | At 7th level, you can use skill increases to increase your  proficiency rank to master in a skill in which you're already  an expert, and at 15th level, you can use them to increase  your proficiency |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/18` | 0.514061 | You add to this spell repertoire as you increase in level.  Each time you get a spell slot (see Witchwarper Spells per  Day on page 167), you add a spell to your spell repertoire of  the same rank. At |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/13` | 0.509327 | In addition to the ancestry feat you started with, you gain an  ancestry feat at 5th level and every 4 levels thereafter. The  list of ancestry feats available to you can be found in your  ancestry's |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/3` | 0.502212 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/8` | 0.464159 | When you get spell slots of 2nd rank and higher, you can fill  those slots with stronger versions of lower-rank spells. This  increases the spell's rank, heightening it to match the spell  slot. You m |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/24` | 0.460149 | At 2nd level and every even-numbered level thereafter, you  gain a skill feat. Skill feats can be found in Chapter 5 and  have the skill trait. You must be trained or better in the  corresponding skil |

### Query 100
- Text: What is the rule about Your existence is contrary to the status quo of the universe,  causing quantum ripples that empower your spellcasting  talent and open doorways to other worlds. Perhaps you're?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/2/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/2/Text/9', 'PZO22001 Starfinder Player Core 162-173::/page/3/Text/1', 'PZO22001 Starfinder Player Core 162-173::/page/10/Text/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/9` | 0.992398 | Your existence is contrary to the status quo of the universe,  causing quantum ripples that empower your spellcasting  talent and open doorways to other worlds. Perhaps you're |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/1` | 0.646036 | You're always ready to let loose with your paradoxical  abilities, and when imperiled, you instinctively release a pulse  of quantum energy. As combat begins, you Warp Reality. |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/25` | 0.636349 | You expose this reality to a realm of pure darkness filled with  gibbering voices and otherworldly entities. The area of your  quantum field functions as though it were an area of 2ndrank *darkness*. |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/15` | 0.594095 | You can draw on paradoxical forces to create a reality-warping  quantum field. It might manifest as a haze in the air that shows  shimmers of alternate realities, appear as walls of glowing  magical e |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/8` | 0.583238 | Your existence is an anomaly that defies the normal  parameters of your current reality. You might have  encountered something that disrupted your core existence,  or you crossed the veil from an alte |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/8/Text/42` | 0.580276 | **Trigger** A creature, trap, or similar object within your quantum  field casts a spell that you don't have in your spell repertoire,  and you're aware of the casting. |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/16` | 0.578261 | Your paradox represents an event or force that forever altered  you. Your chosen paradox determines your spellcasting  tradition and grants you trained proficiency in the listed  paradox skill. You au |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/10` | 0.574774 | from an alternate reality or a different timeline, or perhaps  you experienced an unnatural phenomenon that altered your  path, discovered a time-glitching alien device, or wrote a  treatise on quantu |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/35` | 0.571504 | The reality you conjure is much brighter than your own. The  area of your quantum field becomes bright light. Creatures  who begin their in your quantum field must attempt a  Fortitude save against yo |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/21` | 0.571179 | You temporarily share your quantum field with an ally. You  cause your quantum field to emanate from an ally you can  see instead of yourself. The ally gains all the benefits of your  quantum field, a |

### Query 101
- Text: Lookup values for Spell RankYour LevelCantrips1st2nd3rd4th5th6th7th8th9th10th153—————————254—————————3543————————4544————————55443———————65444———————754443——————854444——————9544443—————10544444—————115444443————125444444————1354444443———1454444444———15544444443——16544444444——175444444443—185444444444—1954444444441*2054444444441*
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/5/Table/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/5/Table/2', 'PZO22001 Starfinder Player Core 162-173::/page/2/Table/2', 'PZO22001 Starfinder Player Core 162-173::/page/6/Text/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/5/Table/2` | 1.019312 | Spell RankYour LevelCantrips1st2nd3rd4th5th6th7th8th9th10th153—————————254—————————3543————————4544————————55443———————65444———————754443——————854444——————9544443—————10544444—————115444443————1254444 |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/2/Table/2` | 0.640582 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, paradox, anchor, quantum field, witchwarper spellcasting, spell repertoire2Skill feat, witchwarper feat32nd-r |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/22` | 0.638738 | **Paradox Spells** cantrip: *injury echo*; 1st: *fleet step*; 2nd:  *temporal bullets*; 3rd: *time's edge*; 4th: *weight of ages*; 5th:  *chrono push*; 6th: *phantasmal calamity*; 7th: *true target*; |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/10` | 0.576433 | **Paradox Spells** cantrip: *stumble*; 1st: *shifting* *surge*; 2nd:  *dispel magic*; 3rd: *void* *whispers*; 4th: *eldritch* *wrath*; 5th:  *wall of stone*; 6th: *slice reality*; 7th: *death sentence |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/16` | 0.574687 | **Paradox Spells** cantrip: *daze*; 1st: *delete*; 2nd: *instant virus*;  3rd: *entropy strike*; 4th: *confusion*; 5th: *synaptic pulse*;  6th: *repulsion*; 7th: *warp mind*; 8th: *disappearance*; 9th |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/855` | 0.563108 | Spell Rank |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/7/Table/3` | 0.562724 | FeatLevelAdvanced Warp8Anchoring Strike1Borrow Spell14Cantrip Expansion2Complete Transposition18Conceal Spell2Danger Zone8Debris Zone1Enlarge Quantum Field6Folded Paradoxes16Fundamental Understanding2 |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/7/Table/13` | 0.543992 | FeatLevelPredict Outcome6Predictive Positioning2Quantum Aura6Quantum Entanglement8Quantum Negation20Quantum Recycle4Quantum Research20Quickened Casting10Radiant Zone12Reach Spell1Scrub Psyche2Sense Ab |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/20` | 0.539954 | **Paradox Spells** cantrip: *analyze* *target*; 1st: *sure strike*; 2nd:  *sift* *the* *sphere*; 3rd: *hypercognition*; 4th: *translocate*; 5th:  *subjective reality*; 6th: *truesight*; 7th: *retrocog |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/10` | 0.530724 | Some of your spells are cantrips. A cantrip is a special type  of spell that doesn't use spell slots. You can cast a cantrip  at will, any number of times per day. A cantrip is always  automatically h |

### Query 102
- Text: Lookup values for FeatLevelAdvanced Warp8Anchoring Strike1Borrow Spell14Cantrip Expansion2Complete Transposition18Conceal Spell2Danger Zone8Debris Zone1Enlarge Quantum Field6Folded Paradoxes16Fundamental Understanding2Greater Warp10In Another Life12Infinite Magic18Meandering Mind4Multiverse Magic14Nonlethal Spell2Otherworldly Spell1Persistent Quantum Field14
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/7/Table/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/7/Table/3', 'PZO22001 Starfinder Player Core 162-173::/page/7/Table/13', 'PZO22001 Starfinder Player Core 162-173::/page/2/Table/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/7/Table/3` | 1.007942 | FeatLevelAdvanced Warp8Anchoring Strike1Borrow Spell14Cantrip Expansion2Complete Transposition18Conceal Spell2Danger Zone8Debris Zone1Enlarge Quantum Field6Folded Paradoxes16Fundamental Understanding2 |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/Table/13` | 0.807384 | FeatLevelPredict Outcome6Predictive Positioning2Quantum Aura6Quantum Entanglement8Quantum Negation20Quantum Recycle4Quantum Research20Quickened Casting10Radiant Zone12Reach Spell1Scrub Psyche2Sense Ab |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/Table/2` | 0.717505 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, paradox, anchor, quantum field, witchwarper spellcasting, spell repertoire2Skill feat, witchwarper feat32nd-r |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/21` | 0.622656 | **Warp Spells** initial: *warp* *probability*; advanced: *alternate* *outcome*; greater: *quantum* *analysis* |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/16` | 0.606929 | Your paradox represents an event or force that forever altered  you. Your chosen paradox determines your spellcasting  tradition and grants you trained proficiency in the listed  paradox skill. You au |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/11` | 0.599995 | At 1st level, choose your paradox. Your chosen paradox  determines the tradition of your spells, additional trained  skills, additional spells you learn, and the effects of your  quantum field. You al |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/11` | 0.569467 | **Warp Spells** initial: *warp* *terrain*; advanced: *warp world*;  greater: *parallel* *forms* |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/395` | 0.567163 | Ancestry and background, attribute boosts, initial proficiencies, paradox, anchor, quantum field, witchwarper spellcasting, spell repertoire |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/431` | 0.559057 | General feat, legendary spellcaster, quantum thesis, skill increase, warped infinities |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/10` | 0.555863 | **Paradox Spells** cantrip: *stumble*; 1st: *shifting* *surge*; 2nd:  *dispel magic*; 3rd: *void* *whispers*; 4th: *eldritch* *wrath*; 5th:  *wall of stone*; 6th: *slice reality*; 7th: *death sentence |

### Query 103
- Text: Lookup values for FeatLevelPredict Outcome6Predictive Positioning2Quantum Aura6Quantum Entanglement8Quantum Negation20Quantum Recycle4Quantum Research20Quickened Casting10Radiant Zone12Reach Spell1Scrub Psyche2Sense Abnormalities12Share Quantum Aura10Soothing Anchor1Spellsurge Ammo4Twisted Dark Zone10Warp Wounds2Widen Spell1Zone Overlap16
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/7/Table/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/7/Table/13', 'PZO22001 Starfinder Player Core 162-173::/page/7/Table/3', 'PZO22001 Starfinder Player Core 162-173::/page/2/Table/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/7/Table/13` | 0.989652 | FeatLevelPredict Outcome6Predictive Positioning2Quantum Aura6Quantum Entanglement8Quantum Negation20Quantum Recycle4Quantum Research20Quickened Casting10Radiant Zone12Reach Spell1Scrub Psyche2Sense Ab |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/Table/3` | 0.768383 | FeatLevelAdvanced Warp8Anchoring Strike1Borrow Spell14Cantrip Expansion2Complete Transposition18Conceal Spell2Danger Zone8Debris Zone1Enlarge Quantum Field6Folded Paradoxes16Fundamental Understanding2 |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/2/Table/2` | 0.660709 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, paradox, anchor, quantum field, witchwarper spellcasting, spell repertoire2Skill feat, witchwarper feat32nd-r |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/21` | 0.575164 | **Warp Spells** initial: *warp* *probability*; advanced: *alternate* *outcome*; greater: *quantum* *analysis* |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/5/Footnote/3` | 0.524983 | * The quantum thesis class feature gives you a 10th-rank spell slot that works a bit differently from other spell slots. |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/35` | 0.522766 | **Trigger** You cast a 2nd-rank or higher spell, and the spell  targets a creature or area within your quantum field. |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/11` | 0.518054 | At 1st level, choose your paradox. Your chosen paradox  determines the tradition of your spells, additional trained  skills, additional spells you learn, and the effects of your  quantum field. You al |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/2` | 0.517794 | Use this table to look up witchwarper feats by name. |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/16` | 0.517505 | Your paradox represents an event or force that forever altered  you. Your chosen paradox determines your spellcasting  tradition and grants you trained proficiency in the listed  paradox skill. You au |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/5/Table/2` | 0.515815 | Spell RankYour LevelCantrips1st2nd3rd4th5th6th7th8th9th10th153—————————254—————————3543————————4544————————55443———————65444———————754443——————854444——————9544443—————10544444—————115444443————1254444 |

### Query 104
- Text: What are the requirements for **ANCHORING STRIKE **[one-action] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/16', 'PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/19', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/530']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/16` | 0.921057 | **ANCHORING STRIKE **[one-action] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/19` | 0.642968 | **SOOTHING ANCHOR **[one-action] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/530` | 0.623101 | Anchoring Strike |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/21` | 0.564103 | **Critical Success** The Strike gains the anchoring trait. You can  reroll the damage dice rolled for this strike, but you must  use the second result, even if it's worse. |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/22` | 0.540333 | **Success** The Strike gains the anchoring trait. |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/15` | 0.460651 | **REACH SPELL **[one-action] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/2` | 0.442553 | **QUANTUM ENTANGLEMENT **[one-action] **FEAT 8** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/8/Text/23` | 0.439993 | **Requirements** Your last action was to Sustain your quantum  field or had the anchoring trait. |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/25` | 0.439353 | **WIDEN SPELL **[one-action] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/45` | 0.426363 | **ENLARGE QUANTUM FIELD **[one-action] **FEAT 6** |

### Query 105
- Text: What are the requirements for **DEBRIS ZONE **[one-action] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/23', 'PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/63', 'PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/23` | 0.902533 | **DEBRIS ZONE **[one-action] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/63` | 0.654373 | **DANGER ZONE **[one-action] **FEAT 8** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/32` | 0.596333 | **RADIANT ZONE **[one-action] **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/22` | 0.549402 | **TWISTED DARK ZONE **[one-action] **FEAT 10** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/542` | 0.548336 | Debris Zone |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/7` | 0.511100 | **ZONE OVERLAP **[one-action] **FEAT 16** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/25` | 0.464525 | **WIDEN SPELL **[one-action] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/15` | 0.453502 | **REACH SPELL **[one-action] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/12` | 0.445407 | You cause a second zone to overlap your quantum field. You  can choose to apply another zone you're able to create, or  apply the existing zone again, improving its effects as follows:  Danger Zone de |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/27` | 0.439702 | **OTHERWORLDLY SPELL **[one-action] **FEAT 1** |

### Query 106
- Text: What are the requirements for **OTHERWORLDLY SPELL **[one-action] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/27', 'PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/25', 'PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/27` | 0.900021 | **OTHERWORLDLY SPELL **[one-action] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/25` | 0.711307 | **WIDEN SPELL **[one-action] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/15` | 0.698555 | **REACH SPELL **[one-action] **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/34` | 0.651555 | **CONCEAL SPELL **[one-action] **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/2` | 0.646638 | **NONLETHAL SPELL **[one-action] **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/562` | 0.498711 | Otherworldly Spell |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/44` | 0.498027 | **BORROW SPELL **[free-action] **FEAT 14** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/23` | 0.482301 | **DEBRIS ZONE **[one-action] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/19` | 0.479400 | **SOOTHING ANCHOR **[one-action] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/3/SectionHeader/29` | 0.476771 | **ISOLATED SPELL MATRIX **[one-action] |

### Query 107
- Text: What are the requirements for **REACH SPELL **[one-action] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/15', 'PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/25', 'PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/15` | 0.912330 | **REACH SPELL **[one-action] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/25` | 0.704854 | **WIDEN SPELL **[one-action] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/34` | 0.696623 | **CONCEAL SPELL **[one-action] **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/27` | 0.613660 | **OTHERWORLDLY SPELL **[one-action] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/2` | 0.610940 | **NONLETHAL SPELL **[one-action] **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/586` | 0.497331 | Reach Spell |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/44` | 0.493631 | **BORROW SPELL **[free-action] **FEAT 14** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/3/SectionHeader/29` | 0.483541 | **ISOLATED SPELL MATRIX **[one-action] |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/46` | 0.471806 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/33` | 0.471806 | **SPELLS** |

### Query 108
- Text: What are the requirements for **SOOTHING ANCHOR **[one-action] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/19', 'PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/16', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/594']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/19` | 0.914953 | **SOOTHING ANCHOR **[one-action] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/16` | 0.634755 | **ANCHORING STRIKE **[one-action] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/594` | 0.508480 | Soothing Anchor |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/25` | 0.442622 | **WIDEN SPELL **[one-action] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/2` | 0.436356 | **QUANTUM ENTANGLEMENT **[one-action] **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/15` | 0.435883 | **REACH SPELL **[one-action] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/27` | 0.434723 | **OTHERWORLDLY SPELL **[one-action] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/14` | 0.430468 | one of the following feats. You must satisfy any prerequisites  before taking the feat. |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/5` | 0.427411 | **Anchor Benefit** Your single-minded focus helps you  concentrate. If a reaction would disrupt your spellcasting  action, attempt a DC 15 flat check. If you succeed, your  action isn't disrupted. |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/34` | 0.426040 | **CONCEAL SPELL **[one-action] **FEAT 2** |

### Query 109
- Text: What are the requirements for **WIDEN SPELL **[one-action] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/25', 'PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/15', 'PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/25` | 0.901243 | **WIDEN SPELL **[one-action] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/15` | 0.714043 | **REACH SPELL **[one-action] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/34` | 0.698789 | **CONCEAL SPELL **[one-action] **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/27` | 0.636039 | **OTHERWORLDLY SPELL **[one-action] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/2` | 0.629089 | **NONLETHAL SPELL **[one-action] **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/44` | 0.502578 | **BORROW SPELL **[free-action] **FEAT 14** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/26` | 0.476273 | **MEANDERING MIND **[one-action] **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/23` | 0.474447 | **DEBRIS ZONE **[one-action] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/19` | 0.464463 | **SOOTHING ANCHOR **[one-action] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/602` | 0.463077 | Widen Spell |

### Query 110
- Text: What are the requirements for **CANTRIP EXPANSION** **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/30', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/534', 'PZO22001 Starfinder Player Core 162-173::/page/7/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/30` | 0.912715 | **CANTRIP EXPANSION** **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/534` | 0.561950 | Cantrip Expansion |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/14` | 0.458572 | one of the following feats. You must satisfy any prerequisites  before taking the feat. |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/4/Text/13` | 0.414767 | In addition to the ancestry feat you started with, you gain an  ancestry feat at 5th level and every 4 levels thereafter. The  list of ancestry feats available to you can be found in your  ancestry's |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/Table/3` | 0.404639 | FeatLevelAdvanced Warp8Anchoring Strike1Borrow Spell14Cantrip Expansion2Complete Transposition18Conceal Spell2Danger Zone8Debris Zone1Enlarge Quantum Field6Folded Paradoxes16Fundamental Understanding2 |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/38` | 0.401948 | **FUNDAMENTAL UNDERSTANDING **[reaction] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/3/SectionHeader/22` | 0.388703 | SKILL FEATS 2ND |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/3/SectionHeader/25` | 0.385922 | WITCHWARPER FEATS 2ND |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/399` | 0.374112 | 2nd-rank spells, general feat, isolated spell matrix, signature spells, skill increase |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/Table/2` | 0.368597 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, paradox, anchor, quantum field, witchwarper spellcasting, spell repertoire2Skill feat, witchwarper feat32nd-r |

### Query 111
- Text: What are the requirements for **CONCEAL SPELL **[one-action] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/34', 'PZO22001 Starfinder Player Core 162-173::/page/9/Text/2', 'PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/34` | 0.904200 | **CONCEAL SPELL **[one-action] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/2` | 0.717039 | **NONLETHAL SPELL **[one-action] **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/25` | 0.671951 | **WIDEN SPELL **[one-action] **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/15` | 0.625761 | **REACH SPELL **[one-action] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/27` | 0.583479 | **OTHERWORLDLY SPELL **[one-action] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/44` | 0.494669 | **BORROW SPELL **[free-action] **FEAT 14** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/538` | 0.477880 | Conceal Spell |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/3/SectionHeader/29` | 0.456291 | **ISOLATED SPELL MATRIX **[one-action] |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/42` | 0.453673 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/46` | 0.453673 | **SPELLS** |

### Query 112
- Text: What are the requirements for **FUNDAMENTAL UNDERSTANDING **[reaction] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/38']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/38', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/548', 'PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/38` | 0.931470 | **FUNDAMENTAL UNDERSTANDING **[reaction] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/548` | 0.616699 | Fundamental Understanding |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/6` | 0.527978 | **PREDICTIVE POSITIONING **[reaction] **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/19` | 0.441959 | **WARP WOUNDS **[reaction] **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/30` | 0.421022 | **CANTRIP EXPANSION** **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/13` | 0.412785 | **SCRUB PSYCHE **[reaction] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/31` | 0.400349 | **Prerequisites** quantum thesis |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/3/SectionHeader/22` | 0.399750 | SKILL FEATS 2ND |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/14` | 0.396987 | one of the following feats. You must satisfy any prerequisites  before taking the feat. |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/54` | 0.389850 | **PERSISTENT QUANTUM FIELD **[two-actions] **FEAT 14** |

### Query 113
- Text: What are the requirements for **Prerequisites** analyst paradox?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/8/Text/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/8/Text/41', 'PZO22001 Starfinder Player Core 162-173::/page/9/Text/22', 'PZO22001 Starfinder Player Core 162-173::/page/11/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/8/Text/41` | 0.975276 | **Prerequisites** analyst paradox |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/22` | 0.757139 | **Prerequisites** anomaly paradox |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/5` | 0.712148 | **Prerequisites** master in a paradox skill for a paradox other  than your chosen paradox |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/9` | 0.642544 | **Prerequisites** precog paradox |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/16` | 0.552393 | **Prerequisites** Gap influenced paradox |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/31` | 0.485270 | **Prerequisites** quantum thesis |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/58` | 0.480276 | Trained in one skill determined by  your paradox |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/6` | 0.470956 | Your paradoxical nature has become multifaceted. During daily  preparations, you can replace one of your paradox spells with a  spell of another paradox that grants training in the prerequisite  parad |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/11` | 0.435706 | At 1st level, choose your paradox. Your chosen paradox  determines the tradition of your spells, additional trained  skills, additional spells you learn, and the effects of your  quantum field. You al |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/546` | 0.434584 | Folded Paradoxes |

### Query 114
- Text: What are the requirements for **NONLETHAL SPELL **[one-action] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/9/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/9/Text/2', 'PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/34', 'PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/2` | 0.894659 | **NONLETHAL SPELL **[one-action] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/34` | 0.724612 | **CONCEAL SPELL **[one-action] **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/25` | 0.644864 | **WIDEN SPELL **[one-action] **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/15` | 0.590850 | **REACH SPELL **[one-action] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/27` | 0.589168 | **OTHERWORLDLY SPELL **[one-action] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/560` | 0.505909 | Nonlethal Spell |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/44` | 0.486762 | **BORROW SPELL **[free-action] **FEAT 14** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/2` | 0.447544 | **QUANTUM ENTANGLEMENT **[one-action] **FEAT 8** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/3/SectionHeader/29` | 0.439795 | **ISOLATED SPELL MATRIX **[one-action] |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/40` | 0.433016 | **SKILLS** **FEATS** |

### Query 115
- Text: What are the requirements for **PREDICTIVE POSITIONING **[reaction] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/6', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/570', 'PZO22001 Starfinder Player Core 162-173::/page/8/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/6` | 0.908944 | **PREDICTIVE POSITIONING **[reaction] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/570` | 0.605135 | Predictive Positioning |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/8/Text/11` | 0.577599 | Predictive Positioning (2nd), Predict Outcome (8th),  Quickened Casting (10th) |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/38` | 0.513127 | **FUNDAMENTAL UNDERSTANDING **[reaction] **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/14` | 0.455934 | one of the following feats. You must satisfy any prerequisites  before taking the feat. |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/49` | 0.433564 | **PREDICT OUTCOME** **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/9` | 0.427103 | **Prerequisites** precog paradox |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/1/SectionHeader/51` | 0.418594 | **INITIAL PROFICIENCIES** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/13` | 0.406492 | **SCRUB PSYCHE **[reaction] **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/31` | 0.398366 | **SKILLS** **FEATS** |

### Query 116
- Text: What are the requirements for **Prerequisites** precog paradox?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/9/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/9/Text/9', 'PZO22001 Starfinder Player Core 162-173::/page/8/Text/41', 'PZO22001 Starfinder Player Core 162-173::/page/9/Text/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/9` | 0.976822 | **Prerequisites** precog paradox |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/8/Text/41` | 0.721810 | **Prerequisites** analyst paradox |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/22` | 0.704393 | **Prerequisites** anomaly paradox |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/5` | 0.606702 | **Prerequisites** master in a paradox skill for a paradox other  than your chosen paradox |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/16` | 0.569167 | **Prerequisites** Gap influenced paradox |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/2` | 0.549322 | **PRECOG** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/8/Text/9` | 0.522449 | Precog |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/6/SectionHeader/19` | 0.518476 | PRECOG |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/31` | 0.471870 | **Prerequisites** quantum thesis |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/19` | 0.444195 | **Prerequisites** quantum aura |

### Query 117
- Text: What are the requirements for **SCRUB PSYCHE **[reaction] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/13', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/588', 'PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/38']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/13` | 0.892918 | **SCRUB PSYCHE **[reaction] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/588` | 0.598382 | Scrub Psyche |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/38` | 0.536666 | **FUNDAMENTAL UNDERSTANDING **[reaction] **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/6` | 0.467569 | **PREDICTIVE POSITIONING **[reaction] **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/42` | 0.430751 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/31` | 0.430751 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/78` | 0.430751 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/40` | 0.430751 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/14` | 0.421561 | one of the following feats. You must satisfy any prerequisites  before taking the feat. |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/3/SectionHeader/22` | 0.418730 | SKILL FEATS 2ND |

### Query 118
- Text: What are the requirements for **Prerequisites** Gap influenced paradox?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/9/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/9/Text/16', 'PZO22001 Starfinder Player Core 162-173::/page/8/Text/41', 'PZO22001 Starfinder Player Core 162-173::/page/9/Text/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/16` | 0.948783 | **Prerequisites** Gap influenced paradox |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/8/Text/41` | 0.702739 | **Prerequisites** analyst paradox |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/22` | 0.678409 | **Prerequisites** anomaly paradox |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/9` | 0.621449 | **Prerequisites** precog paradox |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/5` | 0.607712 | **Prerequisites** master in a paradox skill for a paradox other  than your chosen paradox |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/6/SectionHeader/13` | 0.518924 | GAP INFLUENCED |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/31` | 0.478176 | **Prerequisites** quantum thesis |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/16` | 0.457436 | Your paradox represents an event or force that forever altered  you. Your chosen paradox determines your spellcasting  tradition and grants you trained proficiency in the listed  paradox skill. You au |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/11` | 0.456844 | At 1st level, choose your paradox. Your chosen paradox  determines the tradition of your spells, additional trained  skills, additional spells you learn, and the effects of your  quantum field. You al |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/546` | 0.438778 | Folded Paradoxes |

### Query 119
- Text: What are the requirements for **WARP WOUNDS **[reaction] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/19', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/600', 'PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/38']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/19` | 0.877632 | **WARP WOUNDS **[reaction] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/600` | 0.579417 | Warp Wounds |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/38` | 0.550520 | **FUNDAMENTAL UNDERSTANDING **[reaction] **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/3/SectionHeader/25` | 0.482116 | WITCHWARPER FEATS 2ND |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/59` | 0.480666 | **ADVANCED WARP** **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/7` | 0.468431 | **GREATER WARP** **FEAT 10** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/SectionHeader/17` | 0.466734 | **WARP REALITY **[one-action] |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/6` | 0.438517 | **PREDICTIVE POSITIONING **[reaction] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/13` | 0.428266 | **SCRUB PSYCHE **[reaction] **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/42` | 0.417408 | **SKILLS** **FEATS** |

### Query 120
- Text: What are the requirements for **Prerequisites** anomaly paradox?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/9/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/9/Text/22', 'PZO22001 Starfinder Player Core 162-173::/page/8/Text/41', 'PZO22001 Starfinder Player Core 162-173::/page/9/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/22` | 0.958580 | **Prerequisites** anomaly paradox |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/8/Text/41` | 0.776093 | **Prerequisites** analyst paradox |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/9` | 0.698631 | **Prerequisites** precog paradox |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/5` | 0.637104 | **Prerequisites** master in a paradox skill for a paradox other  than your chosen paradox |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/16` | 0.550977 | **Prerequisites** Gap influenced paradox |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/31` | 0.482245 | **Prerequisites** quantum thesis |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/19` | 0.461042 | **Prerequisites** quantum aura |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/6` | 0.454668 | Your paradoxical nature has become multifaceted. During daily  preparations, you can replace one of your paradox spells with a  spell of another paradox that grants training in the prerequisite  parad |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/16` | 0.443101 | Your paradox represents an event or force that forever altered  you. Your chosen paradox determines your spellcasting  tradition and grants you trained proficiency in the listed  paradox skill. You au |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/546` | 0.436323 | Folded Paradoxes |

### Query 121
- Text: What are the requirements for **MEANDERING MIND **[one-action] **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/26', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/556', 'PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/26` | 0.893608 | **MEANDERING MIND **[one-action] **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/556` | 0.576332 | Meandering Mind |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/25` | 0.508778 | **WIDEN SPELL **[one-action] **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/2` | 0.459325 | **QUANTUM ENTANGLEMENT **[one-action] **FEAT 8** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/63` | 0.442823 | **DANGER ZONE **[one-action] **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/45` | 0.436414 | **ENLARGE QUANTUM FIELD **[one-action] **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/23` | 0.429542 | **DEBRIS ZONE **[one-action] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/14` | 0.427043 | one of the following feats. You must satisfy any prerequisites  before taking the feat. |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/32` | 0.425929 | **RADIANT ZONE **[one-action] **FEAT 12** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/38` | 0.424840 | **FUNDAMENTAL UNDERSTANDING **[reaction] **FEAT 2** |

### Query 122
- Text: What are the requirements for **QUANTUM RECYCLE **[reaction] **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/31', 'PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/28', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/578']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/31` | 0.932155 | **QUANTUM RECYCLE **[reaction] **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/28` | 0.637418 | **QUANTUM RESEARCH** **FEAT 20** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/578` | 0.606312 | Quantum Recycle |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/2` | 0.561004 | **QUANTUM ENTANGLEMENT **[one-action] **FEAT 8** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/24` | 0.545902 | **QUANTUM NEGATION** **FEAT 20** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/54` | 0.515726 | **QUANTUM AURA** **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/31` | 0.486381 | **Prerequisites** quantum thesis |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/SectionHeader/22` | 0.485654 | **QUANTUM PULSE **[free-action] |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/16` | 0.464188 | **SHARE QUANTUM AURA **[one-action] **FEAT 10** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/45` | 0.457130 | **ENLARGE QUANTUM FIELD **[one-action] **FEAT 6** |

### Query 123
- Text: What are the requirements for **SPELLSURGE AMMO **[free-action] **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/38']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/38', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/596', 'PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/44']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/38` | 0.915996 | **SPELLSURGE AMMO **[free-action] **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/596` | 0.608800 | Spellsurge Ammo |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/44` | 0.493562 | **BORROW SPELL **[free-action] **FEAT 14** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/2` | 0.428012 | **NONLETHAL SPELL **[one-action] **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/15` | 0.425532 | **REACH SPELL **[one-action] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/34` | 0.418874 | **CONCEAL SPELL **[one-action] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/14` | 0.400429 | one of the following feats. You must satisfy any prerequisites  before taking the feat. |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/25` | 0.395900 | **WIDEN SPELL **[one-action] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/27` | 0.389371 | **OTHERWORLDLY SPELL **[one-action] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/26` | 0.375237 | **MEANDERING MIND **[one-action] **FEAT 4** |

### Query 124
- Text: What are the requirements for **ENLARGE QUANTUM FIELD **[one-action] **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/45']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/45', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/544', 'PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/45` | 0.923014 | **ENLARGE QUANTUM FIELD **[one-action] **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/544` | 0.649432 | Enlarge Quantum Field |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/2` | 0.618059 | **QUANTUM ENTANGLEMENT **[one-action] **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/54` | 0.547044 | **PERSISTENT QUANTUM FIELD **[two-actions] **FEAT 14** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/19` | 0.527804 | **Requirements** Your quantum field is active. |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/11` | 0.527804 | **Requirements** Your quantum field is active. |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/29` | 0.527804 | **Requirements** Your quantum field is active. |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/16` | 0.525284 | **SHARE QUANTUM AURA **[one-action] **FEAT 10** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/11` | 0.518603 | **Requirements** Your quantum field is active with one zone  affecting it. |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/19` | 0.516729 | **Requirements** Your quantum field isn't active. |

### Query 125
- Text: What are the requirements for **PREDICT OUTCOME** **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/49']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/49', 'PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/54', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/573']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/49` | 0.888426 | **PREDICT OUTCOME** **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/54` | 0.497592 | **QUANTUM AURA** **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/573` | 0.457151 | 6 |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/928` | 0.415151 | 6 |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/569` | 0.415151 | 6 |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/545` | 0.415151 | 6 |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/404` | 0.415151 | 6 |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/45` | 0.414452 | **ENLARGE QUANTUM FIELD **[one-action] **FEAT 6** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/14` | 0.405103 | one of the following feats. You must satisfy any prerequisites  before taking the feat. |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/6` | 0.395713 | **PREDICTIVE POSITIONING **[reaction] **FEAT 2** |

### Query 126
- Text: What are the requirements for **QUANTUM AURA** **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/54']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/54', 'PZO22001 Starfinder Player Core 162-173::/page/10/Text/19', 'PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/54` | 0.909218 | **QUANTUM AURA** **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/19` | 0.640817 | **Prerequisites** quantum aura |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/16` | 0.615034 | **SHARE QUANTUM AURA **[one-action] **FEAT 10** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/28` | 0.532648 | **QUANTUM RESEARCH** **FEAT 20** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/31` | 0.501910 | **QUANTUM RECYCLE **[reaction] **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/24` | 0.500951 | **QUANTUM NEGATION** **FEAT 20** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/2` | 0.499993 | **QUANTUM ENTANGLEMENT **[one-action] **FEAT 8** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/49` | 0.497655 | **PREDICT OUTCOME** **FEAT 6** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/572` | 0.494168 | Quantum Aura |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/45` | 0.485317 | **ENLARGE QUANTUM FIELD **[one-action] **FEAT 6** |

### Query 127
- Text: What are the requirements for **ADVANCED WARP** **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/59']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/59', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/528', 'PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/59` | 0.923286 | **ADVANCED WARP** **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/528` | 0.577209 | Advanced Warp |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/7` | 0.555076 | **GREATER WARP** **FEAT 10** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/2/SectionHeader/1` | 0.417211 | **WITCHWARPER ADVANCEMENT** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/529` | 0.414807 | 8 |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/11` | 0.408748 | WITCHWARPER FEATS |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/19` | 0.406860 | **WARP WOUNDS **[reaction] **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/575` | 0.402808 | 8 |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/541` | 0.402808 | 8 |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/952` | 0.402808 | 8 |

### Query 128
- Text: What are the requirements for **DANGER ZONE **[one-action] **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/63']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/63', 'PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/23', 'PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/63` | 0.899985 | **DANGER ZONE **[one-action] **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/23` | 0.661126 | **DEBRIS ZONE **[one-action] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/32` | 0.650264 | **RADIANT ZONE **[one-action] **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/22` | 0.600205 | **TWISTED DARK ZONE **[one-action] **FEAT 10** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/540` | 0.575016 | Danger Zone |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/2` | 0.524582 | **QUANTUM ENTANGLEMENT **[one-action] **FEAT 8** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/7` | 0.511879 | **ZONE OVERLAP **[one-action] **FEAT 16** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/66` | 0.483463 | Your quantum field merges with a more dangerous reality,  becoming hazardous terrain that deals 1 damage to an enemy  each time it enters a square in the area. You choose the damage  type when you use |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/45` | 0.456706 | **ENLARGE QUANTUM FIELD **[one-action] **FEAT 6** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/25` | 0.454378 | **WIDEN SPELL **[one-action] **FEAT 1** |

### Query 129
- Text: What are the requirements for **QUANTUM ENTANGLEMENT **[one-action] **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/2', 'PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/45', 'PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/24']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/2` | 0.943253 | **QUANTUM ENTANGLEMENT **[one-action] **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/45` | 0.609168 | **ENLARGE QUANTUM FIELD **[one-action] **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/24` | 0.564135 | **QUANTUM NEGATION** **FEAT 20** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/16` | 0.514999 | **SHARE QUANTUM AURA **[one-action] **FEAT 10** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/31` | 0.514375 | **QUANTUM RECYCLE **[reaction] **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/28` | 0.500628 | **QUANTUM RESEARCH** **FEAT 20** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/63` | 0.498987 | **DANGER ZONE **[one-action] **FEAT 8** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/2/SectionHeader/22` | 0.492564 | **QUANTUM PULSE **[free-action] |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/574` | 0.492082 | Quantum Entanglement |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/54` | 0.488664 | **QUANTUM AURA** **FEAT 6** |

### Query 130
- Text: What are the requirements for **GREATER WARP** **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/7', 'PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/59', 'PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/7` | 0.906134 | **GREATER WARP** **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/59` | 0.587393 | **ADVANCED WARP** **FEAT 8** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/11` | 0.492864 | WITCHWARPER FEATS |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/550` | 0.436420 | Greater Warp |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/14` | 0.429005 | one of the following feats. You must satisfy any prerequisites  before taking the feat. |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/528` | 0.428551 | Advanced Warp |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/1` | 0.419583 | **WITCHWARPER FEATS BY NAME** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/3/SectionHeader/25` | 0.410111 | WITCHWARPER FEATS 2ND |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/19` | 0.406841 | **WARP WOUNDS **[reaction] **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/23` | 0.391527 | **Warp Spells** initial: *warp* *time*; advanced: *accelerate*; greater:  *time* *loop* |

### Query 131
- Text: What are the requirements for **QUICKENED CASTING **[free-action] **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/11', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/582', 'PZO22001 Starfinder Player Core 162-173::/page/8/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/11` | 0.926167 | **QUICKENED CASTING **[free-action] **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/582` | 0.590758 | Quickened Casting |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/8/Text/11` | 0.516041 | Predictive Positioning (2nd), Predict Outcome (8th),  Quickened Casting (10th) |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/22` | 0.462596 | **TWISTED DARK ZONE **[one-action] **FEAT 10** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/16` | 0.433632 | **SHARE QUANTUM AURA **[one-action] **FEAT 10** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/14` | 0.403126 | one of the following feats. You must satisfy any prerequisites  before taking the feat. |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/78` | 0.390936 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/42` | 0.390936 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/40` | 0.390936 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/31` | 0.390936 | **SKILLS** **FEATS** |

### Query 132
- Text: What are the requirements for **SHARE QUANTUM AURA **[one-action] **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/16', 'PZO22001 Starfinder Player Core 162-173::/page/10/Text/19', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/592']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/16` | 0.940890 | **SHARE QUANTUM AURA **[one-action] **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/19` | 0.658164 | **Prerequisites** quantum aura |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/592` | 0.658056 | Share Quantum Aura |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/54` | 0.555095 | **QUANTUM AURA** **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/572` | 0.523449 | Quantum Aura |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/45` | 0.506956 | **ENLARGE QUANTUM FIELD **[one-action] **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/7/Table/13` | 0.504209 | FeatLevelPredict Outcome6Predictive Positioning2Quantum Aura6Quantum Entanglement8Quantum Negation20Quantum Recycle4Quantum Research20Quickened Casting10Radiant Zone12Reach Spell1Scrub Psyche2Sense Ab |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/2` | 0.498892 | **QUANTUM ENTANGLEMENT **[one-action] **FEAT 8** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/31` | 0.454276 | **Prerequisites** quantum thesis |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/22` | 0.451441 | **TWISTED DARK ZONE **[one-action] **FEAT 10** |

### Query 133
- Text: What are the requirements for **Prerequisites** quantum aura?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/10/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/10/Text/19', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/572', 'PZO22001 Starfinder Player Core 162-173::/page/11/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/19` | 0.975065 | **Prerequisites** quantum aura |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/572` | 0.693568 | Quantum Aura |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/31` | 0.675841 | **Prerequisites** quantum thesis |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/592` | 0.598555 | Share Quantum Aura |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/19` | 0.540615 | **Requirements** Your quantum field isn't active. |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/11` | 0.539804 | **Requirements** Your quantum field is active. |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/29` | 0.539804 | **Requirements** Your quantum field is active. |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/19` | 0.539804 | **Requirements** Your quantum field is active. |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/8/Text/23` | 0.466156 | **Requirements** Your last action was to Sustain your quantum  field or had the anchoring trait. |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/16` | 0.457413 | **SHARE QUANTUM AURA **[one-action] **FEAT 10** |

### Query 134
- Text: What are the requirements for **TWISTED DARK ZONE **[one-action] **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/22', 'PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/63', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/598']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/22` | 0.893172 | **TWISTED DARK ZONE **[one-action] **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/63` | 0.619997 | **DANGER ZONE **[one-action] **FEAT 8** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/598` | 0.619466 | Twisted Dark Zone |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/32` | 0.570800 | **RADIANT ZONE **[one-action] **FEAT 12** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/23` | 0.538000 | **DEBRIS ZONE **[one-action] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/11` | 0.500514 | **QUICKENED CASTING **[free-action] **FEAT 10** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/16` | 0.498548 | **SHARE QUANTUM AURA **[one-action] **FEAT 10** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/12` | 0.470798 | You cause a second zone to overlap your quantum field. You  can choose to apply another zone you're able to create, or  apply the existing zone again, improving its effects as follows:  Danger Zone de |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/7` | 0.466292 | **ZONE OVERLAP **[one-action] **FEAT 16** |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/24` | 0.448621 | **ANCHORING** **DARKNESS** **WITCHWARPER** **ZONE** |

### Query 135
- Text: What are the requirements for **IN ANOTHER LIFE** **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/27', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/552', 'PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/39']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/27` | 0.858470 | **IN ANOTHER LIFE** **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/552` | 0.575932 | In Another Life |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/39` | 0.548597 | **SENSE ABNORMALITIES** **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/553` | 0.487593 | 12 |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/1000` | 0.475593 | 12 |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/416` | 0.475593 | 12 |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/585` | 0.475593 | 12 |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/591` | 0.475593 | 12 |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/26` | 0.447448 | 12TH LEVEL |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/32` | 0.439532 | **RADIANT ZONE **[one-action] **FEAT 12** |

### Query 136
- Text: What are the requirements for **RADIANT ZONE **[one-action] **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/32', 'PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/63', 'PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/32` | 0.912257 | **RADIANT ZONE **[one-action] **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/63` | 0.647254 | **DANGER ZONE **[one-action] **FEAT 8** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/22` | 0.621591 | **TWISTED DARK ZONE **[one-action] **FEAT 10** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/584` | 0.572057 | Radiant Zone |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/23` | 0.557402 | **DEBRIS ZONE **[one-action] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/7` | 0.517226 | **ZONE OVERLAP **[one-action] **FEAT 16** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/11` | 0.474651 | **Requirements** Your quantum field is active with one zone  affecting it. |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/45` | 0.470325 | **ENLARGE QUANTUM FIELD **[one-action] **FEAT 6** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/5` | 0.447328 | **Zone:** These actions apply an additional effect to your  quantum field. You can apply the effects of a zone only  to a quantum field that doesn't have a zone effect. |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/25` | 0.437084 | **WIDEN SPELL **[one-action] **FEAT 1** |

### Query 137
- Text: What are the requirements for **SENSE ABNORMALITIES** **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/39', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/590', 'PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/27']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/39` | 0.910534 | **SENSE ABNORMALITIES** **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/590` | 0.596435 | Sense Abnormalities |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/27` | 0.498261 | **IN ANOTHER LIFE** **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/40` | 0.432250 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/42` | 0.432250 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/78` | 0.432250 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/31` | 0.432250 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/591` | 0.410918 | 12 |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/22` | 0.407496 | **Prerequisites** anomaly paradox |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/4/SectionHeader/21` | 0.407106 | PERCEPTION EXPERTISE 11TH |

### Query 138
- Text: What are the requirements for **BORROW SPELL **[free-action] **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/44', 'PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/34', 'PZO22001 Starfinder Player Core 162-173::/page/9/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/44` | 0.906630 | **BORROW SPELL **[free-action] **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/34` | 0.573103 | **CONCEAL SPELL **[one-action] **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/2` | 0.559378 | **NONLETHAL SPELL **[one-action] **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/15` | 0.517025 | **REACH SPELL **[one-action] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/25` | 0.513664 | **WIDEN SPELL **[one-action] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/27` | 0.476672 | **OTHERWORLDLY SPELL **[one-action] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/38` | 0.474543 | **SPELLSURGE AMMO **[free-action] **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/532` | 0.458258 | Borrow Spell |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/14` | 0.416511 | one of the following feats. You must satisfy any prerequisites  before taking the feat. |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/46` | 0.416471 | **SPELLS** |

### Query 139
- Text: What are the requirements for **MULTIVERSE MAGIC** **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/50']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/50', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/558', 'PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/54']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/50` | 0.906048 | **MULTIVERSE MAGIC** **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/558` | 0.591150 | Multiverse Magic |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/54` | 0.496944 | **PERSISTENT QUANTUM FIELD **[two-actions] **FEAT 14** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/19` | 0.445519 | **INFINITE MAGIC** **FEAT 18** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/Table/3` | 0.422914 | FeatLevelAdvanced Warp8Anchoring Strike1Borrow Spell14Cantrip Expansion2Complete Transposition18Conceal Spell2Danger Zone8Debris Zone1Enlarge Quantum Field6Folded Paradoxes16Fundamental Understanding2 |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/559` | 0.422192 | 14 |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/43` | 0.413821 | 14TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/44` | 0.411752 | **BORROW SPELL **[free-action] **FEAT 14** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/1024` | 0.410192 | 14 |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/565` | 0.410192 | 14 |

### Query 140
- Text: What are the requirements for **PERSISTENT QUANTUM FIELD **[two-actions] **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/54']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/54', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/564', 'PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/45']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/54` | 0.927423 | **PERSISTENT QUANTUM FIELD **[two-actions] **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/564` | 0.660160 | Persistent Quantum Field |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/45` | 0.609555 | **ENLARGE QUANTUM FIELD **[one-action] **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/19` | 0.556405 | **Requirements** Your quantum field isn't active. |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/48` | 0.554054 | **Trigger** You use an action that Sustains your quantum field,  and the quantum field is still active. |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/29` | 0.553152 | **Requirements** Your quantum field is active. |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/11` | 0.553152 | **Requirements** Your quantum field is active. |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/19` | 0.553152 | **Requirements** Your quantum field is active. |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/SectionHeader/14` | 0.525660 | QUANTUM FIELD |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/8/Text/23` | 0.519148 | **Requirements** Your last action was to Sustain your quantum  field or had the anchoring trait. |

### Query 141
- Text: What are the requirements for **FOLDED PARADOXES** **FEAT 16**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/2', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/546', 'PZO22001 Starfinder Player Core 162-173::/page/5/SectionHeader/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/2` | 0.901188 | **FOLDED PARADOXES** **FEAT 16** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/546` | 0.569318 | Folded Paradoxes |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/5/SectionHeader/15` | 0.560101 | PARADOXES |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/8` | 0.504603 | **Paradox** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/SectionHeader/8` | 0.494100 | PARADOX |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/22` | 0.457656 | **Paradox Spells** cantrip: *injury echo*; 1st: *fleet step*; 2nd:  *temporal bullets*; 3rd: *time's edge*; 4th: *weight of ages*; 5th:  *chrono push*; 6th: *phantasmal calamity*; 7th: *true target*; |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/5` | 0.444555 | **Prerequisites** master in a paradox skill for a paradox other  than your chosen paradox |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/6/Text/10` | 0.436956 | **Paradox Spells** cantrip: *stumble*; 1st: *shifting* *surge*; 2nd:  *dispel magic*; 3rd: *void* *whispers*; 4th: *eldritch* *wrath*; 5th:  *wall of stone*; 6th: *slice reality*; 7th: *death sentence |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/9` | 0.431194 | **Prerequisites** precog paradox |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/547` | 0.428552 | 16 |

### Query 142
- Text: What are the requirements for **Prerequisites** master in a paradox skill for a paradox other  than your chosen paradox?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/11/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/11/Text/5', 'PZO22001 Starfinder Player Core 162-173::/page/8/Text/41', 'PZO22001 Starfinder Player Core 162-173::/page/9/Text/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/5` | 0.973808 | **Prerequisites** master in a paradox skill for a paradox other  than your chosen paradox |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/8/Text/41` | 0.771055 | **Prerequisites** analyst paradox |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/22` | 0.724379 | **Prerequisites** anomaly paradox |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/58` | 0.660597 | Trained in one skill determined by  your paradox |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/6` | 0.658645 | Your paradoxical nature has become multifaceted. During daily  preparations, you can replace one of your paradox spells with a  spell of another paradox that grants training in the prerequisite  parad |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/9` | 0.628653 | **Prerequisites** precog paradox |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/11` | 0.628236 | At 1st level, choose your paradox. Your chosen paradox  determines the tradition of your spells, additional trained  skills, additional spells you learn, and the effects of your  quantum field. You al |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/5/Text/16` | 0.613163 | Your paradox represents an event or force that forever altered  you. Your chosen paradox determines your spellcasting  tradition and grants you trained proficiency in the listed  paradox skill. You au |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/16` | 0.572140 | **Prerequisites** Gap influenced paradox |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/3/Text/15` | 0.550315 | You learn warp spells based on your paradox. |

### Query 143
- Text: What are the requirements for **ZONE OVERLAP **[one-action] **FEAT 16**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/7', 'PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/23', 'PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/7` | 0.915618 | **ZONE OVERLAP **[one-action] **FEAT 16** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/SectionHeader/23` | 0.600383 | **DEBRIS ZONE **[one-action] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/32` | 0.593969 | **RADIANT ZONE **[one-action] **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/604` | 0.549827 | Zone Overlap |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/63` | 0.547263 | **DANGER ZONE **[one-action] **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/22` | 0.507622 | **TWISTED DARK ZONE **[one-action] **FEAT 10** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/45` | 0.491094 | **ENLARGE QUANTUM FIELD **[one-action] **FEAT 6** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/8/SectionHeader/15` | 0.444959 | **REACH SPELL **[one-action] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/12` | 0.444808 | You cause a second zone to overlap your quantum field. You  can choose to apply another zone you're able to create, or  apply the existing zone again, improving its effects as follows:  Danger Zone de |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/2` | 0.439544 | **NONLETHAL SPELL **[one-action] **FEAT 2** |

### Query 144
- Text: What are the requirements for **COMPLETE TRANSPOSITION** **FEAT 18**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/14', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/536', 'PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/14` | 0.916669 | **COMPLETE TRANSPOSITION** **FEAT 18** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/536` | 0.634004 | Complete Transposition |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/19` | 0.528331 | **INFINITE MAGIC** **FEAT 18** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/537` | 0.432693 | 18 |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/428` | 0.420693 | 18 |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/1072` | 0.420693 | 18 |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/555` | 0.420693 | 18 |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/13` | 0.401604 | 18TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/14` | 0.400565 | one of the following feats. You must satisfy any prerequisites  before taking the feat. |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/1/Text/44` | 0.356632 | **FEATS** |

### Query 145
- Text: What are the requirements for **INFINITE MAGIC** **FEAT 18**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/19', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/554', 'PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/19` | 0.896073 | **INFINITE MAGIC** **FEAT 18** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/554` | 0.596621 | Infinite Magic |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/14` | 0.587615 | **COMPLETE TRANSPOSITION** **FEAT 18** |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/13` | 0.476642 | 18TH LEVEL |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/555` | 0.454845 | 18 |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/14` | 0.443529 | one of the following feats. You must satisfy any prerequisites  before taking the feat. |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/5/TableCell/1072` | 0.442845 | 18 |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/537` | 0.442845 | 18 |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/2/TableCell/428` | 0.442845 | 18 |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/50` | 0.427083 | **MULTIVERSE MAGIC** **FEAT 14** |

### Query 146
- Text: What are the requirements for **QUANTUM NEGATION** **FEAT 20**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/24', 'PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/28', 'PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/576']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/24` | 0.934630 | **QUANTUM NEGATION** **FEAT 20** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/28` | 0.765594 | **QUANTUM RESEARCH** **FEAT 20** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/576` | 0.555457 | Quantum Negation |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/2` | 0.504141 | **QUANTUM ENTANGLEMENT **[one-action] **FEAT 8** |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/31` | 0.485154 | **QUANTUM RECYCLE **[reaction] **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/31` | 0.457886 | **Prerequisites** quantum thesis |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/54` | 0.456677 | **QUANTUM AURA** **FEAT 6** |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/23` | 0.449422 | 20TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/577` | 0.438043 | 20 |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/5/SectionHeader/10` | 0.431379 | QUANTUM THESIS 19TH |

### Query 147
- Text: What are the requirements for **QUANTUM RESEARCH** **FEAT 20**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/28', 'PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/24', 'PZO22001 Starfinder Player Core 162-173::/page/11/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/28` | 0.914709 | **QUANTUM RESEARCH** **FEAT 20** |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/24` | 0.746375 | **QUANTUM NEGATION** **FEAT 20** |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/31` | 0.577806 | **Prerequisites** quantum thesis |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/580` | 0.518219 | Quantum Research |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/31` | 0.508855 | **QUANTUM RECYCLE **[reaction] **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/9/SectionHeader/54` | 0.491342 | **QUANTUM AURA** **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/5/SectionHeader/10` | 0.476206 | QUANTUM THESIS 19TH |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/10/SectionHeader/2` | 0.456509 | **QUANTUM ENTANGLEMENT **[one-action] **FEAT 8** |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/11/SectionHeader/23` | 0.443819 | 20TH LEVEL |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/19` | 0.432083 | **Prerequisites** quantum aura |

### Query 148
- Text: What are the requirements for **Prerequisites** quantum thesis?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 162-173::/page/11/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 162-173::/page/11/Text/31', 'PZO22001 Starfinder Player Core 162-173::/page/10/Text/19', 'PZO22001 Starfinder Player Core 162-173::/page/5/Footnote/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 162-173::/page/11/Text/31` | 0.973364 | **Prerequisites** quantum thesis |
| 2 | `PZO22001 Starfinder Player Core 162-173::/page/10/Text/19` | 0.677050 | **Prerequisites** quantum aura |
| 3 | `PZO22001 Starfinder Player Core 162-173::/page/5/Footnote/3` | 0.584695 | * The quantum thesis class feature gives you a 10th-rank spell slot that works a bit differently from other spell slots. |
| 4 | `PZO22001 Starfinder Player Core 162-173::/page/7/Text/19` | 0.537379 | **Requirements** Your quantum field is active. |
| 5 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/29` | 0.537379 | **Requirements** Your quantum field is active. |
| 6 | `PZO22001 Starfinder Player Core 162-173::/page/9/Text/11` | 0.537379 | **Requirements** Your quantum field is active. |
| 7 | `PZO22001 Starfinder Player Core 162-173::/page/2/Text/19` | 0.531647 | **Requirements** Your quantum field isn't active. |
| 8 | `PZO22001 Starfinder Player Core 162-173::/page/7/TableCell/580` | 0.509201 | Quantum Research |
| 9 | `PZO22001 Starfinder Player Core 162-173::/page/8/Text/41` | 0.481859 | **Prerequisites** analyst paradox |
| 10 | `PZO22001 Starfinder Player Core 162-173::/page/8/Text/23` | 0.469211 | **Requirements** Your last action was to Sustain your quantum  field or had the anchoring trait. |
