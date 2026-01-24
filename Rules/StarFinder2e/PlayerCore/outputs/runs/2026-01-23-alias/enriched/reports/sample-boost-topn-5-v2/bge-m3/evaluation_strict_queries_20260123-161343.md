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
- MRR: `0.8069`
- hit@1: `0.7450`
- hit@3: `0.8300`
- hit@5: `0.8950`
- hit@10: `0.9550`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=5, same_kind_only=False, decay=0.4)

## Timings (ms)
- Embedding: `107216`
- Evaluation: `223`

## Query Details
### Query 0
- Text: Summarize **Arcane**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `32`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/8/Text/27', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/79', 'PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6` | 0.864568 | **Arcane** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/491` | 0.673609 | Arcane |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.606128 | **SUBTLE SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/27` | 0.603141 | ARCANE 1ST-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/79` | 0.598628 | **GAME** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.598432 | **Summoned** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/44` | 0.587429 | **CONCENTRATE** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.587429 | **CONCENTRATE** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/6` | 0.574704 | **Traditions** arcane, divine, occult, primal |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/1` | 0.571462 | **ALIEN CORE DRAGONS** |

### Query 1
- Text: What is the rule about SPONTANEOUS SPELLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `34`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13` | 0.800037 | SPONTANEOUS SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/13` | 0.632768 | SUSTAINING SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5` | 0.604383 | SPELL SLOTS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.603411 | CHAPTER 7: SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.592703 | SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` | 0.544548 | FOCUS SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4` | 0.538001 | Heightened Spontaneous Spells |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.530274 | SPELL ATTACKS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.529491 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/16` | 0.529396 | READING SPELLS |

### Query 2
- Text: What does **CLEANSE CUISINE **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `32`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39', 'PZO22001 Starfinder Player Core 294-329::/page/16/Text/64', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54', 'PZO22001 Starfinder Player Core 294-329::/page/11/Text/50']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47` | 0.769090 | **CLEANSE CUISINE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** divine, primal  **Range **10 feet;** Area** 1 cubic foot  You transform all food and beverages in the area |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39` | 0.678648 | **CLEANSE AFFLICTION **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  Gentle restorative |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/64` | 0.633377 | **Cleanse** **Cuisine**H Make food and drink safe and delicious. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` | 0.621478 | **CLEAR MIND **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You drive menta |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/50` | 0.614299 | **Cleanse Cuisine**H Make food and drink safe and delicious. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/12` | 0.558701 | **GREASE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet;** Area** 4 contiguous 5-foot squares or** Targets** 1  object of 1 Bulk or less |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.557521 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/7` | 0.554497 | PREPARED SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/49` | 0.553690 | **DETECT POISON **[two-actions] **SPELL 1**  **UNCOMMON** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** divine, primal  **Range **30 feet;** Targets** 1 object or creature  You detect w |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.550978 | SPELLS |

### Query 3
- Text: What does **CAIRN FORM **[one-action] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70', 'PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/71', 'PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/71', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/70` | 0.700572 | **CAIRN FORM **[one-action] **SPELL 4**  **CONCENTRATE** **EARTH** **MANIPULATE** **MORPH**  **Traditions** arcane, primal  **Range **touch;** Targets** 1 creature  **Duration** 1 minute  Your target' |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/71` | 0.640599 | ARCANE 4TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/71` | 0.638038 | PRIMAL 4TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.635319 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/17` | 0.615628 | OCCULT 4TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/36` | 0.564772 | **AERIAL FORM **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Duration** 1 minute  You harness your mastery of the sky to reshape your body |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/40` | 0.560398 | DIVINE 4TH-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/36` | 0.559753 | **CELLULAR STIMULANT **[one-action] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **VITALITY**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 willing living creature that isn't  fatig |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/24` | 0.559051 | **Heightened (4th)** The spell's range is touch and it targets 1  willing creature. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.558550 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |

### Query 4
- Text: What does **AVATAR **[two-actions] **SPELL 10** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/40']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `21`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/29', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/40', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23', 'PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/33']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/20` | 0.656907 | ARCANE 10TH-RANK SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/29` | 0.648125 | OCCULT 10TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/40` | 0.646873 | **AVATAR **[two-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** divine **Duration** 1 minute  You transform into an avatar of your deity, assuming a Huge  battle fo |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.633783 | SPELL ATTACKS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/33` | 0.623221 | DIVINE 10TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47` | 0.614634 | **REVIVAL **[two-actions] **SPELL 10**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet;** Targets** dead creatures and living creatures of  y |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.590008 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` | 0.579457 | **CONTROL MACHINE **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature or hazard with t |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/34` | 0.576802 | **FREEZE TIME **[three-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  You temporarily stop time for everything but yourself,  allowing you to use several actions |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/32/SectionHeader/56` | 0.569689 | **SPIRITUAL ARMAMENT **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SANCTIFIED** **SPIRIT**  **Traditions** divine, occult  **Range **120 feet; **Targets** 1 creature  **Defense** AC; * |

### Query 5
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/32']
- Expected found: `True`
- Expected rank: `15`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/35/Text/64', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/22', 'PZO22001 Starfinder Player Core 294-329::/page/31/Text/56', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/61', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/82']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/64` | 0.866254 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/56` | 0.866254 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/61` | 0.866254 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/22` | 0.866254 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/82` | 0.866254 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/64` | 0.824254 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/82` | 0.824254 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/70` | 0.824254 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/76` | 0.824254 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/30` | 0.824254 | **CLASSES** |

### Query 6
- Text: What is the rule about If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `45`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/22', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/21', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/13', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.996064 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.800492 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.788923 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` | 0.748364 | Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.720847 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.665842 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` | 0.653520 | With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own met |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/4` | 0.645739 | Spellcasting creates obvious sensory manifestations, such  as bright lights, crackling sounds, and sharp smells from the  gathering magic. Nearly all spells manifest a spell signature—a  colorful, glo |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.645581 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/23` | 0.638793 | It's possible, especially through archetypes, to gain focus  spells from more than one source. If this happens, you  have just one focus pool, counting all your focus spells to  determine the points i |

### Query 7
- Text: What does **Traditions** divine, occult, primal do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/34', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/45', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/6', 'PZO22001 Starfinder Player Core 330-363::/page/8/Text/24', 'PZO22001 Starfinder Player Core 330-363::/page/13/SectionHeader/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/34` | 0.877153 | **Traditions** divine, occult, primal |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/45` | 0.835370 | **Traditions** divine, primal |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/6` | 0.816625 | **Traditions** arcane, divine, occult, primal |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/24` | 0.703475 | **Traditions** occult |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/13/SectionHeader/43` | 0.619666 | **MANIFESTATION **[three-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  You spin secrets from the fundaments of magic, shaping them  into a power |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.617653 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1` | 0.605348 | **MAGICAL TRADITIONS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/14` | 0.585084 | The practitioners of occult traditions seek  to understand the unexplainable, categorize  the bizarre, and otherwise access the ephemeral in a |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/10` | 0.560027 | The power of the divine is steeped in faith,  the unseen, and belief in a power source from |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/499` | 0.554501 | Divine |

### Query 8
- Text: What is the rule about Focus spells are automatically heightened to half your level  rounded up, just like cantrips are. You can't cast a focus spell  if its minimum rank is greater than half your level rounded  up, even if you somehow gain access to it.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `34`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/1', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/13', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` | 0.975382 | Focus spells are automatically heightened to half your level  rounded up, just like cantrips are. You can't cast a focus spell  if its minimum rank is greater than half your level rounded  up, even if |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 0.790449 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.695367 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` | 0.693763 | Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` | 0.682486 | Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your p |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/17` | 0.636393 | Each spell uses the following format. Entries appear only  when applicable, so not all spells will have every entry  described here. The spell's name line also lists the type  of spell if it's a cantr |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.629385 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` | 0.619117 | In addition, many spells have additional specific benefits  when they are heightened, such as increased damage. These  extra benefits are described at the end of the spell's stat  block. Some heighten |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.617624 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.613269 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |

### Query 9
- Text: What does **FLICKER **[two-actions] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/62']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `21`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/62', 'PZO22001 Starfinder Player Core 330-363::/page/22/SectionHeader/8', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/32', 'PZO22001 Starfinder Player Core 330-363::/page/11/Text/66', 'PZO22001 Starfinder Player Core 330-363::/page/13/Text/64']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/62` | 0.704284 | **FLICKER **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **TELEPORTATION**  **Traditions** arcane, occult  **Duration** 1 minute  You flicker quickly between your current plane and anothe |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/22/SectionHeader/8` | 0.613099 | **PLANAR TETHER **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** varies  You |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.604682 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/66` | 0.592418 | **Spells** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/64` | 0.592418 | **Spells** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/17` | 0.582741 | OCCULT 4TH-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/71` | 0.581480 | PRIMAL 4TH-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/71` | 0.580924 | ARCANE 4TH-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.577361 | SPELL ATTACKS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.575364 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |

### Query 10
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/18', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/28', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/62', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/55', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/18` | 0.913367 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/55` | 0.913367 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/20` | 0.913367 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/62` | 0.913367 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/28` | 0.913367 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/74` | 0.871367 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/62` | 0.871367 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/59` | 0.871367 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/38` | 0.871367 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/54` | 0.871367 | **INTRODUCTION** |

### Query 11
- Text: What is the rule about Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell by preparing it in a higher-rank slot than  its normal spell rank, while a spontaneous spellcaster can  heighten a spell by casting it using a higher-rank spell slot,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `45`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/16', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/1', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/5', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.989088 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.838928 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.794402 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` | 0.779440 | As a spontaneous caster, you can also choose to cast  a lower-rank spell using a higher-rank spell slot without  heightening it or knowing it at a higher rank. This casts the  spell at the rank you kn |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.756130 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` | 0.711912 | In addition, many spells have additional specific benefits  when they are heightened, such as increased damage. These  extra benefits are described at the end of the spell's stat  block. Some heighten |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.688784 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.687049 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 0.661110 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.658312 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |

### Query 12
- Text: Summarize **REFOCUS**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/68', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/46', 'PZO22001 Starfinder Player Core 294-329::/page/9/Text/89', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/39']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/17` | 0.897040 | **REFOCUS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/68` | 0.696410 | **Focus Spells** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/39` | 0.696410 | **Focus Spells** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/46` | 0.696410 | **Focus Spells** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/89` | 0.696410 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.688347 | **CONCENTRATE** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/44` | 0.688347 | **CONCENTRATE** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/63` | 0.654410 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/64` | 0.654410 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/29` | 0.654410 | **Focus Spells** |

### Query 13
- Text: What does **ARCTIC RIFT **[two-actions] **SPELL 8** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `34`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/2', 'PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/47', 'PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/48']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/11` | 0.687337 | **ARCTIC RIFT **[two-actions] **SPELL 8**  **COLD** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Area** 120-foot line  **Defense** Fortitude  A jagged crack opens in the air, deali |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/17` | 0.670987 | OCCULT 8TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/2` | 0.666849 | ARCANE 8TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/47` | 0.628921 | **EARTHQUAKE **[two-actions] **SPELL 8**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Area** 60-foot burst  **Duration** 1 round  You shake the groun |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/48` | 0.619243 | PRIMAL 8TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/21` | 0.573750 | DIVINE 8TH-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.562059 | SPELL ATTACKS |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/51` | 0.558113 | **PHANTASMAL FLEET **[two-actions] **SPELL 8**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **500 feet; **Area** 60-foot burst  **Defense** Will  A m |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/36` | 0.547966 | **EARTHBIND **[two-actions] **SPELL 3**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 flying creature  **Defense** Fortitude; **Duration** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/18` | 0.537546 | **DIVINE INSPIRATION **[two-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine  **Range **touch;** Targets** 1 willing creature  You infuse a target with spiritual |

