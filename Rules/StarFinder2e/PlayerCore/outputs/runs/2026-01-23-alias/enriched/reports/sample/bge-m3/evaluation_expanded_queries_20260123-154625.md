# RulesLawyer Evaluation Report: bge-m3

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `1994`
- Query count: `200`
- Evaluated queries: `200`
- Coverage: `1.0000`
- MRR: `0.7636`
- hit@1: `0.7150`
- hit@3: `0.7650`
- hit@5: `0.8200`
- hit@10: `0.8800`
- Embeddings reused: `False`

### Expanded Gold Metrics
- Coverage: `1.0000`
- MRR: `0.7636`
- hit@1: `0.7150`
- hit@3: `0.7650`
- hit@5: `0.8200`
- hit@10: `0.8800`

### Expanded Gold Expansion Stats
- Queries with additions: `200`
- Avg added per query: `1.99`
- Max added: `2`
- Addition reasons:
  - graph_depth_1: `398`

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
- Embedding: `106737`
- Evaluation: `92`

## Query Details
### Query 0
- Text: Summarize **Arcane**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6` | 0.814568 | **Arcane** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/491` | 0.673609 | Arcane |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/44` | 0.587429 | **CONCENTRATE** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.587429 | **CONCENTRATE** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/6` | 0.574704 | **Traditions** arcane, divine, occult, primal |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/1` | 0.571462 | **ALIEN CORE DRAGONS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.556128 | **SUBTLE SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/27` | 0.553141 | ARCANE 1ST-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` | 0.549764 | **CONCENTRATE** **MANIPULATE** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/79` | 0.548628 | **GAME** |

### Query 1
- Text: What is the rule about SPONTANEOUS SPELLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13` | 0.750037 | SPONTANEOUS SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/13` | 0.582768 | SUSTAINING SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5` | 0.554383 | SPELL SLOTS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.553411 | CHAPTER 7: SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.542703 | SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` | 0.536548 | FOCUS SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4` | 0.530001 | Heightened Spontaneous Spells |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.522274 | SPELL ATTACKS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.521491 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/16` | 0.521396 | READING SPELLS |

### Query 2
- Text: What does **CLEANSE CUISINE **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47` | 0.719090 | **CLEANSE CUISINE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** divine, primal  **Range **10 feet;** Area** 1 cubic foot  You transform all food and beverages in the area |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39` | 0.628648 | **CLEANSE AFFLICTION **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  Gentle restorative |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/64` | 0.583377 | **Cleanse** **Cuisine**H Make food and drink safe and delicious. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` | 0.571478 | **CLEAR MIND **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You drive menta |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/50` | 0.564299 | **Cleanse Cuisine**H Make food and drink safe and delicious. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/12` | 0.558701 | **GREASE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet;** Area** 4 contiguous 5-foot squares or** Targets** 1  object of 1 Bulk or less |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.549521 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/7` | 0.546497 | PREPARED SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/49` | 0.545690 | **DETECT POISON **[two-actions] **SPELL 1**  **UNCOMMON** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** divine, primal  **Range **30 feet;** Targets** 1 object or creature  You detect w |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.542978 | SPELLS |

### Query 3
- Text: What does **CAIRN FORM **[one-action] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62', 'PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70` | 0.650572 | **CAIRN FORM **[one-action] **SPELL 4**  **CONCENTRATE** **EARTH** **MANIPULATE** **MORPH**  **Traditions** arcane, primal  **Range **touch;** Targets** 1 creature  **Duration** 1 minute  Your target' |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/71` | 0.590599 | ARCANE 4TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/71` | 0.588038 | PRIMAL 4TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.585319 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/17` | 0.565628 | OCCULT 4TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/24` | 0.559051 | **Heightened (4th)** The spell's range is touch and it targets 1  willing creature. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/36` | 0.556772 | **AERIAL FORM **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Duration** 1 minute  You harness your mastery of the sky to reshape your body |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/40` | 0.552398 | DIVINE 4TH-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/36` | 0.551753 | **CELLULAR STIMULANT **[one-action] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **VITALITY**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 willing living creature that isn't  fatig |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.550550 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |

### Query 4
- Text: What does **AVATAR **[two-actions] **SPELL 10** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/40']
- Expected found: `True`
- Expected rank: `4`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/40', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/33', 'PZO22001 Starfinder Player Core 294-329::/page/22/ListItem/48']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/22/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/22/ListItem/48` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47` | 0.614634 | **REVIVAL **[two-actions] **SPELL 10**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet;** Targets** dead creatures and living creatures of  y |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/20` | 0.606907 | ARCANE 10TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/29` | 0.598125 | OCCULT 10TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/40` | 0.596873 | **AVATAR **[two-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** divine **Duration** 1 minute  You transform into an avatar of your deity, assuming a Huge  battle fo |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.590008 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.583783 | SPELL ATTACKS |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/34` | 0.576802 | **FREEZE TIME **[three-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  You temporarily stop time for everything but yourself,  allowing you to use several actions |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/33` | 0.573221 | DIVINE 10TH-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` | 0.571457 | **CONTROL MACHINE **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature or hazard with t |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/32/SectionHeader/56` | 0.569689 | **SPIRITUAL ARMAMENT **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SANCTIFIED** **SPIRIT**  **Traditions** divine, occult  **Range **120 feet; **Targets** 1 creature  **Defense** AC; * |

### Query 5
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/32']
- Expected found: `True`
- Expected rank: `29`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/31', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/33']
- Expanded expected found: `True`
- Expanded expected rank: `29`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/33` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/64` | 0.816254 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/63` | 0.816254 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/60` | 0.816254 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/22` | 0.816254 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/41` | 0.816254 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/56` | 0.816254 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/61` | 0.816254 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/68` | 0.816254 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/82` | 0.816254 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/64` | 0.816254 | **CLASSES** |

### Query 6
- Text: What is the rule about If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/22', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.946064 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.750492 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.738923 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` | 0.698364 | Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.670847 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.657842 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` | 0.645520 | With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own met |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/4` | 0.637739 | Spellcasting creates obvious sensory manifestations, such  as bright lights, crackling sounds, and sharp smells from the  gathering magic. Nearly all spells manifest a spell signature—a  colorful, glo |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.637581 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/23` | 0.630793 | It's possible, especially through archetypes, to gain focus  spells from more than one source. If this happens, you  have just one focus pool, counting all your focus spells to  determine the points i |

### Query 7
- Text: What does **Traditions** divine, occult, primal do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/34']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/34', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/74', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/35']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/7/Text/74` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/7/Text/35` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/34` | 0.827153 | **Traditions** divine, occult, primal |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/45` | 0.785370 | **Traditions** divine, primal |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/6` | 0.766625 | **Traditions** arcane, divine, occult, primal |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/24` | 0.653475 | **Traditions** occult |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.617653 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1` | 0.605348 | **MAGICAL TRADITIONS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/14` | 0.585084 | The practitioners of occult traditions seek  to understand the unexplainable, categorize  the bizarre, and otherwise access the ephemeral in a |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/13/SectionHeader/43` | 0.569666 | **MANIFESTATION **[three-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  You spin secrets from the fundaments of magic, shaping them  into a power |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/10` | 0.560027 | The power of the divine is steeped in faith,  the unseen, and belief in a power source from |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/499` | 0.546501 | Divine |

### Query 8
- Text: What is the rule about Focus spells are automatically heightened to half your level  rounded up, just like cantrips are. You can't cast a focus spell  if its minimum rank is greater than half your level rounded  up, even if you somehow gain access to it.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/15', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` | 0.925382 | Focus spells are automatically heightened to half your level  rounded up, just like cantrips are. You can't cast a focus spell  if its minimum rank is greater than half your level rounded  up, even if |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 0.740449 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.645367 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` | 0.643763 | Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` | 0.632486 | Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your p |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/17` | 0.628393 | Each spell uses the following format. Entries appear only  when applicable, so not all spells will have every entry  described here. The spell's name line also lists the type  of spell if it's a cantr |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.621385 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.609624 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.605269 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.604955 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |

### Query 9
- Text: What does **FLICKER **[two-actions] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/62']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/62', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/56', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/69']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/2/Text/56` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/2/Text/69` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/62` | 0.654284 | **FLICKER **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **TELEPORTATION**  **Traditions** arcane, occult  **Duration** 1 minute  You flicker quickly between your current plane and anothe |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/17` | 0.582741 | OCCULT 4TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/71` | 0.581480 | PRIMAL 4TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/71` | 0.580924 | ARCANE 4TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.577361 | SPELL ATTACKS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.575364 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/40` | 0.564749 | DIVINE 4TH-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/22/SectionHeader/8` | 0.563099 | **PLANAR TETHER **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** varies  You |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` | 0.561106 | FOCUS SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.556762 | **SPELL NAME **[one-action] **SPELL (RANK)** |

### Query 10
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/18', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/18` | 0.863367 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/55` | 0.863367 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/28` | 0.863367 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/28` | 0.863367 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/61` | 0.863367 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/62` | 0.863367 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/57` | 0.863367 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/55` | 0.863367 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/39` | 0.863367 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/20` | 0.863367 | **INTRODUCTION** |

### Query 11
- Text: What is the rule about Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell by preparing it in a higher-rank slot than  its normal spell rank, while a spontaneous spellcaster can  heighten a spell by casting it using a higher-rank spell slot,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/16', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.939088 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.788928 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.744402 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` | 0.729440 | As a spontaneous caster, you can also choose to cast  a lower-rank spell using a higher-rank spell slot without  heightening it or knowing it at a higher rank. This casts the  spell at the rank you kn |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.706130 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` | 0.691912 | In addition, many spells have additional specific benefits  when they are heightened, such as increased damage. These  extra benefits are described at the end of the spell's stat  block. Some heighten |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.680784 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.679049 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 0.653110 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.650312 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |

### Query 12
- Text: Summarize **REFOCUS**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/16', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/17` | 0.847040 | **REFOCUS** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/44` | 0.688347 | **CONCENTRATE** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.688347 | **CONCENTRATE** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/68` | 0.646410 | **Focus Spells** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/46` | 0.646410 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/67` | 0.646410 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/63` | 0.646410 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/89` | 0.646410 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/39` | 0.646410 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/77` | 0.646410 | **Focus Spells** |

### Query 13
- Text: What does **ARCTIC RIFT **[two-actions] **SPELL 8** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/18', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/22/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/22/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/11` | 0.637336 | **ARCTIC RIFT **[two-actions] **SPELL 8**  **COLD** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Area** 120-foot line  **Defense** Fortitude  A jagged crack opens in the air, deali |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/17` | 0.620987 | OCCULT 8TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/2` | 0.616849 | ARCANE 8TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/47` | 0.578921 | **EARTHQUAKE **[two-actions] **SPELL 8**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Area** 60-foot burst  **Duration** 1 round  You shake the groun |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/48` | 0.569243 | PRIMAL 8TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/21` | 0.565750 | DIVINE 8TH-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/51` | 0.558113 | **PHANTASMAL FLEET **[two-actions] **SPELL 8**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **500 feet; **Area** 60-foot burst  **Defense** Will  A m |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.554059 | SPELL ATTACKS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/18` | 0.529546 | **DIVINE INSPIRATION **[two-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine  **Range **touch;** Targets** 1 willing creature  You infuse a target with spiritual |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/36` | 0.527966 | **EARTHBIND **[two-actions] **SPELL 3**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 flying creature  **Defense** Fortitude; **Duration** |

