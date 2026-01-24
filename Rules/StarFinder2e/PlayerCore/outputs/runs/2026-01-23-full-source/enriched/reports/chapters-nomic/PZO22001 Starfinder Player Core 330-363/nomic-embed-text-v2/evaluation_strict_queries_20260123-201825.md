# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `604`
- Query count: `151`
- Evaluated queries: `151`
- Coverage: `1.0000`
- MRR: `0.8122`
- hit@1: `0.7417`
- hit@3: `0.8411`
- hit@5: `0.9073`
- hit@10: `0.9603`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

## Timings (ms)
- Embedding (chunks): `22560`
- Embedding (queries): `3235`
- Evaluation (strict): `97`
- Evaluation (expanded): `0`
- Total: `30307`

### Timing Estimates (ms)
- Evaluation (strict): `105`
- Evaluation (expanded): `None`
- Total: `25900`

## Query Details
### Query 0
- Text: Summarize **ALIEN CORE DRAGONS**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 330-363::/page/0/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/486']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/1` | 1.001281 | **ALIEN CORE DRAGONS** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/2` | 0.692995 | The dragons from *Alien Core* use the following  specifications for *dragon form*. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/486` | 0.495896 | Dragon |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/0/Table/3` | 0.355009 | DragonTraditionSpeedsDragon BreathAbysiumArcane—Cone of poison (Fortitude)AkashicOccult—Cone of mental (Will)CosmicDivine—Cone of spirit (Will)HostPrimalClimbCone of piercing (Reflex) |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/0` | 0.319545 | 7 PLAYER CORE |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/0` | 0.319545 | 7 PLAYER CORE |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/0` | 0.319545 | 7 PLAYER CORE |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/15/SectionHeader/0` | 0.319545 | 7 PLAYER CORE |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/58` | 0.303790 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/41` | 0.303790 | **CLASSES** |

### Query 1
- Text: Summarize The dragons from *Alien Core* use the following  specifications for *dragon form*.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 330-363::/page/0/Table/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/2` | 1.037013 | The dragons from *Alien Core* use the following  specifications for *dragon form*. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/1` | 0.657941 | **ALIEN CORE DRAGONS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/0/Table/3` | 0.493584 | DragonTraditionSpeedsDragon BreathAbysiumArcane—Cone of poison (Fortitude)AkashicOccult—Cone of mental (Will)CosmicDivine—Cone of spirit (Will)HostPrimalClimbCone of piercing (Reflex) |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/486` | 0.454245 | Dragon |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/22` | 0.418874 | You gain specific abilities based on the form you choose: |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/1` | 0.405925 | traits while in this form, as well as any trait related to  the creature's kind (such as goblin or human). If this  transformation reduces your size, it reduces your reach  accordingly (typically to 5 |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/50` | 0.400093 | **HUMANOID FORM **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, occult, primal  **Duration** 10 minutes  You transform your appearance to that of a Sm |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/32/SectionHeader/17` | 0.376476 | **SPEAK WITH COMPUTERS **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine  **Duration** 1 hour  You can ask questions of and receive answers from the  spirits i |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/20/Text/9` | 0.373926 | **Force Body** A phantasmal minion's body is made of  magical force. It can't use attack actions. Though it  has no physical weight, it can move and use Interact  actions to do things such as fetch ob |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/18/SectionHeader/45` | 0.373055 | **OUTCAST'S CURSE **[two-actions] **SPELL 4**  **CONCENTRATE** **CURSE** **MANIPULATE** **MENTAL** **MISFORTUNE**  **Traditions** arcane, divine, occult **Range **touch;** Targets** 1 creature  **Defe |

### Query 2
- Text: Lookup values for DragonTraditionSpeedsDragon BreathAbysiumArcane—Cone of poison
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/Table/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/Table/3', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/493', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/Table/3` | 0.824501 | DragonTraditionSpeedsDragon BreathAbysiumArcane—Cone of poison (Fortitude)AkashicOccult—Cone of mental (Will)CosmicDivine—Cone of spirit (Will)HostPrimalClimbCone of piercing (Reflex) |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/493` | 0.561033 | Cone of poison (Fortitude) |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/6` | 0.485247 | **Traditions** arcane, divine, occult, primal |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/2` | 0.431987 | The dragons from *Alien Core* use the following  specifications for *dragon form*. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/491` | 0.430578 | Arcane |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/31/Text/13` | 0.430461 | **SONIC SCREAM **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SONIC**  **Traditions** arcane, occult, primal  **Area** 15-foot cone  **Defense** Fortitude  You unleash a painfully rapid |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/489` | 0.411430 | Dragon Breath |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/26` | 0.406509 | **PROMESSION **[two-actions] **SPELL 6**  **ATTACK** **COLD** **CONCENTRATE** **DEATH** **MANIPULATE** **SONIC**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 creature or unattende |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/24` | 0.405021 | **OAKEN RESILIENCE **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **PLANT** **WOOD**  **Traditions** arcane, primal  **Range **touch; **Targets** 1 willing creature  **Duration** 10 minut |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/11/ListItem/29` | 0.404182 | **Spider** Speed 25 feet, climb 25 feet; darkvision; **Melee **[one-action] fangs, **Damage **1d6 piercing plus 1d4 persistent poison;  **Ranged **[one-action] web (range increment 20 feet), **Damage |

### Query 3
- Text: Summarize Dragon
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/486']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/486', 'PZO22001 Starfinder Player Core 330-363::/page/0/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/489']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/486` | 0.832036 | Dragon |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/2` | 0.565034 | The dragons from *Alien Core* use the following  specifications for *dragon form*. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/489` | 0.544531 | Dragon Breath |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/1` | 0.488120 | **ALIEN CORE DRAGONS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/0/Table/3` | 0.437298 | DragonTraditionSpeedsDragon BreathAbysiumArcane—Cone of poison (Fortitude)AkashicOccult—Cone of mental (Will)CosmicDivine—Cone of spirit (Will)HostPrimalClimbCone of piercing (Reflex) |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/19` | 0.328336 | **STUMBLE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **100 feet; **Targets** 1 creature  **Defense** Reflex  A burst of micrograv |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/31/Text/3` | 0.324486 | **SLOW **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 creature **Defense** Fortitude; **Duration** varies  You dila |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/15` | 0.323167 | **PARALYZE **[two-actions] **SPELL 3**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature  **Defense** Will; **Durat |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/20` | 0.322821 | **ENTHRALL **[two-actions] **SPELL 3**  **AUDITORY** **CONCENTRATE** **EMOTION** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet;** Targets** all creatures in range  **Defense** Will |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/50` | 0.319679 | **HUMANOID FORM **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, occult, primal  **Duration** 10 minutes  You transform your appearance to that of a Sm |

### Query 4
- Text: Summarize Tradition
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/487']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/487', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/45', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/487` | 0.823824 | Tradition |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/45` | 0.527257 | **Traditions** divine, primal |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/6` | 0.487731 | **Traditions** arcane, divine, occult, primal |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/34` | 0.444731 | **Traditions** divine, occult, primal |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/24` | 0.429129 | **Traditions** occult |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/48` | 0.319846 | **Rituals** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/71` | 0.319846 | **Rituals** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/66` | 0.319846 | **Rituals** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/66` | 0.319846 | **Rituals** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/68` | 0.319846 | **Rituals** |

### Query 5
- Text: Summarize Speeds
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/488']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/488', 'PZO22001 Starfinder Player Core 330-363::/page/20/ListItem/16', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/56']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/488` | 0.837856 | Speeds |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/20/ListItem/16` | 0.495459 | Speed 20 feet. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/56` | 0.481867 | **FLEET STEP **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Duration** 1 minute  You gain a +30-foot status bonus to your Speed. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/20/Text/12` | 0.388108 | **Speed **fly 30 feet |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/16/ListItem/7` | 0.365638 | **Nyssholora** Speed 40 feet; **Melee **[one-action] jaws (reach 10  feet), **Damage** 2d12+20 piercing; **Melee **[one-action] phasic blade  (razing, reach 15 feet), **Damage **2d10+13 sonic plus  ph |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/11/ListItem/24` | 0.363839 | **Beetle** Speed 25 feet; **Melee **[one-action] mandibles, **Damage ** 2d10 bludgeoning. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/31/Text/3` | 0.361309 | **SLOW **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 creature **Defense** Fortitude; **Duration** varies  You dila |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/22/ListItem/28` | 0.343649 | **Void Palm** Speed 15 feet; resistance 10 to poison; **Melee ** [one-action][one-actio void frond (reach 10 feet), **Damage **2d8 slashing |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/20/Text/14` | 0.341143 | You gain the following statistics and abilities: |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/9` | 0.339028 | The target can soar through the air, gaining a fly Speed equal  to its Speed or 20 feet, whichever is greater. |

### Query 6
- Text: Summarize Dragon Breath
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/489']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/489', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/486', 'PZO22001 Starfinder Player Core 330-363::/page/0/Table/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/489` | 0.940612 | Dragon Breath |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/486` | 0.605213 | Dragon |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/0/Table/3` | 0.451494 | DragonTraditionSpeedsDragon BreathAbysiumArcane—Cone of poison (Fortitude)AkashicOccult—Cone of mental (Will)CosmicDivine—Cone of spirit (Will)HostPrimalClimbCone of piercing (Reflex) |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/2` | 0.375085 | The dragons from *Alien Core* use the following  specifications for *dragon form*. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/1` | 0.335082 | **ALIEN CORE DRAGONS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/27/SectionHeader/48` | 0.325362 | **SHADOW BLAST **[two-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SHADOW**  **Traditions** divine, occult  **Range **varies;** Area** varies  **Defense** basic Reflex or Will (target's choi |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/37` | 0.321057 | **PEACEFUL BUBBLE** **SPELL 4**  **UNCOMMON** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Cast** 10 minutes  **Range **touch; **Area** 100-foot burst  **Duration** 24 hours  An op |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/16/ListItem/8` | 0.312551 | **Space Worm **Speed 40 feet, burrow 40 feet, swim 40  feet; **Melee **[one-action] jaws (reach 15 feet), **Damage** 2d12+20  piercing; **Melee **[one-action] tongue (finesse, reach 30 feet), **Effect |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/13` | 0.310335 | **NOISE BLAST **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **SONIC**  **Traditions** arcane, divine, occult **Range **30 feet;** Area** 10-foot burst  **Defense** Fortitude  A cacophono |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/32/SectionHeader/39` | 0.309647 | **SPIRIT BLAST **[two-actions] **SPELL 6**  **CONCENTRATE** **MANIPULATE** **SPIRIT**  **Traditions** divine, occult  **Range **30 feet; **Targets** 1 creature  **Defense** basic Fortitude  You concen |

### Query 7
- Text: Summarize Abysium
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/490']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/490', 'PZO22001 Starfinder Player Core 330-363::/page/0/Table/3', 'PZO22001 Starfinder Player Core 330-363::/page/27/SectionHeader/28']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/490` | 0.937533 | Abysium |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/Table/3` | 0.356389 | DragonTraditionSpeedsDragon BreathAbysiumArcane—Cone of poison (Fortitude)AkashicOccult—Cone of mental (Will)CosmicDivine—Cone of spirit (Will)HostPrimalClimbCone of piercing (Reflex) |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/27/SectionHeader/28` | 0.354346 | **SEEK THE STARS **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** divine, occult, primal  In your mind's eye, you chart a path through the cosmos. If  you're i |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/19` | 0.292667 | **STUMBLE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **100 feet; **Targets** 1 creature  **Defense** Reflex  A burst of micrograv |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/26` | 0.292546 | **PARANOIA **[two-actions] **SPELL 2**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** occult  **Range **30 feet; **Targets** 1 creature **Defense** Will; **Duration** 1 minute |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/32` | 0.292395 | **PHANTASMAGORIA **[two-actions] **SPELL 9**  **CONCENTRATE** **DEATH** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **120 feet; **Targets** any number of creatures |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/43` | 0.291197 | **PHANTASMAL CALAMITY **[two-actions] **SPELL 6**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **500 feet; **Area** 30-foot burst  **Defense** Will |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/56` | 0.282096 | **ILLUSORY CREATURE**[two-actions] **SPELL 2**  **AUDITORY** **CONCENTRATE** **ILLUSION** **MANIPULATE** **OLFACTORY** **VISUAL**  **Traditions** arcane, occult  **Range **500 feet  **Duration** susta |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/1` | 0.276220 | Illusions bend light around the target, rendering it  invisible. This makes it undetected to all creatures, though  the creatures can attempt to find the target, making it  hidden to them instead (pag |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/31/Text/3` | 0.273515 | **SLOW **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 creature **Defense** Fortitude; **Duration** varies  You dila |

### Query 8
- Text: Summarize Arcane
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/491']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/491', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/6', 'PZO22001 Starfinder Player Core 330-363::/page/0/Table/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/491` | 0.873418 | Arcane |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/6` | 0.522625 | **Traditions** arcane, divine, occult, primal |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/0/Table/3` | 0.502553 | DragonTraditionSpeedsDragon BreathAbysiumArcane—Cone of poison (Fortitude)AkashicOccult—Cone of mental (Will)CosmicDivine—Cone of spirit (Will)HostPrimalClimbCone of piercing (Reflex) |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/24` | 0.414600 | **OAKEN RESILIENCE **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **PLANT** **WOOD**  **Traditions** arcane, primal  **Range **touch; **Targets** 1 willing creature  **Duration** 10 minut |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/26/Text/12` | 0.408391 | **RICOCHET **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE** **METAL**  **Traditions** arcane, divine  **Range **30 feet; **Targets** 1 or 2 creatures  **Defense** basic Reflex |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/15/SectionHeader/34` | 0.405833 | **MIST **[three-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **WATER**  **Traditions** arcane, primal  **Range **120 feet;** Area** 20-foot burst  **Duration** 1 minute  You call forth a cloud |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/60` | 0.403999 | **PEST FORM **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Duration** 10 minutes |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/26` | 0.398564 | **PROMESSION **[two-actions] **SPELL 6**  **ATTACK** **COLD** **CONCENTRATE** **DEATH** **MANIPULATE** **SONIC**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 creature or unattende |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.396827 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/36` | 0.390428 | **HASTE **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Range **30 feet;** Targets** 1 creature  **Duration** 1 minute  Magic empowers the target |

### Query 9
- Text: Summarize —
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/492']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/496', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/500', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/492']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/496` | 0.572766 | — |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/500` | 0.572766 | — |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/492` | 0.572766 | — |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/15` | 0.340791 | **PARALYZE **[two-actions] **SPELL 3**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature  **Defense** Will; **Durat |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/19` | 0.337940 | **STUMBLE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **100 feet; **Targets** 1 creature  **Defense** Reflex  A burst of micrograv |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/56` | 0.324488 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/39` | 0.324488 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/66` | 0.324488 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/55` | 0.324488 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/39` | 0.324488 | **INTRODUCTION** |

### Query 10
- Text: Summarize Cone of poison
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/493']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/493', 'PZO22001 Starfinder Player Core 330-363::/page/0/Table/3', 'PZO22001 Starfinder Player Core 330-363::/page/22/ListItem/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/493` | 0.742463 | Cone of poison (Fortitude) |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/Table/3` | 0.532994 | DragonTraditionSpeedsDragon BreathAbysiumArcane—Cone of poison (Fortitude)AkashicOccult—Cone of mental (Will)CosmicDivine—Cone of spirit (Will)HostPrimalClimbCone of piercing (Reflex) |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/22/ListItem/23` | 0.512169 | Resistance 10 to poison. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/501` | 0.460050 | Cone of spirit (Will) |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/497` | 0.438873 | Cone of mental (Will) |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/505` | 0.423823 | Cone of piercing (Reflex) |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/31/Text/13` | 0.415392 | **SONIC SCREAM **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SONIC**  **Traditions** arcane, occult, primal  **Area** 15-foot cone  **Defense** Fortitude  You unleash a painfully rapid |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/20` | 0.400466 | **EXPLOSION OF ROT **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **POISON**  **Traditions** divine, primal  **Range **120 feet;** Area** 20-foot burst  **Defense** Reflex  A giant pustul |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/11/ListItem/28` | 0.398994 | piercing plus 1d4 persistent poison; **Melee **[one-action] pincer  (agile), **Damage **1d6 bludgeoning. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/11/ListItem/25` | 0.392727 | **Centipede** Speed 25 feet, climb 25 feet; darkvision;  **Melee **[one-action] mandibles, **Damage **1d8 piercing plus 1d4  persistent poison. |

### Query 11
- Text: Summarize Akashic
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/494']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/494', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/498', 'PZO22001 Starfinder Player Core 330-363::/page/0/Table/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/494` | 0.919846 | Akashic |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/498` | 0.445817 | Cosmic |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/0/Table/3` | 0.435855 | DragonTraditionSpeedsDragon BreathAbysiumArcane—Cone of poison (Fortitude)AkashicOccult—Cone of mental (Will)CosmicDivine—Cone of spirit (Will)HostPrimalClimbCone of piercing (Reflex) |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/16/SectionHeader/28` | 0.315961 | **MYSTIC ARMOR **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Duration** until your next daily preparations  You ward yourself with shimm |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/20` | 0.310219 | **ENTHRALL **[two-actions] **SPELL 3**  **AUDITORY** **CONCENTRATE** **EMOTION** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet;** Targets** all creatures in range  **Defense** Will |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/43` | 0.305246 | **PHANTASMAL CALAMITY **[two-actions] **SPELL 6**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **500 feet; **Area** 30-foot burst  **Defense** Will |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/15` | 0.301986 | **PARALYZE **[two-actions] **SPELL 3**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature  **Defense** Will; **Durat |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/3` | 0.301118 | **INJURY ECHO **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **60 feet; **Targets** 1 creature  **Defense** Will  You manifest an inj |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/14/SectionHeader/7` | 0.296305 | **MASSACRE **[two-actions] **SPELL 9**  **CONCENTRATE** **DEATH** **MANIPULATE** **VOID**  **Traditions** arcane, divine, primal  **Area** 60-foot line  **Defense** Fortitude  You unleash a wave of de |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/26` | 0.295687 | **PROMESSION **[two-actions] **SPELL 6**  **ATTACK** **COLD** **CONCENTRATE** **DEATH** **MANIPULATE** **SONIC**  **Traditions** arcane, primal  **Range **120 feet;** Targets** 1 creature or unattende |

### Query 12
- Text: Summarize Occult
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/495']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/495', 'PZO22001 Starfinder Player Core 330-363::/page/8/Text/24', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/495` | 0.874859 | Occult |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/24` | 0.632573 | **Traditions** occult |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/34` | 0.548039 | **Traditions** divine, occult, primal |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/6` | 0.491105 | **Traditions** arcane, divine, occult, primal |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/18/SectionHeader/45` | 0.449402 | **OUTCAST'S CURSE **[two-actions] **SPELL 4**  **CONCENTRATE** **CURSE** **MANIPULATE** **MENTAL** **MISFORTUNE**  **Traditions** arcane, divine, occult **Range **touch;** Targets** 1 creature  **Defe |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/33` | 0.405063 | **FIGMENT **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet  **Duration** sustained  You create a simp |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/12` | 0.401581 | **HALLUCINATION **[two-actions] **SPELL 5**  **ILLUSION** **INCAPACITATION** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** 1 creature  **Duration* |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/24/Text/20` | 0.400519 | **READ OMENS** **SPELL 4**  **UNCOMMON** **CONCENTRATE** **MANIPULATE** **PREDICTION**  **Traditions** divine, occult  **Cast** 10 minutes  You peek into the future. Choose a particular goal or activi |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/0/Table/3` | 0.395494 | DragonTraditionSpeedsDragon BreathAbysiumArcane—Cone of poison (Fortitude)AkashicOccult—Cone of mental (Will)CosmicDivine—Cone of spirit (Will)HostPrimalClimbCone of piercing (Reflex) |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/50` | 0.394376 | **SUBJECTIVE REALITY **[one-action] **SPELL 5**  **CONCENTRATE** **MANIPULATE**  **Traditions** occult  **Range **500 feet;** Targets** 1 creature or object  **Duration** sustained up to 1 minute  You |

### Query 13
- Text: Summarize —
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/496']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/492', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/496', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/500']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/492` | 0.572766 | — |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/496` | 0.572766 | — |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/500` | 0.572766 | — |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/15` | 0.340791 | **PARALYZE **[two-actions] **SPELL 3**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature  **Defense** Will; **Durat |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/19` | 0.337940 | **STUMBLE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **100 feet; **Targets** 1 creature  **Defense** Reflex  A burst of micrograv |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/39` | 0.324488 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/66` | 0.324488 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/28` | 0.324488 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/39` | 0.324488 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/55` | 0.324488 | **INTRODUCTION** |

### Query 14
- Text: Summarize Cone of mental
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/497']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/497', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/501', 'PZO22001 Starfinder Player Core 330-363::/page/0/Table/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/497` | 0.783299 | Cone of mental (Will) |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/501` | 0.575132 | Cone of spirit (Will) |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/0/Table/3` | 0.517939 | DragonTraditionSpeedsDragon BreathAbysiumArcane—Cone of poison (Fortitude)AkashicOccult—Cone of mental (Will)CosmicDivine—Cone of spirit (Will)HostPrimalClimbCone of piercing (Reflex) |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/15/SectionHeader/13` | 0.461730 | **MIND SKEWER **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **60 feet;** Targets** 1 creature  **Defense** basic Will  You overload a c |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/505` | 0.427851 | Cone of piercing (Reflex) |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/493` | 0.415117 | Cone of poison (Fortitude) |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/15/SectionHeader/3` | 0.402759 | **MIND READING **[two-actions] **SPELL 3**  **UNCOMMON** **CONCENTRATE** **DETECTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature  **Defense** W |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/14/SectionHeader/49` | 0.397883 | **MIND PROBE** **SPELL 5**  **UNCOMMON** **CONCENTRATE** **LINGUISTIC** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Cast** 1 minute  **Range **30 feet; **Targets** 1 creature  **Defens |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/27/SectionHeader/42` | 0.397466 | **SENDING **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult  **Range **planetary;** Targets** 1 creature you know well  You send the creat |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/15/SectionHeader/21` | 0.390653 | **MINDLINK **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **touch; **Targets** 1 willing creature  You link your mind to the target's mi |

### Query 15
- Text: Summarize Cosmic
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/498']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/498', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/494', 'PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/498` | 0.866002 | Cosmic |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/494` | 0.436392 | Akashic |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/19` | 0.413785 | **STUMBLE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **100 feet; **Targets** 1 creature  **Defense** Reflex  A burst of micrograv |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/0/Table/3` | 0.361060 | DragonTraditionSpeedsDragon BreathAbysiumArcane—Cone of poison (Fortitude)AkashicOccult—Cone of mental (Will)CosmicDivine—Cone of spirit (Will)HostPrimalClimbCone of piercing (Reflex) |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/51` | 0.345255 | **PHANTASMAL FLEET **[two-actions] **SPELL 8**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **500 feet; **Area** 60-foot burst  **Defense** Will  A m |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/20/SectionHeader/43` | 0.342520 | **PHANTASMAL CALAMITY **[two-actions] **SPELL 6**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **500 feet; **Area** 30-foot burst  **Defense** Will |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/30/Text/1` | 0.341320 | **SINGULARITY SEED **[three-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE** **VOID**  **Traditions** divine, primal  **Range **100 feet; **Area** one 5-foot square and one 50-foot  emanation surr |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/30/Text/15` | 0.335604 | **SKIM DATA **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **touch; **Targets** one dataset contained within a  touched object  You touch one objec |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/30/SectionHeader/43` | 0.332228 | **SLICE REALITY **[three-actions] **SPELL 6**  **CONCENTRATE** **MANIPULATE** **VOID**  **Traditions** arcane, divine, occult  **Range **120 feet  **Defense** basic Reflex;** Duration** 1 minute  You |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/46` | 0.327874 | **GRAVITY FIELD **[three-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **100 feet; **Area** 30-foot radius, 100-foot-tall cylinder  **Dur |

### Query 16
- Text: Summarize Divine
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/499']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/499', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/34', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/45']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/499` | 0.842666 | Divine |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/34` | 0.460633 | **Traditions** divine, occult, primal |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/45` | 0.458791 | **Traditions** divine, primal |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/6` | 0.388039 | **Traditions** arcane, divine, occult, primal |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/0/Table/3` | 0.359174 | DragonTraditionSpeedsDragon BreathAbysiumArcane—Cone of poison (Fortitude)AkashicOccult—Cone of mental (Will)CosmicDivine—Cone of spirit (Will)HostPrimalClimbCone of piercing (Reflex) |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/5` | 0.344891 | **STABILIZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet; **Targets** 1 dying creature  Life ene |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/31/SectionHeader/30` | 0.332789 | **SOUL SURGE **[two-actions] **SPELL 2**  **ATTACK** **CONCENTRATE** **MANIPULATE** **SANCTIFIED** **SPIRIT**  **Traditions** divine, primal  **Range **60 feet; **Targets** 1 creature  **Defense** AC |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/18/SectionHeader/45` | 0.330069 | **OUTCAST'S CURSE **[two-actions] **SPELL 4**  **CONCENTRATE** **CURSE** **MANIPULATE** **MENTAL** **MISFORTUNE**  **Traditions** arcane, divine, occult **Range **touch;** Targets** 1 creature  **Defe |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/5/SectionHeader/20` | 0.327150 | **GUIDANCE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE**  **Traditions** divine, occult, primal  **Range **30 feet; **Targets** 1 creature  **Duration** until the start of your next turn |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/15` | 0.326932 | **PARALYZE **[two-actions] **SPELL 3**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature  **Defense** Will; **Durat |

### Query 17
- Text: Summarize —
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/500']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/492', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/496', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/500']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/492` | 0.572766 | — |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/496` | 0.572766 | — |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/500` | 0.572766 | — |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/15` | 0.340791 | **PARALYZE **[two-actions] **SPELL 3**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature  **Defense** Will; **Durat |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/19` | 0.337940 | **STUMBLE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **100 feet; **Targets** 1 creature  **Defense** Reflex  A burst of micrograv |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/39` | 0.324488 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/66` | 0.324488 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/28` | 0.324488 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/39` | 0.324488 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/55` | 0.324488 | **INTRODUCTION** |