### Query 14
- Text: What does **BLAZING BOLT **[one-action]** TO **[three-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `18`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/20', 'PZO22001 Starfinder Player Core 294-329::/page/9/Text/6', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20` | 0.742657 | **BLAZING BOLT **[one-action]** TO **[three-actions] **SPELL 2**  **ATTACK** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets** 1 or more creatures |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/20` | 0.659580 | **Blazing Bolt**H Fire one to three flaming bolts at different foes. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/6` | 0.659580 | **Blazing Bolt**H Fire one to three flaming bolts at different foes. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.625382 | SPELL ATTACKS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/23` | 0.621465 | **ATOMIC BLAST **[three-actions] **SPELL 9**  **CONCENTRATE** **FIRE** **MANIPULATE** **RADIATION**  **Traditions** arcane, primal  **Range **500 feet;** Area** 100-foot burst **Defense** Reflex; **Du |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.590975 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` | 0.575001 | **HYPNOTIZE **[two-actions] **SPELL 3**  **ILLUSION** **MANIPULATE** **SUBTLE** **VISUAL**  **Traditions** arcane, occult  **Range **120 feet; **Area** 10-foot burst  **Defense** Will;** Duration** su |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.574164 | **LIFE SEAL **[reaction] **SPELL 3** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/42` | 0.570802 | **HOWLING BLIZZARD **[two-actions]** TO **[three-actions] **SPELL 5**  **AIR** **COLD** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Area** varies  **Defense** basic Reflex  Freezi |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/29` | 0.562094 | **BLESS **[two-actions] **SPELL 1**  **AURA** **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Area** 15-foot emanation  **Duration** 1 minute  Blessings from beyond help yo |

### Query 15
- Text: What is the rule about **Failure** The creature takes full damage.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/9', 'PZO22001 Starfinder Player Core 330-363::/page/23/Text/52', 'PZO22001 Starfinder Player Core 330-363::/page/18/Text/21', 'PZO22001 Starfinder Player Core 330-363::/page/28/Text/32', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/9` | 0.835151 | **Failure** The creature takes full damage. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/52` | 0.786943 | **Failure** The creature takes full damage and is pushed 5 feet  away from you. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/34/Text/15` | 0.785151 | **Failure** The creature takes full damage. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/21` | 0.772863 | **Failure** The creature takes full damage and is deafened for  1 round. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/32` | 0.758930 | **Failure** The creature takes full damage and is clumsy 1 for 1  minute. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/4` | 0.744793 | **Failure** The creature takes full damage, is slowed 3 until the  end of its next turn, and slowed 1 for 1 minute. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/32/Text/16` | 0.737348 | **Failure** The creature takes full damage and persistent damage. **Critical Failure** The creature takes double damage and double  persistent damage. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/34/Text/35` | 0.733827 | **Failure** The creature takes full damage and is sickened 1. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/32/Text/41` | 0.733827 | **Failure** The creature takes full damage and is sickened 1. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/24/Text/10` | 0.722863 | **Failure** The creature takes full damage and is deafened for  1 round. |

### Query 16
- Text: What is the rule about If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with more freedom in your spellcasting, but you  have fewer spells in your spell repertoire, as determined by  your character level and class. When you make your daily  preparations, all your spell slots are refreshed, but you don't  get to change the spells in your repertoire.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `49`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/26', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/5', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 1.001622 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.794969 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.751307 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.744811 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` | 0.743433 | As a spontaneous caster, you can also choose to cast  a lower-rank spell using a higher-rank spell slot without  heightening it or knowing it at a higher rank. This casts the  spell at the rank you kn |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/Text/16` | 0.696610 | If a spell's duration says it lasts until your next daily  preparations, on the next day you can refrain from preparing  a new spell in that spell's slot. (If you are a spontaneous caster,  you can in |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.688910 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.679871 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.678651 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.673082 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |

### Query 17
- Text: What does **ACID GRIP **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/16', 'PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/25', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19', 'PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/16` | 0.690187 | **ACID GRIP **[two-actions] **SPELL 2**  **ACID** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 creature  **Defense** Reflex  An ephemeral, taloned h |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/4` | 0.627322 | ARCANE 2ND-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/25` | 0.616441 | OCCULT 2ND-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19` | 0.588143 | **CAUSTIC BLAST **[two-actions] **CANTRIP 1**  **ACID** **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Area** 5-foot burst  **Defense** basic Reflex  Y |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/17` | 0.585332 | PRIMAL 2ND-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/27` | 0.549821 | **CAUSTIC CONVERSION **[two-actions] **SPELL 2**  **ACID** **ATTACK** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 creature  **Defense** AC  You lau |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/18` | 0.541267 | **Acid Grip**H Move and harm foes with a hand of acid. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/5` | 0.541267 | **Acid Grip**H Move and harm foes with a hand of acid. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/71` | 0.538755 | DIVINE 2ND-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/12` | 0.524698 | **GREASE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet;** Area** 4 contiguous 5-foot squares or** Targets** 1  object of 1 Bulk or less |

### Query 18
- Text: What is the rule about **Heightened (5th)** You can take on the appearance of a Large  humanoid. If this increases your size, you gain the effects  of the *enlarge* spell.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/8/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `29`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/8/Text/4', 'PZO22001 Starfinder Player Core 330-363::/page/11/Text/31', 'PZO22001 Starfinder Player Core 330-363::/page/0/Text/4', 'PZO22001 Starfinder Player Core 330-363::/page/22/Text/29', 'PZO22001 Starfinder Player Core 330-363::/page/11/Text/30']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/4` | 0.913400 | **Heightened (5th)** You can take on the appearance of a Large  humanoid. If this increases your size, you gain the effects  of the *enlarge* spell. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/31` | 0.724320 | **Heightened (5th)** Your battle form is Huge, and your attacks  have 15-foot reach. You instead gain 20 temporary HP,  attack modifier +18, damage bonus +2 and double damage  dice (including persiste |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/4` | 0.711393 | **ENLARGE **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Range **30 feet;** Targets** 1 willing creature  **Duration** 5 minutes  Bolstered |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/22/Text/29` | 0.687776 | **Heightened (6th)** Your battle form is Huge, and the reach of  your attacks increases by 5 feet. You instead gain AC = 22  + your level, 24 temporary HP, attack modifier +21, damage  bonus +16, and |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/30` | 0.685138 | **Heightened (4th)** Your battle form is Large, and your attacks  have 10-foot reach. You instead gain 15 temporary HP,  attack modifier +16, damage bonus +6, and Athletics +16. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/3` | 0.668685 | **Heightened (5th)** Your battle form is Huge and your attacks  have 15-foot reach. You instead gain 20 temporary HP, AC  = 18 + your level, attack modifier +18, damage bonus +7  and double the number |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/20/Text/2` | 0.661981 | **Heightened (5th)** Your battle form is Large and your fly  Speed gains a +10-foot status bonus. You instead gain 10  temporary HP, attack modifier +18, damage bonus +8, and  Acrobatics +20. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/1` | 0.642566 | traits while in this form, as well as any trait related to  the creature's kind (such as goblin or human). If this  transformation reduces your size, it reduces your reach  accordingly (typically to 5 |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/12` | 0.628135 | **Heightened (6th)** Your battle form is Large and your attacks  have 10-foot reach. You instead gain AC = 22 + your level,  15 temporary HP, an attack modifier of +23, a damage  bonus of +13, and Acr |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/2` | 0.622542 | **Heightened (4th)** Your battle form is Large and your attacks  have 10-foot reach. You instead gain 15 temporary HP, AC  = 18 + your level, attack modifier +16, damage bonus +9,  and Athletics +16. |

### Query 19
- Text: What does **FIREBALL **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/48']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/12/Text/42', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/48', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21', 'PZO22001 Starfinder Player Core 330-363::/page/30/SectionHeader/22', 'PZO22001 Starfinder Player Core 330-363::/page/0/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.727452 | **LIFE SEAL **[reaction] **SPELL 3** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/48` | 0.702645 | **FIREBALL **[two-actions] **SPELL 3**  **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Area** 20-foot burst  **Defense** basic Reflex  A roaring blast of |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.675152 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/30/SectionHeader/22` | 0.643881 | **SKYFIRE WINGS **[two-actions] **SPELL 3**  **CONCENTRATE** **ELECTRICITY** **FIRE** **MANIPULATE** **MORPH**  **Traditions** arcane, divine, occult, primal  **Duration** 1 minute  Wings of plasma gr |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/20` | 0.643517 | **ENTHRALL **[two-actions] **SPELL 3**  **AUDITORY** **CONCENTRATE** **EMOTION** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet;** Targets** all creatures in range  **Defense** Will |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.626881 | SPELL ATTACKS |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` | 0.599355 | **HYPNOTIZE **[two-actions] **SPELL 3**  **ILLUSION** **MANIPULATE** **SUBTLE** **VISUAL**  **Traditions** arcane, occult  **Range **120 feet; **Area** 10-foot burst  **Defense** Will;** Duration** su |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/36` | 0.598935 | **EARTHBIND **[two-actions] **SPELL 3**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 flying creature  **Defense** Fortitude; **Duration** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/21` | 0.596496 | **HOLY LIGHT **[two-actions] **SPELL 3**  **ATTACK** **CONCENTRATE** **FIRE** **HOLY** **LIGHT** **MANIPULATE**  **Traditions** divine, primal  **Range **120 feet;** Targets** 1 creature  **Defense** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20` | 0.594742 | **BLAZING BOLT **[one-action]** TO **[three-actions] **SPELL 2**  **ATTACK** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets** 1 or more creatures |

### Query 20
- Text: What does **ATOMIC BLAST **[three-actions] **SPELL 9** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `31`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/24', 'PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/11', 'PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/56', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/23` | 0.750915 | **ATOMIC BLAST **[three-actions] **SPELL 9**  **CONCENTRATE** **FIRE** **MANIPULATE** **RADIATION**  **Traditions** arcane, primal  **Range **500 feet;** Area** 100-foot burst **Defense** Reflex; **Du |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/24` | 0.655848 | OCCULT 9TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/11` | 0.643575 | ARCANE 9TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/56` | 0.617695 | PRIMAL 9TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.613933 | SPELL ATTACKS |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.562855 | **LIFE SEAL **[reaction] **SPELL 3** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/42` | 0.556092 | ARCANE 3RD-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/44` | 0.555309 | **FALLING STARS **[two-actions] **SPELL 9**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Area** four 40-foot bursts  **Defense** basic Reflex  You reach into t |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20` | 0.550577 | **BLAZING BOLT **[one-action]** TO **[three-actions] **SPELL 2**  **ATTACK** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets** 1 or more creatures |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/62` | 0.550557 | OCCULT 3RD-RANK SPELLS |

### Query 21
- Text: What does **FORESIGHT **[two-actions] **SPELL 9** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/26']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `27`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/32', 'PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/26', 'PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/32', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/4', 'PZO22001 Starfinder Player Core 330-363::/page/13/SectionHeader/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.647169 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/26` | 0.646574 | **FORESIGHT **[two-actions] **SPELL 9**  **CONCENTRATE** **MANIPULATE** **MENTAL** **PREDICTION**  **Traditions** arcane, divine, occult **Range **touch;** Targets** 1 creature  **Duration** 1 hour  Y |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/32` | 0.624723 | **PHANTASMAGORIA **[two-actions] **SPELL 9**  **CONCENTRATE** **DEATH** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **120 feet; **Targets** any number of creatures |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/4` | 0.616749 | **HONEYED WORDS **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes  You unlock the |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/24` | 0.612464 | OCCULT 9TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/13/SectionHeader/43` | 0.602518 | **MANIFESTATION **[three-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  You spin secrets from the fundaments of magic, shaping them  into a power |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/56` | 0.599221 | PRIMAL 9TH-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/1` | 0.566609 | **HEROISM **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult **Duration** 10 minutes |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/11` | 0.563392 | ARCANE 9TH-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.562957 | SPELL ATTACKS |

### Query 22
- Text: What does **COMMAND **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/28/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23', 'PZO22001 Starfinder Player Core 294-329::/page/30/Text/49']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/2` | 0.711935 | **COMMAND **[two-actions] **SPELL 1**  **AUDITORY** **CONCENTRATE** **LINGUISTIC** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult **Range **30 feet;** Targets** 1 creature  **Defense |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.667414 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` | 0.653674 | **CONTROL MACHINE **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature or hazard with t |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.652558 | SPELL ATTACKS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/49` | 0.652333 | **DETECT POISON **[two-actions] **SPELL 1**  **UNCOMMON** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** divine, primal  **Range **30 feet;** Targets** 1 object or creature  You detect w |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.630614 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.610228 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/39` | 0.609165 | **SUBCONSCIOUS SUGGESTION **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **LINGUISTIC** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet;** Targe |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/47` | 0.605240 | **DISPEL MAGIC **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **120 feet;** Targets** 1 spell effect or unattended magic  item  You |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/29` | 0.605110 | **STUPEFY **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** varies  You du |

### Query 23
- Text: What is the rule about With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own method of learning, preparing,  and casting spells, and every individual spell produces a  specific effect, so learning new spells gives a spellcaster  an increasing array of options to accomplish their goals.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `39`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` | 0.965533 | With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own met |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.761513 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/4` | 0.743722 | Spellcasting creates obvious sensory manifestations, such  as bright lights, crackling sounds, and sharp smells from the  gathering magic. Nearly all spells manifest a spell signature—a  colorful, glo |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/3` | 0.738987 | The casting of a spell can range from a simple word of magical  might that creates a fleeting effect to a complex process  taking hours to cast and producing a long-term impact.  Casting a spell requi |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` | 0.736973 | Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.668930 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.668351 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.664388 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.660219 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.659381 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |

### Query 24
- Text: Summarize AREAS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `34`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/18', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22', 'PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14', 'PZO22001 Starfinder Player Core 294-329::/page/14/Text/74', 'PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/18` | 0.786930 | AREAS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22` | 0.633377 | FOCUS POINTS FROM MULTIPLE  SOURCES |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14` | 0.618725 | RANGES, AREAS, AND  TARGETS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.614139 | insight about a topic. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/6` | 0.604759 | COUNTERACTING |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.552468 | **Summoned** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/48` | 0.541603 | **Bane** Weaken enemies' attacks in an aura around you. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/61` | 0.541603 | **Bane** Weaken enemies' attacks in an aura around you. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/44` | 0.535225 | **CONCENTRATE** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.535225 | **CONCENTRATE** |

### Query 25
- Text: What is the rule about traits while in this form, as well as any trait related to  the creature's kind (such as goblin or human). If this  transformation reduces your size, it reduces your reach  accordingly (typically to 5 feet). This transformation doesn't  change your statistics in any way, and you don't gain any  special abilities of the humanoid form you assume. You  can still wear and use your gear, which changes size (if  necessary) to match your new form. If items leave your  person, they return to their usual size.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/8/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `29`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/8/Text/1', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/50', 'PZO22001 Starfinder Player Core 330-363::/page/20/Text/13', 'PZO22001 Starfinder Player Core 330-363::/page/8/Text/4', 'PZO22001 Starfinder Player Core 330-363::/page/11/Text/30']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/1` | 1.004740 | traits while in this form, as well as any trait related to  the creature's kind (such as goblin or human). If this  transformation reduces your size, it reduces your reach  accordingly (typically to 5 |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/50` | 0.688155 | **HUMANOID FORM **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, occult, primal  **Duration** 10 minutes  You transform your appearance to that of a Sm |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/20/Text/13` | 0.686647 | You transform into the battle form of a Tiny animal, such as  a cat, insect, lizard, or rat. You can decide the specific type of  animal (such as a squox or praying mantis), but this has no  effect on |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/4` | 0.673939 | **Heightened (5th)** You can take on the appearance of a Large  humanoid. If this increases your size, you gain the effects  of the *enlarge* spell. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/30` | 0.672213 | **Heightened (4th)** Your battle form is Large, and your attacks  have 10-foot reach. You instead gain 15 temporary HP,  attack modifier +16, damage bonus +6, and Athletics +16. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/15` | 0.650368 | If you take on a battle form with a polymorph spell, the  special statistics can be adjusted only by circumstance  bonuses, status bonuses, and penalties. Unless otherwise  noted, the battle form prev |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/31` | 0.637288 | **Heightened (5th)** Your battle form is Huge, and your attacks  have 15-foot reach. You instead gain 20 temporary HP,  attack modifier +18, damage bonus +2 and double damage  dice (including persiste |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/12` | 0.632193 | Spells that slightly alter a creature's form have the morph trait.  Any Strikes specifically granted by a magical morph effect also  gain the magical trait. You can be affected by multiple morph  spel |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/22/Text/29` | 0.621296 | **Heightened (6th)** Your battle form is Huge, and the reach of  your attacks increases by 5 feet. You instead gain AC = 22  + your level, 24 temporary HP, attack modifier +21, damage  bonus +16, and |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/24` | 0.620219 | **Success** The creature takes half damage and no persistent  damage, and the claw moves it up to 5 feet in a direction  of your choice. |

### Query 26
- Text: What does **ENTANGLING FLORA **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `27`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/13', 'PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/37', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/32', 'PZO22001 Starfinder Player Core 330-363::/page/32/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/0/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/13` | 0.732807 | **ENTANGLING FLORA **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **PLANT** **WOOD**  **Traditions** arcane, primal  **Range **120 feet; **Area** all squares in a 20-foot burst  **Duratio |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/37` | 0.631403 | **REVEALING LIGHT **[two-actions] **SPELL 2**  **CONCENTRATE** **LIGHT** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **120 feet;** Area** 10-foot burst  **Defense** Reflex; * |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.626462 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/32/Text/2` | 0.622140 | **SOUND BODY **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You send a su |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/20` | 0.612581 | **ENTHRALL **[two-actions] **SPELL 3**  **AUDITORY** **CONCENTRATE** **EMOTION** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet;** Targets** all creatures in range  **Defense** Will |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/30` | 0.578144 | **Entangling Flora** Sprout plants to hinder movement in an area. **Environmental Endurance**H Protect a creature from severe |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.573476 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` | 0.567500 | **CLEAR MIND **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You drive menta |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/17` | 0.566370 | **Entangling Flora** Sprout plants to hinder movement in an area. **Environmental Endurance**H Protect a creature from severe  cold or heat. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20` | 0.564808 | **BLAZING BOLT **[one-action]** TO **[three-actions] **SPELL 2**  **ATTACK** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets** 1 or more creatures |

### Query 27
- Text: What does **HOWL **[two-actions] **SPELL 7** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/32', 'PZO22001 Starfinder Player Core 330-363::/page/22/SectionHeader/3', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27', 'PZO22001 Starfinder Player Core 330-363::/page/22/SectionHeader/37', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.782443 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.654193 | CHAPTER 7: SPELLS |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/22/SectionHeader/3` | 0.616995 | **PLANAR SEAL **[two-actions] **SPELL 7**  **UNCOMMON** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult **Range **120 feet; **Area** 60-foot burst **Duration** until your next da |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` | 0.615151 | **HYPNOTIZE **[two-actions] **SPELL 3**  **ILLUSION** **MANIPULATE** **SUBTLE** **VISUAL**  **Traditions** arcane, occult  **Range **120 feet; **Area** 10-foot burst  **Defense** Will;** Duration** su |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/22/SectionHeader/37` | 0.604558 | **POSSESSION **[two-actions] **SPELL 7**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL** **POSSESSION**  **Traditions** occult  **Range **30 feet; **Targets** 1 living creat |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/12` | 0.604402 | **EXECUTE **[two-actions] **SPELL 7**  **CONCENTRATE** **DEATH** **MANIPULATE** **VOID**  **Traditions** divine, primal  **Range **30 feet; **Targets** 1 creature  **Defense** basic Fortitude  You poi |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/5` | 0.596061 | OCCULT 7TH-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.568249 | SPELL ATTACKS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/34` | 0.565885 | PRIMAL 7TH-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/36` | 0.557743 | **HASTE **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Range **30 feet;** Targets** 1 creature  **Duration** 1 minute  Magic empowers the target |

### Query 28
- Text: Summarize RANGES, AREAS, AND  TARGETS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14', 'PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/16', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14` | 0.925952 | RANGES, AREAS, AND  TARGETS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20` | 0.702411 | TARGETS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/16` | 0.648479 | TOUCH RANGE |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22` | 0.647442 | FOCUS POINTS FROM MULTIPLE  SOURCES |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/23` | 0.646180 | **Range, Area, and Targets** This entry lists the range of the  spell, the area it affects, and the targets it can affect, if  any. If none of these entries are present, the spell affects  only the ca |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/7` | 0.615081 | **Range **touch;** Targets** 1 creature |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41` | 0.589768 | **ANALYZE TARGET **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **30 feet; **Targets** 1 creature  **Dur |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.583321 | insight about a topic. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/38` | 0.569813 | **Analyze** **Target**H Gather data about a target's basic physiology. **Caustic Blast**H Fling a glob of acid that splashes a small area. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/8` | 0.569813 | **Analyze** **Target**H Gather data about a target's basic physiology. **Caustic Blast**H Fling a glob of acid that splashes a small area. |

### Query 29
- Text: What does **ANT HAUL **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/22/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/8/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/16/Text/60', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/4` | 0.759731 | **ANT HAUL **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal **Range **touch; **Targets** 1 creature  **Duration** 8 hours  You reinforce the target's musculos |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/60` | 0.650846 | **Ant Haul** Target can carry more. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/30` | 0.650846 | **Ant Haul** Target can carry more. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.646210 | SPELL ATTACKS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52` | 0.623711 | **CHARM **[two-actions] **SPELL 1**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 creatur |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.609976 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` | 0.570998 | **HYPNOTIZE **[two-actions] **SPELL 3**  **ILLUSION** **MANIPULATE** **SUBTLE** **VISUAL**  **Traditions** arcane, occult  **Range **120 feet; **Area** 10-foot burst  **Defense** Will;** Duration** su |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.568589 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.567286 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/31/SectionHeader/22` | 0.564257 | **SOOTHE **[two-actions] **SPELL 1**  **CONCENTRATE** **EMOTION** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** occult  **Range **30 feet;** Targets** 1 willing creature  **Duration** 1 minute |

### Query 30
- Text: Summarize Cone of piercing
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/505']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `12`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/505', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/493', 'PZO22001 Starfinder Player Core 330-363::/page/11/ListItem/28', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/497', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/501']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/505` | 0.778333 | Cone of piercing (Reflex) |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/493` | 0.594195 | Cone of poison (Fortitude) |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/11/ListItem/28` | 0.568664 | piercing plus 1d4 persistent poison; **Melee **[one-action] pincer  (agile), **Damage **1d6 bludgeoning. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/497` | 0.562066 | Cone of mental (Will) |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/501` | 0.525584 | Cone of spirit (Will) |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/21/ListItem/19` | 0.518887 | **Bull** Speed 30 feet; **Melee **[one-action] horn, **Damage **2d8 piercing. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/21/ListItem/20` | 0.489672 | **Canine** Speed 40 feet; **Melee **[one-action] jaws, **Damage **2d8  piercing. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.486241 | insight about a topic. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/51` | 0.484145 | **Shadow Blast**H Shape a damaging cone of shadow substance  to deal damage of a type you choose. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/60` | 0.484145 | **Shadow Blast**H Shape a damaging cone of shadow substance  to deal damage of a type you choose. |

### Query 31
- Text: What is the rule about You rapidly catalog and collate information relevant to  your current situation. You can instantly use up to 6 Recall  Knowledge actions as part of Casting this Spell. For these?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/8/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `15`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/8/Text/25', 'PZO22001 Starfinder Player Core 330-363::/page/28/Text/66', 'PZO22001 Starfinder Player Core 330-363::/page/27/SectionHeader/42', 'PZO22001 Starfinder Player Core 330-363::/page/13/Text/11', 'PZO22001 Starfinder Player Core 330-363::/page/24/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/25` | 0.985222 | You rapidly catalog and collate information relevant to  your current situation. You can instantly use up to 6 Recall  Knowledge actions as part of Casting this Spell. For these |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/5` | 0.654807 | If you want to identify a spell but don't have it prepared  or in your repertoire, you must spend an action on your  turn attempting to identify it using Recall Knowledge. You  typically notice a spel |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.633775 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.619814 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/66` | 0.609486 | **SIFT THE SPHERE** **SPELL 2**  **CONCENTRATE** **MANIPULATE** **PREDICTION**  **Traditions** divine, occult  **Cast** 10 minutes  You ritually sift through the local infosphere and gain  mystical in |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/27/SectionHeader/42` | 0.609244 | **SENDING **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult  **Range **planetary;** Targets** 1 creature you know well  You send the creat |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/11` | 0.606951 | **LOCATE** **SPELL 3**  **UNCOMMON** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** arcane, divine, occult  **Cast** 10 minutes  **Range **500 feet;** Targets** 1 specific object or type |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/24/Text/20` | 0.606207 | **READ OMENS** **SPELL 4**  **UNCOMMON** **CONCENTRATE** **MANIPULATE** **PREDICTION**  **Traditions** divine, occult  **Cast** 10 minutes  You peek into the future. Choose a particular goal or activi |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21` | 0.588143 | **CONTINGENCY** **SPELL 7**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane  **Cast** 10 minutes **Duration** until your next daily preparations  You prepare a spell that will trigger later. Wh |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 0.579220 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |

### Query 32
- Text: What is the rule about **Spell Lists**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/63']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `21`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/27/Text/63', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/68', 'PZO22001 Starfinder Player Core 330-363::/page/15/Text/61', 'PZO22001 Starfinder Player Core 330-363::/page/25/Text/61', 'PZO22001 Starfinder Player Core 330-363::/page/19/Text/73']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/63` | 0.782608 | **Spell Lists** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/73` | 0.782608 | **Spell Lists** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/61` | 0.782608 | **Spell Lists** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/61` | 0.782608 | **Spell Lists** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/68` | 0.782608 | **Spell Lists** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/65` | 0.740608 | **Spell Lists** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/63` | 0.740608 | **Spell Lists** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/62` | 0.740608 | **Spell Lists** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/63` | 0.740608 | **Spell Lists** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/46` | 0.740608 | **Spell Lists** |

### Query 33
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/64']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/23/Text/65', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/58', 'PZO22001 Starfinder Player Core 330-363::/page/27/Text/60', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/64', 'PZO22001 Starfinder Player Core 330-363::/page/25/Text/58']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/64` | 0.777771 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/58` | 0.777771 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/58` | 0.777771 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/60` | 0.777771 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/65` | 0.777771 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/58` | 0.735771 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/59` | 0.735771 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/61` | 0.735771 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/42` | 0.735771 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/61` | 0.735771 | **SKILLS** |

### Query 34
- Text: Summarize **Requirements** You have a focus pool.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `31`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/16', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/15', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/89']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/19` | 1.016705 | **Requirements** You have a focus pool. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` | 0.736685 | FOCUS SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/16` | 0.729593 | You replenish all the Focus Points in your pool during your  daily preparations. You can also use the Refocus activity to  pray, study, meditate, or otherwise reattune yourself to the  source of your |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` | 0.726769 | Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your p |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/89` | 0.701013 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` | 0.670136 | **CONCENTRATE** **MANIPULATE** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.662878 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/63` | 0.659013 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/68` | 0.659013 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/71` | 0.659013 | **Focus Spells** |

### Query 35
- Text: What is the rule about **Failure** The creature takes full damage, is slowed 3 until the  end of its next turn, and slowed 1 for 1 minute.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/4', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/5', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/3', 'PZO22001 Starfinder Player Core 330-363::/page/28/Text/32', 'PZO22001 Starfinder Player Core 330-363::/page/18/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/4` | 0.898758 | **Failure** The creature takes full damage, is slowed 3 until the  end of its next turn, and slowed 1 for 1 minute. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/5` | 0.822819 | **Critical Failure** The creature takes double damage, is slowed  3 until the end of its next turn, and slowed 2 for 1 minute. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/20` | 0.809216 | **Failure** The creature takes full damage and is slowed 1 until  the start of your next turn. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/13` | 0.809216 | **Failure** The creature takes full damage and is slowed 1 until the  start of your next turn. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/3` | 0.795244 | **Success** The creature takes half damage and is slowed 1 until  the end of its next turn. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/32` | 0.784575 | **Failure** The creature takes full damage and is clumsy 1 for 1  minute. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/21` | 0.772023 | **Failure** The creature takes full damage and is deafened for  1 round. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/24/Text/10` | 0.722023 | **Failure** The creature takes full damage and is deafened for  1 round. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/33` | 0.714359 | **Critical Failure** The creature takes full damage and is clumsy  2 for 1 minute. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/32/Text/42` | 0.709901 | **Critical Failure** The creature takes full damage and is sickened  2; while it's sickened, it's also slowed 1. |

### Query 36
- Text: What does **ENTROPY STRIKE **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `27`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/32', 'PZO22001 Starfinder Player Core 330-363::/page/0/Text/20', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/42', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/32` | 0.695545 | **ENTROPY STRIKE **[two-actions] **SPELL 3**  **ACID** **ATTACK** **CONCENTRATE** **MANIPULATE** **VOID**  **Traditions** arcane, divine, occult  **Range **30 feet; **Targets** 1 creature or unattende |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/20` | 0.647610 | **ENTHRALL **[two-actions] **SPELL 3**  **AUDITORY** **CONCENTRATE** **EMOTION** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet;** Targets** all creatures in range  **Defense** Will |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.627073 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.617132 | **LIFE SEAL **[reaction] **SPELL 3** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` | 0.608508 | **HYPNOTIZE **[two-actions] **SPELL 3**  **ILLUSION** **MANIPULATE** **SUBTLE** **VISUAL**  **Traditions** arcane, occult  **Range **120 feet; **Area** 10-foot burst  **Defense** Will;** Duration** su |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.564999 | SPELL ATTACKS |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/23` | 0.558017 | **SHARE PAIN **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **30 feet;** Targets** 1 creature  **Defense** Will  You telepathically shar |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/15` | 0.555461 | **PARALYZE **[two-actions] **SPELL 3**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature  **Defense** Will; **Durat |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/18` | 0.554221 | **FELINE SENSES **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MORPH**  **Traditions** divine, primal  **Duration** 1 hour |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/29` | 0.552317 | **STUPEFY **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** varies  You du |

### Query 37
- Text: What does **CHILLING DARKNESS **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6', 'PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/51', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36', 'PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/22', 'PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/62']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6` | 0.730003 | **CHILLING DARKNESS **[two-actions] **SPELL 3**  **ATTACK** **COLD** **CONCENTRATE** **DARKNESS** **MANIPULATE** **UNHOLY**  **Traditions** divine  **Range **120 feet;** Targets** 1 creature  **Defens |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/51` | 0.629152 | **DARKVISION **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Duration** 1 hour  You grant yourself supernatural sight in areas of darkness |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36` | 0.627407 | **BLINDNESS **[two-actions] **SPELL 3**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet;** Targets** 1 creature  **Defense** Fortit |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.617053 | **LIFE SEAL **[reaction] **SPELL 3** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.616408 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/22` | 0.614763 | DIVINE 3RD-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/62` | 0.613244 | OCCULT 3RD-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/21` | 0.589320 | **HOLY LIGHT **[two-actions] **SPELL 3**  **ATTACK** **CONCENTRATE** **FIRE** **HOLY** **LIGHT** **MANIPULATE**  **Traditions** divine, primal  **Range **120 feet;** Targets** 1 creature  **Defense** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/23` | 0.579523 | **SHARE PAIN **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **30 feet;** Targets** 1 creature  **Defense** Will  You telepathically shar |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` | 0.569656 | **HYPNOTIZE **[two-actions] **SPELL 3**  **ILLUSION** **MANIPULATE** **SUBTLE** **VISUAL**  **Traditions** arcane, occult  **Range **120 feet; **Area** 10-foot burst  **Defense** Will;** Duration** su |

### Query 38
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/24']
- Expected found: `True`
- Expected rank: `12`
- Graph boost applied: `True`
- Graph boosted count: `29`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/27/Text/68', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/59', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/65', 'PZO22001 Starfinder Player Core 294-329::/page/31/Text/60', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/61']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/65` | 0.806592 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/68` | 0.806592 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/59` | 0.806592 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/61` | 0.806592 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/60` | 0.806592 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/86` | 0.764592 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/68` | 0.764592 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/86` | 0.764592 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.764592 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.764592 | **SPELLS** |

### Query 39
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/57']
- Expected found: `True`
- Expected rank: `12`
- Graph boost applied: `True`
- Graph boosted count: `22`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/63', 'PZO22001 Starfinder Player Core 330-363::/page/11/Text/60', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/41', 'PZO22001 Starfinder Player Core 330-363::/page/19/Text/68', 'PZO22001 Starfinder Player Core 330-363::/page/23/Text/64']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/63` | 0.866254 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/60` | 0.866254 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/41` | 0.866254 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/64` | 0.866254 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/68` | 0.866254 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/59` | 0.824254 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/41` | 0.824254 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/57` | 0.824254 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/57` | 0.824254 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/60` | 0.824254 | **CLASSES** |

### Query 40
- Text: What is the rule about The practitioners of occult traditions seek  to understand the unexplainable, categorize  the bizarre, and otherwise access the ephemeral in a?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `33`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/15', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/18', 'PZO22001 Starfinder Player Core 294-329::/page/14/Text/74']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/14` | 0.949293 | The practitioners of occult traditions seek  to understand the unexplainable, categorize  the bizarre, and otherwise access the ephemeral in a |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.630738 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.625381 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.579911 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.569271 | insight about a topic. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/24` | 0.568948 | **Traditions** occult |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/34` | 0.553408 | **Traditions** divine, occult, primal |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/6` | 0.539048 | **Traditions** arcane, divine, occult, primal |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/19` | 0.527662 | are determined by their connection, and a witchwarper's are  determined by their paradox. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.523366 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |

### Query 41
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/63']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/63', 'PZO22001 Starfinder Player Core 330-363::/page/11/Text/60', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/41', 'PZO22001 Starfinder Player Core 330-363::/page/19/Text/68', 'PZO22001 Starfinder Player Core 330-363::/page/23/Text/64']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/63` | 0.866254 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/60` | 0.866254 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/41` | 0.866254 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/64` | 0.866254 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/68` | 0.866254 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/59` | 0.824254 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/41` | 0.824254 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/57` | 0.824254 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/57` | 0.824254 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/60` | 0.824254 | **CLASSES** |

### Query 42
- Text: What is the rule about The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any number of times per day. If you're a prepared caster, you  can prepare a specific number of cantrips each day. You can't  prepare a cantrip in a spell slot.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `48`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/9', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/26', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/5', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` | 1.021436 | The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any nu |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 0.858159 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.780862 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.780049 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/17` | 0.727553 | Each spell uses the following format. Entries appear only  when applicable, so not all spells will have every entry  described here. The spell's name line also lists the type  of spell if it's a cantr |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.681533 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/9` | 0.669950 | A cantrip is a special type of spell that's weaker than other  spells but can be used with greater freedom and flexibility. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 0.668470 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.666984 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.653084 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |

### Query 43
- Text: Summarize **ALIEN CORE DRAGONS**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `17`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 330-363::/page/0/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/11/Text/70', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/7', 'PZO22001 Starfinder Player Core 330-363::/page/8/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/1` | 0.872822 | **ALIEN CORE DRAGONS** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/2` | 0.712068 | The dragons from *Alien Core* use the following  specifications for *dragon form*. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/70` | 0.584269 | **GAME** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/7` | 0.570875 | **Range **touch;** Targets** 1 creature |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.562539 | **CONCENTRATE** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/6` | 0.562227 | **Arcane** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/79` | 0.534269 | **GAME** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/4` | 0.531072 | **DRAGON FORM **[two-actions] **SPELL 6**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, divine, occult, primal  **Duration** 1 minute  Calling upon powerful magic, you gain a L |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.530403 | **SUBTLE SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13` | 0.527209 | **Occult** |

### Query 44
- Text: What does **EVERLIGHT **[three-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/6', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/42', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21', 'PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/37', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/6` | 0.699784 | **EVERLIGHT **[three-actions] **SPELL 2**  **CONCENTRATE** **LIGHT** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **touch; **Targets** a gemstone worth 60 credits or more **D |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.671106 | **LIFE SEAL **[reaction] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.662204 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/37` | 0.646981 | **REVEALING LIGHT **[two-actions] **SPELL 2**  **CONCENTRATE** **LIGHT** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **120 feet;** Area** 10-foot burst  **Defense** Reflex; * |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/21` | 0.642727 | **HOLY LIGHT **[two-actions] **SPELL 3**  **ATTACK** **CONCENTRATE** **FIRE** **HOLY** **LIGHT** **MANIPULATE**  **Traditions** divine, primal  **Range **120 feet;** Targets** 1 creature  **Defense** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.590827 | SPELL ATTACKS |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.587332 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/20` | 0.577435 | **ENTHRALL **[two-actions] **SPELL 3**  **AUDITORY** **CONCENTRATE** **EMOTION** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet;** Targets** all creatures in range  **Defense** Will |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` | 0.575830 | **HYPNOTIZE **[two-actions] **SPELL 3**  **ILLUSION** **MANIPULATE** **SUBTLE** **VISUAL**  **Traditions** arcane, occult  **Range **120 feet; **Area** 10-foot burst  **Defense** Will;** Duration** su |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/44` | 0.574741 | **Success** The light affects the creature for 2 rounds. |

### Query 45
- Text: Summarize DURATIONS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/15', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/8/Text/53', 'PZO22001 Starfinder Player Core 294-329::/page/14/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/9` | 0.806102 | DURATIONS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/15` | 0.775048 | LONG DURATIONS |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/8` | 0.651307 | **Duration** 5 minutes |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/48` | 0.642875 | **Duration** 1 minute |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.629098 | **SUBTLE SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/53` | 0.613332 | **Mindlink** Mentally impart 10 minutes worth of information  in an instant. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/14` | 0.612439 | **Mindlink** Mentally impart 10 minutes' worth of information  in an instant. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/32/Text/31` | 0.610399 | **Heightened (4th)** The duration is 8 hours. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/18` | 0.601128 | **FELINE SENSES **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MORPH**  **Traditions** divine, primal  **Duration** 1 hour |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/1` | 0.599776 | **HEROISM **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult **Duration** 10 minutes |

### Query 46
- Text: What is the rule about You unleash the power of a supermassive black hole. All  creatures in the area take 6d10 bludgeoning and 6d10 void  damage. *Event horizon* ignores up to 10 resistance creatures  in the area have to bludgeoning, and up to 10 resistance they  have to void. Each creature attempts a Reflex save.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `35`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/1', 'PZO22001 Starfinder Player Core 330-363::/page/14/SectionHeader/7', 'PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/3', 'PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/44', 'PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/1` | 0.956848 | You unleash the power of a supermassive black hole. All  creatures in the area take 6d10 bludgeoning and 6d10 void  damage. *Event horizon* ignores up to 10 resistance creatures  in the area have to b |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/14/SectionHeader/7` | 0.669571 | **MASSACRE **[two-actions] **SPELL 9**  **CONCENTRATE** **DEATH** **MANIPULATE** **VOID**  **Traditions** arcane, divine, primal  **Area** 60-foot line  **Defense** Fortitude  You unleash a wave of de |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/3` | 0.658605 | **OVERLOAD SYSTEMS **[two-actions] **SPELL 5**  **CONCENTRATE** **ELECTRICITY** **MANIPULATE**  **Traditions** arcane, primal  **Area** 60-foot cone  **Defense** Reflex  You flood the area with a wave |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/44` | 0.655668 | **FALLING STARS **[two-actions] **SPELL 9**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Area** four 40-foot bursts  **Defense** basic Reflex  You reach into t |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/43` | 0.652720 | **PUMMELING RUBBLE **[two-actions] **SPELL 1**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Area** 15-foot cone  **Defense** Reflex  A spray of heavy rocks flies through |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/6` | 0.640415 | **ECLIPSE BURST **[two-actions] **SPELL 7**  **COLD** **CONCENTRATE** **DARKNESS** **MANIPULATE** **VOID**  **Traditions** arcane, divine, primal **Range **500 feet;** Area** 60-foot burst  **Defense* |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/5` | 0.628251 | **CATACLYSM **[two-actions] **SPELL 10**  **ACID** **AIR** **COLD** **CONCENTRATE** **EARTH** **ELECTRICITY** **FIRE** **MANIPULATE** **WATER**  **Traditions** arcane, primal  **Range **1,000 feet;** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/15` | 0.605201 | **Success** The creature takes 9d6 void damage. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/10/SectionHeader/25` | 0.604812 | **IMPLOSION **[two-actions] **SPELL 9**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet;** Targets** 1 corporeal creature  **Defense** basic Fortitude; **Duration** s |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/18/SectionHeader/55` | 0.601804 | **OVERHEAT **[two-actions] **SPELL 1**  **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets **1 creature  **Defense** basic Reflex  You vent heat towar |

### Query 47
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/19']
- Expected found: `True`
- Expected rank: `11`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/35/Text/63', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/56', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/60', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/31', 'PZO22001 Starfinder Player Core 294-329::/page/31/Text/55']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/63` | 0.830013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/56` | 0.830013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/60` | 0.830013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/31` | 0.830013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/55` | 0.830013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/54` | 0.788013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/21` | 0.788013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/39` | 0.788013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/63` | 0.788013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/69` | 0.788013 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 48
- Text: What is the rule about After Triune's Signal connected cultures across the  Universe, the peoples of the galaxy have learned more  than ever before about the Universe's composition  thanks to science and technology. As technology  improves and creates mass-market marvels rivaling  what was once only possible for a powerful spellcaster,  magic is more static, with arcane universities,  occult societies, and religious orders preserving  ancient techniques and tomes into the modern  era. Many specialty tech items incorporate hybrid  magitechnology, and most spellcasters carry a backup  gun or other tech gear on them for when they run  out of spells. Magic and technology coexist, but most  spellcasters use analog spellcasting, and blending the  two together to create a hybrid item requires training.  Only a few spellcasters mix magic with technology they're seen as mavericks by most established magical  institutions. Technomancers and spellcasters who  have learned to command machines or connect with  computers using magic blaze a trail few have explored.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `41`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/12', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/12` | 0.973560 | After Triune's Signal connected cultures across the  Universe, the peoples of the galaxy have learned more  than ever before about the Universe's composition  thanks to science and technology. As tech |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` | 0.641306 | Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.632077 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.631796 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/8` | 0.592186 | If you're a prepared spellcaster—such as a technomancer  (see *Starfinder Tech Core*)—you must spend time each day  preparing spells for that day. At the start of your daily  preparations, you select |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` | 0.556846 | With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own met |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.547997 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/17` | 0.543336 | Magic with the illusion trait creates false sensory stimuli.  Sometimes illusions allow creatures a chance to disbelieve  the spell, which lets the creature ignore the spell if it succeeds  at doing s |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/2` | 0.542726 | The grand variety of spells includes those in the following pages and far more. Taught at magical  academies, drawn from other worlds, bestowed by mystical connections, and granted by all manner of  u |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.537977 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |

### Query 49
- Text: Summarize Host
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/502']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `8`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/502', 'PZO22001 Starfinder Player Core 330-363::/page/8/Text/23', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/44', 'PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/502` | 0.760635 | Host |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/8` | 0.577015 | HOSTILE ACTIONS |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.543279 | **CONCENTRATE** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/44` | 0.543279 | **CONCENTRATE** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.531221 | insight about a topic. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` | 0.528975 | **CONCENTRATE** **MANIPULATE** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.517316 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22` | 0.511689 | FOCUS POINTS FROM MULTIPLE  SOURCES |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.510844 | **Summoned** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/34` | 0.497811 | **Shrink**H Reduce a willing creature to Tiny size. |

### Query 50
- Text: What is the rule about Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, though it's generally poor at affecting the spirit or  the soul. Witchwarpers who analyze probability and  spellcasters who draw magic from the underlying code  of the Universe are practitioners of arcane magic.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `47`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 1.005577 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/2` | 0.691819 | Spellcasters cast spells from one of four different spell lists, each representing a different magical tradition: arcane,  divine, occult, and primal. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` | 0.688762 | Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.683211 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.661405 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/1` | 0.609729 | Whether it comes in the form of eldritch artifacts, otherworldly beings, or witchwarpers altering  reality with strange spells, magic brings fantasy and wonder to Starfinder. This chapter explains how |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` | 0.606975 | With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own met |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.605866 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/14` | 0.590419 | The practitioners of occult traditions seek  to understand the unexplainable, categorize  the bizarre, and otherwise access the ephemeral in a |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/4` | 0.578299 | Spellcasting creates obvious sensory manifestations, such  as bright lights, crackling sounds, and sharp smells from the  gathering magic. Nearly all spells manifest a spell signature—a  colorful, glo |

### Query 51
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/67']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `21`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/33/Text/64', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/67', 'PZO22001 Starfinder Player Core 330-363::/page/17/Text/45', 'PZO22001 Starfinder Player Core 330-363::/page/19/Text/72', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/61']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.806592 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.806592 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.806592 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.806592 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.806592 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.764592 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.764592 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.764592 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.764592 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/62` | 0.764592 | **SPELLS** |

### Query 52
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/41']
- Expected found: `True`
- Expected rank: `9`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/29', 'PZO22001 Starfinder Player Core 294-329::/page/15/Text/85', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/91', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/79', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/64']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/29` | 0.938833 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/85` | 0.938833 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/91` | 0.938833 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/79` | 0.938833 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/64` | 0.938833 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/70` | 0.896833 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/88` | 0.896833 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/65` | 0.896833 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/41` | 0.896833 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/48` | 0.896833 | **PLAYING THE ** **GAME** |

### Query 53
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/22']
- Expected found: `True`
- Expected rank: `16`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/24', 'PZO22001 Starfinder Player Core 294-329::/page/9/Text/84', 'PZO22001 Starfinder Player Core 294-329::/page/15/Text/78', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/66', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/59']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/66` | 0.735680 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/24` | 0.735680 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/84` | 0.735680 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/78` | 0.735680 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/59` | 0.735680 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/81` | 0.693680 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/32` | 0.693680 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/66` | 0.693680 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/63` | 0.693680 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/58` | 0.693680 | **FEATS** |

### Query 54
- Text: Summarize 7 PLAYER CORE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/0']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/0', 'PZO22001 Starfinder Player Core 330-363::/page/15/SectionHeader/0', 'PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/0', 'PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/0` | 0.937057 | 7 PLAYER CORE |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/15/SectionHeader/0` | 0.937057 | 7 PLAYER CORE |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/0` | 0.937057 | 7 PLAYER CORE |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/0` | 0.937057 | 7 PLAYER CORE |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/34` | 0.617430 | PRIMAL 7TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.592220 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.585704 | CHAPTER 7: SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/5` | 0.576973 | OCCULT 7TH-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/57` | 0.569744 | ARCANE 7TH-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/11` | 0.551292 | DIVINE 7TH-RANK SPELLS |

### Query 55
- Text: Summarize **Divine**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/45']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9` | 0.857907 | **Divine** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/499` | 0.653043 | Divine |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/45` | 0.628489 | **Traditions** divine, primal |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.622090 | **SUBTLE SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.619070 | **Summoned** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13` | 0.613413 | **Occult** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/45` | 0.609440 | DIVINE 1ST-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/34` | 0.603020 | **Traditions** divine, occult, primal |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/6` | 0.579213 | **Traditions** arcane, divine, occult, primal |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.567918 | **CONCENTRATE** |

### Query 56
- Text: Summarize **CONCENTRATE** **MANIPULATE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5', 'PZO22001 Starfinder Player Core 330-363::/page/8/Text/23', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/44', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/32', 'PZO22001 Starfinder Player Core 330-363::/page/33/Text/67']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` | 0.971250 | **CONCENTRATE** **MANIPULATE** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.834510 | **CONCENTRATE** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/44` | 0.834510 | **CONCENTRATE** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/18` | 0.743427 | **CONCENTRATE** **EXPLORATION** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.742679 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/67` | 0.724155 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/64` | 0.682155 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/70` | 0.682155 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/67` | 0.682155 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/63` | 0.682155 | **Focus Spells** |

### Query 57
- Text: What is the rule about **Focus Spells**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/27']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `29`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/23/Text/46', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/62', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/89', 'PZO22001 Starfinder Player Core 294-329::/page/27/Text/71', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/68']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/46` | 0.849140 | **Focus Spells** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/62` | 0.849140 | **Focus Spells** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/89` | 0.849140 | **Focus Spells** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/68` | 0.849140 | **Focus Spells** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/71` | 0.849140 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/63` | 0.807140 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/39` | 0.807140 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/27` | 0.807140 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/89` | 0.807140 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/86` | 0.807140 | **Focus Spells** |

### Query 58
- Text: Summarize LINE OF EFFECT
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `31`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/7', 'PZO22001 Starfinder Player Core 294-329::/page/14/Text/74', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/25', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/7` | 0.893147 | LINE OF EFFECT |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.612539 | insight about a topic. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.596336 | **SUBTLE SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/25` | 0.592657 | A horizontal line follows defense and duration, and the  effects of the spell are described after this line. This section  might also detail the possible results of a saving throw:  critical success, |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/13` | 0.584803 | SPONTANEOUS SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22` | 0.536078 | FOCUS POINTS FROM MULTIPLE  SOURCES |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` | 0.531853 | **CONCENTRATE** **MANIPULATE** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/19/ListItem/45` | 0.531353 | Low-light vision. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/11/ListItem/19` | 0.523353 | Low-light vision. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/22/ListItem/24` | 0.523353 | Low-light vision. |

### Query 59
- Text: What is the rule about actions, you can't use any special abilities, reactions, or free  actions that trigger when you Recall Knowledge.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/8/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `32`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/8/Text/26', 'PZO22001 Starfinder Player Core 330-363::/page/8/Text/25', 'PZO22001 Starfinder Player Core 330-363::/page/26/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/17/SectionHeader/14', 'PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/28']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/26` | 0.899669 | actions, you can't use any special abilities, reactions, or free  actions that trigger when you Recall Knowledge. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/25` | 0.605032 | You rapidly catalog and collate information relevant to  your current situation. You can instantly use up to 6 Recall  Knowledge actions as part of Casting this Spell. For these |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/26/Text/2` | 0.579891 | **REWRITE MEMORY **[two-actions] **SPELL 4**  **UNCOMMON** **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult  **Range **30 feet; **Targets** 1 creature **Defense** Will; **Duration** un |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/17/SectionHeader/14` | 0.566907 | **NEVER MIND **[two-actions] **SPELL 6**  **CONCENTRATE** **CURSE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature **Defense** W |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/28` | 0.566507 | **RETROCOGNITION** **SPELL 7**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Cast** 1 minute  **Duration** sustained  Opening your mind to mental echoes, you gain impressions  from |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/12` | 0.546664 | **AKASHIC DOWNLOAD **[three-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** occult  **Requirements** You have a comm unit or computer, used as  a locus.  **Duration** 1 day  You e |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/5` | 0.534002 | If you want to identify a spell but don't have it prepared  or in your repertoire, you must spend an action on your  turn attempting to identify it using Recall Knowledge. You  typically notice a spel |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47` | 0.518418 | **REVIVAL **[two-actions] **SPELL 10**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet;** Targets** dead creatures and living creatures of  y |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/34` | 0.511438 | **FREEZE TIME **[three-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  You temporarily stop time for everything but yourself,  allowing you to use several actions |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/24/Text/45` | 0.511061 | **REMAKE** **SPELL 10**  **UNCOMMON** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Cast** 1 hour; **Cost** a remnant of the item  **Range **5 feet  You fully re-crea |

### Query 60
- Text: What does **BANISHMENT **[two-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26', 'PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/7', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29', 'PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/40', 'PZO22001 Starfinder Player Core 294-329::/page/15/Text/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26` | 0.738083 | **BANISHMENT **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet; **Targets** 1 creature that isn't on its |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/7` | 0.619117 | PRIMAL 5TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` | 0.616166 | **CONTROL MACHINE **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature or hazard with t |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/40` | 0.615724 | OCCULT 5TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/41` | 0.611046 | **Banishment**H Send a creature back to its home plane. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/18/Text/8` | 0.581046 | **Banishment**H Send a creature back to its home plane. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/39` | 0.574811 | **SUBCONSCIOUS SUGGESTION **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **LINGUISTIC** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet;** Targe |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/55` | 0.569046 | **Banishment**H Send a creature back to its home plane. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/16` | 0.569046 | **Banishment**H Send a creature back to its home plane. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/15` | 0.568222 | ARCANE 5TH-RANK SPELLS |

### Query 61
- Text: Summarize Occult
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/495']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `21`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/495', 'PZO22001 Starfinder Player Core 330-363::/page/8/Text/24', 'PZO22001 Starfinder Player Core 330-363::/page/16/ListItem/3', 'PZO22001 Starfinder Player Core 330-363::/page/16/ListItem/46', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/495` | 0.832515 | Occult |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13` | 0.716491 | **Occult** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/24` | 0.652188 | **Traditions** occult |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/16/ListItem/3` | 0.599677 | Darkvision. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/16/ListItem/46` | 0.599677 | Darkvision. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/34` | 0.584479 | **Traditions** divine, occult, primal |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/35/ListItem/2` | 0.549677 | Darkvision. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/22/ListItem/48` | 0.549677 | Darkvision. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.543819 | insight about a topic. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/58` | 0.539138 | OCCULT 1ST-RANK SPELLS |

### Query 62
- Text: What does **FIRE SHIELD **[two-actions] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/41']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `29`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/12/Text/42', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/41', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/37', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/48', 'PZO22001 Starfinder Player Core 330-363::/page/18/Text/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.654366 | **LIFE SEAL **[reaction] **SPELL 3** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/41` | 0.653313 | **FIRE SHIELD **[two-actions] **SPELL 4**  **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Duration** 1 minute  You create a hovering shield made of fire. As long as the  shi |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/37` | 0.630808 | **IGNITION **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Targets** 1 creature  **Defense** AC  You |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/48` | 0.627587 | **FIREBALL **[two-actions] **SPELL 3**  **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Area** 20-foot burst  **Defense** basic Reflex  A roaring blast of |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/3` | 0.620681 | **NIGHTMARE** **SPELL 4**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Cast** 10 minutes  **Range **planetary;** Targets** 1 creature you know by name  **D |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.597061 | SPELL ATTACKS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/17` | 0.590490 | OCCULT 4TH-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.588701 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/71` | 0.578726 | ARCANE 4TH-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/30/SectionHeader/22` | 0.568201 | **SKYFIRE WINGS **[two-actions] **SPELL 3**  **CONCENTRATE** **ELECTRICITY** **FIRE** **MANIPULATE** **MORPH**  **Traditions** arcane, divine, occult, primal  **Duration** 1 minute  Wings of plasma gr |

### Query 63
- Text: Summarize **Rituals**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/30']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `30`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/31/Text/64', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/27/Text/72', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/69', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/47']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/64` | 0.889916 | **Rituals** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/30` | 0.889916 | **Rituals** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/72` | 0.889916 | **Rituals** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/69` | 0.889916 | **Rituals** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/47` | 0.889916 | **Rituals** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/28` | 0.847916 | **Rituals** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/78` | 0.847916 | **Rituals** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/84` | 0.847916 | **Rituals** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/90` | 0.847916 | **Rituals** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/90` | 0.847916 | **Rituals** |

### Query 64
- Text: What is the rule about A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `38`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/14', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/26', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/1', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 0.985015 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` | 0.797923 | Focus spells are automatically heightened to half your level  rounded up, just like cantrips are. You can't cast a focus spell  if its minimum rank is greater than half your level rounded  up, even if |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.742762 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.726737 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.691067 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` | 0.635113 | The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any nu |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.625087 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/17` | 0.622566 | Each spell uses the following format. Entries appear only  when applicable, so not all spells will have every entry  described here. The spell's name line also lists the type  of spell if it's a cantr |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.610825 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` | 0.610311 | In addition, many spells have additional specific benefits  when they are heightened, such as increased damage. These  extra benefits are described at the end of the spell's stat  block. Some heighten |

### Query 65
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/31']
- Expected found: `True`
- Expected rank: `14`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/29', 'PZO22001 Starfinder Player Core 294-329::/page/15/Text/85', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/91', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/79', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/64']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/29` | 0.938833 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/85` | 0.938833 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/91` | 0.938833 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/79` | 0.938833 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/64` | 0.938833 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/70` | 0.896833 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/88` | 0.896833 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/65` | 0.896833 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/41` | 0.896833 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/48` | 0.896833 | **PLAYING THE ** **GAME** |

### Query 66
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/20']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/18', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/28', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/62', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/55', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/18` | 0.913367 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/55` | 0.913367 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/20` | 0.913367 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/62` | 0.913367 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/28` | 0.913367 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/74` | 0.871367 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/62` | 0.871367 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/59` | 0.871367 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/38` | 0.871367 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/54` | 0.871367 | **INTRODUCTION** |

### Query 67
- Text: Summarize **MAGICAL TRADITIONS**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `29`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/40', 'PZO22001 Starfinder Player Core 294-329::/page/15/Text/84', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/90']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1` | 0.898082 | **MAGICAL TRADITIONS** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/30` | 0.721920 | **Rituals** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/40` | 0.721920 | **Rituals** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/90` | 0.721920 | **Rituals** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/84` | 0.721920 | **Rituals** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/37` | 0.679920 | **Rituals** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/64` | 0.679920 | **Rituals** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/69` | 0.679920 | **Rituals** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/72` | 0.679920 | **Rituals** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/47` | 0.679920 | **Rituals** |

### Query 68
- Text: Summarize Climb
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/504']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `17`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/504', 'PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/19', 'PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/5', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/488', 'PZO22001 Starfinder Player Core 330-363::/page/24/SectionHeader/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/504` | 0.834968 | Climb |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/19` | 0.548010 | **STUMBLE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **100 feet; **Targets** 1 creature  **Defense** Reflex  A burst of micrograv |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.547817 | insight about a topic. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/5` | 0.546600 | **STABILIZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet; **Targets** 1 dying creature  Life ene |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/488` | 0.542853 | Speeds |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/24/SectionHeader/26` | 0.536873 | **RECHARGE WEAPON **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **touch; **Targets** 1 weapon with capacity  You touch a weapon with |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/4` | 0.534111 | **Jump**H Make an impressive leap. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/50` | 0.534111 | **Jump**H Make an impressive leap. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.524588 | **Summoned** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15` | 0.505947 | HEIGHTENED SPELLS |

### Query 69
- Text: What is the rule about NON-SPELLCASTERS WITH  FOCUS SPELLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `35`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/21', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20` | 0.872212 | NON-SPELLCASTERS WITH  FOCUS SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21` | 0.777302 | SPELLCASTERS WITH FOCUS  SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` | 0.635847 | FOCUS SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.568412 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5` | 0.566367 | SPELL SLOTS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` | 0.519105 | Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/13` | 0.515715 | SUSTAINING SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/27` | 0.515280 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/89` | 0.515280 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/29` | 0.515280 | **Focus Spells** |

### Query 70
- Text: Summarize 7 PLAYER CORE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/0']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/0', 'PZO22001 Starfinder Player Core 330-363::/page/15/SectionHeader/0', 'PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/0', 'PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/0` | 0.937057 | 7 PLAYER CORE |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/15/SectionHeader/0` | 0.937057 | 7 PLAYER CORE |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/0` | 0.937057 | 7 PLAYER CORE |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/0` | 0.937057 | 7 PLAYER CORE |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/34` | 0.617430 | PRIMAL 7TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.592220 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.585704 | CHAPTER 7: SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/5` | 0.576973 | OCCULT 7TH-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/57` | 0.569744 | ARCANE 7TH-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/11` | 0.551292 | DIVINE 7TH-RANK SPELLS |

### Query 71
- Text: What does **HEROISM **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `30`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/1', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/42', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/18', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/1` | 0.737135 | **HEROISM **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult **Duration** 10 minutes |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.679357 | **LIFE SEAL **[reaction] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.660523 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/18` | 0.636642 | **FELINE SENSES **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MORPH**  **Traditions** divine, primal  **Duration** 1 hour |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` | 0.635092 | **HYPNOTIZE **[two-actions] **SPELL 3**  **ILLUSION** **MANIPULATE** **SUBTLE** **VISUAL**  **Traditions** arcane, occult  **Range **120 feet; **Area** 10-foot burst  **Defense** Will;** Duration** su |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/4` | 0.597992 | **HONEYED WORDS **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes  You unlock the |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/44` | 0.592085 | **HEAL **[one-action]** TO **[three-actions] **SPELL 1**  **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **varies; **Targets** 1 willing living creature or 1 undead  c |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.588135 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/13` | 0.579199 | **HOLOGRAPHIC MEMORY **[two-actions] **SPELL 3**  **UNCOMMON** **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **touch;** Targets** 1 creature or corpse  **Defense** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/23` | 0.578791 | **SHARE PAIN **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **30 feet;** Targets** 1 creature  **Defense** Will  You telepathically shar |

### Query 72
- Text: Summarize Cosmic
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/498']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `14`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/498', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/499', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/494', 'PZO22001 Starfinder Player Core 330-363::/page/8/Text/23', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/44']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/498` | 0.814366 | Cosmic |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/22/ListItem/49` | 0.627749 | Cosmic trait. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/499` | 0.577123 | Divine |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/494` | 0.551662 | Akashic |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/44` | 0.548846 | **CONCENTRATE** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.548846 | **CONCENTRATE** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.545614 | **Summoned** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.529329 | insight about a topic. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/18/Text/58` | 0.518205 | **Call** **Cosmos**H Call down a column of cosmic matter to burn  and freeze. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/29` | 0.518205 | **Call** **Cosmos**H Call down a column of cosmic matter to burn  and freeze. |

### Query 73
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/20']
- Expected found: `True`
- Expected rank: `14`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/35/Text/64', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/22', 'PZO22001 Starfinder Player Core 294-329::/page/31/Text/56', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/61', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/82']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/64` | 0.866254 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/56` | 0.866254 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/61` | 0.866254 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/22` | 0.866254 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/82` | 0.866254 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/64` | 0.824254 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/82` | 0.824254 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/70` | 0.824254 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/76` | 0.824254 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/30` | 0.824254 | **CLASSES** |

### Query 74
- Text: Summarize Speeds
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/488']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `12`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/488', 'PZO22001 Starfinder Player Core 330-363::/page/20/ListItem/16', 'PZO22001 Starfinder Player Core 330-363::/page/20/Text/12', 'PZO22001 Starfinder Player Core 330-363::/page/11/ListItem/24', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/56']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/488` | 0.865034 | Speeds |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/20/ListItem/16` | 0.647143 | Speed 20 feet. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/20/Text/12` | 0.641050 | **Speed **fly 30 feet |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/14` | 0.622642 | **Tailwind**H Increase your speed for an hour. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/2` | 0.622642 | **Tailwind**H Increase your speed for an hour. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/11/ListItem/24` | 0.621979 | **Beetle** Speed 25 feet; **Melee **[one-action] mandibles, **Damage ** 2d10 bludgeoning. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/56` | 0.620690 | **FLEET STEP **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Duration** 1 minute  You gain a +30-foot status bonus to your Speed. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/2` | 0.601206 | **Fly**H Grant a target a fly Speed. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/70` | 0.586665 | **Fleet Step** Make your Speed much faster. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/42` | 0.586665 | **Fleet Step** Make your Speed much faster. |

### Query 75
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/61']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `21`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/33/Text/64', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/67', 'PZO22001 Starfinder Player Core 330-363::/page/17/Text/45', 'PZO22001 Starfinder Player Core 330-363::/page/19/Text/72', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/61']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.806592 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.806592 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.806592 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.806592 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.806592 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.764592 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.764592 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.764592 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.764592 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/62` | 0.764592 | **SPELLS** |

### Query 76
- Text: What is the rule about Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus spells only through special class features or feats,  rather than choosing them from a spell list. Furthermore, you  cast focus spells using a special pool of Focus Points—you can't  prepare a focus spell in a spell slot or use your spell slots to  cast focus spells; similarly, you can't spend your Focus Points  to cast spells that aren't focus spells. Even some classes that  don't normally grant spellcasting can grant focus spells. The  title of a focus spell's stat block says "Focus" instead of "Spell",  and the spell has the focus trait.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `47`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/13', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/21', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/5', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` | 1.015476 | Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.877564 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.808719 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/23` | 0.802230 | It's possible, especially through archetypes, to gain focus  spells from more than one source. If this happens, you  have just one focus pool, counting all your focus spells to  determine the points i |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` | 0.779543 | Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your p |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` | 0.738377 | Focus spells are automatically heightened to half your level  rounded up, just like cantrips are. You can't cast a focus spell  if its minimum rank is greater than half your level rounded  up, even if |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.725145 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.705728 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.705047 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/21` | 0.696572 | Some spells allow you to target a creature, an object, or  something more specific. The target must be within the  spell's range, and you must be able to see it (or otherwise  perceive it with a preci |