### Query 14
- Text: What does **BLAZING BOLT **[one-action]** TO **[three-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20` | 0.692657 | **BLAZING BOLT **[one-action]** TO **[three-actions] **SPELL 2**  **ATTACK** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets** 1 or more creatures |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/20` | 0.609580 | **Blazing Bolt**H Fire one to three flaming bolts at different foes. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/6` | 0.609580 | **Blazing Bolt**H Fire one to three flaming bolts at different foes. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.590975 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.575382 | SPELL ATTACKS |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` | 0.575001 | **HYPNOTIZE **[two-actions] **SPELL 3**  **ILLUSION** **MANIPULATE** **SUBTLE** **VISUAL**  **Traditions** arcane, occult  **Range **120 feet; **Area** 10-foot burst  **Defense** Will;** Duration** su |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.574164 | **LIFE SEAL **[reaction] **SPELL 3** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/23` | 0.571465 | **ATOMIC BLAST **[three-actions] **SPELL 9**  **CONCENTRATE** **FIRE** **MANIPULATE** **RADIATION**  **Traditions** arcane, primal  **Range **500 feet;** Area** 100-foot burst **Defense** Reflex; **Du |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/42` | 0.570802 | **HOWLING BLIZZARD **[two-actions]** TO **[three-actions] **SPELL 5**  **AIR** **COLD** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Area** varies  **Defense** basic Reflex  Freezi |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/48` | 0.560524 | **FIREBALL **[two-actions] **SPELL 3**  **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Area** 20-foot burst  **Defense** basic Reflex  A roaring blast of |

### Query 15
- Text: What is the rule about **Failure** The creature takes full damage.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/9', 'PZO22001 Starfinder Player Core 330-363::/page/5/Text/10', 'PZO22001 Starfinder Player Core 330-363::/page/5/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/5/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/5/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/9` | 0.785151 | **Failure** The creature takes full damage. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/34/Text/15` | 0.785151 | **Failure** The creature takes full damage. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/32/Text/16` | 0.737348 | **Failure** The creature takes full damage and persistent damage. **Critical Failure** The creature takes double damage and double  persistent damage. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/52` | 0.736943 | **Failure** The creature takes full damage and is pushed 5 feet  away from you. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/34/Text/35` | 0.733827 | **Failure** The creature takes full damage and is sickened 1. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/32/Text/41` | 0.733827 | **Failure** The creature takes full damage and is sickened 1. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/24/Text/10` | 0.722863 | **Failure** The creature takes full damage and is deafened for  1 round. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/21` | 0.722863 | **Failure** The creature takes full damage and is deafened for  1 round. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/20` | 0.719034 | **Failure** The creature takes full damage and is slowed 1 until  the start of your next turn. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/13` | 0.719034 | **Failure** The creature takes full damage and is slowed 1 until the  start of your next turn. |

### Query 16
- Text: What is the rule about If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with more freedom in your spellcasting, but you  have fewer spells in your spell repertoire, as determined by  your character level and class. When you make your daily  preparations, all your spell slots are refreshed, but you don't  get to change the spells in your repertoire.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.951622 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.744969 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.701307 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.694811 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` | 0.693433 | As a spontaneous caster, you can also choose to cast  a lower-rank spell using a higher-rank spell slot without  heightening it or knowing it at a higher rank. This casts the  spell at the rank you kn |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/Text/16` | 0.688610 | If a spell's duration says it lasts until your next daily  preparations, on the next day you can refrain from preparing  a new spell in that spell's slot. (If you are a spontaneous caster,  you can in |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.680910 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.671871 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.670651 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.665082 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |

### Query 17
- Text: What does **ACID GRIP **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/16', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/19/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/19/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/16` | 0.640187 | **ACID GRIP **[two-actions] **SPELL 2**  **ACID** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 creature  **Defense** Reflex  An ephemeral, taloned h |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/4` | 0.577322 | ARCANE 2ND-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/25` | 0.566441 | OCCULT 2ND-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19` | 0.538143 | **CAUSTIC BLAST **[two-actions] **CANTRIP 1**  **ACID** **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Area** 5-foot burst  **Defense** basic Reflex  Y |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/17` | 0.535332 | PRIMAL 2ND-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/71` | 0.530755 | DIVINE 2ND-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/27` | 0.529821 | **CAUSTIC CONVERSION **[two-actions] **SPELL 2**  **ACID** **ATTACK** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 creature  **Defense** AC  You lau |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/12` | 0.524698 | **GREASE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet;** Area** 4 contiguous 5-foot squares or** Targets** 1  object of 1 Bulk or less |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/5` | 0.521267 | **Acid Grip**H Move and harm foes with a hand of acid. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/18` | 0.521267 | **Acid Grip**H Move and harm foes with a hand of acid. |

### Query 18
- Text: What is the rule about **Heightened (5th)** You can take on the appearance of a Large  humanoid. If this increases your size, you gain the effects  of the *enlarge* spell.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/8/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/8/Text/4', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/5', 'PZO22001 Starfinder Player Core 330-363::/page/8/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/8/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/4` | 0.863400 | **Heightened (5th)** You can take on the appearance of a Large  humanoid. If this increases your size, you gain the effects  of the *enlarge* spell. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/31` | 0.674320 | **Heightened (5th)** Your battle form is Huge, and your attacks  have 15-foot reach. You instead gain 20 temporary HP,  attack modifier +18, damage bonus +2 and double damage  dice (including persiste |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/3` | 0.668685 | **Heightened (5th)** Your battle form is Huge and your attacks  have 15-foot reach. You instead gain 20 temporary HP, AC  = 18 + your level, attack modifier +18, damage bonus +7  and double the number |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/20/Text/2` | 0.661981 | **Heightened (5th)** Your battle form is Large and your fly  Speed gains a +10-foot status bonus. You instead gain 10  temporary HP, attack modifier +18, damage bonus +8, and  Acrobatics +20. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/4` | 0.661393 | **ENLARGE **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Range **30 feet;** Targets** 1 willing creature  **Duration** 5 minutes  Bolstered |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/22/Text/29` | 0.637776 | **Heightened (6th)** Your battle form is Huge, and the reach of  your attacks increases by 5 feet. You instead gain AC = 22  + your level, 24 temporary HP, attack modifier +21, damage  bonus +16, and |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/30` | 0.635138 | **Heightened (4th)** Your battle form is Large, and your attacks  have 10-foot reach. You instead gain 15 temporary HP,  attack modifier +16, damage bonus +6, and Athletics +16. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/1` | 0.634566 | traits while in this form, as well as any trait related to  the creature's kind (such as goblin or human). If this  transformation reduces your size, it reduces your reach  accordingly (typically to 5 |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/12` | 0.628135 | **Heightened (6th)** Your battle form is Large and your attacks  have 10-foot reach. You instead gain AC = 22 + your level,  15 temporary HP, an attack modifier of +23, a damage  bonus of +13, and Acr |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/2` | 0.622542 | **Heightened (4th)** Your battle form is Large and your attacks  have 10-foot reach. You instead gain 15 temporary HP, AC  = 18 + your level, attack modifier +16, damage bonus +9,  and Athletics +16. |

### Query 19
- Text: What does **FIREBALL **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/48']
- Expected found: `True`
- Expected rank: `2`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/48', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/56', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/41']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/2/Text/56` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/2/Text/41` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.677452 | **LIFE SEAL **[reaction] **SPELL 3** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/48` | 0.652645 | **FIREBALL **[two-actions] **SPELL 3**  **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Area** 20-foot burst  **Defense** basic Reflex  A roaring blast of |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.626881 | SPELL ATTACKS |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.625152 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/36` | 0.598935 | **EARTHBIND **[two-actions] **SPELL 3**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 flying creature  **Defense** Fortitude; **Duration** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20` | 0.594742 | **BLAZING BOLT **[one-action]** TO **[three-actions] **SPELL 2**  **ATTACK** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets** 1 or more creatures |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/30/SectionHeader/22` | 0.593881 | **SKYFIRE WINGS **[two-actions] **SPELL 3**  **CONCENTRATE** **ELECTRICITY** **FIRE** **MANIPULATE** **MORPH**  **Traditions** arcane, divine, occult, primal  **Duration** 1 minute  Wings of plasma gr |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/20` | 0.593517 | **ENTHRALL **[two-actions] **SPELL 3**  **AUDITORY** **CONCENTRATE** **EMOTION** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet;** Targets** all creatures in range  **Defense** Will |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` | 0.591355 | **HYPNOTIZE **[two-actions] **SPELL 3**  **ILLUSION** **MANIPULATE** **SUBTLE** **VISUAL**  **Traditions** arcane, occult  **Range **120 feet; **Area** 10-foot burst  **Defense** Will;** Duration** su |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/21` | 0.588495 | **HOLY LIGHT **[two-actions] **SPELL 3**  **ATTACK** **CONCENTRATE** **FIRE** **HOLY** **LIGHT** **MANIPULATE**  **Traditions** divine, primal  **Range **120 feet;** Targets** 1 creature  **Defense** |

### Query 20
- Text: What does **ATOMIC BLAST **[three-actions] **SPELL 9** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/33', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/22/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/22/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/23` | 0.700915 | **ATOMIC BLAST **[three-actions] **SPELL 9**  **CONCENTRATE** **FIRE** **MANIPULATE** **RADIATION**  **Traditions** arcane, primal  **Range **500 feet;** Area** 100-foot burst **Defense** Reflex; **Du |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/24` | 0.605848 | OCCULT 9TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/11` | 0.593575 | ARCANE 9TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/56` | 0.567695 | PRIMAL 9TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.563933 | SPELL ATTACKS |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.562855 | **LIFE SEAL **[reaction] **SPELL 3** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/44` | 0.555309 | **FALLING STARS **[two-actions] **SPELL 9**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Area** four 40-foot bursts  **Defense** basic Reflex  You reach into t |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/42` | 0.548092 | ARCANE 3RD-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/10/SectionHeader/25` | 0.545951 | **IMPLOSION **[two-actions] **SPELL 9**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet;** Targets** 1 corporeal creature  **Defense** basic Fortitude; **Duration** s |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20` | 0.542577 | **BLAZING BOLT **[one-action]** TO **[three-actions] **SPELL 2**  **ATTACK** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets** 1 or more creatures |

### Query 21
- Text: What does **FORESIGHT **[two-actions] **SPELL 9** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/26']
- Expected found: `True`
- Expected rank: `4`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/26', 'PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/34', 'PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/19']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/24` | 0.612464 | OCCULT 9TH-RANK SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/56` | 0.599221 | PRIMAL 9TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.597169 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/26` | 0.596574 | **FORESIGHT **[two-actions] **SPELL 9**  **CONCENTRATE** **MANIPULATE** **MENTAL** **PREDICTION**  **Traditions** arcane, divine, occult **Range **touch;** Targets** 1 creature  **Duration** 1 hour  Y |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/32` | 0.574723 | **PHANTASMAGORIA **[two-actions] **SPELL 9**  **CONCENTRATE** **DEATH** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **120 feet; **Targets** any number of creatures |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/4` | 0.566749 | **HONEYED WORDS **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes  You unlock the |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/11` | 0.563392 | ARCANE 9TH-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.562957 | SPELL ATTACKS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` | 0.562917 | FOCUS SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.556214 | CHAPTER 7: SPELLS |

### Query 22
- Text: What does **COMMAND **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/28/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/28/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/28/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/28/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/2` | 0.661935 | **COMMAND **[two-actions] **SPELL 1**  **AUDITORY** **CONCENTRATE** **LINGUISTIC** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult **Range **30 feet;** Targets** 1 creature  **Defense |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.630614 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.617414 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.610228 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/39` | 0.609165 | **SUBCONSCIOUS SUGGESTION **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **LINGUISTIC** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet;** Targe |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/29` | 0.605110 | **STUPEFY **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** varies  You du |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` | 0.603674 | **CONTROL MACHINE **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature or hazard with t |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.602558 | SPELL ATTACKS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/49` | 0.602333 | **DETECT POISON **[two-actions] **SPELL 1**  **UNCOMMON** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** divine, primal  **Range **30 feet;** Targets** 1 object or creature  You detect w |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/11` | 0.601756 | **STATUS **[two-actions] **SPELL 2**  **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch;** Targets** 1 willing living creature  **Duration** until yo |

### Query 23
- Text: What is the rule about With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own method of learning, preparing,  and casting spells, and every individual spell produces a  specific effect, so learning new spells gives a spellcaster  an increasing array of options to accomplish their goals.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` | 0.915533 | With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own met |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.711513 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/4` | 0.693722 | Spellcasting creates obvious sensory manifestations, such  as bright lights, crackling sounds, and sharp smells from the  gathering magic. Nearly all spells manifest a spell signature—a  colorful, glo |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/3` | 0.688987 | The casting of a spell can range from a simple word of magical  might that creates a fleeting effect to a complex process  taking hours to cast and producing a long-term impact.  Casting a spell requi |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` | 0.686973 | Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.660930 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.660351 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.652219 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.651381 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.651267 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |

### Query 24
- Text: Summarize AREAS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/18', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/18` | 0.736930 | AREAS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22` | 0.583377 | FOCUS POINTS FROM MULTIPLE  SOURCES |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14` | 0.568725 | RANGES, AREAS, AND  TARGETS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.564139 | insight about a topic. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/6` | 0.554759 | COUNTERACTING |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.544468 | **Summoned** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/44` | 0.535225 | **CONCENTRATE** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.535225 | **CONCENTRATE** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/48` | 0.533603 | **Bane** Weaken enemies' attacks in an aura around you. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/61` | 0.533603 | **Bane** Weaken enemies' attacks in an aura around you. |

### Query 25
- Text: What is the rule about traits while in this form, as well as any trait related to  the creature's kind (such as goblin or human). If this  transformation reduces your size, it reduces your reach  accordingly (typically to 5 feet). This transformation doesn't  change your statistics in any way, and you don't gain any  special abilities of the humanoid form you assume. You  can still wear and use your gear, which changes size (if  necessary) to match your new form. If items leave your  person, they return to their usual size.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/8/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/8/Text/1', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/69', 'PZO22001 Starfinder Player Core 330-363::/page/8/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/7/Text/69` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/8/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/1` | 0.954740 | traits while in this form, as well as any trait related to  the creature's kind (such as goblin or human). If this  transformation reduces your size, it reduces your reach  accordingly (typically to 5 |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/15` | 0.650368 | If you take on a battle form with a polymorph spell, the  special statistics can be adjusted only by circumstance  bonuses, status bonuses, and penalties. Unless otherwise  noted, the battle form prev |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/50` | 0.638155 | **HUMANOID FORM **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, occult, primal  **Duration** 10 minutes  You transform your appearance to that of a Sm |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/20/Text/13` | 0.636647 | You transform into the battle form of a Tiny animal, such as  a cat, insect, lizard, or rat. You can decide the specific type of  animal (such as a squox or praying mantis), but this has no  effect on |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/12` | 0.632193 | Spells that slightly alter a creature's form have the morph trait.  Any Strikes specifically granted by a magical morph effect also  gain the magical trait. You can be affected by multiple morph  spel |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/4` | 0.623939 | **Heightened (5th)** You can take on the appearance of a Large  humanoid. If this increases your size, you gain the effects  of the *enlarge* spell. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/30` | 0.622213 | **Heightened (4th)** Your battle form is Large, and your attacks  have 10-foot reach. You instead gain 15 temporary HP,  attack modifier +16, damage bonus +6, and Athletics +16. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/24` | 0.620219 | **Success** The creature takes half damage and no persistent  damage, and the claw moves it up to 5 feet in a direction  of your choice. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/31` | 0.617288 | **Heightened (5th)** Your battle form is Huge, and your attacks  have 15-foot reach. You instead gain 20 temporary HP,  attack modifier +18, damage bonus +2 and double damage  dice (including persiste |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/22/Text/29` | 0.613296 | **Heightened (6th)** Your battle form is Huge, and the reach of  your attacks increases by 5 feet. You instead gain AC = 22  + your level, 24 temporary HP, attack modifier +21, damage  bonus +16, and |

### Query 26
- Text: What does **ENTANGLING FLORA **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/13', 'PZO22001 Starfinder Player Core 330-363::/page/0/Text/20', 'PZO22001 Starfinder Player Core 330-363::/page/0/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/0/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/0/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/13` | 0.682807 | **ENTANGLING FLORA **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **PLANT** **WOOD**  **Traditions** arcane, primal  **Range **120 feet; **Area** all squares in a 20-foot burst  **Duratio |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/37` | 0.581403 | **REVEALING LIGHT **[two-actions] **SPELL 2**  **CONCENTRATE** **LIGHT** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **120 feet;** Area** 10-foot burst  **Defense** Reflex; * |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/30` | 0.578144 | **Entangling Flora** Sprout plants to hinder movement in an area. **Environmental Endurance**H Protect a creature from severe |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.576462 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.573476 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/32/Text/2` | 0.572140 | **SOUND BODY **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You send a su |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` | 0.567500 | **CLEAR MIND **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You drive menta |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/17` | 0.566370 | **Entangling Flora** Sprout plants to hinder movement in an area. **Environmental Endurance**H Protect a creature from severe  cold or heat. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20` | 0.564808 | **BLAZING BOLT **[one-action]** TO **[three-actions] **SPELL 2**  **ATTACK** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets** 1 or more creatures |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39` | 0.564293 | **CLEANSE AFFLICTION **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  Gentle restorative |

### Query 27
- Text: What does **HOWL **[two-actions] **SPELL 7** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/32']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/32', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/74', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/7/Text/74` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/7/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.732443 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.654193 | CHAPTER 7: SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/5` | 0.596061 | OCCULT 7TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.568249 | SPELL ATTACKS |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/22/SectionHeader/3` | 0.566995 | **PLANAR SEAL **[two-actions] **SPELL 7**  **UNCOMMON** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult **Range **120 feet; **Area** 60-foot burst **Duration** until your next da |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/34` | 0.565885 | PRIMAL 7TH-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` | 0.565151 | **HYPNOTIZE **[two-actions] **SPELL 3**  **ILLUSION** **MANIPULATE** **SUBTLE** **VISUAL**  **Traditions** arcane, occult  **Range **120 feet; **Area** 10-foot burst  **Defense** Will;** Duration** su |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/22/SectionHeader/37` | 0.554558 | **POSSESSION **[two-actions] **SPELL 7**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL** **POSSESSION**  **Traditions** occult  **Range **30 feet; **Targets** 1 living creat |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/12` | 0.554402 | **EXECUTE **[two-actions] **SPELL 7**  **CONCENTRATE** **DEATH** **MANIPULATE** **VOID**  **Traditions** divine, primal  **Range **30 feet; **Targets** 1 creature  **Defense** basic Fortitude  You poi |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/4` | 0.552540 | **ANT HAUL **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal **Range **touch; **Targets** 1 creature  **Duration** 8 hours  You reinforce the target's musculos |

### Query 28
- Text: Summarize RANGES, AREAS, AND  TARGETS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/15', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14` | 0.875952 | RANGES, AREAS, AND  TARGETS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20` | 0.652411 | TARGETS |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/7` | 0.615081 | **Range **touch;** Targets** 1 creature |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/16` | 0.598479 | TOUCH RANGE |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22` | 0.597441 | FOCUS POINTS FROM MULTIPLE  SOURCES |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/23` | 0.596180 | **Range, Area, and Targets** This entry lists the range of the  spell, the area it affects, and the targets it can affect, if  any. If none of these entries are present, the spell affects  only the ca |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41` | 0.581768 | **ANALYZE TARGET **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **30 feet; **Targets** 1 creature  **Dur |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.575321 | insight about a topic. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/38` | 0.561813 | **Analyze** **Target**H Gather data about a target's basic physiology. **Caustic Blast**H Fling a glob of acid that splashes a small area. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/8` | 0.561813 | **Analyze** **Target**H Gather data about a target's basic physiology. **Caustic Blast**H Fling a glob of acid that splashes a small area. |

### Query 29
- Text: What does **ANT HAUL **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/22/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/22/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/4` | 0.709731 | **ANT HAUL **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal **Range **touch; **Targets** 1 creature  **Duration** 8 hours  You reinforce the target's musculos |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.609976 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/30` | 0.600846 | **Ant Haul** Target can carry more. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/60` | 0.600846 | **Ant Haul** Target can carry more. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.596210 | SPELL ATTACKS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52` | 0.573711 | **CHARM **[two-actions] **SPELL 1**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 creatur |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` | 0.570998 | **HYPNOTIZE **[two-actions] **SPELL 3**  **ILLUSION** **MANIPULATE** **SUBTLE** **VISUAL**  **Traditions** arcane, occult  **Range **120 feet; **Area** 10-foot burst  **Defense** Will;** Duration** su |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.568589 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/31/SectionHeader/22` | 0.564257 | **SOOTHE **[two-actions] **SPELL 1**  **CONCENTRATE** **EMOTION** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** occult  **Range **30 feet;** Targets** 1 willing creature  **Duration** 1 minute |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.559286 | **SPELL NAME **[one-action] **SPELL (RANK)** |

### Query 30
- Text: Summarize Cone of piercing
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/505']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/505', 'PZO22001 Starfinder Player Core 330-363::/page/0/Text/4', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/504']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/0/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/504` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/505` | 0.728333 | Cone of piercing (Reflex) |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/493` | 0.544195 | Cone of poison (Fortitude) |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/21/ListItem/19` | 0.518887 | **Bull** Speed 30 feet; **Melee **[one-action] horn, **Damage **2d8 piercing. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/11/ListItem/28` | 0.518664 | piercing plus 1d4 persistent poison; **Melee **[one-action] pincer  (agile), **Damage **1d6 bludgeoning. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/497` | 0.512066 | Cone of mental (Will) |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/21/ListItem/20` | 0.489672 | **Canine** Speed 40 feet; **Melee **[one-action] jaws, **Damage **2d8  piercing. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.486241 | insight about a topic. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/51` | 0.484145 | **Shadow Blast**H Shape a damaging cone of shadow substance  to deal damage of a type you choose. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/60` | 0.484145 | **Shadow Blast**H Shape a damaging cone of shadow substance  to deal damage of a type you choose. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/9` | 0.483732 | **Pummeling Rubble**H Hurl a cone of rocks to batter creatures. |

### Query 31
- Text: What is the rule about You rapidly catalog and collate information relevant to  your current situation. You can instantly use up to 6 Recall  Knowledge actions as part of Casting this Spell. For these?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/8/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/8/Text/25', 'PZO22001 Starfinder Player Core 330-363::/page/8/Text/24', 'PZO22001 Starfinder Player Core 330-363::/page/8/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/8/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/8/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/25` | 0.935222 | You rapidly catalog and collate information relevant to  your current situation. You can instantly use up to 6 Recall  Knowledge actions as part of Casting this Spell. For these |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/5` | 0.654807 | If you want to identify a spell but don't have it prepared  or in your repertoire, you must spend an action on your  turn attempting to identify it using Recall Knowledge. You  typically notice a spel |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.633775 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.619814 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21` | 0.588143 | **CONTINGENCY** **SPELL 7**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane  **Cast** 10 minutes **Duration** until your next daily preparations  You prepare a spell that will trigger later. Wh |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 0.579220 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.578701 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.577811 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/2` | 0.571732 | **Hypercognition** Recall massive amounts of information in an  instant. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/3` | 0.570999 | The casting of a spell can range from a simple word of magical  might that creates a fleeting effect to a complex process  taking hours to cast and producing a long-term impact.  Casting a spell requi |

### Query 32
- Text: What is the rule about **Spell Lists**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/63']
- Expected found: `True`
- Expected rank: `23`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/63', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/62', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/64']
- Expanded expected found: `True`
- Expanded expected rank: `23`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/7/Text/64` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/87` | 0.732608 | **Spell Lists** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/25` | 0.732608 | **Spell Lists** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/60` | 0.732608 | **Spell Lists** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/69` | 0.732608 | **Spell Lists** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/44` | 0.732608 | **Spell Lists** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/69` | 0.732608 | **Spell Lists** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/75` | 0.732608 | **Spell Lists** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/62` | 0.732608 | **Spell Lists** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/84` | 0.732608 | **Spell Lists** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/61` | 0.732608 | **Spell Lists** |

### Query 33
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/64']
- Expected found: `True`
- Expected rank: `8`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/64', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/63', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/65']
- Expanded expected found: `True`
- Expanded expected rank: `8`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/63` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/65` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/65` | 0.727771 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/57` | 0.727771 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/58` | 0.727771 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/65` | 0.727771 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/58` | 0.727771 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/60` | 0.727771 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/62` | 0.727771 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/64` | 0.727771 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/33` | 0.727771 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/58` | 0.727771 | **SKILLS** |

### Query 34
- Text: Summarize **Requirements** You have a focus pool.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/20', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/19` | 0.966705 | **Requirements** You have a focus pool. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` | 0.686685 | FOCUS SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/16` | 0.679593 | You replenish all the Focus Points in your pool during your  daily preparations. You can also use the Refocus activity to  pray, study, meditate, or otherwise reattune yourself to the  source of your |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` | 0.676769 | Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your p |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` | 0.670136 | **CONCENTRATE** **MANIPULATE** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.662878 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/47` | 0.657121 | **Spells** **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/67` | 0.651013 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/89` | 0.651013 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/46` | 0.651013 | **Focus Spells** |

### Query 35
- Text: What is the rule about **Failure** The creature takes full damage, is slowed 3 until the  end of its next turn, and slowed 1 for 1 minute.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/4', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/3', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/4` | 0.848758 | **Failure** The creature takes full damage, is slowed 3 until the  end of its next turn, and slowed 1 for 1 minute. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/13` | 0.809216 | **Failure** The creature takes full damage and is slowed 1 until the  start of your next turn. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/20` | 0.809216 | **Failure** The creature takes full damage and is slowed 1 until  the start of your next turn. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/5` | 0.772819 | **Critical Failure** The creature takes double damage, is slowed  3 until the end of its next turn, and slowed 2 for 1 minute. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/3` | 0.745243 | **Success** The creature takes half damage and is slowed 1 until  the end of its next turn. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/32` | 0.734575 | **Failure** The creature takes full damage and is clumsy 1 for 1  minute. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/24/Text/10` | 0.722023 | **Failure** The creature takes full damage and is deafened for  1 round. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/21` | 0.722023 | **Failure** The creature takes full damage and is deafened for  1 round. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/32/Text/42` | 0.709901 | **Critical Failure** The creature takes full damage and is sickened  2; while it's sickened, it's also slowed 1. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/33` | 0.694359 | **Critical Failure** The creature takes full damage and is clumsy  2 for 1 minute. |

### Query 36
- Text: What does **ENTROPY STRIKE **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/32']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/32', 'PZO22001 Starfinder Player Core 330-363::/page/0/Text/20', 'PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/39']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/0/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/39` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/32` | 0.645545 | **ENTROPY STRIKE **[two-actions] **SPELL 3**  **ACID** **ATTACK** **CONCENTRATE** **MANIPULATE** **VOID**  **Traditions** arcane, divine, occult  **Range **30 feet; **Targets** 1 creature or unattende |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/20` | 0.597610 | **ENTHRALL **[two-actions] **SPELL 3**  **AUDITORY** **CONCENTRATE** **EMOTION** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet;** Targets** all creatures in range  **Defense** Will |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.577073 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.567132 | **LIFE SEAL **[reaction] **SPELL 3** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.564999 | SPELL ATTACKS |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` | 0.558508 | **HYPNOTIZE **[two-actions] **SPELL 3**  **ILLUSION** **MANIPULATE** **SUBTLE** **VISUAL**  **Traditions** arcane, occult  **Range **120 feet; **Area** 10-foot burst  **Defense** Will;** Duration** su |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/36` | 0.551706 | **EARTHBIND **[two-actions] **SPELL 3**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 flying creature  **Defense** Fortitude; **Duration** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/35/SectionHeader/32` | 0.551227 | **ENFEEBLE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Range **30 feet;** Targets** 1 creature  **Defense** Fortitude; **Duration** varies  Yo |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36` | 0.550309 | **BLINDNESS **[two-actions] **SPELL 3**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet;** Targets** 1 creature  **Defense** Fortit |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/23` | 0.550017 | **SHARE PAIN **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **30 feet;** Targets** 1 creature  **Defense** Will  You telepathically shar |

### Query 37
- Text: What does **CHILLING DARKNESS **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6` | 0.680003 | **CHILLING DARKNESS **[two-actions] **SPELL 3**  **ATTACK** **COLD** **CONCENTRATE** **DARKNESS** **MANIPULATE** **UNHOLY**  **Traditions** divine  **Range **120 feet;** Targets** 1 creature  **Defens |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.617053 | **LIFE SEAL **[reaction] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.616408 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/21` | 0.589320 | **HOLY LIGHT **[two-actions] **SPELL 3**  **ATTACK** **CONCENTRATE** **FIRE** **HOLY** **LIGHT** **MANIPULATE**  **Traditions** divine, primal  **Range **120 feet;** Targets** 1 creature  **Defense** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/23` | 0.579523 | **SHARE PAIN **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **30 feet;** Targets** 1 creature  **Defense** Will  You telepathically shar |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/51` | 0.579152 | **DARKVISION **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Duration** 1 hour  You grant yourself supernatural sight in areas of darkness |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36` | 0.577407 | **BLINDNESS **[two-actions] **SPELL 3**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet;** Targets** 1 creature  **Defense** Fortit |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` | 0.569656 | **HYPNOTIZE **[two-actions] **SPELL 3**  **ILLUSION** **MANIPULATE** **SUBTLE** **VISUAL**  **Traditions** arcane, occult  **Range **120 feet; **Area** 10-foot burst  **Defense** Will;** Duration** su |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/18` | 0.568193 | **FELINE SENSES **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MORPH**  **Traditions** divine, primal  **Duration** 1 hour |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/20` | 0.565816 | **ENTHRALL **[two-actions] **SPELL 3**  **AUDITORY** **CONCENTRATE** **EMOTION** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet;** Targets** all creatures in range  **Defense** Will |

### Query 38
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/24']
- Expected found: `True`
- Expected rank: `24`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/24', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/25', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/23']
- Expanded expected found: `True`
- Expanded expected rank: `24`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.756592 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/68` | 0.756592 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.756592 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/65` | 0.756592 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/60` | 0.756592 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.756592 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.756592 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.756592 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.756592 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.756592 | **SPELLS** |

### Query 39
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/57']
- Expected found: `True`
- Expected rank: `27`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/57', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/56', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/58']
- Expanded expected found: `True`
- Expanded expected rank: `27`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/3/Text/56` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/3/Text/58` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/64` | 0.816254 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/63` | 0.816254 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/60` | 0.816254 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/22` | 0.816254 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/41` | 0.816254 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/56` | 0.816254 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/61` | 0.816254 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/68` | 0.816254 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/82` | 0.816254 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/64` | 0.816254 | **CLASSES** |

### Query 40
- Text: What is the rule about The practitioners of occult traditions seek  to understand the unexplainable, categorize  the bizarre, and otherwise access the ephemeral in a?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/14` | 0.899293 | The practitioners of occult traditions seek  to understand the unexplainable, categorize  the bizarre, and otherwise access the ephemeral in a |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.580738 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.575381 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/24` | 0.568948 | **Traditions** occult |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/34` | 0.553408 | **Traditions** divine, occult, primal |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/6` | 0.539048 | **Traditions** arcane, divine, occult, primal |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.529911 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.519271 | insight about a topic. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.515366 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/12` | 0.513554 | **HALLUCINATION **[two-actions] **SPELL 5**  **ILLUSION** **INCAPACITATION** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** 1 creature  **Duration* |

### Query 41
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/63']
- Expected found: `True`
- Expected rank: `2`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/63', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/64', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/62']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/64` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/62` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/64` | 0.816254 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/63` | 0.816254 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/60` | 0.816254 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/22` | 0.816254 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/41` | 0.816254 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/56` | 0.816254 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/61` | 0.816254 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/68` | 0.816254 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/82` | 0.816254 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/64` | 0.816254 | **CLASSES** |

### Query 42
- Text: What is the rule about The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any number of times per day. If you're a prepared caster, you  can prepare a specific number of cantrips each day. You can't  prepare a cantrip in a spell slot.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/9', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` | 0.971436 | The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any nu |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 0.808159 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.730862 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.730049 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/17` | 0.677553 | Each spell uses the following format. Entries appear only  when applicable, so not all spells will have every entry  described here. The spell's name line also lists the type  of spell if it's a cantr |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.673533 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.658984 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/9` | 0.649950 | A cantrip is a special type of spell that's weaker than other  spells but can be used with greater freedom and flexibility. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 0.648470 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.645084 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |

### Query 43
- Text: Summarize **ALIEN CORE DRAGONS**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 330-363::/page/0/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/0/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/1` | 0.822822 | **ALIEN CORE DRAGONS** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/2` | 0.662068 | The dragons from *Alien Core* use the following  specifications for *dragon form*. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6` | 0.562227 | **Arcane** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/70` | 0.534269 | **GAME** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/79` | 0.534269 | **GAME** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/4` | 0.531072 | **DRAGON FORM **[two-actions] **SPELL 6**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, divine, occult, primal  **Duration** 1 minute  Calling upon powerful magic, you gain a L |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.530403 | **SUBTLE SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13` | 0.527209 | **Occult** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/55` | 0.525674 | **Summon Dragon**H Conjure a dragon to fight on your behalf. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/63` | 0.525674 | **Summon Dragon**H Conjure a dragon to fight on your behalf. |

### Query 44
- Text: What does **EVERLIGHT **[three-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/6', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/5', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/6` | 0.649784 | **EVERLIGHT **[three-actions] **SPELL 2**  **CONCENTRATE** **LIGHT** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **touch; **Targets** a gemstone worth 60 credits or more **D |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.621106 | **LIFE SEAL **[reaction] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.612204 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/37` | 0.596981 | **REVEALING LIGHT **[two-actions] **SPELL 2**  **CONCENTRATE** **LIGHT** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **120 feet;** Area** 10-foot burst  **Defense** Reflex; * |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/21` | 0.592727 | **HOLY LIGHT **[two-actions] **SPELL 3**  **ATTACK** **CONCENTRATE** **FIRE** **HOLY** **LIGHT** **MANIPULATE**  **Traditions** divine, primal  **Range **120 feet;** Targets** 1 creature  **Defense** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.590827 | SPELL ATTACKS |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.579332 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/20` | 0.569435 | **ENTHRALL **[two-actions] **SPELL 3**  **AUDITORY** **CONCENTRATE** **EMOTION** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet;** Targets** all creatures in range  **Defense** Will |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` | 0.567829 | **HYPNOTIZE **[two-actions] **SPELL 3**  **ILLUSION** **MANIPULATE** **SUBTLE** **VISUAL**  **Traditions** arcane, occult  **Range **120 feet; **Area** 10-foot burst  **Defense** Will;** Duration** su |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/62` | 0.564875 | OCCULT 3RD-RANK SPELLS |

### Query 45
- Text: Summarize DURATIONS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/6/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/6/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/6/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/6/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/9` | 0.756102 | DURATIONS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/15` | 0.725048 | LONG DURATIONS |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/8` | 0.651307 | **Duration** 5 minutes |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/48` | 0.642875 | **Duration** 1 minute |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/32/Text/31` | 0.610399 | **Heightened (4th)** The duration is 8 hours. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/18` | 0.601128 | **FELINE SENSES **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MORPH**  **Traditions** divine, primal  **Duration** 1 hour |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/1` | 0.599776 | **HEROISM **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult **Duration** 10 minutes |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/60` | 0.586925 | **PEST FORM **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Duration** 10 minutes |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/10` | 0.586457 | **Heightened (7th)** The duration increases to 1 hour. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.579098 | **SUBTLE SPELLS** |