### Query 18
- Text: Summarize Cone of spirit (Will)
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/501']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/501', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/497', 'PZO22001 Starfinder Player Core 330-363::/page/0/Table/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/501` | 0.990730 | Cone of spirit (Will) |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/497` | 0.841072 | Cone of mental (Will) |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/0/Table/3` | 0.624560 | DragonTraditionSpeedsDragon BreathAbysiumArcane—Cone of poison (Fortitude)AkashicOccult—Cone of mental (Will)CosmicDivine—Cone of spirit (Will)HostPrimalClimbCone of piercing (Reflex) |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/493` | 0.498980 | Cone of poison (Fortitude) |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/36` | 0.436231 | **Defense** Will |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/47` | 0.428124 | **ILL OMEN **[two-actions] **SPELL 1**  **CONCENTRATE** **CURSE** **MANIPULATE** **MISFORTUNE**  **Traditions** occult  **Range **30 feet; **Targets** 1 creature **Defense** Will;** Duration** 1 round |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/505` | 0.421829 | Cone of piercing (Reflex) |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/39` | 0.420453 | **SUBCONSCIOUS SUGGESTION **[two-actions] **SPELL 5**  **CONCENTRATE** **INCAPACITATION** **LINGUISTIC** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet;** Targe |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/31/Text/13` | 0.417545 | **SONIC SCREAM **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **SONIC**  **Traditions** arcane, occult, primal  **Area** 15-foot cone  **Defense** Fortitude  You unleash a painfully rapid |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/14/SectionHeader/49` | 0.410384 | **MIND PROBE** **SPELL 5**  **UNCOMMON** **CONCENTRATE** **LINGUISTIC** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Cast** 1 minute  **Range **30 feet; **Targets** 1 creature  **Defens |

### Query 19
- Text: Summarize Host
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/502']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/502', 'PZO22001 Starfinder Player Core 330-363::/page/19/Text/80', 'PZO22001 Starfinder Player Core 330-363::/page/6/Text/36']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/502` | 0.801136 | Host |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/80` | 0.380637 | **CHARACTER ** **SHEET** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/36` | 0.343460 | **HASTE **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Range **30 feet;** Targets** 1 creature  **Duration** 1 minute  Magic empowers the target |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/16/ListItem/2` | 0.296131 | 20 temporary Hit Points. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/20/Text/11` | 0.290131 | **HP **4; **Immunities **disease, mental, non-magical attacks,  paralysis, poison, precision, spirit, unconscious;  **Resistances **all damage 5 (except force or *ghost * *touch*) |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/19` | 0.285803 | **STUMBLE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **100 feet; **Targets** 1 creature  **Defense** Reflex  A burst of micrograv |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/18/SectionHeader/55` | 0.283446 | **OVERHEAT **[two-actions] **SPELL 1**  **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets **1 creature  **Defense** basic Reflex  You vent heat towar |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/24/Text/3` | 0.272185 | **RAISE DEAD** **SPELL 6**  **UNCOMMON** **CONCENTRATE** **HEALING** **MANIPULATE**  **Traditions** divine  **Cast** 10 minutes; **Cost** gemstones worth a total value of the  target's level (minimum |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/2` | 0.268409 | **Heightened (4th)** The spell lasts 1 minute, but it doesn't end if  the target uses a hostile action. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/26/Text/1` | 0.267852 | temporarily rouses those recently slain. All living targets  regain 10d8+40 Hit Points. You return any number of  dead targets to life temporarily, with the same effects and  limitations as *raise dea |

### Query 20
- Text: Summarize Primal
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/503']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/503', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/45', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/503` | 0.909768 | Primal |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/45` | 0.540615 | **Traditions** divine, primal |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/34` | 0.473279 | **Traditions** divine, occult, primal |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/60` | 0.391022 | **PEST FORM **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Duration** 10 minutes |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/6` | 0.387679 | **Traditions** arcane, divine, occult, primal |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/18` | 0.331205 | **FELINE SENSES **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MORPH**  **Traditions** divine, primal  **Duration** 1 hour |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/49` | 0.330632 | **EVENT HORIZON **[two-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE** **VOID**  **Traditions** primal  **Range **500 feet;** Area** 50-foot burst **Defense** Reflex; **Duration** 1 minute |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/16/SectionHeader/37` | 0.317097 | **NATURE INCARNATE **[two-actions] **SPELL 10**  **UNCOMMON** **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** primal  **Duration** 1 minute  The primal power of the world flows through yo |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/32/Text/11` | 0.294483 | **SPEAK WITH ANIMALS **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** primal  **Duration** 1 hour  You can ask questions of, receive answers from, and use the  Diplomacy ski |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47` | 0.283328 | **REVIVAL **[two-actions] **SPELL 10**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet;** Targets** dead creatures and living creatures of  y |

### Query 21
- Text: Summarize Climb
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/504']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/504', 'PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/19', 'PZO22001 Starfinder Player Core 330-363::/page/23/ListItem/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/504` | 0.888617 | Climb |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/19` | 0.489001 | **STUMBLE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **100 feet; **Targets** 1 creature  **Defense** Reflex  A burst of micrograv |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/23/ListItem/14` | 0.450587 | **Lift** Slowly lift an unattended object of light Bulk or  less 1 foot off the ground. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/11/ListItem/23` | 0.369897 | **Ant** Speed 30 feet, climb 30 feet; **Melee **[one-action] mandibles,  **Damage **2d6 bludgeoning. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/12` | 0.362808 | **JUMP **[one-action] **SPELL 1**  **MANIPULATE** **MOVE**  **Traditions** arcane, primal  Your legs surge with strength, ready to leap high and far. You  jump 30 feet in any direction without touchin |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/46` | 0.350869 | **GRAVITY FIELD **[three-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **100 feet; **Area** 30-foot radius, 100-foot-tall cylinder  **Dur |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/36` | 0.349407 | **LEVITATE **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 unattended object or willing creature **Duration** 5 minutes  You |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/26/Text/12` | 0.334856 | **RICOCHET **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE** **METAL**  **Traditions** arcane, divine  **Range **30 feet; **Targets** 1 or 2 creatures  **Defense** basic Reflex |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/20/ListItem/19` | 0.326601 | Acrobatics and Stealth modifiers of +10, unless your  own is higher; Athletics modifier –4. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/14/SectionHeader/19` | 0.325054 | **MEASURE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE**  **Traditions** arcane, divine, occult, primal  **Area** 200-foot emanation  **Duration** sustained up to 1 minute  You learn the ap |

### Query 22
- Text: Summarize Cone of piercing
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/505']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/505', 'PZO22001 Starfinder Player Core 330-363::/page/0/Table/3', 'PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/501']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/505` | 0.790881 | Cone of piercing (Reflex) |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/Table/3` | 0.458223 | DragonTraditionSpeedsDragon BreathAbysiumArcane—Cone of poison (Fortitude)AkashicOccult—Cone of mental (Will)CosmicDivine—Cone of spirit (Will)HostPrimalClimbCone of piercing (Reflex) |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/501` | 0.453257 | Cone of spirit (Will) |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/11/ListItem/26` | 0.401934 | **Mantis** Speed 40 feet; imprecise scent 30 feet; **Melee **[one-action] foreleg, **Damage **2d8 piercing. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/11/ListItem/28` | 0.398715 | piercing plus 1d4 persistent poison; **Melee **[one-action] pincer  (agile), **Damage **1d6 bludgeoning. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/493` | 0.384055 | Cone of poison (Fortitude) |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/0/TableCell/497` | 0.383572 | Cone of mental (Will) |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/11/ListItem/25` | 0.355043 | **Centipede** Speed 25 feet, climb 25 feet; darkvision;  **Melee **[one-action] mandibles, **Damage **1d8 piercing plus 1d4  persistent poison. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/10/SectionHeader/5` | 0.337106 | **IMPALING SPIKE **[two-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **METAL**  **Traditions** arcane, primal  **Range **30 feet; **Targets** 1 creature **Defense** Reflex; **Duration** 1 minu |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/39` | 0.330584 | **GOUGING CLAW **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE** **MORPH**  **Traditions** arcane, primal **Range **touch; **Targets** 1 creature  **Defense** AC  Yo |

### Query 23
- Text: What does **ENLARGE **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/Text/4', 'PZO22001 Starfinder Player Core 330-363::/page/27/Text/62', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/67']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/4` | 0.580000 | **ENLARGE **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Range **30 feet;** Targets** 1 willing creature  **Duration** 5 minutes  Bolstered |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.570003 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/62` | 0.570003 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.528003 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.528003 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.528003 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.528003 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.528003 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.528003 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.528003 | **SPELLS** |

### Query 24
- Text: What does **ENTANGLING FLORA **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/13', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/67', 'PZO22001 Starfinder Player Core 330-363::/page/23/Text/68']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/13` | 0.724642 | **ENTANGLING FLORA **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **PLANT** **WOOD**  **Traditions** arcane, primal  **Range **120 feet; **Area** all squares in a 20-foot burst  **Duratio |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.561864 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.561864 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.519864 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.519864 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.519864 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.519864 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.519864 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.519864 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.519864 | **SPELLS** |

### Query 25
- Text: What does **ENTHRALL **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/Text/20']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/12/Text/42', 'PZO22001 Starfinder Player Core 330-363::/page/0/Text/20', 'PZO22001 Starfinder Player Core 330-363::/page/17/Text/45']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.616866 | **LIFE SEAL **[reaction] **SPELL 3** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/20` | 0.614840 | **ENTHRALL **[two-actions] **SPELL 3**  **AUDITORY** **CONCENTRATE** **EMOTION** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet;** Targets** all creatures in range  **Defense** Will |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.593129 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.551129 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.551129 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.551129 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.551129 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.551129 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.551129 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.551129 | **SPELLS** |

### Query 26
- Text: What does **ENTROPY STRIKE **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/32', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/32` | 0.692019 | **ENTROPY STRIKE **[two-actions] **SPELL 3**  **ACID** **ATTACK** **CONCENTRATE** **MANIPULATE** **VOID**  **Traditions** arcane, divine, occult  **Range **30 feet; **Targets** 1 creature or unattende |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.562260 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.560944 | **LIFE SEAL **[reaction] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.494757 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.494757 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.494757 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.494757 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.494757 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.494757 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.494757 | **SPELLS** |

### Query 27
- Text: What does **ENVIRONMENTAL ENDURANCE** **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/39']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/13/Text/61', 'PZO22001 Starfinder Player Core 330-363::/page/11/Text/63', 'PZO22001 Starfinder Player Core 330-363::/page/15/Text/60']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/61` | 0.622383 | **EQUIPMENT** **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/63` | 0.622383 | **EQUIPMENT** **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/60` | 0.622383 | **EQUIPMENT** **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/39` | 0.555987 | **ENVIRONMENTAL ENDURANCE** **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, primal  **Cast** 10 minutes  **Range **touch;** Targets** 1 willing creature  **Duration** until |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.544822 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.544822 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.544822 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.544822 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.544822 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.544822 | **SPELLS** |

### Query 28
- Text: What does **EVENT HORIZON **[two-actions] **SPELL 10** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/49']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/49', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/32', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/49` | 0.750134 | **EVENT HORIZON **[two-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE** **VOID**  **Traditions** primal  **Range **500 feet;** Area** 50-foot burst **Defense** Reflex; **Duration** 1 minute |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.532473 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/1` | 0.532422 | You unleash the power of a supermassive black hole. All  creatures in the area take 6d10 bludgeoning and 6d10 void  damage. *Event horizon* ignores up to 10 resistance creatures  in the area have to b |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/1` | 0.477220 | **HEROISM **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult **Duration** 10 minutes |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47` | 0.475064 | **REVIVAL **[two-actions] **SPELL 10**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet;** Targets** dead creatures and living creatures of  y |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/61` | 0.462750 | **EQUIPMENT** **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/63` | 0.462750 | **EQUIPMENT** **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/60` | 0.462750 | **EQUIPMENT** **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.453876 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.451528 | **SPELLS** |

### Query 29
- Text: Summarize 7 PLAYER CORE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/0']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/0', 'PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/0']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/0` | 0.997218 | 7 PLAYER CORE |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/0` | 0.997218 | 7 PLAYER CORE |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/0` | 0.997218 | 7 PLAYER CORE |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/15/SectionHeader/0` | 0.955218 | 7 PLAYER CORE |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/69` | 0.359383 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/72` | 0.359383 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/67` | 0.359383 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/49` | 0.359383 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/67` | 0.359383 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/77` | 0.359383 | **PLAYING THE ** **GAME** |