### Query 77
- Text: What does **CHRONO PUSH **[two-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/15/Text/42', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29', 'PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/40', 'PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/17` | 0.756895 | **CHRONO PUSH **[two-actions] **SPELL 5**  **ATTACK** **CONCENTRATE** **FORCE** **MANIPULATE**  **Traditions** occult  **Range **500 feet;** Targets** 1 creature **Defense** AC and basic Reflex  You p |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/42` | 0.642211 | **Chrono** **Push ** H Push a target away and damage creatures  nearby. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` | 0.624176 | **CONTROL MACHINE **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature or hazard with t |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/40` | 0.623145 | OCCULT 5TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/15` | 0.610511 | ARCANE 5TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.568264 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/39` | 0.567276 | **SUBCONSCIOUS SUGGESTION **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **LINGUISTIC** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet;** Targe |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/7` | 0.563598 | PRIMAL 5TH-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/5` | 0.560047 | **HYDRAULIC PUSH **[two-actions] **SPELL 1**  **ATTACK** **CONCENTRATE** **MANIPULATE** **WATER**  **Traditions** arcane, primal  **Range **60 feet;** Targets** 1 creature or unattended object **Defen |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.555006 | SPELL ATTACKS |

### Query 78
- Text: What does **EXECUTE **[two-actions] **SPELL 7** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/12']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `31`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/32', 'PZO22001 Starfinder Player Core 330-363::/page/22/SectionHeader/3', 'PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/39', 'PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.750462 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.654362 | CHAPTER 7: SPELLS |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/22/SectionHeader/3` | 0.650798 | **PLANAR SEAL **[two-actions] **SPELL 7**  **UNCOMMON** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult **Range **120 feet; **Area** 60-foot burst **Duration** until your next da |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/39` | 0.644948 | **SUBCONSCIOUS SUGGESTION **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **LINGUISTIC** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet;** Targe |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.638646 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/12` | 0.633295 | **EXECUTE **[two-actions] **SPELL 7**  **CONCENTRATE** **DEATH** **MANIPULATE** **VOID**  **Traditions** divine, primal  **Range **30 feet; **Targets** 1 creature  **Defense** basic Fortitude  You poi |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/5` | 0.616030 | OCCULT 7TH-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.604920 | SPELL ATTACKS |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/29` | 0.598338 | **STUPEFY **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** varies  You du |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/13/SectionHeader/48` | 0.587583 | **MASK OF TERROR **[two-actions] **SPELL 7**  **CONCENTRATE** **EMOTION** **FEAR** **ILLUSION** **MANIPULATE** **MENTAL** **VISUAL**  **Traditions** arcane, occult, primal  **Range **30 feet; **Target |

### Query 79
- Text: Summarize **Occult**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8', 'PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/3', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/78']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13` | 0.865280 | **Occult** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/495` | 0.707703 | Occult |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/24` | 0.687696 | **Traditions** occult |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.682540 | **SUBTLE SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.642814 | **Summoned** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/3` | 0.638109 | **Darkness and Light** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/78` | 0.635112 | **Rituals** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/34` | 0.614549 | **Traditions** divine, occult, primal |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` | 0.607813 | **CONCENTRATE** **MANIPULATE** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/44` | 0.602578 | **CONCENTRATE** |

