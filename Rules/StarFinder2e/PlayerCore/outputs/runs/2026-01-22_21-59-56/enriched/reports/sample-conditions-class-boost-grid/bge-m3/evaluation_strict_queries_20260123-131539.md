# RulesLawyer Evaluation Report: bge-m3

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `2533`
- Query count: `200`
- Evaluated queries: `200`
- Coverage: `1.0000`
- MRR: `0.8499`
- hit@1: `0.7900`
- hit@3: `0.9000`
- hit@5: `0.9250`
- hit@10: `0.9700`
- Embeddings reused: `False`
- Graph boost: `0.1` (depth=2, top_k=100)

## Timings (ms)
- Embedding: `76900`
- Evaluation: `154`

## Query Details
### Query 0
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/58']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `11`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/44` | 1.000802 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/58` | 1.000802 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/52` | 1.000802 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/64` | 0.906468 | **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/35` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/40` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/52` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/62` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/31` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/70` | 0.900802 | **CONDITIONS ** **APPENDIX** |

### Query 1
- Text: Summarize **Hero Points**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `42`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/35` | 0.984027 | **Hero Points** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/16` | 0.984027 | **Hero Points** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/47` | 0.984027 | **Hero Points** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/33` | 0.984027 | **Hero Points** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/41` | 0.984027 | **Hero Points** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/26` | 0.984027 | **Hero Points** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/36` | 0.984027 | **Hero Points** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/60` | 0.984027 | **Hero Points** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/38` | 0.890040 | Hero Points |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/59` | 0.884027 | **Hero Points** |

### Query 2
- Text: What is the rule about [three-actions] Three-Action Activity?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `59`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/16` | 0.855502 | [three-actions] Three-Action Activity |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/15` | 0.713783 | [two-actions] Two-Action Activity |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.670029 | These rules clarify some of the specifics of using actions. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/39` | 0.659204 | Actions |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/1` | 0.651109 | ACTIONS |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/1` | 0.642352 | BASIC ACTIONS |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/6` | 0.642352 | BASIC ACTIONS |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.639536 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/14` | 0.638261 | [one-action] Single Action |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/7` | 0.638101 | There are four types of actions: single actions, activities,  reactions, and free actions. |

### Query 3
- Text: What are the requirements for **OPERATIVE DEDICATION** **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `62`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/10` | 0.881866 | **OPERATIVE DEDICATION** **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.825369 | **Prerequisites** Operative Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.825369 | **Prerequisites** Operative Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.825369 | **Prerequisites** Operative Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/5` | 0.764143 | **MYSTIC DEDICATION** **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/10` | 0.763877 | **SOLDIER DEDICATION** **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/27` | 0.749979 | **ENVOY DEDICATION** **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/10` | 0.741545 | **SOLARIAN DEDICATION** **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/65` | 0.741292 | **Prerequisites** Operative Dedication, class granting no more Hit  Points per level than 6 + your Constitution |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/36` | 0.739222 | **Prerequisites** Operative Dedication, expert in Perception |

### Query 4
- Text: What is the rule about When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency ranks range from trained to legendary.  For instance, a character trained with a battle ribbon can  use it effectively to dispatch foes, while a character who  is legendary with the weapon might be able to spell out  their name in decorative cursive script with just a flick of  their wrist!?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `61`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 1.069972 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.868451 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 0.847653 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` | 0.814114 | Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  char |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.797368 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.792363 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/8` | 0.781001 | If something isn't listed in your character's class entry,  their proficiency rank in that statistic is untrained unless  they gain training from another source. If your character  is untrained in som |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 0.780107 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/10` | 0.779774 | from their class features; and more. Your character's class  entry also provides the information needed when they  gain levels, so it will be a vital reference throughout the  course of your campaign. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.779204 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |

### Query 5
- Text: Summarize **Mystic**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/25']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `21`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/42` | 0.903583 | **Mystic** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/25` | 0.903583 | **Mystic** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/52` | 0.903583 | **Mystic** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/35` | 0.903583 | **Mystic** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/30` | 0.903583 | **Mystic** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/60` | 0.903583 | **Mystic** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/47` | 0.803583 | **Mystic** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/51` | 0.803583 | **Mystic** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/41` | 0.803583 | **Mystic** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/23` | 0.761011 | **Mystic** **Page 114** |

### Query 6
- Text: Summarize KEY ATTRIBUTE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `32`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/13` | 0.916928 | KEY ATTRIBUTE |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/4` | 0.839983 | **KEY ATTRIBUTE** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/1` | 0.704515 | **KEY TERMS** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/4` | 0.699623 | **Attributes** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11` | 0.685806 | CLASS FEATURES |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26` | 0.685806 | CLASS FEATURES |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/14` | 0.681393 | ENVOY FEATS |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/43` | 0.681393 | ENVOY FEATS |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/1` | 0.677525 | **ENVOY FEATS BY NAME** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7` | 0.658049 | **HIT POINTS** |

### Query 7
- Text: Summarize You fall prone.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/2/Text/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `61`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/24` | 1.019201 | You fall prone. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/31` | 0.877160 | **Trigger** You fall. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/5` | 0.875317 | You stand up from being prone. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/96` | 0.812457 | **Prone:** You're lying on the ground and easier to attack. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/99` | 0.808306 | creature has you pinned. |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/105` | 0.807092 | **Unconscious:** You're asleep or knocked out. |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/7/SectionHeader/4` | 0.805941 | FALLING ON A CREATURE |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/68` | 0.796562 | vitality. **Dying:** You're slipping closer to death. |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/16` | 0.788181 | **Trigger** You fall from or past an edge or handhold. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/63` | 0.755548 | **Confused:** You attack indiscriminately. |

### Query 8
- Text: What is the rule about Mystic operatives might run out of spells, but they won't  run out of shells.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/ListItem/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `36`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/ListItem/6` | 0.974070 | Mystic operatives might run out of spells, but they won't  run out of shells. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/4` | 0.609099 | Mystics support allies and themselves with powerful magic. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/6` | 0.601802 | Mystic solarians can augment themselves with  powerful spells and heal themselves while confronting  power enemies on the frontline. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/31` | 0.591019 | You gain one mystic feat. For the purpose of meeting its  prerequisites, your mystic level is half your character level. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/51` | 0.589081 | **Prerequisites** Expert Mystic Spellcasting; legendary in  connection skill |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/26` | 0.585863 | You gain a 1st- or 2nd-level mystic feat. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/22` | 0.582850 | You gain one operative feat. For the purpose of meeting its  prerequisites, your operative level is half your character level. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/1` | 0.573519 | MYSTIC |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/10` | 0.573461 | You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by you |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/5/ListItem/6` | 0.568952 | Mystic soldiers with the elemental connection can make  different area weapons on the fly that deal different  types of damage. |

### Query 9
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `39`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/27` | 0.856592 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/33` | 0.856592 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/35` | 0.856592 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/30` | 0.850199 | SPELLS |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/30` | 0.756592 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/36` | 0.756592 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/60` | 0.756592 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/38` | 0.756592 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/68` | 0.756592 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/32` | 0.756592 | **SPELLS** |

### Query 10
- Text: What is the rule about You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common spell of your connection's tradition, or one of your  connection's granted spells.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `42`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 1.032125 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/29` | 0.928349 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the witchwarper  archetype, add a spell of the appropriate spell rank to your  repertoire: a co |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/10` | 0.848804 | You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by you |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/42` | 0.847619 | Increase the number of spells in your repertoire and number  of spell slots you gain from mystic archetype feats by 1 for  each spell rank other than your two highest mystic spell slots. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/17` | 0.823970 | **Basic Spellcasting Feat:** Usually available at 4th level,  these feats grant a 1st-rank spell slot. At 6th level, they  grant you a 2nd-rank spell slot, and if you have a spell  repertoire, you can |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/40` | 0.803936 | Your repertoire expands, and you can cast more spells of your  paradox's tradition each day. Increase the number of spells  in your repertoire and number of spell slots you gain from  witchwarper arch |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.797445 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/9` | 0.785411 | Choose a connection (see page 119). You become trained in  the connection's skill or, if you were already trained, you  become trained in a skill of your choice. You don't gain any  other abilities fr |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/18` | 0.768556 | **Expert Spellcasting Feat:** Typically taken at 12th level,  these feats make you an expert in spell attack modifiers  and spell DCs and grant you a 4th-rank spell slot. If you  have a spell repertoi |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/19` | 0.756385 | **Master Spellcasting Feat:** Usually found at 18th level, these  feats make you a master in spell attack modifiers and spell  DCs and grant you a 7th-rank spell slot. If you have a spell  repertoire, |

### Query 11
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/27']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `31`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/31` | 0.827771 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/37` | 0.827771 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/29` | 0.827771 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/26` | 0.827771 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/27` | 0.827771 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/27` | 0.827771 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/33` | 0.827771 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/48` | 0.827771 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/29` | 0.827771 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/9/SectionHeader/25` | 0.825791 | SKILLS |

### Query 12
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/26']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `28`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/24` | 0.963367 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/26` | 0.963367 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/34` | 0.963367 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/24` | 0.963367 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/26` | 0.963367 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/45` | 0.963367 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/28` | 0.963367 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/30` | 0.963367 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/23` | 0.963367 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/21` | 0.863367 | **INTRODUCTION** |

### Query 13
- Text: What is the rule about MULTICLASS ENVOY  CHARACTERS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/3` | 0.949274 | MULTICLASS ENVOY  CHARACTERS |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/3` | 0.756588 | MULTICLASS OPERATIVE  CHARACTERS |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/3` | 0.700508 | MULTICLASS SOLDIER  CHARACTERS |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/3` | 0.695265 | MULTICLASS MYSTIC  CHARACTERS |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/3` | 0.680710 | MULTICLASS SOLARIAN  CHARACTERS |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/3` | 0.676311 | MULTICLASS WITCHWARPER  CHARACTERS |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/8` | 0.672063 | Multiclass Dedications |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.662581 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/1` | 0.652033 | ENVOY |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.634328 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |

### Query 14
- Text: What is the rule about case of an activity, you usually lose all actions spent for the  activity up through the end of that turn. For instance, if you  began to Cast a Spell requiring 3 actions and the first action  was disrupted, you lose all 3 actions that you committed to  that activity.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `39`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/18` | 1.036784 | case of an activity, you usually lose all actions spent for the  activity up through the end of that turn. For instance, if you  began to Cast a Spell requiring 3 actions and the first action  was dis |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.849202 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/6` | 0.743668 | Effects can change the number of actions you can use on  your turn, or whether you can use actions at all. The slowed  condition, for example, causes you to lose actions, while the  quickened conditio |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/6` | 0.742112 | You'll need to track your actions carefully in an encounter. At  the start of each turn you take in an encounter, you regain 3  actions and 1 reaction to spend that round. (Regaining your  actions is |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` | 0.737128 | Sometimes you need to attempt something not already  covered by defined actions in the game. When this happens,  the rules tell you how many actions you need to spend as  well as any traits your actio |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/9` | 0.731981 | Various abilities and conditions, such as a Reactive Strike,  can disrupt an action. When an action is disrupted, you still  use the actions or reactions you committed, and you still  expend any costs |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` | 0.727301 | Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or S |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/25` | 0.725321 | If an activity outside of an encounter is interrupted or  disrupted, as described in Disrupting Actions on page 407,  you usually lose the time you put in, but no additional time. |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/24` | 0.712267 | Activities that take longer than a turn can't normally be  performed during an encounter. Spells with a casting time of  1 minute or more are a common example, as are several skill  actions. When you |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/43` | 0.696708 | If your Sustain action is disrupted, the ability ends. |

### Query 15
- Text: What is the rule about You gain the envoy directives class feature (see page  104), but do not gain the Lead by Example benefits  of the Get 'Em! envoy directive. You become trained in  Deception, Diplomacy, or Intimidation plus another skill of your  choice. If you were already trained in Deception, Diplomacy,  and Intimidation, you instead become trained in an additional  skill of your choice. You also become trained in envoy class DC.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `21`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/30` | 1.064120 | You gain the envoy directives class feature (see page  104), but do not gain the Lead by Example benefits  of the Get 'Em! envoy directive. You become trained in  Deception, Diplomacy, or Intimidation |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/13` | 0.798416 | You become trained in Intimidation. If you  were already trained in Intimidation, you  instead become trained in a skill of your choice.  Increase your maximum and encumbered Bulk limits  by 2. You be |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/20` | 0.769358 | You gain the Lead by Example benefit for your Get 'Em!  directive, except you and your allies get a +2 status bonus  to damage on both the initial and subsequent Strikes. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/61` | 0.733887 | Choose a specialization. You become trained in one skill  determined by your specialization; if you were already trained  in that skill, you instead become trained in another skill of your  choice. Yo |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.729674 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/9` | 0.728211 | Choose a connection (see page 119). You become trained in  the connection's skill or, if you were already trained, you  become trained in a skill of your choice. You don't gain any  other abilities fr |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/35` | 0.719527 | You gain a 1st- or 2nd-level envoy feat of your choice. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/14` | 0.719267 | You become trained in simple and martial guns (see page 132  for the definition of a gun). You become trained in operative  class DC. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/14` | 0.710751 | You become trained in light armor and medium armor. If  you already were trained in light armor and medium armor,  you gain training in heavy armor as well. Whenever you gain  a class feature that gra |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/56` | 0.709495 | Trained in one of the following skills  of your choice: Deception, Diplomacy,  Intimidation |

### Query 16
- Text: What are the requirements for **CHANGE OF PLANS **[reaction] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `44`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/9` | 0.934216 | **CHANGE OF PLANS **[reaction] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/544` | 0.756451 | Change of Plans |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.734681 | **READY ARMS! **[one-action]** TO **[two-actions] |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.729180 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.715899 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.708032 | **WATCH OUT **[reaction] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.705171 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12` | 0.688659 | **GET 'EM! **[one-action]** TO **[two-actions] |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/5` | 0.685822 | **COORDINATED AMBUSH! **[one-action]** TO **[two-actions] |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/26` | 0.682996 | **QUIP **[reaction] **FEAT 1** |

### Query 17
- Text: What is the rule about An activity typically involves using multiple actions to create  an effect greater than you can produce with a single action,  or combining multiple single actions to produce an effect  that's different from merely the sum of those actions. In some  cases, usually when spellcasting, an activity can consist of  only 1 action, 1 reaction, or even 1 free action.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `59`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/20` | 1.030952 | An activity typically involves using multiple actions to create  an effect greater than you can produce with a single action,  or combining multiple single actions to produce an effect  that's differe |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` | 0.800539 | Sometimes you need to attempt something not already  covered by defined actions in the game. When this happens,  the rules tell you how many actions you need to spend as  well as any traits your actio |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/12` | 0.786586 | Abilities that generate an effect typically work within a  specified range or a reach. Most spells and abilities list a  **range**—the maximum distance from the creature or object  creating the effect |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/7` | 0.777842 | Some effects are even more restrictive. Certain abilities,  instead of or in addition to changing the number of actions  you can use, say specifically that you can't use reactions.  The most restricti |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/9` | 0.775650 | **Activities** usually take longer and require using multiple  actions, which must be spent in succession. Strike is a single  action, but Double Tap is an activity in which you use both  the Aim and |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` | 0.762549 | Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or S |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/6` | 0.755012 | Effects can change the number of actions you can use on  your turn, or whether you can use actions at all. The slowed  condition, for example, causes you to lose actions, while the  quickened conditio |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.752036 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/28` | 0.747898 | There are only a few basic reactions and free actions that  all characters can use. You're more likely to gain actions with  triggers from your class, feats, and magic items. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 0.747334 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |

### Query 18
- Text: What is the rule about ACTIVITIES?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `61`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/19` | 0.766120 | ACTIVITIES |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/1` | 0.729326 | ACTIONS |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.708252 | These rules clarify some of the specifics of using actions. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/39` | 0.692839 | Actions |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/1` | 0.676969 | BASIC ACTIONS |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/6` | 0.676969 | BASIC ACTIONS |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/10` | 0.658853 | **IN-DEPTH ACTION RULES** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/9` | 0.639727 | **Activities** usually take longer and require using multiple  actions, which must be spent in succession. Strike is a single  action, but Double Tap is an activity in which you use both  the Aim and |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.634603 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 0.634021 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |

### Query 19
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/22']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `36`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/21` | 0.880013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/35` | 0.880013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/24` | 0.880013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/22` | 0.880013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/48` | 0.880013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/28` | 0.880013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/25` | 0.826490 | ANCESTRIES & BACKGROUNDS |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/25` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/31` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/25` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 20
- Text: What is the rule about from their class features; and more. Your character's class  entry also provides the information needed when they  gain levels, so it will be a vital reference throughout the  course of your campaign.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `57`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/10` | 0.970731 | from their class features; and more. Your character's class  entry also provides the information needed when they  gain levels, so it will be a vital reference throughout the  course of your campaign. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.828830 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.793865 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` | 0.774946 | Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  char |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` | 0.762397 | This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chos |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.752972 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.748077 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/Table/2` | 0.741681 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat2Envoy feat, skill feat, skill increase3Adaptive talent, genera |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.741589 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.740750 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |

### Query 21
- Text: What is the rule about HIT POINTS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/18` | 0.820602 | HIT POINTS |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7` | 0.721307 | **HIT POINTS** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` | 0.683833 | This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chos |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/31` | 0.677244 | Your confidence is a battery that keeps your allies going.  When you use a directive that grants temporary Hit Points, |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 0.670843 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/32` | 0.647814 | increase the temporary Hit Points by your level. When you  use a directive that doesn't grant temporary Hit Points, you  can grant one ally affected by that directive temporary Hit  Points equal to ha |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/11` | 0.644852 | **Trigger** The target of your Get 'Em! is reduced to 0 Hit Points. **Requirements** You used Get 'Em! against a creature on your  last turn. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/1` | 0.639809 | rush into battle with weapons raised gain a higher number  of Hit Points each level, while characters who cast spells or  engage in trickery gain fewer. |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/15` | 0.621836 | **Hit Points, ** **Healing, and ** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/11` | 0.611536 | **Success** The target gains temporary Hit Points equal to their  level plus your Charisma modifier. |

### Query 22
- Text: What is the rule about Archetypes allow you to further customize your character concepts by taking more than one class.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `49`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/2` | 0.953845 | Archetypes allow you to further customize your character concepts by taking more than one class. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.787725 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.755893 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/4` | 0.738362 | You gain an archetype by selecting archetype feats instead  of your normal feats. First, find the archetype that best  fits your character concept. Then select that archetype's  dedication feat, using |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.737155 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/16` | 0.719031 | class feat you have. As you continue selecting operative  archetype class feats, you continue to gain additional Hit Points  in this way. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/5` | 0.715471 | An archetype feat is subject to any restrictions on the class  feat it replaces. For example, if you had an ability at 6th level  that granted you a bonus class feat, but that class feat had to  be 4t |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` | 0.708274 | Some archetypes include a list of "Additional Feats" that  appear in other sources. The list includes each feat's level,  which might be different than normal when gained from the  archetype. You can |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/4` | 0.692410 | The operative archetype allows you to deal high damage to  a single target and select class feats and exploits that add to  your offensive options in combat. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/66` | 0.690478 | You gain 3 additional Hit Points for each operative archetype |

### Query 23
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/38']
- Expected found: `True`
- Expected rank: `44`
- Graph boost applied: `True`
- Graph boosted count: `64`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/23` | 0.937823 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/54` | 0.937823 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/59` | 0.937823 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/64` | 0.937823 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/18` | 0.937823 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/44` | 0.937823 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/39` | 0.937823 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/49` | 0.937823 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/30` | 0.937823 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/35` | 0.937823 | **ARCHETYPE** |

### Query 24
- Text: What is the rule about [reaction] Reaction?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `52`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/17` | 0.746029 | [reaction] Reaction |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` | 0.698388 | **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reac |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/7` | 0.663725 | **AID **[reaction] |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/8/SectionHeader/4` | 0.661905 | **REACTIVE STRIKE **[reaction] |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/14` | 0.650661 | **GRAB AN EDGE **[reaction] |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.649004 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.642750 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.641789 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.639569 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/2` | 0.638771 | Some reactions and free actions are triggered by a  creature using an action with the move trait. The most  notable example is Reactive Strike (reproduced below).  Actions with the move trait can trig |

### Query 25
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/12']
- Expected found: `True`
- Expected rank: `16`
- Graph boost applied: `True`
- Graph boosted count: `64`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/23` | 0.937823 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/54` | 0.937823 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/59` | 0.937823 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/64` | 0.937823 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/18` | 0.937823 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/44` | 0.937823 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/39` | 0.937823 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/49` | 0.937823 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/30` | 0.937823 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/35` | 0.937823 | **ARCHETYPE** |

### Query 26
- Text: Lookup values for Type of CoverBonusCan HideLesser+1 to ACNoStandard+2 to AC, Reflex,
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/10/Table/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `40`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/10/Table/10` | 0.995374 | Type of CoverBonusCan HideLesser+1 to ACNoStandard+2 to AC, Reflex, StealthYesGreater+4 to AC, Reflex, StealthYes |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/10/TableCell/309` | 0.787232 | +2 to AC, Reflex, Stealth |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/10/TableCell/312` | 0.771309 | +4 to AC, Reflex, Stealth |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/10/Text/9` | 0.751752 | When you're behind an obstacle that could block weapons,  guard you against explosions, and make you harder to detect,  you're behind cover. Standard cover gives you a +2 circumstance  bonus to AC, to |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/23` | 0.703351 | You press yourself against a wall or duck behind an obstacle  to take better advantage of cover (page 416). If you would  have standard cover, you instead gain greater cover, which  provides a +4 circ |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/10/TableCell/306` | 0.688668 | +1 to AC |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/10/TableCell/302` | 0.649207 | Type of Cover |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/10/TableCell/304` | 0.629637 | Can Hide |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/22` | 0.606938 | **Requirements** You are benefiting from cover, are near a  feature that allows you to take cover, or are prone. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/10/SectionHeader/8` | 0.599265 | COVER |

### Query 27
- Text: What are the requirements for **Prerequisites** Basic Mystic Spellcasting; master in  connection skill?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/46']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `69`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/46` | 0.984699 | **Prerequisites** Basic Mystic Spellcasting; master in  connection skill |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/51` | 0.945235 | **Prerequisites** Expert Mystic Spellcasting; legendary in  connection skill |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41` | 0.852527 | **Prerequisites** Basic Mystic Spellcasting |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/44` | 0.779327 | **Prerequisites** Basic Witchwarper Spellcasting; master in Arcana  or Occultism, depending on paradox |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/39` | 0.775288 | **Prerequisites** Basic Witchwarper Spellcasting |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25` | 0.758131 | **Prerequisites** Mystic Dedication |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20` | 0.758131 | **Prerequisites** Mystic Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/15` | 0.758131 | **Prerequisites** Mystic Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/36` | 0.758131 | **Prerequisites** Mystic Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/30` | 0.731693 | **Prerequisites** Basic Mysticism |

### Query 28
- Text: What is the rule about MULTICLASS MYSTIC  CHARACTERS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `38`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/3` | 0.865017 | MULTICLASS MYSTIC  CHARACTERS |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/3` | 0.741030 | MULTICLASS ENVOY  CHARACTERS |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/3` | 0.731632 | MULTICLASS SOLDIER  CHARACTERS |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/3` | 0.718427 | MULTICLASS WITCHWARPER  CHARACTERS |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/3` | 0.706006 | MULTICLASS OPERATIVE  CHARACTERS |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/3` | 0.694906 | MULTICLASS SOLARIAN  CHARACTERS |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/1` | 0.641708 | MYSTIC |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.626165 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/51` | 0.614090 | **Prerequisites** Expert Mystic Spellcasting; legendary in  connection skill |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.609154 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |

### Query 29
- Text: What is the rule about You gain your connection's initial epiphany spell. If  you don't already have one, you also gain a focus  pool of 1 Focus Point, which you can Refocus by  reflecting on your connection.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `32`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/37` | 0.986821 | You gain your connection's initial epiphany spell. If  you don't already have one, you also gain a focus  pool of 1 Focus Point, which you can Refocus by  reflecting on your connection. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/25` | 0.817738 | You gain your paradox's initial warp spell. If you don't already  have one, you also gain a focus pool of 1 Focus Point, which you  can Refocus by contemplating infinite worlds. (For more on warp  spe |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/26` | 0.705424 | You gain a 1st- or 2nd-level mystic feat. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.683684 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/9` | 0.672814 | Choose a connection (see page 119). You become trained in  the connection's skill or, if you were already trained, you  become trained in a skill of your choice. You don't gain any  other abilities fr |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/20` | 0.666447 | You gain a 1st- or 2nd-level solarian feat. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/51` | 0.660652 | You gain a 1st- or 2nd-level operative feat. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/31` | 0.655097 | You gain one mystic feat. For the purpose of meeting its  prerequisites, your mystic level is half your character level. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/10` | 0.654907 | You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by you |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/35` | 0.647167 | You gain a 1st- or 2nd-level envoy feat of your choice. |

### Query 30
- Text: What is the rule about Unlike a check, where the result is compared to a DC, the  results of initiative rolls are ranked. This ranking sets the  order in which the encounter's participants act—the initiative  order. The character with the highest result goes first. The  second highest follows, and so on until whoever had the  lowest result takes their turn last.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `35`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/9` | 1.063702 | Unlike a check, where the result is compared to a DC, the  results of initiative rolls are ranked. This ranking sets the  order in which the encounter's participants act—the initiative  order. The cha |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/6` | 0.843409 | When the GM calls for it, you'll roll initiative to determine  your place in the initiative order, which is the sequence in  which the encounter's participants will take their turns.  Rolling initiati |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/13` | 0.834684 | A round begins when the participant with the highest  initiative roll result starts their turn, and it ends when the  one with the lowest initiative ends their turn. The process  of taking a turn is d |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/10` | 0.831714 | If your result is tied with an enemy's result, the enemy  goes first. If your result is tied with another PC's, you can  decide between yourselves who goes first when you reach  that place in the init |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/4` | 0.818052 | An encounter is played out in a series of rounds, during which  the player characters, adversaries, and other participants in the  encounter act in sequence. You roll initiative to determine this  ord |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/15` | 0.800292 | Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/2` | 0.787161 | The GM keeps track of the initiative order for an  encounter. It's usually okay for the players to know  this order since they'll see who goes when and be  aware of one another's results. However, the |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/8` | 0.773471 | The GM rolls initiative for anyone other than the player  characters in the encounter. If these include a number of  identical creatures, the GM could roll once for the group as a  whole and have them |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/11` | 0.768916 | initiative order usually don't change during the encounter.  (But see the Delay basic action on page 408.) |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/18` | 0.743118 | Once you've done all the things you want to do with the actions  you have available, you reach the end of your turn. Take the  following steps in any order you choose. Play then proceeds to  the next |

### Query 31
- Text: What are the requirements for **ACQUIRE ASSET **[one-action] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `33`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/5` | 0.943050 | **ACQUIRE ASSET **[one-action] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.772654 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/542` | 0.772035 | Acquire Asset |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.740106 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12` | 0.734745 | **GET 'EM! **[one-action]** TO **[two-actions] |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.723501 | **READY ARMS! **[one-action]** TO **[two-actions] |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.721497 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/13` | 0.720291 | **DON'T YOU DIE ON ME **[one-action] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/35` | 0.707742 | You gain the benefits of the 2-action Get 'Em! when using  1-action Get 'Em! on an asset. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.700167 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |

### Query 32
- Text: Summarize PLAYING THE CLASS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/11` | 0.973376 | PLAYING THE CLASS |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/1` | 0.780688 | CHAPTER 3: CLASSES |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/34` | 0.761442 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/45` | 0.761442 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/51` | 0.761442 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/61` | 0.761442 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/69` | 0.761442 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/19` | 0.761442 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/39` | 0.761442 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/42` | 0.761442 | **PLAYING THE ** **GAME** |

### Query 33
- Text: What are the requirements for **HANG IN THERE **[one-action] **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/5` | 0.927071 | **HANG IN THERE **[one-action] **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/14` | 0.765204 | **HURRY **[one-action] **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.724473 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/578` | 0.708143 | Hang in There |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.684086 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.678469 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/2` | 0.672677 | **DISTANT FEINT** **FEAT 6** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/40` | 0.655766 | 6TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/12` | 0.652846 | **Failure** The target is unaffected, and you can't use Hang in  There again for 1 minute. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/39` | 0.647411 | **KEEP ON KEEPING ON!** [one-action]** TO **[two-actions] |

### Query 34
- Text: What are the requirements for **Prerequisites** Charisma +2?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `51`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/29` | 0.974442 | **Prerequisites** Charisma +2 |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/8` | 0.815194 | **Prerequisites** Wisdom +2 |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/13` | 0.772850 | **Prerequisites** Dexterity +2 |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/8` | 0.770768 | **Prerequisites** Intelligence +2 |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/12` | 0.740350 | **Prerequisites** Constitution +2 |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/13` | 0.678959 | **Prerequisites** Strength +2 You gain the stellar attunement class feature (page 140), but |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25` | 0.653767 | **Prerequisites** Mystic Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/15` | 0.653767 | **Prerequisites** Mystic Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20` | 0.653767 | **Prerequisites** Mystic Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/36` | 0.653767 | **Prerequisites** Mystic Dedication |

### Query 35
- Text: What is the rule about A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is trained in Perception, a saving throw,  or another statistic, they gain a proficiency bonus equal to  their level + 2, while if they have expert proficiency, they  gain a proficiency bonus equal to their level + 4. For more  about proficiency ranks, see page 24.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `57`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 1.072806 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.913143 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/8` | 0.882664 | If something isn't listed in your character's class entry,  their proficiency rank in that statistic is untrained unless  they gain training from another source. If your character  is untrained in som |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.851435 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.827175 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/50` | 0.806080 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/3` | 0.792010 | You gain more skill increases than members of other classes.  At 2nd level and every level thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you' |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/25` | 0.788575 | You've learned a few tricks with your weapons. Your  proficiency ranks for simple weapons, martial weapons, and  unarmed attacks increase to expert. Whenever you attack  the target of your Get 'Em!, y |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.787534 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.786661 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |

### Query 36
- Text: Summarize DIM LIGHT
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `38`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/11` | 0.958163 | DIM LIGHT |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/7` | 0.701595 | LIGHT |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/2` | 0.650575 | LOW-LIGHT VISION |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/8` | 0.644149 | There are three levels of light: bright light, dim light, and  darkness. The rules in this book assume that all creatures are  in bright light unless otherwise noted. A source of light lists  the radi |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/9` | 0.640878 | BRIGHT LIGHT |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/3` | 0.601055 | A creature with low-light vision can see in dim light as though  it were bright light, so it ignores the concealed condition due  to dim light. |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/13` | 0.589777 | DARKNESS |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/12` | 0.585606 | Areas in shadow or lit by weak light sources are in dim  light. Creatures and objects in dim light have the concealed  condition, unless the seeker has darkvision or low-light vision  (page 425), or a |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/14` | 0.574869 | Chapter 4: Skills includes several downtime activities,  which are summarized here. |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/37` | 0.570636 | **Hit Points, ** **Healing, and ** **Dying** |

### Query 37
- Text: What is the rule about In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means sight. If you can't observe the creature,  it's either hidden, undetected, or unnoticed, and you'll need  to factor in the targeting restrictions. Even if a creature is  observed, it might still be concealed.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `52`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 1.063211 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.902142 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/20` | 0.890994 | Anything in plain view is observed by you. If a creature takes  measures to avoid detection, such as by using Stealth to Hide,  it can become hidden or undetected instead of observed. If you |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/9` | 0.880458 | Three conditions measure the degree to which you can sense  a creature: observed, hidden, and undetected. However, the  concealed and invisible conditions can partially mask a  creature, and the unnot |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` | 0.871737 | With the exception of invisible, these conditions are  relative to the viewer—it's possible for a creature to be  observed to you but hidden from your ally. Most of these  rules apply to objects as we |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.863683 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 0.858099 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.857650 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.857350 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/24` | 0.857056 | If a creature is undetected, you don't know what space it  occupies and you're off-guard to it. The Seek basic action can  help you find an undetected creature, usually making it hidden  from you inst |

### Query 38
- Text: What is the rule about There are four types of actions: single actions, activities,  reactions, and free actions.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `61`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/7` | 0.966302 | There are four types of actions: single actions, activities,  reactions, and free actions. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.770649 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.758127 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/3` | 0.740708 | Some actions, such as Step, specifically state  they don't trigger reactions or free actions based on  movement. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.725024 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.717473 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` | 0.716419 | Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action. |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/20` | 0.704924 | An activity typically involves using multiple actions to create  an effect greater than you can produce with a single action,  or combining multiple single actions to produce an effect  that's differe |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 0.701268 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/2` | 0.692391 | Some reactions and free actions are triggered by a  creature using an action with the move trait. The most  notable example is Reactive Strike (reproduced below).  Actions with the move trait can trig |

### Query 39
- Text: What are the requirements for **GUN EXPERT** **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/28` | 0.819406 | **GUN EXPERT** **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/17` | 0.687821 | **ADVANCED GUNNER** **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/21` | 0.649255 | **Prerequisites** Basic Gunner |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/32` | 0.641487 | Your proficiency ranks for simple and martial guns increase to  expert. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/47` | 0.639688 | **SOLAR MANIFESTATION EXPERT** **FEAT 12** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/2` | 0.633399 | You're a professional with crack aim and lethal instincts. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/65` | 0.628605 | **Prerequisites** Operative Dedication, class granting no more Hit  Points per level than 6 + your Constitution |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/33` | 0.626540 | **MASTER SPY** **FEAT 12** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/43` | 0.625486 | **EXPERT MYSTIC SPELLCASTING** **FEAT 12** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/31` | 0.619727 | **Prerequisites** Operative Dedication, expert in any kind of  weapon or unarmed attack |

### Query 40
- Text: Summarize BRIGHT LIGHT
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `32`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/9` | 0.920980 | BRIGHT LIGHT |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/7` | 0.787671 | LIGHT |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/11` | 0.664940 | DIM LIGHT |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/37` | 0.574901 | **Hit Points, ** **Healing, and ** **Dying** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/58` | 0.574901 | **Hit Points, ** **Healing, and ** **Dying** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/41` | 0.574901 | **Hit Points, ** **Healing, and ** **Dying** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/46` | 0.574901 | **Hit Points, ** **Healing, and ** **Dying** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/39` | 0.574901 | **Hit Points, ** **Healing, and ** **Dying** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/13` | 0.573112 | DARKNESS |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/2` | 0.570915 | LOW-LIGHT VISION |

### Query 41
- Text: Summarize The following clarifications might be relevant when  Aiding an ally.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/19` | 1.036344 | The following clarifications might be relevant when  Aiding an ally. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/9` | 0.797610 | **Requirements** The ally is willing to accept your aid, and you've  prepared to help (see below). |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/21` | 0.716146 | **Proximity:** You don't necessarily need to be next to  your ally to aid, though you must be in a reasonable  location to help them both when you set up and when  you take the reaction. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/10` | 0.712957 | You try to help your ally with a task. To use this reaction, you  must first prepare to help, usually by using an action during  your turn. You must explain to the GM exactly how you're trying  to hel |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.703410 | These rules clarify some of the specifics of using actions. |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/19` | 0.699844 | Some effects target or require an ally, or otherwise refer  to an ally. This must be someone on your side, often another  PC, but it might be a bystander you're trying to protect. You  don't count as |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/13` | 0.676241 | **Success** You grant your ally a +1 circumstance bonus to the  triggering check. |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/22` | 0.660503 | **Repetition:** Aiding the same creature multiple times  can have diminishing returns. In particular, if you  try to repeatedly Aid attacks or skill checks against  a creature, the GM will usually inc |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/30` | 0.654145 | You indicate a creature that you can see to one or more allies,  gesturing in a direction and describing the distance verbally.  That creature is hidden to your allies, rather than undetected  (page 4 |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/8` | 0.651098 | **Trigger** An ally is about to use an action that requires a skill  check or attack roll. |

### Query 42
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/35']
- Expected found: `True`
- Expected rank: `23`
- Graph boost applied: `True`
- Graph boosted count: `64`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/23` | 0.937823 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/54` | 0.937823 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/59` | 0.937823 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/64` | 0.937823 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/18` | 0.937823 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/44` | 0.937823 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/39` | 0.937823 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/49` | 0.937823 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/30` | 0.937823 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/35` | 0.937823 | **ARCHETYPE** |

### Query 43
- Text: What is the rule about When the GM calls for it, you'll roll initiative to determine  your place in the initiative order, which is the sequence in  which the encounter's participants will take their turns.  Rolling initiative marks the start of an encounter. More often  than not, you'll roll initiative when you enter a battle.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `36`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/6` | 1.071672 | When the GM calls for it, you'll roll initiative to determine  your place in the initiative order, which is the sequence in  which the encounter's participants will take their turns.  Rolling initiati |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/9` | 0.864465 | Unlike a check, where the result is compared to a DC, the  results of initiative rolls are ranked. This ranking sets the  order in which the encounter's participants act—the initiative  order. The cha |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/4` | 0.860121 | An encounter is played out in a series of rounds, during which  the player characters, adversaries, and other participants in the  encounter act in sequence. You roll initiative to determine this  ord |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/8` | 0.852547 | The GM rolls initiative for anyone other than the player  characters in the encounter. If these include a number of  identical creatures, the GM could roll once for the group as a  whole and have them |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/2` | 0.851493 | The GM keeps track of the initiative order for an  encounter. It's usually okay for the players to know  this order since they'll see who goes when and be  aware of one another's results. However, the |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/15` | 0.843590 | Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/13` | 0.809649 | A round begins when the participant with the highest  initiative roll result starts their turn, and it ends when the  one with the lowest initiative ends their turn. The process  of taking a turn is d |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/10` | 0.798529 | If your result is tied with an enemy's result, the enemy  goes first. If your result is tied with another PC's, you can  decide between yourselves who goes first when you reach  that place in the init |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/7` | 0.792173 | Typically, you'll roll a Perception check to determine your  initiative—the more aware you are of your surroundings,  the more quickly you can respond. Sometimes, though, the  GM might call on you to |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/6` | 0.787732 | Perception is frequently used for rolling initiative in an  encounter, and for the Seek action. See page 396 for the  procedure for rolling a Perception check. |

### Query 44
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/18']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `16`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/38` | 0.856592 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/50` | 0.856592 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/68` | 0.856592 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/60` | 0.856592 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/44` | 0.856592 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/18` | 0.856592 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/41` | 0.856592 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/33` | 0.856592 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/33` | 0.756592 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/36` | 0.756592 | **SPELLS** |

### Query 45
- Text: Summarize **Effects**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/43']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `29`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/62` | 0.956705 | **Effects** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/50` | 0.956705 | **Effects** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/43` | 0.956705 | **Effects** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/41` | 0.956705 | **Effects** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/45` | 0.889083 | **Effects** **Area** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/44` | 0.856705 | **Effects** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/18` | 0.856705 | **Effects** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/39` | 0.856705 | **Effects** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/63` | 0.856705 | **Effects** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/29` | 0.856705 | **Effects** |

### Query 46
- Text: Summarize **CONCENTRATE** **SECRET**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `29`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/15` | 1.017915 | **CONCENTRATE** **SECRET** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/27` | 1.017915 | **CONCENTRATE** **SECRET** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/7` | 0.926715 | **CONCENTRATE** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/40` | 0.926715 | **CONCENTRATE** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/8` | 0.926715 | **CONCENTRATE** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/42` | 0.793178 | **CONCENTRATE** **ENVOY** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/8/SectionHeader/15` | 0.772466 | **CONCENTRATE** **EXPLORATION** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/8/SectionHeader/12` | 0.772466 | **CONCENTRATE** **EXPLORATION** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/8/SectionHeader/9` | 0.772466 | **CONCENTRATE** **EXPLORATION** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/6/SectionHeader/26` | 0.772466 | **CONCENTRATE** **EXPLORATION** |

### Query 47
- Text: What is the rule about Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each class provides your character  with an attribute boost to a key attribute; a number of  Hit Points they receive at each level; proficiency ranks for  various abilities, equipment, and skills; special abilities?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `52`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 1.048194 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/10` | 0.891455 | from their class features; and more. Your character's class  entry also provides the information needed when they  gain levels, so it will be a vital reference throughout the  course of your campaign. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` | 0.875462 | This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chos |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.845384 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.827811 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.826668 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.814250 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 0.809846 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 0.808937 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 0.806566 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |

### Query 48
- Text: What are the requirements for **Prerequisites** Operative Dedication, expert in any kind of  weapon or unarmed attack?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `57`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/31` | 0.968760 | **Prerequisites** Operative Dedication, expert in any kind of  weapon or unarmed attack |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/50` | 0.874259 | **Prerequisites** Solarian Dedication, expert in any kind of  weapon or unarmed attack |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.856239 | **Prerequisites** Operative Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.856239 | **Prerequisites** Operative Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.856239 | **Prerequisites** Operative Dedication |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/36` | 0.833684 | **Prerequisites** Operative Dedication, expert in Perception |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/65` | 0.770926 | **Prerequisites** Operative Dedication, class granting no more Hit  Points per level than 6 + your Constitution |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/44` | 0.753647 | **Prerequisites** Soldier Dedication, expert in Fortitude saves. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/39` | 0.739138 | **Prerequisites** Soldier Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/18` | 0.739138 | **Prerequisites** Soldier Dedication |

### Query 49
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/17']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `29`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/59` | 0.965652 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/43` | 0.965652 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/37` | 0.965652 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/40` | 0.965652 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/49` | 0.965652 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/32` | 0.965652 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/17` | 0.965652 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/67` | 0.965652 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/35` | 0.865652 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/31` | 0.865652 | **EQUIPMENT** |

### Query 50
- Text: What is the rule about Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the cycle until the encounter ends.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `44`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/15` | 1.023099 | Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/4` | 0.851427 | An encounter is played out in a series of rounds, during which  the player characters, adversaries, and other participants in the  encounter act in sequence. You roll initiative to determine this  ord |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/13` | 0.845920 | A round begins when the participant with the highest  initiative roll result starts their turn, and it ends when the  one with the lowest initiative ends their turn. The process  of taking a turn is d |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/6` | 0.814557 | When the GM calls for it, you'll roll initiative to determine  your place in the initiative order, which is the sequence in  which the encounter's participants will take their turns.  Rolling initiati |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/9` | 0.797167 | Unlike a check, where the result is compared to a DC, the  results of initiative rolls are ranked. This ranking sets the  order in which the encounter's participants act—the initiative  order. The cha |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/18` | 0.790350 | Once you've done all the things you want to do with the actions  you have available, you reach the end of your turn. Take the  following steps in any order you choose. Play then proceeds to  the next |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/8` | 0.758745 | The GM rolls initiative for anyone other than the player  characters in the encounter. If these include a number of  identical creatures, the GM could roll once for the group as a  whole and have them |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/21` | 0.745843 | Many things happen automatically at the start of your turn it's a common point for tracking the passage of time for  effects that last multiple rounds. At the start of each of your  turns, take these |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/11` | 0.744798 | initiative order usually don't change during the encounter.  (But see the Delay basic action on page 408.) |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/17` | 0.742657 | When your foes are defeated, some sort of truce is reached,  or some other event or circumstance ends the combat, the  encounter is over. You and the other participants no longer  follow the initiativ |

### Query 51
- Text: What is the rule about When every individual action counts, you enter the encounter mode of play. In this mode, time  is divided into rounds, each of which is 6 seconds of time in the game world. Every round, each  participant takes a turn in an established order. During your turn, you can use actions, and depending  on the details of the encounter, you might have the opportunity to use reactions and free actions on  your own turn and on others' turns.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `47`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/1` | 1.024380 | When every individual action counts, you enter the encounter mode of play. In this mode, time  is divided into rounds, each of which is 6 seconds of time in the game world. Every round, each  particip |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/4` | 0.848043 | An encounter is played out in a series of rounds, during which  the player characters, adversaries, and other participants in the  encounter act in sequence. You roll initiative to determine this  ord |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/24` | 0.801526 | Activities that take longer than a turn can't normally be  performed during an encounter. Spells with a casting time of  1 minute or more are a common example, as are several skill  actions. When you |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/15` | 0.782378 | Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/26` | 0.781386 | Your reactions let you respond immediately to what's  happening around you. The GM determines whether you can  use reactions before your first turn begins, depending on the  situation in which the enc |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/21` | 0.776818 | Many things happen automatically at the start of your turn it's a common point for tracking the passage of time for  effects that last multiple rounds. At the start of each of your  turns, take these |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/13` | 0.747425 | A round begins when the participant with the highest  initiative roll result starts their turn, and it ends when the  one with the lowest initiative ends their turn. The process  of taking a turn is d |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/19` | 0.743784 | When it's your turn to act, you can use single actions ([one-action]),  short activities ([two-actions] and [three-actions]), reactions ([reaction]), and free actions  ([free-action]). When you're fin |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/6` | 0.736977 | your first turn of a fight, it would affect you during that  turn, decrease to 2 rounds of duration at the start of your  second turn, decrease to 1 round of duration at the start of  your third turn, |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/13` | 0.736955 | You can use actions in any order you wish during your  turn, but you have to complete one action or activity before  beginning another; for example, you can't use a single action in  the middle of per |

### Query 52
- Text: Summarize At 1st level, your class gives you  an attribute boost to Charisma.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `61`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/6` | 1.058617 | At 1st level, your class gives you  an attribute boost to Charisma. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/4` | 0.858848 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.843946 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.816554 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/15` | 0.804238 | **Lead by Example** If you used two actions, Strike the target.  You gain a status bonus to the damage roll equal to your  Charisma modifier. Regardless of whether the Strike hits, you  and your allie |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/1` | 0.803958 | designated target. Your ally gains a status bonus to damage  equal to your Charisma modifier. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/29` | 0.796335 | In addition to what you get from your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/7` | 0.794295 | At 1st level, you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start  of this class. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/11` | 0.789176 | **Success** The target gains temporary Hit Points equal to their  level plus your Charisma modifier. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/Table/2` | 0.785326 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat2Envoy feat, skill feat, skill increase3Adaptive talent, genera |

### Query 53
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/24']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `31`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/26` | 0.827771 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/50` | 0.827771 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/23` | 0.827771 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/5` | 0.827771 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/16` | 0.827771 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/37` | 0.827771 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/24` | 0.827771 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/30` | 0.827771 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/27` | 0.825791 | SKILLS |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/29` | 0.727771 | **SKILLS** |

### Query 54
- Text: Summarize The shirren mystic **Chk Chk** worships Zon-Shelyn, the god of creating art from suffering.  He enjoys creatively expressing himself by  writing poetry and dueling enemies with his painglaive.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/27` | 1.086880 | The shirren mystic **Chk Chk** worships Zon-Shelyn, the god of creating art from suffering.  He enjoys creatively expressing himself by  writing poetry and dueling enemies with his painglaive. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/44` | 0.629389 | **Zemir** the human witchwarper jumps between  realities and timelines, trusting his uncanny  luck and years of experience to keep him  anchored while searching for the loved ones he  lost years ago t |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/24` | 0.601466 | The mystic is a spellcaster with a connection  to a divine, occult, or primal aspect of the universe. A  mystic casts powerful spells, learning new epiphanies  based on their chosen connection, and he |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/26` | 0.595916 | **Chk Chk** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/23` | 0.586571 | **Trigger** A creature targets you with a melee attack. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/48` | 0.576128 | attacks while soaking attacks from enemies. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/9/SectionHeader/4` | 0.575768 | **DIRECTIVE** **ENVOY** **HEALING** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/11` | 0.571797 | The solarian is a warrior who channels the  cosmic cycle. Every solarian creates weapons of pure  stellar energy that they can manifest at will. Cycling  between graviton and photon attunement, a sola |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/14` | 0.565632 | The pahtra solarian **Dae** loves showing off  by combining their flashy dance moves with  solar flares or turning their battle ribbon into  a electrotether or a whip of solar fire. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/25` | 0.563560 | **Mystic** |

### Query 55
- Text: Summarize LOW-LIGHT VISION
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `43`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/2` | 0.962474 | LOW-LIGHT VISION |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/7` | 0.720032 | LIGHT |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/11` | 0.701659 | DIM LIGHT |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/3` | 0.680799 | A creature with low-light vision can see in dim light as though  it were bright light, so it ignores the concealed condition due  to dim light. |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/1` | 0.678754 | PERCEPTION AND  DETECTION |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15` | 0.669512 | **DETECTING WITH OTHER SENSES** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/12` | 0.667601 | Areas in shadow or lit by weak light sources are in dim  light. Creatures and objects in dim light have the concealed  condition, unless the seeker has darkvision or low-light vision  (page 425), or a |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/7/SectionHeader/3` | 0.661898 | **AUDITORY** **CONCENTRATE** **EXPLORATION** **VISUAL** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/8` | 0.658129 | DETECTING CREATURES |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/10` | 0.656027 | In bright light, such as sunlight, creatures and objects can  be observed clearly by anyone with average vision or better. |

### Query 56
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/20']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `26`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/52` | 1.000802 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/62` | 1.000802 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/70` | 1.000802 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/43` | 1.000802 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/35` | 1.000802 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/40` | 1.000802 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/20` | 1.000802 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/46` | 1.000802 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/31` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/37` | 0.900802 | **CONDITIONS ** **APPENDIX** |

### Query 57
- Text: What are the requirements for **Prerequisites** Envoy Dedication?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/39']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/19` | 0.977387 | **Prerequisites** Envoy Dedication |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/24` | 0.977387 | **Prerequisites** Envoy Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/34` | 0.977387 | **Prerequisites** Envoy Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/39` | 0.977387 | **Prerequisites** Envoy Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/18` | 0.814548 | **Prerequisites** Soldier Dedication |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/39` | 0.814548 | **Prerequisites** Soldier Dedication |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/34` | 0.814548 | **Prerequisites** Soldier Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.795225 | **Prerequisites** Operative Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.795225 | **Prerequisites** Operative Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.795225 | **Prerequisites** Operative Dedication |

### Query 58
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `26`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/52` | 1.000802 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/62` | 1.000802 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/70` | 1.000802 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/43` | 1.000802 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/35` | 1.000802 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/40` | 1.000802 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/20` | 1.000802 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/46` | 1.000802 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/31` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/37` | 0.900802 | **CONDITIONS ** **APPENDIX** |

### Query 59
- Text: Summarize In bright light, such as sunlight, creatures and objects can  be observed clearly by anyone with average vision or better.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `58`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/10` | 1.071085 | In bright light, such as sunlight, creatures and objects can  be observed clearly by anyone with average vision or better. |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/28` | 0.808188 | A creature with darkvision or greater darkvision can see  perfectly well in areas of darkness and dim light, though |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/3` | 0.803111 | A creature with low-light vision can see in dim light as though  it were bright light, so it ignores the concealed condition due  to dim light. |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/12` | 0.802801 | Areas in shadow or lit by weak light sources are in dim  light. Creatures and objects in dim light have the concealed  condition, unless the seeker has darkvision or low-light vision  (page 425), or a |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/14` | 0.786498 | A creature or object within darkness is hidden or undetected  unless the seeker has darkvision or a precise sense other  than vision. A creature without darkvision or another means  of perceiving in d |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.774316 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/18` | 0.767840 | Average vision is a precise sense—a sense that can be used to  perceive the world in nuanced detail. The only way to target |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/8` | 0.764396 | There are three levels of light: bright light, dim light, and  darkness. The rules in this book assume that all creatures are  in bright light unless otherwise noted. A source of light lists  the radi |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/20` | 0.761181 | Anything in plain view is observed by you. If a creature takes  measures to avoid detection, such as by using Stealth to Hide,  it can become hidden or undetected instead of observed. If you |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` | 0.745553 | With the exception of invisible, these conditions are  relative to the viewer—it's possible for a creature to be  observed to you but hidden from your ally. Most of these  rules apply to objects as we |

### Query 60
- Text: What is the rule about ACTIONS WITH TRIGGERS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `53`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/26` | 0.865806 | ACTIONS WITH TRIGGERS |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/29` | 0.779522 | LIMITATIONS ON TRIGGERS |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.693440 | These rules clarify some of the specifics of using actions. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.666045 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/10` | 0.663992 | **IN-DEPTH ACTION RULES** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/2` | 0.663581 | Some reactions and free actions are triggered by a  creature using an action with the move trait. The most  notable example is Reactive Strike (reproduced below).  Actions with the move trait can trig |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.654270 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` | 0.653340 | **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reac |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/1` | 0.651076 | ACTIONS |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` | 0.650367 | Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action. |

### Query 61
- Text: What is the rule about You're a professional with crack aim and lethal instincts.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `12`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/2` | 0.913331 | You're a professional with crack aim and lethal instincts. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/32` | 0.684344 | Your proficiency ranks for simple and martial guns increase to  expert. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/51` | 0.624945 | Your proficiency ranks for solar flare and solar weapon  increase to expert. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/31` | 0.621548 | **Prerequisites** Operative Dedication, expert in any kind of  weapon or unarmed attack |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/2` | 0.618759 | You step up and lead others to victory while manipulating  those who stand in your way. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/10` | 0.604229 | You lead your team by making an impression with firepower.  Your bombastic personality has a barrage of gunfire to back it  up, and you always shoot first. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/51` | 0.603029 | You gain a 1st- or 2nd-level operative feat. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/37` | 0.596103 | Your proficiency rank for Perception increases to master. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/4` | 0.594428 | The soldier archetype is ideal for characters who want to  specialize in area attacks. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/51` | 0.592955 | **Prerequisites** Expert Mystic Spellcasting; legendary in  connection skill |

### Query 62
- Text: What are the requirements for **Prerequisites** trained in Deception or Diplomacy?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `38`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25` | 0.999447 | **Prerequisites** trained in Deception or Diplomacy |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/22` | 0.884922 | **Prerequisites** trained in Deception |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/23` | 0.884922 | **Prerequisites** trained in Deception |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/56` | 0.837855 | Trained in one of the following skills  of your choice: Deception, Diplomacy,  Intimidation |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/5` | 0.809953 | **Prerequisites** master in Deception |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.773755 | **Prerequisites** trained in Intimidation |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/8` | 0.759416 | **Prerequisites** expert in Diplomacy |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/12` | 0.706222 | **Trigger** You roll a skill check for any of the following skills  you're legendary in: Deception, Diplomacy, Intimidation, or  your leadership skill. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/46` | 0.691225 | **Prerequisites** master in Intimidation |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/33` | 0.691211 | **Trigger** You're about to roll a Deception, Diplomacy, or  Intimidation check, but you haven't rolled yet. |

### Query 63
- Text: What is the rule about **Master Spellcasting Feat:** Usually found at 18th level, these  feats make you a master in spell attack modifiers and spell  DCs and grant you a 7th-rank spell slot. If you have a spell  repertoire, you can select a third spell from your repertoire as  a signature spell. At 20th level, they grant you an 8th-rank  spell slot. Archetypes refer to these benefits as the "master  spellcasting benefits."?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `36`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/19` | 1.063368 | **Master Spellcasting Feat:** Usually found at 18th level, these  feats make you a master in spell attack modifiers and spell  DCs and grant you a 7th-rank spell slot. If you have a spell  repertoire, |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/18` | 0.946893 | **Expert Spellcasting Feat:** Typically taken at 12th level,  these feats make you an expert in spell attack modifiers  and spell DCs and grant you a 4th-rank spell slot. If you  have a spell repertoi |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/17` | 0.926958 | **Basic Spellcasting Feat:** Usually available at 4th level,  these feats grant a 1st-rank spell slot. At 6th level, they  grant you a 2nd-rank spell slot, and if you have a spell  repertoire, you can |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.782724 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/52` | 0.773310 | You gain the master spellcasting benefits (page 174). |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/50` | 0.773310 | You gain the master spellcasting benefits (page 174). |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.757079 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/29` | 0.748350 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the witchwarper  archetype, add a spell of the appropriate spell rank to your  repertoire: a co |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/10` | 0.737820 | You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by you |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/42` | 0.727984 | Increase the number of spells in your repertoire and number  of spell slots you gain from mystic archetype feats by 1 for  each spell rank other than your two highest mystic spell slots. |

### Query 64
- Text: Summarize **Exploration ** **Mode**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `45`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/43` | 0.962946 | **Exploration ** **Mode** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/35` | 0.962946 | **Exploration ** **Mode** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/44` | 0.962946 | **Exploration ** **Mode** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/68` | 0.962946 | **Exploration ** **Mode** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/49` | 0.962946 | **Exploration ** **Mode** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/55` | 0.962946 | **Exploration ** **Mode** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/25` | 0.900592 | **Exploration ** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/41` | 0.900592 | **Exploration ** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/48` | 0.862946 | **Exploration ** **Mode** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/46` | 0.862946 | **Exploration ** **Mode** |

### Query 65
- Text: Summarize **Charisma**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `21`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/5` | 0.930013 | **Charisma** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/11` | 0.676498 | **Success** The target gains temporary Hit Points equal to their  level plus your Charisma modifier. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/10` | 0.663203 | **Critical Success** The target gains temporary Hit Points equal  to double their level plus your Charisma modifier. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/29` | 0.662268 | **Prerequisites** Charisma +2 |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/4` | 0.659826 | **KEY ATTRIBUTE** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/4` | 0.657671 | **Attributes** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/9/SectionHeader/4` | 0.657506 | **DIRECTIVE** **ENVOY** **HEALING** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/8` | 0.654024 | **Leadership Style** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/55` | 0.651811 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/5` | 0.649935 | Prioritize Charisma. Dexterity, Intelligence, and  Constitution round out your abilities and defenses. |

### Query 66
- Text: What is the rule about Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `52`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` | 0.966992 | Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.880046 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.871151 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.864627 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/2` | 0.781847 | Some reactions and free actions are triggered by a  creature using an action with the move trait. The most  notable example is Reactive Strike (reproduced below).  Actions with the move trait can trig |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.768444 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` | 0.758296 | **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reac |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/8` | 0.757185 | You prepare to use an action that will occur outside your  turn. Choose a single action or free action you can use, and  designate a trigger. Your turn then ends. If the trigger you  designated occurs |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 0.743304 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/9` | 0.703218 | Various abilities and conditions, such as a Reactive Strike,  can disrupt an action. When an action is disrupted, you still  use the actions or reactions you committed, and you still  expend any costs |

### Query 67
- Text: What is the rule about Operative envoys become incredibly precise killing  machines that can combine Aim with abilities like Get  'em! and Distant Feint. Ghost operatives also appreciate  extra feats that use Deception.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `33`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/6` | 1.000059 | Operative envoys become incredibly precise killing  machines that can combine Aim with abilities like Get  'em! and Distant Feint. Ghost operatives also appreciate  extra feats that use Deception. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/ListItem/5` | 0.732256 | Envoy operatives direct allies while lining up perfect shots. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/8` | 0.726016 | Soldier envoys make natural commanders who can  use their defensive capabilities to keep the bonuses  of their directive's active against powerful enemies  while clearing out weaker foes with area fir |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/30` | 0.670415 | You gain the envoy directives class feature (see page  104), but do not gain the Lead by Example benefits  of the Get 'Em! envoy directive. You become trained in  Deception, Diplomacy, or Intimidation |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/2` | 0.652892 | You're a professional with crack aim and lethal instincts. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/ListItem/5` | 0.649302 | Envoy soldiers are natural tacticians who use directives to  position enemies and allies to optimize their area attacks. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/5` | 0.646784 | Mystic envoys can choose between using their magic  or directives to empower their allies, widening the  breadth of options available to them. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/ListItem/7` | 0.642217 | Operative soldiers become versatile damage dealers  that can use their area weapons in situations where Aim  isn't as useful. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/35` | 0.637773 | You gain a 1st- or 2nd-level envoy feat of your choice. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/15` | 0.637606 | **Special** You can select this feat more than once. Each time  you select it, you gain another envoy feat. |

### Query 68
- Text: What is the rule about Class Feats?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `41`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/14` | 0.851346 | Class Feats |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.720953 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26` | 0.713435 | CLASS FEATURES |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11` | 0.713435 | CLASS FEATURES |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/408` | 0.695422 | Class Features |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16` | 0.644521 | Skill Feats |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/18` | 0.637776 | General Feats |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.636781 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.632916 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/11` | 0.623880 | PLAYING THE CLASS |

### Query 69
- Text: What is the rule about Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidden condition instead of the observed condition.  It might be undetected by you if it's using Stealth or in an  environment that distorts the sense, such as a noisy room  in the case of hearing. In those cases, you have to use the  Seek basic action to detect the creature. At best, an imprecise  sense can be used to make an undetected creature (or one  you didn't even know was there) merely hidden—it can't make  the creature observed.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `62`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 1.077983 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.889289 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/21` | 0.873765 | A creature that's hidden is only barely perceptible. You only  know what space it occupies. Perhaps the creature just used  the Hide action. Your target might be behind some obstruction,  where you ca |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.873622 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/24` | 0.870442 | If a creature is undetected, you don't know what space it  occupies and you're off-guard to it. The Seek basic action can  help you find an undetected creature, usually making it hidden  from you inst |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 0.864841 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.861333 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.858624 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.847588 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/23` | 0.841635 | A character also has many vague senses—ones that can alert  you that something is there but aren't useful for zeroing in on  it to determine exactly what it is. The most useful of these  for a typical |

### Query 70
- Text: Summarize **Archetypes**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/52']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `62`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/38` | 0.968834 | **Archetypes** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/52` | 0.968834 | **Archetypes** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/46` | 0.968834 | **Archetypes** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/56` | 0.968834 | **Archetypes** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/35` | 0.890248 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/49` | 0.890248 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/27` | 0.890248 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16` | 0.890248 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21` | 0.890248 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/33` | 0.890248 | **ARCHETYPE** |

### Query 71
- Text: Summarize **Mystic**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/47']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `26`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/41` | 0.903583 | **Mystic** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/47` | 0.903583 | **Mystic** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/51` | 0.903583 | **Mystic** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/25` | 0.803583 | **Mystic** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/35` | 0.803583 | **Mystic** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/30` | 0.803583 | **Mystic** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/60` | 0.803583 | **Mystic** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/52` | 0.803583 | **Mystic** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/42` | 0.803583 | **Mystic** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/1` | 0.791345 | MYSTIC |

### Query 72
- Text: What is the rule about attacks while soaking attacks from enemies.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/48']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `46`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/48` | 0.905277 | attacks while soaking attacks from enemies. |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/23` | 0.678846 | Use these rules for battles in water or underwater. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/8` | 0.669914 | **Lead by Example** If you used two actions, Hide or Sneak.  Until the start of your next turn, you can Strike the enemy  target as a reaction the first time the ally you targeted attacks  your design |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/20` | 0.656930 | You succinctly direct your allies to find cover by any means  necessary. You and all allies within 60 feet count any form of  lesser cover as standard cover until the start of your next turn. **Lead b |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/27` | 0.652861 | When you warn an ally of an attack, you follow up with a  shot at your enemy. The first time each round you use your  Watch Out reaction, you can make a melee or ranged Strike  against the triggering |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/29` | 0.650934 | **Trigger** A creature within 30 feet is damaged by an ally's Strike. You follow up on your ally's success by hurling a cunning, welltimed taunt at a foe they wounded. Attempt to Demoralize the  trigg |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/12` | 0.648296 | When the target you directed your allies to take down falls  unconscious or is destroyed, you quickly direct them at another  target. You use Get 'Em! against a new target following all the  normal ta |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/5/ListItem/26` | 0.641454 | You take a –2 circumstance penalty to your attack rolls for  bludgeoning or slashing attacks that pass through water. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/18` | 0.640817 | You follow-up your issued directive with an understood  order by attacking a notable foe. Make a Strike. If the Strike  hits, the target is affected by a 1-action Get 'Em. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/14` | 0.637124 | You single out an enemy for you and your allies to focus your  attacks on. Select an enemy within 60 feet that you can see.  You and your allies gain a +1 status bonus to attacks against  that target |

### Query 73
- Text: What are the requirements for **LEADER'S CONFIDENCE** **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `39`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/21` | 0.872437 | **LEADER'S CONFIDENCE** **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/25` | 0.698972 | You gain the leader's confidence class feature (see page  107). |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/28` | 0.667414 | **GUN EXPERT** **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/13` | 0.663650 | **Prerequisites** Basic Leadership |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/31` | 0.659492 | **BASIC LEADERSHIP** **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/10` | 0.652581 | **ADVANCED LEADERSHIP** **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/41` | 0.637142 | **SOLDIER'S TOUGHNESS** **FEAT 12** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/47` | 0.637092 | **SOLAR MANIFESTATION EXPERT** **FEAT 12** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/33` | 0.634898 | **MASTER SPY** **FEAT 12** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/43` | 0.626892 | **EXPERT MYSTIC SPELLCASTING** **FEAT 12** |

### Query 74
- Text: Summarize **Perception and ** **Detection**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/53']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `42`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/41` | 0.999207 | **Perception and ** **Detection** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/53` | 0.999207 | **Perception and ** **Detection** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/66` | 0.999207 | **Perception and ** **Detection** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/33` | 0.999207 | **Perception and ** **Detection** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/42` | 0.937320 | **Perception and ** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/39` | 0.937320 | **Perception and ** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/47` | 0.937320 | **Perception and ** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/50` | 0.937320 | **Perception and ** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/46` | 0.899207 | **Perception and ** **Detection** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/65` | 0.899207 | **Perception and ** **Detection** |

### Query 75
- Text: What are the requirements for **EXPANDED CONNECTION** **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/38']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/38` | 0.902482 | **EXPANDED CONNECTION** **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/16` | 0.716889 | **REALLY GET EM!** **FEAT 8** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/24` | 0.712432 | **OPERATIVE EXPLOIT** **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/36` | 0.711568 | **QUANTUM BREADTH** **FEAT 8** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/19` | 0.703181 | **STARFINDER PROVISIONS** **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/10` | 0.681565 | ADDITIONAL FEATS |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/25` | 0.678408 | **VETERAN TRAP FINDER** **FEAT 8** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/31` | 0.667277 | **ADVANCED STELLAR ATTUNEMENT** **FEAT 6** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/17` | 0.664927 | **ADVANCED GUNNER** **FEAT 6** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/30` | 0.661381 | **ADVANCED DISTORTION** **FEAT 6** |

### Query 76
- Text: What is the rule about Various abilities and conditions, such as a Reactive Strike,  can disrupt an action. When an action is disrupted, you still  use the actions or reactions you committed, and you still  expend any costs, but the action's effects don't occur. In the?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `52`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/9` | 1.011586 | Various abilities and conditions, such as a Reactive Strike,  can disrupt an action. When an action is disrupted, you still  use the actions or reactions you committed, and you still  expend any costs |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` | 0.774708 | Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or S |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.768386 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/25` | 0.763280 | If an activity outside of an encounter is interrupted or  disrupted, as described in Disrupting Actions on page 407,  you usually lose the time you put in, but no additional time. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/7` | 0.761432 | Some effects are even more restrictive. Certain abilities,  instead of or in addition to changing the number of actions  you can use, say specifically that you can't use reactions.  The most restricti |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.761060 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/18` | 0.750102 | case of an activity, you usually lose all actions spent for the  activity up through the end of that turn. For instance, if you  began to Cast a Spell requiring 3 actions and the first action  was dis |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/16` | 0.738959 | An action might allow you to use a simpler action usually one of the Basic Actions on page 408—in a  different circumstance or with different effects. This  subordinate action still has its normal tra |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/2` | 0.735362 | Some reactions and free actions are triggered by a  creature using an action with the move trait. The most  notable example is Reactive Strike (reproduced below).  Actions with the move trait can trig |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` | 0.734239 | Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action. |

### Query 77
- Text: What is the rule about You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its trigger is satisfied—and *only* when it's satisfied—you  can use the reaction or free action, though you don't have to  use the action if you don't want to.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `56`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 1.038700 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.905170 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.902617 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` | 0.891135 | Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` | 0.846852 | **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reac |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/8` | 0.837888 | You prepare to use an action that will occur outside your  turn. Choose a single action or free action you can use, and  designate a trigger. Your turn then ends. If the trigger you  designated occurs |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/2` | 0.822657 | Some reactions and free actions are triggered by a  creature using an action with the move trait. The most  notable example is Reactive Strike (reproduced below).  Actions with the move trait can trig |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.788007 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 0.781007 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/9` | 0.747330 | Various abilities and conditions, such as a Reactive Strike,  can disrupt an action. When an action is disrupted, you still  use the actions or reactions you committed, and you still  expend any costs |

### Query 78
- Text: What is the rule about You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by your connection, or any other cantrips of that  tradition you learn or discover. You're trained in the spell  attack modifier and spell DC statistics. Your key spellcasting  attribute for mystic archetype spells is Wisdom, and they are  mystic spells of your connection's tradition.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `37`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/10` | 1.045594 | You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by you |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/10` | 0.927623 | You cast spells like a witchwarper. You gain access to the Cast  a Spell activity. You gain a spell repertoire with two common  cantrips from the spell list associated with your paradox, from  the spe |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.865421 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.856380 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/29` | 0.785456 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the witchwarper  archetype, add a spell of the appropriate spell rank to your  repertoire: a co |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/42` | 0.757658 | Increase the number of spells in your repertoire and number  of spell slots you gain from mystic archetype feats by 1 for  each spell rank other than your two highest mystic spell slots. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/40` | 0.752322 | Your repertoire expands, and you can cast more spells of your  paradox's tradition each day. Increase the number of spells  in your repertoire and number of spell slots you gain from  witchwarper arch |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/9` | 0.750201 | Choose a connection (see page 119). You become trained in  the connection's skill or, if you were already trained, you  become trained in a skill of your choice. You don't gain any  other abilities fr |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/15` | 0.736222 | Some archetypes grant you a substantial degree of  spellcasting, albeit delayed compared to a character from a  spellcasting class. The spellcasting ability from a spellcasting  archetype also allows |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/19` | 0.723679 | **Master Spellcasting Feat:** Usually found at 18th level, these  feats make you a master in spell attack modifiers and spell  DCs and grant you a 7th-rank spell slot. If you have a spell  repertoire, |

### Query 79
- Text: What is the rule about For instance, this is the attribute modifier you'll use to  determine the Difficulty Class (DC) associated with your  character's class features and feats. This is called your  class DC. If your character is a member of a spellcasting  class, this key attribute is used to calculate spell DCs and  similar values.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `33`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/15` | 1.031421 | For instance, this is the attribute modifier you'll use to  determine the Difficulty Class (DC) associated with your  character's class features and feats. This is called your  class DC. If your chara |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/14` | 0.791741 | This is the attribute modifier that a member of your class  cares about the most. Many of your most useful and  powerful abilities are tied to this attribute in some way. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 0.755735 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.754684 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.745862 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` | 0.740597 | This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chos |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/7` | 0.738979 | Spellcasting classes grant a proficiency rank for spell  attacks and DCs, which are further detailed in each class's  entry. These classes rarely use their class DC. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` | 0.738207 | Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  char |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/16` | 0.735026 | Most classes are associated with one key attribute  modifier, but some allow you to choose from two options.  For instance, if you're a witchwarper, you can choose  either Intelligence or Charisma as |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.732662 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |

### Query 80
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/41']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `12`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/49` | 0.965652 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/60` | 0.965652 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/41` | 0.965652 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/55` | 0.965652 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/32` | 0.865652 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/59` | 0.865652 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/40` | 0.865652 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/17` | 0.865652 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/32` | 0.865652 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/28` | 0.865652 | **EQUIPMENT** |

### Query 81
- Text: What is the rule about This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `52`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 1.039891 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.863950 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.862170 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.854382 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/27` | 0.848026 | You gain these abilities as an envoy. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.842039 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.837589 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.826032 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.822329 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/3` | 0.811700 | You gain more skill increases than members of other classes.  At 2nd level and every level thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you' |

### Query 82
- Text: What is the rule about Typically, the GM tracks how well creatures detect each  other since neither party has perfect information. For  example, you might think a creature is in the last place  you sensed it, but it was able to Sneak away. Or you  might think a creature can't see you in the dark, but it has  darkvision.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `58`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/11` | 1.063724 | Typically, the GM tracks how well creatures detect each  other since neither party has perfect information. For  example, you might think a creature is in the last place  you sensed it, but it was abl |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/14` | 0.818082 | A creature or object within darkness is hidden or undetected  unless the seeker has darkvision or a precise sense other  than vision. A creature without darkvision or another means  of perceiving in d |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/24` | 0.813204 | When one creature might detect another, the GM almost  always uses the most precise sense available. |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/2` | 0.806528 | The GM keeps track of the initiative order for an  encounter. It's usually okay for the players to know  this order since they'll see who goes when and be  aware of one another's results. However, the |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` | 0.797712 | With the exception of invisible, these conditions are  relative to the viewer—it's possible for a creature to be  observed to you but hidden from your ally. Most of these  rules apply to objects as we |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.793397 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/17` | 0.768020 | The GM attempts a single secret Perception check for  you and compares the result to the Stealth DCs of any  undetected or hidden creatures in the area, or the DC to  detect each object in the area (a |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/16` | 0.766710 | Most abilities that designate "a creature you can see"  or the like function just as well if the user can precisely  sense the subject with a different sense. If a monster  uses a sense other than vis |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.761180 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/21` | 0.761030 | A creature that's hidden is only barely perceptible. You only  know what space it occupies. Perhaps the creature just used  the Hide action. Your target might be behind some obstruction,  where you ca |

### Query 83
- Text: What is the rule about A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses other than sight ignore the invisible  condition. You can Seek (page 409) to attempt to figure out  an invisible creature's location, making it only hidden from  you. This lasts until the invisible creature successfully  uses Sneak to become undetected again. If you're already  observing a creature when it becomes invisible, it starts  out hidden since you know where it was, though it can  then Sneak to become undetected.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/2/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `62`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 1.064775 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/18` | 0.887367 | You can't be seen. You're undetected to everyone. Creatures  can Seek to detect you; if a creature succeeds at its Perception  check against your Stealth DC, you become hidden to that  creature until |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/24` | 0.880113 | If a creature is undetected, you don't know what space it  occupies and you're off-guard to it. The Seek basic action can  help you find an undetected creature, usually making it hidden  from you inst |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.869803 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/14` | 0.860019 | A creature or object within darkness is hidden or undetected  unless the seeker has darkvision or a precise sense other  than vision. A creature without darkvision or another means  of perceiving in d |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.854042 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/4` | 0.853433 | If you have no idea a creature is even present, that creature  is unnoticed by you. A creature that's undetected might also  be unnoticed. This condition usually matters for abilities  that can be use |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.849528 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/2` | 0.844806 | When you're undetected by a creature, that creature can't  see you at all, has no idea what space you occupy, and can't  target you, though you still can be affected by abilities that  target an area. |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/9` | 0.840968 | Three conditions measure the degree to which you can sense  a creature: observed, hidden, and undetected. However, the  concealed and invisible conditions can partially mask a  creature, and the unnot |

### Query 84
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/26']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `30`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/32` | 0.965652 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/7` | 0.965652 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/26` | 0.965652 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/29` | 0.960819 | **EQUIPMENT ** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/28` | 0.893143 | **EQUIPMENT** **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/39` | 0.893143 | **EQUIPMENT** **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/25` | 0.893143 | **EQUIPMENT** **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/18` | 0.893143 | **EQUIPMENT** **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/52` | 0.893143 | **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/40` | 0.865652 | **EQUIPMENT** |

### Query 85
- Text: What is the rule about If your result is tied with an enemy's result, the enemy  goes first. If your result is tied with another PC's, you can  decide between yourselves who goes first when you reach  that place in the initiative order. After that, your places in the?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `32`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/10` | 1.062222 | If your result is tied with an enemy's result, the enemy  goes first. If your result is tied with another PC's, you can  decide between yourselves who goes first when you reach  that place in the init |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/9` | 0.830798 | Unlike a check, where the result is compared to a DC, the  results of initiative rolls are ranked. This ranking sets the  order in which the encounter's participants act—the initiative  order. The cha |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/2` | 0.790814 | The GM keeps track of the initiative order for an  encounter. It's usually okay for the players to know  this order since they'll see who goes when and be  aware of one another's results. However, the |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/6` | 0.776282 | When the GM calls for it, you'll roll initiative to determine  your place in the initiative order, which is the sequence in  which the encounter's participants will take their turns.  Rolling initiati |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/4` | 0.749123 | An encounter is played out in a series of rounds, during which  the player characters, adversaries, and other participants in the  encounter act in sequence. You roll initiative to determine this  ord |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/18` | 0.747244 | Once you've done all the things you want to do with the actions  you have available, you reach the end of your turn. Take the  following steps in any order you choose. Play then proceeds to  the next |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/11` | 0.735013 | initiative order usually don't change during the encounter.  (But see the Delay basic action on page 408.) |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/15` | 0.718735 | Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/5` | 0.714028 | Any method used to track the initiative order needs to  be flexible because the order can change. A creature can  use the Delay basic action to change its place in the order,  in which case you can er |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/8` | 0.708652 | The GM rolls initiative for anyone other than the player  characters in the encounter. If these include a number of  identical creatures, the GM could roll once for the group as a  whole and have them |

### Query 86
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/33']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `31`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/37` | 0.988833 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/40` | 0.988833 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/33` | 0.988833 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/35` | 0.988833 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/30` | 0.988833 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/52` | 0.988833 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/31` | 0.930070 | **PLAYING THE ** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/34` | 0.912216 | **GAME** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/52` | 0.912216 | **GAME** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/32` | 0.909060 | **SPELLS** **PLAYING THE ** |

### Query 87
- Text: What are the requirements for **CHEER UP **[one-action] **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `43`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18` | 0.934673 | **CHEER UP **[one-action] **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/37` | 0.728630 | **SIDESTEP **[reaction] **FEAT 8** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/546` | 0.725812 | Cheer Up |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/21` | 0.711424 | You encourage an adjacent ally to overcome their minor  ailments by patting them on the back, providing them useful  advice, or offering some form of comfort or inspiration. The  target reduces the va |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/14` | 0.698659 | **HURRY **[one-action] **FEAT 6** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.694732 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.688820 | **READY ARMS! **[one-action]** TO **[two-actions] |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.686492 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.681029 | **WATCH OUT **[reaction] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/22` | 0.680454 | **DANCE PARTNER! **[one-action]** TO **[two-actions] |

### Query 88
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/56']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `10`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/56` | 0.856592 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/50` | 0.856592 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/42` | 0.856592 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/61` | 0.856592 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/68` | 0.756592 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/32` | 0.756592 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/30` | 0.756592 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/36` | 0.756592 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/38` | 0.756592 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/44` | 0.756592 | **SPELLS** |

### Query 89
- Text: Summarize **Obozaya**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `54`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/31` | 0.936660 | **Obozaya** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/53` | 0.702377 | **Operative ** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/43` | 0.702377 | **Operative ** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/31` | 0.702377 | **Operative ** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/34` | 0.702377 | **Operative ** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/26` | 0.702377 | **Operative ** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/36` | 0.702377 | **Operative ** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/61` | 0.702377 | **Operative ** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/37` | 0.681209 | **Solarian** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/44` | 0.681209 | **Solarian** |

### Query 90
- Text: Summarize **Critical Success** Any undetected or hidden creature you  critically succeeded against becomes observed by you.  You learn the location of objects in the area you critically  succeeded against.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `32`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/24` | 1.080049 | **Critical Success** Any undetected or hidden creature you  critically succeeded against becomes observed by you.  You learn the location of objects in the area you critically  succeeded against. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/25` | 0.945358 | **Success** Any undetected creature you succeeded against  becomes hidden from you instead of undetected, and  any hidden creature you succeeded against becomes  observed by you. You learn the locatio |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/29` | 0.838263 | **Critical Success** You determine the creature's true intentions  and get a solid idea of any mental magic affecting it. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/30` | 0.788009 | You indicate a creature that you can see to one or more allies,  gesturing in a direction and describing the distance verbally.  That creature is hidden to your allies, rather than undetected  (page 4 |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/17` | 0.783779 | The GM attempts a single secret Perception check for  you and compares the result to the Stealth DCs of any  undetected or hidden creatures in the area, or the DC to  detect each object in the area (a |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/79` | 0.777243 | **Hidden:** A creature you're hidden from knows your location  but can't see you. |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/31` | 0.769889 | **Failure** You detect what a deceptive creature wants you to  believe. If they're not being deceptive, you believe they're  behaving normally. |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/106` | 0.762318 | **Undetected:** A creature you're undetected by doesn't |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/89` | 0.761887 | strong opinion about you. **Invisible:** Creatures can't see you. **Observed:** You're in plain view. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/29` | 0.759977 | **Requirements** A creature is undetected by one or more of  your allies but isn't undetected by you. |

### Query 91
- Text: Summarize **Zemir**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/42']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `31`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/42` | 0.916399 | **Zemir** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/1` | 0.617443 | **KEY TERMS** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7` | 0.612187 | **HIT POINTS** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/38` | 0.602097 | **Soldier** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/28` | 0.602097 | **Soldier** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/45` | 0.602097 | **Soldier** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/33` | 0.602097 | **Soldier** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/36` | 0.602097 | **Soldier** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/63` | 0.602097 | **Soldier** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/55` | 0.602097 | **Soldier** |

### Query 92
- Text: What is the rule about The mystic is a spellcaster with a connection  to a divine, occult, or primal aspect of the universe. A  mystic casts powerful spells, learning new epiphanies  based on their chosen connection, and heals allies  using a vitality network that acts as a floating pool of  Hit Points. Play the mystic if you want to be a powerful  spellcaster who also heals your allies through your  supernatural bonds while casting powerful spells.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `32`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/24` | 1.048564 | The mystic is a spellcaster with a connection  to a divine, occult, or primal aspect of the universe. A  mystic casts powerful spells, learning new epiphanies  based on their chosen connection, and he |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 0.740125 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/10` | 0.714768 | You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by you |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/2` | 0.703807 | You're a master influencer. You make your way in the universe with a charming smile, quick wit, and keen  sense of self-preservation. You're a leader who motivates your teammates, pushes them past the |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/11` | 0.688755 | The solarian is a warrior who channels the  cosmic cycle. Every solarian creates weapons of pure  stellar energy that they can manifest at will. Cycling  between graviton and photon attunement, a sola |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/4` | 0.684804 | The envoy is a plucky leader who supports their  allies with battlefield directives, social savviness, and  a suite of skills. Envoys call out directives to their  allies, granting powerful boons that |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/29` | 0.682992 | The soldier is a weapons expert with a mountain  of Hit Points who isn't afraid to get between their allies  and danger. They unleash suppressing attacks with  area weapons that pin foes. They designa |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/41` | 0.679276 | A witchwarper alters reality by drawing on the  infinite possibilities of other universes and timelines.  Every witchwarper is influenced by an event, and they  can harness paradoxical powers to creat |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` | 0.668234 | Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  char |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/28` | 0.658462 | You control the flow of information, playing a critical role  during a battle or while planning your next mission. You might  give commands through a comm unit or datapad or using  telepathic communic |

### Query 93
- Text: What is the rule about **Leveling Up **on page 29 tells you how to make your  character stronger when you get enough Experience  Points to reach a new level.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `65`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/6` | 0.984717 | **Leveling Up **on page 29 tells you how to make your  character stronger when you get enough Experience  Points to reach a new level. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 0.748703 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/24` | 0.723729 | At 5th level and every 5 levels thereafter, your character  boosts four different attribute modifiers. This is described  briefly in the class. For the full details on attribute  modifiers and applyin |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.719112 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.717340 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/8` | 0.714447 | As your envoy level increases, so does your ability to adapt  to new situations. At 9th level and 15th level, increase the  number of skill feats you gain this way by 1. You can use  feats that you te |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/9` | 0.713393 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.705860 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/1` | 0.704774 | rush into battle with weapons raised gain a higher number  of Hit Points each level, while characters who cast spells or  engage in trickery gain fewer. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/Table/2` | 0.701375 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat2Envoy feat, skill feat, skill increase3Adaptive talent, genera |

### Query 94
- Text: What are the requirements for **BASIC MYSTIC SPELLCASTING** **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `62`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/17` | 0.902640 | **BASIC MYSTIC SPELLCASTING** **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/26` | 0.791408 | **BASIC WITCHWARPER SPELLCASTING** **FEAT 4** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/22` | 0.773543 | **BASIC MYSTICISM** **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41` | 0.734279 | **Prerequisites** Basic Mystic Spellcasting |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/43` | 0.728887 | **EXPERT MYSTIC SPELLCASTING** **FEAT 12** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/51` | 0.724726 | **Prerequisites** Expert Mystic Spellcasting; legendary in  connection skill |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/46` | 0.719319 | **Prerequisites** Basic Mystic Spellcasting; master in  connection skill |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/21` | 0.714183 | **BASIC WARP SPELL** **FEAT 4** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/48` | 0.711964 | **MASTER MYSTIC SPELLCASTING** **FEAT 18** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/16` | 0.708870 | **BASIC STELLAR ATTUNEMENT** **FEAT 4** |

### Query 95
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/36']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/36` | 0.979439 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/71` | 0.979439 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/53` | 0.979439 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/47` | 0.979439 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/41` | 0.979439 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/44` | 0.979439 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/70` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/58` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/65` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/53` | 0.879439 | **GLOSSARY & ** **INDEX** |

### Query 96
- Text: Summarize **Downtime ** **Mode**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/49']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `29`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/49` | 0.985345 | **Downtime ** **Mode** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/47` | 0.985345 | **Downtime ** **Mode** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/51` | 0.985345 | **Downtime ** **Mode** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/56` | 0.985345 | **Downtime ** **Mode** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/68` | 0.985345 | **Downtime ** **Mode** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/69` | 0.885345 | **Downtime ** **Mode** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/56` | 0.885345 | **Downtime ** **Mode** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/50` | 0.885345 | **Downtime ** **Mode** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/36` | 0.885345 | **Downtime ** **Mode** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/45` | 0.885345 | **Downtime ** **Mode** |

### Query 97
- Text: What are the requirements for **Prerequisites** Mystic Dedication?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `65`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20` | 0.962366 | **Prerequisites** Mystic Dedication |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/15` | 0.962366 | **Prerequisites** Mystic Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25` | 0.962366 | **Prerequisites** Mystic Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/36` | 0.962366 | **Prerequisites** Mystic Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/39` | 0.799468 | **Prerequisites** Soldier Dedication |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/34` | 0.799468 | **Prerequisites** Soldier Dedication |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/18` | 0.799468 | **Prerequisites** Soldier Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/30` | 0.785533 | **Prerequisites** Basic Mysticism |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.779959 | **Prerequisites** Operative Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.779959 | **Prerequisites** Operative Dedication |

### Query 98
- Text: Summarize You channel a fundamental force of the universe.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/2` | 1.050736 | You channel a fundamental force of the universe. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/2` | 0.735276 | You step up and lead others to victory while manipulating  those who stand in your way. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/2` | 0.717404 | You are a solar knight attuned to the powerful forces  of gravity and light, manifesting the cosmic cycle into  armaments made of stellar energy. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/20` | 0.715699 | Your quantum field gains the effect of your chosen paradox. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/2` | 0.703473 | You're a professional with crack aim and lethal instincts. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/51` | 0.684270 | You gain a 1st- or 2nd-level operative feat. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/26` | 0.683689 | You gain a 1st- or 2nd-level mystic feat. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/2` | 0.671397 | You can draw on the infinite possibilities of other universes and  timelines to warp reality with powerful magic. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/20` | 0.662747 | You gain a 1st- or 2nd-level solarian feat. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/35` | 0.654699 | You gain a 1st- or 2nd-level envoy feat of your choice. |

### Query 99
- Text: What is the rule about **IN-DEPTH ACTION RULES**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `44`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/10` | 0.970468 | **IN-DEPTH ACTION RULES** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.663508 | These rules clarify some of the specifics of using actions. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/29` | 0.608060 | **Rules Overview** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/54` | 0.608060 | **Rules Overview** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/35` | 0.608060 | **Rules Overview** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/41` | 0.608060 | **Rules Overview** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/20` | 0.608060 | **Rules Overview** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/27` | 0.608060 | **Rules Overview** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/30` | 0.608060 | **Rules Overview** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/37` | 0.608060 | **Rules Overview** |

### Query 100
- Text: What is the rule about **Special** You can select this feat a second time as a 10th level  feat and a 16th level feat, increasing the number of skill  feats you gain using adaptive talent by 1.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `39`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/41` | 0.984874 | **Special** You can select this feat a second time as a 10th level  feat and a 16th level feat, increasing the number of skill  feats you gain using adaptive talent by 1. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/40` | 0.756159 | You gain the adaptive talent class feature, but you do not  gain additional skill feats at higher levels. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/23` | 0.755845 | **Special** You can select this feat more than once. Each time you  do, you gain another operative feat. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/32` | 0.752084 | **Special** You can select this feat more than once. Each time  you do, you gain another mystic feat. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.739243 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/36` | 0.739018 | **Special** You can select this feat more than once. Each  time you do, you gain another solarian feat. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/35` | 0.734126 | **Special** You can select this feat more than once. Each time  you do, you gain another witchwarper feat. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/30` | 0.733626 | **Special** You can select this feat more than once. Each time  you do, you gain another soldier feat. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/15` | 0.731644 | **Special** You can select this feat more than once. Each time  you select it, you gain another envoy feat. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/18` | 0.721960 | **Expert Spellcasting Feat:** Typically taken at 12th level,  these feats make you an expert in spell attack modifiers  and spell DCs and grant you a 4th-rank spell slot. If you  have a spell repertoi |

### Query 101
- Text: Summarize PRECISE SENSES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `36`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17` | 0.969955 | PRECISE SENSES |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20` | 0.922158 | IMPRECISE SENSES |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/25` | 0.814469 | SPECIAL SENSES |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15` | 0.770288 | SENSES |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/22` | 0.744785 | VAGUE SENSES |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15` | 0.681453 | **DETECTING WITH OTHER SENSES** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/18` | 0.668675 | Average vision is a precise sense—a sense that can be used to  perceive the world in nuanced detail. The only way to target |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/17` | 0.646197 | **Using Stealth with Other Senses** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/6` | 0.646064 | TREMORSENSE |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/8/SectionHeader/5` | 0.638487 | **REPEAT A SPELL** |

### Query 102
- Text: Summarize **Failure** You detect what a deceptive creature wants you to  believe. If they're not being deceptive, you believe they're  behaving normally.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `34`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/31` | 1.069909 | **Failure** You detect what a deceptive creature wants you to  believe. If they're not being deceptive, you believe they're  behaving normally. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/32` | 0.829410 | **Critical Failure** You get a false sense of the creature's  intentions. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/30` | 0.822201 | **Success** You can tell whether the creature is behaving  normally, but you don't know its exact intentions or what  magic might be affecting it. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/29` | 0.806681 | **Critical Success** You determine the creature's true intentions  and get a solid idea of any mental magic affecting it. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/28` | 0.791374 | You try to tell whether a creature's behavior is abnormal.  Choose one creature and assess it for odd body language,  signs of nervousness, and other indicators that it might be  trying to deceive som |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/25` | 0.764279 | **Success** Any undetected creature you succeeded against  becomes hidden from you instead of undetected, and  any hidden creature you succeeded against becomes  observed by you. You learn the locatio |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/24` | 0.748368 | **Critical Success** Any undetected or hidden creature you  critically succeeded against becomes observed by you.  You learn the location of objects in the area you critically  succeeded against. |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/79` | 0.740356 | **Hidden:** A creature you're hidden from knows your location  but can't see you. |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/106` | 0.736901 | **Undetected:** A creature you're undetected by doesn't |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/64` | 0.736323 | **Controlled:** Another creature determines your actions. |

### Query 103
- Text: What is the rule about **Expert Spellcasting Feat:** Typically taken at 12th level,  these feats make you an expert in spell attack modifiers  and spell DCs and grant you a 4th-rank spell slot. If you  have a spell repertoire, you can select a second spell from  your repertoire as a signature spell. At 14th level, they grant  you a 5th-rank spell slot, and at 16th level, they grant you a  6th-rank spell slot. Archetypes refer to these benefits as the  "expert spellcasting benefits."?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `38`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/18` | 1.068388 | **Expert Spellcasting Feat:** Typically taken at 12th level,  these feats make you an expert in spell attack modifiers  and spell DCs and grant you a 4th-rank spell slot. If you  have a spell repertoi |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/19` | 0.956246 | **Master Spellcasting Feat:** Usually found at 18th level, these  feats make you a master in spell attack modifiers and spell  DCs and grant you a 7th-rank spell slot. If you have a spell  repertoire, |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/17` | 0.942549 | **Basic Spellcasting Feat:** Usually available at 4th level,  these feats grant a 1st-rank spell slot. At 6th level, they  grant you a 2nd-rank spell slot, and if you have a spell  repertoire, you can |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.785527 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/29` | 0.766128 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the witchwarper  archetype, add a spell of the appropriate spell rank to your  repertoire: a co |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.750227 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/45` | 0.747653 | You gain the expert spellcasting benefits (page 174). |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/47` | 0.747653 | You gain the expert spellcasting benefits (page 174). |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/41` | 0.735669 | **Special** You can select this feat a second time as a 10th level  feat and a 16th level feat, increasing the number of skill  feats you gain using adaptive talent by 1. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/10` | 0.733707 | You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by you |

### Query 104
- Text: What is the rule about Most abilities that designate "a creature you can see"  or the like function just as well if the user can precisely  sense the subject with a different sense. If a monster  uses a sense other than vision, the GM can adapt ways  of avoiding detection that work with the monster's  senses. For example, a creature that has echolocation  might use hearing as a primary sense. This could mean  its quarry is concealed in a noisy chamber, hidden in  a great enough din, or invisible under a *silence* spell.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `54`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/16` | 1.049516 | Most abilities that designate "a creature you can see"  or the like function just as well if the user can precisely  sense the subject with a different sense. If a monster  uses a sense other than vis |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.811468 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.809939 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` | 0.805734 | With the exception of invisible, these conditions are  relative to the viewer—it's possible for a creature to be  observed to you but hidden from your ally. Most of these  rules apply to objects as we |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/11` | 0.802664 | Typically, the GM tracks how well creatures detect each  other since neither party has perfect information. For  example, you might think a creature is in the last place  you sensed it, but it was abl |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.795481 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/23` | 0.787217 | A character also has many vague senses—ones that can alert  you that something is there but aren't useful for zeroing in on  it to determine exactly what it is. The most useful of these  for a typical |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 0.781999 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/14` | 0.779981 | A creature or object within darkness is hidden or undetected  unless the seeker has darkvision or a precise sense other  than vision. A creature without darkvision or another means  of perceiving in d |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/20` | 0.778620 | Anything in plain view is observed by you. If a creature takes  measures to avoid detection, such as by using Stealth to Hide,  it can become hidden or undetected instead of observed. If you |

### Query 105
- Text: What is the rule about • If you created an effect lasting for a certain number of  rounds, reduce the number of rounds remaining by 1. The  effect ends if the duration is reduced to 0. For example,  if you cast a spell that lasts 3 rounds on yourself during?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `44`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/22` | 1.061030 | • If you created an effect lasting for a certain number of  rounds, reduce the number of rounds remaining by 1. The  effect ends if the duration is reduced to 0. For example,  if you cast a spell that |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/4/ListItem/19` | 0.896777 | End any effects that last until the end of your turn. For  example, spells with a sustained duration end at the end of  your turn unless you used the Sustain a Spell action during  your turn to extend |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/6` | 0.794297 | your first turn of a fight, it would affect you during that  turn, decrease to 2 rounds of duration at the start of your  second turn, decrease to 1 round of duration at the start of  your third turn, |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/18` | 0.792662 | You can have a given condition only once at a time. If  an effect would impose a condition you already have,  you now have that condition for the longer of the two  durations. The shorter-duration con |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/22` | 0.790693 | Conditions with different values are considered  different conditions. If you're affected by a condition  with a value multiple times, you apply only the  highest value, although you might have to tra |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/8` | 0.777431 | For an effect that lasts a number of rounds, the remaining  duration decreases by 1 at the start of each turn of the  creature that created the effect. Detrimental effects often  last "until the end o |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/3` | 0.774269 | Conditions are persistent. Whenever you're affected by a  condition, its effects last until the condition's stated duration  ends, the condition is removed, or terms dictated in the  condition itself |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/9` | 0.761981 | Instead of lasting a fixed number of rounds, a duration  might end only when certain conditions are met (or cease to  be true). If so, the effects last until those conditions are met. |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/5` | 0.747955 | Some conditions have a number after the condition, called a  condition value. This value conveys the severity of a condition,  and such conditions often give you a bonus or penalty equal  to their val |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/21` | 0.744262 | Many things happen automatically at the start of your turn it's a common point for tracking the passage of time for  effects that last multiple rounds. At the start of each of your  turns, take these |

### Query 106
- Text: Summarize SENSES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `37`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15` | 0.874995 | SENSES |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20` | 0.863015 | IMPRECISE SENSES |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/25` | 0.815454 | SPECIAL SENSES |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/22` | 0.802942 | VAGUE SENSES |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17` | 0.798170 | PRECISE SENSES |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15` | 0.714700 | **DETECTING WITH OTHER SENSES** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/4` | 0.692929 | SCENT |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/8/SectionHeader/5` | 0.685260 | **REPEAT A SPELL** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/6` | 0.683633 | TREMORSENSE |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/17` | 0.679043 | **Using Stealth with Other Senses** |

### Query 107
- Text: What are the requirements for **LOOK ALIVE** **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `35`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/31` | 0.844439 | **LOOK ALIVE** **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/594` | 0.681105 | Look Alive |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/17` | 0.674298 | 8TH LEVEL |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18` | 0.665581 | **CHEER UP **[one-action] **FEAT 8** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/37` | 0.649894 | **SIDESTEP **[reaction] **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34` | 0.643577 | **Prerequisites** Watch Out |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/26` | 0.643577 | **Prerequisites** Watch Out |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/8` | 0.623046 | **8 + Constitution modifier** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.617273 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/22` | 0.615294 | **CONFOUNDING DISQUISITION **[two-actions] **FEAT 8** |

### Query 108
- Text: Summarize IMPRECISE SENSES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `39`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20` | 1.002717 | IMPRECISE SENSES |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17` | 0.834312 | PRECISE SENSES |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/25` | 0.757276 | SPECIAL SENSES |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/22` | 0.755747 | VAGUE SENSES |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15` | 0.754324 | SENSES |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/6` | 0.670368 | TREMORSENSE |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/16/SectionHeader/6` | 0.668883 | UNCONSCIOUS |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/11/SectionHeader/18` | 0.665961 | CONFUSED |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15` | 0.664705 | **DETECTING WITH OTHER SENSES** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/16/SectionHeader/4` | 0.660744 | SUPPRESSED |

### Query 109
- Text: What is the rule about Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining their Hit Points, see page 21.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `44`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 1.061536 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` | 0.932649 | This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chos |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/24` | 0.802802 | At 5th level and every 5 levels thereafter, your character  boosts four different attribute modifiers. This is described  briefly in the class. For the full details on attribute  modifiers and applyin |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.797971 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/6` | 0.792299 | **Leveling Up **on page 29 tells you how to make your  character stronger when you get enough Experience  Points to reach a new level. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/9` | 0.779547 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/1` | 0.777783 | rush into battle with weapons raised gain a higher number  of Hit Points each level, while characters who cast spells or  engage in trickery gain fewer. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.766111 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.751260 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/5` | 0.750969 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |

### Query 110
- Text: What are the requirements for **Prerequisites** master in Medicine or Augmentation Specialist **Requirements** You have a medkit.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/7/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `15`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/11` | 1.000946 | **Prerequisites** master in Medicine or Augmentation Specialist **Requirements** You have a medkit. |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/6/Text/17` | 0.678283 | **Requirements** You have environmental protection on your  armor or a field scientist's kit. |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/15` | 0.659510 | **Requirements** You have a repair kit and one free hand. |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/12` | 0.656089 | You safely implant or remove an augmentation on a willing  creature. This takes 1 hour per item level of the augmentation  if using a medkit or half the normal amount of time if you  have access to a |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/43` | 0.629748 | **Requirements** You must have an item with a camera and one  free hand, mount, or uniclamp. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/20` | 0.625777 | **Prerequisites** trained in Medicine |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/12` | 0.610820 | **Requirements** You have at least one hand or leg (or suitable  appendage) free, and you're untethered. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/46` | 0.608699 | **Prerequisites** master in Intimidation |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/7/SectionHeader/13` | 0.602855 | **INSTALL UPGRADE** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/48` | 0.597028 | **CONDITIONS ** **APPENDIX** |

### Query 111
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/29']
- Expected found: `True`
- Expected rank: `20`
- Graph boost applied: `True`
- Graph boosted count: `64`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/23` | 0.937823 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/54` | 0.937823 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/59` | 0.937823 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/64` | 0.937823 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/18` | 0.937823 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/44` | 0.937823 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/39` | 0.937823 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/49` | 0.937823 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/30` | 0.937823 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/35` | 0.937823 | **ARCHETYPE** |

### Query 112
- Text: What is the rule about Witchwarper envoys make powerful battlefield  controllers that help maximize a partys mobility while  inhibiting their foe's movement capabilities with area  spells and quantum field.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `32`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/9` | 0.995647 | Witchwarper envoys make powerful battlefield  controllers that help maximize a partys mobility while  inhibiting their foe's movement capabilities with area  spells and quantum field. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/ListItem/9` | 0.768325 | Witchwarper operatives combine operative mobility  feats with their quantum field to shake up enemy. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/8` | 0.727943 | Soldier envoys make natural commanders who can  use their defensive capabilities to keep the bonuses  of their directive's active against powerful enemies  while clearing out weaker foes with area fir |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/4` | 0.704706 | The witchwarper archetype allows you to cast reality warping  spells and manifest a quantum field. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/9` | 0.698851 | Witchwarper solarians can use gravity abilities to push  and pull enemies into their quantum auras. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/ListItem/5` | 0.695230 | Envoy soldiers are natural tacticians who use directives to  position enemies and allies to optimize their area attacks. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/ListItem/9` | 0.688020 | Witchwarper soldiers want to further  hamper their enemy's movements and  are excellent at using grenades. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/5` | 0.659345 | Envoy solarians can rush into close quarters to  properly assess an enemy's abilities and positioning  when determining what directives to use. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/4` | 0.643390 | The envoy archetype allows you to take on a leadership role  by giving out directives that can support allies or hinder  enemies. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/5` | 0.642363 | Mystic envoys can choose between using their magic  or directives to empower their allies, widening the  breadth of options available to them. |

### Query 113
- Text: Summarize **Perception and ** **Detection**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/46']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `42`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/46` | 0.999207 | **Perception and ** **Detection** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/48` | 0.999207 | **Perception and ** **Detection** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/65` | 0.999207 | **Perception and ** **Detection** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/44` | 0.999207 | **Perception and ** **Detection** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/41` | 0.899207 | **Perception and ** **Detection** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/66` | 0.899207 | **Perception and ** **Detection** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/33` | 0.899207 | **Perception and ** **Detection** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/53` | 0.899207 | **Perception and ** **Detection** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/53` | 0.893193 | **Counteracting** **Perception and ** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/1` | 0.890240 | PERCEPTION AND  DETECTION |

### Query 114
- Text: What is the rule about You gain a 1st- or 2nd-level mystic feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `40`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/26` | 0.956935 | You gain a 1st- or 2nd-level mystic feat. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/51` | 0.847260 | You gain a 1st- or 2nd-level operative feat. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/19` | 0.844988 | You gain a 1st- or 2nd-level soldier feat. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/20` | 0.827827 | You gain a 1st- or 2nd-level solarian feat. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/31` | 0.819990 | You gain one mystic feat. For the purpose of meeting its  prerequisites, your mystic level is half your character level. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/35` | 0.790990 | You gain a 1st- or 2nd-level envoy feat of your choice. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/15` | 0.780237 | Your disruptive powers grow. You gain a 1st- or 2nd-level  witchwarper feat. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/32` | 0.755578 | **Special** You can select this feat more than once. Each time  you do, you gain another mystic feat. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/17` | 0.715594 | **Basic Spellcasting Feat:** Usually available at 4th level,  these feats grant a 1st-rank spell slot. At 6th level, they  grant you a 2nd-rank spell slot, and if you have a spell  repertoire, you can |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/22` | 0.708184 | You gain one operative feat. For the purpose of meeting its  prerequisites, your operative level is half your character level. |

### Query 115
- Text: What is the rule about **Navasi**, the human envoy, is a former space  pirate with a heart of gold. She's got a witty  remark for every occasion and a bullet for  anyone who would hurt one of her friends.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `56`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/7` | 1.002835 | **Navasi**, the human envoy, is a former space  pirate with a heart of gold. She's got a witty  remark for every occasion and a bullet for  anyone who would hurt one of her friends. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/6` | 0.581372 | **Navasi** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/31` | 0.579895 | Your confidence is a battery that keeps your allies going.  When you use a directive that grants temporary Hit Points, |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/436` | 0.579147 | Envoy feat, skill feat, skill increase |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/420` | 0.579147 | Envoy feat, skill feat, skill increase |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/416` | 0.579147 | Envoy feat, skill feat, skill increase |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/444` | 0.579147 | Envoy feat, skill feat, skill increase |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/412` | 0.579147 | Envoy feat, skill feat, skill increase |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/432` | 0.579147 | Envoy feat, skill feat, skill increase |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/440` | 0.579147 | Envoy feat, skill feat, skill increase |

### Query 116
- Text: What is the rule about This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the same time, and it's unclear in what order  they happen, the GM determines the order based on the  narrative.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `49`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 1.063704 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.891695 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` | 0.818100 | **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reac |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/2` | 0.761259 | Some reactions and free actions are triggered by a  creature using an action with the move trait. The most  notable example is Reactive Strike (reproduced below).  Actions with the move trait can trig |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.755076 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.747570 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/14` | 0.745107 | The GM might allow Tiny creatures to flank other  Tiny creatures if they're all in the same square, but  this is best left for special circumstances and uses  the GM's best judgment. |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/22` | 0.745104 | Usually the creature or effect forcing the movement  chooses the path the victim takes. If you're pushed or  pulled, you can usually be moved through hazardous  terrain, pushed out of an airlock, or t |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/8` | 0.744928 | You prepare to use an action that will occur outside your  turn. Choose a single action or free action you can use, and  designate a trigger. Your turn then ends. If the trigger you  designated occurs |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/18` | 0.742966 | Some effects require a target to be willing. Only you  can decide whether your PC is willing, and the GM decides  whether an NPC is willing. Even if you or your character  don't know what the effect i |

### Query 117
- Text: What is the rule about Most classes are associated with one key attribute  modifier, but some allow you to choose from two options.  For instance, if you're a witchwarper, you can choose  either Intelligence or Charisma as your key attribute.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `49`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/16` | 1.055925 | Most classes are associated with one key attribute  modifier, but some allow you to choose from two options.  For instance, if you're a witchwarper, you can choose  either Intelligence or Charisma as |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/18` | 0.809127 | You're an efficient multitasker, and you always have more  than one goal in mind or scheme on the go. You can maintain  twice your Charisma modifier of assets. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 0.759405 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/15` | 0.757922 | For instance, this is the attribute modifier you'll use to  determine the Difficulty Class (DC) associated with your  character's class features and feats. This is called your  class DC. If your chara |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.750830 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/5` | 0.749181 | Prioritize Charisma. Dexterity, Intelligence, and  Constitution round out your abilities and defenses. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/36` | 0.748959 | You can maintain a number of assets equal to your Charisma  modifier. If you Size Up other assets after that, your new asset  replaces a previous one. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/6` | 0.737855 | At 1st level, your class gives you  an attribute boost to Charisma. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/14` | 0.736109 | This is the attribute modifier that a member of your class  cares about the most. Many of your most useful and  powerful abilities are tied to this attribute in some way. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` | 0.719037 | Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  char |

### Query 118
- Text: What is the rule about STEP 1: ROLL INITIATIVE?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `36`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/5` | 0.942380 | STEP 1: ROLL INITIATIVE |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/20` | 0.737835 | STEP 1: START YOUR TURN |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/6` | 0.699147 | When the GM calls for it, you'll roll initiative to determine  your place in the initiative order, which is the sequence in  which the encounter's participants will take their turns.  Rolling initiati |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/9` | 0.696972 | Unlike a check, where the result is compared to a DC, the  results of initiative rolls are ranked. This ranking sets the  order in which the encounter's participants act—the initiative  order. The cha |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/12` | 0.687139 | STEP 2: PLAY A ROUND |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/15` | 0.684228 | Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/14` | 0.673809 | STEP 3: BEGIN THE NEXT ROUND |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/4/SectionHeader/12` | 0.669044 | STEP 2: ACT |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/13` | 0.660950 | A round begins when the participant with the highest  initiative roll result starts their turn, and it ends when the  one with the lowest initiative ends their turn. The process  of taking a turn is d |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/4/SectionHeader/4` | 0.660087 | **Changing the Initiative Order** |

### Query 119
- Text: What is the rule about Ancestry Feats?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `37`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/25` | 0.795871 | Ancestry Feats |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/442` | 0.688075 | Ancestry feat, greater resolve, incredible senses, inscrutable, skill increase |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/26` | 0.663400 | This section serves as a reminder of the ancestry feats your  character gains at 5th, 9th, 13th, and 17th levels. Ancestry  feats are detailed in each ancestry entry in Chapter 2, which  begins on pag |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/434` | 0.660058 | Ancestry feat, light armor expertise, skill increase, tactician, weapon mastery |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/14` | 0.622413 | In addition to the initial ancestry feat you started with, you  gain an ancestry feat at 5th level and every 4 levels thereafter. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/18` | 0.621604 | General Feats |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/418` | 0.620804 | Ancestry feat, attribute boosts, improvised mastery, perception expertise, skill increase, weapon expertise |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16` | 0.612128 | Skill Feats |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/410` | 0.601677 | Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/14` | 0.594611 | Class Feats |

### Query 120
- Text: What are the requirements for **PARDON ME** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/21` | 0.885870 | **PARDON ME** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/30` | 0.713327 | **SIZE UP** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/600` | 0.709913 | Pardon Me |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.674608 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/16` | 0.669398 | 1ST LEVEL |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/13` | 0.667690 | **DON'T YOU DIE ON ME **[one-action] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17` | 0.664764 | **Prerequisites** Size Up |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/7` | 0.664764 | **Prerequisites** Size Up |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.660478 | **WATCH OUT **[reaction] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.642497 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |

### Query 121
- Text: What is the rule about rush into battle with weapons raised gain a higher number  of Hit Points each level, while characters who cast spells or  engage in trickery gain fewer.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `47`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/1` | 0.989806 | rush into battle with weapons raised gain a higher number  of Hit Points each level, while characters who cast spells or  engage in trickery gain fewer. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 0.724123 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/9` | 0.693730 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/428` | 0.688719 | Attribute boosts, envoy feat, skill feat, skill increase |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/448` | 0.688719 | Attribute boosts, envoy feat, skill feat, skill increase |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.684349 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` | 0.682789 | This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chos |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.679803 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/32` | 0.679604 | increase the temporary Hit Points by your level. When you  use a directive that doesn't grant temporary Hit Points, you  can grant one ally affected by that directive temporary Hit  Points equal to ha |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/25` | 0.679113 | You've learned a few tricks with your weapons. Your  proficiency ranks for simple weapons, martial weapons, and  unarmed attacks increase to expert. Whenever you attack  the target of your Get 'Em!, y |

### Query 122
- Text: What is the rule about Some effects are even more restrictive. Certain abilities,  instead of or in addition to changing the number of actions  you can use, say specifically that you can't use reactions.  The most restrictive form of reducing actions is when an  effect states that you can't act: this means you can't use  any actions, or even speak. When you can't act, you still  regain your actions unless another effect (like the stunned  condition) prevents it.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `54`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/7` | 1.061502 | Some effects are even more restrictive. Certain abilities,  instead of or in addition to changing the number of actions  you can use, say specifically that you can't use reactions.  The most restricti |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/16` | 0.806518 | Some conditions prevent you from taking a certain  subset of actions, typically reactions. Other conditions  simply say you can't act. When you can't act, you're  unable to take any actions at all. Un |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/6` | 0.800621 | Effects can change the number of actions you can use on  your turn, or whether you can use actions at all. The slowed  condition, for example, causes you to lose actions, while the  quickened conditio |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/9` | 0.782461 | Various abilities and conditions, such as a Reactive Strike,  can disrupt an action. When an action is disrupted, you still  use the actions or reactions you committed, and you still  expend any costs |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/14` | 0.771786 | you from acting. If you can't act, you can't use any actions,  including reactions and free actions. |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/58` | 0.745627 | Some effects apply conditions to a creature or item. These change your state of being in some way. Conditions are  persistent, lasting until the stated duration ends, the condition is removed, or term |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/20` | 0.741571 | An activity typically involves using multiple actions to create  an effect greater than you can produce with a single action,  or combining multiple single actions to produce an effect  that's differe |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.740701 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` | 0.731329 | **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reac |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` | 0.725097 | Sometimes you need to attempt something not already  covered by defined actions in the game. When this happens,  the rules tell you how many actions you need to spend as  well as any traits your actio |

### Query 123
- Text: What is the rule about **Archetypes** on page 174 gives you thematic options  that allow you to further customize your character's  abilities. Though these rules are not recommended for  beginners, the archetypes in this book allow you to  gain abilities from other classes starting at 2nd level.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `45`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/7` | 1.031019 | **Archetypes** on page 174 gives you thematic options  that allow you to further customize your character's  abilities. Though these rules are not recommended for  beginners, the archetypes in this bo |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.763450 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/3` | 0.748029 | You gain more skill increases than members of other classes.  At 2nd level and every level thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you' |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.736129 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/Table/2` | 0.731152 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat2Envoy feat, skill feat, skill increase3Adaptive talent, genera |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.729854 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.728609 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.724529 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.724426 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 0.721223 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |

### Query 124
- Text: What is the rule about **Special** You can select this feat more than once. Each time  you select it, you gain another envoy feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `40`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/15` | 0.973734 | **Special** You can select this feat more than once. Each time  you select it, you gain another envoy feat. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/30` | 0.852839 | **Special** You can select this feat more than once. Each time  you do, you gain another soldier feat. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/32` | 0.839433 | **Special** You can select this feat more than once. Each time  you do, you gain another mystic feat. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/23` | 0.839063 | **Special** You can select this feat more than once. Each time you  do, you gain another operative feat. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/35` | 0.827806 | You gain a 1st- or 2nd-level envoy feat of your choice. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/36` | 0.827210 | **Special** You can select this feat more than once. Each  time you do, you gain another solarian feat. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/35` | 0.817516 | **Special** You can select this feat more than once. Each time  you do, you gain another witchwarper feat. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/14` | 0.783029 | You gain one envoy feat. For the purpose of meeting its  prerequisites, your envoy level is equal to half your character  level. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.757003 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/41` | 0.741800 | **Special** You can select this feat a second time as a 10th level  feat and a 16th level feat, increasing the number of skill  feats you gain using adaptive talent by 1. |

### Query 125
- Text: What is the rule about You gain the expert spellcasting benefits (page 174).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/47']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `38`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/45` | 0.942040 | You gain the expert spellcasting benefits (page 174). |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/47` | 0.942040 | You gain the expert spellcasting benefits (page 174). |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/52` | 0.907606 | You gain the master spellcasting benefits (page 174). |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/50` | 0.907606 | You gain the master spellcasting benefits (page 174). |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/18` | 0.722190 | **Expert Spellcasting Feat:** Typically taken at 12th level,  these feats make you an expert in spell attack modifiers  and spell DCs and grant you a 4th-rank spell slot. If you  have a spell repertoi |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.715991 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/29` | 0.693374 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the witchwarper  archetype, add a spell of the appropriate spell rank to your  repertoire: a co |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/25` | 0.690027 | You gain the leader's confidence class feature (see page  107). |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/19` | 0.689474 | **Master Spellcasting Feat:** Usually found at 18th level, these  feats make you a master in spell attack modifiers and spell  DCs and grant you a 7th-rank spell slot. If you have a spell  repertoire, |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/40` | 0.689016 | You gain the primary target class feature (page 152). |

### Query 126
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/30']
- Expected found: `True`
- Expected rank: `9`
- Graph boost applied: `True`
- Graph boosted count: `64`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/23` | 0.937823 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/54` | 0.937823 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/59` | 0.937823 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/64` | 0.937823 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/18` | 0.937823 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/44` | 0.937823 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/39` | 0.937823 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/49` | 0.937823 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/30` | 0.937823 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/35` | 0.937823 | **ARCHETYPE** |

### Query 127
- Text: What are the requirements for **OPERATIVE EXPLOIT** **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `34`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/24` | 0.873778 | **OPERATIVE EXPLOIT** **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/19` | 0.709955 | **STARFINDER PROVISIONS** **FEAT 8** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/25` | 0.706305 | **VETERAN TRAP FINDER** **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/16` | 0.702520 | **REALLY GET EM!** **FEAT 8** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/38` | 0.688090 | **EXPANDED CONNECTION** **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/1` | 0.669903 | OPERATIVE |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/57` | 0.667484 | **SPECIALIZED OPERATIVE** **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/65` | 0.666244 | **Prerequisites** Operative Dedication, class granting no more Hit  Points per level than 6 + your Constitution |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/36` | 0.656700 | **QUANTUM BREADTH** **FEAT 8** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.646499 | **Prerequisites** Operative Dedication |

### Query 128
- Text: Summarize **ARCHETYPE** **DEDICATION** **MULTICLASS**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `65`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/7` | 1.005741 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/28` | 1.005741 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/7` | 1.005741 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/12` | 1.005741 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/12` | 1.005741 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/11` | 1.005741 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/5` | 1.005741 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/8` | 0.825892 | Multiclass Dedications |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/50` | 0.793249 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/38` | 0.793249 | **ARCHETYPE** |

### Query 129
- Text: What are the requirements for **Prerequisites** Influence?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/Text/58']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/58` | 0.924744 | **Prerequisites** Influence |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/592` | 0.751815 | Influence |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.730916 | **Prerequisites** trained in Intimidation |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/25` | 0.725731 | **Prerequisites** adaptive talent |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/26` | 0.715443 | **Prerequisites** Watch Out |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34` | 0.715443 | **Prerequisites** Watch Out |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/19` | 0.706610 | **Prerequisites **Improvised Mastery |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17` | 0.704213 | **Prerequisites** Size Up |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/7` | 0.704213 | **Prerequisites** Size Up |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/46` | 0.696920 | **Prerequisites** master in Intimidation |

### Query 130
- Text: Summarize YOU MIGHT...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `24`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/18` | 0.890459 | YOU MIGHT... |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/22` | 0.796164 | OTHERS PROBABLY... |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/16` | 0.720362 | IN DOWNTIME... |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/14` | 0.697732 | WHILE EXPLORING... |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/12` | 0.662992 | DURING SOCIAL ENCOUNTERS... |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10` | 0.653680 | DURING COMBAT ENCOUNTERS... |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/632` | 0.648312 | You Can Do It |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/ListItem/25` | 0.641284 | Assume you like being in charge. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49` | 0.625007 | **YOU CAN DO IT **[one-action] **FEAT 14** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/38` | 0.614176 | **Trigger** You're about to roll initiative. |

### Query 131
- Text: What is the rule about **CHARACTER ** **SHEET**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/60']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `40`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/47` | 0.884532 | **CHARACTER ** **SHEET** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/60` | 0.884532 | **CHARACTER ** **SHEET** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/55` | 0.884532 | **CHARACTER ** **SHEET** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/48` | 0.784532 | **CHARACTER ** **SHEET** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/56` | 0.784532 | **CHARACTER ** **SHEET** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/22` | 0.784532 | **CHARACTER ** **SHEET** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/72` | 0.784532 | **CHARACTER ** **SHEET** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/66` | 0.752967 | **CHARACTER ** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/35` | 0.735377 | **INDEX** **CHARACTER ** **SHEET** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/51` | 0.694344 | CHARACTER Sheet |

### Query 132
- Text: What are the requirements for **CONFOUNDING DISQUISITION **[two-actions] **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `29`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/22` | 0.923459 | **CONFOUNDING DISQUISITION **[two-actions] **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/5` | 0.682435 | **ACQUIRE ASSET **[one-action] **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/548` | 0.682435 | Confounding Disquisition |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/19` | 0.681870 | **SITUATIONAL AWARENESS **[two-actions] **FEAT 12** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.679833 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.671506 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22` | 0.668527 | **SEARCH HIGH AND LOW! **[one-action]** TO **[two-actions] **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/31` | 0.668315 | **DIGITAL ASSESSMENT! **[one-action]** TO **[two-actions] |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/37` | 0.661358 | **SIDESTEP **[reaction] **FEAT 8** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/5` | 0.656342 | **COORDINATED AMBUSH! **[one-action]** TO **[two-actions] |

### Query 133
- Text: Summarize **Success** You get free and remove the grabbed, immobilized,  and restrained conditions imposed by your chosen  target.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/2/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `43`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/29` | 1.068550 | **Success** You get free and remove the grabbed, immobilized,  and restrained conditions imposed by your chosen  target. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/28` | 0.879109 | **Critical Success** You get free and remove the grabbed,  immobilized, and restrained conditions imposed by your  chosen target. You can then Stride up to 5 feet. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/22` | 0.761387 | **Requirements** You are benefiting from cover, are near a  feature that allows you to take cover, or are prone. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/12` | 0.746503 | You release something you're holding in your hand or hands.  This might mean dropping an item, removing one hand from  your weapon while continuing to hold it in another hand,  releasing a cable suspe |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/18` | 0.745497 | **Success** You make a damage roll according to the weapon or  unarmed attack and deal damage. |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/17` | 0.733558 | **Requirements** Your hands are not tied behind your back or  otherwise restrained. |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/33` | 0.732195 | **Requirements** You have at least one hand or leg (or suitable  appendage) free, and you're untethered. |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/103` | 0.728278 | **Suppressed: **You're in a dangerous situation that forces |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/5` | 0.727604 | You stand up from being prone. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/78` | 0.726219 | **Grabbed:** A creature, object, or magic holds you in place. **Helpful:** An NPC with this condition wants to assist you. |

### Query 134
- Text: What is the rule about In some cases, rolling a Dexterity-based Stealth  skill check to Sneak doesn't make the most sense.  For example, a PC trying to avoid being detected by  a creature that senses heartbeats might meditate  to slow their heart rate, using Wisdom instead of  Dexterity for their Stealth check. When a creature  could detect you using multiple different senses, use  your lowest applicable attribute modifier.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `59`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/19` | 1.066823 | In some cases, rolling a Dexterity-based Stealth  skill check to Sneak doesn't make the most sense.  For example, a PC trying to avoid being detected by  a creature that senses heartbeats might medita |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/18` | 0.833271 | The Stealth skill is designed to use Hide for avoiding  visual detection and Avoid Notice and Sneak to avoid  being both seen and heard. For many special senses,  a player can describe how they're avo |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/6/Text/21` | 0.817723 | You attempt a Stealth check to avoid notice while traveling  at half speed. If you're Avoiding Notice at the start of an  encounter, you usually roll a Stealth check instead of a  Perception check bot |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/7` | 0.759053 | Typically, you'll roll a Perception check to determine your  initiative—the more aware you are of your surroundings,  the more quickly you can respond. Sometimes, though, the  GM might call on you to |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.741293 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/18` | 0.740635 | You can't be seen. You're undetected to everyone. Creatures  can Seek to detect you; if a creature succeeds at its Perception  check against your Stealth DC, you become hidden to that  creature until |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/11` | 0.738683 | Typically, the GM tracks how well creatures detect each  other since neither party has perfect information. For  example, you might think a creature is in the last place  you sensed it, but it was abl |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/16/Text/15` | 0.732981 | noise), waking up if you succeed. If  creatures are attempting to stay quiet  around you, this Perception check uses  their Stealth DCs. Some effects make you sleep  so deeply that they don't allow yo |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.731452 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/16` | 0.727507 | Most abilities that designate "a creature you can see"  or the like function just as well if the user can precisely  sense the subject with a different sense. If a monster  uses a sense other than vis |

### Query 135
- Text: What is the rule about When it's your turn to act, you can use single actions ([one-action]),  short activities ([two-actions] and [three-actions]), reactions ([reaction]), and free actions  ([free-action]). When you're finished, your turn ends and the character  next in the initiative order begins their turn. Sometimes it's  important to note when during your turn something happens,  so a turn is divided into three steps.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `30`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/19` | 1.045126 | When it's your turn to act, you can use single actions ([one-action]),  short activities ([two-actions] and [three-actions]), reactions ([reaction]), and free actions  ([free-action]). When you're fin |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/13` | 0.877453 | You can use actions in any order you wish during your  turn, but you have to complete one action or activity before  beginning another; for example, you can't use a single action in  the middle of per |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/4/ListItem/7` | 0.842131 | You can use 1 free action or reaction with a trigger of  "Your turn begins" or something similar. |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/4/ListItem/21` | 0.837692 | You can use 1 free action or reaction with a trigger of  "Your turn ends" or something similar. |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/15` | 0.824127 | If you begin a 2-action or 3-action activity on your turn,  you must be able to complete it on your turn. You can't, for  example, begin to High Jump using your final action on one  turn and then comp |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/16` | 0.818253 | Once you've spent all three of your actions, your turn ends  (as described in Step 3) and the next creature's turn begins. You  can choose to end your turn early, losing all remaining actions  (but no |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/11` | 0.815292 | • Regain your 3 actions and 1 reaction. If you haven't spent  your reaction from your last turn, you lose it—you can't  "save" actions or reactions from one turn to use during the  next turn. Some abi |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/26` | 0.813405 | Your reactions let you respond immediately to what's  happening around you. The GM determines whether you can  use reactions before your first turn begins, depending on the  situation in which the enc |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/18` | 0.806700 | Once you've done all the things you want to do with the actions  you have available, you reach the end of your turn. Take the  following steps in any order you choose. Play then proceeds to  the next |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/14` | 0.792074 | you from acting. If you can't act, you can't use any actions,  including reactions and free actions. |

### Query 136
- Text: Summarize **Operative **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/26']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `18`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/34` | 0.938875 | **Operative ** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/53` | 0.938875 | **Operative ** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/26` | 0.938875 | **Operative ** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/31` | 0.938875 | **Operative ** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/36` | 0.938875 | **Operative ** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/43` | 0.938875 | **Operative ** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/61` | 0.938875 | **Operative ** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/52` | 0.838875 | **Operative ** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/48` | 0.838875 | **Operative ** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/42` | 0.838875 | **Operative ** |

### Query 137
- Text: What is the rule about For instance, suppose an enemy witchwarper cast  *invisibility* and then Sneaked away. You suspect that with  the witchwarper's Speed of 25 feet, they probably moved 15  feet toward an open door. You move up and attack a space 15  feet from where the witchwarper started and directly on the  path to the door. The GM secretly rolls an attack roll and flat  check, but they know that you weren't quite correct—your foe  was actually in the adjacent space! The GM tells you that you  missed, so you decide to make your next attack on the adjacent  space, just in case. This time, it's the right space, and the GM's  secret attack roll and flat check both succeed, so you hit!?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/2/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `33`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/2` | 1.040418 | For instance, suppose an enemy witchwarper cast  *invisibility* and then Sneaked away. You suspect that with  the witchwarper's Speed of 25 feet, they probably moved 15  feet toward an open door. You |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/1` | 0.776764 | Targeting an undetected creature is difficult. If you suspect  there's a creature around, you can pick a square and attempt  an attack. This works like targeting a hidden creature, but the  flat check |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/3` | 0.766782 | A creature you're undetected by can guess which square  you're in to try targeting you. It must pick a square and  attempt an attack. This works like targeting a hidden  creature (requiring a DC 11 fl |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/8/Text/13` | 0.731733 | You Seek meticulously for hidden doors, concealed hazards,  and so on. You can usually make an educated guess as to which  locations are best to check and move at half speed, but if you  want to be th |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.710796 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/6/Text/21` | 0.708985 | You attempt a Stealth check to avoid notice while traveling  at half speed. If you're Avoiding Notice at the start of an  encounter, you usually roll a Stealth check instead of a  Perception check bot |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/10` | 0.706093 | Attackers can target either you or your mount. An area effect  affects both of you as long as you're both in the area. You're  in an attacker's reach or range if any square of your mount is  within re |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/22` | 0.704013 | When targeting a hidden creature, before you roll to  determine your effect, you must attempt a DC 11 flat check.  If you fail, you don't affect the creature, though the actions  you used are still ex |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/6/Text/6` | 0.699356 | Depending on how the GM tracks movement, you move  in feet or miles based on your character's Speed with the  relevant movement type. Typical rates are on the table below. |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/1` | 0.692427 | your travel speed or slower. You have no chance of accidentally  overlooking a magic aura at a travel speed up to 300 feet per  minute, but must be traveling no more than 150 feet per minute  to detec |

### Query 138
- Text: Summarize SPECIAL ARCHETYPES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `69`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/20` | 0.952544 | SPECIAL ARCHETYPES |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/1` | 0.821735 | ARCHETYPES |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/46` | 0.725303 | **Archetypes** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/52` | 0.725303 | **Archetypes** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/38` | 0.725303 | **Archetypes** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/56` | 0.725303 | **Archetypes** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/14` | 0.722034 | SPELLCASTING ARCHETYPES |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/27` | 0.709839 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/21` | 0.709839 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/11` | 0.709839 | **ARCHETYPE** |

### Query 139
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/34']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `32`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/61` | 0.988833 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/45` | 0.988833 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/51` | 0.988833 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/69` | 0.988833 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/39` | 0.988833 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/34` | 0.988833 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/42` | 0.988833 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/19` | 0.988833 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/28` | 0.888833 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/57` | 0.888833 | **PLAYING THE ** **GAME** |

### Query 140
- Text: What are the requirements for **ENVOY DEDICATION** **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `43`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/27` | 0.885382 | **ENVOY DEDICATION** **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/24` | 0.791118 | **Prerequisites** Envoy Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/19` | 0.791118 | **Prerequisites** Envoy Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/34` | 0.791118 | **Prerequisites** Envoy Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/39` | 0.791118 | **Prerequisites** Envoy Dedication |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/10` | 0.786117 | **OPERATIVE DEDICATION** **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/5` | 0.760726 | **MYSTIC DEDICATION** **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/6` | 0.746690 | DEDICATION DETAILS |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/10` | 0.740750 | **SOLDIER DEDICATION** **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.730358 | **Prerequisites** Operative Dedication |

### Query 141
- Text: What are the requirements for **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `42`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.979799 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.890917 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12` | 0.877651 | **GET 'EM! **[one-action]** TO **[two-actions] |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.873763 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.854815 | **READY ARMS! **[one-action]** TO **[two-actions] |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.836623 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/22` | 0.823287 | **DANCE PARTNER! **[one-action]** TO **[two-actions] |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/39` | 0.821798 | **KEEP ON KEEPING ON!** [one-action]** TO **[two-actions] |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/9/SectionHeader/3` | 0.821010 | **STEEL YOURSELVES! **[one-action]** TO **[two-actions] |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/5` | 0.809367 | **COORDINATED AMBUSH! **[one-action]** TO **[two-actions] |

### Query 142
- Text: What is the rule about You gain the leader's confidence class feature (see page  107).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/25` | 0.941096 | You gain the leader's confidence class feature (see page  107). |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/40` | 0.768339 | You gain the primary target class feature (page 152). |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/35` | 0.745722 | You gain the suppressing fire class feature (page 152). |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/50` | 0.673025 | You gain the master spellcasting benefits (page 174). |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/52` | 0.673025 | You gain the master spellcasting benefits (page 174). |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/13` | 0.665166 | **Prerequisites** Strength +2 You gain the stellar attunement class feature (page 140), but |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/20` | 0.658452 | You gain the Lead by Example benefit for your Get 'Em!  directive, except you and your allies get a +2 status bonus  to damage on both the initial and subsequent Strikes. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/30` | 0.654207 | You gain the envoy directives class feature (see page  104), but do not gain the Lead by Example benefits  of the Get 'Em! envoy directive. You become trained in  Deception, Diplomacy, or Intimidation |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/47` | 0.653306 | You gain the expert spellcasting benefits (page 174). |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/45` | 0.653306 | You gain the expert spellcasting benefits (page 174). |

### Query 143
- Text: What are the requirements for **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `37`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.992294 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.877147 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.852087 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.845818 | **READY ARMS! **[one-action]** TO **[two-actions] |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12` | 0.834232 | **GET 'EM! **[one-action]** TO **[two-actions] |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/22` | 0.832511 | **DANCE PARTNER! **[one-action]** TO **[two-actions] |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.816834 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22` | 0.810746 | **SEARCH HIGH AND LOW! **[one-action]** TO **[two-actions] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/39` | 0.809687 | **KEEP ON KEEPING ON!** [one-action]** TO **[two-actions] |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/5` | 0.803524 | **COORDINATED AMBUSH! **[one-action]** TO **[two-actions] |

### Query 144
- Text: What is the rule about Scent involves sensing creatures or objects by smell, and is  usually a vague sense. The range is listed in the ability, and it  functions only if the creature or object being detected emits  an aroma. If a creature emits a heavy aroma or is upwind, the  GM can double or even triple the range of scent abilities used  to detect that creature, and the GM can reduce the range if a  creature is downwind.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `53`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/5` | 1.032098 | Scent involves sensing creatures or objects by smell, and is  usually a vague sense. The range is listed in the ability, and it  functions only if the creature or object being detected emits  an aroma |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/23` | 0.761512 | A character also has many vague senses—ones that can alert  you that something is there but aren't useful for zeroing in on  it to determine exactly what it is. The most useful of these  for a typical |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/16` | 0.756735 | Most abilities that designate "a creature you can see"  or the like function just as well if the user can precisely  sense the subject with a different sense. If a monster  uses a sense other than vis |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/7` | 0.755647 | Tremorsense allows a creature to feel the vibrations through  a solid surface caused by movement. It's usually an imprecise  sense with a limited range (listed in the ability). Tremorsense  functions |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/11` | 0.753076 | Typically, the GM tracks how well creatures detect each  other since neither party has perfect information. For  example, you might think a creature is in the last place  you sensed it, but it was abl |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.741827 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.729395 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.727157 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/24` | 0.720427 | When one creature might detect another, the GM almost  always uses the most precise sense available. |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 0.718244 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |

### Query 145
- Text: Summarize SPECIAL SENSES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `36`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/25` | 0.916069 | SPECIAL SENSES |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20` | 0.832168 | IMPRECISE SENSES |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17` | 0.804314 | PRECISE SENSES |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15` | 0.769832 | SENSES |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/22` | 0.734241 | VAGUE SENSES |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15` | 0.708328 | **DETECTING WITH OTHER SENSES** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/17` | 0.682403 | **Using Stealth with Other Senses** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/9/SectionHeader/25` | 0.640959 | SKILLS |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/5/SectionHeader/2` | 0.639628 | SPECIAL BATTLES |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/10/SectionHeader/3` | 0.634918 | CLASS FEATURES |

### Query 146
- Text: Summarize **MOVE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/2/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `58`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/23` | 0.939825 | **MOVE** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/16` | 0.939825 | **MOVE** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/2` | 0.939825 | **MOVE** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/7` | 0.939825 | **MOVE** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/32` | 0.939825 | **MOVE** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/11` | 0.939825 | **MOVE** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/4` | 0.939825 | **MOVE** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/23` | 0.939825 | **MOVE** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/4` | 0.939825 | **MOVE** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/12` | 0.939825 | **MOVE** |

### Query 147
- Text: What is the rule about An archetype feat is subject to any restrictions on the class  feat it replaces. For example, if you had an ability at 6th level  that granted you a bonus class feat, but that class feat had to  be 4th level or lower and have the vesk trait, you could use  that class feat to take an archetype class feat, but only one of  4th level or lower with the vesk trait.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `36`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/5` | 1.057195 | An archetype feat is subject to any restrictions on the class  feat it replaces. For example, if you had an ability at 6th level  that granted you a bonus class feat, but that class feat had to  be 4t |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` | 0.811259 | Some archetypes include a list of "Additional Feats" that  appear in other sources. The list includes each feat's level,  which might be different than normal when gained from the  archetype. You can |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.811107 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.804962 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/4` | 0.759286 | You gain an archetype by selecting archetype feats instead  of your normal feats. First, find the archetype that best  fits your character concept. Then select that archetype's  dedication feat, using |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/7` | 0.702333 | Each archetype's dedication feat represents your character's  dedicated effort learning a new set of abilities, making it  impossible to split your focus and pursue another archetype  at the same time |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/17` | 0.702275 | **Basic Spellcasting Feat:** Usually available at 4th level,  these feats grant a 1st-rank spell slot. At 6th level, they  grant you a 2nd-rank spell slot, and if you have a spell  repertoire, you can |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.698161 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.696423 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/16` | 0.691969 | class feat you have. As you continue selecting operative  archetype class feats, you continue to gain additional Hit Points  in this way. |

### Query 148
- Text: What are the requirements for **READY TO ROLL **[free-action] **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `36`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44` | 0.931694 | **READY TO ROLL **[free-action] **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/35` | 0.702612 | **SAW IT COMING **[free-action] **FEAT 4** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49` | 0.682475 | **YOU CAN DO IT **[one-action] **FEAT 14** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/2` | 0.673248 | **EXTEND DIRECTIVE **[free-action] **FEAT 16** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/34` | 0.667505 | **DOWN TO THE WIRE **[reaction] **FEAT 14** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.660248 | **READY ARMS! **[one-action]** TO **[two-actions] |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/39` | 0.657825 | **MASTER PLAN** **FEAT 14** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/33` | 0.651141 | 14TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.648916 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/16` | 0.641032 | **IMPROVISED LEGEND **[free-action] **FEAT 18** |

### Query 149
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `36`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/21` | 0.963367 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/47` | 0.963367 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/34` | 0.963367 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/23` | 0.963367 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/27` | 0.963367 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/30` | 0.963367 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/20` | 0.963367 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/24` | 0.866772 | INTRODUCTION |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/45` | 0.863367 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/24` | 0.863367 | **INTRODUCTION** |

### Query 150
- Text: What is the rule about There are only a few basic reactions and free actions that  all characters can use. You're more likely to gain actions with  triggers from your class, feats, and magic items.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `36`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/28` | 1.001834 | There are only a few basic reactions and free actions that  all characters can use. You're more likely to gain actions with  triggers from your class, feats, and magic items. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` | 0.770311 | **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reac |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.768412 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.758348 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/2` | 0.756900 | Some reactions and free actions are triggered by a  creature using an action with the move trait. The most  notable example is Reactive Strike (reproduced below).  Actions with the move trait can trig |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.754299 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.753163 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/2` | 0.748244 | Basic actions represent common tasks like moving around,  attacking, and helping others. As such, every creature can  use basic actions except in some extreme circumstances,  and many of those actions |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/7` | 0.735688 | Most effects are discrete, creating an instantaneous effect  when you let the GM know what actions you're going to use.  Firing a gun, moving to a new space, or taking something  out of your pack all |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` | 0.715754 | Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action. |

### Query 151
- Text: Summarize **Immunity, ** **Weakness, & ** **Resistance**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/32']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `43`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/57` | 1.014897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/38` | 1.014897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/44` | 1.014897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/23` | 1.014897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/33` | 1.014897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/30` | 1.014897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/32` | 1.014897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/13` | 0.954285 | **Immunity, ** **Weakness, & ** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/44` | 0.914897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/37` | 0.914897 | **Immunity, ** **Weakness, & ** **Resistance** |

### Query 152
- Text: Summarize **MANIPULATE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `48`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/11` | 0.947105 | **MANIPULATE** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/32` | 0.947105 | **MANIPULATE** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/15` | 0.947105 | **MANIPULATE** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/28` | 0.813032 | **AUDITORY** **MANIPULATE** **VISUAL** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/7/SectionHeader/14` | 0.769994 | **EXPLORATION** **MANIPULATE** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/7/SectionHeader/10` | 0.769994 | **EXPLORATION** **MANIPULATE** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/8/SectionHeader/3` | 0.769994 | **EXPLORATION** **MANIPULATE** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/27` | 0.717887 | **POINT OUT **[one-action] |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/8` | 0.708502 | **CONCENTRATE** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/40` | 0.708502 | **CONCENTRATE** |

### Query 153
- Text: What is the rule about Tremorsense allows a creature to feel the vibrations through  a solid surface caused by movement. It's usually an imprecise  sense with a limited range (listed in the ability). Tremorsense  functions only if the detecting creature is on the same surface  as the subject, and only if the subject is moving along (or  burrowing through) the surface.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `47`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/7` | 1.037607 | Tremorsense allows a creature to feel the vibrations through  a solid surface caused by movement. It's usually an imprecise  sense with a limited range (listed in the ability). Tremorsense  functions |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/5` | 0.756503 | Scent involves sensing creatures or objects by smell, and is  usually a vague sense. The range is listed in the ability, and it  functions only if the creature or object being detected emits  an aroma |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.735655 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 0.718863 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.715255 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.709952 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/16` | 0.695966 | Most abilities that designate "a creature you can see"  or the like function just as well if the user can precisely  sense the subject with a different sense. If a monster  uses a sense other than vis |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.695260 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/9` | 0.693578 | Three conditions measure the degree to which you can sense  a creature: observed, hidden, and undetected. However, the  concealed and invisible conditions can partially mask a  creature, and the unnot |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/23` | 0.693298 | A character also has many vague senses—ones that can alert  you that something is there but aren't useful for zeroing in on  it to determine exactly what it is. The most useful of these  for a typical |

### Query 154
- Text: Summarize **Immunity, ** **Weakness, & ** **Resistance**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/37']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `35`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/35` | 1.014897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/37` | 1.014897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/56` | 1.014897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/39` | 1.014897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/44` | 1.014897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/30` | 0.914897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/44` | 0.914897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/33` | 0.914897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/38` | 0.914897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/23` | 0.914897 | **Immunity, ** **Weakness, & ** **Resistance** |

### Query 155
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/24']
- Expected found: `True`
- Expected rank: `25`
- Graph boost applied: `True`
- Graph boosted count: `64`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/23` | 0.937823 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/54` | 0.937823 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/59` | 0.937823 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/64` | 0.937823 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/18` | 0.937823 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/44` | 0.937823 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/39` | 0.937823 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/49` | 0.937823 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/30` | 0.937823 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/35` | 0.937823 | **ARCHETYPE** |

### Query 156
- Text: What is the rule about **Checks**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `32`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/35` | 0.871192 | **Checks** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/33` | 0.871192 | **Checks** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/54` | 0.871192 | **Checks** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/37` | 0.871192 | **Checks** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/42` | 0.871192 | **Checks** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/28` | 0.771192 | **Checks** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/38` | 0.771192 | **Checks** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/30` | 0.771192 | **Checks** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/36` | 0.771192 | **Checks** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/31` | 0.771192 | **Checks** |

### Query 157
- Text: What are the requirements for **Prerequisites** Envoy Dedication?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/34']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/19` | 0.977387 | **Prerequisites** Envoy Dedication |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/24` | 0.977387 | **Prerequisites** Envoy Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/34` | 0.977387 | **Prerequisites** Envoy Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/39` | 0.977387 | **Prerequisites** Envoy Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/18` | 0.814548 | **Prerequisites** Soldier Dedication |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/39` | 0.814548 | **Prerequisites** Soldier Dedication |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/34` | 0.814548 | **Prerequisites** Soldier Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.795225 | **Prerequisites** Operative Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.795225 | **Prerequisites** Operative Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.795225 | **Prerequisites** Operative Dedication |

### Query 158
- Text: What is the rule about Effects can change the number of actions you can use on  your turn, or whether you can use actions at all. The slowed  condition, for example, causes you to lose actions, while the  quickened condition causes you to gain them. Conditions are  detailed in the appendix on pages 435–441. Whenever you  lose a number of actions—whether from these conditions or  in any other way—you choose which to lose if there's any  difference between them. For instance, the *haste* spell makes  you quickened, but it limits what you can use your extra  action to do. If you lost an action while *haste* was active, you  might want to lose the action from *haste* first since it's more  limited than your normal actions.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `44`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/6` | 1.078423 | Effects can change the number of actions you can use on  your turn, or whether you can use actions at all. The slowed  condition, for example, causes you to lose actions, while the  quickened conditio |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/15` | 0.861745 | Quickened, slowed, and stunned are the primary  ways you can gain or lose actions on a turn. The rules  for how this works appear on page 407. In brief, these  conditions alter how many actions you re |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` | 0.859891 | Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or S |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.830496 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/7` | 0.829866 | Some effects are even more restrictive. Certain abilities,  instead of or in addition to changing the number of actions  you can use, say specifically that you can't use reactions.  The most restricti |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/58` | 0.823719 | Some effects apply conditions to a creature or item. These change your state of being in some way. Conditions are  persistent, lasting until the stated duration ends, the condition is removed, or term |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/18` | 0.822432 | case of an activity, you usually lose all actions spent for the  activity up through the end of that turn. For instance, if you  began to Cast a Spell requiring 3 actions and the first action  was dis |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/7` | 0.807962 | Most effects are discrete, creating an instantaneous effect  when you let the GM know what actions you're going to use.  Firing a gun, moving to a new space, or taking something  out of your pack all |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/41` | 0.793537 | Choose one of your effects that has a sustained duration or  lists a special benefit when you Sustain it. Most such effects  come from spells or magic item activations. If the effect has a  sustained |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` | 0.788978 | Sometimes you need to attempt something not already  covered by defined actions in the game. When this happens,  the rules tell you how many actions you need to spend as  well as any traits your actio |

### Query 159
- Text: Summarize You issue directives to your allies, granting benefits and letting you take the lead.  Your words and deeds bolster your allies or harry your foes, and your cunning can  get you and your team out of danger.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `71`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/11` | 1.059160 | You issue directives to your allies, granting benefits and letting you take the lead.  Your words and deeds bolster your allies or harry your foes, and your cunning can  get you and your team out of d |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/9` | 0.857325 | Envoys encourage their allies with directives. A directive is  an order that benefits allies who follow it. Envoy directives  include a way for the envoy to lead by example by spending  more actions f |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/54` | 0.841181 | You provide a quick follow-up to your ongoing directive,  encouraging your ally when they successfully hit your |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/19` | 0.837589 | You're most comfortable leading your allies from the front lines  of battle while you fight alongside them. You might raise a  shield to help weather the storm of incoming gunfire or simply  lead with |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/48` | 0.834613 | You instinctively react to trouble by directing your allies to  act at the exact moment their intervention would matter  most. Issue a 1-action directive. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/3` | 0.831534 | **Directive**: Actions with this trait are special orders  that provide benefits for your allies if they follow  them. Your allies must be able to sense you to benefit  from your directives. This acti |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/36` | 0.829549 | You step up to lead during difficult times. You might have  experienced a traumatic event, perhaps escaping a pirate ship  during a mutiny, or you fought in some notorious battle. Your  allies trust y |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/15` | 0.817203 | People follow your lead because you help push them to  their ultimate potential. Each of your allies gain a second  reaction if they start their turn within 100 feet of you and  can perceive you. This |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/4` | 0.816301 | The envoy is a plucky leader who supports their  allies with battlefield directives, social savviness, and  a suite of skills. Envoys call out directives to their  allies, granting powerful boons that |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/2` | 0.808987 | You prefer to direct your allies in subtle ways, without drawing  much attention from foes. You might sneak in behind your  bodyguards or support your team from a safe distance. |

### Query 160
- Text: Summarize You increase your maximum number  of HP by this number at 1st level and  every level thereafter.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `45`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/9` | 1.034135 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 0.800500 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/1` | 0.745109 | rush into battle with weapons raised gain a higher number  of Hit Points each level, while characters who cast spells or  engage in trickery gain fewer. |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/5` | 0.743089 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/3` | 0.742523 | You gain more skill increases than members of other classes.  At 2nd level and every level thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you' |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/6` | 0.740410 | At 1st level, your class gives you  an attribute boost to Charisma. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/14` | 0.736042 | In addition to the initial ancestry feat you started with, you  gain an ancestry feat at 5th level and every 4 levels thereafter. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/44` | 0.733538 | At 1st level and every even-numbered level, you gain an envoy  class feat. These begin on page 108. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.731817 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/4` | 0.727872 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |

### Query 161
- Text: What are the requirements for **ADVANCED MYSTICISM** **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `45`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/27` | 0.836218 | **ADVANCED MYSTICISM** **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/17` | 0.741681 | **ADVANCED GUNNER** **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/31` | 0.740593 | **ADVANCED STELLAR ATTUNEMENT** **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/30` | 0.739199 | **ADVANCED DISTORTION** **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/25` | 0.738552 | **ADVANCED SOLDIER TRAINING** **FEAT 6** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/10` | 0.730838 | **ADVANCED LEADERSHIP** **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25` | 0.693326 | **Prerequisites** Mystic Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/36` | 0.693326 | **Prerequisites** Mystic Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/15` | 0.693326 | **Prerequisites** Mystic Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20` | 0.693326 | **Prerequisites** Mystic Dedication |

### Query 162
- Text: What are the requirements for **CUT 'EM DEEP** **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `29`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/43` | 0.809269 | **CUT 'EM DEEP** **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/550` | 0.705740 | Cut 'Em Deep |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/49` | 0.681325 | **GOT 'EM **[free-action] **FEAT 10** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/42` | 0.667979 | 10TH LEVEL |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/2` | 0.635784 | **SMOOTH DIVERSIONS** **FEAT 10** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/6/TableCell/352` | 0.628078 | 10 feet |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/7/TableCell/567` | 0.628078 | 10 feet |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/7/TableCell/561` | 0.628078 | 10 feet |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/7/TableCell/562` | 0.628078 | 10 feet |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/7` | 0.619902 | **Prerequisites** Size Up |

### Query 163
- Text: What is the rule about Some archetypes grant you a substantial degree of  spellcasting, albeit delayed compared to a character from a  spellcasting class. The spellcasting ability from a spellcasting  archetype also allows you to use Cast a Spell activations of  items (such as spell chips and spell gems).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `33`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/15` | 1.035048 | Some archetypes grant you a substantial degree of  spellcasting, albeit delayed compared to a character from a  spellcasting class. The spellcasting ability from a spellcasting  archetype also allows |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.842467 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.797090 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/5` | 0.774827 | An archetype feat is subject to any restrictions on the class  feat it replaces. For example, if you had an ability at 6th level  that granted you a bonus class feat, but that class feat had to  be 4t |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/2` | 0.767064 | Archetypes allow you to further customize your character concepts by taking more than one class. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` | 0.766461 | Some archetypes include a list of "Additional Feats" that  appear in other sources. The list includes each feat's level,  which might be different than normal when gained from the  archetype. You can |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.747585 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/10` | 0.747473 | You cast spells like a witchwarper. You gain access to the Cast  a Spell activity. You gain a spell repertoire with two common  cantrips from the spell list associated with your paradox, from  the spe |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/10` | 0.744618 | You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by you |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.743105 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |

### Query 164
- Text: Summarize **Soldier**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/28']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `34`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/38` | 0.907669 | **Soldier** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/28` | 0.907669 | **Soldier** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/33` | 0.907669 | **Soldier** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/36` | 0.907669 | **Soldier** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/55` | 0.907669 | **Soldier** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/45` | 0.907669 | **Soldier** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/63` | 0.907669 | **Soldier** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/54` | 0.807669 | **Soldier** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/50` | 0.807669 | **Soldier** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/44` | 0.807669 | **Soldier** |

### Query 165
- Text: What is the rule about Solarian envoys are beacons of hope amid a chaotic  battlefield leading the charge with feats like Pardon  Me and Get in There! A solarian envoy can use Adaptive  Talent to choose different Athletics feats based on the  terrain they expect to encounter.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `34`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/7` | 1.020184 | Solarian envoys are beacons of hope amid a chaotic  battlefield leading the charge with feats like Pardon  Me and Get in There! A solarian envoy can use Adaptive  Talent to choose different Athletics |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/5` | 0.735547 | Envoy solarians can rush into close quarters to  properly assess an enemy's abilities and positioning  when determining what directives to use. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/4` | 0.688847 | The solarian archetype allows characters to wield powerful  solar weapons and engage in melee combat. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/8` | 0.668736 | Soldier envoys make natural commanders who can  use their defensive capabilities to keep the bonuses  of their directive's active against powerful enemies  while clearing out weaker foes with area fir |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/ListItem/5` | 0.667674 | Envoy soldiers are natural tacticians who use directives to  position enemies and allies to optimize their area attacks. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/4` | 0.658356 | The envoy archetype allows you to take on a leadership role  by giving out directives that can support allies or hinder  enemies. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/6` | 0.650250 | Mystic solarians can augment themselves with  powerful spells and heal themselves while confronting  power enemies on the frontline. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/5` | 0.641420 | Mystic envoys can choose between using their magic  or directives to empower their allies, widening the  breadth of options available to them. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/35` | 0.636382 | You gain a 1st- or 2nd-level envoy feat of your choice. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/8` | 0.630252 | Soldier solarians with the close quarters fighting style  can use their solar weapon to dispatch multiple foes at  once, while using solar flare as a potent ranged option. |

### Query 166
- Text: What is the rule about **Activities** usually take longer and require using multiple  actions, which must be spent in succession. Strike is a single  action, but Double Tap is an activity in which you use both  the Aim and Strike actions to generate its effect.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `47`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/9` | 1.030780 | **Activities** usually take longer and require using multiple  actions, which must be spent in succession. Strike is a single  action, but Double Tap is an activity in which you use both  the Aim and |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 0.882368 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` | 0.798394 | Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or S |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/2` | 0.755543 | Basic actions represent common tasks like moving around,  attacking, and helping others. As such, every creature can  use basic actions except in some extreme circumstances,  and many of those actions |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/20` | 0.750237 | An activity typically involves using multiple actions to create  an effect greater than you can produce with a single action,  or combining multiple single actions to produce an effect  that's differe |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/9` | 0.747151 | Various abilities and conditions, such as a Reactive Strike,  can disrupt an action. When an action is disrupted, you still  use the actions or reactions you committed, and you still  expend any costs |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.742782 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` | 0.733372 | Sometimes you need to attempt something not already  covered by defined actions in the game. When this happens,  the rules tell you how many actions you need to spend as  well as any traits your actio |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/20` | 0.714100 | **Long Tasks:** For a task that takes longer than a  round, you often need to spend more than one action  preparing to help, as determined by the GM. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.707055 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |

### Query 167
- Text: Summarize **Movement**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/37']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `56`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/28` | 0.918841 | **Movement** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/49` | 0.918841 | **Movement** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/62` | 0.918841 | **Movement** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/38` | 0.918841 | **Movement** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/35` | 0.918841 | **Movement** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/43` | 0.918841 | **Movement** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/37` | 0.918841 | **Movement** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/45` | 0.918841 | **Movement** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/16` | 0.898496 | **MOVE** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/12` | 0.898496 | **MOVE** |

### Query 168
- Text: What is the rule about **Actions**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/41']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `21`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/48` | 0.817762 | **Actions** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/39` | 0.817762 | **Actions** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/41` | 0.817762 | **Actions** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/60` | 0.817762 | **Actions** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/43` | 0.817762 | **Actions** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/48` | 0.717762 | **Actions** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/42` | 0.717762 | **Actions** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/37` | 0.717762 | **Actions** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/34` | 0.717762 | **Actions** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/44` | 0.717762 | **Actions** |

### Query 169
- Text: What is the rule about The Stealth skill is designed to use Hide for avoiding  visual detection and Avoid Notice and Sneak to avoid  being both seen and heard. For many special senses,  a player can describe how they're avoiding detection  by that special sense and use the most applicable  Stealth action. For instance, a creature stepping lightly  to avoid being detected via tremorsense would be using Sneak.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `53`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/18` | 1.056445 | The Stealth skill is designed to use Hide for avoiding  visual detection and Avoid Notice and Sneak to avoid  being both seen and heard. For many special senses,  a player can describe how they're avo |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/19` | 0.856948 | In some cases, rolling a Dexterity-based Stealth  skill check to Sneak doesn't make the most sense.  For example, a PC trying to avoid being detected by  a creature that senses heartbeats might medita |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/12` | 0.850915 | You can attempt to avoid detection by using the Stealth  skill (page 207) to Avoid Notice, Hide, or Sneak, or by using  Deception to Create a Diversion (page 198). |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/6/Text/21` | 0.835000 | You attempt a Stealth check to avoid notice while traveling  at half speed. If you're Avoiding Notice at the start of an  encounter, you usually roll a Stealth check instead of a  Perception check bot |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.793818 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/18` | 0.791772 | You can't be seen. You're undetected to everyone. Creatures  can Seek to detect you; if a creature succeeds at its Perception  check against your Stealth DC, you become hidden to that  creature until |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.785817 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.777194 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/20` | 0.764971 | Anything in plain view is observed by you. If a creature takes  measures to avoid detection, such as by using Stealth to Hide,  it can become hidden or undetected instead of observed. If you |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 0.761319 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |

### Query 170
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/59']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `11`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/65` | 0.979439 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/59` | 0.979439 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/45` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/51` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/49` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/58` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/70` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/58` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/71` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/44` | 0.879439 | **GLOSSARY & ** **INDEX** |

### Query 171
- Text: Summarize **Rules Overview**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/34']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `33`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/53` | 1.006238 | **Rules Overview** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/34` | 1.006238 | **Rules Overview** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/32` | 1.006238 | **Rules Overview** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/36` | 1.006238 | **Rules Overview** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/41` | 1.006238 | **Rules Overview** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/54` | 0.906238 | **Rules Overview** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/20` | 0.906238 | **Rules Overview** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/30` | 0.906238 | **Rules Overview** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/37` | 0.906238 | **Rules Overview** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/41` | 0.906238 | **Rules Overview** |

### Query 172
- Text: Lookup values for SpeedFeet per
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/6/Table/8']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `28`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/6/TableCell/349` | 0.777223 | Feet per Minute |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/6/Table/8` | 0.752784 | SpeedFeet per MinuteMiles per HourMiles per Day10 feet1001815 feet1501-1/21220 feet20021625 feet2502-1/22030 feet30032435 feet3503-1/22840 feet40043250 feet50054060 feet600648 |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/6/TableCell/348` | 0.716698 | Speed |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/6/TableCell/350` | 0.691636 | Miles per Hour |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/6/SectionHeader/7` | 0.682344 | **TRAVEL SPEED** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/6/TableCell/351` | 0.673524 | Miles per Day |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/8/Text/13` | 0.664696 | You Seek meticulously for hidden doors, concealed hazards,  and so on. You can usually make an educated guess as to which  locations are best to check and move at half speed, but if you  want to be th |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/6/SectionHeader/5` | 0.661365 | TRAVEL SPEED |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/6/Text/6` | 0.648064 | Depending on how the GM tracks movement, you move  in feet or miles based on your character's Speed with the  relevant movement type. Typical rates are on the table below. |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/6/TableCell/356` | 0.618912 | 15 feet |

### Query 173
- Text: Summarize Three conditions measure the degree to which you can sense  a creature: observed, hidden, and undetected. However, the  concealed and invisible conditions can partially mask a  creature, and the unnoticed condition indicates you have no  idea a creature is around. You can find these conditions in  the Conditions Appendix on pages 435–441.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `59`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/9` | 1.090904 | Three conditions measure the degree to which you can sense  a creature: observed, hidden, and undetected. However, the  concealed and invisible conditions can partially mask a  creature, and the unnot |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.906386 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.885906 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/24` | 0.879654 | If a creature is undetected, you don't know what space it  occupies and you're off-guard to it. The Seek basic action can  help you find an undetected creature, usually making it hidden  from you inst |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/4` | 0.852990 | If you have no idea a creature is even present, that creature  is unnoticed by you. A creature that's undetected might also  be unnoticed. This condition usually matters for abilities  that can be use |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.848656 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.846404 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/20` | 0.839917 | Anything in plain view is observed by you. If a creature takes  measures to avoid detection, such as by using Stealth to Hide,  it can become hidden or undetected instead of observed. If you |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` | 0.833344 | With the exception of invisible, these conditions are  relative to the viewer—it's possible for a creature to be  observed to you but hidden from your ally. Most of these  rules apply to objects as we |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/23` | 0.827552 | A character also has many vague senses—ones that can alert  you that something is there but aren't useful for zeroing in on  it to determine exactly what it is. The most useful of these  for a typical |

### Query 174
- Text: What are the requirements for **Prerequisites** Size Up?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17` | 0.970795 | **Prerequisites** Size Up |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/7` | 0.970795 | **Prerequisites** Size Up |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/612` | 0.801945 | Size Up |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/30` | 0.757186 | **SIZE UP** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34` | 0.737380 | **Prerequisites** Watch Out |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/26` | 0.737380 | **Prerequisites** Watch Out |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.680369 | **Prerequisites** trained in Intimidation |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/58` | 0.667548 | **Prerequisites** Influence |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/25` | 0.665220 | **Prerequisites** adaptive talent |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/19` | 0.660268 | **Prerequisites **Improvised Mastery |

### Query 175
- Text: Summarize **AID DETAILS**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `40`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/18` | 0.981891 | **AID DETAILS** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/7` | 0.791094 | **AID **[reaction] |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/31` | 0.776373 | **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/54` | 0.747715 | **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/44` | 0.747715 | **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/35` | 0.746956 | **Rules Overview** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/30` | 0.746956 | **Rules Overview** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/37` | 0.746956 | **Rules Overview** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/54` | 0.746956 | **Rules Overview** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/20` | 0.746956 | **Rules Overview** |

### Query 176
- Text: Summarize Average vision is a precise sense—a sense that can be used to  perceive the world in nuanced detail. The only way to target
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `41`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/18` | 1.064171 | Average vision is a precise sense—a sense that can be used to  perceive the world in nuanced detail. The only way to target |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/10` | 0.762359 | In bright light, such as sunlight, creatures and objects can  be observed clearly by anyone with average vision or better. |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.756608 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/12/Text/14` | 0.754569 | Your eyes are overstimulated or your vision is swimming. If  vision is your only precise sense, all creatures and objects are  concealed from you. |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.751181 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.721885 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.709604 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/2` | 0.685095 | Your Perception measures your ability to notice things, search for what's hidden, and tell whether  something about a situation is suspicious. |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/1` | 0.681448 | such vision is in black and white only. Some forms of magical  darkness, such as a 4th-rank *darkness* spell, block normal  darkvision. A creature with greater darkvision, however, can  see through ev |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/12/Text/3` | 0.680708 | **Detection**: Observed, hidden, undetected, unnoticed **Senses**: Blinded, concealed, dazzled, deafened,  invisible |

### Query 177
- Text: What is the rule about You affect the world around you primarily by using actions, which produce effects. Actions are most  closely measured and restricted during the encounter mode of play, but even when it isn't important for  you to keep strict track of actions, they remain the way in which you interact with the game world.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `51`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/2` | 1.016674 | You affect the world around you primarily by using actions, which produce effects. Actions are most  closely measured and restricted during the encounter mode of play, but even when it isn't important |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/6/Text/2` | 0.825689 | Your movement and position determine how you interact with the world. Moving in exploration and  downtime modes is relatively fluid. Movement in encounter mode follows additional rules explained in  T |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/33` | 0.751179 | You use your hand or hands to manipulate an object or the  terrain. You can grab an unattended or stored object, draw  a weapon, swap a held item for another (see the Changing  Equipment table on page |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.749195 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/14/Text/1` | 0.748611 | An area always has a point of origin and extends out from that  point. There are four types of areas: bursts, cones, emanations,  and lines. When you're playing in encounter mode and using a  grid, ar |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/2` | 0.741811 | Anything you do in the game has an effect. Many of these outcomes are easy to adjudicate during the  game. If you tell the GM that you draw your laser pistol, no check is needed. Other times, the spec |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/13` | 0.737860 | Your movement during encounter mode—and at other times  where precise movement matters—depends on the actions  and other abilities you use. Whether you Stride, Step, Swim,  or Climb, the maximum dista |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/82` | 0.735560 | effect, though the GM makes the final call. In an area effect, creatures or targets must have line of  effect to the point of origin to be affected. If there's no line  of effect between the origin of |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/16` | 0.735358 | You attack with a weapon you're wielding or with an unarmed  attack, targeting one creature within your reach (for a melee  attack) or within range (for a ranged attack). Roll an attack  roll using th |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/6` | 0.724975 | You'll need to track your actions carefully in an encounter. At  the start of each turn you take in an encounter, you regain 3  actions and 1 reaction to spend that round. (Regaining your  actions is |

### Query 178
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/50']
- Expected found: `True`
- Expected rank: `28`
- Graph boost applied: `True`
- Graph boosted count: `64`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/23` | 0.937823 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/54` | 0.937823 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/59` | 0.937823 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/64` | 0.937823 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/18` | 0.937823 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/44` | 0.937823 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/39` | 0.937823 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/49` | 0.937823 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/30` | 0.937823 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/35` | 0.937823 | **ARCHETYPE** |

### Query 179
- Text: What are the requirements for **EXTEND DIRECTIVE **[free-action] **FEAT 16**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `55`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/2` | 0.965106 | **EXTEND DIRECTIVE **[free-action] **FEAT 16** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/566` | 0.773117 | Extend Directive |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44` | 0.730054 | **READY TO ROLL **[free-action] **FEAT 14** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/14` | 0.722796 | **SECONDARY DIRECTIVE **[one-action] **FEAT 12** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/16` | 0.698777 | **IMPROVISED LEGEND **[free-action] **FEAT 18** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/28` | 0.693016 | **UNSTOPPABLE DIRECTIVES** **FEAT 12** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/7` | 0.682100 | **GET THEM!** **FEAT 16** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/55` | 0.680617 | **EFFORTLESS INFLUENCER** **FEAT 16** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/54` | 0.667765 | 16TH LEVEL |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/8/SectionHeader/17` | 0.663089 | **IMPROVISED MASTERY **[free-action] |

### Query 180
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/40']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `26`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/28` | 0.988833 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/36` | 0.988833 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/26` | 0.988833 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/29` | 0.988833 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/34` | 0.988833 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/53` | 0.988833 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/40` | 0.988833 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/19` | 0.930070 | **PLAYING THE ** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/41` | 0.912216 | **GAME** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/34` | 0.888833 | **PLAYING THE ** **GAME** |

### Query 181
- Text: What is the rule about You gain an archetype by selecting archetype feats instead  of your normal feats. First, find the archetype that best  fits your character concept. Then select that archetype's  dedication feat, using one of your class feat choices. Once  you've taken the dedication feat, you can select any feat from  that archetype, as long as you meet its prerequisites. Most  archetype feats are taken in place of class feats, and so these  are called archetype class feats.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `44`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/4` | 1.049521 | You gain an archetype by selecting archetype feats instead  of your normal feats. First, find the archetype that best  fits your character concept. Then select that archetype's  dedication feat, using |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` | 0.916757 | Some archetypes include a list of "Additional Feats" that  appear in other sources. The list includes each feat's level,  which might be different than normal when gained from the  archetype. You can |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.898760 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.891906 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/7` | 0.887092 | Each archetype's dedication feat represents your character's  dedicated effort learning a new set of abilities, making it  impossible to split your focus and pursue another archetype  at the same time |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/5` | 0.847286 | An archetype feat is subject to any restrictions on the class  feat it replaces. For example, if you had an ability at 6th level  that granted you a bonus class feat, but that class feat had to  be 4t |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.831217 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/16` | 0.820416 | class feat you have. As you continue selecting operative  archetype class feats, you continue to gain additional Hit Points  in this way. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/24` | 0.776167 | You gain 3 additional Hit Points for each soldier archetype  class feat you have. As you continue selecting soldier  archetype class feats, you continue to gain additional Hit  Points in this way. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/2` | 0.773175 | Archetypes allow you to further customize your character concepts by taking more than one class. |

### Query 182
- Text: Summarize **Rules Overview**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `42`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/29` | 1.006238 | **Rules Overview** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/27` | 1.006238 | **Rules Overview** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/54` | 1.006238 | **Rules Overview** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/37` | 1.006238 | **Rules Overview** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/30` | 1.006238 | **Rules Overview** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/20` | 1.006238 | **Rules Overview** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/41` | 1.006238 | **Rules Overview** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/35` | 1.006238 | **Rules Overview** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/53` | 0.906238 | **Rules Overview** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/36` | 0.906238 | **Rules Overview** |

### Query 183
- Text: Summarize **Witchwarper**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/51']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `32`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/45` | 0.905156 | **Witchwarper** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/55` | 0.905156 | **Witchwarper** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/51` | 0.905156 | **Witchwarper** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/64` | 0.805156 | **Witchwarper** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/46` | 0.805156 | **Witchwarper** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/37` | 0.805156 | **Witchwarper** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/29` | 0.805156 | **Witchwarper** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/40` | 0.805156 | **Witchwarper** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/56` | 0.805156 | **Witchwarper** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/34` | 0.805156 | **Witchwarper** |

### Query 184
- Text: What is the rule about Skill Feats?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `57`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16` | 0.871982 | Skill Feats |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.728628 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/45` | 0.690010 | SKILL FEATS 2ND |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/42` | 0.688669 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/15` | 0.688669 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/66` | 0.688669 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/58` | 0.688669 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/31` | 0.688669 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/48` | 0.688669 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.669124 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |

### Query 185
- Text: What are the requirements for **Prerequisites** Operative Dedication?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/50']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `54`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.984207 | **Prerequisites** Operative Dedication |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.984207 | **Prerequisites** Operative Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.984207 | **Prerequisites** Operative Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/31` | 0.865466 | **Prerequisites** Operative Dedication, expert in any kind of  weapon or unarmed attack |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/36` | 0.851529 | **Prerequisites** Operative Dedication, expert in Perception |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/39` | 0.835639 | **Prerequisites** Soldier Dedication |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/18` | 0.835639 | **Prerequisites** Soldier Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/34` | 0.835639 | **Prerequisites** Soldier Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/65` | 0.819997 | **Prerequisites** Operative Dedication, class granting no more Hit  Points per level than 6 + your Constitution |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/45` | 0.797047 | **Prerequisites** Solarian Dedication |

### Query 186
- Text: Summarize Your Perception measures your ability to notice things, search for what's hidden, and tell whether  something about a situation is suspicious.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `49`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/2` | 1.061810 | Your Perception measures your ability to notice things, search for what's hidden, and tell whether  something about a situation is suspicious. |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.785412 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.763885 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/12/Text/3` | 0.759724 | **Detection**: Observed, hidden, undetected, unnoticed **Senses**: Blinded, concealed, dazzled, deafened,  invisible |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/9` | 0.753669 | Three conditions measure the degree to which you can sense  a creature: observed, hidden, and undetected. However, the  concealed and invisible conditions can partially mask a  creature, and the unnot |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.745447 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/7` | 0.740806 | Typically, you'll roll a Perception check to determine your  initiative—the more aware you are of your surroundings,  the more quickly you can respond. Sometimes, though, the  GM might call on you to |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/20` | 0.737069 | Anything in plain view is observed by you. If a creature takes  measures to avoid detection, such as by using Stealth to Hide,  it can become hidden or undetected instead of observed. If you |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/6` | 0.734531 | Perception is frequently used for rolling initiative in an  encounter, and for the Seek action. See page 396 for the  procedure for rolling a Perception check. |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/12/Text/14` | 0.728938 | Your eyes are overstimulated or your vision is swimming. If  vision is your only precise sense, all creatures and objects are  concealed from you. |

### Query 187
- Text: What is the rule about Targeting an undetected creature is difficult. If you suspect  there's a creature around, you can pick a square and attempt  an attack. This works like targeting a hidden creature, but the  flat check and attack roll are both rolled in secret by the GM.  The GM won't tell you why you missed—whether it was due  to failing the flat check, rolling an insufficient attack roll, or  choosing the wrong square. The GM might allow you to try  targeting an undetected creature with some spells or other  abilities in a similar fashion. Undetected creatures are subject  to area effects normally.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/2/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `39`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/1` | 1.069255 | Targeting an undetected creature is difficult. If you suspect  there's a creature around, you can pick a square and attempt  an attack. This works like targeting a hidden creature, but the  flat check |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/3` | 0.967205 | A creature you're undetected by can guess which square  you're in to try targeting you. It must pick a square and  attempt an attack. This works like targeting a hidden  creature (requiring a DC 11 fl |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/22` | 0.873652 | When targeting a hidden creature, before you roll to  determine your effect, you must attempt a DC 11 flat check.  If you fail, you don't affect the creature, though the actions  you used are still ex |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/17` | 0.844294 | You're difficult for one or more creatures to see due to thick  fog or some other obscuring feature. You can be concealed  to some creatures but not others. While concealed, you can  still be observed |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.832833 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/2` | 0.807211 | For instance, suppose an enemy witchwarper cast  *invisibility* and then Sneaked away. You suspect that with  the witchwarper's Speed of 25 feet, they probably moved 15  feet toward an open door. You |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/6` | 0.793806 | A concealed creature is in mist, within dim light, or amid  something else that obscures sight but isn't a physical  barrier. When you target a creature that's concealed  from you, you must attempt a |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/24` | 0.780757 | If a creature is undetected, you don't know what space it  occupies and you're off-guard to it. The Seek basic action can  help you find an undetected creature, usually making it hidden  from you inst |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/2` | 0.777046 | When you're undetected by a creature, that creature can't  see you at all, has no idea what space you occupy, and can't  target you, though you still can be affected by abilities that  target an area. |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/4` | 0.774732 | If you have no idea a creature is even present, that creature  is unnoticed by you. A creature that's undetected might also  be unnoticed. This condition usually matters for abilities  that can be use |

### Query 188
- Text: What are the requirements for **BASIC EPIPHANY** **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/33']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `36`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/33` | 0.858249 | **BASIC EPIPHANY** **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/17` | 0.680931 | **ADVANCED GUNNER** **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/25` | 0.680061 | **ADVANCED SOLDIER TRAINING** **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/31` | 0.662034 | **ADVANCED STELLAR ATTUNEMENT** **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/65` | 0.657548 | **Prerequisites** Operative Dedication, class granting no more Hit  Points per level than 6 + your Constitution |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/31` | 0.657156 | **SUPPRESSING FIRE** **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/36` | 0.651675 | **ADAPTIVE TALENT** **FEAT 6** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/37` | 0.646190 | **SOLAR FLARE** **FEAT 6** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/10` | 0.645589 | **ADVANCED LEADERSHIP** **FEAT 6** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/42` | 0.644321 | **SOLAR NIMBUS** **FEAT 6** |

### Query 189
- Text: Summarize ENVOY
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `81`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/1` | 0.917912 | ENVOY |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/43` | 0.838983 | ENVOY FEATS |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/14` | 0.838983 | ENVOY FEATS |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/46` | 0.825760 | **ENVOY** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/39` | 0.825760 | **ENVOY** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/9` | 0.825760 | **ENVOY** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/16` | 0.825760 | **ENVOY** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/3` | 0.825760 | **ENVOY** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/43` | 0.825760 | **ENVOY** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/31` | 0.825760 | **ENVOY** |

### Query 190
- Text: Summarize if you're using an imprecise sense or if an effect (such as  *invisibility*) prevents the subject from being observed.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `53`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/23` | 1.038307 | if you're using an imprecise sense or if an effect (such as  *invisibility*) prevents the subject from being observed. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/89` | 0.799735 | strong opinion about you. **Invisible:** Creatures can't see you. **Observed:** You're in plain view. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/62` | 0.774433 | **Concealed:** Fog or similar obscuration makes you difficult  to see and target. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/59` | 0.727221 | **Blinded:** You're unable to see. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/103` | 0.708206 | **Suppressed: **You're in a dangerous situation that forces |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/106` | 0.707845 | **Undetected:** A creature you're undetected by doesn't |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/16/Text/18` | 0.706438 | an effect followed by an interval in parentheses. When you  reach a given stage of an affliction, you're subjected to the  effects listed for that stage. |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/28` | 0.704937 | **AUDITORY** **MANIPULATE** **VISUAL** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/9` | 0.704494 | You end an effect that states you can Dismiss it. Dismissing  ends the entire effect unless noted otherwise. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/63` | 0.702090 | **Confused:** You attack indiscriminately. |

### Query 191
- Text: What is the rule about Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the dedication. There are also class archetypes that can  modify your class's abilities as soon as 1st level. You can  never have more than one class archetype.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `37`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 1.057474 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` | 0.899417 | Some archetypes include a list of "Additional Feats" that  appear in other sources. The list includes each feat's level,  which might be different than normal when gained from the  archetype. You can |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.882655 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.880917 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/4` | 0.864502 | You gain an archetype by selecting archetype feats instead  of your normal feats. First, find the archetype that best  fits your character concept. Then select that archetype's  dedication feat, using |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/5` | 0.861268 | An archetype feat is subject to any restrictions on the class  feat it replaces. For example, if you had an ability at 6th level  that granted you a bonus class feat, but that class feat had to  be 4t |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/7` | 0.840833 | Each archetype's dedication feat represents your character's  dedicated effort learning a new set of abilities, making it  impossible to split your focus and pursue another archetype  at the same time |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/2` | 0.774484 | Archetypes allow you to further customize your character concepts by taking more than one class. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/15` | 0.752077 | Some archetypes grant you a substantial degree of  spellcasting, albeit delayed compared to a character from a  spellcasting class. The spellcasting ability from a spellcasting  archetype also allows |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/16` | 0.748172 | class feat you have. As you continue selecting operative  archetype class feats, you continue to gain additional Hit Points  in this way. |

### Query 192
- Text: What is the rule about Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. These feats share their name with the  archetype; for instance, the witchwarper's master spellcasting  feat is called Master Witchwarper Spellcasting. All spell slots  you gain from spellcasting archetypes are subject to the  restrictions within the archetype. For instance, the mystic  archetype allows you to pick a connection when you take  its dedication feat. If you pick a connection granting divine  spells, the archetype then grants you spell slots you can use  only to cast divine spells you prepare as a mystic, even if you  are a witchwarper with occult spells in your repertoire.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `43`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 1.068128 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/10` | 0.858843 | You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by you |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/10` | 0.851622 | You cast spells like a witchwarper. You gain access to the Cast  a Spell activity. You gain a spell repertoire with two common  cantrips from the spell list associated with your paradox, from  the spe |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/15` | 0.824817 | Some archetypes grant you a substantial degree of  spellcasting, albeit delayed compared to a character from a  spellcasting class. The spellcasting ability from a spellcasting  archetype also allows |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.817542 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/29` | 0.791981 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the witchwarper  archetype, add a spell of the appropriate spell rank to your  repertoire: a co |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/17` | 0.761703 | **Basic Spellcasting Feat:** Usually available at 4th level,  these feats grant a 1st-rank spell slot. At 6th level, they  grant you a 2nd-rank spell slot, and if you have a spell  repertoire, you can |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/19` | 0.756586 | **Master Spellcasting Feat:** Usually found at 18th level, these  feats make you a master in spell attack modifiers and spell  DCs and grant you a 7th-rank spell slot. If you have a spell  repertoire, |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/44` | 0.756372 | **Prerequisites** Basic Witchwarper Spellcasting; master in Arcana  or Occultism, depending on paradox |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/5` | 0.752327 | An archetype feat is subject to any restrictions on the class  feat it replaces. For example, if you had an ability at 6th level  that granted you a bonus class feat, but that class feat had to  be 4t |

### Query 193
- Text: What is the rule about ACTIONS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `57`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/1` | 0.827995 | ACTIONS |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/39` | 0.747915 | Actions |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.740043 | These rules clarify some of the specifics of using actions. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/1` | 0.723445 | BASIC ACTIONS |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/6` | 0.723445 | BASIC ACTIONS |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/10` | 0.689055 | **IN-DEPTH ACTION RULES** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/5` | 0.682902 | GAINING AND LOSING  ACTIONS |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/61` | 0.672595 | **Actions** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/48` | 0.672595 | **Actions** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/34` | 0.672595 | **Actions** |

### Query 194
- Text: What is the rule about You gain a 1st- or 2nd-level envoy feat of your choice.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `38`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/35` | 0.969381 | You gain a 1st- or 2nd-level envoy feat of your choice. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/19` | 0.849455 | You gain a 1st- or 2nd-level soldier feat. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/26` | 0.810895 | You gain a 1st- or 2nd-level mystic feat. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/51` | 0.809038 | You gain a 1st- or 2nd-level operative feat. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/14` | 0.802403 | You gain one envoy feat. For the purpose of meeting its  prerequisites, your envoy level is equal to half your character  level. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/15` | 0.786331 | **Special** You can select this feat more than once. Each time  you select it, you gain another envoy feat. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/20` | 0.767376 | You gain a 1st- or 2nd-level solarian feat. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.747470 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/30` | 0.707917 | You gain the envoy directives class feature (see page  104), but do not gain the Lead by Example benefits  of the Get 'Em! envoy directive. You become trained in  Deception, Diplomacy, or Intimidation |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/15` | 0.705875 | Your disruptive powers grow. You gain a 1st- or 2nd-level  witchwarper feat. |

### Query 195
- Text: Summarize **Navasi**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/6` | 0.908894 | **Navasi** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/31` | 0.674164 | **Obozaya** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/7` | 0.672998 | **Navasi**, the human envoy, is a former space  pirate with a heart of gold. She's got a witty  remark for every occasion and a bullet for  anyone who would hurt one of her friends. |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7` | 0.663887 | **HIT POINTS** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/10` | 0.661086 | **Feats** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/44` | 0.661061 | **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/67` | 0.661061 | **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/56` | 0.661061 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/26` | 0.655493 | **Operative ** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/36` | 0.655493 | **Operative ** |

### Query 196
- Text: What are the requirements for **DOWN TO THE WIRE **[reaction] **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `46`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/34` | 0.895001 | **DOWN TO THE WIRE **[reaction] **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44` | 0.733881 | **READY TO ROLL **[free-action] **FEAT 14** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.695150 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.690072 | **WATCH OUT **[reaction] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49` | 0.688143 | **YOU CAN DO IT **[one-action] **FEAT 14** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.680325 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/33` | 0.669256 | 14TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/26` | 0.665827 | **QUIP **[reaction] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/19` | 0.663365 | **NOT IN THE FACE **[reaction] **FEAT 4** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.653477 | **READY ARMS! **[one-action]** TO **[two-actions] |

### Query 197
- Text: What is the rule about These icons appear in stat blocks as shorthand for each  type of action. As a player, you'll usually see the icon in  an action's header (such as in a basic action, skill action,  feat, or spell). In a creature stat block, or a feat that  gives you a new action in addition to other benefits, the  icon will appear in the running text. For examples, see  the formatting of rules on page 15.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `39`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/13` | 1.065800 | These icons appear in stat blocks as shorthand for each  type of action. As a player, you'll usually see the icon in  an action's header (such as in a basic action, skill action,  feat, or spell). In |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/16/Text/5` | 0.755333 | Whether appearing in a spell, as an item, or within a creature's  stat block, afflictions appear in the following format. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/58` | 0.705913 | Some effects apply conditions to a creature or item. These change your state of being in some way. Conditions are  persistent, lasting until the stated duration ends, the condition is removed, or term |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` | 0.686410 | Sometimes you need to attempt something not already  covered by defined actions in the game. When this happens,  the rules tell you how many actions you need to spend as  well as any traits your actio |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/6/Text/11` | 0.684972 | Most characters and monsters have a Speed statistic that  indicates how quickly they can move on a solid surface. This  statistic is referred to as land Speed when it's necessary to  differentiate it |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/7` | 0.683347 | Most effects are discrete, creating an instantaneous effect  when you let the GM know what actions you're going to use.  Firing a gun, moving to a new space, or taking something  out of your pack all |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/6` | 0.681302 | You'll need to track your actions carefully in an encounter. At  the start of each turn you take in an encounter, you regain 3  actions and 1 reaction to spend that round. (Regaining your  actions is |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/16/Text/7` | 0.680141 | The affliction's name is given first, followed by its traits in  parentheses—including the trait for the type of affliction  (curse, disease, poison, and so forth). If the affliction needs  to have a |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/3` | 0.674359 | Actions that are used less frequently but are still available  to most creatures are presented in Specialty Basic Actions  starting on page 410. These typically have requirements that  not all charact |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/2` | 0.673584 | Basic actions represent common tasks like moving around,  attacking, and helping others. As such, every creature can  use basic actions except in some extreme circumstances,  and many of those actions |

### Query 198
- Text: What are the requirements for **Prerequisites** Wisdom +2?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `47`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/8` | 0.977407 | **Prerequisites** Wisdom +2 |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/8` | 0.834266 | **Prerequisites** Intelligence +2 |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/29` | 0.813181 | **Prerequisites** Charisma +2 |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/13` | 0.801798 | **Prerequisites** Dexterity +2 |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/12` | 0.764555 | **Prerequisites** Constitution +2 |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/13` | 0.693861 | **Prerequisites** Strength +2 You gain the stellar attunement class feature (page 140), but |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/26` | 0.644008 | You gain a 1st- or 2nd-level mystic feat. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/45` | 0.643073 | Your proficiency rank in Fortitude saves increases to master. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/36` | 0.638548 | **Prerequisites** Mystic Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20` | 0.638548 | **Prerequisites** Mystic Dedication |

### Query 199
- Text: What are the requirements for **EXPERT MYSTIC SPELLCASTING** **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `56`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/43` | 0.898416 | **EXPERT MYSTIC SPELLCASTING** **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/41` | 0.799871 | **EXPERT WITCHWARPER SPELLCASTING** **FEAT 12** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/51` | 0.770623 | **Prerequisites** Expert Mystic Spellcasting; legendary in  connection skill |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/48` | 0.725479 | **MASTER MYSTIC SPELLCASTING** **FEAT 18** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/33` | 0.714985 | **MASTER SPY** **FEAT 12** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/28` | 0.704809 | **GUN EXPERT** **FEAT 12** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/17` | 0.698182 | **BASIC MYSTIC SPELLCASTING** **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/46` | 0.695210 | **Prerequisites** Basic Mystic Spellcasting; master in  connection skill |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41` | 0.678641 | **Prerequisites** Basic Mystic Spellcasting |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/18` | 0.665941 | **Expert Spellcasting Feat:** Typically taken at 12th level,  these feats make you an expert in spell attack modifiers  and spell DCs and grant you a 4th-rank spell slot. If you  have a spell repertoi |