### Query 30
- Text: What is the rule about You unleash the power of a supermassive black hole. All  creatures in the area take 6d10 bludgeoning and 6d10 void  damage. *Event horizon* ignores up to 10 resistance creatures  in the area have to bludgeoning, and up to 10 resistance they  have to void. Each creature attempts a Reflex save.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/1', 'PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/49', 'PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/1` | 0.980474 | You unleash the power of a supermassive black hole. All  creatures in the area take 6d10 bludgeoning and 6d10 void  damage. *Event horizon* ignores up to 10 resistance creatures  in the area have to b |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/49` | 0.574701 | **EVENT HORIZON **[two-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE** **VOID**  **Traditions** primal  **Range **500 feet;** Area** 50-foot burst **Defense** Reflex; **Duration** 1 minute |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/3` | 0.543258 | **OVERLOAD SYSTEMS **[two-actions] **SPELL 5**  **CONCENTRATE** **ELECTRICITY** **MANIPULATE**  **Traditions** arcane, primal  **Area** 60-foot cone  **Defense** Reflex  You flood the area with a wave |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/30/Text/1` | 0.499985 | **SINGULARITY SEED **[three-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE** **VOID**  **Traditions** divine, primal  **Range **100 feet; **Area** one 5-foot square and one 50-foot  emanation surr |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/44` | 0.474928 | **FALLING STARS **[two-actions] **SPELL 9**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Area** four 40-foot bursts  **Defense** basic Reflex  You reach into t |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/37` | 0.472500 | You let out a powerful ululation full of psychic resonance that  compels others who hear it to join in. You deal 7d12 sonic  damage and 1d8 persistent mental damage to other creatures  who can hear wi |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/19` | 0.467208 | **STUMBLE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **100 feet; **Targets** 1 creature  **Defense** Reflex  A burst of micrograv |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/14` | 0.467026 | **HYDRAULIC TORRENT **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **WATER**  **Traditions** primal  **Area** 60-foot line  **Defense** Fortitude  A swirling torrent of water manifests al |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/22/SectionHeader/30` | 0.464132 | **POCKET VACUUM **[two-actions] **SPELL 6**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, primal **Range **120 feet; **Area** 20-foot burst **Defense** basic Fortitude; **Duration** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/20` | 0.463214 | **EXPLOSION OF ROT **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **POISON**  **Traditions** divine, primal  **Range **120 feet;** Area** 20-foot burst  **Defense** Reflex  A giant pustul |

### Query 31
- Text: Summarize **Critical Success** The creature is unaffected.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/30/Text/38', 'PZO22001 Starfinder Player Core 330-363::/page/28/Text/30']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/2` | 1.018921 | **Critical Success** The creature is unaffected. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/30/Text/38` | 1.018921 | **Critical Success** The creature is unaffected. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/30` | 1.018921 | **Critical Success** The creature is unaffected. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/7` | 0.976921 | **Critical Success** The creature is unaffected. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/8` | 0.976921 | **Critical Success** The creature is unaffected. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/20` | 0.976921 | **Critical Success** The creature is unaffected. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/14` | 0.976921 | **Critical Success** The creature is unaffected. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/50` | 0.976921 | **Critical Success** The creature is unaffected. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/19` | 0.976921 | **Critical Success** The creature is unaffected. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/30/Text/11` | 0.976004 | **Critical Success **The creature is unaffected. |

### Query 32
- Text: What is the rule about **Success** The creature takes half damage and is slowed 1 until  the end of its next turn.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/3', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/4', 'PZO22001 Starfinder Player Core 330-363::/page/28/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/3` | 0.852328 | **Success** The creature takes half damage and is slowed 1 until  the end of its next turn. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/4` | 0.775842 | **Failure** The creature takes full damage, is slowed 3 until the  end of its next turn, and slowed 1 for 1 minute. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/31` | 0.719302 | **Success** The creature takes half damage. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/5` | 0.686806 | **Critical Failure** The creature takes double damage, is slowed  3 until the end of its next turn, and slowed 2 for 1 minute. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/51` | 0.677302 | **Success** The creature takes half damage. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/20` | 0.677302 | **Success** The creature takes half damage. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/26/Text/48` | 0.617367 | **Failure** The creature can't attack the target and wastes the  action. It can't attempt further attacks against the target  this turn. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/9` | 0.599827 | **Failure** The creature takes full damage. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/26/Text/47` | 0.597611 | **Success** The creature can attempt its attack and any other  attacks against the target this turn. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/31/Text/3` | 0.586377 | **SLOW **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 creature **Defense** Fortitude; **Duration** varies  You dila |

### Query 33
- Text: What is the rule about **Failure** The creature takes full damage, is slowed 3 until the  end of its next turn, and slowed 1 for 1 minute.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/4', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/5', 'PZO22001 Starfinder Player Core 330-363::/page/26/Text/48']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/4` | 0.916804 | **Failure** The creature takes full damage, is slowed 3 until the  end of its next turn, and slowed 1 for 1 minute. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/5` | 0.801759 | **Critical Failure** The creature takes double damage, is slowed  3 until the end of its next turn, and slowed 2 for 1 minute. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/26/Text/48` | 0.764187 | **Failure** The creature can't attack the target and wastes the  action. It can't attempt further attacks against the target  this turn. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/9` | 0.700926 | **Failure** The creature takes full damage. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/32` | 0.677185 | **Failure** The creature takes full damage and is clumsy 1 for 1  minute. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/3` | 0.676651 | **Success** The creature takes half damage and is slowed 1 until  the end of its next turn. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/30/Text/40` | 0.659002 | **Failure** The creature falls unconscious. If it's still unconscious  after 1 minute, it wakes up automatically. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/52` | 0.652893 | **Failure** The creature takes full damage and is pushed 5 feet  away from you. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/21` | 0.652682 | **Failure** The creature takes full damage and is deafened for  1 round. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/5` | 0.643144 | **Critical Failure** The creature becomes frightened 2, and its  action fails and is wasted. |

### Query 34
- Text: What is the rule about **Critical Failure** The creature takes double damage, is slowed  3 until the end of its next turn, and slowed 2 for 1 minute.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/5', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/4', 'PZO22001 Starfinder Player Core 330-363::/page/14/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/5` | 0.918610 | **Critical Failure** The creature takes double damage, is slowed  3 until the end of its next turn, and slowed 2 for 1 minute. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/4` | 0.806935 | **Failure** The creature takes full damage, is slowed 3 until the  end of its next turn, and slowed 1 for 1 minute. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/5` | 0.772713 | **Critical Failure** The creature becomes frightened 2, and its  action fails and is wasted. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/41` | 0.692620 | **Critical Failure** As failure, but the target takes double the  initial and persistent damage. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/22` | 0.690598 | **Critical Failure** The creature takes double damage, is  deafened for 1 minute, and is stunned 1. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/17` | 0.684000 | **Critical Failure** The creature dies. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/53` | 0.671353 | **Critical Failure** The creature takes double damage and is  pushed 10 feet away from you. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/33` | 0.667929 | **Critical Failure** The creature takes full damage and is clumsy  2 for 1 minute. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/26/Text/48` | 0.655392 | **Failure** The creature can't attack the target and wastes the  action. It can't attempt further attacks against the target  this turn. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/26/Text/49` | 0.653872 | **Critical Failure** The creature wastes the action and can't  attempt to attack the target for the rest of *sanctuary*'s  duration. |

### Query 35
- Text: What does **EVERLIGHT **[three-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/6', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21', 'PZO22001 Starfinder Player Core 330-363::/page/15/Text/60']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/6` | 0.638102 | **EVERLIGHT **[three-actions] **SPELL 2**  **CONCENTRATE** **LIGHT** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **touch; **Targets** a gemstone worth 60 credits or more **D |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.591498 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/60` | 0.575522 | **EQUIPMENT** **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/63` | 0.533522 | **EQUIPMENT** **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/61` | 0.533522 | **EQUIPMENT** **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.528459 | **LIFE SEAL **[reaction] **SPELL 3** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.526198 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.526198 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/62` | 0.526198 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.526198 | **SPELLS** |

### Query 36
- Text: What does **EXECUTE **[two-actions] **SPELL 7** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/12']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/32', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/12', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.621273 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/12` | 0.607742 | **EXECUTE **[two-actions] **SPELL 7**  **CONCENTRATE** **DEATH** **MANIPULATE** **VOID**  **Traditions** divine, primal  **Range **30 feet; **Targets** 1 creature  **Defense** basic Fortitude  You poi |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.532758 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/13/SectionHeader/48` | 0.482785 | **MASK OF TERROR **[two-actions] **SPELL 7**  **CONCENTRATE** **EMOTION** **FEAR** **ILLUSION** **MANIPULATE** **MENTAL** **VISUAL**  **Traditions** arcane, occult, primal  **Range **30 feet; **Target |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.477931 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.477931 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.477931 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.477931 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.477931 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.477931 | **SPELLS** |

### Query 37
- Text: What does **EXPLOSION OF ROT **[two-actions] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/20', 'PZO22001 Starfinder Player Core 330-363::/page/18/SectionHeader/45', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/20` | 0.711483 | **EXPLOSION OF ROT **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **POISON**  **Traditions** divine, primal  **Range **120 feet;** Area** 20-foot burst  **Defense** Reflex  A giant pustul |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/18/SectionHeader/45` | 0.519734 | **OUTCAST'S CURSE **[two-actions] **SPELL 4**  **CONCENTRATE** **CURSE** **MANIPULATE** **MENTAL** **MISFORTUNE**  **Traditions** arcane, divine, occult **Range **touch;** Targets** 1 creature  **Defe |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.518351 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/12` | 0.478204 | **EXECUTE **[two-actions] **SPELL 7**  **CONCENTRATE** **DEATH** **MANIPULATE** **VOID**  **Traditions** divine, primal  **Range **30 feet; **Targets** 1 creature  **Defense** basic Fortitude  You poi |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.469320 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.469320 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.469320 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.469320 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.469320 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.469320 | **SPELLS** |

### Query 38
- Text: What does **FABRICATED TRUTH **[three-actions] **SPELL 10** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/32', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/1', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/32` | 0.725624 | **FABRICATED TRUTH **[three-actions] **SPELL 10**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** occult  **Range **100 feet;** Targets** up to 5 creatures  **Defense** W |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/1` | 0.535640 | **HEROISM **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult **Duration** 10 minutes |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.525951 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/17/SectionHeader/25` | 0.476877 | **NEW GAME **[three-actions] **SPELL 10**  **CONCENTRATE** **EXTRADIMENSIONAL** **MANIPULATE**  **Traditions** arcane  **Requirements** You have access to a computer with a vidgame  installed on it, w |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.473526 | **LIFE SEAL **[reaction] **SPELL 3** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47` | 0.470611 | **REVIVAL **[two-actions] **SPELL 10**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet;** Targets** dead creatures and living creatures of  y |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.466612 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/49` | 0.466454 | **EVENT HORIZON **[two-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE** **VOID**  **Traditions** primal  **Range **500 feet;** Area** 50-foot burst **Defense** Reflex; **Duration** 1 minute |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.455689 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/4` | 0.448459 | **HONEYED WORDS **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes  You unlock the |

### Query 39
- Text: What does **FALLING STARS **[two-actions] **SPELL 9** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/44', 'PZO22001 Starfinder Player Core 330-363::/page/19/Text/72', 'PZO22001 Starfinder Player Core 330-363::/page/17/Text/45']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/44` | 0.666654 | **FALLING STARS **[two-actions] **SPELL 9**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Area** four 40-foot bursts  **Defense** basic Reflex  You reach into t |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.579411 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.579411 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.537411 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/62` | 0.537411 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.537411 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.537411 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.537411 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.537411 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.537411 | **SPELLS** |

### Query 40
- Text: What does **FALSE VISION** **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/52']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/52', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/61', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/67']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/52` | 0.689024 | **FALSE VISION** **SPELL 5**  **UNCOMMON** **CONCENTRATE** **ILLUSION** **MANIPULATE**  **Traditions** arcane, occult  **Cast** 10 minutes  **Range **touch;** Area** 100-foot burst  **Duration** until |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.564299 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.564299 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.522299 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/62` | 0.522299 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.522299 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.522299 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.522299 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.522299 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.522299 | **SPELLS** |

### Query 41
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/61']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/61', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/55', 'PZO22001 Starfinder Player Core 330-363::/page/25/Text/55']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/61` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/55` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/55` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/39` | 0.838541 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/55` | 0.838541 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/56` | 0.838541 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/57` | 0.838541 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/57` | 0.838541 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/62` | 0.838541 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/58` | 0.838541 | **INTRODUCTION** |

### Query 42
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/62']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/62', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/56', 'PZO22001 Starfinder Player Core 330-363::/page/11/Text/59']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/62` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/56` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/59` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/58` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/40` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/63` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/56` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/59` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/58` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/40` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 43
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/63']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/17/Text/41', 'PZO22001 Starfinder Player Core 330-363::/page/13/Text/58', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/63']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/41` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/58` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/63` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/60` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/60` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/57` | 0.910061 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/64` | 0.910061 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/57` | 0.910061 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/57` | 0.910061 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/59` | 0.910061 | **CLASSES** |

### Query 44
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/64']
- Expected found: `True`
- Expected rank: `9`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/19/Text/69', 'PZO22001 Starfinder Player Core 330-363::/page/27/Text/60', 'PZO22001 Starfinder Player Core 330-363::/page/17/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/69` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/60` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/42` | 0.864442 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/65` | 0.822442 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/59` | 0.822442 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/58` | 0.822442 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/61` | 0.822442 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/58` | 0.822442 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/64` | 0.822442 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/58` | 0.822442 | **SKILLS** |

### Query 45
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/65']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/23/Text/66', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/65', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/66` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/65` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/43` | 0.871817 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/60` | 0.829817 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/59` | 0.829817 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/59` | 0.829817 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/70` | 0.829817 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/62` | 0.829817 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/43` | 0.829817 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/62` | 0.829817 | **FEATS** |

### Query 46
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/66']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/66', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/60', 'PZO22001 Starfinder Player Core 330-363::/page/17/Text/44']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/66` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/60` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/44` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/71` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/61` | 0.902726 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/63` | 0.902726 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/67` | 0.902726 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/44` | 0.902726 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/61` | 0.627947 | **FEATS** **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/59` | 0.627947 | **FEATS** **EQUIPMENT** |

### Query 47
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/67']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/45', 'PZO22001 Starfinder Player Core 330-363::/page/17/Text/45', 'PZO22001 Starfinder Player Core 330-363::/page/25/Text/60']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.847304 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.847304 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.847304 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.847304 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/62` | 0.847303 | **SPELLS** |

### Query 48
- Text: What is the rule about **Spell Lists**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/68']
- Expected found: `True`
- Expected rank: `13`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/33/Text/65', 'PZO22001 Starfinder Player Core 330-363::/page/17/Text/46', 'PZO22001 Starfinder Player Core 330-363::/page/15/Text/61']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/65` | 0.890837 | **Spell Lists** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/46` | 0.890837 | **Spell Lists** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/61` | 0.890837 | **Spell Lists** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/70` | 0.848837 | **Spell Lists** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/46` | 0.848837 | **Spell Lists** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/61` | 0.848837 | **Spell Lists** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/65` | 0.848837 | **Spell Lists** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/63` | 0.848837 | **Spell Lists** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/63` | 0.848837 | **Spell Lists** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/63` | 0.848837 | **Spell Lists** |

### Query 49
- Text: What is the rule about **Spells**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/69']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/33/Text/66', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/69', 'PZO22001 Starfinder Player Core 330-363::/page/13/Text/64']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/66` | 0.798799 | **Spells** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/69` | 0.798799 | **Spells** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/64` | 0.798799 | **Spells** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/63` | 0.756799 | **Spells** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/62` | 0.756799 | **Spells** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/62` | 0.756799 | **Spells** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/64` | 0.756799 | **Spells** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/74` | 0.756799 | **Spells** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/66` | 0.756799 | **Spells** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/47` | 0.756799 | **Spells** |

### Query 50
- Text: What is the rule about **Focus Spells**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/70']
- Expected found: `True`
- Expected rank: `10`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/65', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/64', 'PZO22001 Starfinder Player Core 330-363::/page/15/Text/63']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/65` | 0.926221 | **Focus Spells** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/64` | 0.926221 | **Focus Spells** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/63` | 0.926221 | **Focus Spells** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/67` | 0.884221 | **Focus Spells** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/65` | 0.884221 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/75` | 0.884221 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/63` | 0.884221 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/67` | 0.884221 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/65` | 0.884221 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/70` | 0.884221 | **Focus Spells** |

### Query 51
- Text: Summarize **Rituals**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/71']
- Expected found: `True`
- Expected rank: `10`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/65', 'PZO22001 Starfinder Player Core 330-363::/page/23/Text/73', 'PZO22001 Starfinder Player Core 330-363::/page/19/Text/76']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/65` | 0.971114 | **Rituals** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/76` | 0.971114 | **Rituals** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/73` | 0.971114 | **Rituals** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/64` | 0.929114 | **Rituals** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/68` | 0.929113 | **Rituals** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/48` | 0.929113 | **Rituals** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/66` | 0.929113 | **Rituals** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/66` | 0.929113 | **Rituals** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/66` | 0.929113 | **Rituals** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/71` | 0.929113 | **Rituals** |

### Query 52
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/72']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/49', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/67', 'PZO22001 Starfinder Player Core 330-363::/page/15/Text/65']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/49` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/67` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/65` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/72` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/77` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/49` | 0.923000 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/69` | 0.923000 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/67` | 0.923000 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/74` | 0.923000 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/67` | 0.923000 | **PLAYING THE ** **GAME** |

### Query 53
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/73']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/33/Text/70', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/68', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/67']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/70` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/68` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/67` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/73` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/50` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/66` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/71` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/78` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/68` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/51` | 0.769880 | **APPENDIX** |

### Query 54
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/74']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/33/Text/71', 'PZO22001 Starfinder Player Core 330-363::/page/17/Text/51', 'PZO22001 Starfinder Player Core 330-363::/page/13/Text/69']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/71` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/51` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/69` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/68` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/74` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/67` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/52` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/69` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/77` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/72` | 0.951465 | **GLOSSARY & ** **INDEX** |

### Query 55
- Text: What does **FALSE VITALITY **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/2/SectionHeader/1', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/42', 'PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/2/SectionHeader/1` | 0.699232 | **FALSE VITALITY **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Duration** 8 hours  You augment your flesh with the energies typically used to  manipulat |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.564825 | **LIFE SEAL **[reaction] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47` | 0.559706 | **REVIVAL **[two-actions] **SPELL 10**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet;** Targets** dead creatures and living creatures of  y |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.515696 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.503805 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.503467 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.503467 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.503467 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/62` | 0.503467 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.503467 | **SPELLS** |

### Query 56
- Text: What does **FEAR **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/8', 'PZO22001 Starfinder Player Core 330-363::/page/25/Text/60', 'PZO22001 Starfinder Player Core 330-363::/page/33/Text/64']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/8` | 0.684609 | **FEAR **[two-actions] **SPELL 1**  **CONCENTRATE** **EMOTION** **FEAR** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult, primal  **Range **30 feet;** Targets** 1 creature **Defense** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.597696 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.597696 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.555696 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.555696 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.555696 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.555696 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.555696 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.555696 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.555696 | **SPELLS** |

### Query 57
- Text: What does **FELINE SENSES **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/18', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/42', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/18` | 0.757451 | **FELINE SENSES **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MORPH**  **Traditions** divine, primal  **Duration** 1 hour |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.606925 | **LIFE SEAL **[reaction] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.605374 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.542462 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.542462 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.542462 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.542462 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/62` | 0.542462 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.542462 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.542462 | **SPELLS** |

### Query 58
- Text: Summarize Your senses improve as you gain feline eyes, ears, and  whiskers. You gain darkvision and electromagnetic scent  as an imprecise sense out to 30 feet, allowing you to detect  living and technological creatures.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/23', 'PZO22001 Starfinder Player Core 330-363::/page/20/ListItem/18', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/23` | 1.039615 | Your senses improve as you gain feline eyes, ears, and  whiskers. You gain darkvision and electromagnetic scent  as an imprecise sense out to 30 feet, allowing you to detect  living and technological |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/20/ListItem/18` | 0.579976 | Low-light vision and imprecise scent 30 feet. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/1` | 0.554249 | You create an illusory image of a Large or smaller creature. It  generates the appropriate sounds, smells, and feels believable  to the touch. If you and the image are ever farther than 500  feet apar |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/3` | 0.508278 | **Heightened (3rd)** You gain darkvision or low-light vision if the  form you assume has that ability. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/20/Text/5` | 0.493139 | **Perception **+0; darkvision |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/50` | 0.490875 | **SUBJECTIVE REALITY **[one-action] **SPELL 5**  **CONCENTRATE** **MANIPULATE**  **Traditions** occult  **Range **500 feet;** Targets** 1 creature or object  **Duration** sustained up to 1 minute  You |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/3` | 0.479442 | **SCOUTING EYE** **SPELL 5**  **CONCENTRATE** **MANIPULATE** **SCRYING**  **Traditions** arcane, divine, occult  **Cast** 1 minute **Range **see text **Duration** sustained  You create an invisible, f |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/33` | 0.474479 | **FIGMENT **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet  **Duration** sustained  You create a simp |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/10` | 0.468814 | **SCRYING** **SPELL 6**  **UNCOMMON** **CONCENTRATE** **MANIPULATE** **SCRYING**  **Traditions** arcane, occult  **Cast** 10 minutes  **Range **planetary;** Targets** 1 creature  **Defense** Will; **D |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/21` | 0.468189 | **Success** The creature perceives what you chose until it  disbelieves, but it knows what the hallucination is. |

### Query 59
- Text: What is the rule about **Heightened (4th)** The spell's range is touch and it targets 1  willing creature.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/24', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/25', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/24` | 0.962701 | **Heightened (4th)** The spell's range is touch and it targets 1  willing creature. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/25` | 0.830090 | **Heightened (6th)** The spell's range is touch and it targets 1 willing  creature. The duration is until your next daily preparations. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/2` | 0.803509 | **Heightened (4th)** The spell lasts 1 minute, but it doesn't end if  the target uses a hostile action. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/29/Text/6` | 0.680767 | **Heightened** **(4th)** The spell can predict results up to 1 week  into the future. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/34` | 0.671763 | **Heightened (6th)** The spell targets up to four creatures and  deals 6d12 mental damage. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/50` | 0.667464 | **Heightened (7th)** You can target up to 5 additional creatures  to gain protection against the environment the triggering  creature entered. The spell lasts for 8 hours and also  protects against ex |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/30` | 0.664788 | **Heightened (4th)** Your battle form is Large, and your attacks  have 10-foot reach. You instead gain 15 temporary HP,  attack modifier +16, damage bonus +6, and Athletics +16. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/6` | 0.653827 | **Heightened (8th)** You can target up to 5 creatures. If a  creature uses a hostile action or reaction that affects  multiple targets simultaneously, it needs to attempt only  one save against *mask |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/11` | 0.652257 | **STATUS **[two-actions] **SPELL 2**  **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch;** Targets** 1 willing living creature  **Duration** until yo |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/25` | 0.647627 | **Heightened (8th)** Choose to either target any number of  creatures or change the spell's duration to unlimited. |