### Query 46
- Text: What is the rule about You unleash the power of a supermassive black hole. All  creatures in the area take 6d10 bludgeoning and 6d10 void  damage. *Event horizon* ignores up to 10 resistance creatures  in the area have to bludgeoning, and up to 10 resistance they  have to void. Each creature attempts a Reflex save.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/1', 'PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/0` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/1` | 0.906848 | You unleash the power of a supermassive black hole. All  creatures in the area take 6d10 bludgeoning and 6d10 void  damage. *Event horizon* ignores up to 10 resistance creatures  in the area have to b |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/6` | 0.640415 | **ECLIPSE BURST **[two-actions] **SPELL 7**  **COLD** **CONCENTRATE** **DARKNESS** **MANIPULATE** **VOID**  **Traditions** arcane, divine, primal **Range **500 feet;** Area** 60-foot burst  **Defense* |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/5` | 0.628251 | **CATACLYSM **[two-actions] **SPELL 10**  **ACID** **AIR** **COLD** **CONCENTRATE** **EARTH** **ELECTRICITY** **FIRE** **MANIPULATE** **WATER**  **Traditions** arcane, primal  **Range **1,000 feet;** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/14/SectionHeader/7` | 0.619571 | **MASSACRE **[two-actions] **SPELL 9**  **CONCENTRATE** **DEATH** **MANIPULATE** **VOID**  **Traditions** arcane, divine, primal  **Area** 60-foot line  **Defense** Fortitude  You unleash a wave of de |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/3` | 0.608605 | **OVERLOAD SYSTEMS **[two-actions] **SPELL 5**  **CONCENTRATE** **ELECTRICITY** **MANIPULATE**  **Traditions** arcane, primal  **Area** 60-foot cone  **Defense** Reflex  You flood the area with a wave |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/44` | 0.605668 | **FALLING STARS **[two-actions] **SPELL 9**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Area** four 40-foot bursts  **Defense** basic Reflex  You reach into t |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/43` | 0.602720 | **PUMMELING RUBBLE **[two-actions] **SPELL 1**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Area** 15-foot cone  **Defense** Reflex  A spray of heavy rocks flies through |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/38` | 0.599152 | **DISINTEGRATE **[two-actions] **SPELL 6**  **ATTACK** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane  **Range **120 feet;** Targets** 1 creature, unattended object, or  force construct  **Defe |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/7` | 0.597368 | **DIVINE IMMOLATION **[two-actions] **SPELL 5**  **CONCENTRATE** **FIRE** **MANIPULATE** **SANCTIFIED** **SPIRIT**  **Traditions** divine  **Range **120 feet;** Area** 20-foot burst  **Defense** Refle |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/15` | 0.597201 | **Success** The creature takes 9d6 void damage. |

### Query 47
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/19']
- Expected found: `True`
- Expected rank: `27`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/20', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `27`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/63` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/56` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/60` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/31` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/55` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/63` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/81` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/40` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/78` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/59` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 48
- Text: What is the rule about After Triune's Signal connected cultures across the  Universe, the peoples of the galaxy have learned more  than ever before about the Universe's composition  thanks to science and technology. As technology  improves and creates mass-market marvels rivaling  what was once only possible for a powerful spellcaster,  magic is more static, with arcane universities,  occult societies, and religious orders preserving  ancient techniques and tomes into the modern  era. Many specialty tech items incorporate hybrid  magitechnology, and most spellcasters carry a backup  gun or other tech gear on them for when they run  out of spells. Magic and technology coexist, but most  spellcasters use analog spellcasting, and blending the  two together to create a hybrid item requires training.  Only a few spellcasters mix magic with technology they're seen as mavericks by most established magical  institutions. Technomancers and spellcasters who  have learned to command machines or connect with  computers using magic blaze a trail few have explored.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/12', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/12` | 0.923560 | After Triune's Signal connected cultures across the  Universe, the peoples of the galaxy have learned more  than ever before about the Universe's composition  thanks to science and technology. As tech |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` | 0.591306 | Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.582077 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.581796 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/8` | 0.542186 | If you're a prepared spellcaster—such as a technomancer  (see *Starfinder Tech Core*)—you must spend time each day  preparing spells for that day. At the start of your daily  preparations, you select |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.539997 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` | 0.536846 | With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own met |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/17` | 0.535336 | Magic with the illusion trait creates false sensory stimuli.  Sometimes illusions allow creatures a chance to disbelieve  the spell, which lets the creature ignore the spell if it succeeds  at doing s |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/2` | 0.534726 | The grand variety of spells includes those in the following pages and far more. Taught at magical  academies, drawn from other worlds, bestowed by mystical connections, and granted by all manner of  u |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.529977 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |

### Query 49
- Text: Summarize Host
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/502']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/502', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/503', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/501']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/503` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/501` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/502` | 0.710635 | Host |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/8` | 0.577015 | HOSTILE ACTIONS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.531221 | insight about a topic. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22` | 0.511689 | FOCUS POINTS FROM MULTIPLE  SOURCES |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.510844 | **Summoned** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/34` | 0.497811 | **Shrink**H Reduce a willing creature to Tiny size. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/36` | 0.496875 | **Translocate**H Teleport a moderate distance. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/10` | 0.496875 | **Translocate**H Teleport a moderate distance. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11` | 0.494937 | **SPELLCASTING IN STARFINDER** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.493279 | **CONCENTRATE** |

### Query 50
- Text: What is the rule about Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, though it's generally poor at affecting the spirit or  the soul. Witchwarpers who analyze probability and  spellcasters who draw magic from the underlying code  of the Universe are practitioners of arcane magic.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.955577 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/2` | 0.641819 | Spellcasters cast spells from one of four different spell lists, each representing a different magical tradition: arcane,  divine, occult, and primal. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` | 0.638762 | Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.633211 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.611405 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.597866 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/1` | 0.589729 | Whether it comes in the form of eldritch artifacts, otherworldly beings, or witchwarpers altering  reality with strange spells, magic brings fantasy and wonder to Starfinder. This chapter explains how |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` | 0.586975 | With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own met |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/14` | 0.570419 | The practitioners of occult traditions seek  to understand the unexplainable, categorize  the bizarre, and otherwise access the ephemeral in a |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/4` | 0.570299 | Spellcasting creates obvious sensory manifestations, such  as bright lights, crackling sounds, and sharp smells from the  gathering magic. Nearly all spells manifest a spell signature—a  colorful, glo |

### Query 51
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/67']
- Expected found: `True`
- Expected rank: `10`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/67', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/66', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/68']
- Expanded expected found: `True`
- Expanded expected rank: `10`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/66` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/68` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.756592 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/68` | 0.756592 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.756592 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/65` | 0.756592 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/60` | 0.756592 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.756592 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.756592 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.756592 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.756592 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.756592 | **SPELLS** |

### Query 52
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/41']
- Expected found: `True`
- Expected rank: `12`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/41', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/42', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/40']
- Expanded expected found: `True`
- Expanded expected rank: `12`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/40` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/29` | 0.888833 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/85` | 0.888833 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/91` | 0.888833 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/79` | 0.888833 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/64` | 0.888833 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/70` | 0.888833 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/88` | 0.888833 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/65` | 0.888833 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/67` | 0.888833 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/48` | 0.888833 | **PLAYING THE ** **GAME** |

### Query 53
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/22']
- Expected found: `True`
- Expected rank: `25`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/22', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `25`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/59` | 0.685680 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/24` | 0.685680 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/84` | 0.685680 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/78` | 0.685680 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/65` | 0.685680 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/43` | 0.685680 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/66` | 0.685680 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/59` | 0.685680 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/62` | 0.685680 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/60` | 0.685680 | **FEATS** |

### Query 54
- Text: Summarize 7 PLAYER CORE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/0']
- Expected found: `True`
- Expected rank: `3`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/0', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/1', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/69']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/3/Text/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/2/Text/69` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/0` | 0.887057 | 7 PLAYER CORE |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/15/SectionHeader/0` | 0.887057 | 7 PLAYER CORE |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/0` | 0.887057 | 7 PLAYER CORE |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/0` | 0.887057 | 7 PLAYER CORE |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/34` | 0.617430 | PRIMAL 7TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.585704 | CHAPTER 7: SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/5` | 0.576973 | OCCULT 7TH-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/57` | 0.569744 | ARCANE 7TH-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/11` | 0.551292 | DIVINE 7TH-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.542220 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |

### Query 55
- Text: Summarize **Divine**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9` | 0.807907 | **Divine** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/499` | 0.653043 | Divine |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/45` | 0.628489 | **Traditions** divine, primal |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/34` | 0.603020 | **Traditions** divine, occult, primal |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/6` | 0.579213 | **Traditions** arcane, divine, occult, primal |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.572090 | **SUBTLE SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.569070 | **Summoned** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.567918 | **CONCENTRATE** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/44` | 0.567918 | **CONCENTRATE** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13` | 0.563413 | **Occult** |

### Query 56
- Text: Summarize **CONCENTRATE** **MANIPULATE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/3/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/3/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` | 0.921250 | **CONCENTRATE** **MANIPULATE** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.784510 | **CONCENTRATE** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/44` | 0.784510 | **CONCENTRATE** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18` | 0.743427 | **CONCENTRATE** **EXPLORATION** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.692679 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/46` | 0.674155 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/67` | 0.674155 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/64` | 0.674155 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/83` | 0.674155 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/63` | 0.674155 | **Focus Spells** |

### Query 57
- Text: What is the rule about **Focus Spells**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/27']
- Expected found: `True`
- Expected rank: `11`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/27', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/28', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `11`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/46` | 0.799140 | **Focus Spells** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/62` | 0.799140 | **Focus Spells** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/89` | 0.799140 | **Focus Spells** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/65` | 0.799140 | **Focus Spells** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/71` | 0.799140 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/68` | 0.799140 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/63` | 0.799140 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/72` | 0.799140 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/70` | 0.799140 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/77` | 0.799140 | **Focus Spells** |

### Query 58
- Text: Summarize LINE OF EFFECT
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/7', 'PZO22001 Starfinder Player Core 294-329::/page/6/Text/6', 'PZO22001 Starfinder Player Core 294-329::/page/6/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/6/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/6/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/7` | 0.843147 | LINE OF EFFECT |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.562539 | insight about a topic. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.546336 | **SUBTLE SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/25` | 0.542657 | A horizontal line follows defense and duration, and the  effects of the spell are described after this line. This section  might also detail the possible results of a saving throw:  critical success, |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13` | 0.534803 | SPONTANEOUS SPELLS |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` | 0.531853 | **CONCENTRATE** **MANIPULATE** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22` | 0.528078 | FOCUS POINTS FROM MULTIPLE  SOURCES |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/19/ListItem/45` | 0.523353 | Low-light vision. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/11/ListItem/19` | 0.523353 | Low-light vision. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/22/ListItem/24` | 0.523353 | Low-light vision. |

### Query 59
- Text: What is the rule about actions, you can't use any special abilities, reactions, or free  actions that trigger when you Recall Knowledge.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/8/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/8/Text/26', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27', 'PZO22001 Starfinder Player Core 330-363::/page/8/Text/25']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/8/Text/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/26` | 0.849669 | actions, you can't use any special abilities, reactions, or free  actions that trigger when you Recall Knowledge. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/25` | 0.555032 | You rapidly catalog and collate information relevant to  your current situation. You can instantly use up to 6 Recall  Knowledge actions as part of Casting this Spell. For these |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/12` | 0.546664 | **AKASHIC DOWNLOAD **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** occult  **Requirements** You have a comm unit or computer, used as  a locus.  **Duration** 1 day  You e |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/5` | 0.534002 | If you want to identify a spell but don't have it prepared  or in your repertoire, you must spend an action on your  turn attempting to identify it using Recall Knowledge. You  typically notice a spel |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/26/Text/2` | 0.529891 | **REWRITE MEMORY **[two-actions] **SPELL 4**  **UNCOMMON** **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult  **Range **30 feet; **Targets** 1 creature **Defense** Will; **Duration** un |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/17/SectionHeader/14` | 0.516906 | **NEVER MIND **[two-actions] **SPELL 6**  **CONCENTRATE** **CURSE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature **Defense** W |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/28` | 0.516507 | **RETROCOGNITION** **SPELL 7**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Cast** 1 minute  **Duration** sustained  Opening your mind to mental echoes, you gain impressions  from |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47` | 0.510418 | **REVIVAL **[two-actions] **SPELL 10**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet;** Targets** dead creatures and living creatures of  y |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/9` | 0.505094 | A creature called by a spell or effect gains the summoned  trait. A summoned creature can't summon other creatures,  create things of value, or cast spells that require a cost. It  has the minion trai |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/34` | 0.503438 | **FREEZE TIME **[three-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  You temporarily stop time for everything but yourself,  allowing you to use several actions |

### Query 60
- Text: What does **BANISHMENT **[two-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/38', 'PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/23/Text/38` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26` | 0.688083 | **BANISHMENT **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet; **Targets** 1 creature that isn't on its |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/39` | 0.574811 | **SUBCONSCIOUS SUGGESTION **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **LINGUISTIC** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet;** Targe |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/7` | 0.569117 | PRIMAL 5TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` | 0.566166 | **CONTROL MACHINE **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature or hazard with t |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/40` | 0.565724 | OCCULT 5TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/41` | 0.561046 | **Banishment**H Send a creature back to its home plane. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/55` | 0.561046 | **Banishment**H Send a creature back to its home plane. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/18/Text/8` | 0.561046 | **Banishment**H Send a creature back to its home plane. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/16` | 0.561046 | **Banishment**H Send a creature back to its home plane. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/15` | 0.560222 | ARCANE 5TH-RANK SPELLS |

### Query 61
- Text: Summarize Occult
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/495']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/495', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/496', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/494']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/496` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/494` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/495` | 0.782515 | Occult |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13` | 0.716491 | **Occult** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/24` | 0.602188 | **Traditions** occult |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/16/ListItem/3` | 0.549677 | Darkvision. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/35/ListItem/2` | 0.549677 | Darkvision. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/16/ListItem/46` | 0.549677 | Darkvision. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/22/ListItem/48` | 0.549677 | Darkvision. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.543819 | insight about a topic. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/58` | 0.539138 | OCCULT 1ST-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/34` | 0.534479 | **Traditions** divine, occult, primal |

### Query 62
- Text: What does **FIRE SHIELD **[two-actions] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/41']
- Expected found: `True`
- Expected rank: `2`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/41', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/33', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/48']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/2/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/2/Text/48` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.604366 | **LIFE SEAL **[reaction] **SPELL 3** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/41` | 0.603313 | **FIRE SHIELD **[two-actions] **SPELL 4**  **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Duration** 1 minute  You create a hovering shield made of fire. As long as the  shi |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.597061 | SPELL ATTACKS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/17` | 0.590490 | OCCULT 4TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.588701 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/37` | 0.580808 | **IGNITION **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Targets** 1 creature  **Defense** AC  You |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/71` | 0.578726 | ARCANE 4TH-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/48` | 0.577587 | **FIREBALL **[two-actions] **SPELL 3**  **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Area** 20-foot burst  **Defense** basic Reflex  A roaring blast of |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/3` | 0.570681 | **NIGHTMARE** **SPELL 4**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Cast** 10 minutes  **Range **planetary;** Targets** 1 creature you know by name  **D |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/71` | 0.563064 | PRIMAL 4TH-RANK SPELLS |

### Query 63
- Text: Summarize **Rituals**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/30']
- Expected found: `True`
- Expected rank: `2`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/31', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/64` | 0.839916 | **Rituals** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/30` | 0.839916 | **Rituals** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/72` | 0.839916 | **Rituals** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/69` | 0.839916 | **Rituals** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/71` | 0.839916 | **Rituals** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/47` | 0.839916 | **Rituals** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/73` | 0.839916 | **Rituals** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/84` | 0.839916 | **Rituals** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/66` | 0.839916 | **Rituals** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/90` | 0.839916 | **Rituals** |

### Query 64
- Text: What is the rule about A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 0.935015 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` | 0.747923 | Focus spells are automatically heightened to half your level  rounded up, just like cantrips are. You can't cast a focus spell  if its minimum rank is greater than half your level rounded  up, even if |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.692762 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.676737 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.641067 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.617087 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` | 0.615113 | The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any nu |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/17` | 0.614566 | Each spell uses the following format. Entries appear only  when applicable, so not all spells will have every entry  described here. The spell's name line also lists the type  of spell if it's a cantr |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.602825 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 0.590519 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |

### Query 65
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/31']
- Expected found: `True`
- Expected rank: `14`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/31', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/32']
- Expanded expected found: `True`
- Expanded expected rank: `14`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/32` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/29` | 0.888833 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/85` | 0.888833 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/91` | 0.888833 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/79` | 0.888833 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/64` | 0.888833 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/70` | 0.888833 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/88` | 0.888833 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/65` | 0.888833 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/67` | 0.888833 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/48` | 0.888833 | **PLAYING THE ** **GAME** |

### Query 66
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/20']
- Expected found: `True`
- Expected rank: `10`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/20', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/21', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `10`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/18` | 0.863367 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/55` | 0.863367 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/28` | 0.863367 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/28` | 0.863367 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/61` | 0.863367 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/62` | 0.863367 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/57` | 0.863367 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/55` | 0.863367 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/39` | 0.863367 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/20` | 0.863367 | **INTRODUCTION** |

### Query 67
- Text: Summarize **MAGICAL TRADITIONS**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1` | 0.848082 | **MAGICAL TRADITIONS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/30` | 0.671920 | **Rituals** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/40` | 0.671920 | **Rituals** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/66` | 0.671920 | **Rituals** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/66` | 0.671920 | **Rituals** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/71` | 0.671920 | **Rituals** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/84` | 0.671920 | **Rituals** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/48` | 0.671920 | **Rituals** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/90` | 0.671920 | **Rituals** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/37` | 0.671920 | **Rituals** |

### Query 68
- Text: Summarize Climb
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/504']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/504', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/503', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/505']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/503` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/505` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/504` | 0.784968 | Climb |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.547817 | insight about a topic. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/50` | 0.534111 | **Jump**H Make an impressive leap. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/4` | 0.534111 | **Jump**H Make an impressive leap. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.524588 | **Summoned** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15` | 0.505947 | HEIGHTENED SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/21/ListItem/17` | 0.505618 | **Ape** Speed 25 feet, climb 20 feet; **Melee **[one-action] fist, **Damage ** 2d6 bludgeoning. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.500407 | **SUBTLE SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18` | 0.498781 | **CONCENTRATE** **EXPLORATION** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/19` | 0.498010 | **STUMBLE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **100 feet; **Targets** 1 creature  **Defense** Reflex  A burst of micrograv |

### Query 69
- Text: What is the rule about NON-SPELLCASTERS WITH  FOCUS SPELLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20` | 0.822212 | NON-SPELLCASTERS WITH  FOCUS SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21` | 0.727302 | SPELLCASTERS WITH FOCUS  SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` | 0.585847 | FOCUS SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.518412 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5` | 0.516367 | SPELL SLOTS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/13` | 0.507715 | SUSTAINING SPELLS |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/67` | 0.507280 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/27` | 0.507280 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/64` | 0.507280 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/62` | 0.507280 | **Focus Spells** |

### Query 70
- Text: Summarize 7 PLAYER CORE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/0']
- Expected found: `True`
- Expected rank: `4`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/49', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/0` | 0.887057 | 7 PLAYER CORE |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/15/SectionHeader/0` | 0.887057 | 7 PLAYER CORE |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/0` | 0.887057 | 7 PLAYER CORE |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/0` | 0.887057 | 7 PLAYER CORE |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/34` | 0.617430 | PRIMAL 7TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.585704 | CHAPTER 7: SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/5` | 0.576973 | OCCULT 7TH-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/57` | 0.569744 | ARCANE 7TH-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/11` | 0.551292 | DIVINE 7TH-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.542220 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |

### Query 71
- Text: What does **HEROISM **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/1', 'PZO22001 Starfinder Player Core 330-363::/page/6/Text/44', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/6/Text/44` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/7/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/1` | 0.687135 | **HEROISM **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult **Duration** 10 minutes |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.629357 | **LIFE SEAL **[reaction] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.610523 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/18` | 0.586642 | **FELINE SENSES **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MORPH**  **Traditions** divine, primal  **Duration** 1 hour |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` | 0.585092 | **HYPNOTIZE **[two-actions] **SPELL 3**  **ILLUSION** **MANIPULATE** **SUBTLE** **VISUAL**  **Traditions** arcane, occult  **Range **120 feet; **Area** 10-foot burst  **Defense** Will;** Duration** su |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.580135 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/4` | 0.577992 | **HONEYED WORDS **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes  You unlock the |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/44` | 0.572085 | **HEAL **[one-action]** TO **[three-actions] **SPELL 1**  **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **varies; **Targets** 1 willing living creature or 1 undead  c |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/13` | 0.571199 | **HOLOGRAPHIC MEMORY **[two-actions] **SPELL 3**  **UNCOMMON** **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **touch;** Targets** 1 creature or corpse  **Defense** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/23` | 0.570791 | **SHARE PAIN **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **30 feet;** Targets** 1 creature  **Defense** Will  You telepathically shar |

### Query 72
- Text: Summarize Cosmic
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/498']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/498', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/499', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/497']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/499` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/497` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/498` | 0.764366 | Cosmic |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/22/ListItem/49` | 0.627749 | Cosmic trait. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.545614 | **Summoned** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.529329 | insight about a topic. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/499` | 0.527123 | Divine |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/18/Text/58` | 0.518205 | **Call** **Cosmos**H Call down a column of cosmic matter to burn  and freeze. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/29` | 0.518205 | **Call** **Cosmos**H Call down a column of cosmic matter to burn  and freeze. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/62` | 0.514440 | **Summon Celestial**H Conjure a celestial to fight for you. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/494` | 0.501662 | Akashic |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.499409 | **SUBTLE SPELLS** |

### Query 73
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/20']
- Expected found: `True`
- Expected rank: `23`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/20', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `23`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/64` | 0.816254 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/63` | 0.816254 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/60` | 0.816254 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/22` | 0.816254 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/41` | 0.816254 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/56` | 0.816254 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/61` | 0.816254 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/68` | 0.816254 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/82` | 0.816254 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/64` | 0.816254 | **CLASSES** |

### Query 74
- Text: Summarize Speeds
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/488']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/488', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/489', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/487']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/489` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/487` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/488` | 0.815034 | Speeds |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/14` | 0.622642 | **Tailwind**H Increase your speed for an hour. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/2` | 0.622642 | **Tailwind**H Increase your speed for an hour. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/2` | 0.601206 | **Fly**H Grant a target a fly Speed. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/20/ListItem/16` | 0.597143 | Speed 20 feet. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/20/Text/12` | 0.591050 | **Speed **fly 30 feet |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/70` | 0.586665 | **Fleet Step** Make your Speed much faster. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/42` | 0.586665 | **Fleet Step** Make your Speed much faster. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/25` | 0.583927 | **Fly**H Grant the target a fly Speed. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/76` | 0.583927 | **Fly**H Grant the target a fly Speed. |

### Query 75
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/61']
- Expected found: `True`
- Expected rank: `13`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/61', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/62', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/60']
- Expanded expected found: `True`
- Expanded expected rank: `13`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/3/Text/62` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/3/Text/60` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.756592 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/68` | 0.756592 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.756592 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/65` | 0.756592 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/60` | 0.756592 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.756592 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.756592 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.756592 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.756592 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.756592 | **SPELLS** |

### Query 76
- Text: What is the rule about Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus spells only through special class features or feats,  rather than choosing them from a spell list. Furthermore, you  cast focus spells using a special pool of Focus Points—you can't  prepare a focus spell in a spell slot or use your spell slots to  cast focus spells; similarly, you can't spend your Focus Points  to cast spells that aren't focus spells. Even some classes that  don't normally grant spellcasting can grant focus spells. The  title of a focus spell's stat block says "Focus" instead of "Spell",  and the spell has the focus trait.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/13', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` | 0.965476 | Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.827564 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.758719 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/23` | 0.752230 | It's possible, especially through archetypes, to gain focus  spells from more than one source. If this happens, you  have just one focus pool, counting all your focus spells to  determine the points i |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` | 0.729543 | Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your p |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` | 0.718377 | Focus spells are automatically heightened to half your level  rounded up, just like cantrips are. You can't cast a focus spell  if its minimum rank is greater than half your level rounded  up, even if |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.717145 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.697728 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.697047 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/21` | 0.688572 | Some spells allow you to target a creature, an object, or  something more specific. The target must be within the  spell's range, and you must be able to see it (or otherwise  perceive it with a preci |