### Query 80
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/58']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `23`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/23/Text/65', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/58', 'PZO22001 Starfinder Player Core 330-363::/page/27/Text/60', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/64', 'PZO22001 Starfinder Player Core 330-363::/page/25/Text/58']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/64` | 0.777771 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/58` | 0.777771 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/58` | 0.777771 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/60` | 0.777771 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/65` | 0.777771 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/58` | 0.735771 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/59` | 0.735771 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/61` | 0.735771 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/42` | 0.735771 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/61` | 0.735771 | **SKILLS** |

### Query 81
- Text: What does **BIND UNDEAD **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `21`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/36', 'PZO22001 Starfinder Player Core 294-329::/page/14/Text/63', 'PZO22001 Starfinder Player Core 294-329::/page/12/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/9/Text/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/13` | 0.705847 | **BIND UNDEAD **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Range **30 feet; **Targets** 1 mindless undead creature with a  level no greater tha |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/36` | 0.640424 | **EARTHBIND **[two-actions] **SPELL 3**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 flying creature  **Defense** Fortitude; **Duration** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/63` | 0.640419 | **Bind Undead** Take control of a mindless undead. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/43` | 0.640419 | **Bind Undead** Take control of a mindless undead. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/23` | 0.640419 | **Bind Undead** Take control of a mindless undead. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.629306 | **LIFE SEAL **[reaction] **SPELL 3** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.600398 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36` | 0.584953 | **BLINDNESS **[two-actions] **SPELL 3**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet;** Targets** 1 creature  **Defense** Fortit |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.579867 | SPELL ATTACKS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/62` | 0.577290 | OCCULT 3RD-RANK SPELLS |

### Query 82
- Text: What is the rule about **Focus Spells**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/64']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `21`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/27/Text/65', 'PZO22001 Starfinder Player Core 330-363::/page/23/Text/72', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/70', 'PZO22001 Starfinder Player Core 330-363::/page/15/Text/63', 'PZO22001 Starfinder Player Core 330-363::/page/11/Text/67']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/65` | 0.849140 | **Focus Spells** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/67` | 0.849140 | **Focus Spells** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/63` | 0.849140 | **Focus Spells** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/72` | 0.849140 | **Focus Spells** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/70` | 0.849140 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/63` | 0.807140 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/64` | 0.807140 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/75` | 0.807140 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/65` | 0.807140 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/67` | 0.807140 | **Focus Spells** |

### Query 83
- Text: Summarize FOCUS POINTS FROM MULTIPLE  SOURCES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `33`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22', 'PZO22001 Starfinder Player Core 294-329::/page/14/Text/74', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/39', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/27', 'PZO22001 Starfinder Player Core 294-329::/page/27/Text/71']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22` | 0.956768 | FOCUS POINTS FROM MULTIPLE  SOURCES |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.653259 | insight about a topic. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/39` | 0.635211 | **Focus Spells** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/71` | 0.635211 | **Focus Spells** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/27` | 0.635211 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/83` | 0.593211 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/77` | 0.593211 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/29` | 0.593211 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/36` | 0.593211 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/63` | 0.593211 | **Focus Spells** |

### Query 84
- Text: Summarize —
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/496']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/12/Text/44', 'PZO22001 Starfinder Player Core 330-363::/page/8/Text/23', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/500', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/496', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/492']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.622939 | insight about a topic. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.621699 | **CONCENTRATE** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/44` | 0.621699 | **CONCENTRATE** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/492` | 0.613244 | — |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/500` | 0.613244 | — |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/496` | 0.613244 | — |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.582530 | **Summoned** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.566608 | **SUBTLE SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/17` | 0.555216 | DISMISSING |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` | 0.552306 | **CONCENTRATE** **MANIPULATE** |