### Query 60
- Text: What is the rule about **Heightened (6th)** The spell's range is touch and it targets 1 willing  creature. The duration is until your next daily preparations.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/25', 'PZO22001 Starfinder Player Core 330-363::/page/6/Text/24', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/24']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/25` | 0.973811 | **Heightened (6th)** The spell's range is touch and it targets 1 willing  creature. The duration is until your next daily preparations. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/24` | 0.850586 | **Heightened (6th)** Choose to either target up to 10 creatures  or change the spell's duration to until your next daily  preparations. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/24` | 0.833060 | **Heightened (4th)** The spell's range is touch and it targets 1  willing creature. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/34` | 0.743366 | **Heightened (6th)** The spell targets up to four creatures and  deals 6d12 mental damage. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/50` | 0.709738 | **Heightened (7th)** You can target up to 5 additional creatures  to gain protection against the environment the triggering  creature entered. The spell lasts for 8 hours and also  protects against ex |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/25` | 0.699053 | **Heightened (8th)** Choose to either target any number of  creatures or change the spell's duration to unlimited. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/2` | 0.697134 | **Heightened (4th)** The spell lasts 1 minute, but it doesn't end if  the target uses a hostile action. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/51` | 0.686885 | **Heightened (10th)** You can target up to 10 additional  creatures to gain protection against the environment the  triggering creature entered. The spell lasts until your next  daily preparations and |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/22/Text/29` | 0.659931 | **Heightened (6th)** Your battle form is Huge, and the reach of  your attacks increases by 5 feet. You instead gain AC = 22  + your level, 24 temporary HP, attack modifier +21, damage  bonus +16, and |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/10/Text/3` | 0.654019 | **Heightened (6th)** Creatures or objects in your scene can  speak. You must speak the specific lines for each actor  when creating your program. The spell disguises your  voice for each actor. |

### Query 61
- Text: What does **FIELD OF LIFE **[two-actions] **SPELL 6** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/26', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/42', 'PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/26` | 0.691065 | **FIELD OF LIFE **[two-actions] **SPELL 6**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet; **Area** 20-foot burst **Duration** sustained up |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.554506 | **LIFE SEAL **[reaction] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47` | 0.530042 | **REVIVAL **[two-actions] **SPELL 10**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet;** Targets** dead creatures and living creatures of  y |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.487410 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.478023 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.478023 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.478023 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.478023 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.478023 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.478023 | **SPELLS** |

### Query 62
- Text: What does **FIGMENT **[two-actions] **CANTRIP 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/33']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/33', 'PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/6', 'PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/33` | 0.673553 | **FIGMENT **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet  **Duration** sustained  You create a simp |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/6` | 0.642598 | **PRESTIDIGITATION **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **10 feet; **Targets** 1 object (cook, lift, or tid |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/19` | 0.613454 | **STUMBLE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **100 feet; **Targets** 1 creature  **Defense** Reflex  A burst of micrograv |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/5` | 0.565328 | **STABILIZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet; **Targets** 1 dying creature  Life ene |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/5/SectionHeader/20` | 0.564207 | **GUIDANCE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE**  **Traditions** divine, occult, primal  **Range **30 feet; **Targets** 1 creature  **Duration** until the start of your next turn |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/37` | 0.562250 | **IGNITION **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Targets** 1 creature  **Defense** AC  You |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/11` | 0.542580 | **FORBIDDING WARD **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** divine, occult  **Range **30 feet; **Targets** 1 ally and 1 enemy  **Duration** sustained up |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/26/Text/12` | 0.535755 | **RICOCHET **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE** **METAL**  **Traditions** arcane, divine  **Range **30 feet; **Targets** 1 or 2 creatures  **Defense** basic Reflex |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/39` | 0.526618 | **FROSTBITE **[two-actions] **CANTRIP 1**  **CANTRIP** **COLD** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets** 1 creature  **Defense** Fortitude  An orb |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/14/SectionHeader/19` | 0.524915 | **MEASURE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE**  **Traditions** arcane, divine, occult, primal  **Area** 200-foot emanation  **Duration** sustained up to 1 minute  You learn the ap |

### Query 63
- Text: What does **FIRE SHIELD **[two-actions] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/41', 'PZO22001 Starfinder Player Core 330-363::/page/17/Text/45', 'PZO22001 Starfinder Player Core 330-363::/page/23/Text/68']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/41` | 0.706918 | **FIRE SHIELD **[two-actions] **SPELL 4**  **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Duration** 1 minute  You create a hovering shield made of fire. As long as the  shi |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.556185 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.556185 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.514185 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.514185 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.514185 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.514185 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.514185 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/62` | 0.514185 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.514185 | **SPELLS** |

### Query 64
- Text: What does **FIREBALL **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/48']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/48', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/42', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/48` | 0.645852 | **FIREBALL **[two-actions] **SPELL 3**  **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Area** 20-foot burst  **Defense** basic Reflex  A roaring blast of |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.614673 | **LIFE SEAL **[reaction] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.610200 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.525901 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.525901 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.525901 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.525901 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.525901 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.525901 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.525901 | **SPELLS** |

### Query 65
- Text: What does **FLEET STEP **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/56']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/56', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/62', 'PZO22001 Starfinder Player Core 330-363::/page/25/Text/60']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/56` | 0.692812 | **FLEET STEP **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Duration** 1 minute  You gain a +30-foot status bonus to your Speed. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.593962 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.593962 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.551962 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.551962 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.551962 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.551962 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.551962 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.551962 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.551962 | **SPELLS** |

### Query 66
- Text: What does **FLICKER **[two-actions] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/62']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/62', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/67', 'PZO22001 Starfinder Player Core 330-363::/page/23/Text/68']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/62` | 0.635064 | **FLICKER **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **TELEPORTATION**  **Traditions** arcane, occult  **Duration** 1 minute  You flicker quickly between your current plane and anothe |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.571514 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.571514 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.529514 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.529514 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.529514 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.529514 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.529514 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.529514 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.529514 | **SPELLS** |

### Query 67
- Text: What does **FLOATING FLAME **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/69']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/2/Text/69', 'PZO22001 Starfinder Player Core 330-363::/page/33/Text/64', 'PZO22001 Starfinder Player Core 330-363::/page/19/Text/72']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/69` | 0.703685 | **FLOATING FLAME **[two-actions] **SPELL 2**  **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Targets** one 5-foot square  **Defense** Reflex; **Duration** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.572520 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.572520 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.530520 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.530520 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.530520 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/62` | 0.530520 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.530520 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.530520 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.530520 | **SPELLS** |

### Query 68
- Text: Summarize 7 PLAYER CORE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/0']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/0', 'PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/0', 'PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/0']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/0` | 0.997218 | 7 PLAYER CORE |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/0` | 0.997218 | 7 PLAYER CORE |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/0` | 0.997218 | 7 PLAYER CORE |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/15/SectionHeader/0` | 0.955218 | 7 PLAYER CORE |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/69` | 0.359383 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/72` | 0.359383 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/67` | 0.359383 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/49` | 0.359383 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/67` | 0.359383 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/77` | 0.359383 | **PLAYING THE ** **GAME** |

### Query 69
- Text: What is the rule about When you Sustain this spell, you can levitate the flame up to  10 feet. It then deals damage to each creature whose space  it shared at any point during its flight. This uses the same  damage and save, and you roll the damage once each time  you Sustain. A given creature can take damage from *floating * *flame* only once per round.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/1', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/36', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/69']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/1` | 0.997132 | When you Sustain this spell, you can levitate the flame up to  10 feet. It then deals damage to each creature whose space  it shared at any point during its flight. This uses the same  damage and save |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/36` | 0.655241 | **LEVITATE **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 unattended object or willing creature **Duration** 5 minutes  You |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/69` | 0.610335 | **FLOATING FLAME **[two-actions] **SPELL 2**  **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Targets** one 5-foot square  **Defense** Reflex; **Duration** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/3` | 0.560193 | In combat, the illusion can use 2 actions per turn, which  it uses when you Sustain the spell. It uses your spell attack  modifier for attack rolls and your spell DC for its AC. Its  saving throw modi |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/44` | 0.527881 | **FALLING STARS **[two-actions] **SPELL 9**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **500 feet;** Area** four 40-foot bursts  **Defense** basic Reflex  You reach into t |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/62` | 0.527683 | **FLICKER **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **TELEPORTATION**  **Traditions** arcane, occult  **Duration** 1 minute  You flicker quickly between your current plane and anothe |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/10/SectionHeader/25` | 0.526033 | **IMPLOSION **[two-actions] **SPELL 9**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet;** Targets** 1 corporeal creature  **Defense** basic Fortitude; **Duration** s |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/16` | 0.518898 | **SHARE LIFE **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** divine  **Range **30 feet;** Targets** 1 creature  **Duration** 10 minutes  You forge a temporary link between |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/17` | 0.507989 | *Prestidigitation* can't deal damage or cause adverse  conditions. Any actual change to an object (beyond what is  noted above) persists only as long as you Sustain the spell. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/52` | 0.500430 | **Failure** The creature takes full damage and is pushed 5 feet  away from you. |

### Query 70
- Text: What is the rule about **Heightened (+1)** The damage increases by 1d6.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/18/Text/23', 'PZO22001 Starfinder Player Core 330-363::/page/23/Text/54']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/2` | 0.904103 | **Heightened (+1)** The damage increases by 1d6. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/23` | 0.862523 | **Heightened (+1)** The damage increases by 1d10. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/54` | 0.811515 | **Heightened (+1)** The damage increases by 2d4. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/6` | 0.667978 | **Heightened (+1)** The damage of the image's Strikes increases  by 1d4, and the maximum size of creature you can create  increases by one (to a maximum of Gargantuan). |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/22/Text/29` | 0.636320 | **Heightened (6th)** Your battle form is Huge, and the reach of  your attacks increases by 5 feet. You instead gain AC = 22  + your level, 24 temporary HP, attack modifier +21, damage  bonus +16, and |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/11` | 0.634375 | **Heightened (+1)** The void damage increases by 2d4, and the  persistent bleed damage increases by 1. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/31` | 0.620626 | **Heightened (5th)** Your battle form is Huge, and your attacks  have 15-foot reach. You instead gain 20 temporary HP,  attack modifier +18, damage bonus +2 and double damage  dice (including persiste |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/16/Text/9` | 0.612745 | **Heightened (9th)** You instead gain AC = 22 + your level, 25  temporary HP, attack modifier +31, increase damage by  one damage die, and Athletics +33. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/18` | 0.607682 | **Heightened (10th)** The spell can affect living creatures up to  19th level. Increase the damage to 10d6 on a success, and  to 115 on a failure. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/34` | 0.600051 | **Heightened (6th)** The spell targets up to four creatures and  deals 6d12 mental damage. |

### Query 71
- Text: Summarize **CONCENTRATE** **MANIPULATE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/44', 'PZO22001 Starfinder Player Core 330-363::/page/8/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` | 0.991744 | **CONCENTRATE** **MANIPULATE** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/44` | 0.810298 | **CONCENTRATE** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/23` | 0.810298 | **CONCENTRATE** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/13/SectionHeader/43` | 0.592027 | **MANIFESTATION **[three-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  You spin secrets from the fundaments of magic, shaping them  into a power |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.531286 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/14/SectionHeader/27` | 0.529030 | **MENDING** **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Cast** 10 minutes  **Range **touch;** Targets** non-magical object of light Bulk or less You r |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/1` | 0.519637 | **HEROISM **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult **Duration** 10 minutes |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/10/SectionHeader/25` | 0.517381 | **IMPLOSION **[two-actions] **SPELL 9**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet;** Targets** 1 corporeal creature  **Defense** basic Fortitude; **Duration** s |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/60` | 0.515438 | **PEST FORM **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Duration** 10 minutes |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/36` | 0.515136 | **HASTE **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Range **30 feet;** Targets** 1 creature  **Duration** 1 minute  Magic empowers the target |

### Query 72
- Text: What does **Traditions** arcane, divine, occult, primal do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/6', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/34', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/45']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/6` | 0.931940 | **Traditions** arcane, divine, occult, primal |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/34` | 0.896098 | **Traditions** divine, occult, primal |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/45` | 0.845997 | **Traditions** divine, primal |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/24` | 0.769434 | **Traditions** occult |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/0/Table/3` | 0.511877 | DragonTraditionSpeedsDragon BreathAbysiumArcane—Cone of poison (Fortitude)AkashicOccult—Cone of mental (Will)CosmicDivine—Cone of spirit (Will)HostPrimalClimbCone of piercing (Reflex) |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/6` | 0.466951 | **PRESTIDIGITATION **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **10 feet; **Targets** 1 object (cook, lift, or tid |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/76` | 0.463920 | **Rituals** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/73` | 0.463920 | **Rituals** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/65` | 0.463920 | **Rituals** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/64` | 0.463920 | **Rituals** |

### Query 73
- Text: Summarize **Range **touch;** Targets** 1 creature
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/7', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/47', 'PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/7` | 1.023820 | **Range **touch;** Targets** 1 creature |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/47` | 0.679483 | **Range **60 feet; **Targets** the triggering creature |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/11` | 0.677127 | **STATUS **[two-actions] **SPELL 2**  **CONCENTRATE** **DETECTION** **MANIPULATE**  **Traditions** divine, occult, primal  **Range **touch;** Targets** 1 willing living creature  **Duration** until yo |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/24` | 0.618367 | **Heightened (4th)** The spell's range is touch and it targets 1  willing creature. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/35` | 0.614130 | **PROTECTION **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** divine, occult  **Range **touch;** Targets** 1 willing creature  **Duration** 1 minute  You ward a creature aga |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.603868 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/6` | 0.597798 | **Heightened (8th)** You can target up to 5 creatures. If a  creature uses a hostile action or reaction that affects  multiple targets simultaneously, it needs to attempt only  one save against *mask |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/29/SectionHeader/14` | 0.596260 | **SILENCE **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** divine, occult  **Range **touch;** Targets** 1 willing creature  **Duration** 1 minute  The target makes n |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/31/Text/3` | 0.592670 | **SLOW **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 creature **Defense** Fortitude; **Duration** varies  You dila |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/32` | 0.591881 | **INSTANT VIRUS **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane  **Range **touch; **Targets** 1 creature with the tech trait  **Defense** Fortitude  Your touch insta |

### Query 74
- Text: Summarize **Duration** 5 minutes
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/8', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/48', 'PZO22001 Starfinder Player Core 330-363::/page/32/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/8` | 0.911526 | **Duration** 5 minutes |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/48` | 0.806483 | **Duration** 1 minute |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/32/Text/31` | 0.437490 | **Heightened (4th)** The duration is 8 hours. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/32/SectionHeader/17` | 0.391333 | **SPEAK WITH COMPUTERS **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine  **Duration** 1 hour  You can ask questions of and receive answers from the  spirits i |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/1` | 0.389610 | **HEROISM **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult **Duration** 10 minutes |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/10` | 0.387068 | **Heightened (7th)** The duration increases to 1 hour. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/24/Text/20` | 0.384881 | **READ OMENS** **SPELL 4**  **UNCOMMON** **CONCENTRATE** **MANIPULATE** **PREDICTION**  **Traditions** divine, occult  **Cast** 10 minutes  You peek into the future. Choose a particular goal or activi |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/32/SectionHeader/32` | 0.383585 | **SPEAK WITH STONES **[two-actions] **SPELL 5**  **CONCENTRATE** **EARTH** **MANIPULATE**  **Traditions** divine, occult, primal  **Duration** 1 hour  You can ask questions of and receive answers from |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/39` | 0.379964 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/66` | 0.379964 | **INTRODUCTION** |

### Query 75
- Text: Summarize The target can soar through the air, gaining a fly Speed equal  to its Speed or 20 feet, whichever is greater.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/9', 'PZO22001 Starfinder Player Core 330-363::/page/20/Text/20', 'PZO22001 Starfinder Player Core 330-363::/page/20/Text/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/9` | 1.031129 | The target can soar through the air, gaining a fly Speed equal  to its Speed or 20 feet, whichever is greater. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/20/Text/20` | 0.629786 | **Heightened (4th)** You can turn into a flying creature, such as  a bird, which grants you a fly Speed of 20 feet. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/20/Text/12` | 0.579455 | **Speed **fly 30 feet |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/20/ListItem/16` | 0.493164 | Speed 20 feet. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/31/Text/3` | 0.478818 | **SLOW **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 creature **Defense** Fortitude; **Duration** varies  You dila |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/22/ListItem/27` | 0.461416 | **Moonflower** Speed 30 feet; resistance 10 to electricity;  **Melee **[one-action] bite (reach 15 feet), **Damage **2d10 piercing;  **Melee **[one-action] root (reach 15 feet), **Damage **2d8 bludgeo |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/46` | 0.453197 | **GRAVITY FIELD **[three-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **100 feet; **Area** 30-foot radius, 100-foot-tall cylinder  **Dur |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/47` | 0.450355 | **Range **60 feet; **Targets** the triggering creature |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/38` | 0.449456 | **Critical Success** The target is unaffected. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/30/Text/13` | 0.448432 | **Failure **The creature is pulled 20 feet toward the  singularity. |

### Query 76
- Text: Summarize **Heightened (7th)** The duration increases to 1 hour.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/10', 'PZO22001 Starfinder Player Core 330-363::/page/32/Text/31', 'PZO22001 Starfinder Player Core 330-363::/page/10/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/10` | 1.019804 | **Heightened (7th)** The duration increases to 1 hour. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/32/Text/31` | 0.808533 | **Heightened (4th)** The duration is 8 hours. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/10/Text/4` | 0.763965 | **Heightened (8th)** As the 6th-rank version, and the duration  is unlimited. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/24` | 0.639058 | **Heightened (6th)** Choose to either target up to 10 creatures  or change the spell's duration to until your next daily  preparations. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/25` | 0.625857 | **Heightened (8th)** Choose to either target any number of  creatures or change the spell's duration to unlimited. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/50` | 0.624402 | **Heightened (7th)** You can target up to 5 additional creatures  to gain protection against the environment the triggering  creature entered. The spell lasts for 8 hours and also  protects against ex |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/2` | 0.619922 | **Heightened (+1)** The damage increases by 1d6. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/22/Text/29` | 0.610650 | **Heightened (6th)** Your battle form is Huge, and the reach of  your attacks increases by 5 feet. You instead gain AC = 22  + your level, 24 temporary HP, attack modifier +21, damage  bonus +16, and |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/2` | 0.610364 | **Heightened (4th)** The spell lasts 1 minute, but it doesn't end if  the target uses a hostile action. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/16/Text/9` | 0.602253 | **Heightened (9th)** You instead gain AC = 22 + your level, 25  temporary HP, attack modifier +31, increase damage by  one damage die, and Athletics +33. |

### Query 77
- Text: What does **FORBIDDING WARD **[two-actions] **CANTRIP 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/11', 'PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/6', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/33']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/11` | 0.781123 | **FORBIDDING WARD **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** divine, occult  **Range **30 feet; **Targets** 1 ally and 1 enemy  **Duration** sustained up |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/6` | 0.604790 | **PRESTIDIGITATION **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **10 feet; **Targets** 1 object (cook, lift, or tid |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/33` | 0.563346 | **FIGMENT **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet  **Duration** sustained  You create a simp |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/39` | 0.517907 | **FROSTBITE **[two-actions] **CANTRIP 1**  **CANTRIP** **COLD** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets** 1 creature  **Defense** Fortitude  An orb |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/5/SectionHeader/20` | 0.511799 | **GUIDANCE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE**  **Traditions** divine, occult, primal  **Range **30 feet; **Targets** 1 creature  **Duration** until the start of your next turn |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/19` | 0.494700 | **STUMBLE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **100 feet; **Targets** 1 creature  **Defense** Reflex  A burst of micrograv |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/5` | 0.491824 | **STABILIZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet; **Targets** 1 dying creature  Life ene |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/37` | 0.491112 | **IGNITION **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Targets** 1 creature  **Defense** AC  You |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/14/SectionHeader/19` | 0.461575 | **MEASURE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE**  **Traditions** arcane, divine, occult, primal  **Area** 200-foot emanation  **Duration** sustained up to 1 minute  You learn the ap |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/3` | 0.460115 | **INJURY ECHO **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **60 feet; **Targets** 1 creature  **Defense** Will  You manifest an inj |

### Query 78
- Text: What does **FORCE BARRAGE **[one-action]** TO **[three-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/19', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21', 'PZO22001 Starfinder Player Core 330-363::/page/27/SectionHeader/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/19` | 0.722688 | **FORCE BARRAGE **[one-action]** TO **[three-actions] **SPELL 1**  **CONCENTRATE** **FORCE** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet;** Targets** 1 creature  You fire a shard |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.592326 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/27/SectionHeader/42` | 0.563292 | **SENDING **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult  **Range **planetary;** Targets** 1 creature you know well  You send the creat |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/15` | 0.514542 | **PARALYZE **[two-actions] **SPELL 3**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature  **Defense** Will; **Durat |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/8` | 0.508771 | **FEAR **[two-actions] **SPELL 1**  **CONCENTRATE** **EMOTION** **FEAR** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult, primal  **Range **30 feet;** Targets** 1 creature **Defense** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/31/Text/3` | 0.508186 | **SLOW **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 creature **Defense** Fortitude; **Duration** varies  You dila |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/44` | 0.505569 | **HEAL **[one-action]** TO **[three-actions] **SPELL 1**  **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **varies; **Targets** 1 willing living creature or 1 undead  c |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/26` | 0.504133 | **HARM **[one-action]** TO **[three-actions] **SPELL 1**  **MANIPULATE** **VOID**  **Traditions** divine  **Range **varies; **Targets** 1 living creature or 1 willing undead  creature  You channel voi |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/60` | 0.501738 | **PEST FORM **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Duration** 10 minutes |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/49` | 0.497614 | **EVENT HORIZON **[two-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE** **VOID**  **Traditions** primal  **Range **500 feet;** Area** 50-foot burst **Defense** Reflex; **Duration** 1 minute |

### Query 79
- Text: What does **FORESIGHT **[two-actions] **SPELL 9** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/26', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/26` | 0.651445 | **FORESIGHT **[two-actions] **SPELL 9**  **CONCENTRATE** **MANIPULATE** **MENTAL** **PREDICTION**  **Traditions** arcane, divine, occult **Range **touch;** Targets** 1 creature  **Duration** 1 hour  Y |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.528127 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/8` | 0.518265 | **FEAR **[two-actions] **SPELL 1**  **CONCENTRATE** **EMOTION** **FEAR** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult, primal  **Range **30 feet;** Targets** 1 creature **Defense** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.473619 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.473619 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.473619 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.473619 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/62` | 0.473619 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.473619 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.473619 | **SPELLS** |

### Query 80
- Text: What does **FREEZE TIME **[three-actions] **SPELL 10** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/34', 'PZO22001 Starfinder Player Core 330-363::/page/31/Text/3', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/34` | 0.731530 | **FREEZE TIME **[three-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  You temporarily stop time for everything but yourself,  allowing you to use several actions |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/31/Text/3` | 0.529949 | **SLOW **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 creature **Defense** Fortitude; **Duration** varies  You dila |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/1` | 0.521503 | **HEROISM **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult **Duration** 10 minutes |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/49` | 0.474729 | **EVENT HORIZON **[two-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE** **VOID**  **Traditions** primal  **Range **500 feet;** Area** 50-foot burst **Defense** Reflex; **Duration** 1 minute |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47` | 0.472938 | **REVIVAL **[two-actions] **SPELL 10**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet;** Targets** dead creatures and living creatures of  y |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/15` | 0.472470 | **PARALYZE **[two-actions] **SPELL 3**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature  **Defense** Will; **Durat |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.468924 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.456379 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/18` | 0.455247 | **FELINE SENSES **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MORPH**  **Traditions** divine, primal  **Duration** 1 hour |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/63` | 0.452919 | **EQUIPMENT** **SPELLS** |

### Query 81
- Text: What does **FROSTBITE **[two-actions] **CANTRIP 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/39', 'PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/6', 'PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/39` | 0.754995 | **FROSTBITE **[two-actions] **CANTRIP 1**  **CANTRIP** **COLD** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets** 1 creature  **Defense** Fortitude  An orb |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/6` | 0.578883 | **PRESTIDIGITATION **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **10 feet; **Targets** 1 object (cook, lift, or tid |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/11` | 0.578714 | **FORBIDDING WARD **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** divine, occult  **Range **30 feet; **Targets** 1 ally and 1 enemy  **Duration** sustained up |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/19` | 0.532178 | **STUMBLE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **100 feet; **Targets** 1 creature  **Defense** Reflex  A burst of micrograv |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/5` | 0.529545 | **STABILIZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet; **Targets** 1 dying creature  Life ene |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/33` | 0.523244 | **FIGMENT **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet  **Duration** sustained  You create a simp |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/5/SectionHeader/20` | 0.519202 | **GUIDANCE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE**  **Traditions** divine, occult, primal  **Range **30 feet; **Targets** 1 creature  **Duration** until the start of your next turn |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/37` | 0.497325 | **IGNITION **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Targets** 1 creature  **Defense** AC  You |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/26/Text/12` | 0.488595 | **RICOCHET **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE** **METAL**  **Traditions** arcane, divine  **Range **30 feet; **Targets** 1 or 2 creatures  **Defense** basic Reflex |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/42` | 0.475826 | **SHIELD **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **FORCE**  **Traditions** arcane, divine, occult  **Duration** until the start of your next turn  You raise a magical shield of force |

### Query 82
- Text: What does **GATE **[two-actions] **SPELL 10** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/47']
- Expected found: `True`
- Expected rank: `13`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47', 'PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/49', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/67']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47` | 0.543173 | **REVIVAL **[two-actions] **SPELL 10**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet;** Targets** dead creatures and living creatures of  y |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/49` | 0.535663 | **EVENT HORIZON **[two-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE** **VOID**  **Traditions** primal  **Range **500 feet;** Area** 50-foot burst **Defense** Reflex; **Duration** 1 minute |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.530268 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.488268 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.488268 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/62` | 0.488268 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.488268 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.488268 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.488268 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.488268 | **SPELLS** |

### Query 83
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/55']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/61', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/55', 'PZO22001 Starfinder Player Core 330-363::/page/25/Text/55']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/61` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/55` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/55` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/39` | 0.838541 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/55` | 0.838541 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/56` | 0.838541 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/57` | 0.838541 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/57` | 0.838541 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/62` | 0.838541 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/58` | 0.838541 | **INTRODUCTION** |

### Query 84
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/56']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/62', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/56', 'PZO22001 Starfinder Player Core 330-363::/page/11/Text/59']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/62` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/56` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/59` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/58` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/40` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/63` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/56` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/59` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/58` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/40` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 85
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/57']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/17/Text/41', 'PZO22001 Starfinder Player Core 330-363::/page/13/Text/58', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/63']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/41` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/58` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/63` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/60` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/60` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/57` | 0.910061 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/64` | 0.910061 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/57` | 0.910061 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/57` | 0.910061 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/59` | 0.910061 | **CLASSES** |

### Query 86
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/58']
- Expected found: `True`
- Expected rank: `10`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/19/Text/69', 'PZO22001 Starfinder Player Core 330-363::/page/27/Text/60', 'PZO22001 Starfinder Player Core 330-363::/page/17/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/69` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/60` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/42` | 0.864442 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/65` | 0.822442 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/59` | 0.822442 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/58` | 0.822442 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/61` | 0.822442 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/58` | 0.822442 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/64` | 0.822442 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/58` | 0.822442 | **SKILLS** |

### Query 87
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/59']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/23/Text/66', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/65', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/66` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/65` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/43` | 0.871817 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/60` | 0.829817 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/59` | 0.829817 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/59` | 0.829817 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/70` | 0.829817 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/62` | 0.829817 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/43` | 0.829817 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/62` | 0.829817 | **FEATS** |

### Query 88
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/60']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/66', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/60', 'PZO22001 Starfinder Player Core 330-363::/page/17/Text/44']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/66` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/60` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/44` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/71` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/61` | 0.902726 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/63` | 0.902726 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/67` | 0.902726 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/44` | 0.902726 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/61` | 0.627947 | **FEATS** **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/59` | 0.627947 | **FEATS** **EQUIPMENT** |

### Query 89
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/61']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/45', 'PZO22001 Starfinder Player Core 330-363::/page/17/Text/45', 'PZO22001 Starfinder Player Core 330-363::/page/25/Text/60']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.847304 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.847304 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.847304 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.847304 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/62` | 0.847303 | **SPELLS** |

### Query 90
- Text: What is the rule about **Spell Lists**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/62']
- Expected found: `True`
- Expected rank: `12`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/33/Text/65', 'PZO22001 Starfinder Player Core 330-363::/page/17/Text/46', 'PZO22001 Starfinder Player Core 330-363::/page/15/Text/61']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/65` | 0.890837 | **Spell Lists** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/46` | 0.890837 | **Spell Lists** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/61` | 0.890837 | **Spell Lists** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/70` | 0.848837 | **Spell Lists** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/46` | 0.848837 | **Spell Lists** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/61` | 0.848837 | **Spell Lists** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/65` | 0.848837 | **Spell Lists** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/63` | 0.848837 | **Spell Lists** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/63` | 0.848837 | **Spell Lists** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/63` | 0.848837 | **Spell Lists** |

### Query 91
- Text: What is the rule about **Spells**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/63']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/33/Text/66', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/69', 'PZO22001 Starfinder Player Core 330-363::/page/13/Text/64']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/66` | 0.798799 | **Spells** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/69` | 0.798799 | **Spells** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/64` | 0.798799 | **Spells** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/63` | 0.756799 | **Spells** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/62` | 0.756799 | **Spells** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/62` | 0.756799 | **Spells** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/64` | 0.756799 | **Spells** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/74` | 0.756799 | **Spells** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/66` | 0.756799 | **Spells** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/47` | 0.756799 | **Spells** |

### Query 92
- Text: What is the rule about **Focus Spells**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/64']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/65', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/64', 'PZO22001 Starfinder Player Core 330-363::/page/15/Text/63']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/65` | 0.926221 | **Focus Spells** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/64` | 0.926221 | **Focus Spells** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/63` | 0.926221 | **Focus Spells** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/67` | 0.884221 | **Focus Spells** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/65` | 0.884221 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/75` | 0.884221 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/63` | 0.884221 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/67` | 0.884221 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/65` | 0.884221 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/70` | 0.884221 | **Focus Spells** |

### Query 93
- Text: Summarize **Rituals**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/65']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/65', 'PZO22001 Starfinder Player Core 330-363::/page/23/Text/73', 'PZO22001 Starfinder Player Core 330-363::/page/19/Text/76']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/65` | 0.971114 | **Rituals** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/76` | 0.971114 | **Rituals** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/73` | 0.971114 | **Rituals** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/64` | 0.929114 | **Rituals** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/68` | 0.929113 | **Rituals** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/48` | 0.929113 | **Rituals** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/66` | 0.929113 | **Rituals** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/66` | 0.929113 | **Rituals** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/66` | 0.929113 | **Rituals** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/71` | 0.929113 | **Rituals** |

### Query 94
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/66']
- Expected found: `True`
- Expected rank: `11`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/49', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/67', 'PZO22001 Starfinder Player Core 330-363::/page/15/Text/65']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/49` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/67` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/65` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/72` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/77` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/49` | 0.923000 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/69` | 0.923000 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/67` | 0.923000 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/74` | 0.923000 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/67` | 0.923000 | **PLAYING THE ** **GAME** |

### Query 95
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/67']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/33/Text/70', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/68', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/67']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/70` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/68` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/67` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/73` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/50` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/66` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/71` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/78` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/68` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/51` | 0.769880 | **APPENDIX** |

### Query 96
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/3/Text/68']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/33/Text/71', 'PZO22001 Starfinder Player Core 330-363::/page/17/Text/51', 'PZO22001 Starfinder Player Core 330-363::/page/13/Text/69']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/71` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/51` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/69` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/68` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/74` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/67` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/52` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/69` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/77` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/72` | 0.951465 | **GLOSSARY & ** **INDEX** |