### Query 77
- Text: What does **CHRONO PUSH **[two-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17` | 0.706895 | **CHRONO PUSH **[two-actions] **SPELL 5**  **ATTACK** **CONCENTRATE** **FORCE** **MANIPULATE**  **Traditions** occult  **Range **500 feet;** Targets** 1 creature **Defense** AC and basic Reflex  You p |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/42` | 0.592211 | **Chrono** **Push ** H Push a target away and damage creatures  nearby. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` | 0.574176 | **CONTROL MACHINE **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature or hazard with t |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/40` | 0.573145 | OCCULT 5TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.568264 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/39` | 0.567276 | **SUBCONSCIOUS SUGGESTION **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **LINGUISTIC** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet;** Targe |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/15` | 0.560511 | ARCANE 5TH-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/5` | 0.560047 | **HYDRAULIC PUSH **[two-actions] **SPELL 1**  **ATTACK** **CONCENTRATE** **MANIPULATE** **WATER**  **Traditions** arcane, primal  **Range **60 feet;** Targets** 1 creature or unattended object **Defen |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/7` | 0.555598 | PRIMAL 5TH-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.547006 | SPELL ATTACKS |

### Query 78
- Text: What does **EXECUTE **[two-actions] **SPELL 7** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/12']
- Expected found: `True`
- Expected rank: `10`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/12', 'PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/6', 'PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/20']
- Expanded expected found: `True`
- Expanded expected rank: `10`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.700462 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.654362 | CHAPTER 7: SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/5` | 0.616030 | OCCULT 7TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.604920 | SPELL ATTACKS |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/22/SectionHeader/3` | 0.600798 | **PLANAR SEAL **[two-actions] **SPELL 7**  **UNCOMMON** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult **Range **120 feet; **Area** 60-foot burst **Duration** until your next da |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/39` | 0.594948 | **SUBCONSCIOUS SUGGESTION **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **LINGUISTIC** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet;** Targe |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.588646 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/57` | 0.584249 | ARCANE 7TH-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/34` | 0.583469 | PRIMAL 7TH-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/12` | 0.583295 | **EXECUTE **[two-actions] **SPELL 7**  **CONCENTRATE** **DEATH** **MANIPULATE** **VOID**  **Traditions** divine, primal  **Range **30 feet; **Targets** 1 creature  **Defense** basic Fortitude  You poi |

### Query 79
- Text: Summarize **Occult**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13` | 0.815280 | **Occult** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/495` | 0.707703 | Occult |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/24` | 0.687696 | **Traditions** occult |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.632540 | **SUBTLE SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/34` | 0.614549 | **Traditions** divine, occult, primal |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` | 0.607813 | **CONCENTRATE** **MANIPULATE** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/44` | 0.602578 | **CONCENTRATE** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.602578 | **CONCENTRATE** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/6` | 0.595223 | **Traditions** arcane, divine, occult, primal |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.592814 | **Summoned** |

### Query 80
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/58']
- Expected found: `True`
- Expected rank: `5`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/58', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/59', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/57']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/3/Text/59` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/3/Text/57` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/65` | 0.727771 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/57` | 0.727771 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/58` | 0.727771 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/65` | 0.727771 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/58` | 0.727771 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/60` | 0.727771 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/62` | 0.727771 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/64` | 0.727771 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/33` | 0.727771 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/58` | 0.727771 | **SKILLS** |

### Query 81
- Text: What does **BIND UNDEAD **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/24/Text/12', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/24/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/13` | 0.655847 | **BIND UNDEAD **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Range **30 feet; **Targets** 1 mindless undead creature with a  level no greater tha |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.629306 | **LIFE SEAL **[reaction] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.600398 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/36` | 0.590424 | **EARTHBIND **[two-actions] **SPELL 3**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 flying creature  **Defense** Fortitude; **Duration** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/63` | 0.590419 | **Bind Undead** Take control of a mindless undead. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/23` | 0.590419 | **Bind Undead** Take control of a mindless undead. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/43` | 0.590419 | **Bind Undead** Take control of a mindless undead. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36` | 0.576953 | **BLINDNESS **[two-actions] **SPELL 3**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet;** Targets** 1 creature  **Defense** Fortit |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.571867 | SPELL ATTACKS |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/20` | 0.564150 | **ENTHRALL **[two-actions] **SPELL 3**  **AUDITORY** **CONCENTRATE** **EMOTION** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet;** Targets** all creatures in range  **Defense** Will |

### Query 82
- Text: What is the rule about **Focus Spells**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/64']
- Expected found: `True`
- Expected rank: `23`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/64', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/65', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/63']
- Expanded expected found: `True`
- Expanded expected rank: `23`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/3/Text/65` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/3/Text/63` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/46` | 0.799140 | **Focus Spells** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/62` | 0.799140 | **Focus Spells** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/89` | 0.799140 | **Focus Spells** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/65` | 0.799140 | **Focus Spells** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/71` | 0.799140 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/68` | 0.799140 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/63` | 0.799140 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/72` | 0.799140 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/70` | 0.799140 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/77` | 0.799140 | **Focus Spells** |

### Query 83
- Text: Summarize FOCUS POINTS FROM MULTIPLE  SOURCES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22` | 0.906768 | FOCUS POINTS FROM MULTIPLE  SOURCES |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.603259 | insight about a topic. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.589891 | **CONCENTRATE** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/44` | 0.589891 | **CONCENTRATE** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` | 0.586790 | **CONCENTRATE** **MANIPULATE** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/39` | 0.585211 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/27` | 0.585211 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/65` | 0.585211 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/71` | 0.585211 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/64` | 0.585211 | **Focus Spells** |

### Query 84
- Text: Summarize —
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/496']
- Expected found: `True`
- Expected rank: `7`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/496', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/495', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/497']
- Expanded expected found: `True`
- Expanded expected rank: `7`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/495` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/497` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.622939 | insight about a topic. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.582530 | **Summoned** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/44` | 0.571699 | **CONCENTRATE** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.571699 | **CONCENTRATE** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.566608 | **SUBTLE SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/500` | 0.563244 | — |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/496` | 0.563244 | — |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/492` | 0.563244 | — |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/17` | 0.555216 | DISMISSING |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` | 0.544306 | **CONCENTRATE** **MANIPULATE** |

### Query 85
- Text: Summarize **ANCESTRIES & **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/29', 'PZO22001 Starfinder Player Core 330-363::/page/5/Text/28', 'PZO22001 Starfinder Player Core 330-363::/page/5/Text/34']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/5/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/5/Text/34` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/29` | 0.858853 | **ANCESTRIES & ** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/59` | 0.809019 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/19` | 0.809019 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/54` | 0.809019 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/39` | 0.809019 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/31` | 0.809019 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/55` | 0.809019 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/67` | 0.809019 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/63` | 0.809019 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/40` | 0.809019 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 86
- Text: What does **HEAL **[one-action]** TO **[three-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/6/Text/44']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/6/Text/44', 'PZO22001 Starfinder Player Core 330-363::/page/6/Text/36', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/6/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/7/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/44` | 0.643495 | **HEAL **[one-action]** TO **[three-actions] **SPELL 1**  **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **varies; **Targets** 1 willing living creature or 1 undead  c |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.632702 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/26` | 0.605570 | **HARM **[one-action]** TO **[three-actions] **SPELL 1**  **MANIPULATE** **VOID**  **Traditions** divine  **Range **varies; **Targets** 1 living creature or 1 willing undead  creature  You channel voi |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.600541 | **LIFE SEAL **[reaction] **SPELL 3** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.594887 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/31/SectionHeader/22` | 0.590897 | **SOOTHE **[two-actions] **SPELL 1**  **CONCENTRATE** **EMOTION** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** occult  **Range **30 feet;** Targets** 1 willing creature  **Duration** 1 minute |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/23` | 0.586833 | **SHARE PAIN **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **30 feet;** Targets** 1 creature  **Defense** Will  You telepathically shar |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39` | 0.585087 | **CLEANSE AFFLICTION **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  Gentle restorative |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.578407 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29` | 0.577977 | **BLESS **[two-actions] **SPELL 1**  **AURA** **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Area** 15-foot emanation  **Duration** 1 minute  Blessings from beyond help yo |

### Query 87
- Text: What is the rule about Some types of magic, such as that of most magic items, don't belong to any single tradition. These have the magical  trait instead of a tradition trait.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/4` | 0.876644 | Some types of magic, such as that of most magic items, don't belong to any single tradition. These have the magical  trait instead of a tradition trait. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/21` | 0.641635 | **Tradition** This entry lists the magical traditions the spell  belongs to. Some feats or other abilities might add a  spell to your spell list even if you don't follow the listed  traditions. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.624527 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/6/Text/6` | 0.563761 | Spells that affect multiple creatures in an area can have  both an Area entry and a Targets entry. A spell that has an  area but no targets listed usually affects all creatures in the  area indiscrimi |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/4` | 0.557109 | Non-magical light always shines in non-magical darkness  and always fails to shine in magical darkness. Magical light  always shines in non-magical darkness but shines in magical  darkness only if the |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.554710 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/28` | 0.549993 | If you have an innate spell, you can cast it even if it's not of  a spell rank you can normally cast. This is especially common  for monsters. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/6/Text/2` | 0.548132 | A spell with the subtle trait can be cast  without incantations and doesn't have obvious  manifestations. Most of these spells enhance your  subterfuge or stealth, such as *invisibility*. Some  abilit |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/12` | 0.544213 | Spells that slightly alter a creature's form have the morph trait.  Any Strikes specifically granted by a magical morph effect also  gain the magical trait. You can be affected by multiple morph  spel |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/20` | 0.543552 | **Tradition Resistance** If the dragon's magical tradition  matches that of your *dragon form* spell, you gain the  listed ability. **Arcane** resistance 5 against damage from  spells; **divine** resi |

### Query 88
- Text: What does **ENTHRALL **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/Text/20', 'PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/32', 'PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/20` | 0.654156 | **ENTHRALL **[two-actions] **SPELL 3**  **AUDITORY** **CONCENTRATE** **EMOTION** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet;** Targets** all creatures in range  **Defense** Will |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.647082 | **LIFE SEAL **[reaction] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.645840 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.615803 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.609956 | SPELL ATTACKS |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` | 0.599489 | **HYPNOTIZE **[two-actions] **SPELL 3**  **ILLUSION** **MANIPULATE** **SUBTLE** **VISUAL**  **Traditions** arcane, occult  **Range **120 feet; **Area** 10-foot burst  **Defense** Will;** Duration** su |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/1` | 0.586154 | **HEROISM **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult **Duration** 10 minutes |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/18` | 0.582294 | **FELINE SENSES **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MORPH**  **Traditions** divine, primal  **Duration** 1 hour |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.581395 | CHAPTER 7: SPELLS |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.579549 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |

### Query 89
- Text: Summarize **Darkness and Light**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/3', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/3` | 0.814769 | **Darkness and Light** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/20/Text/5` | 0.579728 | **Perception **+0; darkvision |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13` | 0.569843 | **Occult** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.563011 | **Summoned** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/19/ListItem/45` | 0.558830 | Low-light vision. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/11/ListItem/19` | 0.558830 | Low-light vision. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/22/ListItem/24` | 0.558830 | Low-light vision. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/38` | 0.557700 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/74` | 0.557700 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/58` | 0.557700 | **INTRODUCTION** |

### Query 90
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/66']
- Expected found: `True`
- Expected rank: `9`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/66', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/65', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/67']
- Expanded expected found: `True`
- Expanded expected rank: `9`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/65` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/63` | 0.865652 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/59` | 0.865652 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/60` | 0.865652 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/35` | 0.865652 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/64` | 0.865652 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/58` | 0.865652 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/67` | 0.865652 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/67` | 0.865652 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/66` | 0.865652 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/79` | 0.865652 | **EQUIPMENT** |

### Query 91
- Text: What is the rule about **Spell Lists**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/68']
- Expected found: `True`
- Expected rank: `14`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/68', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/67', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/69']
- Expanded expected found: `True`
- Expanded expected rank: `14`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/69` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/87` | 0.732608 | **Spell Lists** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/25` | 0.732608 | **Spell Lists** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/60` | 0.732608 | **Spell Lists** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/69` | 0.732608 | **Spell Lists** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/44` | 0.732608 | **Spell Lists** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/69` | 0.732608 | **Spell Lists** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/75` | 0.732608 | **Spell Lists** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/62` | 0.732608 | **Spell Lists** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/84` | 0.732608 | **Spell Lists** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/61` | 0.732608 | **Spell Lists** |

### Query 92
- Text: What is the rule about HEIGHTENED SPELLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15` | 0.787925 | HEIGHTENED SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/13` | 0.611323 | SUSTAINING SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4` | 0.568971 | Heightened Spontaneous Spells |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.560898 | CHAPTER 7: SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/7` | 0.556829 | PREPARED SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/3` | 0.553844 | IDENTIFYING SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.549978 | SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` | 0.531954 | FOCUS SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/16` | 0.525790 | READING SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.523040 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |

### Query 93
- Text: What does **GHOSTLY CARRIER **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/17', 'PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/10', 'PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/17` | 0.689742 | **GHOSTLY CARRIER **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet **Duration** 1 minute  You create a Tiny, semi-corporeal figure with a |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.582651 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/32/SectionHeader/56` | 0.582357 | **SPIRITUAL ARMAMENT **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SANCTIFIED** **SPIRIT**  **Traditions** divine, occult  **Range **120 feet; **Targets** 1 creature  **Defense** AC; * |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/25` | 0.582263 | OCCULT 2ND-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.570066 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/17` | 0.569726 | PRIMAL 2ND-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/29` | 0.554035 | **STUPEFY **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** varies  You du |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/23` | 0.552870 | **GHOST KILLER WEAPON **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 weapon that's either unattended or  wielded by you or a |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/56` | 0.552361 | **ILLUSORY CREATURE**[two-actions] **SPELL 2**  **AUDITORY** **CONCENTRATE** **ILLUSION** **MANIPULATE** **OLFACTORY** **VISUAL**  **Traditions** arcane, occult  **Range **500 feet  **Duration** susta |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` | 0.550838 | **HYPNOTIZE **[two-actions] **SPELL 3**  **ILLUSION** **MANIPULATE** **SUBTLE** **VISUAL**  **Traditions** arcane, occult  **Range **120 feet; **Area** 10-foot burst  **Defense** Will;** Duration** su |

### Query 94
- Text: What is the rule about Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule is for spells with the cantrip trait; once  you prepare a cantrip, you can cast it as many times as you  want until the next time you prepare spells. See page 296  for more information on cantrips.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/9', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 0.980242 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` | 0.805906 | The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any nu |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.755661 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.729915 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/10` | 0.699177 | You might gain an ability that allows you to swap  prepared spells or perform other aspects of preparing spells  at different times throughout the day, but only your daily  preparation counts for the |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/Text/16` | 0.686716 | If a spell's duration says it lasts until your next daily  preparations, on the next day you can refrain from preparing  a new spell in that spell's slot. (If you are a spontaneous caster,  you can in |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/8` | 0.675187 | If you're a prepared spellcaster—such as a technomancer  (see *Starfinder Tech Core*)—you must spend time each day  preparing spells for that day. At the start of your daily  preparations, you select |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/17` | 0.674153 | Each spell uses the following format. Entries appear only  when applicable, so not all spells will have every entry  described here. The spell's name line also lists the type  of spell if it's a cantr |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/22` | 0.668755 | **Cast** Spells that take longer than a single turn to cast include  this entry to list the time required, such as "1 minute." If  the spell has a cost, locus, requirements, or a trigger, that  inform |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21` | 0.659551 | **CONTINGENCY** **SPELL 7**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane  **Cast** 10 minutes **Duration** until your next daily preparations  You prepare a spell that will trigger later. Wh |

### Query 95
- Text: Summarize TOUCH RANGE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/16', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/17', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/16` | 0.885916 | TOUCH RANGE |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/7` | 0.666676 | **Range **touch;** Targets** 1 creature |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14` | 0.618447 | RANGES, AREAS, AND  TARGETS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28` | 0.582695 | **ADHERE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Range **touch; **Targets** 1 held or unattended object or a 5-footsquare sur |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.553407 | insight about a topic. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/24` | 0.553221 | **Heightened (4th)** The spell's range is touch and it targets 1  willing creature. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/17` | 0.551230 | A spell with a touch range requires you to physically touch  the target. You use your unarmed reach to determine  whether you can touch the creature. You can usually touch  them automatically, though |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/47` | 0.550149 | **Range **60 feet; **Targets** the triggering creature |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/ListItem/45` | 0.537209 | Low-light vision. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/22/ListItem/24` | 0.537209 | Low-light vision. |

### Query 96
- Text: What does **ADHERE **[one-action] **CANTRIP 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28', 'PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/36', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/19/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28` | 0.707033 | **ADHERE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Range **touch; **Targets** 1 held or unattended object or a 5-footsquare sur |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/5` | 0.596386 | **STABILIZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet; **Targets** 1 dying creature  Life ene |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/5/SectionHeader/20` | 0.594996 | **GUIDANCE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE**  **Traditions** divine, occult, primal  **Range **30 feet; **Targets** 1 creature  **Duration** until the start of your next turn |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/3` | 0.581859 | **INJURY ECHO **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **60 feet; **Targets** 1 creature  **Defense** Will  You manifest an inj |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41` | 0.574693 | **ANALYZE TARGET **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **30 feet; **Targets** 1 creature  **Dur |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/11` | 0.573760 | **FORBIDDING WARD **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** divine, occult  **Range **30 feet; **Targets** 1 ally and 1 enemy  **Duration** sustained up |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/7` | 0.571659 | **Range **touch;** Targets** 1 creature |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/37` | 0.570434 | **IGNITION **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Targets** 1 creature  **Defense** AC  You |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/52` | 0.568214 | **LIGHT **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **LIGHT** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **120 feet  **Duration** until your next daily prepa |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19` | 0.562819 | **CAUSTIC BLAST **[two-actions] **CANTRIP 1**  **ACID** **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Area** 5-foot burst  **Defense** basic Reflex  Y |

### Query 97
- Text: What does **FROSTBITE **[two-actions] **CANTRIP 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/39']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/39', 'PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/34', 'PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/47']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/47` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/39` | 0.663592 | **FROSTBITE **[two-actions] **CANTRIP 1**  **CANTRIP** **COLD** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets** 1 creature  **Defense** Fortitude  An orb |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/5` | 0.609339 | **STABILIZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet; **Targets** 1 dying creature  Life ene |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19` | 0.556492 | **CAUSTIC BLAST **[two-actions] **CANTRIP 1**  **ACID** **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Area** 5-foot burst  **Defense** basic Reflex  Y |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/2` | 0.551320 | **DAZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE** **MENTAL** **NONLETHAL**  **Traditions** arcane, divine, occult **Range **60 feet; **Targets** 1 creature **Defense** W |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/11` | 0.550730 | **FORBIDDING WARD **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** divine, occult  **Range **30 feet; **Targets** 1 ally and 1 enemy  **Duration** sustained up |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28` | 0.550466 | **ADHERE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Range **touch; **Targets** 1 held or unattended object or a 5-footsquare sur |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/26/Text/12` | 0.548412 | **RICOCHET **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE** **METAL**  **Traditions** arcane, divine  **Range **30 feet; **Targets** 1 or 2 creatures  **Defense** basic Reflex |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/19` | 0.547740 | **STUMBLE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **100 feet; **Targets** 1 creature  **Defense** Reflex  A burst of micrograv |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/3` | 0.547125 | **INJURY ECHO **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **60 feet; **Targets** 1 creature  **Defense** Will  You manifest an inj |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/52` | 0.534361 | **LIGHT **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **LIGHT** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **120 feet  **Duration** until your next daily prepa |

### Query 98
- Text: What is the rule about **Focus Spells**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/65']
- Expected found: `True`
- Expected rank: `20`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/65', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/64', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/66']
- Expanded expected found: `True`
- Expanded expected rank: `20`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/7/Text/64` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/7/Text/66` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/46` | 0.799140 | **Focus Spells** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/62` | 0.799140 | **Focus Spells** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/89` | 0.799140 | **Focus Spells** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/65` | 0.799140 | **Focus Spells** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/71` | 0.799140 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/68` | 0.799140 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/63` | 0.799140 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/72` | 0.799140 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/70` | 0.799140 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/77` | 0.799140 | **Focus Spells** |

### Query 99
- Text: What is the rule about Spellcasters cast spells from one of four different spell lists, each representing a different magical tradition: arcane,  divine, occult, and primal.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/2` | 0.839798 | Spellcasters cast spells from one of four different spell lists, each representing a different magical tradition: arcane,  divine, occult, and primal. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.607303 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/6` | 0.599957 | **Traditions** arcane, divine, occult, primal |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.584029 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/13/SectionHeader/43` | 0.579777 | **MANIFESTATION **[three-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  You spin secrets from the fundaments of magic, shaping them  into a power |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.556264 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/34` | 0.555196 | **Traditions** divine, occult, primal |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.541592 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/20` | 0.537246 | **Tradition Resistance** If the dragon's magical tradition  matches that of your *dragon form* spell, you gain the  listed ability. **Arcane** resistance 5 against damage from  spells; **divine** resi |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/2` | 0.536355 | These lists include the spells for each tradition, including cantrips. (Focus spells appear on pages 375–380.)  A superscript "H" indicates a spell has extra effects when heightened, and a spell whose |

### Query 100
- Text: What does **CONTROL MACHINE **[two-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/39', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/39` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` | 0.690624 | **CONTROL MACHINE **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature or hazard with t |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.615401 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/40` | 0.607344 | OCCULT 5TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/39` | 0.600641 | **SUBCONSCIOUS SUGGESTION **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **LINGUISTIC** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet;** Targe |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/15` | 0.581703 | ARCANE 5TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/7` | 0.577844 | PRIMAL 5TH-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.565873 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/3` | 0.565287 | **OVERLOAD SYSTEMS **[two-actions] **SPELL 5**  **CONCENTRATE** **ELECTRICITY** **MANIPULATE**  **Traditions** arcane, primal  **Area** 60-foot cone  **Defense** Reflex  You flood the area with a wave |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/55` | 0.564027 | **DOMINATE **[two-actions] **SPELL 6**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult  **Range **30 feet;** Targets** 1 creature  **D |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/54` | 0.560713 | DIVINE 5TH-RANK SPELLS |

### Query 101
- Text: Summarize **GLOSSARY & **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/34']
- Expected found: `True`
- Expected rank: `3`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/34', 'PZO22001 Starfinder Player Core 330-363::/page/5/Text/29', 'PZO22001 Starfinder Player Core 330-363::/page/6/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/5/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/6/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/79` | 0.829706 | **GLOSSARY & ** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/75` | 0.829706 | **GLOSSARY & ** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/34` | 0.829706 | **GLOSSARY & ** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/93` | 0.774245 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/33` | 0.774245 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/74` | 0.774245 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/43` | 0.774245 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/69` | 0.774245 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/93` | 0.774245 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/67` | 0.774245 | **GLOSSARY & ** **INDEX** |

### Query 102
- Text: What does **FALSE VITALITY **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/74', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/74` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/2/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/2/SectionHeader/1` | 0.684236 | **FALSE VITALITY **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Duration** 8 hours  You augment your flesh with the energies typically used to  manipulat |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.622056 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/39` | 0.600191 | **False Vitality**H Gain temporary Hit Points. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/19` | 0.600191 | **False Vitality**H Gain temporary Hit Points. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.590121 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/32` | 0.589322 | **INSTANT VIRUS **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane  **Range **touch; **Targets** 1 creature with the tech trait  **Defense** Fortitude  Your touch insta |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/29` | 0.589034 | **STUPEFY **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** varies  You du |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47` | 0.587389 | **REVIVAL **[two-actions] **SPELL 10**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet;** Targets** dead creatures and living creatures of  y |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/32/SectionHeader/56` | 0.586896 | **SPIRITUAL ARMAMENT **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SANCTIFIED** **SPIRIT**  **Traditions** divine, occult  **Range **120 feet; **Targets** 1 creature  **Defense** AC; * |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/12` | 0.585725 | **EXECUTE **[two-actions] **SPELL 7**  **CONCENTRATE** **DEATH** **MANIPULATE** **VOID**  **Traditions** divine, primal  **Range **30 feet; **Targets** 1 creature  **Defense** basic Fortitude  You poi |

### Query 103
- Text: Summarize **Rituals**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/71']
- Expected found: `True`
- Expected rank: `5`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/71', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/72', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/70']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/72` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/70` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/64` | 0.839916 | **Rituals** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/30` | 0.839916 | **Rituals** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/72` | 0.839916 | **Rituals** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/69` | 0.839916 | **Rituals** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/71` | 0.839916 | **Rituals** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/47` | 0.839916 | **Rituals** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/73` | 0.839916 | **Rituals** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/84` | 0.839916 | **Rituals** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/66` | 0.839916 | **Rituals** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/90` | 0.839916 | **Rituals** |

### Query 104
- Text: Summarize —
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/500']
- Expected found: `True`
- Expected rank: `6`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/500', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/499', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/501']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/499` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/501` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.622939 | insight about a topic. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.582530 | **Summoned** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/44` | 0.571699 | **CONCENTRATE** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.571699 | **CONCENTRATE** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.566608 | **SUBTLE SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/500` | 0.563244 | — |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/496` | 0.563244 | — |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/492` | 0.563244 | — |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/17` | 0.555216 | DISMISSING |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` | 0.544306 | **CONCENTRATE** **MANIPULATE** |

### Query 105
- Text: What does **CALM **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/25/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/25/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/25/Text/11` | 0.667641 | **CALM **[two-actions] **SPELL 2**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **120 feet;** Area** 10-foot burst  **Defense** Wil |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.622761 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` | 0.607747 | **CLEAR MIND **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You drive menta |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/32/Text/2` | 0.600346 | **SOUND BODY **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You send a su |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/29` | 0.598415 | **STUPEFY **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** varies  You du |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/28` | 0.596984 | **Calm** Suppress strong emotions and hostility. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/29/SectionHeader/14` | 0.595138 | **SILENCE **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** divine, occult  **Range **touch;** Targets** 1 willing creature  **Duration** 1 minute  The target makes n |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52` | 0.594132 | **CHARM **[two-actions] **SPELL 1**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 creatur |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/46` | 0.590034 | **PEACEFUL REST **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **touch;** Targets** 1 corpse  **Duration** until your next daily pr |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/25` | 0.580741 | OCCULT 2ND-RANK SPELLS |

### Query 106
- Text: What is the rule about **Failure** The target takes full damage, persistent mental  damage, and is compelled to howl as long as it takes  persistent mental damage.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/40']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/40', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/39', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/41']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/7/Text/39` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/7/Text/41` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/40` | 0.875303 | **Failure** The target takes full damage, persistent mental  damage, and is compelled to howl as long as it takes  persistent mental damage. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/32/Text/16` | 0.656194 | **Failure** The creature takes full damage and persistent damage. **Critical Failure** The creature takes double damage and double  persistent damage. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/41` | 0.637543 | **Critical Failure** As failure, but the target takes double the  initial and persistent damage. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/24/Text/10` | 0.627778 | **Failure** The creature takes full damage and is deafened for  1 round. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/21` | 0.627778 | **Failure** The creature takes full damage and is deafened for  1 round. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/20` | 0.626566 | **ENTHRALL **[two-actions] **SPELL 3**  **AUDITORY** **CONCENTRATE** **EMOTION** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet;** Targets** all creatures in range  **Defense** Will |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/25` | 0.625531 | **LAUGHING FIT **[two-actions] **SPELL 2**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 living creature  **Defense** Will;** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/39` | 0.619154 | **Success** The target takes half damage and no persistent  mental damage. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/34/Text/15` | 0.616299 | **Failure** The creature takes full damage. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/9` | 0.616299 | **Failure** The creature takes full damage. |

### Query 107
- Text: Summarize Cone of mental
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/497']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/497', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/496', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/498']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/496` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/498` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/497` | 0.696576 | Cone of mental (Will) |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/501` | 0.549193 | Cone of spirit (Will) |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/493` | 0.534056 | Cone of poison (Fortitude) |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/505` | 0.525689 | Cone of piercing (Reflex) |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/14` | 0.522235 | **Mindlink** Mentally impart 10 minutes' worth of information  in an instant. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/53` | 0.520940 | **Mindlink** Mentally impart 10 minutes worth of information  in an instant. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.520376 | insight about a topic. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/57` | 0.512246 | **Synaptic Pulse** Slow creatures with a mental blast. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/24` | 0.501964 | **Magic Passage**H, U Open a temporary passage through a surface. **Mind Probe**U Uncover knowledge and memories in a |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/60` | 0.498684 | **Mind Reading**U Read a creature's surface thoughts. |

### Query 108
- Text: What does **BATTLE SONATA **[two-actions] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/50', 'PZO22001 Starfinder Player Core 294-329::/page/24/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/23/Text/50` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/24/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/1` | 0.654106 | **BATTLE SONATA **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **SONIC**  **Traditions** divine, occult  **Area** 15-foot cone  **Defense** Will  This spell was composed by pahtra battle |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.587205 | SPELL ATTACKS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/17` | 0.577697 | OCCULT 4TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/32/Text/2` | 0.574566 | **SOUND BODY **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You send a su |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.573784 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/71` | 0.559794 | ARCANE 4TH-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.556791 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/3` | 0.550998 | **NIGHTMARE** **SPELL 4**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Cast** 10 minutes  **Range **planetary;** Targets** 1 creature you know by name  **D |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/29/SectionHeader/14` | 0.544268 | **SILENCE **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** divine, occult  **Range **touch;** Targets** 1 willing creature  **Duration** 1 minute  The target makes n |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/1` | 0.542688 | **DISPELLING GLOBE **[two-actions] **SPELL 4**  **UNCOMMON** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Area** 10-foot burst centered on one corner of your space **Durati |

### Query 109
- Text: What is the rule about Many spontaneous spellcasting classes provide abilities  like the signature spells class feature, which allows you to  cast a limited number of spells as heightened versions even if  you know the spell at only a single rank.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/6', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/5', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/6` | 0.899527 | Many spontaneous spellcasting classes provide abilities  like the signature spells class feature, which allows you to  cast a limited number of spells as heightened versions even if  you know the spel |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.680751 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.663938 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.663725 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.662453 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/28` | 0.644883 | If you have an innate spell, you can cast it even if it's not of  a spell rank you can normally cast. This is especially common  for monsters. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` | 0.633762 | As a spontaneous caster, you can also choose to cast  a lower-rank spell using a higher-rank spell slot without  heightening it or knowing it at a higher rank. This casts the  spell at the rank you kn |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.632761 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.631845 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.629949 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |

### Query 110
- Text: Summarize are determined by their connection, and a witchwarper's are  determined by their paradox.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/18', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/19` | 0.929260 | are determined by their connection, and a witchwarper's are  determined by their paradox. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/24` | 0.612300 | spells and precog warp spells, your mystic spells would  remain divine and the witchwarper spells occult. Similarly,  you need to use the attribute modifier determined by the  source of the focus spel |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.602315 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.602109 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/1` | 0.576365 | Whether it comes in the form of eldritch artifacts, otherworldly beings, or witchwarpers altering  reality with strange spells, magic brings fantasy and wonder to Starfinder. This chapter explains how |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/20` | 0.567149 | You spend 10 minutes performing deeds to restore your  magical connection. This restores 1 Focus Point to your focus  pool. The deeds you need to perform are specified in the class  or ability that gi |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.567032 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/29/ListItem/4` | 0.561895 | **Weal** **and** **Woe** The results will be a mix of good and  bad. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/4` | 0.561447 | Spellcasting creates obvious sensory manifestations, such  as bright lights, crackling sounds, and sharp smells from the  gathering magic. Nearly all spells manifest a spell signature—a  colorful, glo |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.557981 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |

### Query 111
- Text: What is the rule about If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single rank so that you have more options when casting it.  For example, if you added *skyfire wings* to your repertoire as  a 3rd-rank spell and again as a 7th-rank spell, you could cast  it as a 3rd-rank or a 7th-rank spell; however, you couldn't cast  it as a 5th-rank spell.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/5', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.959828 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` | 0.746132 | As a spontaneous caster, you can also choose to cast  a lower-rank spell using a higher-rank spell slot without  heightening it or knowing it at a higher rank. This casts the  spell at the rank you kn |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.735139 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.732317 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.717242 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.703798 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.678460 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.677873 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.676756 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/6` | 0.675117 | Many spontaneous spellcasting classes provide abilities  like the signature spells class feature, which allows you to  cast a limited number of spells as heightened versions even if  you know the spel |

### Query 112
- Text: What is the rule about **Heightened (+1)** The void damage increases by 2d4, and the  persistent bleed damage increases by 1.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/11', 'PZO22001 Starfinder Player Core 330-363::/page/5/Text/10', 'PZO22001 Starfinder Player Core 330-363::/page/5/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/5/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/5/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/11` | 0.910064 | **Heightened (+1)** The void damage increases by 2d4, and the  persistent bleed damage increases by 1. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/54` | 0.803548 | **Heightened (+1)** The damage increases by 2d4. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/32/Text/17` | 0.799475 | **Heightened (+1)** The damage increases by 1d6 and persistent  damage increases by 1d6. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/34/Text/17` | 0.781695 | **Heightened (+1)** The cold damage increases by 1d10 and the  void damage against the living increases by 1d4. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/34/Text/37` | 0.766207 | **Heightened (+1)** The damage increases by 1d12. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/23` | 0.765981 | **Heightened (+1)** The damage increases by 1d10. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/32/Text/43` | 0.765981 | **Heightened (+1)** The damage increases by 1d10. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/24/Text/12` | 0.765981 | **Heightened (+1)** The damage increases by 1d10. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/2` | 0.760938 | **Heightened (+1)** The damage increases by 1d6. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/27` | 0.757139 | **Heightened (+2)** The initial damage increases by 2d8, and the  persistent acid damage increases by 1d6. |

### Query 113
- Text: What does **CONFUSION **[two-actions] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/28/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/28/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.707882 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.619857 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.611133 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.605673 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/18/SectionHeader/45` | 0.595692 | **OUTCAST'S CURSE **[two-actions] **SPELL 4**  **CONCENTRATE** **CURSE** **MANIPULATE** **MENTAL** **MISFORTUNE**  **Traditions** arcane, divine, occult **Range **touch;** Targets** 1 creature  **Defe |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/12` | 0.591485 | **HALLUCINATION **[two-actions] **SPELL 5**  **ILLUSION** **INCAPACITATION** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** 1 creature  **Duration* |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/32` | 0.588972 | **PHANTASMAGORIA **[two-actions] **SPELL 9**  **CONCENTRATE** **DEATH** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **120 feet; **Targets** any number of creatures |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/39` | 0.588514 | **SUBCONSCIOUS SUGGESTION **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **LINGUISTIC** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet;** Targe |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/17` | 0.580514 | OCCULT 4TH-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/56` | 0.579462 | **ILLUSORY CREATURE**[two-actions] **SPELL 2**  **AUDITORY** **CONCENTRATE** **ILLUSION** **MANIPULATE** **OLFACTORY** **VISUAL**  **Traditions** arcane, occult  **Range **500 feet  **Duration** susta |

### Query 114
- Text: What does **CLAIRAUDIENCE** **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/24']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/24', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/31']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/24` | 0.638953 | **CLAIRAUDIENCE** **SPELL 3**  **CONCENTRATE** **MANIPULATE** **SCRYING**  **Traditions** arcane, occult  **Cast** 1 minute **Range **500 feet  **Duration** 10 minutes  You create an invisible floatin |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.621823 | **LIFE SEAL **[reaction] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/62` | 0.609142 | OCCULT 3RD-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.600201 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/65` | 0.580175 | **Clairaudience** Hear through an invisible magical sensor. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/45` | 0.580175 | **Clairaudience** Hear through an invisible magical sensor. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/42` | 0.571414 | ARCANE 3RD-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/20` | 0.567569 | **ENTHRALL **[two-actions] **SPELL 3**  **AUDITORY** **CONCENTRATE** **EMOTION** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet;** Targets** all creatures in range  **Defense** Will |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/22` | 0.564789 | DIVINE 3RD-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/49` | 0.562582 | PRIMAL 3RD-RANK SPELLS |

### Query 115
- Text: What does **FALSE VISION** **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/52']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/52', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/61', 'PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/44']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/61` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/44` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/52` | 0.677128 | **FALSE VISION** **SPELL 5**  **UNCOMMON** **CONCENTRATE** **ILLUSION** **MANIPULATE**  **Traditions** arcane, occult  **Cast** 10 minutes  **Range **touch;** Area** 100-foot burst  **Duration** until |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/40` | 0.597452 | OCCULT 5TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/12` | 0.591161 | **HALLUCINATION **[two-actions] **SPELL 5**  **ILLUSION** **INCAPACITATION** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** 1 creature  **Duration* |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/50` | 0.590826 | **SUBJECTIVE REALITY **[one-action] **SPELL 5**  **CONCENTRATE** **MANIPULATE**  **Traditions** occult  **Range **500 feet;** Targets** 1 creature or object  **Duration** sustained up to 1 minute  You |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/45` | 0.578551 | **False Vision**U Trick a scrying spell. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/19` | 0.578551 | **False Vision**U Trick a scrying spell. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/54` | 0.570051 | DIVINE 5TH-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/15` | 0.567657 | ARCANE 5TH-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/3` | 0.566796 | **SCOUTING EYE** **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SCRYING**  **Traditions** arcane, divine, occult  **Cast** 1 minute **Range **see text **Duration** sustained  You create an invisible, f |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/7` | 0.562093 | PRIMAL 5TH-RANK SPELLS |

### Query 116
- Text: What does **CREATE WATER **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/29/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/29/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/9` | 0.732075 | **CREATE WATER **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **WATER**  **Traditions** arcane, divine, primal  **Range **0 feet |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47` | 0.604891 | **CLEANSE CUISINE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** divine, primal  **Range **10 feet;** Area** 1 cubic foot  You transform all food and beverages in the area |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/12` | 0.596543 | **GREASE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet;** Area** 4 contiguous 5-foot squares or** Targets** 1  object of 1 Bulk or less |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.589812 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.588668 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/5` | 0.588429 | **HYDRAULIC PUSH **[two-actions] **SPELL 1**  **ATTACK** **CONCENTRATE** **MANIPULATE** **WATER**  **Traditions** arcane, primal  **Range **60 feet;** Targets** 1 creature or unattended object **Defen |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.582712 | SPELL ATTACKS |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.580639 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/31/SectionHeader/22` | 0.580303 | **SOOTHE **[two-actions] **SPELL 1**  **CONCENTRATE** **EMOTION** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** occult  **Range **30 feet;** Targets** 1 willing creature  **Duration** 1 minute |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/19` | 0.577623 | **ILLUSORY OBJECT **[two-actions] **SPELL 1**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **VISUAL**  **Traditions** arcane, occult  **Range **500 feet;** Area** 20-foot burst  **Duration** 10 minute |

### Query 117
- Text: What does **ANIMAL FORM **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/21/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/21/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41', 'PZO22001 Starfinder Player Core 294-329::/page/21/ListItem/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/21/ListItem/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/21/SectionHeader/4` | 0.648918 | **ANIMAL FORM **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** primal  **Duration** 1 minute  You call upon primal energy to transform yourself into a  Medium |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/60` | 0.625740 | **PEST FORM **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Duration** 10 minutes |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.616775 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/36` | 0.607123 | **AERIAL FORM **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Duration** 1 minute  You harness your mastery of the sky to reshape your body |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/10` | 0.605250 | **INSECT FORM **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Duration** 1 minute  You envision a simple bug and transform into a Medium  an |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.601267 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47` | 0.587478 | **REVIVAL **[two-actions] **SPELL 10**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet;** Targets** dead creatures and living creatures of  y |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/56` | 0.585437 | **ILLUSORY CREATURE**[two-actions] **SPELL 2**  **AUDITORY** **CONCENTRATE** **ILLUSION** **MANIPULATE** **OLFACTORY** **VISUAL**  **Traditions** arcane, occult  **Range **500 feet  **Duration** susta |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/18` | 0.582521 | **FELINE SENSES **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MORPH**  **Traditions** divine, primal  **Duration** 1 hour |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/11` | 0.582182 | **STATUS **[two-actions] **SPELL 2**  **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch;** Targets** 1 willing living creature  **Duration** until yo |

### Query 118
- Text: What is the rule about **Critical Failure** The creature takes double damage, is slowed  3 until the end of its next turn, and slowed 2 for 1 minute.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/5', 'PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/6', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/5` | 0.852843 | **Critical Failure** The creature takes double damage, is slowed  3 until the end of its next turn, and slowed 2 for 1 minute. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/4` | 0.778764 | **Failure** The creature takes full damage, is slowed 3 until the  end of its next turn, and slowed 1 for 1 minute. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/22` | 0.755281 | **Critical Failure** The creature takes double damage, is  deafened for 1 minute, and is stunned 1. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/32/Text/42` | 0.754034 | **Critical Failure** The creature takes full damage and is sickened  2; while it's sickened, it's also slowed 1. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/13` | 0.739436 | **Failure** The creature takes full damage and is slowed 1 until the  start of your next turn. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/20` | 0.739436 | **Failure** The creature takes full damage and is slowed 1 until  the start of your next turn. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/33` | 0.739214 | **Critical Failure** The creature takes full damage and is clumsy  2 for 1 minute. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/24/Text/11` | 0.736223 | **Critical** **Failure** The creature takes double damage, is  deafened for 1 minute, and becomes stunned 1. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/3` | 0.723533 | **Success** The creature takes half damage and is slowed 1 until  the end of its next turn. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/53` | 0.712994 | **Critical Failure** The creature takes double damage and is  pushed 10 feet away from you. |

### Query 119
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/74']
- Expected found: `True`
- Expected rank: `8`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/74', 'PZO22001 Starfinder Player Core 330-363::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/73']
- Expanded expected found: `True`
- Expanded expected rank: `8`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/2/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/73` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/71` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/50` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/32` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/33` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/68` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/69` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/43` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/74` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/72` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/67` | 0.879439 | **GLOSSARY & ** **INDEX** |

### Query 120
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/25']
- Expected found: `True`
- Expected rank: `15`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/25', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/24', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `15`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/63` | 0.865652 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/59` | 0.865652 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/60` | 0.865652 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/35` | 0.865652 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/64` | 0.865652 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/58` | 0.865652 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/67` | 0.865652 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/67` | 0.865652 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/66` | 0.865652 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/79` | 0.865652 | **EQUIPMENT** |

### Query 121
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/60']
- Expected found: `True`
- Expected rank: `11`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/60', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/59', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/61']
- Expanded expected found: `True`
- Expanded expected rank: `11`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/3/Text/59` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/63` | 0.865652 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/59` | 0.865652 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/60` | 0.865652 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/35` | 0.865652 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/64` | 0.865652 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/58` | 0.865652 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/67` | 0.865652 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/67` | 0.865652 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/66` | 0.865652 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/79` | 0.865652 | **EQUIPMENT** |

### Query 122
- Text: What does **FALLING STARS **[two-actions] **SPELL 9** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/44']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/44', 'PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/52', 'PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/32']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/52` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/32` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/44` | 0.688832 | **FALLING STARS **[two-actions] **SPELL 9**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Area** four 40-foot bursts  **Defense** basic Reflex  You reach into t |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/24` | 0.627733 | OCCULT 9TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/56` | 0.603514 | PRIMAL 9TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/11` | 0.593785 | ARCANE 9TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.590695 | SPELL ATTACKS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/28` | 0.589366 | DIVINE 9TH-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4` | 0.587808 | **CALL COSMOS **[two-actions] **SPELL 9**  **COLD** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** divine, primal  **Range **500 feet;** Area** 20-foot radius, 40-foot tall cylinder **Defense |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/32` | 0.586057 | **PHANTASMAGORIA **[two-actions] **SPELL 9**  **CONCENTRATE** **DEATH** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **120 feet; **Targets** any number of creatures |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/23` | 0.572322 | **ATOMIC BLAST **[three-actions] **SPELL 9**  **CONCENTRATE** **FIRE** **MANIPULATE** **RADIATION**  **Traditions** arcane, primal  **Range **500 feet;** Area** 100-foot burst **Defense** Reflex; **Du |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/10/SectionHeader/25` | 0.570819 | **IMPLOSION **[two-actions] **SPELL 9**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet;** Targets** 1 corporeal creature  **Defense** basic Fortitude; **Duration** s |

### Query 123
- Text: What does **CAUSTIC BLAST **[two-actions] **CANTRIP 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19', 'PZO22001 Starfinder Player Core 294-329::/page/26/ListItem/18', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/26/ListItem/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19` | 0.714380 | **CAUSTIC BLAST **[two-actions] **CANTRIP 1**  **ACID** **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Area** 5-foot burst  **Defense** basic Reflex  Y |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/5` | 0.611944 | **STABILIZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet; **Targets** 1 dying creature  Life ene |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/24` | 0.598890 | **DIVINE LANCE **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE** **SANCTIFIED** **SPIRIT**  **Traditions** divine  **Range **60 feet; **Targets** 1 creature  **Defen |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/3` | 0.591694 | **INJURY ECHO **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **60 feet; **Targets** 1 creature  **Defense** Will  You manifest an inj |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/13` | 0.584496 | **NOISE BLAST **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SONIC**  **Traditions** arcane, divine, occult **Range **30 feet;** Area** 10-foot burst  **Defense** Fortitude  A cacophono |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/38` | 0.582188 | **ELECTRIC ARC **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **ELECTRICITY** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Targets** 1 or 2 creatures  **Defense** ba |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/2` | 0.577864 | **DAZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE** **MENTAL** **NONLETHAL**  **Traditions** arcane, divine, occult **Range **60 feet; **Targets** 1 creature **Defense** W |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41` | 0.576325 | **ANALYZE TARGET **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **30 feet; **Targets** 1 creature  **Dur |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/19` | 0.575087 | **STUMBLE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **100 feet; **Targets** 1 creature  **Defense** Reflex  A burst of micrograv |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/11` | 0.573070 | **FORBIDDING WARD **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** divine, occult  **Range **30 feet; **Targets** 1 ally and 1 enemy  **Duration** sustained up |

### Query 124
- Text: What does **CALL COSMOS **[two-actions] **SPELL 9** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70', 'PZO22001 Starfinder Player Core 294-329::/page/25/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/25/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4` | 0.667823 | **CALL COSMOS **[two-actions] **SPELL 9**  **COLD** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** divine, primal  **Range **500 feet;** Area** 20-foot radius, 40-foot tall cylinder **Defense |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/24` | 0.622257 | OCCULT 9TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/28` | 0.583766 | DIVINE 9TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/56` | 0.581609 | PRIMAL 9TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/11` | 0.580810 | ARCANE 9TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.566735 | CHAPTER 7: SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/18/Text/58` | 0.557811 | **Call** **Cosmos**H Call down a column of cosmic matter to burn  and freeze. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/29` | 0.557811 | **Call** **Cosmos**H Call down a column of cosmic matter to burn  and freeze. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.556242 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.555811 | SPELL ATTACKS |

### Query 125
- Text: What is the rule about **Spell Lists**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/25']
- Expected found: `True`
- Expected rank: `2`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/25', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/24', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/87` | 0.732608 | **Spell Lists** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/25` | 0.732608 | **Spell Lists** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/60` | 0.732608 | **Spell Lists** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/69` | 0.732608 | **Spell Lists** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/44` | 0.732608 | **Spell Lists** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/69` | 0.732608 | **Spell Lists** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/75` | 0.732608 | **Spell Lists** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/62` | 0.732608 | **Spell Lists** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/84` | 0.732608 | **Spell Lists** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/61` | 0.732608 | **Spell Lists** |

### Query 126
- Text: What is the rule about The illusion can cause damage by making the target believe  the illusion's attacks are real, but it cannot otherwise directly  affect the physical world. If the illusory creature hits with a  Strike, the target takes 3d4 mental damage. The illusion's  Strikes are nonlethal. If the damage doesn't correspond to  the image of the monster—for example, if an illusory Large  dragon deals only 5 damage—the GM might allow the target  to attempt an immediate Perception check to disbelieve the  spell. Any relevant resistances and weaknesses apply if the  target thinks they do, as judged by the GM. For example, if  the illusion wields a doshko and attacks a creature resistant to  piercing damage, the creature would take less mental damage.  However, illusory damage does not deactivate regeneration or  trigger other effects that require a certain damage type. The  GM should track illusory damage dealt by the illusion.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/4', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/5', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/9/Text/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/9/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/4` | 0.965823 | The illusion can cause damage by making the target believe  the illusion's attacks are real, but it cannot otherwise directly  affect the physical world. If the illusory creature hits with a  Strike, |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/17` | 0.723139 | Magic with the illusion trait creates false sensory stimuli.  Sometimes illusions allow creatures a chance to disbelieve  the spell, which lets the creature ignore the spell if it succeeds  at doing s |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/5` | 0.712420 | Any creature that touches the image or uses the Seek  action to examine it can attempt to disbelieve your illusion.  When a creature disbelieves the illusion, it recovers from half  the damage it had |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/10/Text/2` | 0.654026 | Any creature that touches any part of the image or uses  the Seek action to examine it can attempt to disbelieve  your illusion. If they interact with a portion of the illusion,  they disbelieve only |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/18` | 0.648790 | If a creature engages with an illusion in a way that would  prove it's not what it seems, the creature might know that an  illusion is present, but it still can't ignore the illusion without  successf |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/21` | 0.643709 | Some spells allow you to target a creature, an object, or  something more specific. The target must be within the  spell's range, and you must be able to see it (or otherwise  perceive it with a preci |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/3` | 0.634242 | In combat, the illusion can use 2 actions per turn, which  it uses when you Sustain the spell. It uses your spell attack  modifier for attack rolls and your spell DC for its AC. Its  saving throw modi |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/1` | 0.633852 | Illusions bend light around the target, rendering it  invisible. This makes it undetected to all creatures, though  the creatures can attempt to find the target, making it  hidden to them instead (pag |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/7` | 0.626943 | **ILLUSORY DISGUISE **[two-actions] **SPELL 1**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **VISUAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 willing creature  **Duration** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/21/SectionHeader/8` | 0.626498 | **PHANTOM PAIN **[two-actions] **SPELL 1**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL** **NONLETHAL**  **Traditions** occult  **Range **30 feet; **Targets** 1 creature **Defense** Will; **D |

### Query 127
- Text: Summarize **CONDITIONS **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/30']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/31', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/30` | 0.830718 | **CONDITIONS ** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/68` | 0.830718 | **CONDITIONS ** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/74` | 0.830718 | **CONDITIONS ** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/75` | 0.830718 | **CONDITIONS ** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/67` | 0.830718 | **CONDITIONS ** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/50` | 0.830718 | **CONDITIONS ** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/65` | 0.779096 | **GAME** **CONDITIONS ** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/73` | 0.743212 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/39` | 0.743212 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/66` | 0.743212 | **CONDITIONS ** **APPENDIX** |

### Query 128
- Text: What is the rule about A cantrip is a special type of spell that's weaker than other  spells but can be used with greater freedom and flexibility.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/9', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/8', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/9` | 0.901696 | A cantrip is a special type of spell that's weaker than other  spells but can be used with greater freedom and flexibility. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 0.646548 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` | 0.629512 | The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any nu |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/2` | 0.597731 | These lists include the spells for each tradition, including cantrips. (Focus spells appear on pages 375–380.)  A superscript "H" indicates a spell has extra effects when heightened, and a spell whose |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 0.593791 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.590506 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/17` | 0.583812 | Each spell uses the following format. Entries appear only  when applicable, so not all spells will have every entry  described here. The spell's name line also lists the type  of spell if it's a cantr |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` | 0.570366 | Focus spells are automatically heightened to half your level  rounded up, just like cantrips are. You can't cast a focus spell  if its minimum rank is greater than half your level rounded  up, even if |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/2` | 0.568865 | In rare cases, a spell might have you make some other  type of attack, such as a weapon Strike. Such attacks use the  normal rules and attack bonus for that type of attack. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.564526 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |

### Query 129
- Text: Summarize Cone of poison
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/493']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/493', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/492', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/494']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/492` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/494` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/493` | 0.691636 | Cone of poison (Fortitude) |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/505` | 0.552215 | Cone of piercing (Reflex) |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/22/ListItem/23` | 0.550256 | Resistance 10 to poison. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/18/Text/20` | 0.542474 | **Toxic Cloud**H A bank of poison fog rolls away from you. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/30` | 0.542474 | **Toxic Cloud**H A bank of poison fog rolls away from you. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/51` | 0.537307 | **Shadow Blast**H Shape a damaging cone of shadow substance  to deal damage of a type you choose. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/60` | 0.537307 | **Shadow Blast**H Shape a damaging cone of shadow substance  to deal damage of a type you choose. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/497` | 0.535718 | Cone of mental (Will) |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/9` | 0.532602 | **Pummeling Rubble**H Hurl a cone of rocks to batter creatures. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/11/ListItem/28` | 0.506819 | piercing plus 1d4 persistent poison; **Melee **[one-action] pincer  (agile), **Damage **1d6 bludgeoning. |

### Query 130
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/58']
- Expected found: `True`
- Expected rank: `19`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/58', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/57', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/59']
- Expanded expected found: `True`
- Expanded expected rank: `19`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/7/Text/57` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/7/Text/59` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/63` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/56` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/60` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/31` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/55` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/63` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/81` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/40` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/78` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/59` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 131
- Text: What does **ANALYZE TARGET **[two-actions] **CANTRIP 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41', 'PZO22001 Starfinder Player Core 294-329::/page/20/Text/33', 'PZO22001 Starfinder Player Core 294-329::/page/21/SectionHeader/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/20/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/21/SectionHeader/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41` | 0.688168 | **ANALYZE TARGET **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **30 feet; **Targets** 1 creature  **Dur |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/5` | 0.653994 | **STABILIZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet; **Targets** 1 dying creature  Life ene |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/11` | 0.600099 | **FORBIDDING WARD **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** divine, occult  **Range **30 feet; **Targets** 1 ally and 1 enemy  **Duration** sustained up |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28` | 0.596691 | **ADHERE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Range **touch; **Targets** 1 held or unattended object or a 5-footsquare sur |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/2` | 0.596444 | **DAZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE** **MENTAL** **NONLETHAL**  **Traditions** arcane, divine, occult **Range **60 feet; **Targets** 1 creature **Defense** W |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/3` | 0.596354 | **INJURY ECHO **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **60 feet; **Targets** 1 creature  **Defense** Will  You manifest an inj |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20` | 0.594494 | TARGETS |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/5/SectionHeader/20` | 0.592077 | **GUIDANCE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE**  **Traditions** divine, occult, primal  **Range **30 feet; **Targets** 1 creature  **Duration** until the start of your next turn |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19` | 0.590437 | **CAUSTIC BLAST **[two-actions] **CANTRIP 1**  **ACID** **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Area** 5-foot burst  **Defense** basic Reflex  Y |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/24` | 0.589308 | **DIVINE LANCE **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE** **SANCTIFIED** **SPIRIT**  **Traditions** divine  **Range **60 feet; **Targets** 1 creature  **Defen |

### Query 132
- Text: Lookup values for DragonTraditionSpeedsDragon BreathAbysiumArcane—Cone of poison
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/Table/3']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/Table/3', 'PZO22001 Starfinder Player Core 330-363::/page/0/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/486']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/0/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/486` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/Table/3` | 0.798179 | DragonTraditionSpeedsDragon BreathAbysiumArcane—Cone of poison (Fortitude)AkashicOccult—Cone of mental (Will)CosmicDivine—Cone of spirit (Will)HostPrimalClimbCone of piercing (Reflex) |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/493` | 0.610268 | Cone of poison (Fortitude) |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/19` | 0.597137 | **Dragon Breath**[two-actions] You exhale deadly magical energy  in an area, dealing 10d6 damage to each creature in  the area with a basic save against your spell DC. The  shape, damage type, and sav |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/14` | 0.592481 | Resistance 10 against the damage type of your Dragon  Breath (see below). |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/20` | 0.584664 | **Tradition Resistance** If the dragon's magical tradition  matches that of your *dragon form* spell, you gain the  listed ability. **Arcane** resistance 5 against damage from  spells; **divine** resi |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/21/ListItem/25` | 0.569426 | **Snake** Speed 20 feet, climb 20 feet, swim 20 feet; **Melee ** [one-action] fangs, **Damage **2d4 piercing plus 1d6 poison. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/489` | 0.566534 | Dragon Breath |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/13` | 0.566383 | Speed 40 feet, fly 100 feet. You gain any of the following  Speeds the chosen dragon has, but with the listed  amount: burrow 20 feet, climb 40 feet, swim 60 feet. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/23/ListItem/11` | 0.563752 | **Oras **Speed 50 feet, burrow 30 feet, fly 50 feet, swim  50 feet; **Melee **[one-action] tentacle (agile, finesse, reach 20  feet, versatile S), **Damage **6d6 bludgeoning; **Ranged ** [one-action] |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/11/ListItem/25` | 0.548117 | **Centipede** Speed 25 feet, climb 25 feet; darkvision;  **Melee **[one-action] mandibles, **Damage **1d8 piercing plus 1d4  persistent poison. |

### Query 133
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/72']
- Expected found: `True`
- Expected rank: `18`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/72', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/71', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/73']
- Expanded expected found: `True`
- Expanded expected rank: `18`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/71` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/73` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/29` | 0.888833 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/85` | 0.888833 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/91` | 0.888833 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/79` | 0.888833 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/64` | 0.888833 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/70` | 0.888833 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/88` | 0.888833 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/65` | 0.888833 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/67` | 0.888833 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/48` | 0.888833 | **PLAYING THE ** **GAME** |

### Query 134
- Text: What does **GRIM TENDRILS **[two-actions] **SPELL 1** **CONCENTRATE** **MANIPULATE** **VOID** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/2']
- Expected found: `True`
- Expected rank: `2`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/5/Text/7', 'PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/46']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/5/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/46` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` | 0.629686 | **CONCENTRATE** **MANIPULATE** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/2` | 0.614411 | **GRIM TENDRILS **[two-actions] **SPELL 1** **CONCENTRATE** **MANIPULATE** **VOID**  **Traditions** arcane, occult  **Area** 30-foot line  **Defense** Fortitude  Tendrils of darkness curl out from you |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.613684 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/47` | 0.593813 | **DISPEL MAGIC **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **120 feet;** Targets** 1 spell effect or unattended magic  item  You |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/26` | 0.592399 | **HARM **[one-action]** TO **[three-actions] **SPELL 1**  **MANIPULATE** **VOID**  **Traditions** divine  **Range **varies; **Targets** 1 living creature or 1 willing undead  creature  You channel voi |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.587296 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47` | 0.585422 | **BLUR **[two-actions] **SPELL 2**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **VISUAL**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 1 minute  The target's |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/12` | 0.583667 | **EXECUTE **[two-actions] **SPELL 7**  **CONCENTRATE** **DEATH** **MANIPULATE** **VOID**  **Traditions** divine, primal  **Range **30 feet; **Targets** 1 creature  **Defense** basic Fortitude  You poi |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/26/SectionHeader/39` | 0.583579 | **SANCTUARY **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** divine, occult  **Range **touch;** Targets** 1 creature  **Duration** 1 minute  You ward a creature with protect |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.583288 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |

### Query 135
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/68']
- Expected found: `True`
- Expected rank: `5`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/68', 'PZO22001 Starfinder Player Core 330-363::/page/4/Text/1', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/67']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/4/Text/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/3/Text/67` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/71` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/50` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/32` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/33` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/68` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/69` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/43` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/74` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/72` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/67` | 0.879439 | **GLOSSARY & ** **INDEX** |

### Query 136
- Text: Summarize Cone of spirit (Will)
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/501']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/501', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/500', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/502']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/500` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/502` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/501` | 0.868859 | Cone of spirit (Will) |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/497` | 0.807609 | Cone of mental (Will) |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/493` | 0.593084 | Cone of poison (Fortitude) |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/36` | 0.591438 | **Defense** Will |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/20/Text/10` | 0.533667 | **AC **13; **Fort **+0, **Ref **+4, **Will **+0 |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/44` | 0.527177 | **DIZZYING COLORS **[two-actions] **SPELL 1**  **CONCENTRATE** **ILLUSION** **INCAPACITATION** **MANIPULATE** **VISUAL**  **Traditions** arcane, occult  **Area** 15-foot cone  **Defense** Will; **Dura |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/29/ListItem/2` | 0.516293 | **Weal** The results will be good. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/505` | 0.514065 | Cone of piercing (Reflex) |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/17/SectionHeader/14` | 0.502836 | **NEVER MIND **[two-actions] **SPELL 6**  **CONCENTRATE** **CURSE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature **Defense** W |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/22/SectionHeader/37` | 0.500383 | **POSSESSION **[two-actions] **SPELL 7**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL** **POSSESSION**  **Traditions** occult  **Range **30 feet; **Targets** 1 living creat |

### Query 137
- Text: What is the rule about **SKILLS** **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/60']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/60', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/61', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/59']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/7/Text/61` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/7/Text/59` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/60` | 0.773624 | **SKILLS** **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/65` | 0.653015 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/62` | 0.653015 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/57` | 0.653015 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/61` | 0.653015 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/58` | 0.653015 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/71` | 0.653015 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/60` | 0.653015 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/58` | 0.653015 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/69` | 0.653015 | **SKILLS** |

### Query 138
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/28']
- Expected found: `True`
- Expected rank: `4`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/28', 'PZO22001 Starfinder Player Core 330-363::/page/5/Text/29', 'PZO22001 Starfinder Player Core 330-363::/page/5/SectionHeader/20']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/5/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/5/SectionHeader/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/18` | 0.863367 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/55` | 0.863367 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/28` | 0.863367 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/28` | 0.863367 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/61` | 0.863367 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/62` | 0.863367 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/57` | 0.863367 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/55` | 0.863367 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/39` | 0.863367 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/20` | 0.863367 | **INTRODUCTION** |

### Query 139
- Text: What is the rule about systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/15', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.871515 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.581763 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/19` | 0.563198 | are determined by their connection, and a witchwarper's are  determined by their paradox. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/24` | 0.536036 | spells and precog warp spells, your mystic spells would  remain divine and the witchwarper spells occult. Similarly,  you need to use the attribute modifier determined by the  source of the focus spel |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.523566 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/14` | 0.518327 | The practitioners of occult traditions seek  to understand the unexplainable, categorize  the bizarre, and otherwise access the ephemeral in a |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.517955 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.507654 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/2` | 0.498094 | Spellcasters cast spells from one of four different spell lists, each representing a different magical tradition: arcane,  divine, occult, and primal. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/21` | 0.492585 | **AKASHIC REVIVAL** **SPELL 8**  **CONCENTRATE** **MANIPULATE**  **Traditions** occult **Cast** 10 minutes  **Range** touch; **Targets** 1 willing creature  **Duration** 1 day  You dispatch perfect do |

### Query 140
- Text: What does **CLEAR MIND **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47', 'PZO22001 Starfinder Player Core 294-329::/page/27/Text/62']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/27/Text/62` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` | 0.696473 | **CLEAR MIND **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You drive menta |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/17/SectionHeader/14` | 0.618185 | **NEVER MIND **[two-actions] **SPELL 6**  **CONCENTRATE** **CURSE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature **Defense** W |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.607627 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/32/Text/2` | 0.600477 | **SOUND BODY **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You send a su |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/29` | 0.597108 | **STUPEFY **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** varies  You du |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/15/SectionHeader/3` | 0.587843 | **MIND READING **[two-actions] **SPELL 3**  **UNCOMMON** **CONCENTRATE** **DETECTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature  **Defense** W |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/39` | 0.581673 | **SUBCONSCIOUS SUGGESTION **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **LINGUISTIC** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet;** Targe |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/11` | 0.579656 | **STATUS **[two-actions] **SPELL 2**  **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch;** Targets** 1 willing living creature  **Duration** until yo |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/32/SectionHeader/56` | 0.578311 | **SPIRITUAL ARMAMENT **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SANCTIFIED** **SPIRIT**  **Traditions** divine, occult  **Range **120 feet; **Targets** 1 creature  **Defense** AC; * |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/5` | 0.577303 | **DETECT THOUGHTS **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult **Area** 30-foot emanation  **Defense** Will  You sense the presence of thinking |

### Query 141
- Text: What is the rule about Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to cosmic forces, and  others rewrite the underlying code of the universe to cast  their spells.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/1', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` | 0.919672 | Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.684450 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` | 0.676869 | With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own met |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/1` | 0.636304 | Whether it comes in the form of eldritch artifacts, otherworldly beings, or witchwarpers altering  reality with strange spells, magic brings fantasy and wonder to Starfinder. This chapter explains how |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/2` | 0.636256 | The grand variety of spells includes those in the following pages and far more. Taught at magical  academies, drawn from other worlds, bestowed by mystical connections, and granted by all manner of  u |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.629051 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/3` | 0.627440 | The casting of a spell can range from a simple word of magical  might that creates a fleeting effect to a complex process  taking hours to cast and producing a long-term impact.  Casting a spell requi |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/12` | 0.622023 | After Triune's Signal connected cultures across the  Universe, the peoples of the galaxy have learned more  than ever before about the Universe's composition  thanks to science and technology. As tech |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/4` | 0.617724 | Spellcasting creates obvious sensory manifestations, such  as bright lights, crackling sounds, and sharp smells from the  gathering magic. Nearly all spells manifest a spell signature—a  colorful, glo |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.614487 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |

### Query 142
- Text: Summarize **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/31', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/31` | 0.879192 | **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/75` | 0.879192 | **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/66` | 0.879192 | **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/76` | 0.879192 | **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/51` | 0.879192 | **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/68` | 0.778418 | **APPENDIX** **GLOSSARY & ** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/69` | 0.778418 | **APPENDIX** **GLOSSARY & ** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/68` | 0.774459 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/32` | 0.774459 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/67` | 0.774459 | **CONDITIONS ** **APPENDIX** |

### Query 143
- Text: What does **Traditions** arcane, divine, occult, primal do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/6', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/7', 'PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/3/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/6` | 0.833139 | **Traditions** arcane, divine, occult, primal |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/34` | 0.781278 | **Traditions** divine, occult, primal |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/45` | 0.742184 | **Traditions** divine, primal |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/24` | 0.629226 | **Traditions** occult |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.601981 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1` | 0.598159 | **MAGICAL TRADITIONS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/13/SectionHeader/43` | 0.583082 | **MANIFESTATION **[three-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  You spin secrets from the fundaments of magic, shaping them  into a power |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/2` | 0.572021 | Spellcasters cast spells from one of four different spell lists, each representing a different magical tradition: arcane,  divine, occult, and primal. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/14` | 0.569315 | The practitioners of occult traditions seek  to understand the unexplainable, categorize  the bizarre, and otherwise access the ephemeral in a |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/20` | 0.557280 | **Tradition Resistance** If the dragon's magical tradition  matches that of your *dragon form* spell, you gain the  listed ability. **Arcane** resistance 5 against damage from  spells; **divine** resi |

### Query 144
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/73']
- Expected found: `True`
- Expected rank: `6`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/73', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/74', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/72']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/74` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/72` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/70` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/67` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/92` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/42` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/68` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/73` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/71` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/71` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/32` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/66` | 0.900802 | **CONDITIONS ** **APPENDIX** |

### Query 145
- Text: Summarize **Polymorph**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/13` | 0.836981 | **Polymorph** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/3` | 0.610740 | **SPELLSHAPE** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.610083 | **Summoned** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/11` | 0.603521 | **Morph** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.553675 | **SUBTLE SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/79` | 0.545185 | **GAME** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/70` | 0.545185 | **GAME** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` | 0.543844 | **CONCENTRATE** **MANIPULATE** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.539735 | **CONCENTRATE** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/44` | 0.539735 | **CONCENTRATE** |

### Query 146
- Text: What does **ENLARGE **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/Text/4']
- Expected found: `True`
- Expected rank: `5`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/Text/4', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/505', 'PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/13']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/505` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.622139 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/11` | 0.606844 | **STATUS **[two-actions] **SPELL 2**  **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch;** Targets** 1 willing living creature  **Duration** until yo |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.603471 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.600836 | SPELL ATTACKS |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/4` | 0.587213 | **ENLARGE **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Range **30 feet;** Targets** 1 willing creature  **Duration** 5 minutes  Bolstered |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/35/SectionHeader/14` | 0.586440 | **EMBED MESSAGE **[two-actions] **SPELL 2**  **CONCENTRATE** **ILLUSION** **MANIPULATE**  **Traditions** arcane, occult  **Range **touch; **Targets** 1 object or willing creature  **Duration** unlimit |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/32/Text/2` | 0.584988 | **SOUND BODY **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You send a su |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/17` | 0.583010 | **KNOCK **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 door, lock, or container  **Duration** 1 minute  You make the targe |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15` | 0.581114 | HEIGHTENED SPELLS |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/37` | 0.580385 | **REVEALING LIGHT **[two-actions] **SPELL 2**  **CONCENTRATE** **LIGHT** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **120 feet;** Area** 10-foot burst  **Defense** Reflex; * |

### Query 147
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/42']
- Expected found: `True`
- Expected rank: `4`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/42', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/41', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/43']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/41` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/43` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/70` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/67` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/92` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/42` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/68` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/73` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/71` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/71` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/32` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/66` | 0.900802 | **CONDITIONS ** **APPENDIX** |

### Query 148
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/62']
- Expected found: `True`
- Expected rank: `15`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/62', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/61', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/63']
- Expanded expected found: `True`
- Expanded expected rank: `15`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/7/Text/61` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/7/Text/63` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.756592 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/68` | 0.756592 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.756592 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/65` | 0.756592 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/60` | 0.756592 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.756592 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.756592 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.756592 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.756592 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.756592 | **SPELLS** |

### Query 149
- Text: Summarize Primal
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/503']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/503', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/502', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/504']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/502` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/504` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/503` | 0.749548 | Primal |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/17` | 0.626243 | **Primal** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/57` | 0.602506 | PRIMAL 1ST-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/64` | 0.574944 | PRIMAL 10TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/17` | 0.560184 | PRIMAL 2ND-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/48` | 0.560070 | PRIMAL 8TH-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/56` | 0.556584 | PRIMAL 9TH-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/49` | 0.554742 | PRIMAL 3RD-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/34` | 0.552573 | PRIMAL 7TH-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/71` | 0.549723 | PRIMAL 4TH-RANK SPELLS |

### Query 150
- Text: What is the rule about **Spell Lists**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/62']
- Expected found: `True`
- Expected rank: `27`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/62', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/63', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/61']
- Expanded expected found: `True`
- Expanded expected rank: `27`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/3/Text/63` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/87` | 0.732608 | **Spell Lists** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/25` | 0.732608 | **Spell Lists** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/60` | 0.732608 | **Spell Lists** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/69` | 0.732608 | **Spell Lists** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/44` | 0.732608 | **Spell Lists** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/69` | 0.732608 | **Spell Lists** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/75` | 0.732608 | **Spell Lists** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/62` | 0.732608 | **Spell Lists** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/84` | 0.732608 | **Spell Lists** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/61` | 0.732608 | **Spell Lists** |

### Query 151
- Text: What is the rule about CHAPTER 7: SPELLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.854519 | CHAPTER 7: SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/5` | 0.666278 | OCCULT 7TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.656794 | SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/34` | 0.643216 | PRIMAL 7TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/57` | 0.636854 | ARCANE 7TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/11` | 0.627402 | DIVINE 7TH-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.599134 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.599134 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/36` | 0.599134 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/62` | 0.599134 | **SPELLS** |

### Query 152
- Text: Summarize **Critical Success** The creature is unaffected.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/7']
- Expected found: `True`
- Expected rank: `18`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/7', 'PZO22001 Starfinder Player Core 330-363::/page/5/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/5/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `18`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/5/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/5/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/30/Text/38` | 0.967259 | **Critical Success** The creature is unaffected. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/30` | 0.967259 | **Critical Success** The creature is unaffected. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/11` | 0.967259 | **Critical Success** The creature is unaffected. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/2` | 0.967259 | **Critical Success** The creature is unaffected. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/8` | 0.967259 | **Critical Success** The creature is unaffected. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/14` | 0.967259 | **Critical Success** The creature is unaffected. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/19` | 0.967259 | **Critical Success** The creature is unaffected. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/20` | 0.967259 | **Critical Success** The creature is unaffected. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/34/Text/33` | 0.967259 | **Critical Success** The creature is unaffected. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/32/Text/14` | 0.967259 | **Critical Success** The creature is unaffected. |

### Query 153
- Text: What does **CARCINIZATION **[two-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/21']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/26/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/25/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/26/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/25/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/21` | 0.628038 | **CARCINIZATION **[two-actions] **SPELL 5**  **INCAPACITATION** **MANIPULATE** **POLYMORPH**  **Traditions** primal  **Range **30 feet;** Targets** 1 creature  **Defense** Fortitude; **Duration** 1 mi |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/15` | 0.570017 | ARCANE 5TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/40` | 0.559313 | OCCULT 5TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26` | 0.547668 | **BANISHMENT **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet; **Targets** 1 creature that isn't on its |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/7` | 0.545963 | PRIMAL 5TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/54` | 0.544452 | DIVINE 5TH-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/39` | 0.542847 | **SUBCONSCIOUS SUGGESTION **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **LINGUISTIC** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet;** Targe |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` | 0.541972 | **CONTROL MACHINE **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature or hazard with t |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/23` | 0.536200 | **ATOMIC BLAST **[three-actions] **SPELL 9**  **CONCENTRATE** **FIRE** **MANIPULATE** **RADIATION**  **Traditions** arcane, primal  **Range **500 feet;** Area** 100-foot burst **Defense** Reflex; **Du |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/12` | 0.528225 | **HALLUCINATION **[two-actions] **SPELL 5**  **ILLUSION** **INCAPACITATION** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** 1 creature  **Duration* |

### Query 154
- Text: What is the rule about Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your pool is equal to the number of focus spells you  know or 3, whichever is lower. This counts only spells that  require Focus Points to cast.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/15', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/16', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` | 0.957599 | Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your p |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.748869 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/23` | 0.745824 | It's possible, especially through archetypes, to gain focus  spells from more than one source. If this happens, you  have just one focus pool, counting all your focus spells to  determine the points i |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` | 0.711419 | Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.692107 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` | 0.687931 | Focus spells are automatically heightened to half your level  rounded up, just like cantrips are. You can't cast a focus spell  if its minimum rank is greater than half your level rounded  up, even if |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.674479 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/7` | 0.652403 | Some spells require you to pay a cost or provide a locus. If the  spell lists a **cost**, you must have the listed money, valuable  materials, or other resources to cast the spell (such as gems or  ma |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 0.646403 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/16` | 0.644374 | You replenish all the Focus Points in your pool during your  daily preparations. You can also use the Refocus activity to  pray, study, meditate, or otherwise reattune yourself to the  source of your |

### Query 155
- Text: What does **CATACLYSM **[two-actions] **SPELL 10** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/26/ListItem/17', 'PZO22001 Starfinder Player Core 294-329::/page/26/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/26/ListItem/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/26/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/5` | 0.637211 | **CATACLYSM **[two-actions] **SPELL 10**  **ACID** **AIR** **COLD** **CONCENTRATE** **EARTH** **ELECTRICITY** **FIRE** **MANIPULATE** **WATER**  **Traditions** arcane, primal  **Range **1,000 feet;** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/29` | 0.599491 | OCCULT 10TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47` | 0.591357 | **REVIVAL **[two-actions] **SPELL 10**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet;** Targets** dead creatures and living creatures of  y |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/10/SectionHeader/33` | 0.581127 | **INDESTRUCTIBILITY **[two-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Duration** until the start of your next turn  You sever yourself from |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` | 0.580418 | **CONTROL MACHINE **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature or hazard with t |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/32` | 0.573083 | **PHANTASMAGORIA **[two-actions] **SPELL 9**  **CONCENTRATE** **DEATH** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **120 feet; **Targets** any number of creatures |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/43` | 0.572027 | **PHANTASMAL CALAMITY **[two-actions] **SPELL 6**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **500 feet; **Area** 30-foot burst  **Defense** Will |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/1` | 0.571322 | **HEROISM **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult **Duration** 10 minutes |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/15` | 0.568452 | **PARALYZE **[two-actions] **SPELL 3**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature  **Defense** Will; **Durat |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/23` | 0.564564 | **ATOMIC BLAST **[three-actions] **SPELL 9**  **CONCENTRATE** **FIRE** **MANIPULATE** **RADIATION**  **Traditions** arcane, primal  **Range **500 feet;** Area** 100-foot burst **Defense** Reflex; **Du |

### Query 156
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/29', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/28', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/29` | 0.888833 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/85` | 0.888833 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/91` | 0.888833 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/79` | 0.888833 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/64` | 0.888833 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/70` | 0.888833 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/88` | 0.888833 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/65` | 0.888833 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/67` | 0.888833 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/48` | 0.888833 | **PLAYING THE ** **GAME** |

### Query 157
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/43']
- Expected found: `True`
- Expected rank: `7`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/43', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/42', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `7`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/71` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/50` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/32` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/33` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/68` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/69` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/43` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/74` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/72` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/67` | 0.879439 | **GLOSSARY & ** **INDEX** |

### Query 158
- Text: What is the rule about **Focus Spells**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/70']
- Expected found: `True`
- Expected rank: `9`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/70', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/71', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/69']
- Expanded expected found: `True`
- Expanded expected rank: `9`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/71` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/69` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/46` | 0.799140 | **Focus Spells** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/62` | 0.799140 | **Focus Spells** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/89` | 0.799140 | **Focus Spells** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/65` | 0.799140 | **Focus Spells** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/71` | 0.799140 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/68` | 0.799140 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/63` | 0.799140 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/72` | 0.799140 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/70` | 0.799140 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/77` | 0.799140 | **Focus Spells** |

### Query 159
- Text: What is the rule about You spend 10 minutes performing deeds to restore your  magical connection. This restores 1 Focus Point to your focus  pool. The deeds you need to perform are specified in the class  or ability that gives you your focus spells. These deeds can  usually overlap with other tasks that relate to the source  of your focus spells. For instance, a witchwarper with focus  points from their paradox can usually Refocus while using  their paradox skill.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/20', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/20` | 0.960213 | You spend 10 minutes performing deeds to restore your  magical connection. This restores 1 Focus Point to your focus  pool. The deeds you need to perform are specified in the class  or ability that gi |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/23` | 0.664019 | It's possible, especially through archetypes, to gain focus  spells from more than one source. If this happens, you  have just one focus pool, counting all your focus spells to  determine the points i |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/16` | 0.650355 | You replenish all the Focus Points in your pool during your  daily preparations. You can also use the Refocus activity to  pray, study, meditate, or otherwise reattune yourself to the  source of your |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` | 0.646580 | Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.640096 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.639518 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/47` | 0.633460 | **DISPEL MAGIC **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **120 feet;** Targets** 1 spell effect or unattended magic  item  You |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/18` | 0.631194 | **DIVINE INSPIRATION **[two-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine  **Range **touch;** Targets** 1 willing creature  You infuse a target with spiritual |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/14/SectionHeader/27` | 0.626793 | **MENDING** **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Cast** 10 minutes  **Range **touch;** Targets** non-magical object of light Bulk or less You r |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.626523 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |

### Query 160
- Text: What is the rule about **Heightened (8th)** Choose to either target any number of  creatures or change the spell's duration to unlimited.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/6/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/6/Text/25', 'PZO22001 Starfinder Player Core 330-363::/page/6/Text/26', 'PZO22001 Starfinder Player Core 330-363::/page/6/Text/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/6/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/6/Text/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/25` | 0.872683 | **Heightened (8th)** Choose to either target any number of  creatures or change the spell's duration to unlimited. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/24` | 0.754045 | **Heightened (6th)** Choose to either target up to 10 creatures  or change the spell's duration to until your next daily  preparations. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/6` | 0.682871 | **Heightened (8th)** You can target up to 5 creatures. If a  creature uses a hostile action or reaction that affects  multiple targets simultaneously, it needs to attempt only  one save against *mask |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/50` | 0.663188 | **Heightened (7th)** You can target up to 5 additional creatures  to gain protection against the environment the triggering  creature entered. The spell lasts for 8 hours and also  protects against ex |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/1` | 0.655993 | **Heightened (5th)** The spell's range is touch and it targets  1 willing creature. The duration is until your next daily  preparations. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/11` | 0.652326 | **STATUS **[two-actions] **SPELL 2**  **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch;** Targets** 1 willing living creature  **Duration** until yo |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/36` | 0.650708 | **HASTE **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Range **30 feet;** Targets** 1 creature  **Duration** 1 minute  Magic empowers the target |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/25` | 0.650260 | **Heightened (6th)** The spell's range is touch and it targets 1 willing  creature. The duration is until your next daily preparations. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/51` | 0.648053 | **Heightened (10th)** You can target up to 10 additional  creatures to gain protection against the environment the  triggering creature entered. The spell lasts until your next  daily preparations and |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47` | 0.644669 | **REVIVAL **[two-actions] **SPELL 10**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet;** Targets** dead creatures and living creatures of  y |

### Query 161
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/32']
- Expected found: `True`
- Expected rank: `9`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/33', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/31']
- Expanded expected found: `True`
- Expanded expected rank: `9`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/70` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/67` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/92` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/42` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/68` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/73` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/71` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/71` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/32` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/66` | 0.900802 | **CONDITIONS ** **APPENDIX** |

### Query 162
- Text: What is the rule about **Heightened (+1)** The damage increases by 1d6.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/1', 'PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/3/Text/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/2` | 0.837901 | **Heightened (+1)** The damage increases by 1d6. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/32/Text/17` | 0.830353 | **Heightened (+1)** The damage increases by 1d6 and persistent  damage increases by 1d6. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/34/Text/37` | 0.809002 | **Heightened (+1)** The damage increases by 1d12. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/32/Text/43` | 0.805756 | **Heightened (+1)** The damage increases by 1d10. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/24/Text/12` | 0.805756 | **Heightened (+1)** The damage increases by 1d10. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/23` | 0.805756 | **Heightened (+1)** The damage increases by 1d10. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/54` | 0.776589 | **Heightened (+1)** The damage increases by 2d4. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/34` | 0.763459 | **Heightened (+1)** The damage increases by 2d6 (or by 2d8 if  the target is a divine spellcaster). |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/22` | 0.746913 | **Heightened (+1)** The damage increases by 1d8 and the ice's  Hit Points increase by 5. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/15` | 0.746913 | **Heightened (+1)** The damage increases by 1d8 and the ice's Hit  Points increase by 5. |

### Query 163
- Text: Summarize The target can soar through the air, gaining a fly Speed equal  to its Speed or 20 feet, whichever is greater.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/9', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/8', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/3/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/3/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/9` | 0.952090 | The target can soar through the air, gaining a fly Speed equal  to its Speed or 20 feet, whichever is greater. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/2` | 0.746047 | **Fly**H Grant a target a fly Speed. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/25` | 0.744703 | **Fly**H Grant the target a fly Speed. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/76` | 0.744703 | **Fly**H Grant the target a fly Speed. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/20/Text/20` | 0.735576 | **Heightened (4th)** You can turn into a flying creature, such as  a bird, which grants you a fly Speed of 20 feet. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/20/ListItem/16` | 0.681073 | Speed 20 feet. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/13` | 0.662349 | Speed 40 feet, fly 100 feet. You gain any of the following  Speeds the chosen dragon has, but with the listed  amount: burrow 20 feet, climb 40 feet, swim 60 feet. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/20/Text/12` | 0.661944 | **Speed **fly 30 feet |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/ListItem/50` | 0.647573 | **Bird** Speed 10 feet, fly 50 feet; **Melee **[one-action] beak, **Damage ** 2d8 piercing; **Melee **[one-action] talon (agile), **Damage **1d10  slashing. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/20/Text/3` | 0.641149 | **Heightened (6th)** Your battle form is Huge, your fly Speed  gains a +15-foot status bonus, and your attacks have  10-foot reach. You instead gain AC = 21 + your level, 15  temporary HP, attack modi |

### Query 164
- Text: What is the rule about **Success** The creature takes half damage and is slowed 1 until  the end of its next turn.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/3', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/1/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/3` | 0.837204 | **Success** The creature takes half damage and is slowed 1 until  the end of its next turn. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/31` | 0.734610 | **Success** The creature takes half damage. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/19` | 0.734610 | **Success** The creature takes half damage. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/34/Text/34` | 0.734610 | **Success** The creature takes half damage. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/24/Text/9` | 0.734610 | **Success** The creature takes half damage. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/34/Text/14` | 0.734610 | **Success** The creature takes half damage. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/51` | 0.734610 | **Success** The creature takes half damage. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/32/Text/40` | 0.734610 | **Success** The creature takes half damage. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/12` | 0.734610 | **Success** The creature takes half damage. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/20` | 0.734610 | **Success** The creature takes half damage. |

### Query 165
- Text: Summarize TARGETS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20` | 0.769956 | TARGETS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22` | 0.622032 | FOCUS POINTS FROM MULTIPLE  SOURCES |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14` | 0.620988 | RANGES, AREAS, AND  TARGETS |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/44` | 0.612749 | **CONCENTRATE** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.612749 | **CONCENTRATE** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` | 0.602713 | **CONCENTRATE** **MANIPULATE** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/42` | 0.578946 | **Analyze** **Target**H Gather data about a target's basic physiology. **Daze**H Cloud a creature's mind and possibly stun it. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/29` | 0.578946 | **Analyze** **Target**H Gather data about a target's basic physiology. **Daze**H Cloud a creature's mind and possibly stun it. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/89` | 0.571400 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/67` | 0.571400 | **Focus Spells** |

### Query 166
- Text: What is the rule about The image can't speak, but you can use your actions to  speak through the creature, with the spell disguising your  voice as appropriate. You might need to attempt a Deception  or Performance check to mimic the creature, as determined  by the GM. This is especially likely if you're trying to imitate a  specific person and engage with someone that person knows.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/3', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/9/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/9/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/2` | 0.965358 | The image can't speak, but you can use your actions to  speak through the creature, with the spell disguising your  voice as appropriate. You might need to attempt a Deception  or Performance check to |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/10/Text/3` | 0.695489 | **Heightened (6th)** Creatures or objects in your scene can  speak. You must speak the specific lines for each actor  when creating your program. The spell disguises your  voice for each actor. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/17` | 0.686772 | Magic with the illusion trait creates false sensory stimuli.  Sometimes illusions allow creatures a chance to disbelieve  the spell, which lets the creature ignore the spell if it succeeds  at doing s |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/3` | 0.686755 | The casting of a spell can range from a simple word of magical  might that creates a fleeting effect to a complex process  taking hours to cast and producing a long-term impact.  Casting a spell requi |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/21` | 0.683416 | Some spells allow you to target a creature, an object, or  something more specific. The target must be within the  spell's range, and you must be able to see it (or otherwise  perceive it with a preci |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/1` | 0.666154 | You create an illusory image of a Large or smaller creature. It  generates the appropriate sounds, smells, and feels believable  to the touch. If you and the image are ever farther than 500  feet apar |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/9` | 0.665005 | A creature called by a spell or effect gains the summoned  trait. A summoned creature can't summon other creatures,  create things of value, or cast spells that require a cost. It  has the minion trai |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/11` | 0.662259 | though at the GM's discretion, you might be able to speak  a few sentences. As with other activities that take a long  time, these spells have the exploration trait, and you can't  cast them in an enc |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/10/Text/2` | 0.651636 | Any creature that touches any part of the image or uses  the Seek action to examine it can attempt to disbelieve  your illusion. If they interact with a portion of the illusion,  they disbelieve only |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/5` | 0.650335 | Any creature that touches the image or uses the Seek  action to examine it can attempt to disbelieve your illusion.  When a creature disbelieves the illusion, it recovers from half  the damage it had |

### Query 167
- Text: What is the rule about SPELL SLOTS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/6', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5` | 0.808990 | SPELL SLOTS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.609501 | SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.596041 | SPELL ATTACKS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/13` | 0.575730 | SUSTAINING SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.572034 | CHAPTER 7: SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/3` | 0.549830 | IDENTIFYING SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/8/SectionHeader/1` | 0.544791 | SPELL LISTS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/62` | 0.543476 | **Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/61` | 0.543476 | **Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/67` | 0.543476 | **Spells** |

### Query 168
- Text: Summarize Tradition
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/487']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/487', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/486', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/488']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/486` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/488` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/487` | 0.654175 | Tradition |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.545791 | insight about a topic. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/6` | 0.505688 | COUNTERACTING |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1` | 0.496740 | **MAGICAL TRADITIONS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22` | 0.494070 | FOCUS POINTS FROM MULTIPLE  SOURCES |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.493747 | **Summoned** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/45` | 0.492353 | **Traditions** divine, primal |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/66` | 0.480840 | **Rituals** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/40` | 0.480840 | **Rituals** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/47` | 0.480840 | **Rituals** |

### Query 169
- Text: What does **GRAVITY FIELD **[three-actions] **SPELL 8** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/46']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/46', 'PZO22001 Starfinder Player Core 330-363::/page/5/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/39']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/5/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/39` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/46` | 0.694613 | **GRAVITY FIELD **[three-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **100 feet; **Area** 30-foot radius, 100-foot-tall cylinder  **Dur |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/48` | 0.565325 | PRIMAL 8TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/17` | 0.565063 | OCCULT 8TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.563298 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/36` | 0.559059 | **EARTHBIND **[two-actions] **SPELL 3**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 flying creature  **Defense** Fortitude; **Duration** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/47` | 0.556471 | **EARTHQUAKE **[two-actions] **SPELL 8**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Area** 60-foot burst  **Duration** 1 round  You shake the groun |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/26` | 0.552789 | **FIELD OF LIFE **[two-actions] **SPELL 6**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet; **Area** 20-foot burst **Duration** sustained up |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/23` | 0.538725 | **Gravity** **Field** Create a field of increased gravity in an area as  you desire. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/19` | 0.538725 | **Gravity** **Field** Create a field of increased gravity in an area as  you desire. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/54` | 0.538061 | **PERSONAL GRAVITY **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Duration** 1 hour  You alter gravity's effects on you. You treat gravity as if |

### Query 170
- Text: Summarize LONG CASTING TIMES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/8', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/9` | 0.816559 | LONG CASTING TIMES |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/15` | 0.682872 | LONG DURATIONS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/2` | 0.591742 | CASTING SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21` | 0.559502 | SPELLCASTERS WITH FOCUS  SPELLS |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/8` | 0.558010 | **Duration** 5 minutes |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/9` | 0.550353 | DURATIONS |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/32/Text/31` | 0.545645 | **Heightened (4th)** The duration is 8 hours. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/48` | 0.541283 | **Duration** 1 minute |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22` | 0.533037 | FOCUS POINTS FROM MULTIPLE  SOURCES |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.529685 | **SUBTLE SPELLS** |

### Query 171
- Text: What is the rule about beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.804248 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.521904 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/12` | 0.511670 | After Triune's Signal connected cultures across the  Universe, the peoples of the galaxy have learned more  than ever before about the Universe's composition  thanks to science and technology. As tech |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` | 0.510271 | Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.506074 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.501710 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.497519 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.496106 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/10` | 0.493752 | The power of the divine is steeped in faith,  the unseen, and belief in a power source from |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/24` | 0.479603 | spells and precog warp spells, your mystic spells would  remain divine and the witchwarper spells occult. Similarly,  you need to use the attribute modifier determined by the  source of the focus spel |

### Query 172
- Text: Summarize Your senses improve as you gain feline eyes, ears, and  whiskers. You gain darkvision and electromagnetic scent  as an imprecise sense out to 30 feet, allowing you to detect  living and technological creatures.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/23', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/24', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/2/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/2/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/23` | 0.986196 | Your senses improve as you gain feline eyes, ears, and  whiskers. You gain darkvision and electromagnetic scent  as an imprecise sense out to 30 feet, allowing you to detect  living and technological |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/54` | 0.809276 | **Feline** **Senses**H The target's senses improve with feline ears,  eyes, and whiskers. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/29` | 0.809276 | **Feline** **Senses**H The target's senses improve with feline ears,  eyes, and whiskers. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/21/ListItem/13` | 0.673463 | Low-light vision and imprecise scent 30 feet. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/20/ListItem/18` | 0.673463 | Low-light vision and imprecise scent 30 feet. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/17` | 0.656478 | **Measure**H You get measurements of creatures you can  observe in the area. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/49` | 0.656478 | **Measure**H You get measurements of creatures you can  observe in the area. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/34` | 0.656478 | **Measure**H You get measurements of creatures you can  observe in the area. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/46` | 0.656478 | **Measure**H You get measurements of creatures you can observe  in the area. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/15` | 0.648940 | Darkvision and imprecise scent 60 feet. |

### Query 173
- Text: What is the rule about Falsehoods pass your lips as smoothly as silk. You gain a  +4 status bonus to Deception checks to Lie and against  Perception checks to discern if you are telling the truth, and  you add your level even if untrained. If the implausibility of  your lies prompts a circumstance penalty or a DC increase,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/73']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/73', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/37', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/38']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/7/Text/37` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/7/Text/38` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/73` | 0.958111 | Falsehoods pass your lips as smoothly as silk. You gain a  +4 status bonus to Deception checks to Lie and against  Perception checks to discern if you are telling the truth, and  you add your level ev |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/2` | 0.676725 | *Humanoid form* grants you a +4 status bonus to Deception  checks to pass as a generic member of the chosen ancestry,  and you add your level even if you're untrained, but you  can't make yourself loo |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/2` | 0.627095 | **Critical Failure** As failure, and the target takes a –4  circumstance penalty to Deception checks against your  questions. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/1` | 0.600071 | **Failure** Each round of the spell's duration, you can Sustain the  spell to ask a different question and attempt to uncover  the answer. For each question, the target can attempt  a Deception check |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/13` | 0.597776 | Disguises and illusions fool the spell as long as they  appear to match its parameters. For a spell to detect  something visually, the spell's origin point must have line of  sight. Darkness doesn't p |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/3` | 0.589593 | Other heightened entries give a number after a plus sign,  indicating that heightening grants extra advantages over  multiple ranks. The listed effect applies for every increment  of ranks by which th |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/16/SectionHeader/28` | 0.589557 | **MYSTIC ARMOR **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Duration** until your next daily preparations  You ward yourself with shimm |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/30` | 0.580993 | **GLOW UP **[two-actions] **SPELL 1**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **VISUAL**  **Traditions** arcane, occult, primal  **Range **30 feet;** Targets** 1 willing creature  **Duration** 1 |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/20/ListItem/15` | 0.576663 | AC = 15 + your level. Ignore your armor's check penalty  and Speed reduction. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/ListItem/46` | 0.575478 | One or more unarmed melee attacks specific to the  battle form you choose, which are the only attacks you  can Strike with. You're trained with them. Your attack  modifier is +16, and your damage bonu |

### Query 174
- Text: What is the rule about You let out a powerful ululation full of psychic resonance that  compels others who hear it to join in. You deal 7d12 sonic  damage and 1d8 persistent mental damage to other creatures  who can hear within the area. Targets must attempt a Will  save. The persistent mental damage a creature takes from  this spell increases by 1d8 if at least one other creature is  howling. A howling creature can't use auditory actions or  cast spells except for those with the subtle trait for 1 round.  Calculate the persistent damage after all creatures attempt  their saves.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/37']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/37', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/73', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/36']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/7/Text/73` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/7/Text/36` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/37` | 0.950042 | You let out a powerful ululation full of psychic resonance that  compels others who hear it to join in. You deal 7d12 sonic  damage and 1d8 persistent mental damage to other creatures  who can hear wi |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/40` | 0.683737 | **Failure** The target takes full damage, persistent mental  damage, and is compelled to howl as long as it takes  persistent mental damage. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/13` | 0.678848 | **NOISE BLAST **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SONIC**  **Traditions** arcane, divine, occult **Range **30 feet;** Area** 10-foot burst  **Defense** Fortitude  A cacophono |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/20` | 0.674105 | **ENTHRALL **[two-actions] **SPELL 3**  **AUDITORY** **CONCENTRATE** **EMOTION** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet;** Targets** all creatures in range  **Defense** Will |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/29/SectionHeader/14` | 0.672161 | **SILENCE **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** divine, occult  **Range **touch;** Targets** 1 willing creature  **Duration** 1 minute  The target makes n |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/15` | 0.671195 | **DEATH SENTENCE **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **DEATH** **INCAPACITATION** **SPIRIT**  **Traditions** divine, primal  **Range **30 feet;** Targets** 1 creature  **Defense* |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6` | 0.668236 | **CHILLING DARKNESS **[two-actions] **SPELL 3**  **ATTACK** **COLD** **CONCENTRATE** **DARKNESS** **MANIPULATE** **UNHOLY**  **Traditions** divine  **Range **120 feet;** Targets** 1 creature  **Defens |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/50` | 0.667941 | **Heightened (7th)** You can target up to 5 additional creatures  to gain protection against the environment the triggering  creature entered. The spell lasts for 8 hours and also  protects against ex |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/25/Text/11` | 0.662132 | **CALM **[two-actions] **SPELL 2**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **120 feet;** Area** 10-foot burst  **Defense** Wil |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/31/Text/13` | 0.661296 | **SONIC SCREAM **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SONIC**  **Traditions** arcane, occult, primal  **Area** 15-foot cone  **Defense** Fortitude  You unleash a painfully rapid |