### Query 85
- Text: Summarize **ANCESTRIES & **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/29', 'PZO22001 Starfinder Player Core 330-363::/page/33/Text/59', 'PZO22001 Starfinder Player Core 330-363::/page/19/Text/67', 'PZO22001 Starfinder Player Core 330-363::/page/17/Text/40', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/62']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/29` | 0.908853 | **ANCESTRIES & ** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/59` | 0.859019 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/40` | 0.859019 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/67` | 0.859019 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/62` | 0.859019 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/40` | 0.817019 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/56` | 0.817019 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/58` | 0.817019 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/57` | 0.817019 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/58` | 0.817019 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 86
- Text: What does **HEAL **[one-action]** TO **[three-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/6/Text/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `29`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/6/Text/44', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21', 'PZO22001 Starfinder Player Core 330-363::/page/6/Text/26', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/42', 'PZO22001 Starfinder Player Core 330-363::/page/31/SectionHeader/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/44` | 0.693495 | **HEAL **[one-action]** TO **[three-actions] **SPELL 1**  **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **varies; **Targets** 1 willing living creature or 1 undead  c |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.682702 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/26` | 0.655570 | **HARM **[one-action]** TO **[three-actions] **SPELL 1**  **MANIPULATE** **VOID**  **Traditions** divine  **Range **varies; **Targets** 1 living creature or 1 willing undead  creature  You channel voi |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.650541 | **LIFE SEAL **[reaction] **SPELL 3** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/31/SectionHeader/22` | 0.640897 | **SOOTHE **[two-actions] **SPELL 1**  **CONCENTRATE** **EMOTION** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** occult  **Range **30 feet;** Targets** 1 willing creature  **Duration** 1 minute |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.594887 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/23` | 0.594833 | **SHARE PAIN **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **30 feet;** Targets** 1 creature  **Defense** Will  You telepathically shar |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.586407 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/1` | 0.586101 | **HEROISM **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult **Duration** 10 minutes |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39` | 0.585087 | **CLEANSE AFFLICTION **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  Gentle restorative |

### Query 87
- Text: What is the rule about Some types of magic, such as that of most magic items, don't belong to any single tradition. These have the magical  trait instead of a tradition trait.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `45`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/21', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/6/Text/6', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/4` | 0.926644 | Some types of magic, such as that of most magic items, don't belong to any single tradition. These have the magical  trait instead of a tradition trait. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/21` | 0.691635 | **Tradition** This entry lists the magical traditions the spell  belongs to. Some feats or other abilities might add a  spell to your spell list even if you don't follow the listed  traditions. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.674527 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/6/Text/6` | 0.613761 | Spells that affect multiple creatures in an area can have  both an Area entry and a Targets entry. A spell that has an  area but no targets listed usually affects all creatures in the  area indiscrimi |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/4` | 0.607109 | Non-magical light always shines in non-magical darkness  and always fails to shine in magical darkness. Magical light  always shines in non-magical darkness but shines in magical  darkness only if the |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.562710 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/28` | 0.557993 | If you have an innate spell, you can cast it even if it's not of  a spell rank you can normally cast. This is especially common  for monsters. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/6/Text/2` | 0.556132 | A spell with the subtle trait can be cast  without incantations and doesn't have obvious  manifestations. Most of these spells enhance your  subterfuge or stealth, such as *invisibility*. Some  abilit |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/12` | 0.552213 | Spells that slightly alter a creature's form have the morph trait.  Any Strikes specifically granted by a magical morph effect also  gain the magical trait. You can be affected by multiple morph  spel |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/20` | 0.551552 | **Tradition Resistance** If the dragon's magical tradition  matches that of your *dragon form* spell, you gain the  listed ability. **Arcane** resistance 5 against damage from  spells; **divine** resi |

### Query 88
- Text: What does **ENTHRALL **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/Text/20', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/42', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/32', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/20` | 0.704156 | **ENTHRALL **[two-actions] **SPELL 3**  **AUDITORY** **CONCENTRATE** **EMOTION** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet;** Targets** all creatures in range  **Defense** Will |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.697082 | **LIFE SEAL **[reaction] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.695840 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.665803 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` | 0.649489 | **HYPNOTIZE **[two-actions] **SPELL 3**  **ILLUSION** **MANIPULATE** **SUBTLE** **VISUAL**  **Traditions** arcane, occult  **Range **120 feet; **Area** 10-foot burst  **Defense** Will;** Duration** su |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.609956 | SPELL ATTACKS |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/1` | 0.594154 | **HEROISM **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult **Duration** 10 minutes |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/18` | 0.590294 | **FELINE SENSES **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MORPH**  **Traditions** divine, primal  **Duration** 1 hour |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.587549 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/66` | 0.583194 | **Spells** |

### Query 89
- Text: Summarize **Darkness and Light**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `29`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/3', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8', 'PZO22001 Starfinder Player Core 294-329::/page/19/ListItem/45', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/38']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/3` | 0.864769 | **Darkness and Light** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13` | 0.619843 | **Occult** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.613011 | **Summoned** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/19/ListItem/45` | 0.608831 | Low-light vision. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/38` | 0.607700 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/20/Text/5` | 0.579728 | **Perception **+0; darkvision |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/62` | 0.565700 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/30` | 0.565700 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/53` | 0.565700 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/59` | 0.565700 | **INTRODUCTION** |

### Query 90
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/66']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/33/Text/63', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/66', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/60', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/44', 'PZO22001 Starfinder Player Core 330-363::/page/17/Text/44']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/63` | 0.915652 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/66` | 0.915652 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/44` | 0.915652 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/60` | 0.915652 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/44` | 0.915652 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/61` | 0.873652 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/67` | 0.873652 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/71` | 0.873652 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/64` | 0.865652 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/58` | 0.865652 | **EQUIPMENT** |

### Query 91
- Text: What is the rule about **Spell Lists**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/68']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `21`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/27/Text/63', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/68', 'PZO22001 Starfinder Player Core 330-363::/page/15/Text/61', 'PZO22001 Starfinder Player Core 330-363::/page/25/Text/61', 'PZO22001 Starfinder Player Core 330-363::/page/19/Text/73']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/63` | 0.782608 | **Spell Lists** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/73` | 0.782608 | **Spell Lists** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/61` | 0.782608 | **Spell Lists** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/61` | 0.782608 | **Spell Lists** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/68` | 0.782608 | **Spell Lists** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/65` | 0.740608 | **Spell Lists** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/63` | 0.740608 | **Spell Lists** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/62` | 0.740608 | **Spell Lists** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/63` | 0.740608 | **Spell Lists** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/46` | 0.740608 | **Spell Lists** |

### Query 92
- Text: What is the rule about HEIGHTENED SPELLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `33`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/15` | 0.837925 | HEIGHTENED SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/13` | 0.661323 | SUSTAINING SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/4` | 0.618971 | Heightened Spontaneous Spells |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.610898 | CHAPTER 7: SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/7` | 0.606829 | PREPARED SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/3` | 0.561844 | IDENTIFYING SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.557979 | SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` | 0.539954 | FOCUS SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/16` | 0.533790 | READING SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.531040 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |

### Query 93
- Text: What does **GHOSTLY CARRIER **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `33`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/17', 'PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51', 'PZO22001 Starfinder Player Core 330-363::/page/32/SectionHeader/56', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/32', 'PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/17` | 0.739742 | **GHOSTLY CARRIER **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet **Duration** 1 minute  You create a Tiny, semi-corporeal figure with a |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.632651 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/32/SectionHeader/56` | 0.632357 | **SPIRITUAL ARMAMENT **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SANCTIFIED** **SPIRIT**  **Traditions** divine, occult  **Range **120 feet; **Targets** 1 creature  **Defense** AC; * |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.620066 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/29` | 0.604035 | **STUPEFY **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** varies  You du |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/25` | 0.582263 | OCCULT 2ND-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/23` | 0.572870 | **GHOST KILLER WEAPON **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 weapon that's either unattended or  wielded by you or a |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/17` | 0.569726 | PRIMAL 2ND-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/39` | 0.560377 | **SUBCONSCIOUS SUGGESTION **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **LINGUISTIC** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet;** Targe |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/56` | 0.560361 | **ILLUSORY CREATURE**[two-actions] **SPELL 2**  **AUDITORY** **CONCENTRATE** **ILLUSION** **MANIPULATE** **OLFACTORY** **VISUAL**  **Traditions** arcane, occult  **Range **500 feet  **Duration** susta |

### Query 94
- Text: What is the rule about Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule is for spells with the cantrip trait; once  you prepare a cantrip, you can cast it as many times as you  want until the next time you prepare spells. See page 296  for more information on cantrips.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `48`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/9', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/5', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/26', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 1.030242 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` | 0.855906 | The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any nu |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.805661 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.779915 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/10` | 0.749177 | You might gain an ability that allows you to swap  prepared spells or perform other aspects of preparing spells  at different times throughout the day, but only your daily  preparation counts for the |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/8` | 0.695187 | If you're a prepared spellcaster—such as a technomancer  (see *Starfinder Tech Core*)—you must spend time each day  preparing spells for that day. At the start of your daily  preparations, you select |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/6/Text/16` | 0.694716 | If a spell's duration says it lasts until your next daily  preparations, on the next day you can refrain from preparing  a new spell in that spell's slot. (If you are a spontaneous caster,  you can in |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/17` | 0.682153 | Each spell uses the following format. Entries appear only  when applicable, so not all spells will have every entry  described here. The spell's name line also lists the type  of spell if it's a cantr |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/22` | 0.676755 | **Cast** Spells that take longer than a single turn to cast include  this entry to list the time required, such as "1 minute." If  the spell has a cost, locus, requirements, or a trigger, that  inform |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21` | 0.667551 | **CONTINGENCY** **SPELL 7**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane  **Cast** 10 minutes **Duration** until your next daily preparations  You prepare a spell that will trigger later. Wh |

### Query 95
- Text: Summarize TOUCH RANGE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/16', 'PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14', 'PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28', 'PZO22001 Starfinder Player Core 294-329::/page/14/Text/74', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/16` | 0.935916 | TOUCH RANGE |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14` | 0.668447 | RANGES, AREAS, AND  TARGETS |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/7` | 0.666676 | **Range **touch;** Targets** 1 creature |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28` | 0.632695 | **ADHERE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Range **touch; **Targets** 1 held or unattended object or a 5-footsquare sur |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.603407 | insight about a topic. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/17` | 0.601230 | A spell with a touch range requires you to physically touch  the target. You use your unarmed reach to determine  whether you can touch the creature. You can usually touch  them automatically, though |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/24` | 0.553221 | **Heightened (4th)** The spell's range is touch and it targets 1  willing creature. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/47` | 0.550149 | **Range **60 feet; **Targets** the triggering creature |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/ListItem/45` | 0.545209 | Low-light vision. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22` | 0.543757 | FOCUS POINTS FROM MULTIPLE  SOURCES |

### Query 96
- Text: What does **ADHERE **[one-action] **CANTRIP 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `16`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28', 'PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19', 'PZO22001 Starfinder Player Core 294-329::/page/30/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/38']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28` | 0.757033 | **ADHERE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Range **touch; **Targets** 1 held or unattended object or a 5-footsquare sur |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41` | 0.624693 | **ANALYZE TARGET **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **30 feet; **Targets** 1 creature  **Dur |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19` | 0.612819 | **CAUSTIC BLAST **[two-actions] **CANTRIP 1**  **ACID** **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Area** 5-foot burst  **Defense** basic Reflex  Y |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/2` | 0.610812 | **DAZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE** **MENTAL** **NONLETHAL**  **Traditions** arcane, divine, occult **Range **60 feet; **Targets** 1 creature **Defense** W |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/38` | 0.598885 | **ELECTRIC ARC **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **ELECTRICITY** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Targets** 1 or 2 creatures  **Defense** ba |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/5` | 0.596386 | **STABILIZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet; **Targets** 1 dying creature  Life ene |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/5/SectionHeader/20` | 0.594996 | **GUIDANCE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE**  **Traditions** divine, occult, primal  **Range **30 feet; **Targets** 1 creature  **Duration** until the start of your next turn |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/3` | 0.581859 | **INJURY ECHO **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **60 feet; **Targets** 1 creature  **Defense** Will  You manifest an inj |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/11` | 0.573760 | **FORBIDDING WARD **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** divine, occult  **Range **30 feet; **Targets** 1 ally and 1 enemy  **Duration** sustained up |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/7` | 0.571659 | **Range **touch;** Targets** 1 creature |

### Query 97
- Text: What does **FROSTBITE **[two-actions] **CANTRIP 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `35`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/39', 'PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/5', 'PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/11', 'PZO22001 Starfinder Player Core 330-363::/page/26/Text/12', 'PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/39` | 0.713592 | **FROSTBITE **[two-actions] **CANTRIP 1**  **CANTRIP** **COLD** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets** 1 creature  **Defense** Fortitude  An orb |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/5` | 0.659339 | **STABILIZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet; **Targets** 1 dying creature  Life ene |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/11` | 0.600730 | **FORBIDDING WARD **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** divine, occult  **Range **30 feet; **Targets** 1 ally and 1 enemy  **Duration** sustained up |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/26/Text/12` | 0.598412 | **RICOCHET **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE** **METAL**  **Traditions** arcane, divine  **Range **30 feet; **Targets** 1 or 2 creatures  **Defense** basic Reflex |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/19` | 0.597740 | **STUMBLE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **100 feet; **Targets** 1 creature  **Defense** Reflex  A burst of micrograv |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19` | 0.556492 | **CAUSTIC BLAST **[two-actions] **CANTRIP 1**  **ACID** **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Area** 5-foot burst  **Defense** basic Reflex  Y |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/3` | 0.555125 | **INJURY ECHO **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **60 feet; **Targets** 1 creature  **Defense** Will  You manifest an inj |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/2` | 0.551320 | **DAZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE** **MENTAL** **NONLETHAL**  **Traditions** arcane, divine, occult **Range **60 feet; **Targets** 1 creature **Defense** W |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28` | 0.550466 | **ADHERE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Range **touch; **Targets** 1 held or unattended object or a 5-footsquare sur |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/52` | 0.542361 | **LIGHT **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **LIGHT** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **120 feet  **Duration** until your next daily prepa |

### Query 98
- Text: What is the rule about **Focus Spells**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/65']
- Expected found: `True`
- Expected rank: `9`
- Graph boost applied: `True`
- Graph boosted count: `21`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/27/Text/65', 'PZO22001 Starfinder Player Core 330-363::/page/23/Text/72', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/70', 'PZO22001 Starfinder Player Core 330-363::/page/15/Text/63', 'PZO22001 Starfinder Player Core 330-363::/page/11/Text/67']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/65` | 0.849140 | **Focus Spells** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/67` | 0.849140 | **Focus Spells** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/63` | 0.849140 | **Focus Spells** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/72` | 0.849140 | **Focus Spells** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/70` | 0.849140 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/63` | 0.807140 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/64` | 0.807140 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/75` | 0.807140 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/65` | 0.807140 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/67` | 0.807140 | **Focus Spells** |

### Query 99
- Text: What is the rule about Spellcasters cast spells from one of four different spell lists, each representing a different magical tradition: arcane,  divine, occult, and primal.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `31`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/18', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/2` | 0.889798 | Spellcasters cast spells from one of four different spell lists, each representing a different magical tradition: arcane,  divine, occult, and primal. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.657303 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.634029 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.606264 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/6` | 0.599957 | **Traditions** arcane, divine, occult, primal |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.591592 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/13/SectionHeader/43` | 0.579777 | **MANIFESTATION **[three-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  You spin secrets from the fundaments of magic, shaping them  into a power |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/34` | 0.555196 | **Traditions** divine, occult, primal |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/20` | 0.545246 | **Tradition Resistance** If the dragon's magical tradition  matches that of your *dragon form* spell, you gain the  listed ability. **Arcane** resistance 5 against damage from  spells; **divine** resi |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/2` | 0.544355 | These lists include the spells for each tradition, including cantrips. (Focus spells appear on pages 375–380.)  A superscript "H" indicates a spell has extra effects when heightened, and a spell whose |

### Query 100
- Text: What does **CONTROL MACHINE **[two-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29', 'PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/40', 'PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/15', 'PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/7', 'PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/55']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` | 0.740624 | **CONTROL MACHINE **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature or hazard with t |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/40` | 0.657344 | OCCULT 5TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/15` | 0.631703 | ARCANE 5TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/7` | 0.627844 | PRIMAL 5TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.615401 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/55` | 0.614027 | **DOMINATE **[two-actions] **SPELL 6**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult  **Range **30 feet;** Targets** 1 creature  **D |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/39` | 0.600641 | **SUBCONSCIOUS SUGGESTION **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **LINGUISTIC** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet;** Targe |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/54` | 0.568713 | DIVINE 5TH-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.567135 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.565873 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |

### Query 101
- Text: Summarize **GLOSSARY & **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/19/Text/79', 'PZO22001 Starfinder Player Core 330-363::/page/5/Text/34', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/74', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/69', 'PZO22001 Starfinder Player Core 330-363::/page/15/Text/67']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/34` | 0.879706 | **GLOSSARY & ** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/79` | 0.879706 | **GLOSSARY & ** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/75` | 0.829706 | **GLOSSARY & ** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/67` | 0.824245 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/74` | 0.824245 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/69` | 0.824245 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/77` | 0.782245 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/68` | 0.782245 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/72` | 0.782245 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/52` | 0.782245 | **GLOSSARY & ** **INDEX** |

### Query 102
- Text: What does **FALSE VITALITY **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `37`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/32', 'PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/32', 'PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/2/SectionHeader/1` | 0.734236 | **FALSE VITALITY **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Duration** 8 hours  You augment your flesh with the energies typically used to  manipulat |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.672056 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.640121 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/32` | 0.639322 | **INSTANT VIRUS **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane  **Range **touch; **Targets** 1 creature with the tech trait  **Defense** Fortitude  Your touch insta |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/29` | 0.639034 | **STUPEFY **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** varies  You du |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/39` | 0.604705 | **SUBCONSCIOUS SUGGESTION **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **LINGUISTIC** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet;** Targe |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/39` | 0.600191 | **False Vitality**H Gain temporary Hit Points. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/19` | 0.600191 | **False Vitality**H Gain temporary Hit Points. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47` | 0.595389 | **REVIVAL **[two-actions] **SPELL 10**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet;** Targets** dead creatures and living creatures of  y |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/32/SectionHeader/56` | 0.594896 | **SPIRITUAL ARMAMENT **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SANCTIFIED** **SPIRIT**  **Traditions** divine, occult  **Range **120 feet; **Targets** 1 creature  **Defense** AC; * |

### Query 103
- Text: Summarize **Rituals**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/71']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/71', 'PZO22001 Starfinder Player Core 330-363::/page/23/Text/73', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/66', 'PZO22001 Starfinder Player Core 330-363::/page/19/Text/76', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/48']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/71` | 0.889916 | **Rituals** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/73` | 0.889916 | **Rituals** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/66` | 0.889916 | **Rituals** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/48` | 0.889916 | **Rituals** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/76` | 0.889916 | **Rituals** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/68` | 0.847916 | **Rituals** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/66` | 0.847916 | **Rituals** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/64` | 0.847916 | **Rituals** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/68` | 0.847916 | **Rituals** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/65` | 0.847916 | **Rituals** |

### Query 104
- Text: Summarize —
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/500']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/12/Text/44', 'PZO22001 Starfinder Player Core 330-363::/page/8/Text/23', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/500', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/496', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/492']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.622939 | insight about a topic. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.621699 | **CONCENTRATE** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/44` | 0.621699 | **CONCENTRATE** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/492` | 0.613244 | — |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/500` | 0.613244 | — |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/496` | 0.613244 | — |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.582530 | **Summoned** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.566608 | **SUBTLE SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/17` | 0.555216 | DISMISSING |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` | 0.552306 | **CONCENTRATE** **MANIPULATE** |

### Query 105
- Text: What does **CALM **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/25/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/25/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54', 'PZO22001 Starfinder Player Core 294-329::/page/14/Text/28', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52', 'PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/25/Text/11` | 0.717641 | **CALM **[two-actions] **SPELL 2**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **120 feet;** Area** 10-foot burst  **Defense** Wil |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` | 0.657747 | **CLEAR MIND **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You drive menta |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/28` | 0.646984 | **Calm** Suppress strong emotions and hostility. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/52` | 0.644132 | **CHARM **[two-actions] **SPELL 1**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 creatur |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/25` | 0.630741 | OCCULT 2ND-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.622761 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/32/Text/2` | 0.600346 | **SOUND BODY **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You send a su |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/29` | 0.598415 | **STUPEFY **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** varies  You du |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/29/SectionHeader/14` | 0.595138 | **SILENCE **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** divine, occult  **Range **touch;** Targets** 1 willing creature  **Duration** 1 minute  The target makes n |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/46` | 0.590034 | **PEACEFUL REST **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **touch;** Targets** 1 corpse  **Duration** until your next daily pr |

### Query 106
- Text: What is the rule about **Failure** The target takes full damage, persistent mental  damage, and is compelled to howl as long as it takes  persistent mental damage.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/40']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `29`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/40', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/41', 'PZO22001 Starfinder Player Core 330-363::/page/18/Text/21', 'PZO22001 Starfinder Player Core 330-363::/page/0/Text/20', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/40` | 0.925303 | **Failure** The target takes full damage, persistent mental  damage, and is compelled to howl as long as it takes  persistent mental damage. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/41` | 0.687543 | **Critical Failure** As failure, but the target takes double the  initial and persistent damage. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/21` | 0.677778 | **Failure** The creature takes full damage and is deafened for  1 round. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/20` | 0.676566 | **ENTHRALL **[two-actions] **SPELL 3**  **AUDITORY** **CONCENTRATE** **EMOTION** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet;** Targets** all creatures in range  **Defense** Will |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/25` | 0.675531 | **LAUGHING FIT **[two-actions] **SPELL 2**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 living creature  **Defense** Will;** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/32/Text/16` | 0.656194 | **Failure** The creature takes full damage and persistent damage. **Critical Failure** The creature takes double damage and double  persistent damage. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/39` | 0.639154 | **Success** The target takes half damage and no persistent  mental damage. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/24/Text/10` | 0.627778 | **Failure** The creature takes full damage and is deafened for  1 round. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/9` | 0.624299 | **Failure** The creature takes full damage. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/37` | 0.617377 | You let out a powerful ululation full of psychic resonance that  compels others who hear it to join in. You deal 7d12 sonic  damage and 1d8 persistent mental damage to other creatures  who can hear wi |

### Query 107
- Text: Summarize Cone of mental
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/497']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `18`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/497', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/501', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/493', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/505', 'PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/497` | 0.746576 | Cone of mental (Will) |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/501` | 0.599193 | Cone of spirit (Will) |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/493` | 0.584056 | Cone of poison (Fortitude) |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/505` | 0.575689 | Cone of piercing (Reflex) |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` | 0.543412 | **CONCENTRATE** **MANIPULATE** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/14` | 0.522235 | **Mindlink** Mentally impart 10 minutes' worth of information  in an instant. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/53` | 0.520940 | **Mindlink** Mentally impart 10 minutes worth of information  in an instant. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.520376 | insight about a topic. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/57` | 0.512246 | **Synaptic Pulse** Slow creatures with a mental blast. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/24` | 0.501964 | **Magic Passage**H, U Open a temporary passage through a surface. **Mind Probe**U Uncover knowledge and memories in a |

### Query 108
- Text: What does **BATTLE SONATA **[two-actions] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23', 'PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/71', 'PZO22001 Starfinder Player Core 294-329::/page/28/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/1` | 0.704106 | **BATTLE SONATA **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **SONIC**  **Traditions** divine, occult  **Area** 15-foot cone  **Defense** Will  This spell was composed by pahtra battle |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.637205 | SPELL ATTACKS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/17` | 0.627697 | OCCULT 4TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/71` | 0.609794 | ARCANE 4TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.606791 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/32/Text/2` | 0.574566 | **SOUND BODY **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You send a su |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.573784 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/3` | 0.550998 | **NIGHTMARE** **SPELL 4**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Cast** 10 minutes  **Range **planetary;** Targets** 1 creature you know by name  **D |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/1` | 0.550688 | **DISPELLING GLOBE **[two-actions] **SPELL 4**  **UNCOMMON** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Area** 10-foot burst centered on one corner of your space **Durati |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/71` | 0.547679 | PRIMAL 4TH-RANK SPELLS |

### Query 109
- Text: What is the rule about Many spontaneous spellcasting classes provide abilities  like the signature spells class feature, which allows you to  cast a limited number of spells as heightened versions even if  you know the spell at only a single rank.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `49`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/6', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/5', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/6', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/1', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/6` | 0.949527 | Many spontaneous spellcasting classes provide abilities  like the signature spells class feature, which allows you to  cast a limited number of spells as heightened versions even if  you know the spel |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 0.730751 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.713938 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.713725 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.712453 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` | 0.653762 | As a spontaneous caster, you can also choose to cast  a lower-rank spell using a higher-rank spell slot without  heightening it or knowing it at a higher rank. This casts the  spell at the rank you kn |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/28` | 0.652883 | If you have an innate spell, you can cast it even if it's not of  a spell rank you can normally cast. This is especially common  for monsters. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.640761 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.639845 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.637949 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |

### Query 110
- Text: Summarize are determined by their connection, and a witchwarper's are  determined by their paradox.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `43`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/24', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/15', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/19` | 0.979260 | are determined by their connection, and a witchwarper's are  determined by their paradox. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/24` | 0.662300 | spells and precog warp spells, your mystic spells would  remain divine and the witchwarper spells occult. Similarly,  you need to use the attribute modifier determined by the  source of the focus spel |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.652315 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.652109 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/1` | 0.626365 | Whether it comes in the form of eldritch artifacts, otherworldly beings, or witchwarpers altering  reality with strange spells, magic brings fantasy and wonder to Starfinder. This chapter explains how |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/20` | 0.575149 | You spend 10 minutes performing deeds to restore your  magical connection. This restores 1 Focus Point to your focus  pool. The deeds you need to perform are specified in the class  or ability that gi |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.575032 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/4` | 0.569447 | Spellcasting creates obvious sensory manifestations, such  as bright lights, crackling sounds, and sharp smells from the  gathering magic. Nearly all spells manifest a spell signature—a  colorful, glo |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.565981 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/29/ListItem/4` | 0.561895 | **Weal** **and** **Woe** The results will be a mix of good and  bad. |

### Query 111
- Text: What is the rule about If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single rank so that you have more options when casting it.  For example, if you added *skyfire wings* to your repertoire as  a 3rd-rank spell and again as a 7th-rank spell, you could cast  it as a 3rd-rank or a 7th-rank spell; however, you couldn't cast  it as a 5th-rank spell.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `46`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/5', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/16', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/1', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/5` | 1.009828 | If you're a spontaneous spellcaster, you must know a spell at  the specific rank that you want to cast it in order to heighten  it. You can add a spell to your spell repertoire at more than  a single |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/7` | 0.796132 | As a spontaneous caster, you can also choose to cast  a lower-rank spell using a higher-rank spell slot without  heightening it or knowing it at a higher rank. This casts the  spell at the rank you kn |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/16` | 0.785139 | Both prepared and spontaneous spellcasters can cast a spell  at a higher spell rank than that listed for the spell. This is  called heightening the spell. A prepared spellcaster can  heighten a spell |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.782317 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/4` | 0.767242 | Sometimes you need to identify a spell, especially if its  effects aren't obvious right away. If you notice a spell  being cast, and you have that spell in your repertoire  or prepared it that day (ev |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/1` | 0.711798 | You can't use your spell slots to cast your innate spells, but  you might have an innate spell and also be able to prepare  or cast the same spell through your class. You also can't  heighten innate s |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/6` | 0.695117 | Many spontaneous spellcasting classes provide abilities  like the signature spells class feature, which allows you to  cast a limited number of spells as heightened versions even if  you know the spel |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/14` | 0.686460 | If you're a spontaneous spellcaster—such as a mystic—you  choose which spell from your spell repertoire that you're  using a spell slot for at the moment you decide to cast it. This  provides you with |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.685873 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.684756 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |

### Query 112
- Text: What is the rule about **Heightened (+1)** The void damage increases by 2d4, and the  persistent bleed damage increases by 1.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `29`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/11', 'PZO22001 Starfinder Player Core 330-363::/page/23/Text/54', 'PZO22001 Starfinder Player Core 330-363::/page/18/Text/23', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/11` | 0.960064 | **Heightened (+1)** The void damage increases by 2d4, and the  persistent bleed damage increases by 1. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/54` | 0.853548 | **Heightened (+1)** The damage increases by 2d4. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/23` | 0.815981 | **Heightened (+1)** The damage increases by 1d10. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/2` | 0.810938 | **Heightened (+1)** The damage increases by 1d6. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/32/Text/17` | 0.799475 | **Heightened (+1)** The damage increases by 1d6 and persistent  damage increases by 1d6. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/34/Text/17` | 0.781695 | **Heightened (+1)** The cold damage increases by 1d10 and the  void damage against the living increases by 1d4. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/34/Text/37` | 0.766207 | **Heightened (+1)** The damage increases by 1d12. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/24/Text/12` | 0.765981 | **Heightened (+1)** The damage increases by 1d10. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/32/Text/43` | 0.765981 | **Heightened (+1)** The damage increases by 1d10. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/27` | 0.757139 | **Heightened (+2)** The initial damage increases by 2d8, and the  persistent acid damage increases by 1d6. |

### Query 113
- Text: What does **CONFUSION **[two-actions] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `16`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/28/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54', 'PZO22001 Starfinder Player Core 294-329::/page/30/Text/49', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.757882 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/17` | 0.630514 | OCCULT 4TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` | 0.629458 | **CLEAR MIND **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You drive menta |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.619857 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/49` | 0.619593 | **DETECT POISON **[two-actions] **SPELL 1**  **UNCOMMON** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** divine, primal  **Range **30 feet;** Targets** 1 object or creature  You detect w |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/12` | 0.619461 | FOCUS SPELLS |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.611133 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.605673 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/18/SectionHeader/45` | 0.595692 | **OUTCAST'S CURSE **[two-actions] **SPELL 4**  **CONCENTRATE** **CURSE** **MANIPULATE** **MENTAL** **MISFORTUNE**  **Traditions** arcane, divine, occult **Range **touch;** Targets** 1 creature  **Defe |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/12` | 0.591485 | **HALLUCINATION **[two-actions] **SPELL 5**  **ILLUSION** **INCAPACITATION** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** 1 creature  **Duration* |

### Query 114
- Text: What does **CLAIRAUDIENCE** **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/24', 'PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/62', 'PZO22001 Starfinder Player Core 294-329::/page/14/Text/65', 'PZO22001 Starfinder Player Core 294-329::/page/9/Text/45', 'PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/24` | 0.688953 | **CLAIRAUDIENCE** **SPELL 3**  **CONCENTRATE** **MANIPULATE** **SCRYING**  **Traditions** arcane, occult  **Cast** 1 minute **Range **500 feet  **Duration** 10 minutes  You create an invisible floatin |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/62` | 0.659142 | OCCULT 3RD-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/45` | 0.630175 | **Clairaudience** Hear through an invisible magical sensor. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/65` | 0.630175 | **Clairaudience** Hear through an invisible magical sensor. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.621823 | **LIFE SEAL **[reaction] **SPELL 3** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/42` | 0.621414 | ARCANE 3RD-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.600201 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/31` | 0.574821 | **CLAIRVOYANCE** **SPELL 4**  **CONCENTRATE** **MANIPULATE** **SCRYING**  **Traditions** arcane, occult  **Cast** 1 minute  **Range **500 feet  **Duration** 10 minutes  You create an invisible floatin |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/22` | 0.572789 | DIVINE 3RD-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/49` | 0.570582 | PRIMAL 3RD-RANK SPELLS |

### Query 115
- Text: What does **FALSE VISION** **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/52']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/52', 'PZO22001 Starfinder Player Core 330-363::/page/6/Text/12', 'PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/50', 'PZO22001 Starfinder Player Core 330-363::/page/27/Text/3', 'PZO22001 Starfinder Player Core 330-363::/page/15/SectionHeader/27']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/52` | 0.727128 | **FALSE VISION** **SPELL 5**  **UNCOMMON** **CONCENTRATE** **ILLUSION** **MANIPULATE**  **Traditions** arcane, occult  **Cast** 10 minutes  **Range **touch;** Area** 100-foot burst  **Duration** until |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/12` | 0.641161 | **HALLUCINATION **[two-actions] **SPELL 5**  **ILLUSION** **INCAPACITATION** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** 1 creature  **Duration* |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/50` | 0.640826 | **SUBJECTIVE REALITY **[one-action] **SPELL 5**  **CONCENTRATE** **MANIPULATE**  **Traditions** occult  **Range **500 feet;** Targets** 1 creature or object  **Duration** sustained up to 1 minute  You |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/3` | 0.616796 | **SCOUTING EYE** **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SCRYING**  **Traditions** arcane, divine, occult  **Cast** 1 minute **Range **see text **Duration** sustained  You create an invisible, f |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/15/SectionHeader/27` | 0.607461 | **MISLEAD **[two-actions] **SPELL 6**  **CONCENTRATE** **ILLUSION** **MANIPULATE**  **Traditions** arcane, occult  **Duration** sustained up to 1 minute  You turn yourself invisible and create an illu |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/40` | 0.597452 | OCCULT 5TH-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/45` | 0.578551 | **False Vision**U Trick a scrying spell. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/19` | 0.578551 | **False Vision**U Trick a scrying spell. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/54` | 0.570051 | DIVINE 5TH-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/15` | 0.567657 | ARCANE 5TH-RANK SPELLS |

### Query 116
- Text: What does **CREATE WATER **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23', 'PZO22001 Starfinder Player Core 294-329::/page/11/Text/52']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/9` | 0.782075 | **CREATE WATER **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **WATER**  **Traditions** arcane, divine, primal  **Range **0 feet |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47` | 0.654891 | **CLEANSE CUISINE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** divine, primal  **Range **10 feet;** Area** 1 cubic foot  You transform all food and beverages in the area |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.638668 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.632712 | SPELL ATTACKS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/52` | 0.623766 | **Create Water** Conjure 2 gallons of water. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/12` | 0.596543 | **GREASE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet;** Area** 4 contiguous 5-foot squares or** Targets** 1  object of 1 Bulk or less |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.589812 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/5` | 0.588429 | **HYDRAULIC PUSH **[two-actions] **SPELL 1**  **ATTACK** **CONCENTRATE** **MANIPULATE** **WATER**  **Traditions** arcane, primal  **Range **60 feet;** Targets** 1 creature or unattended object **Defen |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/65` | 0.581766 | **Create Water** Conjure 2 gallons of water. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/34` | 0.581766 | **Create Water** Conjure 2 gallons of water. |

### Query 117
- Text: What does **ANIMAL FORM **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/21/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `21`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/21/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/36', 'PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/17', 'PZO22001 Starfinder Player Core 294-329::/page/25/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/21/SectionHeader/4` | 0.698918 | **ANIMAL FORM **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** primal  **Duration** 1 minute  You call upon primal energy to transform yourself into a  Medium |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/36` | 0.657123 | **AERIAL FORM **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Duration** 1 minute  You harness your mastery of the sky to reshape your body |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/9/SectionHeader/4` | 0.630871 | ARCANE 2ND-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/17` | 0.628646 | PRIMAL 2ND-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/25/Text/11` | 0.628352 | **CALM **[two-actions] **SPELL 2**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **120 feet;** Area** 10-foot burst  **Defense** Wil |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/60` | 0.625740 | **PEST FORM **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Duration** 10 minutes |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.616775 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/10` | 0.605250 | **INSECT FORM **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Duration** 1 minute  You envision a simple bug and transform into a Medium  an |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.601267 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47` | 0.587478 | **REVIVAL **[two-actions] **SPELL 10**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet;** Targets** dead creatures and living creatures of  y |

### Query 118
- Text: What is the rule about **Critical Failure** The creature takes double damage, is slowed  3 until the end of its next turn, and slowed 2 for 1 minute.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/5', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/4', 'PZO22001 Starfinder Player Core 330-363::/page/18/Text/22', 'PZO22001 Starfinder Player Core 330-363::/page/28/Text/33', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/5` | 0.902843 | **Critical Failure** The creature takes double damage, is slowed  3 until the end of its next turn, and slowed 2 for 1 minute. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/4` | 0.828764 | **Failure** The creature takes full damage, is slowed 3 until the  end of its next turn, and slowed 1 for 1 minute. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/22` | 0.805281 | **Critical Failure** The creature takes double damage, is  deafened for 1 minute, and is stunned 1. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/33` | 0.789214 | **Critical Failure** The creature takes full damage and is clumsy  2 for 1 minute. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/3` | 0.773533 | **Success** The creature takes half damage and is slowed 1 until  the end of its next turn. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/32/Text/42` | 0.754034 | **Critical Failure** The creature takes full damage and is sickened  2; while it's sickened, it's also slowed 1. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/13` | 0.739436 | **Failure** The creature takes full damage and is slowed 1 until the  start of your next turn. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/20` | 0.739436 | **Failure** The creature takes full damage and is slowed 1 until  the start of your next turn. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/24/Text/11` | 0.736223 | **Critical** **Failure** The creature takes double damage, is  deafened for 1 minute, and becomes stunned 1. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/53` | 0.720994 | **Critical Failure** The creature takes double damage and is  pushed 10 feet away from you. |

### Query 119
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/74']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/33/Text/71', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/68', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/69', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/74', 'PZO22001 Starfinder Player Core 330-363::/page/25/Text/67']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/71` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/67` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/68` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/69` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/74` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/67` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/77` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/52` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/51` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/69` | 0.887439 | **GLOSSARY & ** **INDEX** |

### Query 120
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/25']
- Expected found: `True`
- Expected rank: `10`
- Graph boost applied: `True`
- Graph boosted count: `30`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/31/Text/59', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/60', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/35', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/64', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/58']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/59` | 0.915652 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/64` | 0.915652 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/60` | 0.915652 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/35` | 0.915652 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/58` | 0.915652 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/67` | 0.873652 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/67` | 0.873652 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/85` | 0.873652 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/73` | 0.873652 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/25` | 0.873652 | **EQUIPMENT** |

### Query 121
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/60']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/33/Text/63', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/66', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/60', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/44', 'PZO22001 Starfinder Player Core 330-363::/page/17/Text/44']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/63` | 0.915652 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/66` | 0.915652 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/44` | 0.915652 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/60` | 0.915652 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/44` | 0.915652 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/61` | 0.873652 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/67` | 0.873652 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/71` | 0.873652 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/64` | 0.865652 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/58` | 0.865652 | **EQUIPMENT** |

### Query 122
- Text: What does **FALLING STARS **[two-actions] **SPELL 9** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/44', 'PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/32', 'PZO22001 Starfinder Player Core 330-363::/page/10/SectionHeader/25', 'PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/51', 'PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/44` | 0.738832 | **FALLING STARS **[two-actions] **SPELL 9**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Area** four 40-foot bursts  **Defense** basic Reflex  You reach into t |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/32` | 0.636057 | **PHANTASMAGORIA **[two-actions] **SPELL 9**  **CONCENTRATE** **DEATH** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **120 feet; **Targets** any number of creatures |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/24` | 0.627733 | OCCULT 9TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/10/SectionHeader/25` | 0.620819 | **IMPLOSION **[two-actions] **SPELL 9**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet;** Targets** 1 corporeal creature  **Defense** basic Fortitude; **Duration** s |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/51` | 0.611331 | **PHANTASMAL FLEET **[two-actions] **SPELL 8**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **500 feet; **Area** 60-foot burst  **Defense** Will  A m |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/26` | 0.604719 | **FORESIGHT **[two-actions] **SPELL 9**  **CONCENTRATE** **MANIPULATE** **MENTAL** **PREDICTION**  **Traditions** arcane, divine, occult **Range **touch;** Targets** 1 creature  **Duration** 1 hour  Y |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/56` | 0.603514 | PRIMAL 9TH-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/11` | 0.593785 | ARCANE 9TH-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.590695 | SPELL ATTACKS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/28` | 0.589366 | DIVINE 9TH-RANK SPELLS |

### Query 123
- Text: What does **CAUSTIC BLAST **[two-actions] **CANTRIP 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `18`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19', 'PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/24', 'PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/38', 'PZO22001 Starfinder Player Core 294-329::/page/30/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19` | 0.764380 | **CAUSTIC BLAST **[two-actions] **CANTRIP 1**  **ACID** **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Area** 5-foot burst  **Defense** basic Reflex  Y |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/24` | 0.648890 | **DIVINE LANCE **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE** **SANCTIFIED** **SPIRIT**  **Traditions** divine  **Range **60 feet; **Targets** 1 creature  **Defen |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/38` | 0.632188 | **ELECTRIC ARC **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **ELECTRICITY** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Targets** 1 or 2 creatures  **Defense** ba |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/2` | 0.627864 | **DAZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE** **MENTAL** **NONLETHAL**  **Traditions** arcane, divine, occult **Range **60 feet; **Targets** 1 creature **Defense** W |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41` | 0.626325 | **ANALYZE TARGET **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **30 feet; **Targets** 1 creature  **Dur |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/5` | 0.611944 | **STABILIZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet; **Targets** 1 dying creature  Life ene |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/3` | 0.591694 | **INJURY ECHO **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **60 feet; **Targets** 1 creature  **Defense** Will  You manifest an inj |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/13` | 0.584496 | **NOISE BLAST **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SONIC**  **Traditions** arcane, divine, occult **Range **30 feet;** Area** 10-foot burst  **Defense** Fortitude  A cacophono |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/18` | 0.580083 | **ELDRITCH LANCE **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **30 feet; **Targets** 1 creature  **Defense** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/19` | 0.575087 | **STUMBLE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **100 feet; **Targets** 1 creature  **Defense** Reflex  A burst of micrograv |

### Query 124
- Text: What does **CALL COSMOS **[two-actions] **SPELL 9** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `34`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/24', 'PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/28', 'PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/56', 'PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/4` | 0.717823 | **CALL COSMOS **[two-actions] **SPELL 9**  **COLD** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** divine, primal  **Range **500 feet;** Area** 20-foot radius, 40-foot tall cylinder **Defense |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/24` | 0.672257 | OCCULT 9TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/28` | 0.633766 | DIVINE 9TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/56` | 0.631609 | PRIMAL 9TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/SectionHeader/11` | 0.630810 | ARCANE 9TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/29` | 0.577811 | **Call** **Cosmos**H Call down a column of cosmic matter to burn  and freeze. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.574735 | CHAPTER 7: SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/18/Text/58` | 0.565811 | **Call** **Cosmos**H Call down a column of cosmic matter to burn  and freeze. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.563811 | SPELL ATTACKS |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.556242 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |

### Query 125
- Text: What is the rule about **Spell Lists**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/25']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `29`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/17/Text/87', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/25', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/60', 'PZO22001 Starfinder Player Core 294-329::/page/27/Text/69', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/44']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/87` | 0.782608 | **Spell Lists** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/25` | 0.782608 | **Spell Lists** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/60` | 0.782608 | **Spell Lists** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/44` | 0.782608 | **Spell Lists** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/69` | 0.782608 | **Spell Lists** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/81` | 0.740608 | **Spell Lists** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/75` | 0.740608 | **Spell Lists** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/62` | 0.740608 | **Spell Lists** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/84` | 0.740608 | **Spell Lists** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/61` | 0.740608 | **Spell Lists** |

### Query 126
- Text: What is the rule about The illusion can cause damage by making the target believe  the illusion's attacks are real, but it cannot otherwise directly  affect the physical world. If the illusory creature hits with a  Strike, the target takes 3d4 mental damage. The illusion's  Strikes are nonlethal. If the damage doesn't correspond to  the image of the monster—for example, if an illusory Large  dragon deals only 5 damage—the GM might allow the target  to attempt an immediate Perception check to disbelieve the  spell. Any relevant resistances and weaknesses apply if the  target thinks they do, as judged by the GM. For example, if  the illusion wields a doshko and attacks a creature resistant to  piercing damage, the creature would take less mental damage.  However, illusory damage does not deactivate regeneration or  trigger other effects that require a certain damage type. The  GM should track illusory damage dealt by the illusion.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `30`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/4', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/5', 'PZO22001 Starfinder Player Core 330-363::/page/10/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/3', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/4` | 1.015823 | The illusion can cause damage by making the target believe  the illusion's attacks are real, but it cannot otherwise directly  affect the physical world. If the illusory creature hits with a  Strike, |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/5` | 0.762420 | Any creature that touches the image or uses the Seek  action to examine it can attempt to disbelieve your illusion.  When a creature disbelieves the illusion, it recovers from half  the damage it had |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/17` | 0.723139 | Magic with the illusion trait creates false sensory stimuli.  Sometimes illusions allow creatures a chance to disbelieve  the spell, which lets the creature ignore the spell if it succeeds  at doing s |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/10/Text/2` | 0.704026 | Any creature that touches any part of the image or uses  the Seek action to examine it can attempt to disbelieve  your illusion. If they interact with a portion of the illusion,  they disbelieve only |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/3` | 0.684242 | In combat, the illusion can use 2 actions per turn, which  it uses when you Sustain the spell. It uses your spell attack  modifier for attack rolls and your spell DC for its AC. Its  saving throw modi |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/1` | 0.683852 | Illusions bend light around the target, rendering it  invisible. This makes it undetected to all creatures, though  the creatures can attempt to find the target, making it  hidden to them instead (pag |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/18` | 0.648790 | If a creature engages with an illusion in a way that would  prove it's not what it seems, the creature might know that an  illusion is present, but it still can't ignore the illusion without  successf |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/21` | 0.643709 | Some spells allow you to target a creature, an object, or  something more specific. The target must be within the  spell's range, and you must be able to see it (or otherwise  perceive it with a preci |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/7` | 0.634943 | **ILLUSORY DISGUISE **[two-actions] **SPELL 1**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **VISUAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 willing creature  **Duration** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/21/SectionHeader/8` | 0.634498 | **PHANTOM PAIN **[two-actions] **SPELL 1**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL** **NONLETHAL**  **Traditions** occult  **Range **30 feet; **Targets** 1 creature **Defense** Will; **D |

### Query 127
- Text: Summarize **CONDITIONS **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `30`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/30', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/74', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/67', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/39', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/80']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/30` | 0.880718 | **CONDITIONS ** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/67` | 0.880718 | **CONDITIONS ** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/74` | 0.880718 | **CONDITIONS ** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/50` | 0.830718 | **CONDITIONS ** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/75` | 0.830718 | **CONDITIONS ** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/68` | 0.830718 | **CONDITIONS ** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/80` | 0.793212 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/39` | 0.793212 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/65` | 0.779096 | **GAME** **CONDITIONS ** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/49` | 0.751212 | **CONDITIONS ** **APPENDIX** |

### Query 128
- Text: What is the rule about A cantrip is a special type of spell that's weaker than other  spells but can be used with greater freedom and flexibility.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `36`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/9', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/9', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/8/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/9` | 0.951696 | A cantrip is a special type of spell that's weaker than other  spells but can be used with greater freedom and flexibility. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 0.696548 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/10` | 0.679512 | The title of a cantrip's stat block says "Cantrip" instead of  "Spell", and the spell has the cantrip trait. Casting a cantrip  doesn't use up your spell slots; you can cast a cantrip at will,  any nu |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/2` | 0.647731 | These lists include the spells for each tradition, including cantrips. (Focus spells appear on pages 375–380.)  A superscript "H" indicates a spell has extra effects when heightened, and a spell whose |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/11` | 0.643791 | A cantrip is always automatically heightened to half your  level, rounded up. For a typical spellcaster, this means its  rank is equal to the highest rank of spell slot you have. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/26` | 0.598506 | Certain spells are natural to your character, typically coming  from your ancestry or a magic item. They're called innate  spells. Innate spells don't let you qualify for abilities that  require you t |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/17` | 0.591812 | Each spell uses the following format. Entries appear only  when applicable, so not all spells will have every entry  described here. The spell's name line also lists the type  of spell if it's a cantr |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` | 0.578366 | Focus spells are automatically heightened to half your level  rounded up, just like cantrips are. You can't cast a focus spell  if its minimum rank is greater than half your level rounded  up, even if |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/2` | 0.576865 | In rare cases, a spell might have you make some other  type of attack, such as a weapon Strike. Such attacks use the  normal rules and attack bonus for that type of attack. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.572526 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |

### Query 129
- Text: Summarize Cone of poison
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/493']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `17`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/493', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/505', 'PZO22001 Starfinder Player Core 330-363::/page/22/ListItem/23', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/497', 'PZO22001 Starfinder Player Core 330-363::/page/11/ListItem/28']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/493` | 0.741636 | Cone of poison (Fortitude) |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/505` | 0.602215 | Cone of piercing (Reflex) |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/22/ListItem/23` | 0.600256 | Resistance 10 to poison. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/497` | 0.585718 | Cone of mental (Will) |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/11/ListItem/28` | 0.556819 | piercing plus 1d4 persistent poison; **Melee **[one-action] pincer  (agile), **Damage **1d6 bludgeoning. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/30` | 0.542474 | **Toxic Cloud**H A bank of poison fog rolls away from you. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/18/Text/20` | 0.542474 | **Toxic Cloud**H A bank of poison fog rolls away from you. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/60` | 0.537307 | **Shadow Blast**H Shape a damaging cone of shadow substance  to deal damage of a type you choose. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/51` | 0.537307 | **Shadow Blast**H Shape a damaging cone of shadow substance  to deal damage of a type you choose. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/9` | 0.532602 | **Pummeling Rubble**H Hurl a cone of rocks to batter creatures. |

### Query 130
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/58']
- Expected found: `True`
- Expected rank: `10`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/23/Text/63', 'PZO22001 Starfinder Player Core 330-363::/page/17/Text/40', 'PZO22001 Starfinder Player Core 330-363::/page/11/Text/59', 'PZO22001 Starfinder Player Core 330-363::/page/15/Text/56', 'PZO22001 Starfinder Player Core 330-363::/page/13/Text/57']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/57` | 0.830013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/40` | 0.830013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/63` | 0.830013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/56` | 0.830013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/59` | 0.830013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/56` | 0.788013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/58` | 0.788013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/62` | 0.788013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/40` | 0.788013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/58` | 0.788013 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 131
- Text: What does **ANALYZE TARGET **[two-actions] **CANTRIP 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41', 'PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28', 'PZO22001 Starfinder Player Core 294-329::/page/30/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/41` | 0.738168 | **ANALYZE TARGET **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **30 feet; **Targets** 1 creature  **Dur |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/5` | 0.653994 | **STABILIZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet; **Targets** 1 dying creature  Life ene |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/28` | 0.646691 | **ADHERE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Range **touch; **Targets** 1 held or unattended object or a 5-footsquare sur |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/2` | 0.646444 | **DAZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE** **MENTAL** **NONLETHAL**  **Traditions** arcane, divine, occult **Range **60 feet; **Targets** 1 creature **Defense** W |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20` | 0.644494 | TARGETS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/19` | 0.640437 | **CAUSTIC BLAST **[two-actions] **CANTRIP 1**  **ACID** **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Area** 5-foot burst  **Defense** basic Reflex  Y |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/11` | 0.600099 | **FORBIDDING WARD **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** divine, occult  **Range **30 feet; **Targets** 1 ally and 1 enemy  **Duration** sustained up |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/24` | 0.597308 | **DIVINE LANCE **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE** **SANCTIFIED** **SPIRIT**  **Traditions** divine  **Range **60 feet; **Targets** 1 creature  **Defen |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/3` | 0.596354 | **INJURY ECHO **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **60 feet; **Targets** 1 creature  **Defense** Will  You manifest an inj |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/5/SectionHeader/20` | 0.592077 | **GUIDANCE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE**  **Traditions** divine, occult, primal  **Range **30 feet; **Targets** 1 creature  **Duration** until the start of your next turn |

### Query 132
- Text: Lookup values for DragonTraditionSpeedsDragon BreathAbysiumArcane—Cone of poison
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/Table/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/Table/3', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/493', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/489', 'PZO22001 Starfinder Player Core 330-363::/page/11/ListItem/25', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/Table/3` | 0.848179 | DragonTraditionSpeedsDragon BreathAbysiumArcane—Cone of poison (Fortitude)AkashicOccult—Cone of mental (Will)CosmicDivine—Cone of spirit (Will)HostPrimalClimbCone of piercing (Reflex) |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/493` | 0.660268 | Cone of poison (Fortitude) |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/489` | 0.616534 | Dragon Breath |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/11/ListItem/25` | 0.598117 | **Centipede** Speed 25 feet, climb 25 feet; darkvision;  **Melee **[one-action] mandibles, **Damage **1d8 piercing plus 1d4  persistent poison. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/19` | 0.597137 | **Dragon Breath**[two-actions] You exhale deadly magical energy  in an area, dealing 10d6 damage to each creature in  the area with a basic save against your spell DC. The  shape, damage type, and sav |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/14` | 0.592481 | Resistance 10 against the damage type of your Dragon  Breath (see below). |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/6` | 0.587704 | **Traditions** arcane, divine, occult, primal |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/20` | 0.584664 | **Tradition Resistance** If the dragon's magical tradition  matches that of your *dragon form* spell, you gain the  listed ability. **Arcane** resistance 5 against damage from  spells; **divine** resi |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/21/ListItem/25` | 0.569426 | **Snake** Speed 20 feet, climb 20 feet, swim 20 feet; **Melee ** [one-action] fangs, **Damage **2d4 piercing plus 1d6 poison. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/13` | 0.566383 | Speed 40 feet, fly 100 feet. You gain any of the following  Speeds the chosen dragon has, but with the listed  amount: burrow 20 feet, climb 40 feet, swim 60 feet. |

### Query 133
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/72']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/27/Text/67', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/49', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/67', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/72', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/66']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/67` | 0.938833 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/49` | 0.938833 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/72` | 0.938833 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/67` | 0.938833 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/66` | 0.938833 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/74` | 0.896833 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/67` | 0.896833 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/65` | 0.896833 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/77` | 0.896833 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/49` | 0.896833 | **PLAYING THE ** **GAME** |

### Query 134
- Text: What does **GRIM TENDRILS **[two-actions] **SPELL 1** **CONCENTRATE** **MANIPULATE** **VOID** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/2']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `34`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5', 'PZO22001 Starfinder Player Core 330-363::/page/5/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/32', 'PZO22001 Starfinder Player Core 330-363::/page/6/Text/26', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` | 0.679686 | **CONCENTRATE** **MANIPULATE** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/2` | 0.664411 | **GRIM TENDRILS **[two-actions] **SPELL 1** **CONCENTRATE** **MANIPULATE** **VOID**  **Traditions** arcane, occult  **Area** 30-foot line  **Defense** Fortitude  Tendrils of darkness curl out from you |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.663684 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/26` | 0.642399 | **HARM **[one-action]** TO **[three-actions] **SPELL 1**  **MANIPULATE** **VOID**  **Traditions** divine  **Range **varies; **Targets** 1 living creature or 1 willing undead  creature  You channel voi |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/12` | 0.633667 | **EXECUTE **[two-actions] **SPELL 7**  **CONCENTRATE** **DEATH** **MANIPULATE** **VOID**  **Traditions** divine, primal  **Range **30 feet; **Targets** 1 creature  **Defense** basic Fortitude  You poi |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/47` | 0.593813 | **DISPEL MAGIC **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **120 feet;** Targets** 1 spell effect or unattended magic  item  You |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/26/SectionHeader/39` | 0.591579 | **SANCTUARY **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** divine, occult  **Range **touch;** Targets** 1 creature  **Duration** 1 minute  You ward a creature with protect |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.591288 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/29` | 0.591075 | **STUPEFY **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** varies  You du |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/30/Text/15` | 0.590427 | **SKIM DATA **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **touch; **Targets** one dataset contained within a  touched object  You touch one objec |

### Query 135
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/68']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/33/Text/71', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/68', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/69', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/74', 'PZO22001 Starfinder Player Core 330-363::/page/25/Text/67']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/71` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/67` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/68` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/69` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/74` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/67` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/77` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/52` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/51` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/69` | 0.887439 | **GLOSSARY & ** **INDEX** |

### Query 136
- Text: Summarize Cone of spirit (Will)
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/501']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/501', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/497', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/493', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/36', 'PZO22001 Starfinder Player Core 330-363::/page/20/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/501` | 0.918859 | Cone of spirit (Will) |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/497` | 0.857609 | Cone of mental (Will) |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/493` | 0.643084 | Cone of poison (Fortitude) |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/36` | 0.641438 | **Defense** Will |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/20/Text/10` | 0.583667 | **AC **13; **Fort **+0, **Ref **+4, **Will **+0 |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/44` | 0.527177 | **DIZZYING COLORS **[two-actions] **SPELL 1**  **CONCENTRATE** **ILLUSION** **INCAPACITATION** **MANIPULATE** **VISUAL**  **Traditions** arcane, occult  **Area** 15-foot cone  **Defense** Will; **Dura |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/29/ListItem/2` | 0.524293 | **Weal** The results will be good. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/505` | 0.522065 | Cone of piercing (Reflex) |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/17/SectionHeader/14` | 0.510836 | **NEVER MIND **[two-actions] **SPELL 6**  **CONCENTRATE** **CURSE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature **Defense** W |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/22/SectionHeader/37` | 0.508383 | **POSSESSION **[two-actions] **SPELL 7**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL** **POSSESSION**  **Traditions** occult  **Range **30 feet; **Targets** 1 living creat |

### Query 137
- Text: What is the rule about **SKILLS** **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/60']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/60', 'PZO22001 Starfinder Player Core 330-363::/page/33/Text/61', 'PZO22001 Starfinder Player Core 330-363::/page/27/Text/60', 'PZO22001 Starfinder Player Core 330-363::/page/25/Text/58', 'PZO22001 Starfinder Player Core 330-363::/page/19/Text/69']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/60` | 0.823624 | **SKILLS** **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/60` | 0.703015 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/58` | 0.703015 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/69` | 0.703015 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/61` | 0.703015 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/65` | 0.661015 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/61` | 0.661015 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/58` | 0.661015 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/42` | 0.661015 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/64` | 0.661015 | **SKILLS** |

### Query 138
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/55', 'PZO22001 Starfinder Player Core 330-363::/page/5/Text/28', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/61', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/57', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/39']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/28` | 0.913367 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/55` | 0.913367 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/39` | 0.913367 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/57` | 0.913367 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/61` | 0.913367 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/62` | 0.871367 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/57` | 0.871367 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/58` | 0.871367 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/56` | 0.871367 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/55` | 0.871367 | **INTRODUCTION** |

### Query 139
- Text: What is the rule about systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `34`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/15', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/24', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.921515 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.631763 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/19` | 0.613198 | are determined by their connection, and a witchwarper's are  determined by their paradox. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/24` | 0.586036 | spells and precog warp spells, your mystic spells would  remain divine and the witchwarper spells occult. Similarly,  you need to use the attribute modifier determined by the  source of the focus spel |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.573566 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/14` | 0.538327 | The practitioners of occult traditions seek  to understand the unexplainable, categorize  the bizarre, and otherwise access the ephemeral in a |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.525955 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.515654 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.507809 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/2` | 0.506094 | Spellcasters cast spells from one of four different spell lists, each representing a different magical tradition: arcane,  divine, occult, and primal. |

### Query 140
- Text: What does **CLEAR MIND **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54', 'PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/28/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39', 'PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` | 0.746473 | **CLEAR MIND **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You drive menta |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/5` | 0.627303 | **DETECT THOUGHTS **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult **Area** 30-foot emanation  **Defense** Will  You sense the presence of thinking |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.627283 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/39` | 0.626520 | **CLEANSE AFFLICTION **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  Gentle restorative |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/17/SectionHeader/14` | 0.618185 | **NEVER MIND **[two-actions] **SPELL 6**  **CONCENTRATE** **CURSE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature **Defense** W |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/18` | 0.615014 | **DIVINE INSPIRATION **[two-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine  **Range **touch;** Targets** 1 willing creature  You infuse a target with spiritual |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.607627 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/32/Text/2` | 0.600477 | **SOUND BODY **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You send a su |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/29` | 0.597108 | **STUPEFY **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** varies  You du |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/15/SectionHeader/3` | 0.587843 | **MIND READING **[two-actions] **SPELL 3**  **UNCOMMON** **CONCENTRATE** **DETECTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature  **Defense** W |

### Query 141
- Text: What is the rule about Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to cosmic forces, and  others rewrite the underlying code of the universe to cast  their spells.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `47`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/7', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/4', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/1', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` | 0.969672 | Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.734450 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/4` | 0.726869 | With special gestures and utterances, a spellcaster can  call forth mystic energies, warp the mind, protect themself  against danger, or even create something from nothing.  Each class has its own met |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/1` | 0.686304 | Whether it comes in the form of eldritch artifacts, otherworldly beings, or witchwarpers altering  reality with strange spells, magic brings fantasy and wonder to Starfinder. This chapter explains how |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/2` | 0.686256 | The grand variety of spells includes those in the following pages and far more. Taught at magical  academies, drawn from other worlds, bestowed by mystical connections, and granted by all manner of  u |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.637051 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/3` | 0.635440 | The casting of a spell can range from a simple word of magical  might that creates a fleeting effect to a complex process  taking hours to cast and producing a long-term impact.  Casting a spell requi |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/12` | 0.630023 | After Triune's Signal connected cultures across the  Universe, the peoples of the galaxy have learned more  than ever before about the Universe's composition  thanks to science and technology. As tech |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/4` | 0.625724 | Spellcasting creates obvious sensory manifestations, such  as bright lights, crackling sounds, and sharp smells from the  gathering magic. Nearly all spells manifest a spell signature—a  colorful, glo |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.622487 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |

### Query 142
- Text: Summarize **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/31', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/75', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/68', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/31` | 0.929192 | **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/75` | 0.929192 | **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/66` | 0.879192 | **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/76` | 0.879192 | **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/51` | 0.879192 | **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/68` | 0.828418 | **APPENDIX** **GLOSSARY & ** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/42` | 0.824459 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/32` | 0.824459 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/74` | 0.782459 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/71` | 0.782459 | **CONDITIONS ** **APPENDIX** |

### Query 143
- Text: What does **Traditions** arcane, divine, occult, primal do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/6', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/34', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/45', 'PZO22001 Starfinder Player Core 330-363::/page/8/Text/24', 'PZO22001 Starfinder Player Core 330-363::/page/13/SectionHeader/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/6` | 0.883139 | **Traditions** arcane, divine, occult, primal |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/34` | 0.831278 | **Traditions** divine, occult, primal |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/45` | 0.792184 | **Traditions** divine, primal |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/24` | 0.679226 | **Traditions** occult |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/13/SectionHeader/43` | 0.633082 | **MANIFESTATION **[three-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  You spin secrets from the fundaments of magic, shaping them  into a power |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.601981 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1` | 0.598159 | **MAGICAL TRADITIONS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/2` | 0.572021 | Spellcasters cast spells from one of four different spell lists, each representing a different magical tradition: arcane,  divine, occult, and primal. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/14` | 0.569315 | The practitioners of occult traditions seek  to understand the unexplainable, categorize  the bizarre, and otherwise access the ephemeral in a |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/20` | 0.557280 | **Tradition Resistance** If the dragon's magical tradition  matches that of your *dragon form* spell, you gain the  listed ability. **Arcane** resistance 5 against damage from  spells; **divine** resi |

### Query 144
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/73']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/33/Text/70', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/67', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/68', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/73', 'PZO22001 Starfinder Player Core 330-363::/page/11/Text/71']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/70` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/67` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/68` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/73` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/71` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/68` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/78` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/66` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/50` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/92` | 0.900802 | **CONDITIONS ** **APPENDIX** |

### Query 145
- Text: Summarize **Polymorph**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `32`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/3', 'PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8', 'PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/11', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/13` | 0.886981 | **Polymorph** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/3` | 0.660740 | **SPELLSHAPE** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.660083 | **Summoned** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/11` | 0.653521 | **Morph** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.603675 | **SUBTLE SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/79` | 0.553185 | **GAME** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/33` | 0.550212 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/16` | 0.545548 | **Illusions** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/70` | 0.545185 | **GAME** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/13` | 0.544130 | **Occult** |

### Query 146
- Text: What does **ENLARGE **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/Text/4']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `23`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/32', 'PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/11', 'PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51', 'PZO22001 Starfinder Player Core 330-363::/page/0/Text/4', 'PZO22001 Starfinder Player Core 330-363::/page/32/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.672139 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/11` | 0.656844 | **STATUS **[two-actions] **SPELL 2**  **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch;** Targets** 1 willing living creature  **Duration** until yo |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.653471 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/4` | 0.637213 | **ENLARGE **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Range **30 feet;** Targets** 1 willing creature  **Duration** 5 minutes  Bolstered |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/32/Text/2` | 0.634988 | **SOUND BODY **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You send a su |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.600836 | SPELL ATTACKS |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/17` | 0.591010 | **KNOCK **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 door, lock, or container  **Duration** 1 minute  You make the targe |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/37` | 0.588385 | **REVEALING LIGHT **[two-actions] **SPELL 2**  **CONCENTRATE** **LIGHT** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **120 feet;** Area** 10-foot burst  **Defense** Reflex; * |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/2/SectionHeader/1` | 0.587805 | **FALSE VITALITY **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Duration** 8 hours  You augment your flesh with the energies typically used to  manipulat |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/35/SectionHeader/14` | 0.586440 | **EMBED MESSAGE **[two-actions] **SPELL 2**  **CONCENTRATE** **ILLUSION** **MANIPULATE**  **Traditions** arcane, occult  **Range **touch; **Targets** 1 object or willing creature  **Duration** unlimit |

### Query 147
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/42']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/9/Text/92', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/42', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/71', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/31/Text/66']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/42` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/66` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/92` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/32` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/71` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/49` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/74` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/92` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/65` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/86` | 0.908802 | **CONDITIONS ** **APPENDIX** |

### Query 148
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/62']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/33/Text/64', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/67', 'PZO22001 Starfinder Player Core 330-363::/page/17/Text/45', 'PZO22001 Starfinder Player Core 330-363::/page/19/Text/72', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/61']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.806592 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.806592 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.806592 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.806592 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.806592 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.764592 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.764592 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.764592 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.764592 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/62` | 0.764592 | **SPELLS** |

### Query 149
- Text: Summarize Primal
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/503']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `15`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/503', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/45', 'PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/44', 'PZO22001 Starfinder Player Core 330-363::/page/8/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/503` | 0.799548 | Primal |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/17` | 0.626243 | **Primal** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/57` | 0.602506 | PRIMAL 1ST-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/45` | 0.597199 | **Traditions** divine, primal |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/64` | 0.574944 | PRIMAL 10TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` | 0.569304 | **CONCENTRATE** **MANIPULATE** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.561444 | **CONCENTRATE** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/44` | 0.561444 | **CONCENTRATE** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/17` | 0.560184 | PRIMAL 2ND-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/48` | 0.560070 | PRIMAL 8TH-RANK SPELLS |

### Query 150
- Text: What is the rule about **Spell Lists**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/62']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `21`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/27/Text/63', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/68', 'PZO22001 Starfinder Player Core 330-363::/page/15/Text/61', 'PZO22001 Starfinder Player Core 330-363::/page/25/Text/61', 'PZO22001 Starfinder Player Core 330-363::/page/19/Text/73']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/63` | 0.782608 | **Spell Lists** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/73` | 0.782608 | **Spell Lists** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/61` | 0.782608 | **Spell Lists** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/61` | 0.782608 | **Spell Lists** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/68` | 0.782608 | **Spell Lists** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/65` | 0.740608 | **Spell Lists** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/63` | 0.740608 | **Spell Lists** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/62` | 0.740608 | **Spell Lists** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/63` | 0.740608 | **Spell Lists** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/46` | 0.740608 | **Spell Lists** |

### Query 151
- Text: What is the rule about CHAPTER 7: SPELLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `33`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/34', 'PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/57']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.904519 | CHAPTER 7: SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/5` | 0.716278 | OCCULT 7TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.706794 | SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/34` | 0.693216 | PRIMAL 7TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/57` | 0.686854 | ARCANE 7TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/11` | 0.635402 | DIVINE 7TH-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/74` | 0.607134 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/65` | 0.607134 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/80` | 0.607134 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/36` | 0.607134 | **SPELLS** |

### Query 152
- Text: Summarize **Critical Success** The creature is unaffected.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/7']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/30/Text/38', 'PZO22001 Starfinder Player Core 330-363::/page/28/Text/30', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/6/Text/8', 'PZO22001 Starfinder Player Core 330-363::/page/14/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/30/Text/38` | 1.017259 | **Critical Success** The creature is unaffected. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/30` | 1.017259 | **Critical Success** The creature is unaffected. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/2` | 1.017259 | **Critical Success** The creature is unaffected. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/14` | 1.017259 | **Critical Success** The creature is unaffected. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/8` | 1.017259 | **Critical Success** The creature is unaffected. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/50` | 0.975259 | **Critical Success** The creature is unaffected. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/7` | 0.975259 | **Critical Success** The creature is unaffected. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/19` | 0.975259 | **Critical Success** The creature is unaffected. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/20` | 0.975259 | **Critical Success** The creature is unaffected. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/30/Text/11` | 0.975052 | **Critical Success **The creature is unaffected. |

### Query 153
- Text: What does **CARCINIZATION **[two-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/15', 'PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/40', 'PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26', 'PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/25/SectionHeader/21` | 0.678038 | **CARCINIZATION **[two-actions] **SPELL 5**  **INCAPACITATION** **MANIPULATE** **POLYMORPH**  **Traditions** primal  **Range **30 feet;** Targets** 1 creature  **Defense** Fortitude; **Duration** 1 mi |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/15` | 0.620017 | ARCANE 5TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/40` | 0.609313 | OCCULT 5TH-RANK SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/23/SectionHeader/26` | 0.597668 | **BANISHMENT **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet; **Targets** 1 creature that isn't on its |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/7` | 0.595963 | PRIMAL 5TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/54` | 0.552452 | DIVINE 5TH-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` | 0.549972 | **CONTROL MACHINE **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature or hazard with t |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/23` | 0.544200 | **ATOMIC BLAST **[three-actions] **SPELL 9**  **CONCENTRATE** **FIRE** **MANIPULATE** **RADIATION**  **Traditions** arcane, primal  **Range **500 feet;** Area** 100-foot burst **Defense** Reflex; **Du |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/39` | 0.542847 | **SUBCONSCIOUS SUGGESTION **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **LINGUISTIC** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet;** Targe |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/12` | 0.528225 | **HALLUCINATION **[two-actions] **SPELL 5**  **ILLUSION** **INCAPACITATION** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** 1 creature  **Duration* |

### Query 154
- Text: What is the rule about Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your pool is equal to the number of focus spells you  know or 3, whichever is lower. This counts only spells that  require Focus Points to cast.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `35`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/15', 'PZO22001 Starfinder Player Core 294-329::/page/4/Text/5', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/13', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` | 1.007599 | Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your p |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.798869 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/23` | 0.795824 | It's possible, especially through archetypes, to gain focus  spells from more than one source. If this happens, you  have just one focus pool, counting all your focus spells to  determine the points i |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` | 0.761419 | Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.742107 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/14` | 0.707931 | Focus spells are automatically heightened to half your level  rounded up, just like cantrips are. You can't cast a focus spell  if its minimum rank is greater than half your level rounded  up, even if |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/6` | 0.682479 | Characters of spellcasting classes can cast a number of spells  each day; the spells you can cast in a day are referred to as  spell slots. At 1st level, a character has only a small number  of 1st-ra |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/16` | 0.664374 | You replenish all the Focus Points in your pool during your  daily preparations. You can also use the Refocus activity to  pray, study, meditate, or otherwise reattune yourself to the  source of your |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/7` | 0.660403 | Some spells require you to pay a cost or provide a locus. If the  spell lists a **cost**, you must have the listed money, valuable  materials, or other resources to cast the spell (such as gems or  ma |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/9` | 0.654403 | Each prepared spell is expended after a single casting,  so if you want to cast a particular spell more than once in  a day, you need to prepare that spell multiple times. The  exception to this rule |

### Query 155
- Text: What does **CATACLYSM **[two-actions] **SPELL 10** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/29', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29', 'PZO22001 Starfinder Player Core 294-329::/page/22/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/55']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/26/SectionHeader/5` | 0.687211 | **CATACLYSM **[two-actions] **SPELL 10**  **ACID** **AIR** **COLD** **CONCENTRATE** **EARTH** **ELECTRICITY** **FIRE** **MANIPULATE** **WATER**  **Traditions** arcane, primal  **Range **1,000 feet;** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/29` | 0.649491 | OCCULT 10TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/29` | 0.630418 | **CONTROL MACHINE **[two-actions] **SPELL 5**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature or hazard with t |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/23` | 0.614564 | **ATOMIC BLAST **[three-actions] **SPELL 9**  **CONCENTRATE** **FIRE** **MANIPULATE** **RADIATION**  **Traditions** arcane, primal  **Range **500 feet;** Area** 100-foot burst **Defense** Reflex; **Du |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/55` | 0.608588 | **DOMINATE **[two-actions] **SPELL 6**  **UNCOMMON** **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult  **Range **30 feet;** Targets** 1 creature  **D |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47` | 0.591357 | **REVIVAL **[two-actions] **SPELL 10**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet;** Targets** dead creatures and living creatures of  y |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/10/SectionHeader/33` | 0.581127 | **INDESTRUCTIBILITY **[two-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Duration** until the start of your next turn  You sever yourself from |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/32` | 0.573083 | **PHANTASMAGORIA **[two-actions] **SPELL 9**  **CONCENTRATE** **DEATH** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **120 feet; **Targets** any number of creatures |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/43` | 0.572027 | **PHANTASMAL CALAMITY **[two-actions] **SPELL 6**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **500 feet; **Area** 30-foot burst  **Defense** Will |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/1` | 0.571322 | **HEROISM **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult **Duration** 10 minutes |

### Query 156
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/29', 'PZO22001 Starfinder Player Core 294-329::/page/15/Text/85', 'PZO22001 Starfinder Player Core 294-329::/page/17/Text/91', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/79', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/64']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/29` | 0.938833 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/85` | 0.938833 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/91` | 0.938833 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/79` | 0.938833 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/64` | 0.938833 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/70` | 0.896833 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/88` | 0.896833 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/65` | 0.896833 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/41` | 0.896833 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/48` | 0.896833 | **PLAYING THE ** **GAME** |

### Query 157
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/43']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/23/Text/50', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/33', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/43', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/72']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/32` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/50` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/33` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/43` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/72` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/40` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/81` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/66` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/93` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/67` | 0.887439 | **GLOSSARY & ** **INDEX** |

### Query 158
- Text: What is the rule about **Focus Spells**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/70']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `21`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/27/Text/65', 'PZO22001 Starfinder Player Core 330-363::/page/23/Text/72', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/70', 'PZO22001 Starfinder Player Core 330-363::/page/15/Text/63', 'PZO22001 Starfinder Player Core 330-363::/page/11/Text/67']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/65` | 0.849140 | **Focus Spells** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/67` | 0.849140 | **Focus Spells** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/63` | 0.849140 | **Focus Spells** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/72` | 0.849140 | **Focus Spells** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/70` | 0.849140 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/63` | 0.807140 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/64` | 0.807140 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/75` | 0.807140 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/65` | 0.807140 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/67` | 0.807140 | **Focus Spells** |

### Query 159
- Text: What is the rule about You spend 10 minutes performing deeds to restore your  magical connection. This restores 1 Focus Point to your focus  pool. The deeds you need to perform are specified in the class  or ability that gives you your focus spells. These deeds can  usually overlap with other tasks that relate to the source  of your focus spells. For instance, a witchwarper with focus  points from their paradox can usually Refocus while using  their paradox skill.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/20', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/23', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/16', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/13', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/20` | 1.010213 | You spend 10 minutes performing deeds to restore your  magical connection. This restores 1 Focus Point to your focus  pool. The deeds you need to perform are specified in the class  or ability that gi |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/23` | 0.714019 | It's possible, especially through archetypes, to gain focus  spells from more than one source. If this happens, you  have just one focus pool, counting all your focus spells to  determine the points i |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/16` | 0.700355 | You replenish all the Focus Points in your pool during your  daily preparations. You can also use the Refocus activity to  pray, study, meditate, or otherwise reattune yourself to the  source of your |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/13` | 0.696580 | Focus spells are a special type of spell attained directly from  a specific source, such as a field of study, connection to a  mystical force, or exposure to an alternate reality. You can  learn focus |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.690096 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/21` | 0.647519 | If you get focus spells from a class or other source that  doesn't grant spellcasting ability, the ability that gives you  focus spells also provides your proficiency for your spell  attack modifier a |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/15` | 0.643241 | Casting any of your focus spells costs you 1 Focus Point.  You automatically gain a focus pool the first time you gain an  ability that gives you a focus spell. The maximum number of  points in your p |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/31/SectionHeader/47` | 0.641460 | **DISPEL MAGIC **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **120 feet;** Targets** 1 spell effect or unattended magic  item  You |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/18` | 0.639194 | **DIVINE INSPIRATION **[two-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine  **Range **touch;** Targets** 1 willing creature  You infuse a target with spiritual |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/5` | 0.634523 | Spells can vary in how many actions they take, as shown in  the spell's stat block. You cast cantrips, spells from spell slots,  and focus spells using the same process, but must expend the  spell whe |

### Query 160
- Text: What is the rule about **Heightened (8th)** Choose to either target any number of  creatures or change the spell's duration to unlimited.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/6/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `38`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/6/Text/25', 'PZO22001 Starfinder Player Core 330-363::/page/6/Text/24', 'PZO22001 Starfinder Player Core 330-363::/page/14/Text/6', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/50', 'PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/25` | 0.922683 | **Heightened (8th)** Choose to either target any number of  creatures or change the spell's duration to unlimited. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/24` | 0.804045 | **Heightened (6th)** Choose to either target up to 10 creatures  or change the spell's duration to until your next daily  preparations. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/6` | 0.732871 | **Heightened (8th)** You can target up to 5 creatures. If a  creature uses a hostile action or reaction that affects  multiple targets simultaneously, it needs to attempt only  one save against *mask |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/50` | 0.713188 | **Heightened (7th)** You can target up to 5 additional creatures  to gain protection against the environment the triggering  creature entered. The spell lasts for 8 hours and also  protects against ex |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/11` | 0.702326 | **STATUS **[two-actions] **SPELL 2**  **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch;** Targets** 1 willing living creature  **Duration** until yo |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/51` | 0.668053 | **Heightened (10th)** You can target up to 10 additional  creatures to gain protection against the environment the  triggering creature entered. The spell lasts until your next  daily preparations and |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/36` | 0.658708 | **HASTE **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Range **30 feet;** Targets** 1 creature  **Duration** 1 minute  Magic empowers the target |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/25` | 0.658260 | **Heightened (6th)** The spell's range is touch and it targets 1 willing  creature. The duration is until your next daily preparations. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/1` | 0.655993 | **Heightened (5th)** The spell's range is touch and it targets  1 willing creature. The duration is until your next daily  preparations. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47` | 0.652669 | **REVIVAL **[two-actions] **SPELL 10**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet;** Targets** dead creatures and living creatures of  y |

### Query 161
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/32']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/9/Text/92', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/42', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/71', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/31/Text/66']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/42` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/66` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/92` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/32` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/71` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/49` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/74` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/92` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/65` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/86` | 0.908802 | **CONDITIONS ** **APPENDIX** |

### Query 162
- Text: What is the rule about **Heightened (+1)** The damage increases by 1d6.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/18/Text/23', 'PZO22001 Starfinder Player Core 330-363::/page/23/Text/54', 'PZO22001 Starfinder Player Core 330-363::/page/5/Text/11', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/2` | 0.887901 | **Heightened (+1)** The damage increases by 1d6. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/23` | 0.855756 | **Heightened (+1)** The damage increases by 1d10. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/32/Text/17` | 0.830353 | **Heightened (+1)** The damage increases by 1d6 and persistent  damage increases by 1d6. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/54` | 0.826589 | **Heightened (+1)** The damage increases by 2d4. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/34/Text/37` | 0.809002 | **Heightened (+1)** The damage increases by 1d12. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/32/Text/43` | 0.805756 | **Heightened (+1)** The damage increases by 1d10. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/24/Text/12` | 0.805756 | **Heightened (+1)** The damage increases by 1d10. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/11` | 0.783816 | **Heightened (+1)** The void damage increases by 2d4, and the  persistent bleed damage increases by 1. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/34` | 0.763459 | **Heightened (+1)** The damage increases by 2d6 (or by 2d8 if  the target is a divine spellcaster). |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/6` | 0.751057 | **Heightened (+1)** The damage of the image's Strikes increases  by 1d4, and the maximum size of creature you can create  increases by one (to a maximum of Gargantuan). |

### Query 163
- Text: Summarize The target can soar through the air, gaining a fly Speed equal  to its Speed or 20 feet, whichever is greater.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/9', 'PZO22001 Starfinder Player Core 330-363::/page/20/Text/20', 'PZO22001 Starfinder Player Core 330-363::/page/20/ListItem/16', 'PZO22001 Starfinder Player Core 330-363::/page/20/Text/12', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/47']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/9` | 1.002090 | The target can soar through the air, gaining a fly Speed equal  to its Speed or 20 feet, whichever is greater. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/20/Text/20` | 0.785576 | **Heightened (4th)** You can turn into a flying creature, such as  a bird, which grants you a fly Speed of 20 feet. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/2` | 0.746047 | **Fly**H Grant a target a fly Speed. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/25` | 0.744703 | **Fly**H Grant the target a fly Speed. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/76` | 0.744703 | **Fly**H Grant the target a fly Speed. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/20/ListItem/16` | 0.731073 | Speed 20 feet. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/20/Text/12` | 0.711944 | **Speed **fly 30 feet |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/47` | 0.683624 | **Range **60 feet; **Targets** the triggering creature |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/13` | 0.662349 | Speed 40 feet, fly 100 feet. You gain any of the following  Speeds the chosen dragon has, but with the listed  amount: burrow 20 feet, climb 40 feet, swim 60 feet. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/19/ListItem/50` | 0.647573 | **Bird** Speed 10 feet, fly 50 feet; **Melee **[one-action] beak, **Damage ** 2d8 piercing; **Melee **[one-action] talon (agile), **Damage **1d10  slashing. |