### Query 97
- Text: Summarize or out of the realm of a deity or another similarly powerful  being, that being can prevent the gate from forming.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/4/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/4/Text/1', 'PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/47', 'PZO22001 Starfinder Player Core 330-363::/page/28/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/4/Text/1` | 1.022495 | or out of the realm of a deity or another similarly powerful  being, that being can prevent the gate from forming. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/47` | 0.517877 | **GATE **[two-actions] **SPELL 10**  **UNCOMMON** **CONCENTRATE** **MANIPULATE** **TELEPORTATION**  **Traditions** arcane, divine, occult  **Range **120 feet  **Duration** sustained up to 1 minute  Yo |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/9` | 0.486667 | **Critical Failure** The creature falls off the stone (if applicable)  and lands prone. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/8` | 0.454117 | **Failure** The creature falls prone atop the stone. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/18` | 0.423517 | **Failure** The creature can't move closer to you within the area. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/24/Text/2` | 0.416735 | The squares at the outside vertical edges of the cylinder  prevent creatures from leaving. These squares are greater  difficult terrain, and a creature attempting to push through  must succeed at an A |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/10` | 0.411680 | **Failure** The creature is knocked prone. If it was flying, it takes  the effects of critical failure instead. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/52` | 0.401601 | **Failure** The creature takes full damage and is pushed 5 feet  away from you. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/20/Text/9` | 0.399609 | **Force Body** A phantasmal minion's body is made of  magical force. It can't use attack actions. Though it  has no physical weight, it can move and use Interact  actions to do things such as fetch ob |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/9` | 0.389189 | **REPULSION **[two-actions] **SPELL 6**  **AURA** **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult  **Area** emanation up to 40 feet  **Defense** Will; **Duration** 1 m |

### Query 98
- Text: What does **GENETIC REGENERATION **[two-actions] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/2', 'PZO22001 Starfinder Player Core 330-363::/page/24/SectionHeader/35', 'PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/2` | 0.690625 | **GENETIC REGENERATION **[two-actions] **SPELL 4**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **touch;** Targets** 1 willing creature **Duration** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/24/SectionHeader/35` | 0.561939 | **REGENERATE **[two-actions] **SPELL 7**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **touch;** Targets** 1 willing living creature  **Duration** 1 |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47` | 0.536101 | **REVIVAL **[two-actions] **SPELL 10**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet;** Targets** dead creatures and living creatures of  y |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.492241 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.454064 | **LIFE SEAL **[reaction] **SPELL 3** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.445364 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.445364 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.445364 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.445364 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.445364 | **SPELLS** |

### Query 99
- Text: What does **GENTLE LANDING **[reaction] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/10', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/42', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/61']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/10` | 0.634765 | **GENTLE LANDING **[reaction] **SPELL 1**  **AIR** **CONCENTRATE**  **Traditions** arcane, primal  **Trigger** A creature within range is falling. **Range **60 feet;** Targets** 1 falling creature  ** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.591343 | **LIFE SEAL **[reaction] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.588304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.546304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.546304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.546304 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.546304 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.546304 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.546304 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.546304 | **SPELLS** |

### Query 100
- Text: What does **GHOSTLY CARRIER **[two-actions] **SPELL 2** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/17', 'PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/23', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/17` | 0.704362 | **GHOSTLY CARRIER **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet **Duration** 1 minute  You create a Tiny, semi-corporeal figure with a |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/23` | 0.592650 | **GHOST KILLER WEAPON **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 weapon that's either unattended or  wielded by you or a |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.570322 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/18/SectionHeader/45` | 0.516712 | **OUTCAST'S CURSE **[two-actions] **SPELL 4**  **CONCENTRATE** **CURSE** **MANIPULATE** **MENTAL** **MISFORTUNE**  **Traditions** arcane, divine, occult **Range **touch;** Targets** 1 creature  **Defe |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.507942 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.490449 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.490449 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.490449 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.490449 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.490449 | **SPELLS** |

### Query 101
- Text: What does **GHOST KILLER WEAPON **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/23', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/23` | 0.766365 | **GHOST KILLER WEAPON **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 weapon that's either unattended or  wielded by you or a |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.622213 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.583019 | **LIFE SEAL **[reaction] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/60` | 0.530859 | **EQUIPMENT** **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/63` | 0.530859 | **EQUIPMENT** **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/61` | 0.530859 | **EQUIPMENT** **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/1` | 0.508453 | **HEROISM **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult **Duration** 10 minutes |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.507322 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/36` | 0.506073 | **HASTE **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Range **30 feet;** Targets** 1 creature  **Duration** 1 minute  Magic empowers the target |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/35` | 0.505658 | **PROTECTION **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** divine, occult  **Range **touch;** Targets** 1 willing creature  **Duration** 1 minute  You ward a creature aga |

### Query 102
- Text: What does **GLOW UP **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/30', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/30` | 0.646354 | **GLOW UP **[two-actions] **SPELL 1**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **VISUAL**  **Traditions** arcane, occult, primal  **Range **30 feet;** Targets** 1 willing creature  **Duration** 1 |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.561096 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.559934 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.506572 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.506572 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.506572 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.506572 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.506572 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.506572 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.506572 | **SPELLS** |

### Query 103
- Text: What does **GOUGING CLAW **[two-actions] **CANTRIP 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/39', 'PZO22001 Starfinder Player Core 330-363::/page/5/SectionHeader/20', 'PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/39` | 0.798813 | **GOUGING CLAW **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **MANIPULATE** **MORPH**  **Traditions** arcane, primal **Range **touch; **Targets** 1 creature  **Defense** AC  Yo |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/5/SectionHeader/20` | 0.576008 | **GUIDANCE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE**  **Traditions** divine, occult, primal  **Range **30 feet; **Targets** 1 creature  **Duration** until the start of your next turn |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/6` | 0.566598 | **PRESTIDIGITATION **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **10 feet; **Targets** 1 object (cook, lift, or tid |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/33` | 0.524013 | **FIGMENT **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet  **Duration** sustained  You create a simp |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/37` | 0.502865 | **IGNITION **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Targets** 1 creature  **Defense** AC  You |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/19` | 0.499152 | **STUMBLE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **100 feet; **Targets** 1 creature  **Defense** Reflex  A burst of micrograv |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/11` | 0.497683 | **FORBIDDING WARD **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** divine, occult  **Range **30 feet; **Targets** 1 ally and 1 enemy  **Duration** sustained up |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/29/Text/7` | 0.492328 | **SIGIL **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal **Range **touch; **Targets** 1 creature or object **Duration** unlimite |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/26/Text/12` | 0.481061 | **RICOCHET **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE** **METAL**  **Traditions** arcane, divine  **Range **30 feet; **Targets** 1 or 2 creatures  **Defense** basic Reflex |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/39` | 0.478368 | **FROSTBITE **[two-actions] **CANTRIP 1**  **CANTRIP** **COLD** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **60 feet; **Targets** 1 creature  **Defense** Fortitude  An orb |