### Query 175
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/35']
- Expected found: `True`
- Expected rank: `4`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/35', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/34', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/36']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/36` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/63` | 0.865652 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/59` | 0.865652 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/60` | 0.865652 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/35` | 0.865652 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/64` | 0.865652 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/58` | 0.865652 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/67` | 0.865652 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/67` | 0.865652 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/66` | 0.865652 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/79` | 0.865652 | **EQUIPMENT** |

### Query 176
- Text: What does **BLINDNESS **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36` | 0.633193 | **BLINDNESS **[two-actions] **SPELL 3**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet;** Targets** 1 creature  **Defense** Fortit |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.622092 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.610742 | **LIFE SEAL **[reaction] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` | 0.594753 | **HYPNOTIZE **[two-actions] **SPELL 3**  **ILLUSION** **MANIPULATE** **SUBTLE** **VISUAL**  **Traditions** arcane, occult  **Range **120 feet; **Area** 10-foot burst  **Defense** Will;** Duration** su |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/18` | 0.569649 | **FELINE SENSES **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MORPH**  **Traditions** divine, primal  **Duration** 1 hour |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.568801 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/51` | 0.562182 | **DARKVISION **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Duration** 1 hour  You grant yourself supernatural sight in areas of darkness |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/1` | 0.558760 | **HEROISM **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult **Duration** 10 minutes |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6` | 0.558008 | **CHILLING DARKNESS **[two-actions] **SPELL 3**  **ATTACK** **COLD** **CONCENTRATE** **DARKNESS** **MANIPULATE** **UNHOLY**  **Traditions** divine  **Range **120 feet;** Targets** 1 creature  **Defens |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/8` | 0.556116 | **DEAFNESS **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **30 feet;** Targets** 1 creature  **Defense** Fortitude  The target loses |

### Query 177
- Text: What is the rule about **SPELLCASTING IN STARFINDER**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11` | 0.814402 | **SPELLCASTING IN STARFINDER** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/2` | 0.584243 | CASTING SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21` | 0.562569 | SPELLCASTERS WITH FOCUS  SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20` | 0.540823 | NON-SPELLCASTERS WITH  FOCUS SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5` | 0.521279 | SPELL SLOTS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/3` | 0.507968 | **SPELLSHAPE** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/1` | 0.500799 | Whether it comes in the form of eldritch artifacts, otherworldly beings, or witchwarpers altering  reality with strange spells, magic brings fantasy and wonder to Starfinder. This chapter explains how |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/68` | 0.490277 | **Scrying**U Spy on a creature you choose. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/50` | 0.490277 | **Scrying**U Spy on a creature you choose. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.488889 | **SPELLS** |