### Query 164
- Text: What is the rule about **Success** The creature takes half damage and is slowed 1 until  the end of its next turn.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/3', 'PZO22001 Starfinder Player Core 330-363::/page/28/Text/31', 'PZO22001 Starfinder Player Core 330-363::/page/23/Text/51', 'PZO22001 Starfinder Player Core 330-363::/page/18/Text/20', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/3` | 0.887204 | **Success** The creature takes half damage and is slowed 1 until  the end of its next turn. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/31` | 0.784610 | **Success** The creature takes half damage. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/20` | 0.784610 | **Success** The creature takes half damage. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/51` | 0.784610 | **Success** The creature takes half damage. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/4` | 0.775829 | **Failure** The creature takes full damage, is slowed 3 until the  end of its next turn, and slowed 1 for 1 minute. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/19` | 0.734610 | **Success** The creature takes half damage. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/24/Text/9` | 0.734610 | **Success** The creature takes half damage. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/34/Text/34` | 0.734610 | **Success** The creature takes half damage. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/12` | 0.734610 | **Success** The creature takes half damage. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/34/Text/14` | 0.734610 | **Success** The creature takes half damage. |

### Query 165
- Text: Summarize TARGETS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `34`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22', 'PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/42', 'PZO22001 Starfinder Player Core 294-329::/page/11/Text/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/20` | 0.819956 | TARGETS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22` | 0.672032 | FOCUS POINTS FROM MULTIPLE  SOURCES |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/14` | 0.670988 | RANGES, AREAS, AND  TARGETS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/42` | 0.628946 | **Analyze** **Target**H Gather data about a target's basic physiology. **Daze**H Cloud a creature's mind and possibly stun it. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/29` | 0.628946 | **Analyze** **Target**H Gather data about a target's basic physiology. **Daze**H Cloud a creature's mind and possibly stun it. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/44` | 0.612749 | **CONCENTRATE** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.612749 | **CONCENTRATE** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` | 0.602713 | **CONCENTRATE** **MANIPULATE** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/89` | 0.579400 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/71` | 0.579400 | **Focus Spells** |

### Query 166
- Text: What is the rule about The image can't speak, but you can use your actions to  speak through the creature, with the spell disguising your  voice as appropriate. You might need to attempt a Deception  or Performance check to mimic the creature, as determined  by the GM. This is especially likely if you're trying to imitate a  specific person and engage with someone that person knows.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/10/Text/3', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/1', 'PZO22001 Starfinder Player Core 330-363::/page/10/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/2` | 1.015358 | The image can't speak, but you can use your actions to  speak through the creature, with the spell disguising your  voice as appropriate. You might need to attempt a Deception  or Performance check to |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/10/Text/3` | 0.745489 | **Heightened (6th)** Creatures or objects in your scene can  speak. You must speak the specific lines for each actor  when creating your program. The spell disguises your  voice for each actor. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/1` | 0.716154 | You create an illusory image of a Large or smaller creature. It  generates the appropriate sounds, smells, and feels believable  to the touch. If you and the image are ever farther than 500  feet apar |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/10/Text/2` | 0.701636 | Any creature that touches any part of the image or uses  the Seek action to examine it can attempt to disbelieve  your illusion. If they interact with a portion of the illusion,  they disbelieve only |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/5` | 0.700335 | Any creature that touches the image or uses the Seek  action to examine it can attempt to disbelieve your illusion.  When a creature disbelieves the illusion, it recovers from half  the damage it had |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/17` | 0.686772 | Magic with the illusion trait creates false sensory stimuli.  Sometimes illusions allow creatures a chance to disbelieve  the spell, which lets the creature ignore the spell if it succeeds  at doing s |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/3` | 0.686755 | The casting of a spell can range from a simple word of magical  might that creates a fleeting effect to a complex process  taking hours to cast and producing a long-term impact.  Casting a spell requi |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/4/Text/21` | 0.683416 | Some spells allow you to target a creature, an object, or  something more specific. The target must be within the  spell's range, and you must be able to see it (or otherwise  perceive it with a preci |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/9` | 0.665005 | A creature called by a spell or effect gains the summoned  trait. A summoned creature can't summon other creatures,  create things of value, or cast spells that require a cost. It  has the minion trai |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/4` | 0.663424 | The illusion can cause damage by making the target believe  the illusion's attacks are real, but it cannot otherwise directly  affect the physical world. If the illusory creature hits with a  Strike, |

### Query 167
- Text: What is the rule about SPELL SLOTS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `31`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/13', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5` | 0.858990 | SPELL SLOTS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/19/SectionHeader/1` | 0.659501 | SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.646041 | SPELL ATTACKS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/13` | 0.625730 | SUSTAINING SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.622034 | CHAPTER 7: SPELLS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/3` | 0.557830 | IDENTIFYING SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/8/SectionHeader/1` | 0.552791 | SPELL LISTS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/62` | 0.551476 | **Spells** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/61` | 0.551476 | **Spells** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/67` | 0.551476 | **Spells** |

### Query 168
- Text: Summarize Tradition
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/487']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `21`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/487', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/45', 'PZO22001 Starfinder Player Core 330-363::/page/27/Text/66', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/66', 'PZO22001 Starfinder Player Core 330-363::/page/11/Text/68']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/487` | 0.704175 | Tradition |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.545791 | insight about a topic. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/45` | 0.542353 | **Traditions** divine, primal |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/66` | 0.530840 | **Rituals** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/68` | 0.530840 | **Rituals** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/66` | 0.530840 | **Rituals** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/6` | 0.505688 | COUNTERACTING |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/1` | 0.496740 | **MAGICAL TRADITIONS** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22` | 0.494070 | FOCUS POINTS FROM MULTIPLE  SOURCES |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.493747 | **Summoned** |