### Query 104
- Text: What does **GRAVITY FIELD **[three-actions] **SPELL 8** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/46']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/46', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21', 'PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/54']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/4/SectionHeader/46` | 0.703605 | **GRAVITY FIELD **[three-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **100 feet; **Area** 30-foot radius, 100-foot-tall cylinder  **Dur |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.545069 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/54` | 0.536061 | **PERSONAL GRAVITY **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Duration** 1 hour  You alter gravity's effects on you. You treat gravity as if |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/30/Text/1` | 0.493898 | **SINGULARITY SEED **[three-actions] **SPELL 8**  **CONCENTRATE** **MANIPULATE** **VOID**  **Traditions** divine, primal  **Range **100 feet; **Area** one 5-foot square and one 50-foot  emanation surr |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.460194 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.460194 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.460194 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.460194 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.460194 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.460194 | **SPELLS** |

### Query 105
- Text: What does **GRIM TENDRILS **[two-actions] **SPELL 1** **CONCENTRATE** **MANIPULATE** **VOID** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/32', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/2` | 0.712533 | **GRIM TENDRILS **[two-actions] **SPELL 1** **CONCENTRATE** **MANIPULATE** **VOID**  **Traditions** arcane, occult  **Area** 30-foot line  **Defense** Fortitude  Tendrils of darkness curl out from you |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.606123 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/18` | 0.577267 | **FELINE SENSES **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MORPH**  **Traditions** divine, primal  **Duration** 1 hour |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/5` | 0.528377 | **CONCENTRATE** **MANIPULATE** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/60` | 0.522694 | **PEST FORM **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Duration** 10 minutes |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/1` | 0.510902 | **HEROISM **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult **Duration** 10 minutes |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/27/SectionHeader/42` | 0.508343 | **SENDING **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult  **Range **planetary;** Targets** 1 creature you know well  You send the creat |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/49` | 0.496278 | **EVENT HORIZON **[two-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE** **VOID**  **Traditions** primal  **Range **500 feet;** Area** 50-foot burst **Defense** Reflex; **Duration** 1 minute |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47` | 0.493754 | **REVIVAL **[two-actions] **SPELL 10**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet;** Targets** dead creatures and living creatures of  y |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/36` | 0.479190 | **HASTE **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Range **30 feet;** Targets** 1 creature  **Duration** 1 minute  Magic empowers the target |

### Query 106
- Text: Summarize **Critical Success** The creature is unaffected.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/7']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/30/Text/38', 'PZO22001 Starfinder Player Core 330-363::/page/28/Text/30']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/2` | 1.018921 | **Critical Success** The creature is unaffected. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/30/Text/38` | 1.018921 | **Critical Success** The creature is unaffected. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/30` | 1.018921 | **Critical Success** The creature is unaffected. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/7` | 0.976921 | **Critical Success** The creature is unaffected. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/8` | 0.976921 | **Critical Success** The creature is unaffected. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/20` | 0.976921 | **Critical Success** The creature is unaffected. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/14` | 0.976921 | **Critical Success** The creature is unaffected. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/50` | 0.976921 | **Critical Success** The creature is unaffected. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/19` | 0.976921 | **Critical Success** The creature is unaffected. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/30/Text/11` | 0.976004 | **Critical Success **The creature is unaffected. |

### Query 107
- Text: What is the rule about **Success** The creature takes half the void damage and no  persistent bleed damage.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/8', 'PZO22001 Starfinder Player Core 330-363::/page/5/Text/10', 'PZO22001 Starfinder Player Core 330-363::/page/28/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/8` | 0.854847 | **Success** The creature takes half the void damage and no  persistent bleed damage. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/10` | 0.740333 | **Critical Failure** The creature takes double void damage and  double persistent bleed damage. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/31` | 0.682576 | **Success** The creature takes half damage. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/51` | 0.640576 | **Success** The creature takes half damage. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/20` | 0.640576 | **Success** The creature takes half damage. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/16` | 0.622193 | **Failure** The creature takes 100 void damage. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/9` | 0.612537 | **Failure** The creature takes full damage. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/3` | 0.601510 | **Success** The creature takes half damage and is slowed 1 until  the end of its next turn. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/15` | 0.597645 | **Success** The creature takes 9d6 void damage. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/30` | 0.596846 | **Critical Success** The creature is unaffected. |

### Query 108
- Text: What is the rule about **Failure** The creature takes full damage.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/9', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/4', 'PZO22001 Starfinder Player Core 330-363::/page/23/Text/52']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/9` | 0.896288 | **Failure** The creature takes full damage. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/4` | 0.765262 | **Failure** The creature takes full damage, is slowed 3 until the  end of its next turn, and slowed 1 for 1 minute. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/52` | 0.751990 | **Failure** The creature takes full damage and is pushed 5 feet  away from you. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/26/Text/48` | 0.709765 | **Failure** The creature can't attack the target and wastes the  action. It can't attempt further attacks against the target  this turn. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/21` | 0.689030 | **Failure** The creature takes full damage and is deafened for  1 round. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/32` | 0.682888 | **Failure** The creature takes full damage and is clumsy 1 for 1  minute. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/16` | 0.682545 | **Failure** The creature takes 100 void damage. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/10` | 0.673767 | **Failure** The creature is knocked prone. If it was flying, it takes  the effects of critical failure instead. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/17` | 0.668320 | **Critical Failure** The creature dies. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/5` | 0.653911 | **Critical Failure** The creature becomes frightened 2, and its  action fails and is wasted. |

### Query 109
- Text: What is the rule about **Critical Failure** The creature takes double void damage and  double persistent bleed damage.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/10', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/41', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/10` | 0.937836 | **Critical Failure** The creature takes double void damage and  double persistent bleed damage. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/41` | 0.773992 | **Critical Failure** As failure, but the target takes double the  initial and persistent damage. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/5` | 0.738355 | **Critical Failure** The creature takes double damage, is slowed  3 until the end of its next turn, and slowed 2 for 1 minute. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/17` | 0.682734 | **Critical Failure** The creature dies. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/5` | 0.681329 | **Critical Failure** The creature becomes frightened 2, and its  action fails and is wasted. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/16` | 0.646721 | **Failure** The creature takes 100 void damage. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/53` | 0.642548 | **Critical Failure** The creature takes double damage and is  pushed 10 feet away from you. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/22` | 0.633755 | **Critical Failure** The creature takes double damage, is  deafened for 1 minute, and is stunned 1. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/9` | 0.627762 | **Failure** The creature takes full damage. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/10` | 0.621728 | **Failure** The creature is knocked prone. If it was flying, it takes  the effects of critical failure instead. |

### Query 110
- Text: What is the rule about **Heightened (+1)** The void damage increases by 2d4, and the  persistent bleed damage increases by 1.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/11', 'PZO22001 Starfinder Player Core 330-363::/page/23/Text/54', 'PZO22001 Starfinder Player Core 330-363::/page/18/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/11` | 0.916703 | **Heightened (+1)** The void damage increases by 2d4, and the  persistent bleed damage increases by 1. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/54` | 0.800177 | **Heightened (+1)** The damage increases by 2d4. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/23` | 0.755997 | **Heightened (+1)** The damage increases by 1d10. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/2` | 0.705879 | **Heightened (+1)** The damage increases by 1d6. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/6` | 0.634158 | **Heightened (+1)** The damage of the image's Strikes increases  by 1d4, and the maximum size of creature you can create  increases by one (to a maximum of Gargantuan). |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/31` | 0.583901 | **Heightened (5th)** Your battle form is Huge, and your attacks  have 15-foot reach. You instead gain 20 temporary HP,  attack modifier +18, damage bonus +2 and double damage  dice (including persiste |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/16/Text/9` | 0.575790 | **Heightened (9th)** You instead gain AC = 22 + your level, 25  temporary HP, attack modifier +31, increase damage by  one damage die, and Athletics +33. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/18` | 0.575778 | **Heightened (10th)** The spell can affect living creatures up to  19th level. Increase the damage to 10d6 on a success, and  to 115 on a failure. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/30` | 0.569465 | **Heightened (4th)** Your battle form is Large, and your attacks  have 10-foot reach. You instead gain 15 temporary HP,  attack modifier +16, damage bonus +6, and Athletics +16. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/22/Text/29` | 0.562712 | **Heightened (6th)** Your battle form is Huge, and the reach of  your attacks increases by 5 feet. You instead gain AC = 22  + your level, 24 temporary HP, attack modifier +21, damage  bonus +16, and |

### Query 111
- Text: What does **GREASE **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/12', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/62', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/45']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/12` | 0.627355 | **GREASE **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet;** Area** 4 contiguous 5-foot squares or** Targets** 1  object of 1 Bulk or less |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.587125 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.587125 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.545125 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.545125 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.545125 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.545125 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/62` | 0.545125 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.545125 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.545125 | **SPELLS** |

### Query 112
- Text: What does **GUIDANCE **[one-action] **CANTRIP 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/5/SectionHeader/20', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/33', 'PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/5/SectionHeader/20` | 0.748851 | **GUIDANCE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE**  **Traditions** divine, occult, primal  **Range **30 feet; **Targets** 1 creature  **Duration** until the start of your next turn |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/33` | 0.607287 | **FIGMENT **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet  **Duration** sustained  You create a simp |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/6` | 0.599001 | **PRESTIDIGITATION **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, divine, occult, primal  **Range **10 feet; **Targets** 1 object (cook, lift, or tid |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/14/SectionHeader/19` | 0.550400 | **MEASURE **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE**  **Traditions** arcane, divine, occult, primal  **Area** 200-foot emanation  **Duration** sustained up to 1 minute  You learn the ap |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/5` | 0.531534 | **STABILIZE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet; **Targets** 1 dying creature  Life ene |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/37` | 0.531313 | **IGNITION **[two-actions] **CANTRIP 1**  **ATTACK** **CANTRIP** **CONCENTRATE** **FIRE** **MANIPULATE**  **Traditions** arcane, primal  **Range **30 feet; **Targets** 1 creature  **Defense** AC  You |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/3` | 0.522536 | **REORIENT **[one-action] **CANTRIP 1**  **CONCENTRATE** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **touch; **Targets** 1 creature  Applying a combination of vital energy and |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/33/SectionHeader/19` | 0.520339 | **STUMBLE **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Range **100 feet; **Targets** 1 creature  **Defense** Reflex  A burst of micrograv |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/11` | 0.519774 | **FORBIDDING WARD **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **MANIPULATE**  **Traditions** divine, occult  **Range **30 feet; **Targets** 1 ally and 1 enemy  **Duration** sustained up |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/42` | 0.515423 | **SHIELD **[one-action] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **FORCE**  **Traditions** arcane, divine, occult  **Duration** until the start of your next turn  You raise a magical shield of force |

### Query 113
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/28']
- Expected found: `True`
- Expected rank: `14`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/61', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/55', 'PZO22001 Starfinder Player Core 330-363::/page/25/Text/55']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/61` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/55` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/55` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/39` | 0.838541 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/55` | 0.838541 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/56` | 0.838541 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/57` | 0.838541 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/57` | 0.838541 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/62` | 0.838541 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/58` | 0.838541 | **INTRODUCTION** |

### Query 114
- Text: Summarize **ANCESTRIES & **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/29', 'PZO22001 Starfinder Player Core 330-363::/page/23/Text/63', 'PZO22001 Starfinder Player Core 330-363::/page/33/Text/59']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/29` | 0.992902 | **ANCESTRIES & ** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/63` | 0.838259 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/59` | 0.838259 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/67` | 0.808259 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/62` | 0.808259 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/58` | 0.808259 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/40` | 0.808259 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/58` | 0.808259 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/57` | 0.808259 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/56` | 0.808259 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 115
- Text: Summarize **GLOSSARY & **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/5/Text/34', 'PZO22001 Starfinder Player Core 330-363::/page/19/Text/79', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/68']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/34` | 0.986628 | **GLOSSARY & ** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/79` | 0.986628 | **GLOSSARY & ** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/68` | 0.872894 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/52` | 0.830894 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/72` | 0.830894 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/69` | 0.830894 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/74` | 0.830894 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/67` | 0.830894 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/67` | 0.830894 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/71` | 0.830894 | **GLOSSARY & ** **INDEX** |

### Query 116
- Text: What does **GUST OF WIND **[two-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/6/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/6/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/45', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/62']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/2` | 0.740889 | **GUST OF WIND **[two-actions] **SPELL 1**  **AIR** **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, primal  **Area** 60-foot line  **Defense** Fortitude; **Duration** until the start of your ne |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.563249 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.563249 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.521249 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.521249 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.521249 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.521249 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.521249 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.521249 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.521249 | **SPELLS** |

### Query 117
- Text: What is the rule about **Critical Failure** The creature is pushed 30 feet in the wind's  direction, knocked prone, and takes 2d6 bludgeoning damage.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/6/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/6/Text/11', 'PZO22001 Starfinder Player Core 330-363::/page/6/Text/10', 'PZO22001 Starfinder Player Core 330-363::/page/14/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/11` | 0.912772 | **Critical Failure** The creature is pushed 30 feet in the wind's  direction, knocked prone, and takes 2d6 bludgeoning damage. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/10` | 0.777912 | **Failure** The creature is knocked prone. If it was flying, it takes  the effects of critical failure instead. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/5` | 0.741282 | **Critical Failure** The creature becomes frightened 2, and its  action fails and is wasted. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/9` | 0.690946 | **Critical Failure** The creature falls off the stone (if applicable)  and lands prone. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/5` | 0.689702 | **Critical Failure** The creature takes double damage, is slowed  3 until the end of its next turn, and slowed 2 for 1 minute. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/53` | 0.677530 | **Critical Failure** The creature takes double damage and is  pushed 10 feet away from you. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/30/Text/14` | 0.668555 | **Critical Failure **The creature is pulled 30 feet toward the  singularity. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/17` | 0.659482 | **Critical Failure** The creature dies. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/33` | 0.641137 | **Critical Failure** The creature takes full damage and is clumsy  2 for 1 minute. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/22` | 0.631852 | **Critical Failure** The creature takes double damage, is  deafened for 1 minute, and is stunned 1. |

### Query 118
- Text: What does **HALLUCINATION **[two-actions] **SPELL 5** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/6/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/6/Text/12', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/32', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/12` | 0.670066 | **HALLUCINATION **[two-actions] **SPELL 5**  **ILLUSION** **INCAPACITATION** **MANIPULATE** **MENTAL** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet; **Targets** 1 creature  **Duration* |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.613303 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.578245 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/1` | 0.530866 | **HEROISM **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult **Duration** 10 minutes |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/27/SectionHeader/42` | 0.511792 | **SENDING **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult  **Range **planetary;** Targets** 1 creature you know well  You send the creat |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/11/SectionHeader/51` | 0.491480 | **INVISIBILITY **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/0/SectionHeader/49` | 0.484862 | **EVENT HORIZON **[two-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE** **VOID**  **Traditions** primal  **Range **500 feet;** Area** 50-foot burst **Defense** Reflex; **Duration** 1 minute |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/4` | 0.482082 | **HONEYED WORDS **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes  You unlock the |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47` | 0.477172 | **REVIVAL **[two-actions] **SPELL 10**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet;** Targets** dead creatures and living creatures of  y |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/2/SectionHeader/1` | 0.475866 | **FALSE VITALITY **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Duration** 8 hours  You augment your flesh with the energies typically used to  manipulat |

### Query 119
- Text: What is the rule about **Heightened (6th)** Choose to either target up to 10 creatures  or change the spell's duration to until your next daily  preparations.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/6/Text/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/6/Text/24', 'PZO22001 Starfinder Player Core 330-363::/page/2/Text/25', 'PZO22001 Starfinder Player Core 330-363::/page/6/Text/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/24` | 0.964170 | **Heightened (6th)** Choose to either target up to 10 creatures  or change the spell's duration to until your next daily  preparations. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/25` | 0.822971 | **Heightened (6th)** The spell's range is touch and it targets 1 willing  creature. The duration is until your next daily preparations. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/25` | 0.819029 | **Heightened (8th)** Choose to either target any number of  creatures or change the spell's duration to unlimited. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/51` | 0.736845 | **Heightened (10th)** You can target up to 10 additional  creatures to gain protection against the environment the  triggering creature entered. The spell lasts until your next  daily preparations and |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/50` | 0.716914 | **Heightened (7th)** You can target up to 5 additional creatures  to gain protection against the environment the triggering  creature entered. The spell lasts for 8 hours and also  protects against ex |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/34` | 0.709777 | **Heightened (6th)** The spell targets up to four creatures and  deals 6d12 mental damage. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/18` | 0.679946 | **Heightened (10th)** The spell can affect living creatures up to  19th level. Increase the damage to 10d6 on a success, and  to 115 on a failure. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/6` | 0.658209 | **Heightened (8th)** You can target up to 5 creatures. If a  creature uses a hostile action or reaction that affects  multiple targets simultaneously, it needs to attempt only  one save against *mask |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/5` | 0.643220 | **Heightened (9th)** The duration is 10 minutes, and you can  physically enter the creature's body, protecting your  physical body while the spell lasts. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/24` | 0.637447 | **Heightened (4th)** The spell's range is touch and it targets 1  willing creature. |

### Query 120
- Text: What is the rule about **Heightened (8th)** Choose to either target any number of  creatures or change the spell's duration to unlimited.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/6/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/6/Text/25', 'PZO22001 Starfinder Player Core 330-363::/page/6/Text/24', 'PZO22001 Starfinder Player Core 330-363::/page/14/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/25` | 0.961611 | **Heightened (8th)** Choose to either target any number of  creatures or change the spell's duration to unlimited. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/24` | 0.809250 | **Heightened (6th)** Choose to either target up to 10 creatures  or change the spell's duration to until your next daily  preparations. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/6` | 0.748665 | **Heightened (8th)** You can target up to 5 creatures. If a  creature uses a hostile action or reaction that affects  multiple targets simultaneously, it needs to attempt only  one save against *mask |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/50` | 0.693548 | **Heightened (7th)** You can target up to 5 additional creatures  to gain protection against the environment the triggering  creature entered. The spell lasts for 8 hours and also  protects against ex |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/25` | 0.665630 | **Heightened (6th)** The spell's range is touch and it targets 1 willing  creature. The duration is until your next daily preparations. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/10/Text/4` | 0.657221 | **Heightened (8th)** As the 6th-rank version, and the duration  is unlimited. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/51` | 0.652905 | **Heightened (10th)** You can target up to 10 additional  creatures to gain protection against the environment the  triggering creature entered. The spell lasts until your next  daily preparations and |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/24` | 0.632760 | **Heightened (4th)** The spell's range is touch and it targets 1  willing creature. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/2` | 0.625410 | **Heightened (4th)** The spell lasts 1 minute, but it doesn't end if  the target uses a hostile action. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/5` | 0.620441 | **Heightened (9th)** The duration is 10 minutes, and you can  physically enter the creature's body, protecting your  physical body while the spell lasts. |

### Query 121
- Text: What does **HARM **[one-action]** TO **[three-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/6/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/6/Text/26', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/26` | 0.652963 | **HARM **[one-action]** TO **[three-actions] **SPELL 1**  **MANIPULATE** **VOID**  **Traditions** divine  **Range **varies; **Targets** 1 living creature or 1 willing undead  creature  You channel voi |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.605212 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.593654 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/1` | 0.546371 | **HEROISM **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult **Duration** 10 minutes |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/44` | 0.525649 | **HEAL **[one-action]** TO **[three-actions] **SPELL 1**  **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **varies; **Targets** 1 willing living creature or 1 undead  c |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/27/SectionHeader/42` | 0.513997 | **SENDING **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult  **Range **planetary;** Targets** 1 creature you know well  You send the creat |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/4` | 0.507186 | **HONEYED WORDS **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes  You unlock the |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/35` | 0.504423 | **PROTECTION **[two-actions] **SPELL 1**  **CONCENTRATE** **MANIPULATE**  **Traditions** divine, occult  **Range **touch;** Targets** 1 willing creature  **Duration** 1 minute  You ward a creature aga |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/8` | 0.492236 | **FEAR **[two-actions] **SPELL 1**  **CONCENTRATE** **EMOTION** **FEAR** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult, primal  **Range **30 feet;** Targets** 1 creature **Defense** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/19` | 0.491453 | **FORCE BARRAGE **[one-action]** TO **[three-actions] **SPELL 1**  **CONCENTRATE** **FORCE** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet;** Targets** 1 creature  You fire a shard |

### Query 122
- Text: What does **HASTE **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/6/Text/36']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21', 'PZO22001 Starfinder Player Core 330-363::/page/6/Text/36', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.666139 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/36` | 0.644953 | **HASTE **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal  **Range **30 feet;** Targets** 1 creature  **Duration** 1 minute  Magic empowers the target |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.611495 | **LIFE SEAL **[reaction] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/62` | 0.540039 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.540039 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.540039 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.540039 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.540039 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.540039 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.540039 | **SPELLS** |

### Query 123
- Text: What does **HEAL **[one-action]** TO **[three-actions] **SPELL 1** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/6/Text/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/6/Text/44', 'PZO22001 Starfinder Player Core 330-363::/page/6/Text/26', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/44` | 0.701306 | **HEAL **[one-action]** TO **[three-actions] **SPELL 1**  **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **varies; **Targets** 1 willing living creature or 1 undead  c |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/26` | 0.629735 | **HARM **[one-action]** TO **[three-actions] **SPELL 1**  **MANIPULATE** **VOID**  **Traditions** divine  **Range **varies; **Targets** 1 living creature or 1 willing undead  creature  You channel voi |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.628325 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/1` | 0.559885 | **HEROISM **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult **Duration** 10 minutes |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/47` | 0.552081 | **REVIVAL **[two-actions] **SPELL 10**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **30 feet;** Targets** dead creatures and living creatures of  y |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.541495 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/24/SectionHeader/35` | 0.529100 | **REGENERATE **[two-actions] **SPELL 7**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, primal  **Range **touch;** Targets** 1 willing living creature  **Duration** 1 |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.513446 | **LIFE SEAL **[reaction] **SPELL 3** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/27/SectionHeader/42` | 0.511826 | **SENDING **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult  **Range **planetary;** Targets** 1 creature you know well  You send the creat |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/32/Text/2` | 0.509052 | **SOUND BODY **[two-actions] **SPELL 2**  **CONCENTRATE** **HEALING** **MANIPULATE** **VITALITY**  **Traditions** divine, occult, primal  **Range **touch; **Targets** 1 willing creature  You send a su |