### Query 178
- Text: What does **BREATH OF LIFE **[reaction] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/54']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/54', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/47` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/54` | 0.663561 | **BREATH OF LIFE **[reaction] **SPELL 5**  **CONCENTRATE** **HEALING** **VITALITY**  **Traditions** divine  **Trigger** A living creature within range would die.  **Range **60 feet;** Targets** the tr |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.647665 | **LIFE SEAL **[reaction] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/40` | 0.599628 | OCCULT 5TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/15` | 0.587239 | ARCANE 5TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/56` | 0.583682 | **Breath of Life**H React to revive a character at the moment of  its death. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.565746 | CHAPTER 7: SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4` | 0.563603 | **AIR BUBBLE **[reaction] **SPELL 1**  **AIR** **CONCENTRATE**  **Traditions** arcane, divine, primal  **Trigger** A creature within range enters an environment where  it can't breathe.  **Range **60 |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/7` | 0.563482 | PRIMAL 5TH-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/50` | 0.556475 | **SUBJECTIVE REALITY **[one-action] **SPELL 5**  **CONCENTRATE** **MANIPULATE**  **Traditions** occult  **Range **500 feet;** Targets** 1 creature or object  **Duration** sustained up to 1 minute  You |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/24/SectionHeader/35` | 0.552695 | **REGENERATE **[two-actions] **SPELL 7**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **touch;** Targets** 1 willing living creature  **Duration** 1 |