### Query 169
- Text: What does **GRAVITY FIELD **[three-actions] **SPELL 8** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/46']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `27`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/46', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/26', 'PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/54', 'PZO22001 Starfinder Player Core 330-363::/page/6/Text/44']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/46` | 0.744613 | **GRAVITY FIELD **[three-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **100 feet; **Area** 30-foot radius, 100-foot-tall cylinder  **Dur |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.613298 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/26` | 0.602789 | **FIELD OF LIFE **[two-actions] **SPELL 6**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet; **Area** 20-foot burst **Duration** sustained up |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/54` | 0.588061 | **PERSONAL GRAVITY **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Duration** 1 hour  You alter gravity's effects on you. You treat gravity as if |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/44` | 0.584334 | **HEAL **[one-action]** TO **[three-actions] **SPELL 1**  **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **varies; **Targets** 1 willing living creature or 1 undead  c |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/48` | 0.565325 | PRIMAL 8TH-RANK SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/17` | 0.565063 | OCCULT 8TH-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/36` | 0.559059 | **EARTHBIND **[two-actions] **SPELL 3**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 flying creature  **Defense** Fortitude; **Duration** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/47` | 0.556471 | **EARTHQUAKE **[two-actions] **SPELL 8**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Area** 60-foot burst  **Duration** 1 round  You shake the groun |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/19` | 0.538725 | **Gravity** **Field** Create a field of increased gravity in an area as  you desire. |

### Query 170
- Text: Summarize LONG CASTING TIMES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `30`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/9', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/15', 'PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/2', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/9` | 0.866559 | LONG CASTING TIMES |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/15` | 0.732872 | LONG DURATIONS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/2` | 0.641742 | CASTING SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21` | 0.609502 | SPELLCASTERS WITH FOCUS  SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/9` | 0.600353 | DURATIONS |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/8` | 0.558010 | **Duration** 5 minutes |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/32/Text/31` | 0.545645 | **Heightened (4th)** The duration is 8 hours. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/48` | 0.541283 | **Duration** 1 minute |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/22` | 0.541037 | FOCUS POINTS FROM MULTIPLE  SOURCES |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/1` | 0.537685 | **SUBTLE SPELLS** |

### Query 171
- Text: What is the rule about beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `37`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/18', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/12', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.854248 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.571904 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/12` | 0.561670 | After Triune's Signal connected cultures across the  Universe, the peoples of the galaxy have learned more  than ever before about the Universe's composition  thanks to science and technology. As tech |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/3` | 0.560271 | Even with the widespread presence of technology,  spellcasters can be found in every corner of the galaxy.  Some spellcasters draw magic from other realities, some  from their mystical connections to |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/7` | 0.556074 | Arcane spellcasters use logic and  rationality to categorize the magic inherent  in the world around them. Because of its far-reaching  approach, the arcane tradition has the broadest spell  list, tho |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/10` | 0.513752 | The power of the divine is steeped in faith,  the unseen, and belief in a power source from |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/15` | 0.509710 | systematic way. Witchwarpers touched by the Gap or  alternate timelines, as well as mystics who are psychically  linked to the Akashic Record, are occult spellcasters. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/3` | 0.505519 | Your class determines which tradition of magic your spells use. In some cases, such as when a mystic gains spells from  their connection or when a witchwarper learns spells from their paradox, you mig |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/22` | 0.504106 | If you are a spellcaster, your focus spells are the same tradition  of spell as the class that gave you the focus spell. A mystic's |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/19` | 0.491283 | are determined by their connection, and a witchwarper's are  determined by their paradox. |

### Query 172
- Text: Summarize Your senses improve as you gain feline eyes, ears, and  whiskers. You gain darkvision and electromagnetic scent  as an imprecise sense out to 30 feet, allowing you to detect  living and technological creatures.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `13`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/23', 'PZO22001 Starfinder Player Core 330-363::/page/20/ListItem/18', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/1', 'PZO22001 Starfinder Player Core 330-363::/page/8/Text/3', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/33']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/23` | 1.036196 | Your senses improve as you gain feline eyes, ears, and  whiskers. You gain darkvision and electromagnetic scent  as an imprecise sense out to 30 feet, allowing you to detect  living and technological |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/54` | 0.809276 | **Feline** **Senses**H The target's senses improve with feline ears,  eyes, and whiskers. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/29` | 0.809276 | **Feline** **Senses**H The target's senses improve with feline ears,  eyes, and whiskers. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/20/ListItem/18` | 0.723463 | Low-light vision and imprecise scent 30 feet. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/1` | 0.691412 | You create an illusory image of a Large or smaller creature. It  generates the appropriate sounds, smells, and feels believable  to the touch. If you and the image are ever farther than 500  feet apar |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/3` | 0.689765 | **Heightened (3rd)** You gain darkvision or low-light vision if the  form you assume has that ability. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/33` | 0.686943 | **FIGMENT **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet  **Duration** sustained  You create a simp |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/21/ListItem/13` | 0.673463 | Low-light vision and imprecise scent 30 feet. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/34` | 0.656478 | **Measure**H You get measurements of creatures you can  observe in the area. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/17` | 0.656478 | **Measure**H You get measurements of creatures you can  observe in the area. |

### Query 173
- Text: What is the rule about Falsehoods pass your lips as smoothly as silk. You gain a  +4 status bonus to Deception checks to Lie and against  Perception checks to discern if you are telling the truth, and  you add your level even if untrained. If the implausibility of  your lies prompts a circumstance penalty or a DC increase,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/73']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/73', 'PZO22001 Starfinder Player Core 330-363::/page/8/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/15/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/15/Text/1', 'PZO22001 Starfinder Player Core 330-363::/page/16/SectionHeader/28']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/73` | 1.008111 | Falsehoods pass your lips as smoothly as silk. You gain a  +4 status bonus to Deception checks to Lie and against  Perception checks to discern if you are telling the truth, and  you add your level ev |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/2` | 0.726725 | *Humanoid form* grants you a +4 status bonus to Deception  checks to pass as a generic member of the chosen ancestry,  and you add your level even if you're untrained, but you  can't make yourself loo |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/2` | 0.677095 | **Critical Failure** As failure, and the target takes a –4  circumstance penalty to Deception checks against your  questions. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/1` | 0.650071 | **Failure** Each round of the spell's duration, you can Sustain the  spell to ask a different question and attempt to uncover  the answer. For each question, the target can attempt  a Deception check |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/16/SectionHeader/28` | 0.639557 | **MYSTIC ARMOR **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Duration** until your next daily preparations  You ward yourself with shimm |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/13` | 0.597776 | Disguises and illusions fool the spell as long as they  appear to match its parameters. For a spell to detect  something visually, the spell's origin point must have line of  sight. Darkness doesn't p |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/3` | 0.589593 | Other heightened entries give a number after a plus sign,  indicating that heightening grants extra advantages over  multiple ranks. The listed effect applies for every increment  of ranks by which th |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/30` | 0.588993 | **GLOW UP **[two-actions] **SPELL 1**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **VISUAL**  **Traditions** arcane, occult, primal  **Range **30 feet;** Targets** 1 willing creature  **Duration** 1 |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/20/ListItem/15` | 0.584663 | AC = 15 + your level. Ignore your armor's check penalty  and Speed reduction. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/16/ListItem/1` | 0.582997 | AC = 20 + your level. Ignore your armor's check penalty  and Speed reduction. |

### Query 174
- Text: What is the rule about You let out a powerful ululation full of psychic resonance that  compels others who hear it to join in. You deal 7d12 sonic  damage and 1d8 persistent mental damage to other creatures  who can hear within the area. Targets must attempt a Will  save. The persistent mental damage a creature takes from  this spell increases by 1d8 if at least one other creature is  howling. A howling creature can't use auditory actions or  cast spells except for those with the subtle trait for 1 round.  Calculate the persistent damage after all creatures attempt  their saves.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `34`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/37', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/40', 'PZO22001 Starfinder Player Core 330-363::/page/18/Text/13', 'PZO22001 Starfinder Player Core 330-363::/page/0/Text/20', 'PZO22001 Starfinder Player Core 330-363::/page/29/SectionHeader/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/37` | 1.000042 | You let out a powerful ululation full of psychic resonance that  compels others who hear it to join in. You deal 7d12 sonic  damage and 1d8 persistent mental damage to other creatures  who can hear wi |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/40` | 0.733737 | **Failure** The target takes full damage, persistent mental  damage, and is compelled to howl as long as it takes  persistent mental damage. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/13` | 0.728848 | **NOISE BLAST **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SONIC**  **Traditions** arcane, divine, occult **Range **30 feet;** Area** 10-foot burst  **Defense** Fortitude  A cacophono |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/20` | 0.724105 | **ENTHRALL **[two-actions] **SPELL 3**  **AUDITORY** **CONCENTRATE** **EMOTION** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet;** Targets** all creatures in range  **Defense** Will |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/29/SectionHeader/14` | 0.722161 | **SILENCE **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** divine, occult  **Range **touch;** Targets** 1 willing creature  **Duration** 1 minute  The target makes n |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/50` | 0.675941 | **Heightened (7th)** You can target up to 5 additional creatures  to gain protection against the environment the triggering  creature entered. The spell lasts for 8 hours and also  protects against ex |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/15` | 0.671195 | **DEATH SENTENCE **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **DEATH** **INCAPACITATION** **SPIRIT**  **Traditions** divine, primal  **Range **30 feet;** Targets** 1 creature  **Defense* |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/31/Text/13` | 0.669296 | **SONIC SCREAM **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SONIC**  **Traditions** arcane, occult, primal  **Area** 15-foot cone  **Defense** Fortitude  You unleash a painfully rapid |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6` | 0.668236 | **CHILLING DARKNESS **[two-actions] **SPELL 3**  **ATTACK** **COLD** **CONCENTRATE** **DARKNESS** **MANIPULATE** **UNHOLY**  **Traditions** divine  **Range **120 feet;** Targets** 1 creature  **Defens |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/32/Text/2` | 0.667956 | **SOUND BODY **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You send a su |

### Query 175
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/35']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `30`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/31/Text/59', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/60', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/35', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/64', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/58']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/59` | 0.915652 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/64` | 0.915652 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/60` | 0.915652 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/35` | 0.915652 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/58` | 0.915652 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/67` | 0.873652 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/67` | 0.873652 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/85` | 0.873652 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/73` | 0.873652 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/25` | 0.873652 | **EQUIPMENT** |

### Query 176
- Text: What does **BLINDNESS **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36', 'PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/51', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6', 'PZO22001 Starfinder Player Core 294-329::/page/30/Text/8', 'PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/46']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/36` | 0.683193 | **BLINDNESS **[two-actions] **SPELL 3**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **30 feet;** Targets** 1 creature  **Defense** Fortit |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.622092 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/29/SectionHeader/51` | 0.612182 | **DARKVISION **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Duration** 1 hour  You grant yourself supernatural sight in areas of darkness |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.610742 | **LIFE SEAL **[reaction] **SPELL 3** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/6` | 0.608008 | **CHILLING DARKNESS **[two-actions] **SPELL 3**  **ATTACK** **COLD** **CONCENTRATE** **DARKNESS** **MANIPULATE** **UNHOLY**  **Traditions** divine  **Range **120 feet;** Targets** 1 creature  **Defens |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/8` | 0.606116 | **DEAFNESS **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **30 feet;** Targets** 1 creature  **Defense** Fortitude  The target loses |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/34/SectionHeader/46` | 0.604706 | **ELECTROTETHER **[two-actions] **SPELL 3**  **ATTACK** **CONCENTRATE** **ELECTRICITY** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **30 feet; **Targets** up to two creatures |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` | 0.594753 | **HYPNOTIZE **[two-actions] **SPELL 3**  **ILLUSION** **MANIPULATE** **SUBTLE** **VISUAL**  **Traditions** arcane, occult  **Range **120 feet; **Area** 10-foot burst  **Defense** Will;** Duration** su |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/18` | 0.569649 | **FELINE SENSES **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MORPH**  **Traditions** divine, primal  **Duration** 1 hour |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.568801 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |

### Query 177
- Text: What is the rule about **SPELLCASTING IN STARFINDER**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `34`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/2', 'PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/11` | 0.864402 | **SPELLCASTING IN STARFINDER** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/2` | 0.634243 | CASTING SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/SectionHeader/21` | 0.612569 | SPELLCASTERS WITH FOCUS  SPELLS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/20` | 0.590823 | NON-SPELLCASTERS WITH  FOCUS SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/5` | 0.571279 | SPELL SLOTS |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/3` | 0.515968 | **SPELLSHAPE** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/1` | 0.508799 | Whether it comes in the form of eldritch artifacts, otherworldly beings, or witchwarpers altering  reality with strange spells, magic brings fantasy and wonder to Starfinder. This chapter explains how |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/68` | 0.498277 | **Scrying**U Spy on a creature you choose. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/50` | 0.498277 | **Scrying**U Spy on a creature you choose. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/24` | 0.496889 | **SPELLS** |

### Query 178
- Text: What does **BREATH OF LIFE **[reaction] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/54']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `29`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/54', 'PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/40', 'PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/15', 'PZO22001 Starfinder Player Core 294-329::/page/12/Text/56', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/54` | 0.713561 | **BREATH OF LIFE **[reaction] **SPELL 5**  **CONCENTRATE** **HEALING** **VITALITY**  **Traditions** divine  **Trigger** A living creature within range would die.  **Range **60 feet;** Targets** the tr |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/15/SectionHeader/40` | 0.649628 | OCCULT 5TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.647665 | **LIFE SEAL **[reaction] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/15` | 0.637239 | ARCANE 5TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/56` | 0.633682 | **Breath of Life**H React to revive a character at the moment of  its death. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.615746 | CHAPTER 7: SPELLS |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4` | 0.571603 | **AIR BUBBLE **[reaction] **SPELL 1**  **AIR** **CONCENTRATE**  **Traditions** arcane, divine, primal  **Trigger** A creature within range enters an environment where  it can't breathe.  **Range **60 |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/7` | 0.571482 | PRIMAL 5TH-RANK SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/12/SectionHeader/54` | 0.559675 | DIVINE 5TH-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/50` | 0.556475 | **SUBJECTIVE REALITY **[one-action] **SPELL 5**  **CONCENTRATE** **MANIPULATE**  **Traditions** occult  **Range **500 feet;** Targets** 1 creature or object  **Duration** sustained up to 1 minute  You |