### Query 124
- Text: What does **HEROISM **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/1', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/42', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/1` | 0.759664 | **HEROISM **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult **Duration** 10 minutes |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.614335 | **LIFE SEAL **[reaction] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.612369 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.539764 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.539764 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/62` | 0.539764 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.539764 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.539764 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.539764 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.539764 | **SPELLS** |

### Query 125
- Text: What does **HONEYED WORDS **[two-actions] **SPELL 4** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/4', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/32', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/67']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/4` | 0.631983 | **HONEYED WORDS **[two-actions] **SPELL 4**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **touch;** Targets** 1 creature  **Duration** 10 minutes  You unlock the |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.575040 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.553577 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.511577 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.511577 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.511577 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.511577 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.511577 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.511577 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.511577 | **SPELLS** |

### Query 126
- Text: What does **HOLOGRAPHIC MEMORY **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/13', 'PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/13` | 0.692778 | **HOLOGRAPHIC MEMORY **[two-actions] **SPELL 3**  **UNCOMMON** **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **touch;** Targets** 1 creature or corpse  **Defense** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.651827 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/1` | 0.625290 | **HEROISM **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult **Duration** 10 minutes |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.565292 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.516095 | **LIFE SEAL **[reaction] **SPELL 3** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/26/Text/2` | 0.508241 | **REWRITE MEMORY **[two-actions] **SPELL 4**  **UNCOMMON** **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult  **Range **30 feet; **Targets** 1 creature **Defense** Will; **Duration** un |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/18` | 0.502066 | **FELINE SENSES **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MORPH**  **Traditions** divine, primal  **Duration** 1 hour |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/27/SectionHeader/42` | 0.485408 | **SENDING **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult  **Range **planetary;** Targets** 1 creature you know well  You send the creat |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/15/SectionHeader/3` | 0.483866 | **MIND READING **[two-actions] **SPELL 3**  **UNCOMMON** **CONCENTRATE** **DETECTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature  **Defense** W |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/31/Text/3` | 0.480628 | **SLOW **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult, primal **Range **30 feet;** Targets** 1 creature **Defense** Fortitude; **Duration** varies  You dila |

### Query 127
- Text: What does **HOLY LIGHT **[two-actions] **SPELL 3** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/21', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/1', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/21` | 0.687074 | **HOLY LIGHT **[two-actions] **SPELL 3**  **ATTACK** **CONCENTRATE** **FIRE** **HOLY** **LIGHT** **MANIPULATE**  **Traditions** divine, primal  **Range **120 feet;** Targets** 1 creature  **Defense** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/1` | 0.619508 | **HEROISM **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult **Duration** 10 minutes |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/42` | 0.598131 | **LIFE SEAL **[reaction] **SPELL 3** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.553995 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/8/SectionHeader/21` | 0.535455 | **HYPERCOGNITION **[one-action] **SPELL 3** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.510542 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.510542 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/62` | 0.510542 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.510542 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.510542 | **SPELLS** |

### Query 128
- Text: What does **HOWL **[two-actions] **SPELL 7** do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/32', 'PZO22001 Starfinder Player Core 330-363::/page/27/Text/62', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/67']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/32` | 0.776933 | **HOWL **[two-actions] **SPELL 7**  **AUDITORY** **CONCENTRATE** **MANIPULATE** **MENTAL** **SONIC** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/62` | 0.497990 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.497990 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.455990 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.455990 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.455990 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.455990 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.455990 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.455990 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.455990 | **SPELLS** |

### Query 129
- Text: What does **Traditions** divine, occult, primal do?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/34', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/45', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/34` | 0.936405 | **Traditions** divine, occult, primal |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/45` | 0.893087 | **Traditions** divine, primal |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/6` | 0.869684 | **Traditions** arcane, divine, occult, primal |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/24` | 0.794318 | **Traditions** occult |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/66` | 0.477535 | **Rituals** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/71` | 0.477535 | **Rituals** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/65` | 0.477535 | **Rituals** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/48` | 0.477535 | **Rituals** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/68` | 0.477535 | **Rituals** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/73` | 0.477535 | **Rituals** |

### Query 130
- Text: What is the rule about You let out a powerful ululation full of psychic resonance that  compels others who hear it to join in. You deal 7d12 sonic  damage and 1d8 persistent mental damage to other creatures  who can hear within the area. Targets must attempt a Will  save. The persistent mental damage a creature takes from  this spell increases by 1d8 if at least one other creature is  howling. A howling creature can't use auditory actions or  cast spells except for those with the subtle trait for 1 round.  Calculate the persistent damage after all creatures attempt  their saves.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/37', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/40', 'PZO22001 Starfinder Player Core 330-363::/page/0/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/37` | 1.004768 | You let out a powerful ululation full of psychic resonance that  compels others who hear it to join in. You deal 7d12 sonic  damage and 1d8 persistent mental damage to other creatures  who can hear wi |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/40` | 0.666353 | **Failure** The target takes full damage, persistent mental  damage, and is compelled to howl as long as it takes  persistent mental damage. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/20` | 0.608045 | **ENTHRALL **[two-actions] **SPELL 3**  **AUDITORY** **CONCENTRATE** **EMOTION** **MANIPULATE**  **Traditions** arcane, occult  **Range **120 feet;** Targets** all creatures in range  **Defense** Will |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/21/SectionHeader/8` | 0.565207 | **PHANTOM PAIN **[two-actions] **SPELL 1**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL** **NONLETHAL**  **Traditions** occult  **Range **30 feet; **Targets** 1 creature **Defense** Will; **D |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/4` | 0.551723 | The illusion can cause damage by making the target believe  the illusion's attacks are real, but it cannot otherwise directly  affect the physical world. If the illusory creature hits with a  Strike, |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/13` | 0.543943 | **HOLOGRAPHIC MEMORY **[two-actions] **SPELL 3**  **UNCOMMON** **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **touch;** Targets** 1 creature or corpse  **Defense** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/19/SectionHeader/26` | 0.543931 | **PARANOIA **[two-actions] **SPELL 2**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** occult  **Range **30 feet; **Targets** 1 creature **Defense** Will; **Duration** 1 minute |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/29/SectionHeader/14` | 0.538675 | **SILENCE **[two-actions] **SPELL 2**  **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** divine, occult  **Range **touch;** Targets** 1 willing creature  **Duration** 1 minute  The target makes n |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/23` | 0.536427 | **SHARE PAIN **[two-actions] **SPELL 3**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **30 feet;** Targets** 1 creature  **Defense** Will  You telepathically shar |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/15/SectionHeader/3` | 0.532470 | **MIND READING **[two-actions] **SPELL 3**  **UNCOMMON** **CONCENTRATE** **DETECTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature  **Defense** W |

### Query 131
- Text: What is the rule about Falsehoods pass your lips as smoothly as silk. You gain a  +4 status bonus to Deception checks to Lie and against  Perception checks to discern if you are telling the truth, and  you add your level even if untrained. If the implausibility of  your lies prompts a circumstance penalty or a DC increase,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/73']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/73', 'PZO22001 Starfinder Player Core 330-363::/page/8/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/15/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/73` | 0.995872 | Falsehoods pass your lips as smoothly as silk. You gain a  +4 status bonus to Deception checks to Lie and against  Perception checks to discern if you are telling the truth, and  you add your level ev |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/2` | 0.597017 | *Humanoid form* grants you a +4 status bonus to Deception  checks to pass as a generic member of the chosen ancestry,  and you add your level even if you're untrained, but you  can't make yourself loo |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/2` | 0.569012 | **Critical Failure** As failure, and the target takes a –4  circumstance penalty to Deception checks against your  questions. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/1` | 0.538087 | **Failure** Each round of the spell's duration, you can Sustain the  spell to ask a different question and attempt to uncover  the answer. For each question, the target can attempt  a Deception check |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/15/SectionHeader/27` | 0.477716 | **MISLEAD **[two-actions] **SPELL 6**  **CONCENTRATE** **ILLUSION** **MANIPULATE**  **Traditions** arcane, occult  **Duration** sustained up to 1 minute  You turn yourself invisible and create an illu |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/30/Text/39` | 0.462135 | **Success** The creature takes a –1 status penalty to Perception  checks for 1 round. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/23` | 0.455260 | **Critical Failure** The creature perceives what you chose until  it disbelieves, and it trusts its false senses, taking a –4  circumstance penalty to saves to disbelieve. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/2` | 0.442790 | The image can't speak, but you can use your actions to  speak through the creature, with the spell disguising your  voice as appropriate. You might need to attempt a Deception  or Performance check to |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/52` | 0.440309 | **FALSE VISION** **SPELL 5**  **UNCOMMON** **CONCENTRATE** **ILLUSION** **MANIPULATE**  **Traditions** arcane, occult  **Cast** 10 minutes  **Range **touch;** Area** 100-foot burst  **Duration** until |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/1/SectionHeader/32` | 0.429430 | **FABRICATED TRUTH **[three-actions] **SPELL 10**  **CONCENTRATE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** occult  **Range **100 feet;** Targets** up to 5 creatures  **Defense** W |

### Query 132
- Text: What is the rule about **Success** The target takes half damage and no persistent  mental damage.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/39', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/40', 'PZO22001 Starfinder Player Core 330-363::/page/18/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/39` | 0.858197 | **Success** The target takes half damage and no persistent  mental damage. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/40` | 0.655508 | **Failure** The target takes full damage, persistent mental  damage, and is compelled to howl as long as it takes  persistent mental damage. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/20` | 0.637928 | **Success** The creature takes half damage. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/51` | 0.595928 | **Success** The creature takes half damage. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/31` | 0.595928 | **Success** The creature takes half damage. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/41` | 0.577955 | **Critical Failure** As failure, but the target takes double the  initial and persistent damage. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/38` | 0.576439 | **Critical Success** The target is unaffected. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/3` | 0.567092 | **Success** The creature takes half damage and is slowed 1 until  the end of its next turn. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/37` | 0.547762 | **Success** The target makes progress toward completing the  game. If the target already made progress, it completes  the game and the spell ends. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/26/Text/47` | 0.517679 | **Success** The creature can attempt its attack and any other  attacks against the target this turn. |

### Query 133
- Text: What is the rule about **Failure** The target takes full damage, persistent mental  damage, and is compelled to howl as long as it takes  persistent mental damage.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/40']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/40', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/41', 'PZO22001 Starfinder Player Core 330-363::/page/26/Text/48']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/40` | 0.963371 | **Failure** The target takes full damage, persistent mental  damage, and is compelled to howl as long as it takes  persistent mental damage. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/41` | 0.678877 | **Critical Failure** As failure, but the target takes double the  initial and persistent damage. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/26/Text/48` | 0.677291 | **Failure** The creature can't attack the target and wastes the  action. It can't attempt further attacks against the target  this turn. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/1` | 0.592752 | **Failure** The target makes no progress toward completing  the game. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/2` | 0.590228 | **Critical Failure** The target loses the game and has to start  over. It loses all progress it made. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/37` | 0.585897 | You let out a powerful ululation full of psychic resonance that  compels others who hear it to join in. You deal 7d12 sonic  damage and 1d8 persistent mental damage to other creatures  who can hear wi |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/4` | 0.575515 | **Failure** The creature takes full damage, is slowed 3 until the  end of its next turn, and slowed 1 for 1 minute. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/9` | 0.575194 | **Failure** The creature takes full damage. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/10` | 0.569310 | **Failure** The creature is knocked prone. If it was flying, it takes  the effects of critical failure instead. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/1` | 0.568819 | **Failure** Each round of the spell's duration, you can Sustain the  spell to ask a different question and attempt to uncover  the answer. For each question, the target can attempt  a Deception check |

### Query 134
- Text: What is the rule about **Critical Failure** As failure, but the target takes double the  initial and persistent damage.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/41', 'PZO22001 Starfinder Player Core 330-363::/page/18/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/5/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/41` | 0.961267 | **Critical Failure** As failure, but the target takes double the  initial and persistent damage. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/18/Text/2` | 0.733450 | **Critical Failure** The target loses the game and has to start  over. It loses all progress it made. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/5/Text/10` | 0.693031 | **Critical Failure** The creature takes double void damage and  double persistent bleed damage. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/2` | 0.642346 | **Critical Failure** As failure, and the target takes a –4  circumstance penalty to Deception checks against your  questions. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/40` | 0.637229 | **Failure** The target takes full damage, persistent mental  damage, and is compelled to howl as long as it takes  persistent mental damage. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/5` | 0.622417 | **Critical Failure** The creature takes double damage, is slowed  3 until the end of its next turn, and slowed 2 for 1 minute. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/5` | 0.620258 | **Critical Failure** The creature becomes frightened 2, and its  action fails and is wasted. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/17` | 0.586002 | **Critical Failure** The creature dies. |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/10` | 0.580783 | **Failure** The creature is knocked prone. If it was flying, it takes  the effects of critical failure instead. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/26/Text/49` | 0.577523 | **Critical Failure** The creature wastes the action and can't  attempt to attack the target for the rest of *sanctuary*'s  duration. |

### Query 135
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/58']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/1/Text/62', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/56', 'PZO22001 Starfinder Player Core 330-363::/page/11/Text/59']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/62` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/56` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/59` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/58` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/40` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/63` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/56` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/59` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/58` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/40` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 136
- Text: What is the rule about **SKILLS** **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/60']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/60', 'PZO22001 Starfinder Player Core 330-363::/page/27/Text/60', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/58']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/60` | 0.909736 | **SKILLS** **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/60` | 0.698535 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/58` | 0.698535 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/42` | 0.656535 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/64` | 0.656535 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/61` | 0.656535 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/42` | 0.656535 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/61` | 0.656535 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/58` | 0.656535 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/69` | 0.656535 | **SKILLS** |

### Query 137
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/62']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/45', 'PZO22001 Starfinder Player Core 330-363::/page/17/Text/45', 'PZO22001 Starfinder Player Core 330-363::/page/25/Text/60']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/45` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/45` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/60` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/61` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/64` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/72` | 0.847304 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/62` | 0.847304 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/67` | 0.847304 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/68` | 0.847304 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/62` | 0.847303 | **SPELLS** |

### Query 138
- Text: What is the rule about **Spell Lists**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/63']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/33/Text/65', 'PZO22001 Starfinder Player Core 330-363::/page/17/Text/46', 'PZO22001 Starfinder Player Core 330-363::/page/15/Text/61']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/65` | 0.890837 | **Spell Lists** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/46` | 0.890837 | **Spell Lists** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/61` | 0.890837 | **Spell Lists** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/70` | 0.848837 | **Spell Lists** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/46` | 0.848837 | **Spell Lists** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/61` | 0.848837 | **Spell Lists** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/65` | 0.848837 | **Spell Lists** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/63` | 0.848837 | **Spell Lists** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/63` | 0.848837 | **Spell Lists** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/63` | 0.848837 | **Spell Lists** |

### Query 139
- Text: What is the rule about **Spells**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/64']
- Expected found: `True`
- Expected rank: `12`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/33/Text/66', 'PZO22001 Starfinder Player Core 330-363::/page/1/Text/69', 'PZO22001 Starfinder Player Core 330-363::/page/13/Text/64']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/66` | 0.798799 | **Spells** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/69` | 0.798799 | **Spells** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/64` | 0.798799 | **Spells** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/63` | 0.756799 | **Spells** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/62` | 0.756799 | **Spells** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/62` | 0.756799 | **Spells** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/64` | 0.756799 | **Spells** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/74` | 0.756799 | **Spells** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/66` | 0.756799 | **Spells** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/47` | 0.756799 | **Spells** |

### Query 140
- Text: What is the rule about **Focus Spells**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/65']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/7/Text/65', 'PZO22001 Starfinder Player Core 330-363::/page/3/Text/64', 'PZO22001 Starfinder Player Core 330-363::/page/15/Text/63']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/65` | 0.926221 | **Focus Spells** |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/3/Text/64` | 0.926221 | **Focus Spells** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/63` | 0.926221 | **Focus Spells** |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/67` | 0.884221 | **Focus Spells** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/13/Text/65` | 0.884221 | **Focus Spells** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/19/Text/75` | 0.884221 | **Focus Spells** |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/63` | 0.884221 | **Focus Spells** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/33/Text/67` | 0.884221 | **Focus Spells** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/27/Text/65` | 0.884221 | **Focus Spells** |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/1/Text/70` | 0.884221 | **Focus Spells** |