### Query 179
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/59']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/59', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/60', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/58']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/3/Text/60` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/3/Text/58` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/59` | 0.685680 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/24` | 0.685680 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/84` | 0.685680 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/78` | 0.685680 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/65` | 0.685680 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/43` | 0.685680 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/66` | 0.685680 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/59` | 0.685680 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/62` | 0.685680 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/60` | 0.685680 | **FEATS** |

### Query 180
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/66']
- Expected found: `True`
- Expected rank: `19`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/66', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/65', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/67']
- Expanded expected found: `True`
- Expanded expected rank: `19`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/3/Text/65` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/3/Text/67` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/29` | 0.888833 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/85` | 0.888833 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/91` | 0.888833 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/79` | 0.888833 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/64` | 0.888833 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/70` | 0.888833 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/88` | 0.888833 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/65` | 0.888833 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/67` | 0.888833 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/48` | 0.888833 | **PLAYING THE ** **GAME** |

### Query 181
- Text: What does **AIR BUBBLE **[reaction] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/20/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/20/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4` | 0.727191 | **AIR BUBBLE **[reaction] **SPELL 1**  **AIR** **CONCENTRATE**  **Traditions** arcane, divine, primal  **Trigger** A creature within range enters an environment where  it can't breathe.  **Range **60 |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/46` | 0.625026 | **Air Bubble** React to create air for a creature to breathe. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/58` | 0.625026 | **Air Bubble** React to create air for a creature to breathe. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/28` | 0.625026 | **Air Bubble** React to create air for a creature to breathe. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.606675 | **LIFE SEAL **[reaction] **SPELL 3** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/43` | 0.590906 | **PUMMELING RUBBLE **[two-actions] **SPELL 1**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Area** 15-foot cone  **Defense** Reflex  A spray of heavy rocks flies through |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.573657 | SPELL ATTACKS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.572138 | CHAPTER 7: SPELLS |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` | 0.570569 | **HYPNOTIZE **[two-actions] **SPELL 3**  **ILLUSION** **MANIPULATE** **SUBTLE** **VISUAL**  **Traditions** arcane, occult  **Range **120 feet; **Area** 10-foot burst  **Defense** Will;** Duration** su |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/37` | 0.567173 | **PEACEFUL BUBBLE** **SPELL 4**  **UNCOMMON** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Cast** 10 minutes  **Range **touch; **Area** 100-foot burst  **Duration** 24 hours  An op |

### Query 182
- Text: What does **FEAR **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/8', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/18', 'PZO22001 Starfinder Player Core 330-363::/page/2/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/2/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/2/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/8` | 0.679285 | **FEAR **[two-actions] **SPELL 1**  **CONCENTRATE** **EMOTION** **FEAR** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult, primal  **Range **30 feet;** Targets** 1 creature **Defense** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/29` | 0.620728 | **STUPEFY **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** varies  You du |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/13/SectionHeader/48` | 0.619687 | **MASK OF TERROR **[two-actions] **SPELL 7**  **CONCENTRATE** **EMOTION** **FEAR** **ILLUSION** **MANIPULATE** **MENTAL** **VISUAL**  **Traditions** arcane, occult, primal  **Range **30 feet; **Target |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.613911 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` | 0.611282 | **CLEAR MIND **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You drive menta |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/26` | 0.609133 | **PARANOIA **[two-actions] **SPELL 2**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** occult  **Range **30 feet; **Targets** 1 creature **Defense** Will; **Duration** 1 minute |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/25/Text/11` | 0.606786 | **CALM **[two-actions] **SPELL 2**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **120 feet;** Area** 10-foot burst  **Defense** Wil |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/4` | 0.605845 | **Failure** The creature becomes frightened 2 before using its  action. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52` | 0.600066 | **CHARM **[two-actions] **SPELL 1**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 creatur |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.598948 | **SPELL NAME **[one-action] **SPELL (RANK)** |

### Query 183
- Text: What does **FORCE BARRAGE **[one-action]** TO **[three-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/19', 'PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/11', 'PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/19` | 0.691601 | **FORCE BARRAGE **[one-action]** TO **[three-actions] **SPELL 1**  **CONCENTRATE** **FORCE** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet;** Targets** 1 creature  You fire a shard |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.609468 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.591454 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/50` | 0.586199 | **SHIFTING SURGE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** one weapon held by you or a  willing ally that deals acid, c |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20` | 0.584771 | **BLAZING BOLT **[one-action]** TO **[three-actions] **SPELL 2**  **ATTACK** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets** 1 or more creatures |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/26` | 0.577927 | **HARM **[one-action]** TO **[three-actions] **SPELL 1**  **MANIPULATE** **VOID**  **Traditions** divine  **Range **varies; **Targets** 1 living creature or 1 willing undead  creature  You channel voi |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.576805 | **LIFE SEAL **[reaction] **SPELL 3** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/44` | 0.576698 | **HEAL **[one-action]** TO **[three-actions] **SPELL 1**  **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **varies; **Targets** 1 willing living creature or 1 undead  c |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/35/SectionHeader/32` | 0.574045 | **ENFEEBLE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Range **30 feet;** Targets** 1 creature  **Defense** Fortitude; **Duration** varies  Yo |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/4` | 0.568410 | **ANT HAUL **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal **Range **touch; **Targets** 1 creature  **Duration** 8 hours  You reinforce the target's musculos |