### Query 179
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/59']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/59', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/65', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/43', 'PZO22001 Starfinder Player Core 330-363::/page/11/Text/62', 'PZO22001 Starfinder Player Core 330-363::/page/13/Text/60']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/59` | 0.735680 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/43` | 0.735680 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/65` | 0.735680 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/62` | 0.735680 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/60` | 0.735680 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/59` | 0.693680 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/43` | 0.693680 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/70` | 0.693680 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/66` | 0.693680 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/62` | 0.693680 | **FEATS** |

### Query 180
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/66']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/27/Text/67', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/49', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/67', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/72', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/66']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/67` | 0.938833 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/49` | 0.938833 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/72` | 0.938833 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/67` | 0.938833 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/66` | 0.938833 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/74` | 0.896833 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/67` | 0.896833 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/65` | 0.896833 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/77` | 0.896833 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/49` | 0.896833 | **PLAYING THE ** **GAME** |

### Query 181
- Text: What does **AIR BUBBLE **[reaction] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/11/Text/46', 'PZO22001 Starfinder Player Core 294-329::/page/16/Text/58', 'PZO22001 Starfinder Player Core 294-329::/page/8/Text/28', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4` | 0.777191 | **AIR BUBBLE **[reaction] **SPELL 1**  **AIR** **CONCENTRATE**  **Traditions** arcane, divine, primal  **Trigger** A creature within range enters an environment where  it can't breathe.  **Range **60 |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/46` | 0.675026 | **Air Bubble** React to create air for a creature to breathe. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/58` | 0.675026 | **Air Bubble** React to create air for a creature to breathe. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/28` | 0.675026 | **Air Bubble** React to create air for a creature to breathe. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.623657 | SPELL ATTACKS |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.606675 | **LIFE SEAL **[reaction] **SPELL 3** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/43` | 0.590906 | **PUMMELING RUBBLE **[two-actions] **SPELL 1**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Area** 15-foot cone  **Defense** Reflex  A spray of heavy rocks flies through |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.580138 | CHAPTER 7: SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/57` | 0.572877 | PRIMAL 1ST-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` | 0.570569 | **HYPNOTIZE **[two-actions] **SPELL 3**  **ILLUSION** **MANIPULATE** **SUBTLE** **VISUAL**  **Traditions** arcane, occult  **Range **120 feet; **Area** 10-foot burst  **Defense** Will;** Duration** su |

### Query 182
- Text: What does **FEAR **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `30`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/8', 'PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/29', 'PZO22001 Starfinder Player Core 330-363::/page/13/SectionHeader/48', 'PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/26', 'PZO22001 Starfinder Player Core 330-363::/page/14/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/8` | 0.729285 | **FEAR **[two-actions] **SPELL 1**  **CONCENTRATE** **EMOTION** **FEAR** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult, primal  **Range **30 feet;** Targets** 1 creature **Defense** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/29` | 0.670728 | **STUPEFY **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** varies  You du |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/13/SectionHeader/48` | 0.669687 | **MASK OF TERROR **[two-actions] **SPELL 7**  **CONCENTRATE** **EMOTION** **FEAR** **ILLUSION** **MANIPULATE** **MENTAL** **VISUAL**  **Traditions** arcane, occult, primal  **Range **30 feet; **Target |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/26` | 0.659133 | **PARANOIA **[two-actions] **SPELL 2**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** occult  **Range **30 feet; **Targets** 1 creature **Defense** Will; **Duration** 1 minute |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/4` | 0.655845 | **Failure** The creature becomes frightened 2 before using its  action. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.613911 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/54` | 0.611282 | **CLEAR MIND **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You drive menta |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/25/Text/11` | 0.606786 | **CALM **[two-actions] **SPELL 2**  **CONCENTRATE** **EMOTION** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **120 feet;** Area** 10-foot burst  **Defense** Wil |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.605390 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/39` | 0.600086 | **SUBCONSCIOUS SUGGESTION **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **LINGUISTIC** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet;** Targe |

### Query 183
- Text: What does **FORCE BARRAGE **[one-action]** TO **[three-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `32`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/19', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21', 'PZO22001 Starfinder Player Core 330-363::/page/28/Text/50', 'PZO22001 Starfinder Player Core 330-363::/page/6/Text/26', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/19` | 0.741601 | **FORCE BARRAGE **[one-action]** TO **[three-actions] **SPELL 1**  **CONCENTRATE** **FORCE** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet;** Targets** 1 creature  You fire a shard |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.659468 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/50` | 0.636199 | **SHIFTING SURGE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** one weapon held by you or a  willing ally that deals acid, c |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/26` | 0.627927 | **HARM **[one-action]** TO **[three-actions] **SPELL 1**  **MANIPULATE** **VOID**  **Traditions** divine  **Range **varies; **Targets** 1 living creature or 1 willing undead  creature  You channel voi |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.626805 | **LIFE SEAL **[reaction] **SPELL 3** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.591454 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20` | 0.584771 | **BLAZING BOLT **[one-action]** TO **[three-actions] **SPELL 2**  **ATTACK** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets** 1 or more creatures |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/44` | 0.584698 | **HEAL **[one-action]** TO **[three-actions] **SPELL 1**  **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **varies; **Targets** 1 willing living creature or 1 undead  c |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/35/SectionHeader/32` | 0.574045 | **ENFEEBLE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult  **Range **30 feet;** Targets** 1 creature  **Defense** Fortitude; **Duration** varies  Yo |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/36` | 0.573822 | **HASTE **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Range **30 feet;** Targets** 1 creature  **Duration** 1 minute  Magic empowers the target |

### Query 184
- Text: Summarize Dragon Breath
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/489']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `14`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/489', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/486', 'PZO22001 Starfinder Player Core 330-363::/page/0/Table/3', 'PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 330-363::/page/0/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/489` | 0.830751 | Dragon Breath |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/486` | 0.641997 | Dragon |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/19` | 0.597458 | **Dragon Breath**[two-actions] You exhale deadly magical energy  in an area, dealing 10d6 damage to each creature in  the area with a basic save against your spell DC. The  shape, damage type, and sav |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/0/Table/3` | 0.578736 | DragonTraditionSpeedsDragon BreathAbysiumArcane—Cone of poison (Fortitude)AkashicOccult—Cone of mental (Will)CosmicDivine—Cone of spirit (Will)HostPrimalClimbCone of piercing (Reflex) |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/33/ListItem/14` | 0.569817 | Resistance 10 against the damage type of your Dragon  Breath (see below). |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/1` | 0.520249 | **ALIEN CORE DRAGONS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/2` | 0.492998 | The dragons from *Alien Core* use the following  specifications for *dragon form*. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/21` | 0.478175 | **Heightened (8th)** Your battle form is Huge, you gain a +20 foot status bonus to your fly Speed, and your attacks  have 10-foot reach (or 15-foot reach if they previously  had 10-foot reach). You in |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/63` | 0.475800 | **Summon Dragon**H Conjure a dragon to fight on your behalf. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/55` | 0.475800 | **Summon Dragon**H Conjure a dragon to fight on your behalf. |

### Query 185
- Text: Summarize Divine
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/499']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `12`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/499', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/45', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/34', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/6', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/44']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/499` | 0.800323 | Divine |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/3/SectionHeader/9` | 0.608266 | **Divine** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/45` | 0.583468 | **Traditions** divine, primal |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/34` | 0.568177 | **Traditions** divine, occult, primal |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/6` | 0.544620 | **Traditions** arcane, divine, occult, primal |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/44` | 0.542005 | **CONCENTRATE** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/43` | 0.538146 | **Guidance** Divine guidance improves one roll. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/74` | 0.525307 | insight about a topic. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/10` | 0.520750 | The power of the divine is steeped in faith,  the unseen, and belief in a power source from |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.514533 | **Summoned** |

### Query 186
- Text: What is the rule about **Heightened (6th)** The spell's range is touch and it targets 1 willing  creature. The duration is until your next daily preparations.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `38`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/25', 'PZO22001 Starfinder Player Core 330-363::/page/6/Text/24', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/24', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/50', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/51']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/25` | 0.967645 | **Heightened (6th)** The spell's range is touch and it targets 1 willing  creature. The duration is until your next daily preparations. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/30/Text/1` | 0.855555 | **Heightened (5th)** The spell's range is touch and it targets  1 willing creature. The duration is until your next daily  preparations. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/24` | 0.847041 | **Heightened (6th)** Choose to either target up to 10 creatures  or change the spell's duration to until your next daily  preparations. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/24` | 0.833802 | **Heightened (4th)** The spell's range is touch and it targets 1  willing creature. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/50` | 0.763763 | **Heightened (7th)** You can target up to 5 additional creatures  to gain protection against the environment the triggering  creature entered. The spell lasts for 8 hours and also  protects against ex |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/51` | 0.756574 | **Heightened (10th)** You can target up to 10 additional  creatures to gain protection against the environment the  triggering creature entered. The spell lasts until your next  daily preparations and |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/11` | 0.696156 | **STATUS **[two-actions] **SPELL 2**  **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch;** Targets** 1 willing living creature  **Duration** until yo |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/2` | 0.693661 | **Heightened (4th)** The spell lasts 1 minute, but it doesn't end if  the target uses a hostile action. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/4` | 0.690972 | **HONEYED WORDS **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes  You unlock the |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/34` | 0.690408 | **Heightened (6th)** The spell targets up to four creatures and  deals 6d12 mental damage. |

### Query 187
- Text: What is the rule about You create an illusory image of a Large or smaller creature. It  generates the appropriate sounds, smells, and feels believable  to the touch. If you and the image are ever farther than 500  feet apart, the spell ends.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `34`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/1', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/33', 'PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/19', 'PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/18', 'PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/1` | 0.986495 | You create an illusory image of a Large or smaller creature. It  generates the appropriate sounds, smells, and feels believable  to the touch. If you and the image are ever farther than 500  feet apar |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/33` | 0.759574 | **FIGMENT **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet  **Duration** sustained  You create a simp |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/19` | 0.756121 | **ILLUSORY OBJECT **[two-actions] **SPELL 1**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **VISUAL**  **Traditions** arcane, occult  **Range **500 feet;** Area** 20-foot burst  **Duration** 10 minute |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/18` | 0.753068 | **PROJECT IMAGE **[two-actions] **SPELL 7**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet  **Duration** sustained up to 1 minute  You projec |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/29` | 0.735754 | **ILLUSORY SCENE** **SPELL 5**  **AUDITORY** **CONCENTRATE** **ILLUSION** **MANIPULATE** **OLFACTORY** **VISUAL**  **Traditions** arcane, occult  **Cast** 10 minutes  **Range **500 feet;** Area** 30-f |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/27/SectionHeader/34` | 0.683553 | **SELECTIVE INVISIBILITY **[two-actions] **SPELL 3**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **500 feet; **Targets** 1 willing creature touched and one  within |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/7` | 0.675576 | **ILLUSORY DISGUISE **[two-actions] **SPELL 1**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **VISUAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 willing creature  **Duration** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/9` | 0.664723 | **REPULSION **[two-actions] **SPELL 6**  **AURA** **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult  **Area** emanation up to 40 feet  **Defense** Will; **Duration** 1 m |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/14/SectionHeader/19` | 0.662539 | **MEASURE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE**  **Traditions** arcane, divine, occult, primal  **Area** 200-foot emanation  **Duration** sustained up to 1 minute  You learn the ap |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/52` | 0.657298 | **FALSE VISION** **SPELL 5**  **UNCOMMON** **CONCENTRATE** **ILLUSION** **MANIPULATE**  **Traditions** arcane, occult  **Cast** 10 minutes  **Range **touch;** Area** 100-foot burst  **Duration** until |

### Query 188
- Text: Summarize **Minion**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `31`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8', 'PZO22001 Starfinder Player Core 294-329::/page/14/Text/17', 'PZO22001 Starfinder Player Core 294-329::/page/8/Text/57', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/79']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/5` | 0.858882 | **Minion** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/1` | 0.681031 | **PHANTASMAL MINION STATISTICS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/2` | 0.633182 | **PHANTASMAL MINION** **CREATURE –1** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/5/SectionHeader/8` | 0.623420 | **Summoned** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/14/Text/17` | 0.617114 | **Phantasmal Minion **Create a creature of force to perform  minor tasks. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/57` | 0.617114 | **Phantasmal Minion **Create a creature of force to perform  minor tasks. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/79` | 0.598332 | **GAME** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/44` | 0.564086 | **CONCENTRATE** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.564086 | **CONCENTRATE** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` | 0.558616 | **CONCENTRATE** **MANIPULATE** |

### Query 189
- Text: Summarize The power of the divine is steeped in faith,  the unseen, and belief in a power source from
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `43`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/10', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/22', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/11', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/18', 'PZO22001 Starfinder Player Core 294-329::/page/16/Text/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/10` | 0.987089 | The power of the divine is steeped in faith,  the unseen, and belief in a power source from |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/22` | 0.654988 | **Divine Inspiration** Spiritual energy recovers a creature's  expended spell. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/11` | 0.619134 | beyond the Universe. Mystics connected with the cosmic  forces of healing and shadows are divine spellcasters. |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/18` | 0.615604 | An instinctual connection to and faith in the  world, the cycle of day and night, the turning  of the seasons, and the natural selection of predator and  prey drive the primal tradition. Mystics conne |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/43` | 0.615108 | **Guidance** Divine guidance improves one roll. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/34` | 0.552288 | **Traditions** divine, occult, primal |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/10/Text/53` | 0.546023 | **Truesight** See through illusions and physical transformations. **Vampiric Exsanguination**H Draw blood and life force from |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/32/SectionHeader/18` | 0.544356 | **DIVINE INSPIRATION **[two-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine  **Range **touch;** Targets** 1 willing creature  You infuse a target with spiritual |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/12/Text/57` | 0.541353 | **Divine Immolation**H Call divine fire from the sky. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/499` | 0.539095 | Divine |

### Query 190
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/3/Text/30']
- Expected found: `True`
- Expected rank: `14`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/18', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/28', 'PZO22001 Starfinder Player Core 294-329::/page/35/Text/62', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/55', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/18` | 0.913367 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/55` | 0.913367 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/20` | 0.913367 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/62` | 0.913367 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/28` | 0.913367 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/15/Text/74` | 0.871367 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/62` | 0.871367 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/59` | 0.871367 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/38` | 0.871367 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/54` | 0.871367 | **INTRODUCTION** |

### Query 191
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/1/Text/23']
- Expected found: `True`
- Expected rank: `13`
- Graph boost applied: `True`
- Graph boosted count: `30`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/31/Text/59', 'PZO22001 Starfinder Player Core 294-329::/page/33/Text/60', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/35', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/64', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/58']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/59` | 0.915652 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/64` | 0.915652 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/33/Text/60` | 0.915652 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/35` | 0.915652 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/58` | 0.915652 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/27/Text/67` | 0.873652 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/67` | 0.873652 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/85` | 0.873652 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/73` | 0.873652 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/25` | 0.873652 | **EQUIPMENT** |

### Query 192
- Text: What is the rule about Other heightened entries give a number after a plus sign,  indicating that heightening grants extra advantages over  multiple ranks. The listed effect applies for every increment  of ranks by which the spell is heightened above its lowest  spell rank, and the benefit is cumulative. For example, *slice * *reality* says "**Heightened (+1)** The damage increases by 1d8."  Because *slice reality* deals 7d8 void damage at 6th rank, a  7th-rank *slice reality* would deal 8d8 void damage, an 8thrank spell would deal 9d8 void damage, and so on.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `34`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/2/Text/3', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/2/Text/1', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/26', 'PZO22001 Starfinder Player Core 294-329::/page/32/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/3` | 1.011019 | Other heightened entries give a number after a plus sign,  indicating that heightening grants extra advantages over  multiple ranks. The listed effect applies for every increment  of ranks by which th |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/2` | 0.836461 | In addition, many spells have additional specific benefits  when they are heightened, such as increased damage. These  extra benefits are described at the end of the spell's stat  block. Some heighten |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/2/Text/1` | 0.759375 | so long as they know the spell at that rank (see Heightened  Spontaneous Spells below). When you heighten your spell,  the spell's rank increases to match the higher rank of the  spell slot you've pre |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/26` | 0.722338 | **Heightened** (rank) If the spell has special effects when  heightened (page 295), those effects appear at the end  of the stat block. |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/32/Text/17` | 0.715093 | **Heightened (+1)** The damage increases by 1d6 and persistent  damage increases by 1d6. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/34` | 0.666905 | **Heightened (+1)** The damage increases by 2d6 (or by 2d8 if  the target is a divine spellcaster). |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/22/Text/22` | 0.652761 | **Heightened (+1)** The damage increases by 1d8 and the ice's  Hit Points increase by 5. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/15` | 0.652761 | **Heightened (+1)** The damage increases by 1d8 and the ice's Hit  Points increase by 5. |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/34/Text/37` | 0.643077 | **Heightened (+1)** The damage increases by 1d12. |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/24/Text/12` | 0.639292 | **Heightened (+1)** The damage increases by 1d10. |

### Query 193
- Text: What does **CREATE FOOD** **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/29/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `32`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/29/Text/2', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47', 'PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/25', 'PZO22001 Starfinder Player Core 294-329::/page/11/Text/75']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/2` | 0.661702 | **CREATE FOOD** **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, primal  **Cast** 1 hour  **Range **30 feet  You create enough food to feed six Medium creatures for a  day. |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.614033 | CHAPTER 7: SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/27/SectionHeader/47` | 0.609651 | **CLEANSE CUISINE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** divine, primal  **Range **10 feet;** Area** 1 cubic foot  You transform all food and beverages in the area |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/14/SectionHeader/25` | 0.599706 | OCCULT 2ND-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/11/Text/75` | 0.599216 | **Create Food**H Feed multiple creatures with conjured food. |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/17/Text/24` | 0.557216 | **Create Food**H Feed multiple creatures with conjured food. |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/9` | 0.557216 | **Create Food**H Feed multiple creatures with conjured food. |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.555790 | SPELL ATTACKS |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/12` | 0.550086 | **GREASE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet;** Area** 4 contiguous 5-foot squares or** Targets** 1  object of 1 Bulk or less |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/17/SectionHeader/17` | 0.549660 | PRIMAL 2ND-RANK SPELLS |

### Query 194
- Text: Summarize COSTS AND LOCI
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `31`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/6', 'PZO22001 Starfinder Player Core 294-329::/page/31/Text/67', 'PZO22001 Starfinder Player Core 294-329::/page/23/Text/50', 'PZO22001 Starfinder Player Core 294-329::/page/13/Text/81', 'PZO22001 Starfinder Player Core 294-329::/page/19/Text/66']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/4/SectionHeader/6` | 0.921624 | COSTS AND LOCI |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/67` | 0.521823 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/50` | 0.521823 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/81` | 0.521823 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/66` | 0.521823 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/93` | 0.479823 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/35/Text/76` | 0.479823 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/40` | 0.479823 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/32` | 0.479823 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/43` | 0.479823 | **GLOSSARY & ** **INDEX** |

### Query 195
- Text: What does **GENTLE LANDING **[reaction] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/10', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/42', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21', 'PZO22001 Starfinder Player Core 330-363::/page/5/Text/12', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/10` | 0.691122 | **GENTLE LANDING **[reaction] **SPELL 1**  **AIR** **CONCENTRATE**  **Traditions** arcane, primal  **Trigger** A creature within range is falling. **Range **60 feet;** Targets** 1 falling creature  ** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/8/Text/44` | 0.617263 | **Gentle Landing** React to save a falling creature. |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/16/Text/71` | 0.617263 | **Gentle Landing** React to save a falling creature. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.604011 | **LIFE SEAL **[reaction] **SPELL 3** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.593612 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/12` | 0.592533 | **GREASE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet;** Area** 4 contiguous 5-foot squares or** Targets** 1  object of 1 Bulk or less |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/7` | 0.591473 | **Range **touch;** Targets** 1 creature |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.570142 | CHAPTER 7: SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/57` | 0.553073 | PRIMAL 1ST-RANK SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/33/SectionHeader/36` | 0.547338 | **EARTHBIND **[two-actions] **SPELL 3**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 flying creature  **Defense** Fortitude; **Duration** |

### Query 196
- Text: What does **CONTINGENCY** **SPELL 7** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `27`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/5', 'PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21', 'PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/57', 'PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.734025 | CHAPTER 7: SPELLS |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/16/SectionHeader/5` | 0.683367 | OCCULT 7TH-RANK SPELLS |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/28/SectionHeader/21` | 0.676082 | **CONTINGENCY** **SPELL 7**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane  **Cast** 10 minutes **Duration** until your next daily preparations  You prepare a spell that will trigger later. Wh |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/10/SectionHeader/57` | 0.640781 | ARCANE 7TH-RANK SPELLS |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/18/SectionHeader/34` | 0.631418 | PRIMAL 7TH-RANK SPELLS |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.582469 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/SectionHeader/11` | 0.581568 | DIVINE 7TH-RANK SPELLS |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/7/SectionHeader/3` | 0.568832 | IDENTIFYING SPELLS |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/13` | 0.567111 | SUSTAINING SPELLS |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/28/Text/11` | 0.563082 | **CONFUSION **[two-actions] **SPELL 4**  **CONCENTRATE** **EMOTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature **Defense** Will; **Duration** 1 |

### Query 197
- Text: What does **FLOATING FLAME **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/69']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `30`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/69', 'PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/37', 'PZO22001 Starfinder Player Core 330-363::/page/30/SectionHeader/22', 'PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/51', 'PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/69` | 0.711447 | **FLOATING FLAME **[two-actions] **SPELL 2**  **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Targets** one 5-foot square  **Defense** Reflex; **Duration** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/37` | 0.641635 | **REVEALING LIGHT **[two-actions] **SPELL 2**  **CONCENTRATE** **LIGHT** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **120 feet;** Area** 10-foot burst  **Defense** Reflex; * |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/30/SectionHeader/22` | 0.628545 | **SKYFIRE WINGS **[two-actions] **SPELL 3**  **CONCENTRATE** **ELECTRICITY** **FIRE** **MANIPULATE** **MORPH**  **Traditions** arcane, divine, occult, primal  **Duration** 1 minute  Wings of plasma gr |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/51` | 0.621644 | **PHANTASMAL FLEET **[two-actions] **SPELL 8**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **500 feet; **Area** 60-foot burst  **Defense** Will  A m |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/13` | 0.621239 | **ENTANGLING FLORA **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **PLANT** **WOOD**  **Traditions** arcane, primal  **Range **120 feet; **Area** all squares in a 20-foot burst  **Duratio |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/20` | 0.594022 | **BLAZING BOLT **[one-action]** TO **[three-actions] **SPELL 2**  **ATTACK** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets** 1 or more creatures |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/27` | 0.576146 | **HYPNOTIZE **[two-actions] **SPELL 3**  **ILLUSION** **MANIPULATE** **SUBTLE** **VISUAL**  **Traditions** arcane, occult  **Range **120 feet; **Area** 10-foot burst  **Defense** Will;** Duration** su |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/48` | 0.575186 | **FIREBALL **[two-actions] **SPELL 3**  **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Area** 20-foot burst  **Defense** basic Reflex  A roaring blast of |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/32/SectionHeader/56` | 0.573288 | **SPIRITUAL ARMAMENT **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SANCTIFIED** **SPIRIT**  **Traditions** divine, occult  **Range **120 feet; **Targets** 1 creature  **Defense** AC; * |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/62` | 0.572327 | **FLICKER **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **TELEPORTATION**  **Traditions** arcane, occult  **Duration** 1 minute  You flicker quickly between your current plane and anothe |

### Query 198
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/5/Text/33']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/23/Text/50', 'PZO22001 Starfinder Player Core 294-329::/page/1/Text/32', 'PZO22001 Starfinder Player Core 294-329::/page/5/Text/33', 'PZO22001 Starfinder Player Core 294-329::/page/3/Text/43', 'PZO22001 Starfinder Player Core 294-329::/page/29/Text/72']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/1/Text/32` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/23/Text/50` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/5/Text/33` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/3/Text/43` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/29/Text/72` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/40` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 294-329::/page/13/Text/81` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/19/Text/66` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 294-329::/page/9/Text/93` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 294-329::/page/31/Text/67` | 0.887439 | **GLOSSARY & ** **INDEX** |

### Query 199
- Text: What does **BREATHE FIRE **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `23`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4', 'PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62', 'PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23', 'PZO22001 Starfinder Player Core 294-329::/page/7/Text/19', 'PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 294-329::/page/20/SectionHeader/4` | 0.668109 | **AIR BUBBLE **[reaction] **SPELL 1**  **AIR** **CONCENTRATE**  **Traditions** arcane, divine, primal  **Trigger** A creature within range enters an environment where  it can't breathe.  **Range **60 |
| 2 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/62` | 0.661258 | **BREATHE FIRE **[two-actions] **SPELL 1**  **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Area** 15-foot cone  **Defense** basic Reflex  A gout of flame sprays from your mo |
| 3 | `PZO22001 Starfinder Player Core 294-329::/page/6/SectionHeader/23` | 0.630981 | SPELL ATTACKS |
| 4 | `PZO22001 Starfinder Player Core 294-329::/page/7/Text/19` | 0.630413 | **SPELL NAME **[one-action] **SPELL (RANK)** |
| 5 | `PZO22001 Starfinder Player Core 294-329::/page/1/SectionHeader/0` | 0.629587 | CHAPTER 7: SPELLS |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/30/SectionHeader/22` | 0.611373 | **SKYFIRE WINGS **[two-actions] **SPELL 3**  **CONCENTRATE** **ELECTRICITY** **FIRE** **MANIPULATE** **MORPH**  **Traditions** arcane, divine, occult, primal  **Duration** 1 minute  Wings of plasma gr |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/31/SectionHeader/22` | 0.593391 | **SOOTHE **[two-actions] **SPELL 1**  **CONCENTRATE** **EMOTION** **HEALING** **MANIPULATE** **MENTAL**  **Traditions** occult  **Range **30 feet;** Targets** 1 willing creature  **Duration** 1 minute |
| 8 | `PZO22001 Starfinder Player Core 294-329::/page/24/SectionHeader/54` | 0.591512 | **BREATH OF LIFE **[reaction] **SPELL 5**  **CONCENTRATE** **HEALING** **VITALITY**  **Traditions** divine  **Trigger** A living creature within range would die.  **Range **60 feet;** Targets** the tr |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/37` | 0.587282 | **IGNITION **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Targets** 1 creature  **Defense** AC  You |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.586810 | **LIFE SEAL **[reaction] **SPELL 3** |