### Query 141
- Text: What is the rule about traits while in this form, as well as any trait related to  the creature's kind (such as goblin or human). If this  transformation reduces your size, it reduces your reach  accordingly (typically to 5 feet). This transformation doesn't  change your statistics in any way, and you don't gain any  special abilities of the humanoid form you assume. You  can still wear and use your gear, which changes size (if  necessary) to match your new form. If items leave your  person, they return to their usual size.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/8/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/8/Text/1', 'PZO22001 Starfinder Player Core 330-363::/page/20/Text/13', 'PZO22001 Starfinder Player Core 330-363::/page/8/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/1` | 1.001082 | traits while in this form, as well as any trait related to  the creature's kind (such as goblin or human). If this  transformation reduces your size, it reduces your reach  accordingly (typically to 5 |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/20/Text/13` | 0.611333 | You transform into the battle form of a Tiny animal, such as  a cat, insect, lizard, or rat. You can decide the specific type of  animal (such as a squox or praying mantis), but this has no  effect on |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/4` | 0.598276 | **Heightened (5th)** You can take on the appearance of a Large  humanoid. If this increases your size, you gain the effects  of the *enlarge* spell. |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/50` | 0.495505 | **HUMANOID FORM **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, occult, primal  **Duration** 10 minutes  You transform your appearance to that of a Sm |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/52` | 0.488484 | **Failure** The creature takes full damage and is pushed 5 feet  away from you. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/22` | 0.483777 | You gain specific abilities based on the form you choose: |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/4` | 0.480089 | **ENLARGE **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Range **30 feet;** Targets** 1 willing creature  **Duration** 5 minutes  Bolstered |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/2` | 0.475500 | *Humanoid form* grants you a +4 status bonus to Deception  checks to pass as a generic member of the chosen ancestry,  and you add your level even if you're untrained, but you  can't make yourself loo |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/58` | 0.470652 | **SHRINK **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Range **30 feet;** Targets** 1 willing creature  **Duration** 5 minutes  You warp s |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/25/Text/16` | 0.465968 | **Critical Success** The creature's movement is not restricted. |

### Query 142
- Text: What is the rule about *Humanoid form* grants you a +4 status bonus to Deception  checks to pass as a generic member of the chosen ancestry,  and you add your level even if you're untrained, but you  can't make yourself look like a specific person. If you want to  Impersonate an individual, you still need to create a disguise,  though the GM won't factor in the difference in ancestry  when determining the DC of your Deception check. You can  Dismiss this spell.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/8/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/8/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/7/Text/73', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/2` | 1.006703 | *Humanoid form* grants you a +4 status bonus to Deception  checks to pass as a generic member of the chosen ancestry,  and you add your level even if you're untrained, but you  can't make yourself loo |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/73` | 0.636031 | Falsehoods pass your lips as smoothly as silk. You gain a  +4 status bonus to Deception checks to Lie and against  Perception checks to discern if you are telling the truth, and  you add your level ev |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/2` | 0.607511 | The image can't speak, but you can use your actions to  speak through the creature, with the spell disguising your  voice as appropriate. You might need to attempt a Deception  or Performance check to |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/7` | 0.555310 | **ILLUSORY DISGUISE **[two-actions] **SPELL 1**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **VISUAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 willing creature  **Duration** |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/1` | 0.518773 | traits while in this form, as well as any trait related to  the creature's kind (such as goblin or human). If this  transformation reduces your size, it reduces your reach  accordingly (typically to 5 |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/4` | 0.486411 | **Heightened (5th)** You can take on the appearance of a Large  humanoid. If this increases your size, you gain the effects  of the *enlarge* spell. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/15/SectionHeader/27` | 0.485584 | **MISLEAD **[two-actions] **SPELL 6**  **CONCENTRATE** **ILLUSION** **MANIPULATE**  **Traditions** arcane, occult  **Duration** sustained up to 1 minute  You turn yourself invisible and create an illu |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/1` | 0.464176 | **Failure** Each round of the spell's duration, you can Sustain the  spell to ask a different question and attempt to uncover  the answer. For each question, the target can attempt  a Deception check |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/50` | 0.456616 | **HUMANOID FORM **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, occult, primal  **Duration** 10 minutes  You transform your appearance to that of a Sm |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/20/Text/13` | 0.442102 | You transform into the battle form of a Tiny animal, such as  a cat, insect, lizard, or rat. You can decide the specific type of  animal (such as a squox or praying mantis), but this has no  effect on |

### Query 143
- Text: What is the rule about **Heightened (5th)** You can take on the appearance of a Large  humanoid. If this increases your size, you gain the effects  of the *enlarge* spell.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/8/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/8/Text/4', 'PZO22001 Starfinder Player Core 330-363::/page/0/Text/4', 'PZO22001 Starfinder Player Core 330-363::/page/11/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/4` | 0.990025 | **Heightened (5th)** You can take on the appearance of a Large  humanoid. If this increases your size, you gain the effects  of the *enlarge* spell. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/0/Text/4` | 0.713154 | **ENLARGE **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE** **POLYMORPH**  **Traditions** arcane, primal  **Range **30 feet;** Targets** 1 willing creature  **Duration** 5 minutes  Bolstered |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/31` | 0.695717 | **Heightened (5th)** Your battle form is Huge, and your attacks  have 15-foot reach. You instead gain 20 temporary HP,  attack modifier +18, damage bonus +2 and double damage  dice (including persiste |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/14/Text/18` | 0.628940 | **Heightened (10th)** The spell can affect living creatures up to  19th level. Increase the damage to 10d6 on a success, and  to 115 on a failure. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/1` | 0.618063 | traits while in this form, as well as any trait related to  the creature's kind (such as goblin or human). If this  transformation reduces your size, it reduces your reach  accordingly (typically to 5 |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/30` | 0.609211 | **Heightened (4th)** Your battle form is Large, and your attacks  have 10-foot reach. You instead gain 15 temporary HP,  attack modifier +16, damage bonus +6, and Athletics +16. |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/22/Text/29` | 0.597985 | **Heightened (6th)** Your battle form is Huge, and the reach of  your attacks increases by 5 feet. You instead gain AC = 22  + your level, 24 temporary HP, attack modifier +21, damage  bonus +16, and |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/50` | 0.594483 | **Heightened (7th)** You can target up to 5 additional creatures  to gain protection against the environment the triggering  creature entered. The spell lasts for 8 hours and also  protects against ex |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/51` | 0.593885 | **Heightened (10th)** You can target up to 10 additional  creatures to gain protection against the environment the  triggering creature entered. The spell lasts until your next  daily preparations and |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/6` | 0.592177 | **Heightened (+1)** The damage of the image's Strikes increases  by 1d4, and the maximum size of creature you can create  increases by one (to a maximum of Gargantuan). |

### Query 144
- Text: What is the rule about You rapidly catalog and collate information relevant to  your current situation. You can instantly use up to 6 Recall  Knowledge actions as part of Casting this Spell. For these?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/8/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/8/Text/25', 'PZO22001 Starfinder Player Core 330-363::/page/8/Text/26', 'PZO22001 Starfinder Player Core 330-363::/page/28/Text/66']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/25` | 0.990383 | You rapidly catalog and collate information relevant to  your current situation. You can instantly use up to 6 Recall  Knowledge actions as part of Casting this Spell. For these |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/26` | 0.646129 | actions, you can't use any special abilities, reactions, or free  actions that trigger when you Recall Knowledge. |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/28/Text/66` | 0.540988 | **SIFT THE SPHERE** **SPELL 2**  **CONCENTRATE** **MANIPULATE** **PREDICTION**  **Traditions** divine, occult  **Cast** 10 minutes  You ritually sift through the local infosphere and gain  mystical in |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/30/Text/15` | 0.486806 | **SKIM DATA **[two-actions] **SPELL 2**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Range **touch; **Targets** one dataset contained within a  touched object  You touch one objec |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/15/SectionHeader/3` | 0.462440 | **MIND READING **[two-actions] **SPELL 3**  **UNCOMMON** **CONCENTRATE** **DETECTION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult **Range **30 feet;** Targets** 1 creature  **Defense** W |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/28` | 0.461673 | **RETROCOGNITION** **SPELL 7**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  **Cast** 1 minute  **Duration** sustained  Opening your mind to mental echoes, you gain impressions  from |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/13` | 0.459332 | **HOLOGRAPHIC MEMORY **[two-actions] **SPELL 3**  **UNCOMMON** **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** divine, occult  **Range **touch;** Targets** 1 creature or corpse  **Defense** |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/27/SectionHeader/42` | 0.454678 | **SENDING **[three-actions] **SPELL 5**  **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult  **Range **planetary;** Targets** 1 creature you know well  You send the creat |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/17/SectionHeader/25` | 0.450904 | **NEW GAME **[three-actions] **SPELL 10**  **CONCENTRATE** **EXTRADIMENSIONAL** **MANIPULATE**  **Traditions** arcane  **Requirements** You have access to a computer with a vidgame  installed on it, w |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/24/Text/20` | 0.450325 | **READ OMENS** **SPELL 4**  **UNCOMMON** **CONCENTRATE** **MANIPULATE** **PREDICTION**  **Traditions** divine, occult  **Cast** 10 minutes  You peek into the future. Choose a particular goal or activi |

### Query 145
- Text: What is the rule about actions, you can't use any special abilities, reactions, or free  actions that trigger when you Recall Knowledge.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/8/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/8/Text/26', 'PZO22001 Starfinder Player Core 330-363::/page/8/Text/25', 'PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/26` | 0.984826 | actions, you can't use any special abilities, reactions, or free  actions that trigger when you Recall Knowledge. |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/25` | 0.612830 | You rapidly catalog and collate information relevant to  your current situation. You can instantly use up to 6 Recall  Knowledge actions as part of Casting this Spell. For these |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/3/SectionHeader/34` | 0.482350 | **FREEZE TIME **[three-actions] **SPELL 10**  **CONCENTRATE** **MANIPULATE**  **Traditions** arcane, occult  You temporarily stop time for everything but yourself,  allowing you to use several actions |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/17/SectionHeader/14` | 0.437367 | **NEVER MIND **[two-actions] **SPELL 6**  **CONCENTRATE** **CURSE** **INCAPACITATION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 creature **Defense** W |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/11/Text/22` | 0.417765 | You gain specific abilities based on the form you choose: |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/26/Text/2` | 0.407997 | **REWRITE MEMORY **[two-actions] **SPELL 4**  **UNCOMMON** **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** occult  **Range **30 feet; **Targets** 1 creature **Defense** Will; **Duration** un |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/2` | 0.395218 | The image can't speak, but you can use your actions to  speak through the creature, with the spell disguising your  voice as appropriate. You might need to attempt a Deception  or Performance check to |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/25/SectionHeader/9` | 0.392921 | **REPULSION **[two-actions] **SPELL 6**  **AURA** **CONCENTRATE** **MANIPULATE** **MENTAL**  **Traditions** arcane, divine, occult  **Area** emanation up to 40 feet  **Defense** Will; **Duration** 1 m |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/23/Text/17` | 0.390071 | *Prestidigitation* can't deal damage or cause adverse  conditions. Any actual change to an object (beyond what is  noted above) persists only as long as you Sustain the spell. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/17/Text/1` | 0.388600 | are Strength based (for the purpose of the enfeebled  condition, for example). If your unarmed attack modifier  is higher, you can use it instead. |

### Query 146
- Text: What is the rule about You create an illusory image of a Large or smaller creature. It  generates the appropriate sounds, smells, and feels believable  to the touch. If you and the image are ever farther than 500  feet apart, the spell ends.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/1', 'PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/19', 'PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/1` | 0.991001 | You create an illusory image of a Large or smaller creature. It  generates the appropriate sounds, smells, and feels believable  to the touch. If you and the image are ever farther than 500  feet apar |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/19` | 0.676431 | **ILLUSORY OBJECT **[two-actions] **SPELL 1**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **VISUAL**  **Traditions** arcane, occult  **Range **500 feet;** Area** 20-foot burst  **Duration** 10 minute |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/29` | 0.646023 | **ILLUSORY SCENE** **SPELL 5**  **AUDITORY** **CONCENTRATE** **ILLUSION** **MANIPULATE** **OLFACTORY** **VISUAL**  **Traditions** arcane, occult  **Cast** 10 minutes  **Range **500 feet;** Area** 30-f |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/33` | 0.601532 | **FIGMENT **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet  **Duration** sustained  You create a simp |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/7` | 0.576795 | **ILLUSORY DISGUISE **[two-actions] **SPELL 1**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **VISUAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 willing creature  **Duration** |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/18` | 0.560490 | **PROJECT IMAGE **[two-actions] **SPELL 7**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet  **Duration** sustained up to 1 minute  You projec |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/2` | 0.553875 | The image can't speak, but you can use your actions to  speak through the creature, with the spell disguising your  voice as appropriate. You might need to attempt a Deception  or Performance check to |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/3` | 0.545203 | In combat, the illusion can use 2 actions per turn, which  it uses when you Sustain the spell. It uses your spell attack  modifier for attack rolls and your spell DC for its AC. Its  saving throw modi |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/1` | 0.532555 | Illusions bend light around the target, rendering it  invisible. This makes it undetected to all creatures, though  the creatures can attempt to find the target, making it  hidden to them instead (pag |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/4` | 0.529930 | **Heightened (5th)** You can take on the appearance of a Large  humanoid. If this increases your size, you gain the effects  of the *enlarge* spell. |

### Query 147
- Text: What is the rule about The image can't speak, but you can use your actions to  speak through the creature, with the spell disguising your  voice as appropriate. You might need to attempt a Deception  or Performance check to mimic the creature, as determined  by the GM. This is especially likely if you're trying to imitate a  specific person and engage with someone that person knows.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/7', 'PZO22001 Starfinder Player Core 330-363::/page/10/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/2` | 0.998006 | The image can't speak, but you can use your actions to  speak through the creature, with the spell disguising your  voice as appropriate. You might need to attempt a Deception  or Performance check to |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/7` | 0.668784 | **ILLUSORY DISGUISE **[two-actions] **SPELL 1**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **VISUAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 willing creature  **Duration** |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/10/Text/2` | 0.640471 | Any creature that touches any part of the image or uses  the Seek action to examine it can attempt to disbelieve  your illusion. If they interact with a portion of the illusion,  they disbelieve only |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/10/Text/3` | 0.584742 | **Heightened (6th)** Creatures or objects in your scene can  speak. You must speak the specific lines for each actor  when creating your program. The spell disguises your  voice for each actor. |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/1` | 0.579399 | **Failure** Each round of the spell's duration, you can Sustain the  spell to ask a different question and attempt to uncover  the answer. For each question, the target can attempt  a Deception check |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/5` | 0.572244 | Any creature that touches the image or uses the Seek  action to examine it can attempt to disbelieve your illusion.  When a creature disbelieves the illusion, it recovers from half  the damage it had |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/1` | 0.559518 | You create an illusory image of a Large or smaller creature. It  generates the appropriate sounds, smells, and feels believable  to the touch. If you and the image are ever farther than 500  feet apar |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/8/Text/2` | 0.548426 | *Humanoid form* grants you a +4 status bonus to Deception  checks to pass as a generic member of the chosen ancestry,  and you add your level even if you're untrained, but you  can't make yourself loo |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/3` | 0.545430 | In combat, the illusion can use 2 actions per turn, which  it uses when you Sustain the spell. It uses your spell attack  modifier for attack rolls and your spell DC for its AC. Its  saving throw modi |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/33` | 0.537991 | **FIGMENT **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet  **Duration** sustained  You create a simp |

### Query 148
- Text: What is the rule about In combat, the illusion can use 2 actions per turn, which  it uses when you Sustain the spell. It uses your spell attack  modifier for attack rolls and your spell DC for its AC. Its  saving throw modifiers are equal to your spell DC – 10. It's  substantial enough that it can flank other creatures. If the  image is hit by an attack or fails a save, the spell ends.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/3', 'PZO22001 Starfinder Player Core 330-363::/page/12/Text/1', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/3` | 0.996217 | In combat, the illusion can use 2 actions per turn, which  it uses when you Sustain the spell. It uses your spell attack  modifier for attack rolls and your spell DC for its AC. Its  saving throw modi |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/1` | 0.654885 | Illusions bend light around the target, rendering it  invisible. This makes it undetected to all creatures, though  the creatures can attempt to find the target, making it  hidden to them instead (pag |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/5` | 0.641042 | Any creature that touches the image or uses the Seek  action to examine it can attempt to disbelieve your illusion.  When a creature disbelieves the illusion, it recovers from half  the damage it had |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/4` | 0.609430 | The illusion can cause damage by making the target believe  the illusion's attacks are real, but it cannot otherwise directly  affect the physical world. If the illusory creature hits with a  Strike, |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/23/SectionHeader/18` | 0.596607 | **PROJECT IMAGE **[two-actions] **SPELL 7**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL**  **Traditions** arcane, occult  **Range **30 feet  **Duration** sustained up to 1 minute  You projec |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/15/SectionHeader/27` | 0.592987 | **MISLEAD **[two-actions] **SPELL 6**  **CONCENTRATE** **ILLUSION** **MANIPULATE**  **Traditions** arcane, occult  **Duration** sustained up to 1 minute  You turn yourself invisible and create an illu |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/2/Text/33` | 0.575825 | **FIGMENT **[two-actions] **CANTRIP 1**  **CANTRIP** **CONCENTRATE** **ILLUSION** **MANIPULATE** **SUBTLE**  **Traditions** arcane, occult  **Range **30 feet  **Duration** sustained  You create a simp |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/1` | 0.570130 | **Failure** Each round of the spell's duration, you can Sustain the  spell to ask a different question and attempt to uncover  the answer. For each question, the target can attempt  a Deception check |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/19` | 0.558275 | **ILLUSORY OBJECT **[two-actions] **SPELL 1**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **VISUAL**  **Traditions** arcane, occult  **Range **500 feet;** Area** 20-foot burst  **Duration** 10 minute |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/10/Text/2` | 0.557425 | Any creature that touches any part of the image or uses  the Seek action to examine it can attempt to disbelieve  your illusion. If they interact with a portion of the illusion,  they disbelieve only |

### Query 149
- Text: What is the rule about The illusion can cause damage by making the target believe  the illusion's attacks are real, but it cannot otherwise directly  affect the physical world. If the illusory creature hits with a  Strike, the target takes 3d4 mental damage. The illusion's  Strikes are nonlethal. If the damage doesn't correspond to  the image of the monster—for example, if an illusory Large  dragon deals only 5 damage—the GM might allow the target  to attempt an immediate Perception check to disbelieve the  spell. Any relevant resistances and weaknesses apply if the  target thinks they do, as judged by the GM. For example, if  the illusion wields a doshko and attacks a creature resistant to  piercing damage, the creature would take less mental damage.  However, illusory damage does not deactivate regeneration or  trigger other effects that require a certain damage type. The  GM should track illusory damage dealt by the illusion.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/4', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/5', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/4` | 1.022235 | The illusion can cause damage by making the target believe  the illusion's attacks are real, but it cannot otherwise directly  affect the physical world. If the illusory creature hits with a  Strike, |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/5` | 0.719685 | Any creature that touches the image or uses the Seek  action to examine it can attempt to disbelieve your illusion.  When a creature disbelieves the illusion, it recovers from half  the damage it had |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/3` | 0.648472 | In combat, the illusion can use 2 actions per turn, which  it uses when you Sustain the spell. It uses your spell attack  modifier for attack rolls and your spell DC for its AC. Its  saving throw modi |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/10/Text/2` | 0.597377 | Any creature that touches any part of the image or uses  the Seek action to examine it can attempt to disbelieve  your illusion. If they interact with a portion of the illusion,  they disbelieve only |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/1` | 0.562565 | Illusions bend light around the target, rendering it  invisible. This makes it undetected to all creatures, though  the creatures can attempt to find the target, making it  hidden to them instead (pag |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/21/SectionHeader/8` | 0.532537 | **PHANTOM PAIN **[two-actions] **SPELL 1**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **MENTAL** **NONLETHAL**  **Traditions** occult  **Range **30 feet; **Targets** 1 creature **Defense** Will; **D |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/1` | 0.531161 | **Failure** Each round of the spell's duration, you can Sustain the  spell to ask a different question and attempt to uncover  the answer. For each question, the target can attempt  a Deception check |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/9/SectionHeader/7` | 0.527369 | **ILLUSORY DISGUISE **[two-actions] **SPELL 1**  **CONCENTRATE** **ILLUSION** **MANIPULATE** **VISUAL**  **Traditions** arcane, occult  **Range **30 feet;** Targets** 1 willing creature  **Duration** |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/7/Text/37` | 0.525082 | You let out a powerful ululation full of psychic resonance that  compels others who hear it to join in. You deal 7d12 sonic  damage and 1d8 persistent mental damage to other creatures  who can hear wi |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/15/SectionHeader/27` | 0.523681 | **MISLEAD **[two-actions] **SPELL 6**  **CONCENTRATE** **ILLUSION** **MANIPULATE**  **Traditions** arcane, occult  **Duration** sustained up to 1 minute  You turn yourself invisible and create an illu |

### Query 150
- Text: What is the rule about Any creature that touches the image or uses the Seek  action to examine it can attempt to disbelieve your illusion.  When a creature disbelieves the illusion, it recovers from half  the damage it had taken from it (if any) and doesn't take any  further damage from it.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 330-363::/page/9/Text/5', 'PZO22001 Starfinder Player Core 330-363::/page/10/Text/2', 'PZO22001 Starfinder Player Core 330-363::/page/9/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/5` | 1.004555 | Any creature that touches the image or uses the Seek  action to examine it can attempt to disbelieve your illusion.  When a creature disbelieves the illusion, it recovers from half  the damage it had |
| 2 | `PZO22001 Starfinder Player Core 330-363::/page/10/Text/2` | 0.916774 | Any creature that touches any part of the image or uses  the Seek action to examine it can attempt to disbelieve  your illusion. If they interact with a portion of the illusion,  they disbelieve only |
| 3 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/4` | 0.704547 | The illusion can cause damage by making the target believe  the illusion's attacks are real, but it cannot otherwise directly  affect the physical world. If the illusory creature hits with a  Strike, |
| 4 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/3` | 0.614753 | In combat, the illusion can use 2 actions per turn, which  it uses when you Sustain the spell. It uses your spell attack  modifier for attack rolls and your spell DC for its AC. Its  saving throw modi |
| 5 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/23` | 0.569746 | **Critical Failure** The creature perceives what you chose until  it disbelieves, and it trusts its false senses, taking a –4  circumstance penalty to saves to disbelieve. |
| 6 | `PZO22001 Starfinder Player Core 330-363::/page/12/Text/1` | 0.557278 | Illusions bend light around the target, rendering it  invisible. This makes it undetected to all creatures, though  the creatures can attempt to find the target, making it  hidden to them instead (pag |
| 7 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/21` | 0.551617 | **Success** The creature perceives what you chose until it  disbelieves, but it knows what the hallucination is. |
| 8 | `PZO22001 Starfinder Player Core 330-363::/page/15/Text/1` | 0.551114 | **Failure** Each round of the spell's duration, you can Sustain the  spell to ask a different question and attempt to uncover  the answer. For each question, the target can attempt  a Deception check |
| 9 | `PZO22001 Starfinder Player Core 330-363::/page/6/Text/22` | 0.549515 | **Failure** The creature perceives what you chose until it  disbelieves. |
| 10 | `PZO22001 Starfinder Player Core 330-363::/page/9/Text/2` | 0.538174 | The image can't speak, but you can use your actions to  speak through the creature, with the spell disguising your  voice as appropriate. You might need to attempt a Deception  or Performance check to |