### Query 184
- Text: Summarize Dragon Breath
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/489']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/489', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/490', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/488']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/490` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/488` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/489` | 0.780751 | Dragon Breath |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/19` | 0.597458 | **Dragon Breath**[two-actions] You exhale deadly magical energy  in an area, dealing 10d6 damage to each creature in  the area with a basic save against your spell DC. The  shape, damage type, and sav |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/486` | 0.591997 | Dragon |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/14` | 0.569817 | Resistance 10 against the damage type of your Dragon  Breath (see below). |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/0/Table/3` | 0.528736 | DragonTraditionSpeedsDragon BreathAbysiumArcane—Cone of poison (Fortitude)AkashicOccult—Cone of mental (Will)CosmicDivine—Cone of spirit (Will)HostPrimalClimbCone of piercing (Reflex) |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/21` | 0.478175 | **Heightened (8th)** Your battle form is Huge, you gain a +20 foot status bonus to your fly Speed, and your attacks  have 10-foot reach (or 15-foot reach if they previously  had 10-foot reach). You in |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/63` | 0.475800 | **Summon Dragon**H Conjure a dragon to fight on your behalf. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/55` | 0.475800 | **Summon Dragon**H Conjure a dragon to fight on your behalf. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/18/Text/18` | 0.475800 | **Summon Dragon**H Conjure a dragon to fight on your behalf. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/16` | 0.475551 | The following unarmed melee attacks, which are the  only attacks you can Strike with. You're trained with  them. Your attack modifier is +22, and your damage  bonus is +6. These attacks are Strength b |

### Query 185
- Text: Summarize Divine
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/499']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/499', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/500', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/498']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/500` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/498` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/499` | 0.750323 | Divine |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9` | 0.608266 | **Divine** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/43` | 0.538146 | **Guidance** Divine guidance improves one roll. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/45` | 0.533468 | **Traditions** divine, primal |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.525307 | insight about a topic. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/10` | 0.520750 | The power of the divine is steeped in faith,  the unseen, and belief in a power source from |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/34` | 0.518177 | **Traditions** divine, occult, primal |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.514533 | **Summoned** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/57` | 0.512991 | **Divine Immolation**H Call divine fire from the sky. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/39` | 0.498836 | **Translate**H Grant understanding of a language to one  creature. |

### Query 186
- Text: What is the rule about **Heightened (6th)** The spell's range is touch and it targets 1 willing  creature. The duration is until your next daily preparations.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/25', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/24', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/2/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/2/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/25` | 0.917645 | **Heightened (6th)** The spell's range is touch and it targets 1 willing  creature. The duration is until your next daily preparations. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/1` | 0.855555 | **Heightened (5th)** The spell's range is touch and it targets  1 willing creature. The duration is until your next daily  preparations. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/24` | 0.797041 | **Heightened (6th)** Choose to either target up to 10 creatures  or change the spell's duration to until your next daily  preparations. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/24` | 0.783802 | **Heightened (4th)** The spell's range is touch and it targets 1  willing creature. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/50` | 0.713763 | **Heightened (7th)** You can target up to 5 additional creatures  to gain protection against the environment the triggering  creature entered. The spell lasts for 8 hours and also  protects against ex |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/51` | 0.706574 | **Heightened (10th)** You can target up to 10 additional  creatures to gain protection against the environment the  triggering creature entered. The spell lasts until your next  daily preparations and |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/11` | 0.688156 | **STATUS **[two-actions] **SPELL 2**  **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch;** Targets** 1 willing living creature  **Duration** until yo |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/17` | 0.687036 | A spell with a touch range requires you to physically touch  the target. You use your unarmed reach to determine  whether you can touch the creature. You can usually touch  them automatically, though |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/2` | 0.685661 | **Heightened (4th)** The spell lasts 1 minute, but it doesn't end if  the target uses a hostile action. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/4` | 0.682972 | **HONEYED WORDS **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes  You unlock the |

### Query 187
- Text: What is the rule about You create an illusory image of a Large or smaller creature. It  generates the appropriate sounds, smells, and feels believable  to the touch. If you and the image are ever farther than 500  feet apart, the spell ends.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/1', 'PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/0', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/0` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/9/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/1` | 0.936495 | You create an illusory image of a Large or smaller creature. It  generates the appropriate sounds, smells, and feels believable  to the touch. If you and the image are ever farther than 500  feet apar |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/33` | 0.709574 | **FIGMENT **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet  **Duration** sustained  You create a simp |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/19` | 0.706121 | **ILLUSORY OBJECT **[two-actions] **SPELL 1**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **VISUAL**  **Traditions** arcane, occult  **Range **500 feet;** Area** 20-foot burst  **Duration** 10 minute |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/18` | 0.703068 | **PROJECT IMAGE **[two-actions] **SPELL 7**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet  **Duration** sustained up to 1 minute  You projec |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/29` | 0.685754 | **ILLUSORY SCENE** **SPELL 5**  **AUDITORY** **CONCENTRATE** **ILLUSION** **MANIPULATE** **OLFACTORY** **VISUAL**  **Traditions** arcane, occult  **Cast** 10 minutes  **Range **500 feet;** Area** 30-f |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/27/SectionHeader/34` | 0.675553 | **SELECTIVE INVISIBILITY **[two-actions] **SPELL 3**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **500 feet; **Targets** 1 willing creature touched and one  within |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/9` | 0.656723 | **REPULSION **[two-actions] **SPELL 6**  **AURA** **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult  **Area** emanation up to 40 feet  **Defense** Will; **Duration** 1 m |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/7` | 0.655576 | **ILLUSORY DISGUISE **[two-actions] **SPELL 1**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **VISUAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 willing creature  **Duration** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/14/SectionHeader/19` | 0.654539 | **MEASURE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE**  **Traditions** arcane, divine, occult, primal  **Area** 200-foot emanation  **Duration** sustained up to 1 minute  You learn the ap |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/52` | 0.649298 | **FALSE VISION** **SPELL 5**  **UNCOMMON** **CONCENTRATE** **ILLUSION** **MANIPULATE**  **Traditions** arcane, occult  **Cast** 10 minutes  **Range **touch;** Area** 100-foot burst  **Duration** until |

### Query 188
- Text: Summarize **Minion**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/5` | 0.808882 | **Minion** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/1` | 0.681031 | **PHANTASMAL MINION STATISTICS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/2` | 0.633182 | **PHANTASMAL MINION** **CREATURE –1** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.573420 | **Summoned** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/17` | 0.567114 | **Phantasmal Minion **Create a creature of force to perform  minor tasks. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/57` | 0.567114 | **Phantasmal Minion **Create a creature of force to perform  minor tasks. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/44` | 0.564086 | **CONCENTRATE** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.564086 | **CONCENTRATE** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` | 0.558616 | **CONCENTRATE** **MANIPULATE** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/20/Text/4` | 0.548908 | ** MEDIUM** **FORCE** **MINDLESS** |

### Query 189
- Text: Summarize The power of the divine is steeped in faith,  the unseen, and belief in a power source from
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/10` | 0.937089 | The power of the divine is steeped in faith,  the unseen, and belief in a power source from |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/22` | 0.604988 | **Divine Inspiration** Spiritual energy recovers a creature's  expended spell. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.569134 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.565604 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/43` | 0.565108 | **Guidance** Divine guidance improves one roll. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/34` | 0.552288 | **Traditions** divine, occult, primal |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/499` | 0.539095 | Divine |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/53` | 0.538023 | **Truesight** See through illusions and physical transformations. **Vampiric Exsanguination**H Draw blood and life force from |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/18` | 0.536356 | **DIVINE INSPIRATION **[two-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine  **Range **touch;** Targets** 1 willing creature  You infuse a target with spiritual |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/57` | 0.533353 | **Divine Immolation**H Call divine fire from the sky. |

### Query 190
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/30']
- Expected found: `True`
- Expected rank: `24`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/31', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/28']
- Expanded expected found: `True`
- Expanded expected rank: `24`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/3/Text/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/18` | 0.863367 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/55` | 0.863367 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/28` | 0.863367 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/28` | 0.863367 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/61` | 0.863367 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/62` | 0.863367 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/57` | 0.863367 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/55` | 0.863367 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/39` | 0.863367 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/20` | 0.863367 | **INTRODUCTION** |

### Query 191
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/23']
- Expected found: `True`
- Expected rank: `18`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/24', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `18`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/1/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/63` | 0.865652 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/59` | 0.865652 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/60` | 0.865652 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/35` | 0.865652 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/64` | 0.865652 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/58` | 0.865652 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/67` | 0.865652 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/67` | 0.865652 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/66` | 0.865652 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/79` | 0.865652 | **EQUIPMENT** |

### Query 192
- Text: What is the rule about Other heightened entries give a number after a plus sign,  indicating that heightening grants extra advantages over  multiple ranks. The listed effect applies for every increment  of ranks by which the spell is heightened above its lowest  spell rank, and the benefit is cumulative. For example, *slice * *reality* says "**Heightened (+1)** The damage increases by 1d8."  Because *slice reality* deals 7d8 void damage at 6th rank, a  7th-rank *slice reality* would deal 8d8 void damage, an 8thrank spell would deal 9d8 void damage, and so on.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/3` | 0.961019 | Other heightened entries give a number after a plus sign,  indicating that heightening grants extra advantages over  multiple ranks. The listed effect applies for every increment  of ranks by which th |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` | 0.786461 | In addition, many spells have additional specific benefits  when they are heightened, such as increased damage. These  extra benefits are described at the end of the spell's stat  block. Some heighten |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.709375 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/26` | 0.672338 | **Heightened** (rank) If the spell has special effects when  heightened (page 295), those effects appear at the end  of the stat block. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/32/Text/17` | 0.665093 | **Heightened (+1)** The damage increases by 1d6 and persistent  damage increases by 1d6. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/34` | 0.658905 | **Heightened (+1)** The damage increases by 2d6 (or by 2d8 if  the target is a divine spellcaster). |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/22` | 0.644761 | **Heightened (+1)** The damage increases by 1d8 and the ice's  Hit Points increase by 5. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/15` | 0.644761 | **Heightened (+1)** The damage increases by 1d8 and the ice's Hit  Points increase by 5. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/2` | 0.638318 | **Heightened (+1)** The damage increases by 1d6. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/34/Text/37` | 0.635077 | **Heightened (+1)** The damage increases by 1d12. |

### Query 193
- Text: What does **CREATE FOOD** **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/29/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/29/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/47', 'PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/2` | 0.611702 | **CREATE FOOD** **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, primal  **Cast** 1 hour  **Range **30 feet  You create enough food to feed six Medium creatures for a  day. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.564033 | CHAPTER 7: SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47` | 0.559651 | **CLEANSE CUISINE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** divine, primal  **Range **10 feet;** Area** 1 cubic foot  You transform all food and beverages in the area |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/12` | 0.550086 | **GREASE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet;** Area** 4 contiguous 5-foot squares or** Targets** 1  object of 1 Bulk or less |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/25` | 0.549706 | OCCULT 2ND-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/75` | 0.549216 | **Create Food**H Feed multiple creatures with conjured food. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/24` | 0.549216 | **Create Food**H Feed multiple creatures with conjured food. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/9` | 0.549216 | **Create Food**H Feed multiple creatures with conjured food. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.547790 | SPELL ATTACKS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/17` | 0.541660 | PRIMAL 2ND-RANK SPELLS |

### Query 194
- Text: Summarize COSTS AND LOCI
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/6', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/5', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/4/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/6` | 0.871624 | COSTS AND LOCI |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/67` | 0.471823 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/50` | 0.471823 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/67` | 0.471823 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/81` | 0.471823 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/66` | 0.471823 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/72` | 0.471823 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/74` | 0.471823 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/68` | 0.471823 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/93` | 0.471823 | **GLOSSARY & ** **INDEX** |

### Query 195
- Text: What does **GENTLE LANDING **[reaction] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/10', 'PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/2', 'PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/10` | 0.641122 | **GENTLE LANDING **[reaction] **SPELL 1**  **AIR** **CONCENTRATE**  **Traditions** arcane, primal  **Trigger** A creature within range is falling. **Range **60 feet;** Targets** 1 falling creature  ** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/44` | 0.617263 | **Gentle Landing** React to save a falling creature. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/71` | 0.617263 | **Gentle Landing** React to save a falling creature. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.570142 | CHAPTER 7: SPELLS |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.554011 | **LIFE SEAL **[reaction] **SPELL 3** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/57` | 0.553073 | PRIMAL 1ST-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/36` | 0.547338 | **EARTHBIND **[two-actions] **SPELL 3**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 flying creature  **Defense** Fortitude; **Duration** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.543612 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/12` | 0.542533 | **GREASE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet;** Area** 4 contiguous 5-foot squares or** Targets** 1  object of 1 Bulk or less |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.541492 | **SPELL NAME **[one-action] **SPELL (RANK)** |

### Query 196
- Text: What does **CONTINGENCY** **SPELL 7** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21']
- Expected found: `True`
- Expected rank: `3`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/28/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.684025 | CHAPTER 7: SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/5` | 0.633367 | OCCULT 7TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21` | 0.626082 | **CONTINGENCY** **SPELL 7**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane  **Cast** 10 minutes **Duration** until your next daily preparations  You prepare a spell that will trigger later. Wh |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/57` | 0.590781 | ARCANE 7TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.582469 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/34` | 0.581418 | PRIMAL 7TH-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/11` | 0.573568 | DIVINE 7TH-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/3` | 0.560832 | IDENTIFYING SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/13` | 0.559111 | SUSTAINING SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.552976 | SPELLS |

### Query 197
- Text: What does **FLOATING FLAME **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/69']
- Expected found: `True`
- Expected rank: `1`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/69', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/62', 'PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/0']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 330-363::/page/2/Text/62` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/0` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/69` | 0.661447 | **FLOATING FLAME **[two-actions] **SPELL 2**  **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Targets** one 5-foot square  **Defense** Reflex; **Duration** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20` | 0.594022 | **BLAZING BOLT **[one-action]** TO **[three-actions] **SPELL 2**  **ATTACK** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets** 1 or more creatures |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/37` | 0.591635 | **REVEALING LIGHT **[two-actions] **SPELL 2**  **CONCENTRATE** **LIGHT** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **120 feet;** Area** 10-foot burst  **Defense** Reflex; * |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/30/SectionHeader/22` | 0.578545 | **SKYFIRE WINGS **[two-actions] **SPELL 3**  **CONCENTRATE** **ELECTRICITY** **FIRE** **MANIPULATE** **MORPH**  **Traditions** arcane, divine, occult, primal  **Duration** 1 minute  Wings of plasma gr |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/51` | 0.571644 | **PHANTASMAL FLEET **[two-actions] **SPELL 8**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **500 feet; **Area** 60-foot burst  **Defense** Will  A m |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/13` | 0.571239 | **ENTANGLING FLORA **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **PLANT** **WOOD**  **Traditions** arcane, primal  **Range **120 feet; **Area** all squares in a 20-foot burst  **Duratio |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.570396 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/32` | 0.570084 | **Floating Flame**H Summoned fire moves at your command. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/20` | 0.570084 | **Floating Flame**H Summoned fire moves at your command. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/25` | 0.569966 | OCCULT 2ND-RANK SPELLS |

### Query 198
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/33']
- Expected found: `True`
- Expected rank: `4`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/33', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/5/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/71` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/50` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/32` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/33` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/68` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/69` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/43` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/74` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/72` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/67` | 0.879439 | **GLOSSARY & ** **INDEX** |

### Query 199
- Text: What does **BREATHE FIRE **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62']
- Expected found: `True`
- Expected rank: `3`
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/54']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/54` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4` | 0.618109 | **AIR BUBBLE **[reaction] **SPELL 1**  **AIR** **CONCENTRATE**  **Traditions** arcane, divine, primal  **Trigger** A creature within range enters an environment where  it can't breathe.  **Range **60 |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/30/SectionHeader/22` | 0.611373 | **SKYFIRE WINGS **[two-actions] **SPELL 3**  **CONCENTRATE** **ELECTRICITY** **FIRE** **MANIPULATE** **MORPH**  **Traditions** arcane, divine, occult, primal  **Duration** 1 minute  Wings of plasma gr |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62` | 0.611258 | **BREATHE FIRE **[two-actions] **SPELL 1**  **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Area** 15-foot cone  **Defense** basic Reflex  A gout of flame sprays from your mo |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/31/SectionHeader/22` | 0.593391 | **SOOTHE **[two-actions] **SPELL 1**  **CONCENTRATE** **EMOTION** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** occult  **Range **30 feet;** Targets** 1 willing creature  **Duration** 1 minute |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/37` | 0.587282 | **IGNITION **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Targets** 1 creature  **Defense** AC  You |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.586810 | **LIFE SEAL **[reaction] **SPELL 3** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/32/Text/2` | 0.584828 | **SOUND BODY **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You send a su |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/18/SectionHeader/55` | 0.584186 | **OVERHEAT **[two-actions] **SPELL 1**  **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets **1 creature  **Defense** basic Reflex  You vent heat towar |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/12` | 0.583740 | **GREASE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet;** Area** 4 contiguous 5-foot squares or** Targets** 1  object of 1 Bulk or less |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.580981 | SPELL ATTACKS |
