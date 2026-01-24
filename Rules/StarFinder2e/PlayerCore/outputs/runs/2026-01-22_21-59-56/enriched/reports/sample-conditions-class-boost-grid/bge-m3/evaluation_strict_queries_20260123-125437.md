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
- MRR: `0.8455`
- hit@1: `0.7850`
- hit@3: `0.8900`
- hit@5: `0.9250`
- hit@10: `0.9700`
- Embeddings reused: `False`
- Graph boost: `0.02` (depth=2, top_k=50)

## Timings (ms)
- Embedding: `79924`
- Evaluation: `219`

## Query Details
### Query 0
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/58']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `6`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/44` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/58` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/52` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/52` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/35` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/40` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/62` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/46` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/31` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/70` | 0.900802 | **CONDITIONS ** **APPENDIX** |

### Query 1
- Text: Summarize **Hero Points**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `20`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/16` | 0.904027 | **Hero Points** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/35` | 0.904027 | **Hero Points** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/60` | 0.904027 | **Hero Points** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/36` | 0.904027 | **Hero Points** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/26` | 0.904027 | **Hero Points** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/47` | 0.904027 | **Hero Points** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/33` | 0.904027 | **Hero Points** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/41` | 0.904027 | **Hero Points** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/59` | 0.884027 | **Hero Points** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/42` | 0.884027 | **Hero Points** |

### Query 2
- Text: What is the rule about [three-actions] Three-Action Activity?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/16` | 0.775502 | [three-actions] Three-Action Activity |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/15` | 0.633783 | [two-actions] Two-Action Activity |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/15` | 0.607759 | If you begin a 2-action or 3-action activity on your turn,  you must be able to complete it on your turn. You can't, for  example, begin to High Jump using your final action on one  turn and then comp |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.590029 | These rules clarify some of the specifics of using actions. |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/19` | 0.579977 | When it's your turn to act, you can use single actions ([one-action]),  short activities ([two-actions] and [three-actions]), reactions ([reaction]), and free actions  ([free-action]). When you're fin |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/39` | 0.579204 | Actions |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/1` | 0.571109 | ACTIONS |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/1` | 0.562352 | BASIC ACTIONS |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/6` | 0.562352 | BASIC ACTIONS |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.559536 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |

### Query 3
- Text: What are the requirements for **OPERATIVE DEDICATION** **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `44`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/10` | 0.801866 | **OPERATIVE DEDICATION** **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.745369 | **Prerequisites** Operative Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.745369 | **Prerequisites** Operative Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.745369 | **Prerequisites** Operative Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/5` | 0.684143 | **MYSTIC DEDICATION** **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/10` | 0.683877 | **SOLDIER DEDICATION** **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/27` | 0.669979 | **ENVOY DEDICATION** **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/10` | 0.661545 | **SOLARIAN DEDICATION** **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/65` | 0.661292 | **Prerequisites** Operative Dedication, class granting no more Hit  Points per level than 6 + your Constitution |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/36` | 0.659222 | **Prerequisites** Operative Dedication, expert in Perception |

### Query 4
- Text: What is the rule about When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency ranks range from trained to legendary.  For instance, a character trained with a battle ribbon can  use it effectively to dispatch foes, while a character who  is legendary with the weapon might be able to spell out  their name in decorative cursive script with just a flick of  their wrist!?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `34`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.989972 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.788451 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 0.767653 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` | 0.734114 | Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  char |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.717368 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.712363 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/8` | 0.701001 | If something isn't listed in your character's class entry,  their proficiency rank in that statistic is untrained unless  they gain training from another source. If your character  is untrained in som |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 0.700107 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/10` | 0.699774 | from their class features; and more. Your character's class  entry also provides the information needed when they  gain levels, so it will be a vital reference throughout the  course of your campaign. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.699204 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |

### Query 5
- Text: Summarize **Mystic**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/25']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `14`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/42` | 0.823583 | **Mystic** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/25` | 0.823583 | **Mystic** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/52` | 0.823583 | **Mystic** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/35` | 0.823583 | **Mystic** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/30` | 0.823583 | **Mystic** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/60` | 0.823583 | **Mystic** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/47` | 0.803583 | **Mystic** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/51` | 0.803583 | **Mystic** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/41` | 0.803583 | **Mystic** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/1` | 0.691345 | MYSTIC |

### Query 6
- Text: Summarize KEY ATTRIBUTE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `17`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/13` | 0.836928 | KEY ATTRIBUTE |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/4` | 0.759983 | **KEY ATTRIBUTE** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/1` | 0.624515 | **KEY TERMS** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/4` | 0.619623 | **Attributes** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/51` | 0.607015 | CHARACTER Sheet |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11` | 0.605806 | CLASS FEATURES |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26` | 0.605806 | CLASS FEATURES |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/14` | 0.601393 | ENVOY FEATS |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/43` | 0.601393 | ENVOY FEATS |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/1` | 0.597525 | **ENVOY FEATS BY NAME** |

### Query 7
- Text: Summarize You fall prone.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/2/Text/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `39`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/24` | 0.939201 | You fall prone. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/31` | 0.797160 | **Trigger** You fall. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/5` | 0.795317 | You stand up from being prone. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/96` | 0.732457 | **Prone:** You're lying on the ground and easier to attack. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/99` | 0.728306 | creature has you pinned. |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/105` | 0.727092 | **Unconscious:** You're asleep or knocked out. |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/7/SectionHeader/4` | 0.725941 | FALLING ON A CREATURE |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/68` | 0.716562 | vitality. **Dying:** You're slipping closer to death. |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/16` | 0.708180 | **Trigger** You fall from or past an edge or handhold. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/63` | 0.675548 | **Confused:** You attack indiscriminately. |

### Query 8
- Text: What is the rule about Mystic operatives might run out of spells, but they won't  run out of shells.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/ListItem/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/ListItem/6` | 0.894070 | Mystic operatives might run out of spells, but they won't  run out of shells. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/4` | 0.529099 | Mystics support allies and themselves with powerful magic. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/6` | 0.521802 | Mystic solarians can augment themselves with  powerful spells and heal themselves while confronting  power enemies on the frontline. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/31` | 0.511019 | You gain one mystic feat. For the purpose of meeting its  prerequisites, your mystic level is half your character level. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/51` | 0.509081 | **Prerequisites** Expert Mystic Spellcasting; legendary in  connection skill |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/26` | 0.505863 | You gain a 1st- or 2nd-level mystic feat. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/22` | 0.502850 | You gain one operative feat. For the purpose of meeting its  prerequisites, your operative level is half your character level. |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/7` | 0.499499 | Most effects are discrete, creating an instantaneous effect  when you let the GM know what actions you're going to use.  Firing a gun, moving to a new space, or taking something  out of your pack all |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/1` | 0.493519 | MYSTIC |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/10` | 0.493461 | You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by you |

### Query 9
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `16`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/27` | 0.776592 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/33` | 0.776592 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/35` | 0.776592 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/30` | 0.770199 | SPELLS |
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
- Graph boosted count: `27`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.952125 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/29` | 0.848349 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the witchwarper  archetype, add a spell of the appropriate spell rank to your  repertoire: a co |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/10` | 0.768804 | You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by you |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/42` | 0.767619 | Increase the number of spells in your repertoire and number  of spell slots you gain from mystic archetype feats by 1 for  each spell rank other than your two highest mystic spell slots. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/17` | 0.743970 | **Basic Spellcasting Feat:** Usually available at 4th level,  these feats grant a 1st-rank spell slot. At 6th level, they  grant you a 2nd-rank spell slot, and if you have a spell  repertoire, you can |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/31` | 0.734062 | **Learn a Spell:** You use the skill corresponding to  the spell's tradition to gain access to a new spell  (page 189). |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/40` | 0.723936 | Your repertoire expands, and you can cast more spells of your  paradox's tradition each day. Increase the number of spells  in your repertoire and number of spell slots you gain from  witchwarper arch |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.717445 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/9` | 0.705411 | Choose a connection (see page 119). You become trained in  the connection's skill or, if you were already trained, you  become trained in a skill of your choice. You don't gain any  other abilities fr |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/18` | 0.688556 | **Expert Spellcasting Feat:** Typically taken at 12th level,  these feats make you an expert in spell attack modifiers  and spell DCs and grant you a 4th-rank spell slot. If you  have a spell repertoi |

### Query 11
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/27']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `15`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/31` | 0.747771 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/37` | 0.747771 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/29` | 0.747771 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/26` | 0.747771 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/27` | 0.747771 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/27` | 0.747771 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/33` | 0.747771 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/48` | 0.747771 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/29` | 0.747771 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/9/SectionHeader/25` | 0.745791 | SKILLS |

### Query 12
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/26']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `12`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/24` | 0.883367 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/30` | 0.883367 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/23` | 0.883367 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/26` | 0.883367 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/26` | 0.883367 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/34` | 0.883367 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/24` | 0.883367 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/45` | 0.883367 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/28` | 0.883367 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/31` | 0.863367 | **INTRODUCTION** |

### Query 13
- Text: What is the rule about MULTICLASS ENVOY  CHARACTERS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/3` | 0.869274 | MULTICLASS ENVOY  CHARACTERS |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/3` | 0.676588 | MULTICLASS OPERATIVE  CHARACTERS |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/3` | 0.620508 | MULTICLASS SOLDIER  CHARACTERS |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/3` | 0.615265 | MULTICLASS MYSTIC  CHARACTERS |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/3` | 0.600710 | MULTICLASS SOLARIAN  CHARACTERS |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/3` | 0.596311 | MULTICLASS WITCHWARPER  CHARACTERS |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26` | 0.594364 | CLASS FEATURES |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11` | 0.594364 | CLASS FEATURES |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/10/SectionHeader/3` | 0.594364 | CLASS FEATURES |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/14` | 0.592173 | ENVOY FEATS |

### Query 14
- Text: What is the rule about case of an activity, you usually lose all actions spent for the  activity up through the end of that turn. For instance, if you  began to Cast a Spell requiring 3 actions and the first action  was disrupted, you lose all 3 actions that you committed to  that activity.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/18` | 0.956784 | case of an activity, you usually lose all actions spent for the  activity up through the end of that turn. For instance, if you  began to Cast a Spell requiring 3 actions and the first action  was dis |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.769202 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/24` | 0.712267 | Activities that take longer than a turn can't normally be  performed during an encounter. Spells with a casting time of  1 minute or more are a common example, as are several skill  actions. When you |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/16` | 0.676636 | Once you've spent all three of your actions, your turn ends  (as described in Step 3) and the next creature's turn begins. You  can choose to end your turn early, losing all remaining actions  (but no |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/11` | 0.667260 | • Regain your 3 actions and 1 reaction. If you haven't spent  your reaction from your last turn, you lose it—you can't  "save" actions or reactions from one turn to use during the  next turn. Some abi |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/6` | 0.663668 | Effects can change the number of actions you can use on  your turn, or whether you can use actions at all. The slowed  condition, for example, causes you to lose actions, while the  quickened conditio |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/6` | 0.662112 | You'll need to track your actions carefully in an encounter. At  the start of each turn you take in an encounter, you regain 3  actions and 1 reaction to spend that round. (Regaining your  actions is |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/15` | 0.658026 | Quickened, slowed, and stunned are the primary  ways you can gain or lose actions on a turn. The rules  for how this works appear on page 407. In brief, these  conditions alter how many actions you re |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` | 0.657128 | Sometimes you need to attempt something not already  covered by defined actions in the game. When this happens,  the rules tell you how many actions you need to spend as  well as any traits your actio |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/15` | 0.655919 | If you begin a 2-action or 3-action activity on your turn,  you must be able to complete it on your turn. You can't, for  example, begin to High Jump using your final action on one  turn and then comp |

### Query 15
- Text: What is the rule about You gain the envoy directives class feature (see page  104), but do not gain the Lead by Example benefits  of the Get 'Em! envoy directive. You become trained in  Deception, Diplomacy, or Intimidation plus another skill of your  choice. If you were already trained in Deception, Diplomacy,  and Intimidation, you instead become trained in an additional  skill of your choice. You also become trained in envoy class DC.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `12`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/30` | 0.984120 | You gain the envoy directives class feature (see page  104), but do not gain the Lead by Example benefits  of the Get 'Em! envoy directive. You become trained in  Deception, Diplomacy, or Intimidation |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/13` | 0.718416 | You become trained in Intimidation. If you  were already trained in Intimidation, you  instead become trained in a skill of your choice.  Increase your maximum and encumbered Bulk limits  by 2. You be |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/56` | 0.709495 | Trained in one of the following skills  of your choice: Deception, Diplomacy,  Intimidation |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/10` | 0.705497 | You begin with one envoy directive. You can learn more  directives through the envoy class, envoy class feats, and your  leadership style. You can issue one directive a round. Unless  otherwise stated |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/20` | 0.689358 | You gain the Lead by Example benefit for your Get 'Em!  directive, except you and your allies get a +2 status bonus  to damage on both the initial and subsequent Strikes. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/64` | 0.677804 | Trained in envoy class DC |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.670804 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/17` | 0.655379 | Whether it comes naturally, or you trained for it, you've  developed a personal style of leading others. At 1st level,  select a leadership style. You become trained in the indicated  leadership skill |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/61` | 0.653887 | Choose a specialization. You become trained in one skill  determined by your specialization; if you were already trained  in that skill, you instead become trained in another skill of your  choice. Yo |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.649674 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |

### Query 16
- Text: What are the requirements for **CHANGE OF PLANS **[reaction] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/9` | 0.854216 | **CHANGE OF PLANS **[reaction] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/544` | 0.676451 | Change of Plans |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.654681 | **READY ARMS! **[one-action]** TO **[two-actions] |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.649179 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.635899 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/4/SectionHeader/12` | 0.629977 | STEP 2: ACT |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.628032 | **WATCH OUT **[reaction] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.625171 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/6` | 0.616609 | **READY **[two-actions] |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12` | 0.608659 | **GET 'EM! **[one-action]** TO **[two-actions] |

### Query 17
- Text: What is the rule about An activity typically involves using multiple actions to create  an effect greater than you can produce with a single action,  or combining multiple single actions to produce an effect  that's different from merely the sum of those actions. In some  cases, usually when spellcasting, an activity can consist of  only 1 action, 1 reaction, or even 1 free action.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `37`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/20` | 0.950952 | An activity typically involves using multiple actions to create  an effect greater than you can produce with a single action,  or combining multiple single actions to produce an effect  that's differe |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` | 0.720539 | Sometimes you need to attempt something not already  covered by defined actions in the game. When this happens,  the rules tell you how many actions you need to spend as  well as any traits your actio |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/12` | 0.706586 | Abilities that generate an effect typically work within a  specified range or a reach. Most spells and abilities list a  **range**—the maximum distance from the creature or object  creating the effect |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/7` | 0.697842 | Some effects are even more restrictive. Certain abilities,  instead of or in addition to changing the number of actions  you can use, say specifically that you can't use reactions.  The most restricti |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/9` | 0.695650 | **Activities** usually take longer and require using multiple  actions, which must be spent in succession. Strike is a single  action, but Double Tap is an activity in which you use both  the Aim and |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` | 0.682549 | Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or S |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/6` | 0.675012 | Effects can change the number of actions you can use on  your turn, or whether you can use actions at all. The slowed  condition, for example, causes you to lose actions, while the  quickened conditio |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.672036 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/28` | 0.667898 | There are only a few basic reactions and free actions that  all characters can use. You're more likely to gain actions with  triggers from your class, feats, and magic items. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 0.667334 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |

### Query 18
- Text: What is the rule about ACTIVITIES?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `36`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/19` | 0.686120 | ACTIVITIES |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/1` | 0.649326 | ACTIONS |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.628252 | These rules clarify some of the specifics of using actions. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/39` | 0.612839 | Actions |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/1` | 0.596969 | BASIC ACTIONS |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/6` | 0.596969 | BASIC ACTIONS |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/10` | 0.578853 | **IN-DEPTH ACTION RULES** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/9` | 0.559727 | **Activities** usually take longer and require using multiple  actions, which must be spent in succession. Strike is a single  action, but Double Tap is an activity in which you use both  the Aim and |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/13` | 0.557962 | You can use actions in any order you wish during your  turn, but you have to complete one action or activity before  beginning another; for example, you can't use a single action in  the middle of per |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/4/SectionHeader/23` | 0.556908 | ACTIVITIES IN ENCOUNTERS |

### Query 19
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/22']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `15`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/21` | 0.800013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/35` | 0.800013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/24` | 0.800013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/22` | 0.800013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/48` | 0.800013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/28` | 0.800013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/35` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/25` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/29` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/31` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 20
- Text: What is the rule about from their class features; and more. Your character's class  entry also provides the information needed when they  gain levels, so it will be a vital reference throughout the  course of your campaign.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `38`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/10` | 0.890731 | from their class features; and more. Your character's class  entry also provides the information needed when they  gain levels, so it will be a vital reference throughout the  course of your campaign. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.748830 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.713865 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` | 0.694946 | Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  char |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` | 0.682397 | This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chos |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.672972 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.668077 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/Table/2` | 0.661680 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat2Envoy feat, skill feat, skill increase3Adaptive talent, genera |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.661589 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.660750 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |

### Query 21
- Text: What is the rule about HIT POINTS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `8`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/18` | 0.740602 | HIT POINTS |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7` | 0.641307 | **HIT POINTS** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/15` | 0.621836 | **Hit Points, ** **Healing, and ** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/37` | 0.608817 | Hit Points, Healing, and Dying |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` | 0.603833 | This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chos |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/38` | 0.603250 | Hero Points |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/31` | 0.597244 | Your confidence is a battery that keeps your allies going.  When you use a directive that grants temporary Hit Points, |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 0.590843 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/25` | 0.587461 | **Hit Points, ** **Healing, and ** **Dying** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/34` | 0.587461 | **Hit Points, ** **Healing, and ** **Dying** |

### Query 22
- Text: What is the rule about Archetypes allow you to further customize your character concepts by taking more than one class.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/2` | 0.873845 | Archetypes allow you to further customize your character concepts by taking more than one class. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.707725 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/7` | 0.684603 | **Archetypes** on page 174 gives you thematic options  that allow you to further customize your character's  abilities. Though these rules are not recommended for  beginners, the archetypes in this bo |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.675893 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/4` | 0.658362 | You gain an archetype by selecting archetype feats instead  of your normal feats. First, find the archetype that best  fits your character concept. Then select that archetype's  dedication feat, using |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.657155 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/16` | 0.639031 | class feat you have. As you continue selecting operative  archetype class feats, you continue to gain additional Hit Points  in this way. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/5` | 0.635471 | An archetype feat is subject to any restrictions on the class  feat it replaces. For example, if you had an ability at 6th level  that granted you a bonus class feat, but that class feat had to  be 4t |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` | 0.628273 | Some archetypes include a list of "Additional Feats" that  appear in other sources. The list includes each feat's level,  which might be different than normal when gained from the  archetype. You can |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/4` | 0.612410 | The operative archetype allows you to deal high damage to  a single target and select class feats and exploits that add to  your offensive options in combat. |

### Query 23
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/38']
- Expected found: `True`
- Expected rank: `44`
- Graph boost applied: `True`
- Graph boosted count: `49`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/23` | 0.857823 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/54` | 0.857823 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/59` | 0.857823 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/64` | 0.857823 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/18` | 0.857823 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/44` | 0.857823 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/39` | 0.857823 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/49` | 0.857823 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/30` | 0.857823 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/35` | 0.857823 | **ARCHETYPE** |

### Query 24
- Text: What is the rule about [reaction] Reaction?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `29`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/ListItem/17` | 0.666029 | [reaction] Reaction |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` | 0.618388 | **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reac |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/4/SectionHeader/25` | 0.592027 | REACTIONS IN ENCOUNTERS |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/26` | 0.585359 | Your reactions let you respond immediately to what's  happening around you. The GM determines whether you can  use reactions before your first turn begins, depending on the  situation in which the enc |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/7` | 0.583725 | **AID **[reaction] |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/8/SectionHeader/4` | 0.581905 | **REACTIVE STRIKE **[reaction] |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/14` | 0.570661 | **GRAB AN EDGE **[reaction] |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.569004 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.562750 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.561789 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |

### Query 25
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/12']
- Expected found: `True`
- Expected rank: `16`
- Graph boost applied: `True`
- Graph boosted count: `49`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/23` | 0.857823 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/54` | 0.857823 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/59` | 0.857823 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/64` | 0.857823 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/18` | 0.857823 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/44` | 0.857823 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/39` | 0.857823 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/49` | 0.857823 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/30` | 0.857823 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/35` | 0.857823 | **ARCHETYPE** |

### Query 26
- Text: Lookup values for Type of CoverBonusCan HideLesser+1 to ACNoStandard+2 to AC, Reflex,
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/10/Table/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `24`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/10/Table/10` | 0.915374 | Type of CoverBonusCan HideLesser+1 to ACNoStandard+2 to AC, Reflex, StealthYesGreater+4 to AC, Reflex, StealthYes |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/10/TableCell/309` | 0.707232 | +2 to AC, Reflex, Stealth |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/10/TableCell/312` | 0.691309 | +4 to AC, Reflex, Stealth |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/10/Text/9` | 0.671752 | When you're behind an obstacle that could block weapons,  guard you against explosions, and make you harder to detect,  you're behind cover. Standard cover gives you a +2 circumstance  bonus to AC, to |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/23` | 0.623351 | You press yourself against a wall or duck behind an obstacle  to take better advantage of cover (page 416). If you would  have standard cover, you instead gain greater cover, which  provides a +4 circ |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/10/TableCell/306` | 0.608668 | +1 to AC |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/10/TableCell/302` | 0.569207 | Type of Cover |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/10/TableCell/304` | 0.549636 | Can Hide |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/34` | 0.531250 | You gain a +1 circumstance bonus to Deception, Diplomacy,  Intimidation, and Perception checks against or in relation to  your asset, and a +1 circumstance bonus to attempts to Recall  Knowledge about |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/22` | 0.526937 | **Requirements** You are benefiting from cover, are near a  feature that allows you to take cover, or are prone. |

### Query 27
- Text: What are the requirements for **Prerequisites** Basic Mystic Spellcasting; master in  connection skill?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/46']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `39`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/46` | 0.904699 | **Prerequisites** Basic Mystic Spellcasting; master in  connection skill |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/51` | 0.865235 | **Prerequisites** Expert Mystic Spellcasting; legendary in  connection skill |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41` | 0.772527 | **Prerequisites** Basic Mystic Spellcasting |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/44` | 0.699327 | **Prerequisites** Basic Witchwarper Spellcasting; master in Arcana  or Occultism, depending on paradox |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/39` | 0.695288 | **Prerequisites** Basic Witchwarper Spellcasting |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25` | 0.678131 | **Prerequisites** Mystic Dedication |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20` | 0.678131 | **Prerequisites** Mystic Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/15` | 0.678131 | **Prerequisites** Mystic Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/36` | 0.678131 | **Prerequisites** Mystic Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/30` | 0.651693 | **Prerequisites** Basic Mysticism |

### Query 28
- Text: What is the rule about MULTICLASS MYSTIC  CHARACTERS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/3` | 0.785017 | MULTICLASS MYSTIC  CHARACTERS |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/3` | 0.661030 | MULTICLASS ENVOY  CHARACTERS |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/3` | 0.651632 | MULTICLASS SOLDIER  CHARACTERS |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/3` | 0.638427 | MULTICLASS WITCHWARPER  CHARACTERS |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/3` | 0.626006 | MULTICLASS OPERATIVE  CHARACTERS |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/3` | 0.614906 | MULTICLASS SOLARIAN  CHARACTERS |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/1` | 0.561708 | MYSTIC |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 0.552271 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.546165 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/51` | 0.534090 | **Prerequisites** Expert Mystic Spellcasting; legendary in  connection skill |

### Query 29
- Text: What is the rule about You gain your connection's initial epiphany spell. If  you don't already have one, you also gain a focus  pool of 1 Focus Point, which you can Refocus by  reflecting on your connection.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `17`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/37` | 0.906821 | You gain your connection's initial epiphany spell. If  you don't already have one, you also gain a focus  pool of 1 Focus Point, which you can Refocus by  reflecting on your connection. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/25` | 0.737738 | You gain your paradox's initial warp spell. If you don't already  have one, you also gain a focus pool of 1 Focus Point, which you  can Refocus by contemplating infinite worlds. (For more on warp  spe |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/26` | 0.625424 | You gain a 1st- or 2nd-level mystic feat. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.603684 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/9` | 0.592813 | Choose a connection (see page 119). You become trained in  the connection's skill or, if you were already trained, you  become trained in a skill of your choice. You don't gain any  other abilities fr |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/2` | 0.590903 | You're compelled to focus your attention on something,  distracting you from whatever else is going on around you. You  take a –2 status penalty to Perception and skill checks, and you  can't use conc |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/1` | 0.588425 | your reaction, you lose it at the start of your next turn, though  you typically then gain a reaction at the start of that turn. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/20` | 0.586447 | You gain a 1st- or 2nd-level solarian feat. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/51` | 0.580652 | You gain a 1st- or 2nd-level operative feat. |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/4/ListItem/9` | 0.578966 | Do anything else that's specified to happen at the start of  your turn, such as regaining Hit Points from fast healing  or regeneration. |

### Query 30
- Text: What is the rule about Unlike a check, where the result is compared to a DC, the  results of initiative rolls are ranked. This ranking sets the  order in which the encounter's participants act—the initiative  order. The character with the highest result goes first. The  second highest follows, and so on until whoever had the  lowest result takes their turn last.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/9` | 0.983702 | Unlike a check, where the result is compared to a DC, the  results of initiative rolls are ranked. This ranking sets the  order in which the encounter's participants act—the initiative  order. The cha |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/6` | 0.763409 | When the GM calls for it, you'll roll initiative to determine  your place in the initiative order, which is the sequence in  which the encounter's participants will take their turns.  Rolling initiati |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/13` | 0.754684 | A round begins when the participant with the highest  initiative roll result starts their turn, and it ends when the  one with the lowest initiative ends their turn. The process  of taking a turn is d |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/10` | 0.751714 | If your result is tied with an enemy's result, the enemy  goes first. If your result is tied with another PC's, you can  decide between yourselves who goes first when you reach  that place in the init |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/4` | 0.738052 | An encounter is played out in a series of rounds, during which  the player characters, adversaries, and other participants in the  encounter act in sequence. You roll initiative to determine this  ord |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/15` | 0.720292 | Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/2` | 0.707161 | The GM keeps track of the initiative order for an  encounter. It's usually okay for the players to know  this order since they'll see who goes when and be  aware of one another's results. However, the |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/8` | 0.693471 | The GM rolls initiative for anyone other than the player  characters in the encounter. If these include a number of  identical creatures, the GM could roll once for the group as a  whole and have them |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/11` | 0.688916 | initiative order usually don't change during the encounter.  (But see the Delay basic action on page 408.) |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/18` | 0.663118 | Once you've done all the things you want to do with the actions  you have available, you reach the end of your turn. Take the  following steps in any order you choose. Play then proceeds to  the next |

### Query 31
- Text: What are the requirements for **ACQUIRE ASSET **[one-action] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/5` | 0.863050 | **ACQUIRE ASSET **[one-action] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.692654 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/542` | 0.692035 | Acquire Asset |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.660106 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/4/SectionHeader/12` | 0.658841 | STEP 2: ACT |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12` | 0.654745 | **GET 'EM! **[one-action]** TO **[two-actions] |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.643501 | **READY ARMS! **[one-action]** TO **[two-actions] |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.641497 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/13` | 0.640291 | **DON'T YOU DIE ON ME **[one-action] **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/35` | 0.627742 | You gain the benefits of the 2-action Get 'Em! when using  1-action Get 'Em! on an asset. |

### Query 32
- Text: Summarize PLAYING THE CLASS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `17`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/11` | 0.893376 | PLAYING THE CLASS |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/31` | 0.754143 | PLAYING THE GAME |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/1` | 0.700688 | CHAPTER 3: CLASSES |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/26` | 0.684133 | CLASSES |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/34` | 0.681442 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/45` | 0.681442 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/51` | 0.681442 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/61` | 0.681442 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/39` | 0.681442 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/42` | 0.681442 | **PLAYING THE ** **GAME** |

### Query 33
- Text: What are the requirements for **HANG IN THERE **[one-action] **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `16`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/5` | 0.847071 | **HANG IN THERE **[one-action] **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/14` | 0.685204 | **HURRY **[one-action] **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.644473 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/578` | 0.628143 | Hang in There |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/4/SectionHeader/3` | 0.621059 | **STAND **[one-action] |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.604086 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.598469 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/2` | 0.592677 | **DISTANT FEINT** **FEAT 6** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/17` | 0.578146 | **ADVANCED GUNNER** **FEAT 6** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/40` | 0.575766 | 6TH LEVEL |

### Query 34
- Text: What are the requirements for **Prerequisites** Charisma +2?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `30`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/29` | 0.894442 | **Prerequisites** Charisma +2 |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/8` | 0.735194 | **Prerequisites** Wisdom +2 |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/13` | 0.692850 | **Prerequisites** Dexterity +2 |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/8` | 0.690768 | **Prerequisites** Intelligence +2 |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/12` | 0.660350 | **Prerequisites** Constitution +2 |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/6` | 0.625194 | At 1st level, your class gives you  an attribute boost to Charisma. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/13` | 0.598959 | **Prerequisites** Strength +2 You gain the stellar attunement class feature (page 140), but |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/10` | 0.587452 | **Critical Success** The target gains temporary Hit Points equal  to double their level plus your Charisma modifier. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/5` | 0.586883 | **Charisma** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/36` | 0.573767 | **Prerequisites** Mystic Dedication |

### Query 35
- Text: What is the rule about A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is trained in Perception, a saving throw,  or another statistic, they gain a proficiency bonus equal to  their level + 2, while if they have expert proficiency, they  gain a proficiency bonus equal to their level + 4. For more  about proficiency ranks, see page 24.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `35`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 0.992806 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.833143 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/8` | 0.802664 | If something isn't listed in your character's class entry,  their proficiency rank in that statistic is untrained unless  they gain training from another source. If your character  is untrained in som |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.771435 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/5` | 0.758535 | Thanks to your ally's assistance, you can add your level  as a proficiency bonus to the associated skill check, even if  you're untrained. Additionally, you gain a circumstance bonus  to your skill ch |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.747175 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/50` | 0.726080 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/3` | 0.712010 | You gain more skill increases than members of other classes.  At 2nd level and every level thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you' |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/25` | 0.708575 | You've learned a few tricks with your weapons. Your  proficiency ranks for simple weapons, martial weapons, and  unarmed attacks increase to expert. Whenever you attack  the target of your Get 'Em!, y |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.707534 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |

### Query 36
- Text: Summarize DIM LIGHT
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/11` | 0.878163 | DIM LIGHT |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/7` | 0.621595 | LIGHT |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/2` | 0.570575 | LOW-LIGHT VISION |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/8` | 0.564149 | There are three levels of light: bright light, dim light, and  darkness. The rules in this book assume that all creatures are  in bright light unless otherwise noted. A source of light lists  the radi |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/9` | 0.560878 | BRIGHT LIGHT |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/3` | 0.521055 | A creature with low-light vision can see in dim light as though  it were bright light, so it ignores the concealed condition due  to dim light. |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/13` | 0.509777 | DARKNESS |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/12` | 0.505606 | Areas in shadow or lit by weak light sources are in dim  light. Creatures and objects in dim light have the concealed  condition, unless the seeker has darkvision or low-light vision  (page 425), or a |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/14` | 0.494869 | Chapter 4: Skills includes several downtime activities,  which are summarized here. |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/37` | 0.490636 | **Hit Points, ** **Healing, and ** **Dying** |

### Query 37
- Text: What is the rule about In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means sight. If you can't observe the creature,  it's either hidden, undetected, or unnoticed, and you'll need  to factor in the targeting restrictions. Even if a creature is  observed, it might still be concealed.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `34`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.983211 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.822142 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/20` | 0.810994 | Anything in plain view is observed by you. If a creature takes  measures to avoid detection, such as by using Stealth to Hide,  it can become hidden or undetected instead of observed. If you |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/9` | 0.800458 | Three conditions measure the degree to which you can sense  a creature: observed, hidden, and undetected. However, the  concealed and invisible conditions can partially mask a  creature, and the unnot |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` | 0.791737 | With the exception of invisible, these conditions are  relative to the viewer—it's possible for a creature to be  observed to you but hidden from your ally. Most of these  rules apply to objects as we |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.783683 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 0.778099 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.777650 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.777350 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/24` | 0.777056 | If a creature is undetected, you don't know what space it  occupies and you're off-guard to it. The Seek basic action can  help you find an undetected creature, usually making it hidden  from you inst |

### Query 38
- Text: What is the rule about There are four types of actions: single actions, activities,  reactions, and free actions.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `33`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/7` | 0.886302 | There are four types of actions: single actions, activities,  reactions, and free actions. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.690649 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.678127 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/3` | 0.660708 | Some actions, such as Step, specifically state  they don't trigger reactions or free actions based on  movement. |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/19` | 0.656937 | When it's your turn to act, you can use single actions ([one-action]),  short activities ([two-actions] and [three-actions]), reactions ([reaction]), and free actions  ([free-action]). When you're fin |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.645024 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.637473 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` | 0.636418 | Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action. |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/14` | 0.629261 | you from acting. If you can't act, you can't use any actions,  including reactions and free actions. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/20` | 0.624924 | An activity typically involves using multiple actions to create  an effect greater than you can produce with a single action,  or combining multiple single actions to produce an effect  that's differe |

### Query 39
- Text: What are the requirements for **GUN EXPERT** **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `14`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/28` | 0.739406 | **GUN EXPERT** **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/17` | 0.607821 | **ADVANCED GUNNER** **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/21` | 0.569255 | **Prerequisites** Basic Gunner |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/32` | 0.561487 | Your proficiency ranks for simple and martial guns increase to  expert. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/47` | 0.559688 | **SOLAR MANIFESTATION EXPERT** **FEAT 12** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/2` | 0.553399 | You're a professional with crack aim and lethal instincts. |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/8` | 0.552015 | **Requirements** Your Speed is at least 10 feet. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/65` | 0.548605 | **Prerequisites** Operative Dedication, class granting no more Hit  Points per level than 6 + your Constitution |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/33` | 0.546540 | **MASTER SPY** **FEAT 12** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/43` | 0.545485 | **EXPERT MYSTIC SPELLCASTING** **FEAT 12** |

### Query 40
- Text: Summarize BRIGHT LIGHT
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/9` | 0.840980 | BRIGHT LIGHT |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/7` | 0.707671 | LIGHT |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/11` | 0.584940 | DIM LIGHT |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/18` | 0.507691 | HIT POINTS |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/58` | 0.494900 | **Hit Points, ** **Healing, and ** **Dying** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/37` | 0.494900 | **Hit Points, ** **Healing, and ** **Dying** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/46` | 0.494900 | **Hit Points, ** **Healing, and ** **Dying** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/39` | 0.494900 | **Hit Points, ** **Healing, and ** **Dying** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/41` | 0.494900 | **Hit Points, ** **Healing, and ** **Dying** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/13` | 0.493112 | DARKNESS |

### Query 41
- Text: Summarize The following clarifications might be relevant when  Aiding an ally.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `17`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/19` | 0.956344 | The following clarifications might be relevant when  Aiding an ally. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/9` | 0.717610 | **Requirements** The ally is willing to accept your aid, and you've  prepared to help (see below). |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/21` | 0.636146 | **Proximity:** You don't necessarily need to be next to  your ally to aid, though you must be in a reasonable  location to help them both when you set up and when  you take the reaction. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/10` | 0.632957 | You try to help your ally with a task. To use this reaction, you  must first prepare to help, usually by using an action during  your turn. You must explain to the GM exactly how you're trying  to hel |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.623410 | These rules clarify some of the specifics of using actions. |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/19` | 0.619844 | Some effects target or require an ally, or otherwise refer  to an ally. This must be someone on your side, often another  PC, but it might be a bystander you're trying to protect. You  don't count as |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/14/ListItem/7` | 0.609852 | The action to help might require a skill check or  another roll to determine its effectiveness. |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/13` | 0.596241 | **Success** You grant your ally a +1 circumstance bonus to the  triggering check. |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/6` | 0.591831 | The GM decides how your help works, using the  following examples as guidelines when there's not a  specific action that applies. |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/12/Text/2` | 0.591076 | Some conditions exist relative to one another or share  a similar theme. It can be useful to look at these  conditions together to understand how they interact. |

### Query 42
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/35']
- Expected found: `True`
- Expected rank: `23`
- Graph boost applied: `True`
- Graph boosted count: `49`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/23` | 0.857823 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/54` | 0.857823 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/59` | 0.857823 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/64` | 0.857823 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/18` | 0.857823 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/44` | 0.857823 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/39` | 0.857823 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/49` | 0.857823 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/30` | 0.857823 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/35` | 0.857823 | **ARCHETYPE** |

### Query 43
- Text: What is the rule about When the GM calls for it, you'll roll initiative to determine  your place in the initiative order, which is the sequence in  which the encounter's participants will take their turns.  Rolling initiative marks the start of an encounter. More often  than not, you'll roll initiative when you enter a battle.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/6` | 0.991672 | When the GM calls for it, you'll roll initiative to determine  your place in the initiative order, which is the sequence in  which the encounter's participants will take their turns.  Rolling initiati |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/9` | 0.784465 | Unlike a check, where the result is compared to a DC, the  results of initiative rolls are ranked. This ranking sets the  order in which the encounter's participants act—the initiative  order. The cha |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/4` | 0.780121 | An encounter is played out in a series of rounds, during which  the player characters, adversaries, and other participants in the  encounter act in sequence. You roll initiative to determine this  ord |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/8` | 0.772547 | The GM rolls initiative for anyone other than the player  characters in the encounter. If these include a number of  identical creatures, the GM could roll once for the group as a  whole and have them |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/2` | 0.771493 | The GM keeps track of the initiative order for an  encounter. It's usually okay for the players to know  this order since they'll see who goes when and be  aware of one another's results. However, the |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/15` | 0.763590 | Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/13` | 0.729649 | A round begins when the participant with the highest  initiative roll result starts their turn, and it ends when the  one with the lowest initiative ends their turn. The process  of taking a turn is d |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/10` | 0.718529 | If your result is tied with an enemy's result, the enemy  goes first. If your result is tied with another PC's, you can  decide between yourselves who goes first when you reach  that place in the init |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/7` | 0.712173 | Typically, you'll roll a Perception check to determine your  initiative—the more aware you are of your surroundings,  the more quickly you can respond. Sometimes, though, the  GM might call on you to |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/6` | 0.707732 | Perception is frequently used for rolling initiative in an  encounter, and for the Seek action. See page 396 for the  procedure for rolling a Perception check. |

### Query 44
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/18']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `9`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/38` | 0.776592 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/50` | 0.776592 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/68` | 0.776592 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/60` | 0.776592 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/44` | 0.776592 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/18` | 0.776592 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/41` | 0.776592 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/33` | 0.776592 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/33` | 0.756592 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/36` | 0.756592 | **SPELLS** |

### Query 45
- Text: Summarize **Effects**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/43']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `13`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/41` | 0.876705 | **Effects** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/50` | 0.876705 | **Effects** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/62` | 0.876705 | **Effects** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/43` | 0.876705 | **Effects** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/36` | 0.856705 | **Effects** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/44` | 0.856705 | **Effects** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/63` | 0.856705 | **Effects** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/29` | 0.856705 | **Effects** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/18` | 0.856705 | **Effects** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/39` | 0.856705 | **Effects** |

### Query 46
- Text: Summarize **CONCENTRATE** **SECRET**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `16`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/15` | 0.937915 | **CONCENTRATE** **SECRET** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/27` | 0.937915 | **CONCENTRATE** **SECRET** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/7` | 0.846715 | **CONCENTRATE** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/40` | 0.846715 | **CONCENTRATE** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/8` | 0.846715 | **CONCENTRATE** |
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
- Graph boosted count: `36`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.968194 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/10` | 0.811455 | from their class features; and more. Your character's class  entry also provides the information needed when they  gain levels, so it will be a vital reference throughout the  course of your campaign. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` | 0.795462 | This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chos |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.765384 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.747810 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.746668 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.734250 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 0.729846 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 0.728937 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 0.726566 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |

### Query 48
- Text: What are the requirements for **Prerequisites** Operative Dedication, expert in any kind of  weapon or unarmed attack?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `40`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/31` | 0.888760 | **Prerequisites** Operative Dedication, expert in any kind of  weapon or unarmed attack |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/50` | 0.794259 | **Prerequisites** Solarian Dedication, expert in any kind of  weapon or unarmed attack |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.776239 | **Prerequisites** Operative Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.776239 | **Prerequisites** Operative Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.776239 | **Prerequisites** Operative Dedication |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/36` | 0.753684 | **Prerequisites** Operative Dedication, expert in Perception |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/65` | 0.690926 | **Prerequisites** Operative Dedication, class granting no more Hit  Points per level than 6 + your Constitution |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/44` | 0.673647 | **Prerequisites** Soldier Dedication, expert in Fortitude saves. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/34` | 0.659138 | **Prerequisites** Soldier Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/18` | 0.659138 | **Prerequisites** Soldier Dedication |

### Query 49
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/17']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `17`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/59` | 0.885652 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/43` | 0.885652 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/37` | 0.885652 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/40` | 0.885652 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/49` | 0.885652 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/32` | 0.885652 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/17` | 0.885652 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/67` | 0.885652 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/35` | 0.865652 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/31` | 0.865652 | **EQUIPMENT** |

### Query 50
- Text: What is the rule about Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the cycle until the encounter ends.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `30`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/15` | 0.943099 | Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/4` | 0.771427 | An encounter is played out in a series of rounds, during which  the player characters, adversaries, and other participants in the  encounter act in sequence. You roll initiative to determine this  ord |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/13` | 0.765920 | A round begins when the participant with the highest  initiative roll result starts their turn, and it ends when the  one with the lowest initiative ends their turn. The process  of taking a turn is d |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/6` | 0.734557 | When the GM calls for it, you'll roll initiative to determine  your place in the initiative order, which is the sequence in  which the encounter's participants will take their turns.  Rolling initiati |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/9` | 0.717167 | Unlike a check, where the result is compared to a DC, the  results of initiative rolls are ranked. This ranking sets the  order in which the encounter's participants act—the initiative  order. The cha |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/18` | 0.710350 | Once you've done all the things you want to do with the actions  you have available, you reach the end of your turn. Take the  following steps in any order you choose. Play then proceeds to  the next |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/8` | 0.678745 | The GM rolls initiative for anyone other than the player  characters in the encounter. If these include a number of  identical creatures, the GM could roll once for the group as a  whole and have them |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/20` | 0.677250 | You wait for the right moment to act. The rest of your  turn doesn't happen yet. Instead, you're removed from the  initiative order. You can return to the initiative order as a free  action triggered |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/21` | 0.665843 | Many things happen automatically at the start of your turn it's a common point for tracking the passage of time for  effects that last multiple rounds. At the start of each of your  turns, take these |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/11` | 0.664798 | initiative order usually don't change during the encounter.  (But see the Delay basic action on page 408.) |

### Query 51
- Text: What is the rule about When every individual action counts, you enter the encounter mode of play. In this mode, time  is divided into rounds, each of which is 6 seconds of time in the game world. Every round, each  participant takes a turn in an established order. During your turn, you can use actions, and depending  on the details of the encounter, you might have the opportunity to use reactions and free actions on  your own turn and on others' turns.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/1` | 0.944380 | When every individual action counts, you enter the encounter mode of play. In this mode, time  is divided into rounds, each of which is 6 seconds of time in the game world. Every round, each  particip |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/4` | 0.768043 | An encounter is played out in a series of rounds, during which  the player characters, adversaries, and other participants in the  encounter act in sequence. You roll initiative to determine this  ord |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/24` | 0.721526 | Activities that take longer than a turn can't normally be  performed during an encounter. Spells with a casting time of  1 minute or more are a common example, as are several skill  actions. When you |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/6` | 0.718934 | You'll need to track your actions carefully in an encounter. At  the start of each turn you take in an encounter, you regain 3  actions and 1 reaction to spend that round. (Regaining your  actions is |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/6/Text/2` | 0.703346 | Your movement and position determine how you interact with the world. Moving in exploration and  downtime modes is relatively fluid. Movement in encounter mode follows additional rules explained in  T |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/15` | 0.702378 | Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/26` | 0.701386 | Your reactions let you respond immediately to what's  happening around you. The GM determines whether you can  use reactions before your first turn begins, depending on the  situation in which the enc |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/21` | 0.696818 | Many things happen automatically at the start of your turn it's a common point for tracking the passage of time for  effects that last multiple rounds. At the start of each of your  turns, take these |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.691549 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/2` | 0.677528 | You affect the world around you primarily by using actions, which produce effects. Actions are most  closely measured and restricted during the encounter mode of play, but even when it isn't important |

### Query 52
- Text: Summarize At 1st level, your class gives you  an attribute boost to Charisma.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `34`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/6` | 0.978617 | At 1st level, your class gives you  an attribute boost to Charisma. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/4` | 0.778848 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.763946 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.736554 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/15` | 0.724238 | **Lead by Example** If you used two actions, Strike the target.  You gain a status bonus to the damage roll equal to your  Charisma modifier. Regardless of whether the Strike hits, you  and your allie |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/1` | 0.723958 | designated target. Your ally gains a status bonus to damage  equal to your Charisma modifier. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/29` | 0.716335 | In addition to what you get from your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/7` | 0.714295 | At 1st level, you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start  of this class. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/11` | 0.709176 | **Success** The target gains temporary Hit Points equal to their  level plus your Charisma modifier. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/Table/2` | 0.705326 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat2Envoy feat, skill feat, skill increase3Adaptive talent, genera |

### Query 53
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/24']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `17`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/26` | 0.747771 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/50` | 0.747771 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/23` | 0.747771 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/5` | 0.747771 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/16` | 0.747771 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/37` | 0.747771 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/24` | 0.747771 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/30` | 0.747771 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/27` | 0.745791 | SKILLS |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/29` | 0.727771 | **SKILLS** |

### Query 54
- Text: Summarize The shirren mystic **Chk Chk** worships Zon-Shelyn, the god of creating art from suffering.  He enjoys creatively expressing himself by  writing poetry and dueling enemies with his painglaive.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `17`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/27` | 1.006880 | The shirren mystic **Chk Chk** worships Zon-Shelyn, the god of creating art from suffering.  He enjoys creatively expressing himself by  writing poetry and dueling enemies with his painglaive. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/44` | 0.549389 | **Zemir** the human witchwarper jumps between  realities and timelines, trusting his uncanny  luck and years of experience to keep him  anchored while searching for the loved ones he  lost years ago t |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/4` | 0.539846 | Mystics support allies and themselves with powerful magic. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/6` | 0.528410 | Mystic solarians can augment themselves with  powerful spells and heal themselves while confronting  power enemies on the frontline. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/24` | 0.521466 | The mystic is a spellcaster with a connection  to a divine, occult, or primal aspect of the universe. A  mystic casts powerful spells, learning new epiphanies  based on their chosen connection, and he |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/26` | 0.515916 | **Chk Chk** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/26` | 0.507540 | You gain a 1st- or 2nd-level mystic feat. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/23` | 0.506571 | **Trigger** A creature targets you with a melee attack. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/ListItem/6` | 0.505039 | Mystic soldiers with the elemental connection can make  different area weapons on the fly that deal different  types of damage. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/48` | 0.496128 | attacks while soaking attacks from enemies. |

### Query 55
- Text: Summarize LOW-LIGHT VISION
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `27`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/2` | 0.882474 | LOW-LIGHT VISION |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/7` | 0.640032 | LIGHT |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/11` | 0.621659 | DIM LIGHT |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/13/SectionHeader/83` | 0.605290 | LINE OF SIGHT |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/3` | 0.600799 | A creature with low-light vision can see in dim light as though  it were bright light, so it ignores the concealed condition due  to dim light. |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/1` | 0.598754 | PERCEPTION AND  DETECTION |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15` | 0.589512 | **DETECTING WITH OTHER SENSES** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/12` | 0.587601 | Areas in shadow or lit by weak light sources are in dim  light. Creatures and objects in dim light have the concealed  condition, unless the seeker has darkvision or low-light vision  (page 425), or a |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/7/SectionHeader/3` | 0.581898 | **AUDITORY** **CONCENTRATE** **EXPLORATION** **VISUAL** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/8` | 0.578129 | DETECTING CREATURES |

### Query 56
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/20']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `12`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/52` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/62` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/70` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/43` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/35` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/40` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/20` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/46` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/31` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/37` | 0.900802 | **CONDITIONS ** **APPENDIX** |

### Query 57
- Text: What are the requirements for **Prerequisites** Envoy Dedication?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/39']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `36`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/19` | 0.897387 | **Prerequisites** Envoy Dedication |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/24` | 0.897387 | **Prerequisites** Envoy Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/34` | 0.897387 | **Prerequisites** Envoy Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/39` | 0.897387 | **Prerequisites** Envoy Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/18` | 0.734548 | **Prerequisites** Soldier Dedication |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/39` | 0.734548 | **Prerequisites** Soldier Dedication |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/34` | 0.734548 | **Prerequisites** Soldier Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.715225 | **Prerequisites** Operative Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.715225 | **Prerequisites** Operative Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.715225 | **Prerequisites** Operative Dedication |

### Query 58
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `12`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/52` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/62` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/70` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/43` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/35` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/40` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/20` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/46` | 0.920802 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/31` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/37` | 0.900802 | **CONDITIONS ** **APPENDIX** |

### Query 59
- Text: Summarize In bright light, such as sunlight, creatures and objects can  be observed clearly by anyone with average vision or better.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `37`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/10` | 0.991085 | In bright light, such as sunlight, creatures and objects can  be observed clearly by anyone with average vision or better. |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/28` | 0.728188 | A creature with darkvision or greater darkvision can see  perfectly well in areas of darkness and dim light, though |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/3` | 0.723111 | A creature with low-light vision can see in dim light as though  it were bright light, so it ignores the concealed condition due  to dim light. |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/12` | 0.722801 | Areas in shadow or lit by weak light sources are in dim  light. Creatures and objects in dim light have the concealed  condition, unless the seeker has darkvision or low-light vision  (page 425), or a |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/14` | 0.706498 | A creature or object within darkness is hidden or undetected  unless the seeker has darkvision or a precise sense other  than vision. A creature without darkvision or another means  of perceiving in d |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.694316 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/18` | 0.687840 | Average vision is a precise sense—a sense that can be used to  perceive the world in nuanced detail. The only way to target |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/8` | 0.684396 | There are three levels of light: bright light, dim light, and  darkness. The rules in this book assume that all creatures are  in bright light unless otherwise noted. A source of light lists  the radi |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/20` | 0.681181 | Anything in plain view is observed by you. If a creature takes  measures to avoid detection, such as by using Stealth to Hide,  it can become hidden or undetected instead of observed. If you |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` | 0.665553 | With the exception of invisible, these conditions are  relative to the viewer—it's possible for a creature to be  observed to you but hidden from your ally. Most of these  rules apply to objects as we |

### Query 60
- Text: What is the rule about ACTIONS WITH TRIGGERS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `31`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/26` | 0.785806 | ACTIONS WITH TRIGGERS |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/29` | 0.699522 | LIMITATIONS ON TRIGGERS |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.613440 | These rules clarify some of the specifics of using actions. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.586045 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/10` | 0.583992 | **IN-DEPTH ACTION RULES** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/2` | 0.583581 | Some reactions and free actions are triggered by a  creature using an action with the move trait. The most  notable example is Reactive Strike (reproduced below).  Actions with the move trait can trig |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.574270 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` | 0.573340 | **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reac |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/1` | 0.571076 | ACTIONS |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` | 0.570367 | Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action. |

### Query 61
- Text: What is the rule about You're a professional with crack aim and lethal instincts.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `6`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/2` | 0.833331 | You're a professional with crack aim and lethal instincts. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/32` | 0.604344 | Your proficiency ranks for simple and martial guns increase to  expert. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/10` | 0.604229 | You lead your team by making an impression with firepower.  Your bombastic personality has a barrage of gunfire to back it  up, and you always shoot first. |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/21` | 0.568334 | You trust your instincts to see you through.  You gain master proficiency with the  triggering skill for the skill check. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/37` | 0.552112 | **Requirements** You're wielding a weapon with the automatic  trait. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/27` | 0.551202 | Your physique is incredibly hardy. Your proficiency rank for  Fortitude saves increases to expert. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/25` | 0.547414 | You've learned a few tricks with your weapons. Your  proficiency ranks for simple weapons, martial weapons, and  unarmed attacks increase to expert. Whenever you attack  the target of your Get 'Em!, y |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/51` | 0.544945 | Your proficiency ranks for solar flare and solar weapon  increase to expert. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/16` | 0.543898 | Whether by luck or instinct, you display impressive talent on  the fly. You gain the Improvised Mastery action. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/31` | 0.541548 | **Prerequisites** Operative Dedication, expert in any kind of  weapon or unarmed attack |

### Query 62
- Text: What are the requirements for **Prerequisites** trained in Deception or Diplomacy?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25` | 0.919447 | **Prerequisites** trained in Deception or Diplomacy |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/22` | 0.804922 | **Prerequisites** trained in Deception |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/23` | 0.804922 | **Prerequisites** trained in Deception |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/56` | 0.757855 | Trained in one of the following skills  of your choice: Deception, Diplomacy,  Intimidation |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/5` | 0.729953 | **Prerequisites** master in Deception |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.693755 | **Prerequisites** trained in Intimidation |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/8` | 0.679416 | **Prerequisites** expert in Diplomacy |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/12` | 0.626222 | **Trigger** You roll a skill check for any of the following skills  you're legendary in: Deception, Diplomacy, Intimidation, or  your leadership skill. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/30` | 0.613370 | You gain the envoy directives class feature (see page  104), but do not gain the Lead by Example benefits  of the Get 'Em! envoy directive. You become trained in  Deception, Diplomacy, or Intimidation |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/46` | 0.611225 | **Prerequisites** master in Intimidation |

### Query 63
- Text: What is the rule about **Master Spellcasting Feat:** Usually found at 18th level, these  feats make you a master in spell attack modifiers and spell  DCs and grant you a 7th-rank spell slot. If you have a spell  repertoire, you can select a third spell from your repertoire as  a signature spell. At 20th level, they grant you an 8th-rank  spell slot. Archetypes refer to these benefits as the "master  spellcasting benefits."?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/19` | 0.983368 | **Master Spellcasting Feat:** Usually found at 18th level, these  feats make you a master in spell attack modifiers and spell  DCs and grant you a 7th-rank spell slot. If you have a spell  repertoire, |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/18` | 0.866893 | **Expert Spellcasting Feat:** Typically taken at 12th level,  these feats make you an expert in spell attack modifiers  and spell DCs and grant you a 4th-rank spell slot. If you  have a spell repertoi |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/17` | 0.846958 | **Basic Spellcasting Feat:** Usually available at 4th level,  these feats grant a 1st-rank spell slot. At 6th level, they  grant you a 2nd-rank spell slot, and if you have a spell  repertoire, you can |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.702724 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/52` | 0.693310 | You gain the master spellcasting benefits (page 174). |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/50` | 0.693310 | You gain the master spellcasting benefits (page 174). |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.677079 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/29` | 0.668350 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the witchwarper  archetype, add a spell of the appropriate spell rank to your  repertoire: a co |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/4` | 0.664801 | At 7th level, you can use skill increases to become a master  in a skill in which you're already an expert, and at 15th level,  you can use them to become legendary in a skill in which  you're already |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/22` | 0.662557 | If your character is at least 7th level, they can use a  skill increase to become a master of a skill in which they're  already an expert. If they're at least 15th level, they can use  an increase to |

### Query 64
- Text: Summarize **Exploration ** **Mode**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `21`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/43` | 0.882946 | **Exploration ** **Mode** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/35` | 0.882946 | **Exploration ** **Mode** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/44` | 0.882946 | **Exploration ** **Mode** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/68` | 0.882946 | **Exploration ** **Mode** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/49` | 0.882946 | **Exploration ** **Mode** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/55` | 0.882946 | **Exploration ** **Mode** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/55` | 0.862946 | **Exploration ** **Mode** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/48` | 0.862946 | **Exploration ** **Mode** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/46` | 0.862946 | **Exploration ** **Mode** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/67` | 0.862946 | **Exploration ** **Mode** |

### Query 65
- Text: Summarize **Charisma**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `13`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/5` | 0.850012 | **Charisma** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/29` | 0.662268 | **Prerequisites** Charisma +2 |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/11` | 0.596498 | **Success** The target gains temporary Hit Points equal to their  level plus your Charisma modifier. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/66` | 0.594998 | **CHARACTER ** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/10` | 0.583203 | **Critical Success** The target gains temporary Hit Points equal  to double their level plus your Charisma modifier. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/4` | 0.579826 | **KEY ATTRIBUTE** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/4` | 0.577671 | **Attributes** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/9/SectionHeader/4` | 0.577506 | **DIRECTIVE** **ENVOY** **HEALING** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/8` | 0.574024 | **Leadership Style** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/55` | 0.571810 | **SKILLS** |

### Query 66
- Text: What is the rule about Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `32`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` | 0.886992 | Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.800046 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.791151 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.784627 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/2` | 0.701847 | Some reactions and free actions are triggered by a  creature using an action with the move trait. The most  notable example is Reactive Strike (reproduced below).  Actions with the move trait can trig |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.688444 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` | 0.678296 | **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reac |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/4/ListItem/7` | 0.678039 | You can use 1 free action or reaction with a trigger of  "Your turn begins" or something similar. |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/8` | 0.677185 | You prepare to use an action that will occur outside your  turn. Choose a single action or free action you can use, and  designate a trigger. Your turn then ends. If the trigger you  designated occurs |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/4/ListItem/21` | 0.672398 | You can use 1 free action or reaction with a trigger of  "Your turn ends" or something similar. |

### Query 67
- Text: What is the rule about Operative envoys become incredibly precise killing  machines that can combine Aim with abilities like Get  'em! and Distant Feint. Ghost operatives also appreciate  extra feats that use Deception.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `17`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/6` | 0.920059 | Operative envoys become incredibly precise killing  machines that can combine Aim with abilities like Get  'em! and Distant Feint. Ghost operatives also appreciate  extra feats that use Deception. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/ListItem/5` | 0.652256 | Envoy operatives direct allies while lining up perfect shots. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/8` | 0.646016 | Soldier envoys make natural commanders who can  use their defensive capabilities to keep the bonuses  of their directive's active against powerful enemies  while clearing out weaker foes with area fir |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/436` | 0.607178 | Envoy feat, skill feat, skill increase |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/416` | 0.607178 | Envoy feat, skill feat, skill increase |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/420` | 0.607178 | Envoy feat, skill feat, skill increase |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/444` | 0.607178 | Envoy feat, skill feat, skill increase |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/424` | 0.607178 | Envoy feat, skill feat, skill increase |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/432` | 0.607178 | Envoy feat, skill feat, skill increase |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/440` | 0.607178 | Envoy feat, skill feat, skill increase |

### Query 68
- Text: What is the rule about Class Feats?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/14` | 0.771346 | Class Feats |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.640952 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26` | 0.633435 | CLASS FEATURES |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11` | 0.633435 | CLASS FEATURES |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/408` | 0.615422 | Class Features |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/10/SectionHeader/3` | 0.613435 | CLASS FEATURES |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16` | 0.564520 | Skill Feats |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.557785 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/18` | 0.557776 | General Feats |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.557594 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |

### Query 69
- Text: What is the rule about Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidden condition instead of the observed condition.  It might be undetected by you if it's using Stealth or in an  environment that distorts the sense, such as a noisy room  in the case of hearing. In those cases, you have to use the  Seek basic action to detect the creature. At best, an imprecise  sense can be used to make an undetected creature (or one  you didn't even know was there) merely hidden—it can't make  the creature observed.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `38`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.997983 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.809289 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/21` | 0.793765 | A creature that's hidden is only barely perceptible. You only  know what space it occupies. Perhaps the creature just used  the Hide action. Your target might be behind some obstruction,  where you ca |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.793622 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/24` | 0.790442 | If a creature is undetected, you don't know what space it  occupies and you're off-guard to it. The Seek basic action can  help you find an undetected creature, usually making it hidden  from you inst |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 0.784841 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.781333 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.778624 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.767588 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/23` | 0.761635 | A character also has many vague senses—ones that can alert  you that something is there but aren't useful for zeroing in on  it to determine exactly what it is. The most useful of these  for a typical |

### Query 70
- Text: Summarize **Archetypes**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/52']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `44`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/38` | 0.888834 | **Archetypes** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/52` | 0.888834 | **Archetypes** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/46` | 0.888834 | **Archetypes** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/56` | 0.888834 | **Archetypes** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/41` | 0.868834 | **Archetypes** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/30` | 0.868834 | **Archetypes** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/47` | 0.868834 | **Archetypes** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/57` | 0.868834 | **Archetypes** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/65` | 0.868834 | **Archetypes** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/38` | 0.868834 | **Archetypes** |

### Query 71
- Text: Summarize **Mystic**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/47']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `18`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/41` | 0.823583 | **Mystic** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/47` | 0.823583 | **Mystic** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/51` | 0.823583 | **Mystic** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/25` | 0.803583 | **Mystic** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/35` | 0.803583 | **Mystic** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/30` | 0.803583 | **Mystic** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/60` | 0.803583 | **Mystic** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/52` | 0.803583 | **Mystic** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/42` | 0.803583 | **Mystic** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/1` | 0.711345 | MYSTIC |

### Query 72
- Text: What is the rule about attacks while soaking attacks from enemies.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/48']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/48` | 0.825277 | attacks while soaking attacks from enemies. |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/23` | 0.678846 | Use these rules for battles in water or underwater. |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/5/ListItem/26` | 0.641454 | You take a –2 circumstance penalty to your attack rolls for  bludgeoning or slashing attacks that pass through water. |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/8` | 0.589914 | **Lead by Example** If you used two actions, Hide or Sneak.  Until the start of your next turn, you can Strike the enemy  target as a reaction the first time the ally you targeted attacks  your design |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/20` | 0.576930 | You succinctly direct your allies to find cover by any means  necessary. You and all allies within 60 feet count any form of  lesser cover as standard cover until the start of your next turn. **Lead b |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/5/ListItem/27` | 0.576692 | Ranged attacks made by an underwater creature or against  an underwater target have their range increments halved. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/27` | 0.572861 | When you warn an ally of an attack, you follow up with a  shot at your enemy. The first time each round you use your  Watch Out reaction, you can make a melee or ranged Strike  against the triggering |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/29` | 0.570934 | **Trigger** A creature within 30 feet is damaged by an ally's Strike. You follow up on your ally's success by hurling a cunning, welltimed taunt at a foe they wounded. Attempt to Demoralize the  trigg |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/12` | 0.568296 | When the target you directed your allies to take down falls  unconscious or is destroyed, you quickly direct them at another  target. You use Get 'Em! against a new target following all the  normal ta |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/18` | 0.560817 | You follow-up your issued directive with an understood  order by attacking a notable foe. Make a Strike. If the Strike  hits, the target is affected by a 1-action Get 'Em. |

### Query 73
- Text: What are the requirements for **LEADER'S CONFIDENCE** **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/21` | 0.792437 | **LEADER'S CONFIDENCE** **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/9/SectionHeader/1` | 0.626829 | LEADER'S CONFIDENCE 7TH |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/25` | 0.618972 | You gain the leader's confidence class feature (see page  107). |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/13` | 0.594842 | 12TH LEVEL |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/28` | 0.587414 | **GUN EXPERT** **FEAT 12** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/13` | 0.583650 | **Prerequisites** Basic Leadership |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/27` | 0.579599 | **TRUE LEADER** **FEAT 20** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/31` | 0.579492 | **BASIC LEADERSHIP** **FEAT 4** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/10` | 0.572581 | **ADVANCED LEADERSHIP** **FEAT 6** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/28` | 0.564815 | **UNSTOPPABLE DIRECTIVES** **FEAT 12** |

### Query 74
- Text: Summarize **Perception and ** **Detection**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/53']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `25`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/41` | 0.919207 | **Perception and ** **Detection** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/53` | 0.919207 | **Perception and ** **Detection** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/66` | 0.919207 | **Perception and ** **Detection** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/33` | 0.919207 | **Perception and ** **Detection** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/48` | 0.899207 | **Perception and ** **Detection** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/44` | 0.899207 | **Perception and ** **Detection** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/65` | 0.899207 | **Perception and ** **Detection** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/46` | 0.899207 | **Perception and ** **Detection** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/39` | 0.857320 | **Perception and ** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/50` | 0.857320 | **Perception and ** |

### Query 75
- Text: What are the requirements for **EXPANDED CONNECTION** **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/38']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `11`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/38` | 0.822482 | **EXPANDED CONNECTION** **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/16` | 0.636889 | **REALLY GET EM!** **FEAT 8** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/24` | 0.632432 | **OPERATIVE EXPLOIT** **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/36` | 0.631568 | **QUANTUM BREADTH** **FEAT 8** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/19` | 0.623181 | **STARFINDER PROVISIONS** **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/10` | 0.601565 | ADDITIONAL FEATS |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/566` | 0.600673 | Extend Directive |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/25` | 0.598408 | **VETERAN TRAP FINDER** **FEAT 8** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/17` | 0.590066 | 8TH LEVEL |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/31` | 0.587276 | **ADVANCED STELLAR ATTUNEMENT** **FEAT 6** |

### Query 76
- Text: What is the rule about Various abilities and conditions, such as a Reactive Strike,  can disrupt an action. When an action is disrupted, you still  use the actions or reactions you committed, and you still  expend any costs, but the action's effects don't occur. In the?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `34`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/9` | 0.931586 | Various abilities and conditions, such as a Reactive Strike,  can disrupt an action. When an action is disrupted, you still  use the actions or reactions you committed, and you still  expend any costs |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` | 0.694708 | Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or S |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.688386 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/25` | 0.683280 | If an activity outside of an encounter is interrupted or  disrupted, as described in Disrupting Actions on page 407,  you usually lose the time you put in, but no additional time. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/7` | 0.681432 | Some effects are even more restrictive. Certain abilities,  instead of or in addition to changing the number of actions  you can use, say specifically that you can't use reactions.  The most restricti |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.681060 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/18` | 0.670102 | case of an activity, you usually lose all actions spent for the  activity up through the end of that turn. For instance, if you  began to Cast a Spell requiring 3 actions and the first action  was dis |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/16` | 0.658959 | An action might allow you to use a simpler action usually one of the Basic Actions on page 408—in a  different circumstance or with different effects. This  subordinate action still has its normal tra |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/2` | 0.655362 | Some reactions and free actions are triggered by a  creature using an action with the move trait. The most  notable example is Reactive Strike (reproduced below).  Actions with the move trait can trig |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` | 0.654239 | Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action. |

### Query 77
- Text: What is the rule about You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its trigger is satisfied—and *only* when it's satisfied—you  can use the reaction or free action, though you don't have to  use the action if you don't want to.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `35`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.958700 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.825170 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.822617 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/14` | 0.811135 | Free actions with triggers and reactions work  differently. You can use these whenever the trigger  occurs, even if the trigger occurs in the middle of  another action. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` | 0.766852 | **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reac |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/8` | 0.757888 | You prepare to use an action that will occur outside your  turn. Choose a single action or free action you can use, and  designate a trigger. Your turn then ends. If the trigger you  designated occurs |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/2` | 0.742657 | Some reactions and free actions are triggered by a  creature using an action with the move trait. The most  notable example is Reactive Strike (reproduced below).  Actions with the move trait can trig |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/4/ListItem/21` | 0.714191 | You can use 1 free action or reaction with a trigger of  "Your turn ends" or something similar. |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/4/ListItem/7` | 0.709642 | You can use 1 free action or reaction with a trigger of  "Your turn begins" or something similar. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.708007 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |

### Query 78
- Text: What is the rule about You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by your connection, or any other cantrips of that  tradition you learn or discover. You're trained in the spell  attack modifier and spell DC statistics. Your key spellcasting  attribute for mystic archetype spells is Wisdom, and they are  mystic spells of your connection's tradition.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/10` | 0.965594 | You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by you |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/10` | 0.847623 | You cast spells like a witchwarper. You gain access to the Cast  a Spell activity. You gain a spell repertoire with two common  cantrips from the spell list associated with your paradox, from  the spe |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.785421 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.776380 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/29` | 0.705456 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the witchwarper  archetype, add a spell of the appropriate spell rank to your  repertoire: a co |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/42` | 0.677658 | Increase the number of spells in your repertoire and number  of spell slots you gain from mystic archetype feats by 1 for  each spell rank other than your two highest mystic spell slots. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/40` | 0.672322 | Your repertoire expands, and you can cast more spells of your  paradox's tradition each day. Increase the number of spells  in your repertoire and number of spell slots you gain from  witchwarper arch |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/9` | 0.670201 | Choose a connection (see page 119). You become trained in  the connection's skill or, if you were already trained, you  become trained in a skill of your choice. You don't gain any  other abilities fr |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/24` | 0.656907 | The mystic is a spellcaster with a connection  to a divine, occult, or primal aspect of the universe. A  mystic casts powerful spells, learning new epiphanies  based on their chosen connection, and he |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/15` | 0.656222 | Some archetypes grant you a substantial degree of  spellcasting, albeit delayed compared to a character from a  spellcasting class. The spellcasting ability from a spellcasting  archetype also allows |

### Query 79
- Text: What is the rule about For instance, this is the attribute modifier you'll use to  determine the Difficulty Class (DC) associated with your  character's class features and feats. This is called your  class DC. If your character is a member of a spellcasting  class, this key attribute is used to calculate spell DCs and  similar values.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/15` | 0.951421 | For instance, this is the attribute modifier you'll use to  determine the Difficulty Class (DC) associated with your  character's class features and feats. This is called your  class DC. If your chara |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/14` | 0.711741 | This is the attribute modifier that a member of your class  cares about the most. Many of your most useful and  powerful abilities are tied to this attribute in some way. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/15` | 0.706477 | When attempting a counteract check, add the relevant skill modifier or other appropriate modifier to your check against the target's DC. If you're counteracting an affliction, the DC is in the afflict |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 0.675735 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.674684 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.665862 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` | 0.660596 | This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chos |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/7` | 0.658979 | Spellcasting classes grant a proficiency rank for spell  attacks and DCs, which are further detailed in each class's  entry. These classes rarely use their class DC. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` | 0.658207 | Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  char |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/16` | 0.655026 | Most classes are associated with one key attribute  modifier, but some allow you to choose from two options.  For instance, if you're a witchwarper, you can choose  either Intelligence or Charisma as |

### Query 80
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/41']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `5`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/49` | 0.885652 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/60` | 0.885652 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/41` | 0.885652 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/55` | 0.885652 | **EQUIPMENT** |
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
- Graph boosted count: `39`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 0.959891 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.783950 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.782170 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.774382 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/27` | 0.768026 | You gain these abilities as an envoy. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.762039 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.757589 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.746032 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.742329 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/3` | 0.731700 | You gain more skill increases than members of other classes.  At 2nd level and every level thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you' |

### Query 82
- Text: What is the rule about Typically, the GM tracks how well creatures detect each  other since neither party has perfect information. For  example, you might think a creature is in the last place  you sensed it, but it was able to Sneak away. Or you  might think a creature can't see you in the dark, but it has  darkvision.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `35`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/11` | 0.983724 | Typically, the GM tracks how well creatures detect each  other since neither party has perfect information. For  example, you might think a creature is in the last place  you sensed it, but it was abl |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/17` | 0.768020 | The GM attempts a single secret Perception check for  you and compares the result to the Stealth DCs of any  undetected or hidden creatures in the area, or the DC to  detect each object in the area (a |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/14` | 0.738082 | A creature or object within darkness is hidden or undetected  unless the seeker has darkvision or a precise sense other  than vision. A creature without darkvision or another means  of perceiving in d |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/24` | 0.733204 | When one creature might detect another, the GM almost  always uses the most precise sense available. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/25` | 0.731550 | **Success** Any undetected creature you succeeded against  becomes hidden from you instead of undetected, and  any hidden creature you succeeded against becomes  observed by you. You learn the locatio |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/2` | 0.726528 | The GM keeps track of the initiative order for an  encounter. It's usually okay for the players to know  this order since they'll see who goes when and be  aware of one another's results. However, the |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/28` | 0.718621 | You try to tell whether a creature's behavior is abnormal.  Choose one creature and assess it for odd body language,  signs of nervousness, and other indicators that it might be  trying to deceive som |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` | 0.717712 | With the exception of invisible, these conditions are  relative to the viewer—it's possible for a creature to be  observed to you but hidden from your ally. Most of these  rules apply to objects as we |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.713396 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/16` | 0.686710 | Most abilities that designate "a creature you can see"  or the like function just as well if the user can precisely  sense the subject with a different sense. If a monster  uses a sense other than vis |

### Query 83
- Text: What is the rule about A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses other than sight ignore the invisible  condition. You can Seek (page 409) to attempt to figure out  an invisible creature's location, making it only hidden from  you. This lasts until the invisible creature successfully  uses Sneak to become undetected again. If you're already  observing a creature when it becomes invisible, it starts  out hidden since you know where it was, though it can  then Sneak to become undetected.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/2/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `36`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.984775 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/18` | 0.807367 | You can't be seen. You're undetected to everyone. Creatures  can Seek to detect you; if a creature succeeds at its Perception  check against your Stealth DC, you become hidden to that  creature until |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/24` | 0.800113 | If a creature is undetected, you don't know what space it  occupies and you're off-guard to it. The Seek basic action can  help you find an undetected creature, usually making it hidden  from you inst |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.789803 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/14` | 0.780019 | A creature or object within darkness is hidden or undetected  unless the seeker has darkvision or a precise sense other  than vision. A creature without darkvision or another means  of perceiving in d |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.774042 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/4` | 0.773433 | If you have no idea a creature is even present, that creature  is unnoticed by you. A creature that's undetected might also  be unnoticed. This condition usually matters for abilities  that can be use |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.769528 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/2` | 0.764806 | When you're undetected by a creature, that creature can't  see you at all, has no idea what space you occupy, and can't  target you, though you still can be affected by abilities that  target an area. |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/9` | 0.760968 | Three conditions measure the degree to which you can sense  a creature: observed, hidden, and undetected. However, the  concealed and invisible conditions can partially mask a  creature, and the unnot |

### Query 84
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/26']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `16`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/32` | 0.885652 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/7` | 0.885652 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/26` | 0.885652 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/29` | 0.880819 | **EQUIPMENT ** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/43` | 0.865652 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/59` | 0.865652 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/40` | 0.865652 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/32` | 0.865652 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/41` | 0.865652 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/31` | 0.865652 | **EQUIPMENT** |

### Query 85
- Text: What is the rule about If your result is tied with an enemy's result, the enemy  goes first. If your result is tied with another PC's, you can  decide between yourselves who goes first when you reach  that place in the initiative order. After that, your places in the?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `21`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/10` | 0.982222 | If your result is tied with an enemy's result, the enemy  goes first. If your result is tied with another PC's, you can  decide between yourselves who goes first when you reach  that place in the init |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/9` | 0.750798 | Unlike a check, where the result is compared to a DC, the  results of initiative rolls are ranked. This ranking sets the  order in which the encounter's participants act—the initiative  order. The cha |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/2` | 0.710813 | The GM keeps track of the initiative order for an  encounter. It's usually okay for the players to know  this order since they'll see who goes when and be  aware of one another's results. However, the |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/6` | 0.696282 | When the GM calls for it, you'll roll initiative to determine  your place in the initiative order, which is the sequence in  which the encounter's participants will take their turns.  Rolling initiati |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/4` | 0.669123 | An encounter is played out in a series of rounds, during which  the player characters, adversaries, and other participants in the  encounter act in sequence. You roll initiative to determine this  ord |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/18` | 0.667244 | Once you've done all the things you want to do with the actions  you have available, you reach the end of your turn. Take the  following steps in any order you choose. Play then proceeds to  the next |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/11` | 0.655013 | initiative order usually don't change during the encounter.  (But see the Delay basic action on page 408.) |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/19` | 0.640309 | Some effects target or require an ally, or otherwise refer  to an ally. This must be someone on your side, often another  PC, but it might be a bystander you're trying to protect. You  don't count as |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/15` | 0.638735 | Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/12` | 0.636454 | When the target you directed your allies to take down falls  unconscious or is destroyed, you quickly direct them at another  target. You use Get 'Em! against a new target following all the  normal ta |

### Query 86
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/33']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `18`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/37` | 0.908832 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/40` | 0.908832 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/33` | 0.908832 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/35` | 0.908832 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/30` | 0.908832 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/52` | 0.908832 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/57` | 0.888833 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/45` | 0.888833 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/42` | 0.888833 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/19` | 0.888833 | **PLAYING THE ** **GAME** |

### Query 87
- Text: What are the requirements for **CHEER UP **[one-action] **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18` | 0.854673 | **CHEER UP **[one-action] **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/37` | 0.648630 | **SIDESTEP **[reaction] **FEAT 8** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/546` | 0.645812 | Cheer Up |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/21` | 0.631424 | You encourage an adjacent ally to overcome their minor  ailments by patting them on the back, providing them useful  advice, or offering some form of comfort or inspiration. The  target reduces the va |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/16` | 0.629082 | **REALLY GET EM!** **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/14` | 0.618659 | **HURRY **[one-action] **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/4/SectionHeader/6` | 0.617950 | **STEP **[one-action] |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.614732 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.608820 | **READY ARMS! **[one-action]** TO **[two-actions] |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/30` | 0.608415 | **SWAP UPGRADES **[one-action] **FEAT 10** |

### Query 88
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/56']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `7`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/56` | 0.776592 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/50` | 0.776592 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/42` | 0.776592 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/61` | 0.776592 | **SPELLS** |
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
- Graph boosted count: `24`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/31` | 0.856660 | **Obozaya** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/43` | 0.622377 | **Operative ** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/61` | 0.622377 | **Operative ** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/53` | 0.622377 | **Operative ** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/31` | 0.622377 | **Operative ** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/36` | 0.622377 | **Operative ** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/26` | 0.622377 | **Operative ** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/34` | 0.622377 | **Operative ** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/52` | 0.602377 | **Operative ** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/42` | 0.602377 | **Operative ** |

### Query 90
- Text: Summarize **Critical Success** Any undetected or hidden creature you  critically succeeded against becomes observed by you.  You learn the location of objects in the area you critically  succeeded against.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `18`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/24` | 1.000049 | **Critical Success** Any undetected or hidden creature you  critically succeeded against becomes observed by you.  You learn the location of objects in the area you critically  succeeded against. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/25` | 0.865358 | **Success** Any undetected creature you succeeded against  becomes hidden from you instead of undetected, and  any hidden creature you succeeded against becomes  observed by you. You learn the locatio |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/29` | 0.758263 | **Critical Success** You determine the creature's true intentions  and get a solid idea of any mental magic affecting it. |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/20` | 0.746072 | Anything in plain view is observed by you. If a creature takes  measures to avoid detection, such as by using Stealth to Hide,  it can become hidden or undetected instead of observed. If you |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/13` | 0.723142 | You've become an expert at veiling your schemes. When a  creature rolls a critical success to Sense Motive against you,  or a skill check to Gather Information or Recall Knowledge  about your secrets, |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/37` | 0.721032 | It's nigh impossible for your enemies to unravel your schemes  or your long-term plans. When a creature rolls a critical success  or success on a Perception check to Sense Motive against you,  or on a |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.713525 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/24` | 0.709629 | If a creature is undetected, you don't know what space it  occupies and you're off-guard to it. The Seek basic action can  help you find an undetected creature, usually making it hidden  from you inst |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/30` | 0.708009 | You indicate a creature that you can see to one or more allies,  gesturing in a direction and describing the distance verbally.  That creature is hidden to your allies, rather than undetected  (page 4 |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/21` | 0.704683 | A creature that's hidden is only barely perceptible. You only  know what space it occupies. Perhaps the creature just used  the Hide action. Your target might be behind some obstruction,  where you ca |

### Query 91
- Text: Summarize **Zemir**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/42']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/42` | 0.836399 | **Zemir** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/1` | 0.537443 | **KEY TERMS** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7` | 0.532187 | **HIT POINTS** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/1` | 0.529224 | **AVERT GAZE **[one-action] |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/33` | 0.522097 | **Soldier** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/45` | 0.522097 | **Soldier** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/38` | 0.522097 | **Soldier** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/36` | 0.522097 | **Soldier** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/28` | 0.522097 | **Soldier** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/63` | 0.522097 | **Soldier** |

### Query 92
- Text: What is the rule about The mystic is a spellcaster with a connection  to a divine, occult, or primal aspect of the universe. A  mystic casts powerful spells, learning new epiphanies  based on their chosen connection, and heals allies  using a vitality network that acts as a floating pool of  Hit Points. Play the mystic if you want to be a powerful  spellcaster who also heals your allies through your  supernatural bonds while casting powerful spells.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `16`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/24` | 0.968564 | The mystic is a spellcaster with a connection  to a divine, occult, or primal aspect of the universe. A  mystic casts powerful spells, learning new epiphanies  based on their chosen connection, and he |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/10` | 0.714768 | You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by you |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 0.660125 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.652161 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/6` | 0.649473 | Mystic solarians can augment themselves with  powerful spells and heal themselves while confronting  power enemies on the frontline. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.637250 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/9` | 0.623847 | Choose a connection (see page 119). You become trained in  the connection's skill or, if you were already trained, you  become trained in a skill of your choice. You don't gain any  other abilities fr |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/2` | 0.623807 | You're a master influencer. You make your way in the universe with a charming smile, quick wit, and keen  sense of self-preservation. You're a leader who motivates your teammates, pushes them past the |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/4` | 0.619373 | Mystics support allies and themselves with powerful magic. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/5` | 0.608959 | Mystic envoys can choose between using their magic  or directives to empower their allies, widening the  breadth of options available to them. |

### Query 93
- Text: What is the rule about **Leveling Up **on page 29 tells you how to make your  character stronger when you get enough Experience  Points to reach a new level.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `38`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/6` | 0.904717 | **Leveling Up **on page 29 tells you how to make your  character stronger when you get enough Experience  Points to reach a new level. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 0.668703 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/24` | 0.643729 | At 5th level and every 5 levels thereafter, your character  boosts four different attribute modifiers. This is described  briefly in the class. For the full details on attribute  modifiers and applyin |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.639112 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.637340 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/8` | 0.634447 | As your envoy level increases, so does your ability to adapt  to new situations. At 9th level and 15th level, increase the  number of skill feats you gain this way by 1. You can use  feats that you te |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/9` | 0.633393 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.625860 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/1` | 0.624774 | rush into battle with weapons raised gain a higher number  of Hit Points each level, while characters who cast spells or  engage in trickery gain fewer. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/Table/2` | 0.621375 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat2Envoy feat, skill feat, skill increase3Adaptive talent, genera |

### Query 94
- Text: What are the requirements for **BASIC MYSTIC SPELLCASTING** **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `35`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/17` | 0.822640 | **BASIC MYSTIC SPELLCASTING** **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/26` | 0.711408 | **BASIC WITCHWARPER SPELLCASTING** **FEAT 4** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/22` | 0.693543 | **BASIC MYSTICISM** **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41` | 0.654279 | **Prerequisites** Basic Mystic Spellcasting |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/43` | 0.648887 | **EXPERT MYSTIC SPELLCASTING** **FEAT 12** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/51` | 0.644726 | **Prerequisites** Expert Mystic Spellcasting; legendary in  connection skill |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/46` | 0.639319 | **Prerequisites** Basic Mystic Spellcasting; master in  connection skill |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/21` | 0.634183 | **BASIC WARP SPELL** **FEAT 4** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/48` | 0.631964 | **MASTER MYSTIC SPELLCASTING** **FEAT 18** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/16` | 0.628870 | **BASIC STELLAR ATTUNEMENT** **FEAT 4** |

### Query 95
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/36']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `12`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/36` | 0.899439 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/71` | 0.899439 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/53` | 0.899439 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/47` | 0.899439 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/41` | 0.899439 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/44` | 0.899439 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/70` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/58` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/65` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/53` | 0.879439 | **GLOSSARY & ** **INDEX** |

### Query 96
- Text: Summarize **Downtime ** **Mode**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/49']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `21`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/56` | 0.905345 | **Downtime ** **Mode** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/47` | 0.905345 | **Downtime ** **Mode** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/51` | 0.905345 | **Downtime ** **Mode** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/68` | 0.905345 | **Downtime ** **Mode** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/49` | 0.905345 | **Downtime ** **Mode** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/45` | 0.885345 | **Downtime ** **Mode** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/36` | 0.885345 | **Downtime ** **Mode** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/50` | 0.885345 | **Downtime ** **Mode** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/69` | 0.885345 | **Downtime ** **Mode** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/44` | 0.885345 | **Downtime ** **Mode** |

### Query 97
- Text: What are the requirements for **Prerequisites** Mystic Dedication?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `43`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20` | 0.882366 | **Prerequisites** Mystic Dedication |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/15` | 0.882366 | **Prerequisites** Mystic Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25` | 0.882366 | **Prerequisites** Mystic Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/36` | 0.882366 | **Prerequisites** Mystic Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/39` | 0.719468 | **Prerequisites** Soldier Dedication |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/34` | 0.719468 | **Prerequisites** Soldier Dedication |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/18` | 0.719468 | **Prerequisites** Soldier Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/30` | 0.705533 | **Prerequisites** Basic Mysticism |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.699959 | **Prerequisites** Operative Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.699959 | **Prerequisites** Operative Dedication |

### Query 98
- Text: Summarize You channel a fundamental force of the universe.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `10`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/2` | 0.970736 | You channel a fundamental force of the universe. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/2` | 0.655276 | You step up and lead others to victory while manipulating  those who stand in your way. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/2` | 0.637403 | You are a solar knight attuned to the powerful forces  of gravity and light, manifesting the cosmic cycle into  armaments made of stellar energy. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/20` | 0.635699 | Your quantum field gains the effect of your chosen paradox. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/47` | 0.625577 | **Trigger** You roll initiative. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/2` | 0.623473 | You're a professional with crack aim and lethal instincts. |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/6/Text/27` | 0.605748 | You cast *detect magic* at regular intervals. You move at half |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/51` | 0.604270 | You gain a 1st- or 2nd-level operative feat. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/26` | 0.603689 | You gain a 1st- or 2nd-level mystic feat. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/3` | 0.595131 | You're a charming tech wiz, giving commands using a  datapad or telepathic communications. |

### Query 99
- Text: What is the rule about **IN-DEPTH ACTION RULES**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/10` | 0.890468 | **IN-DEPTH ACTION RULES** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.583508 | These rules clarify some of the specifics of using actions. |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/14/SectionHeader/1` | 0.544342 | **PERSISTENT DAMAGE RULES** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/12/SectionHeader/7` | 0.538351 | **DEATH AND DYING RULES** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/29` | 0.528060 | **Rules Overview** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/41` | 0.528060 | **Rules Overview** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/30` | 0.528060 | **Rules Overview** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/27` | 0.528060 | **Rules Overview** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/54` | 0.528060 | **Rules Overview** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/35` | 0.528060 | **Rules Overview** |

### Query 100
- Text: What is the rule about **Special** You can select this feat a second time as a 10th level  feat and a 16th level feat, increasing the number of skill  feats you gain using adaptive talent by 1.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/41` | 0.904874 | **Special** You can select this feat a second time as a 10th level  feat and a 16th level feat, increasing the number of skill  feats you gain using adaptive talent by 1. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/8` | 0.705764 | As your envoy level increases, so does your ability to adapt  to new situations. At 9th level and 15th level, increase the  number of skill feats you gain this way by 1. You can use  feats that you te |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.687668 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/40` | 0.676159 | You gain the adaptive talent class feature, but you do not  gain additional skill feats at higher levels. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.676073 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/23` | 0.675845 | **Special** You can select this feat more than once. Each time you  do, you gain another operative feat. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/32` | 0.672084 | **Special** You can select this feat more than once. Each time  you do, you gain another mystic feat. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/26` | 0.670623 | Your varied life experiences let you adapt to nearly any  situation. When you gain skill feats using adaptive talent,  you gain two additional skill feats. In addition, you can adapt  to the day's cha |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.659243 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/36` | 0.659018 | **Special** You can select this feat more than once. Each  time you do, you gain another solarian feat. |

### Query 101
- Text: Summarize PRECISE SENSES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `16`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17` | 0.889955 | PRECISE SENSES |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20` | 0.842158 | IMPRECISE SENSES |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/25` | 0.734469 | SPECIAL SENSES |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15` | 0.690288 | SENSES |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/22` | 0.664785 | VAGUE SENSES |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15` | 0.601453 | **DETECTING WITH OTHER SENSES** |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/18` | 0.588675 | Average vision is a precise sense—a sense that can be used to  perceive the world in nuanced detail. The only way to target |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/42` | 0.580747 | **CONCENTRATE** **ENVOY** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/27` | 0.578228 | **CONCENTRATE** **SECRET** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/15` | 0.578228 | **CONCENTRATE** **SECRET** |

### Query 102
- Text: Summarize **Failure** You detect what a deceptive creature wants you to  believe. If they're not being deceptive, you believe they're  behaving normally.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `18`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/31` | 0.989909 | **Failure** You detect what a deceptive creature wants you to  believe. If they're not being deceptive, you believe they're  behaving normally. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/32` | 0.749410 | **Critical Failure** You get a false sense of the creature's  intentions. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/30` | 0.742201 | **Success** You can tell whether the creature is behaving  normally, but you don't know its exact intentions or what  magic might be affecting it. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/29` | 0.726681 | **Critical Success** You determine the creature's true intentions  and get a solid idea of any mental magic affecting it. |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/17` | 0.712676 | **Critical** **Failure** A glitching object you tried to use doesn't  function, and you lose the actions you took to attempt to use  it. A glitching creature uses the same effect as a failure and  is |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/28` | 0.711374 | You try to tell whether a creature's behavior is abnormal.  Choose one creature and assess it for odd body language,  signs of nervousness, and other indicators that it might be  trying to deceive som |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/25` | 0.684279 | **Success** Any undetected creature you succeeded against  becomes hidden from you instead of undetected, and  any hidden creature you succeeded against becomes  observed by you. You learn the locatio |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 0.675934 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.675641 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/13` | 0.674407 | You've become an expert at veiling your schemes. When a  creature rolls a critical success to Sense Motive against you,  or a skill check to Gather Information or Recall Knowledge  about your secrets, |

### Query 103
- Text: What is the rule about **Expert Spellcasting Feat:** Typically taken at 12th level,  these feats make you an expert in spell attack modifiers  and spell DCs and grant you a 4th-rank spell slot. If you  have a spell repertoire, you can select a second spell from  your repertoire as a signature spell. At 14th level, they grant  you a 5th-rank spell slot, and at 16th level, they grant you a  6th-rank spell slot. Archetypes refer to these benefits as the  "expert spellcasting benefits."?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `21`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/18` | 0.988387 | **Expert Spellcasting Feat:** Typically taken at 12th level,  these feats make you an expert in spell attack modifiers  and spell DCs and grant you a 4th-rank spell slot. If you  have a spell repertoi |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/19` | 0.876246 | **Master Spellcasting Feat:** Usually found at 18th level, these  feats make you a master in spell attack modifiers and spell  DCs and grant you a 7th-rank spell slot. If you have a spell  repertoire, |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/17` | 0.862549 | **Basic Spellcasting Feat:** Usually available at 4th level,  these feats grant a 1st-rank spell slot. At 6th level, they  grant you a 2nd-rank spell slot, and if you have a spell  repertoire, you can |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.705527 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 0.696203 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/29` | 0.686128 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the witchwarper  archetype, add a spell of the appropriate spell rank to your  repertoire: a co |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.670227 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.670175 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/45` | 0.667653 | You gain the expert spellcasting benefits (page 174). |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/47` | 0.667653 | You gain the expert spellcasting benefits (page 174). |

### Query 104
- Text: What is the rule about Most abilities that designate "a creature you can see"  or the like function just as well if the user can precisely  sense the subject with a different sense. If a monster  uses a sense other than vision, the GM can adapt ways  of avoiding detection that work with the monster's  senses. For example, a creature that has echolocation  might use hearing as a primary sense. This could mean  its quarry is concealed in a noisy chamber, hidden in  a great enough din, or invisible under a *silence* spell.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `37`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/16` | 0.969516 | Most abilities that designate "a creature you can see"  or the like function just as well if the user can precisely  sense the subject with a different sense. If a monster  uses a sense other than vis |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.731468 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.729939 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` | 0.725734 | With the exception of invisible, these conditions are  relative to the viewer—it's possible for a creature to be  observed to you but hidden from your ally. Most of these  rules apply to objects as we |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/11` | 0.722664 | Typically, the GM tracks how well creatures detect each  other since neither party has perfect information. For  example, you might think a creature is in the last place  you sensed it, but it was abl |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.715481 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/23` | 0.707217 | A character also has many vague senses—ones that can alert  you that something is there but aren't useful for zeroing in on  it to determine exactly what it is. The most useful of these  for a typical |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 0.701999 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/14` | 0.699981 | A creature or object within darkness is hidden or undetected  unless the seeker has darkvision or a precise sense other  than vision. A creature without darkvision or another means  of perceiving in d |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/20` | 0.698620 | Anything in plain view is observed by you. If a creature takes  measures to avoid detection, such as by using Stealth to Hide,  it can become hidden or undetected instead of observed. If you |

### Query 105
- Text: What is the rule about • If you created an effect lasting for a certain number of  rounds, reduce the number of rounds remaining by 1. The  effect ends if the duration is reduced to 0. For example,  if you cast a spell that lasts 3 rounds on yourself during?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `24`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/22` | 0.981030 | • If you created an effect lasting for a certain number of  rounds, reduce the number of rounds remaining by 1. The  effect ends if the duration is reduced to 0. For example,  if you cast a spell that |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/4/ListItem/19` | 0.816777 | End any effects that last until the end of your turn. For  example, spells with a sustained duration end at the end of  your turn unless you used the Sustain a Spell action during  your turn to extend |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/8` | 0.777431 | For an effect that lasts a number of rounds, the remaining  duration decreases by 1 at the start of each turn of the  creature that created the effect. Detrimental effects often  last "until the end o |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/9` | 0.761981 | Instead of lasting a fixed number of rounds, a duration  might end only when certain conditions are met (or cease to  be true). If so, the effects last until those conditions are met. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/41` | 0.720124 | Choose one of your effects that has a sustained duration or  lists a special benefit when you Sustain it. Most such effects  come from spells or magic item activations. If the effect has a  sustained |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/6` | 0.714297 | your first turn of a fight, it would affect you during that  turn, decrease to 2 rounds of duration at the start of your  second turn, decrease to 1 round of duration at the start of  your third turn, |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/18` | 0.712662 | You can have a given condition only once at a time. If  an effect would impose a condition you already have,  you now have that condition for the longer of the two  durations. The shorter-duration con |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/22` | 0.710692 | Conditions with different values are considered  different conditions. If you're affected by a condition  with a value multiple times, you apply only the  highest value, although you might have to tra |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/7` | 0.707006 | Most effects are discrete, creating an instantaneous effect  when you let the GM know what actions you're going to use.  Firing a gun, moving to a new space, or taking something  out of your pack all |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/58` | 0.702559 | Some effects apply conditions to a creature or item. These change your state of being in some way. Conditions are  persistent, lasting until the stated duration ends, the condition is removed, or term |

### Query 106
- Text: Summarize SENSES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15` | 0.794995 | SENSES |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20` | 0.783015 | IMPRECISE SENSES |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/25` | 0.735453 | SPECIAL SENSES |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/22` | 0.722942 | VAGUE SENSES |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17` | 0.718170 | PRECISE SENSES |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15` | 0.634700 | **DETECTING WITH OTHER SENSES** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/51` | 0.624101 | **PERCEPTION** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/4` | 0.612929 | SCENT |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/8/SectionHeader/5` | 0.605260 | **REPEAT A SPELL** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/6` | 0.603633 | TREMORSENSE |

### Query 107
- Text: What are the requirements for **LOOK ALIVE** **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/31` | 0.764439 | **LOOK ALIVE** **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/16` | 0.612185 | **REALLY GET EM!** **FEAT 8** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/19` | 0.601989 | **STARFINDER PROVISIONS** **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/594` | 0.601105 | Look Alive |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/17` | 0.594298 | 8TH LEVEL |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18` | 0.585581 | **CHEER UP **[one-action] **FEAT 8** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/37` | 0.569894 | **SIDESTEP **[reaction] **FEAT 8** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/24` | 0.569829 | **OPERATIVE EXPLOIT** **FEAT 8** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34` | 0.563577 | **Prerequisites** Watch Out |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/26` | 0.563577 | **Prerequisites** Watch Out |

### Query 108
- Text: Summarize IMPRECISE SENSES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20` | 0.922717 | IMPRECISE SENSES |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17` | 0.754312 | PRECISE SENSES |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/25` | 0.677276 | SPECIAL SENSES |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/22` | 0.675747 | VAGUE SENSES |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15` | 0.674323 | SENSES |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/9/SectionHeader/20` | 0.650349 | INCLINES |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/51` | 0.602164 | **PERCEPTION** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/6` | 0.590368 | TREMORSENSE |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/16/SectionHeader/6` | 0.588883 | UNCONSCIOUS |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/11/SectionHeader/18` | 0.585961 | CONFUSED |

### Query 109
- Text: What is the rule about Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining their Hit Points, see page 21.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 0.981536 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` | 0.852649 | This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chos |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/24` | 0.722802 | At 5th level and every 5 levels thereafter, your character  boosts four different attribute modifiers. This is described  briefly in the class. For the full details on attribute  modifiers and applyin |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.717971 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/6` | 0.712299 | **Leveling Up **on page 29 tells you how to make your  character stronger when you get enough Experience  Points to reach a new level. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/9` | 0.699547 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/1` | 0.697783 | rush into battle with weapons raised gain a higher number  of Hit Points each level, while characters who cast spells or  engage in trickery gain fewer. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.686111 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.671260 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/5` | 0.670969 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |

### Query 110
- Text: What are the requirements for **Prerequisites** master in Medicine or Augmentation Specialist **Requirements** You have a medkit.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/7/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `7`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/11` | 0.920946 | **Prerequisites** master in Medicine or Augmentation Specialist **Requirements** You have a medkit. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/20` | 0.625777 | **Prerequisites** trained in Medicine |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/46` | 0.608699 | **Prerequisites** master in Intimidation |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/6/Text/17` | 0.598283 | **Requirements** You have environmental protection on your  armor or a field scientist's kit. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/5` | 0.589201 | **Prerequisites** master in Deception |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17` | 0.584842 | **Prerequisites** Size Up |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/7` | 0.584842 | **Prerequisites** Size Up |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/15` | 0.579510 | **Requirements** You have a repair kit and one free hand. |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/12` | 0.576089 | You safely implant or remove an augmentation on a willing  creature. This takes 1 hour per item level of the augmentation  if using a medkit or half the normal amount of time if you  have access to a |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/35` | 0.561878 | **Requirements** You are holding a repair kit, or you are wearing  it and have a hand free. |

### Query 111
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/29']
- Expected found: `True`
- Expected rank: `20`
- Graph boost applied: `True`
- Graph boosted count: `49`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/23` | 0.857823 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/54` | 0.857823 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/59` | 0.857823 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/64` | 0.857823 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/18` | 0.857823 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/44` | 0.857823 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/39` | 0.857823 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/49` | 0.857823 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/30` | 0.857823 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/35` | 0.857823 | **ARCHETYPE** |

### Query 112
- Text: What is the rule about Witchwarper envoys make powerful battlefield  controllers that help maximize a partys mobility while  inhibiting their foe's movement capabilities with area  spells and quantum field.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `18`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/9` | 0.915647 | Witchwarper envoys make powerful battlefield  controllers that help maximize a partys mobility while  inhibiting their foe's movement capabilities with area  spells and quantum field. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/ListItem/9` | 0.688325 | Witchwarper operatives combine operative mobility  feats with their quantum field to shake up enemy. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/8` | 0.647943 | Soldier envoys make natural commanders who can  use their defensive capabilities to keep the bonuses  of their directive's active against powerful enemies  while clearing out weaker foes with area fir |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/4` | 0.624706 | The witchwarper archetype allows you to cast reality warping  spells and manifest a quantum field. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/9` | 0.618851 | Witchwarper solarians can use gravity abilities to push  and pull enemies into their quantum auras. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/ListItem/5` | 0.615230 | Envoy soldiers are natural tacticians who use directives to  position enemies and allies to optimize their area attacks. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/ListItem/9` | 0.608020 | Witchwarper soldiers want to further  hamper their enemy's movements and  are excellent at using grenades. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/41` | 0.599899 | A witchwarper alters reality by drawing on the  infinite possibilities of other universes and timelines.  Every witchwarper is influenced by an event, and they  can harness paradoxical powers to creat |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/5` | 0.579345 | Envoy solarians can rush into close quarters to  properly assess an enemy's abilities and positioning  when determining what directives to use. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/4` | 0.577824 | The envoy is a plucky leader who supports their  allies with battlefield directives, social savviness, and  a suite of skills. Envoys call out directives to their  allies, granting powerful boons that |

### Query 113
- Text: Summarize **Perception and ** **Detection**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/46']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/46` | 0.919207 | **Perception and ** **Detection** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/48` | 0.919207 | **Perception and ** **Detection** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/65` | 0.919207 | **Perception and ** **Detection** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/44` | 0.919207 | **Perception and ** **Detection** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/41` | 0.899207 | **Perception and ** **Detection** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/66` | 0.899207 | **Perception and ** **Detection** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/33` | 0.899207 | **Perception and ** **Detection** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/53` | 0.899207 | **Perception and ** **Detection** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/39` | 0.837320 | **Perception and ** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/50` | 0.837320 | **Perception and ** |

### Query 114
- Text: What is the rule about You gain a 1st- or 2nd-level mystic feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `27`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/26` | 0.876935 | You gain a 1st- or 2nd-level mystic feat. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/51` | 0.767260 | You gain a 1st- or 2nd-level operative feat. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/19` | 0.764988 | You gain a 1st- or 2nd-level soldier feat. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/20` | 0.747827 | You gain a 1st- or 2nd-level solarian feat. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/31` | 0.739990 | You gain one mystic feat. For the purpose of meeting its  prerequisites, your mystic level is half your character level. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/35` | 0.710990 | You gain a 1st- or 2nd-level envoy feat of your choice. |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/15` | 0.700237 | Your disruptive powers grow. You gain a 1st- or 2nd-level  witchwarper feat. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.694439 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/32` | 0.675578 | **Special** You can select this feat more than once. Each time  you do, you gain another mystic feat. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/17` | 0.635594 | **Basic Spellcasting Feat:** Usually available at 4th level,  these feats grant a 1st-rank spell slot. At 6th level, they  grant you a 2nd-rank spell slot, and if you have a spell  repertoire, you can |

### Query 115
- Text: What is the rule about **Navasi**, the human envoy, is a former space  pirate with a heart of gold. She's got a witty  remark for every occasion and a bullet for  anyone who would hurt one of her friends.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `31`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/7` | 0.922835 | **Navasi**, the human envoy, is a former space  pirate with a heart of gold. She's got a witty  remark for every occasion and a bullet for  anyone who would hurt one of her friends. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/6` | 0.501372 | **Navasi** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/31` | 0.499895 | Your confidence is a battery that keeps your allies going.  When you use a directive that grants temporary Hit Points, |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/412` | 0.499147 | Envoy feat, skill feat, skill increase |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/420` | 0.499146 | Envoy feat, skill feat, skill increase |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/416` | 0.499146 | Envoy feat, skill feat, skill increase |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/444` | 0.499146 | Envoy feat, skill feat, skill increase |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/436` | 0.499146 | Envoy feat, skill feat, skill increase |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/432` | 0.499146 | Envoy feat, skill feat, skill increase |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/440` | 0.499146 | Envoy feat, skill feat, skill increase |

### Query 116
- Text: What is the rule about This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the same time, and it's unclear in what order  they happen, the GM determines the order based on the  narrative.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `27`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.983704 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.811695 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` | 0.738100 | **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reac |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/8` | 0.732466 | The GM rolls initiative for anyone other than the player  characters in the encounter. If these include a number of  identical creatures, the GM could roll once for the group as a  whole and have them |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/26` | 0.681410 | Your reactions let you respond immediately to what's  happening around you. The GM determines whether you can  use reactions before your first turn begins, depending on the  situation in which the enc |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/2` | 0.681259 | Some reactions and free actions are triggered by a  creature using an action with the move trait. The most  notable example is Reactive Strike (reproduced below).  Actions with the move trait can trig |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.675076 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.667570 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/14` | 0.665107 | The GM might allow Tiny creatures to flank other  Tiny creatures if they're all in the same square, but  this is best left for special circumstances and uses  the GM's best judgment. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/22` | 0.665104 | Usually the creature or effect forcing the movement  chooses the path the victim takes. If you're pushed or  pulled, you can usually be moved through hazardous  terrain, pushed out of an airlock, or t |

### Query 117
- Text: What is the rule about Most classes are associated with one key attribute  modifier, but some allow you to choose from two options.  For instance, if you're a witchwarper, you can choose  either Intelligence or Charisma as your key attribute.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/16` | 0.975925 | Most classes are associated with one key attribute  modifier, but some allow you to choose from two options.  For instance, if you're a witchwarper, you can choose  either Intelligence or Charisma as |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/18` | 0.729127 | You're an efficient multitasker, and you always have more  than one goal in mind or scheme on the go. You can maintain  twice your Charisma modifier of assets. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 0.679405 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/15` | 0.677922 | For instance, this is the attribute modifier you'll use to  determine the Difficulty Class (DC) associated with your  character's class features and feats. This is called your  class DC. If your chara |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.670830 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/5` | 0.669181 | Prioritize Charisma. Dexterity, Intelligence, and  Constitution round out your abilities and defenses. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/36` | 0.668959 | You can maintain a number of assets equal to your Charisma  modifier. If you Size Up other assets after that, your new asset  replaces a previous one. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/6` | 0.657855 | At 1st level, your class gives you  an attribute boost to Charisma. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/14` | 0.656109 | This is the attribute modifier that a member of your class  cares about the most. Many of your most useful and  powerful abilities are tied to this attribute in some way. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` | 0.639037 | Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  char |

### Query 118
- Text: What is the rule about STEP 1: ROLL INITIATIVE?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/5` | 0.862380 | STEP 1: ROLL INITIATIVE |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/20` | 0.657835 | STEP 1: START YOUR TURN |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/6` | 0.619147 | When the GM calls for it, you'll roll initiative to determine  your place in the initiative order, which is the sequence in  which the encounter's participants will take their turns.  Rolling initiati |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/9` | 0.616972 | Unlike a check, where the result is compared to a DC, the  results of initiative rolls are ranked. This ranking sets the  order in which the encounter's participants act—the initiative  order. The cha |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/12` | 0.607139 | STEP 2: PLAY A ROUND |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/15` | 0.604228 | Once everyone in the encounter has taken a turn, the round  is over and the next one begins. Don't roll initiative again; the  new round proceeds in the same order as the previous one,  repeating the |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/47` | 0.602932 | **Trigger** You roll initiative. |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/3/SectionHeader/14` | 0.593809 | STEP 3: BEGIN THE NEXT ROUND |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/38` | 0.590753 | **Trigger** You're about to roll initiative. |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/4/SectionHeader/12` | 0.589044 | STEP 2: ACT |

### Query 119
- Text: What is the rule about Ancestry Feats?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/25` | 0.715871 | Ancestry Feats |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/442` | 0.608075 | Ancestry feat, greater resolve, incredible senses, inscrutable, skill increase |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/26` | 0.583400 | This section serves as a reminder of the ancestry feats your  character gains at 5th, 9th, 13th, and 17th levels. Ancestry  feats are detailed in each ancestry entry in Chapter 2, which  begins on pag |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/434` | 0.580058 | Ancestry feat, light armor expertise, skill increase, tactician, weapon mastery |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/14` | 0.542413 | In addition to the initial ancestry feat you started with, you  gain an ancestry feat at 5th level and every 4 levels thereafter. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/18` | 0.541604 | General Feats |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/418` | 0.540804 | Ancestry feat, attribute boosts, improvised mastery, perception expertise, skill increase, weapon expertise |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16` | 0.532128 | Skill Feats |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/410` | 0.521677 | Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/12` | 0.516297 | FEATS THAT GRANT FEATS |

### Query 120
- Text: What are the requirements for **PARDON ME** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `11`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/21` | 0.805870 | **PARDON ME** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/30` | 0.633327 | **SIZE UP** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/600` | 0.629913 | Pardon Me |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/8` | 0.611763 | **Requirements** Your Speed is at least 10 feet. |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/17` | 0.595001 | **Requirements** You're prone, and your Speed is at least 10 feet. You move 5 feet by crawling and continue to stay prone. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.594608 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/16` | 0.589398 | 1ST LEVEL |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/13` | 0.587690 | **DON'T YOU DIE ON ME **[one-action] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17` | 0.584764 | **Prerequisites** Size Up |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/7` | 0.584764 | **Prerequisites** Size Up |

### Query 121
- Text: What is the rule about rush into battle with weapons raised gain a higher number  of Hit Points each level, while characters who cast spells or  engage in trickery gain fewer.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `27`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/1` | 0.909806 | rush into battle with weapons raised gain a higher number  of Hit Points each level, while characters who cast spells or  engage in trickery gain fewer. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 0.644123 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/9` | 0.613730 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/448` | 0.608719 | Attribute boosts, envoy feat, skill feat, skill increase |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/428` | 0.608719 | Attribute boosts, envoy feat, skill feat, skill increase |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/13` | 0.605107 | Ranged and thrown weapons have a **range increment**.  Attacks with such weapons work normally up to that range.  Attacks against targets beyond that range take a –2 penalty,  which worsens by 2 for e |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.604349 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` | 0.602789 | This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chos |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.599803 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/32` | 0.599604 | increase the temporary Hit Points by your level. When you  use a directive that doesn't grant temporary Hit Points, you  can grant one ally affected by that directive temporary Hit  Points equal to ha |

### Query 122
- Text: What is the rule about Some effects are even more restrictive. Certain abilities,  instead of or in addition to changing the number of actions  you can use, say specifically that you can't use reactions.  The most restrictive form of reducing actions is when an  effect states that you can't act: this means you can't use  any actions, or even speak. When you can't act, you still  regain your actions unless another effect (like the stunned  condition) prevents it.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/7` | 0.981502 | Some effects are even more restrictive. Certain abilities,  instead of or in addition to changing the number of actions  you can use, say specifically that you can't use reactions.  The most restricti |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/16` | 0.806518 | Some conditions prevent you from taking a certain  subset of actions, typically reactions. Other conditions  simply say you can't act. When you can't act, you're  unable to take any actions at all. Un |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/14` | 0.771786 | you from acting. If you can't act, you can't use any actions,  including reactions and free actions. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/6` | 0.720621 | Effects can change the number of actions you can use on  your turn, or whether you can use actions at all. The slowed  condition, for example, causes you to lose actions, while the  quickened conditio |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/9` | 0.702461 | Various abilities and conditions, such as a Reactive Strike,  can disrupt an action. When an action is disrupted, you still  use the actions or reactions you committed, and you still  expend any costs |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/11` | 0.678511 | • Regain your 3 actions and 1 reaction. If you haven't spent  your reaction from your last turn, you lose it—you can't  "save" actions or reactions from one turn to use during the  next turn. Some abi |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/22` | 0.669528 | You've become senseless. You can't act. Stunned usually  includes a value, which indicates how many total actions you  lose, possibly over multiple turns, from being stunned. Each  time you regain act |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/58` | 0.665627 | Some effects apply conditions to a creature or item. These change your state of being in some way. Conditions are  persistent, lasting until the stated duration ends, the condition is removed, or term |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/20` | 0.661571 | An activity typically involves using multiple actions to create  an effect greater than you can produce with a single action,  or combining multiple single actions to produce an effect  that's differe |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.660701 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |

### Query 123
- Text: What is the rule about **Archetypes** on page 174 gives you thematic options  that allow you to further customize your character's  abilities. Though these rules are not recommended for  beginners, the archetypes in this book allow you to  gain abilities from other classes starting at 2nd level.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/7` | 0.951019 | **Archetypes** on page 174 gives you thematic options  that allow you to further customize your character's  abilities. Though these rules are not recommended for  beginners, the archetypes in this bo |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.724529 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.716882 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/2` | 0.705266 | Archetypes allow you to further customize your character concepts by taking more than one class. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.683450 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` | 0.670868 | Some archetypes include a list of "Additional Feats" that  appear in other sources. The list includes each feat's level,  which might be different than normal when gained from the  archetype. You can |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/3` | 0.668029 | You gain more skill increases than members of other classes.  At 2nd level and every level thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you' |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/4` | 0.660238 | You gain an archetype by selecting archetype feats instead  of your normal feats. First, find the archetype that best  fits your character concept. Then select that archetype's  dedication feat, using |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.656129 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/Table/2` | 0.651152 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat2Envoy feat, skill feat, skill increase3Adaptive talent, genera |

### Query 124
- Text: What is the rule about **Special** You can select this feat more than once. Each time  you select it, you gain another envoy feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `17`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/15` | 0.893734 | **Special** You can select this feat more than once. Each time  you select it, you gain another envoy feat. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/30` | 0.772839 | **Special** You can select this feat more than once. Each time  you do, you gain another soldier feat. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/32` | 0.759433 | **Special** You can select this feat more than once. Each time  you do, you gain another mystic feat. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/23` | 0.759063 | **Special** You can select this feat more than once. Each time you  do, you gain another operative feat. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/35` | 0.747806 | You gain a 1st- or 2nd-level envoy feat of your choice. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/36` | 0.747210 | **Special** You can select this feat more than once. Each  time you do, you gain another solarian feat. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/15` | 0.740087 | At every level that you gain an envoy feat, you can select  one of the following feats. You must satisfy any prerequisites  before selecting the feat. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/35` | 0.737516 | **Special** You can select this feat more than once. Each time  you do, you gain another witchwarper feat. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/14` | 0.703029 | You gain one envoy feat. For the purpose of meeting its  prerequisites, your envoy level is equal to half your character  level. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/440` | 0.701789 | Envoy feat, skill feat, skill increase |

### Query 125
- Text: What is the rule about You gain the expert spellcasting benefits (page 174).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/Text/47']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `26`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/45` | 0.862040 | You gain the expert spellcasting benefits (page 174). |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/47` | 0.862040 | You gain the expert spellcasting benefits (page 174). |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/52` | 0.827606 | You gain the master spellcasting benefits (page 174). |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/50` | 0.827606 | You gain the master spellcasting benefits (page 174). |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/18` | 0.642190 | **Expert Spellcasting Feat:** Typically taken at 12th level,  these feats make you an expert in spell attack modifiers  and spell DCs and grant you a 4th-rank spell slot. If you  have a spell repertoi |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.635991 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/29` | 0.613374 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the witchwarper  archetype, add a spell of the appropriate spell rank to your  repertoire: a co |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/25` | 0.610027 | You gain the leader's confidence class feature (see page  107). |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/19` | 0.609474 | **Master Spellcasting Feat:** Usually found at 18th level, these  feats make you a master in spell attack modifiers and spell  DCs and grant you a 7th-rank spell slot. If you have a spell  repertoire, |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/40` | 0.609016 | You gain the primary target class feature (page 152). |

### Query 126
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/30']
- Expected found: `True`
- Expected rank: `9`
- Graph boost applied: `True`
- Graph boosted count: `49`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/23` | 0.857823 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/54` | 0.857823 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/59` | 0.857823 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/64` | 0.857823 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/18` | 0.857823 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/44` | 0.857823 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/39` | 0.857823 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/49` | 0.857823 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/30` | 0.857823 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/35` | 0.857823 | **ARCHETYPE** |

### Query 127
- Text: What are the requirements for **OPERATIVE EXPLOIT** **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/24` | 0.793778 | **OPERATIVE EXPLOIT** **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/19` | 0.629954 | **STARFINDER PROVISIONS** **FEAT 8** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/25` | 0.626305 | **VETERAN TRAP FINDER** **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/16` | 0.622520 | **REALLY GET EM!** **FEAT 8** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/38` | 0.608090 | **EXPANDED CONNECTION** **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/1` | 0.589903 | OPERATIVE |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/57` | 0.587484 | **SPECIALIZED OPERATIVE** **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/65` | 0.586244 | **Prerequisites** Operative Dedication, class granting no more Hit  Points per level than 6 + your Constitution |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/36` | 0.576699 | **QUANTUM BREADTH** **FEAT 8** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.566499 | **Prerequisites** Operative Dedication |

### Query 128
- Text: Summarize **ARCHETYPE** **DEDICATION** **MULTICLASS**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/7` | 0.925741 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/28` | 0.925741 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/7` | 0.925741 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/12` | 0.925741 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/12` | 0.925741 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/11` | 0.925741 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/5` | 0.925741 | **ARCHETYPE** **DEDICATION** **MULTICLASS** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/8` | 0.745892 | Multiclass Dedications |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/18` | 0.713249 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/38` | 0.713249 | **ARCHETYPE** |

### Query 129
- Text: What are the requirements for **Prerequisites** Influence?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/Text/58']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `18`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/58` | 0.844744 | **Prerequisites** Influence |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/592` | 0.671815 | Influence |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.650916 | **Prerequisites** trained in Intimidation |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/25` | 0.645731 | **Prerequisites** adaptive talent |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/26` | 0.635443 | **Prerequisites** Watch Out |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34` | 0.635443 | **Prerequisites** Watch Out |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/19` | 0.626610 | **Prerequisites **Improvised Mastery |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17` | 0.624213 | **Prerequisites** Size Up |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/7` | 0.624213 | **Prerequisites** Size Up |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/46` | 0.616920 | **Prerequisites** master in Intimidation |

### Query 130
- Text: Summarize YOU MIGHT...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `15`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/18` | 0.810459 | YOU MIGHT... |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/22` | 0.716164 | OTHERS PROBABLY... |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/16` | 0.640362 | IN DOWNTIME... |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/14` | 0.617732 | WHILE EXPLORING... |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/12` | 0.582992 | DURING SOCIAL ENCOUNTERS... |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10` | 0.573680 | DURING COMBAT ENCOUNTERS... |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/632` | 0.568312 | You Can Do It |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/ListItem/25` | 0.561284 | Assume you like being in charge. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49` | 0.545007 | **YOU CAN DO IT **[one-action] **FEAT 14** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/70` | 0.536411 | manage. |

### Query 131
- Text: What is the rule about **CHARACTER ** **SHEET**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/60']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `5`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/47` | 0.804532 | **CHARACTER ** **SHEET** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/60` | 0.804532 | **CHARACTER ** **SHEET** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/55` | 0.804532 | **CHARACTER ** **SHEET** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/48` | 0.784532 | **CHARACTER ** **SHEET** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/56` | 0.784532 | **CHARACTER ** **SHEET** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/22` | 0.784532 | **CHARACTER ** **SHEET** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/72` | 0.784532 | **CHARACTER ** **SHEET** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/35` | 0.735377 | **INDEX** **CHARACTER ** **SHEET** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/51` | 0.694344 | CHARACTER Sheet |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/66` | 0.672966 | **CHARACTER ** |

### Query 132
- Text: What are the requirements for **CONFOUNDING DISQUISITION **[two-actions] **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `21`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/22` | 0.843459 | **CONFOUNDING DISQUISITION **[two-actions] **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/19` | 0.635166 | **STARFINDER PROVISIONS** **FEAT 8** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/24` | 0.608095 | **OPERATIVE EXPLOIT** **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/5` | 0.602435 | **ACQUIRE ASSET **[one-action] **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/548` | 0.602435 | Confounding Disquisition |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/19` | 0.601870 | **SITUATIONAL AWARENESS **[two-actions] **FEAT 12** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.599833 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.591506 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22` | 0.588527 | **SEARCH HIGH AND LOW! **[one-action]** TO **[two-actions] **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/31` | 0.588315 | **DIGITAL ASSESSMENT! **[one-action]** TO **[two-actions] |

### Query 133
- Text: Summarize **Success** You get free and remove the grabbed, immobilized,  and restrained conditions imposed by your chosen  target.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/2/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/29` | 0.988550 | **Success** You get free and remove the grabbed, immobilized,  and restrained conditions imposed by your chosen  target. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/28` | 0.799109 | **Critical Success** You get free and remove the grabbed,  immobilized, and restrained conditions imposed by your  chosen target. You can then Stride up to 5 feet. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/22` | 0.681387 | **Requirements** You are benefiting from cover, are near a  feature that allows you to take cover, or are prone. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/12` | 0.666503 | You release something you're holding in your hand or hands.  This might mean dropping an item, removing one hand from  your weapon while continuing to hold it in another hand,  releasing a cable suspe |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/18` | 0.665497 | **Success** You make a damage roll according to the weapon or  unarmed attack and deal damage. |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/17` | 0.653558 | **Requirements** Your hands are not tied behind your back or  otherwise restrained. |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/33` | 0.652195 | **Requirements** You have at least one hand or leg (or suitable  appendage) free, and you're untethered. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/2` | 0.651602 | You step up and lead others to victory while manipulating  those who stand in your way. |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/103` | 0.648278 | **Suppressed: **You're in a dangerous situation that forces |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/5` | 0.647604 | You stand up from being prone. |

### Query 134
- Text: What is the rule about In some cases, rolling a Dexterity-based Stealth  skill check to Sneak doesn't make the most sense.  For example, a PC trying to avoid being detected by  a creature that senses heartbeats might meditate  to slow their heart rate, using Wisdom instead of  Dexterity for their Stealth check. When a creature  could detect you using multiple different senses, use  your lowest applicable attribute modifier.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `32`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/19` | 0.986823 | In some cases, rolling a Dexterity-based Stealth  skill check to Sneak doesn't make the most sense.  For example, a PC trying to avoid being detected by  a creature that senses heartbeats might medita |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/18` | 0.753271 | The Stealth skill is designed to use Hide for avoiding  visual detection and Avoid Notice and Sneak to avoid  being both seen and heard. For many special senses,  a player can describe how they're avo |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/6/Text/21` | 0.737723 | You attempt a Stealth check to avoid notice while traveling  at half speed. If you're Avoiding Notice at the start of an  encounter, you usually roll a Stealth check instead of a  Perception check bot |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/7` | 0.679053 | Typically, you'll roll a Perception check to determine your  initiative—the more aware you are of your surroundings,  the more quickly you can respond. Sometimes, though, the  GM might call on you to |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.661293 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/18` | 0.660635 | You can't be seen. You're undetected to everyone. Creatures  can Seek to detect you; if a creature succeeds at its Perception  check against your Stealth DC, you become hidden to that  creature until |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/11` | 0.658683 | Typically, the GM tracks how well creatures detect each  other since neither party has perfect information. For  example, you might think a creature is in the last place  you sensed it, but it was abl |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/16/Text/15` | 0.652981 | noise), waking up if you succeed. If  creatures are attempting to stay quiet  around you, this Perception check uses  their Stealth DCs. Some effects make you sleep  so deeply that they don't allow yo |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/28` | 0.651504 | You try to tell whether a creature's behavior is abnormal.  Choose one creature and assess it for odd body language,  signs of nervousness, and other indicators that it might be  trying to deceive som |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.651452 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |

### Query 135
- Text: What is the rule about When it's your turn to act, you can use single actions ([one-action]),  short activities ([two-actions] and [three-actions]), reactions ([reaction]), and free actions  ([free-action]). When you're finished, your turn ends and the character  next in the initiative order begins their turn. Sometimes it's  important to note when during your turn something happens,  so a turn is divided into three steps.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/3/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `21`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/19` | 0.965126 | When it's your turn to act, you can use single actions ([one-action]),  short activities ([two-actions] and [three-actions]), reactions ([reaction]), and free actions  ([free-action]). When you're fin |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/13` | 0.797453 | You can use actions in any order you wish during your  turn, but you have to complete one action or activity before  beginning another; for example, you can't use a single action in  the middle of per |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.781832 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/4/ListItem/7` | 0.762131 | You can use 1 free action or reaction with a trigger of  "Your turn begins" or something similar. |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/4/ListItem/21` | 0.757692 | You can use 1 free action or reaction with a trigger of  "Your turn ends" or something similar. |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/8` | 0.753419 | You prepare to use an action that will occur outside your  turn. Choose a single action or free action you can use, and  designate a trigger. Your turn then ends. If the trigger you  designated occurs |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.752569 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/15` | 0.744127 | If you begin a 2-action or 3-action activity on your turn,  you must be able to complete it on your turn. You can't, for  example, begin to High Jump using your final action on one  turn and then comp |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.740756 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/16` | 0.738253 | Once you've spent all three of your actions, your turn ends  (as described in Step 3) and the next creature's turn begins. You  can choose to end your turn early, losing all remaining actions  (but no |

### Query 136
- Text: Summarize **Operative **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/26']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `8`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/34` | 0.858875 | **Operative ** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/53` | 0.858875 | **Operative ** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/26` | 0.858875 | **Operative ** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/31` | 0.858875 | **Operative ** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/36` | 0.858875 | **Operative ** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/43` | 0.858875 | **Operative ** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/61` | 0.858875 | **Operative ** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/52` | 0.838875 | **Operative ** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/48` | 0.838875 | **Operative ** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/42` | 0.838875 | **Operative ** |

### Query 137
- Text: What is the rule about For instance, suppose an enemy witchwarper cast  *invisibility* and then Sneaked away. You suspect that with  the witchwarper's Speed of 25 feet, they probably moved 15  feet toward an open door. You move up and attack a space 15  feet from where the witchwarper started and directly on the  path to the door. The GM secretly rolls an attack roll and flat  check, but they know that you weren't quite correct—your foe  was actually in the adjacent space! The GM tells you that you  missed, so you decide to make your next attack on the adjacent  space, just in case. This time, it's the right space, and the GM's  secret attack roll and flat check both succeed, so you hit!?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/2/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `18`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/2` | 0.960418 | For instance, suppose an enemy witchwarper cast  *invisibility* and then Sneaked away. You suspect that with  the witchwarper's Speed of 25 feet, they probably moved 15  feet toward an open door. You |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/1` | 0.696764 | Targeting an undetected creature is difficult. If you suspect  there's a creature around, you can pick a square and attempt  an attack. This works like targeting a hidden creature, but the  flat check |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/3` | 0.686782 | A creature you're undetected by can guess which square  you're in to try targeting you. It must pick a square and  attempt an attack. This works like targeting a hidden  creature (requiring a DC 11 fl |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/8/Text/13` | 0.651733 | You Seek meticulously for hidden doors, concealed hazards,  and so on. You can usually make an educated guess as to which  locations are best to check and move at half speed, but if you  want to be th |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/10/Text/16` | 0.640912 | Your GM might allow you to overcome your target's cover  in some situations. If you're right next to a narrow window,  you can shoot without penalty, but you have greater cover  against someone shooti |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/16` | 0.636402 | You scan an area for signs of creatures or objects, possibly  including secret doors or hazards. Choose an area to scan.  The GM determines the area you can scan with one Seek  action—almost always 30 |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.630796 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/6/Text/21` | 0.628985 | You attempt a Stealth check to avoid notice while traveling  at half speed. If you're Avoiding Notice at the start of an  encounter, you usually roll a Stealth check instead of a  Perception check bot |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/10` | 0.626093 | Attackers can target either you or your mount. An area effect  affects both of you as long as you're both in the area. You're  in an attacker's reach or range if any square of your mount is  within re |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/22` | 0.624013 | When targeting a hidden creature, before you roll to  determine your effect, you must attempt a DC 11 flat check.  If you fail, you don't affect the creature, though the actions  you used are still ex |

### Query 138
- Text: Summarize SPECIAL ARCHETYPES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `44`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/20` | 0.872544 | SPECIAL ARCHETYPES |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/1` | 0.741735 | ARCHETYPES |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/46` | 0.645303 | **Archetypes** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/52` | 0.645303 | **Archetypes** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/38` | 0.645303 | **Archetypes** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/56` | 0.645303 | **Archetypes** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/14` | 0.642034 | SPELLCASTING ARCHETYPES |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/18` | 0.629839 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/16` | 0.629839 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/SectionHeader/11` | 0.629839 | **ARCHETYPE** |

### Query 139
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/34']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `9`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/61` | 0.908832 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/45` | 0.908832 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/51` | 0.908832 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/69` | 0.908832 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/39` | 0.908832 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/34` | 0.908832 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/42` | 0.908832 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/19` | 0.908832 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/28` | 0.888833 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/57` | 0.888833 | **PLAYING THE ** **GAME** |

### Query 140
- Text: What are the requirements for **ENVOY DEDICATION** **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `38`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/27` | 0.805382 | **ENVOY DEDICATION** **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/24` | 0.711118 | **Prerequisites** Envoy Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/19` | 0.711118 | **Prerequisites** Envoy Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/34` | 0.711118 | **Prerequisites** Envoy Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/39` | 0.711118 | **Prerequisites** Envoy Dedication |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/10` | 0.706117 | **OPERATIVE DEDICATION** **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/5` | 0.680726 | **MYSTIC DEDICATION** **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/SectionHeader/6` | 0.666690 | DEDICATION DETAILS |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/10` | 0.660750 | **SOLDIER DEDICATION** **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.650358 | **Prerequisites** Operative Dedication |

### Query 141
- Text: What are the requirements for **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `27`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.899799 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.810917 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12` | 0.797651 | **GET 'EM! **[one-action]** TO **[two-actions] |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.793763 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.774815 | **READY ARMS! **[one-action]** TO **[two-actions] |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.756623 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/22` | 0.743287 | **DANCE PARTNER! **[one-action]** TO **[two-actions] |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/39` | 0.741798 | **KEEP ON KEEPING ON!** [one-action]** TO **[two-actions] |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/9/SectionHeader/3` | 0.741010 | **STEEL YOURSELVES! **[one-action]** TO **[two-actions] |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/5` | 0.729367 | **COORDINATED AMBUSH! **[one-action]** TO **[two-actions] |

### Query 142
- Text: What is the rule about You gain the leader's confidence class feature (see page  107).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `16`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/25` | 0.861096 | You gain the leader's confidence class feature (see page  107). |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/40` | 0.688339 | You gain the primary target class feature (page 152). |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/35` | 0.665722 | You gain the suppressing fire class feature (page 152). |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/31` | 0.615038 | Your confidence is a battery that keeps your allies going.  When you use a directive that grants temporary Hit Points, |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/52` | 0.593025 | You gain the master spellcasting benefits (page 174). |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/50` | 0.593025 | You gain the master spellcasting benefits (page 174). |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/13` | 0.585166 | **Prerequisites** Strength +2 You gain the stellar attunement class feature (page 140), but |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/20` | 0.578452 | You gain the Lead by Example benefit for your Get 'Em!  directive, except you and your allies get a +2 status bonus  to damage on both the initial and subsequent Strikes. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/30` | 0.574207 | You gain the envoy directives class feature (see page  104), but do not gain the Lead by Example benefits  of the Get 'Em! envoy directive. You become trained in  Deception, Diplomacy, or Intimidation |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/10` | 0.574111 | from their class features; and more. Your character's class  entry also provides the information needed when they  gain levels, so it will be a vital reference throughout the  course of your campaign. |

### Query 143
- Text: What are the requirements for **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.912294 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.797147 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.772087 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.765818 | **READY ARMS! **[one-action]** TO **[two-actions] |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12` | 0.754232 | **GET 'EM! **[one-action]** TO **[two-actions] |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/22` | 0.752511 | **DANCE PARTNER! **[one-action]** TO **[two-actions] |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.736834 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22` | 0.730746 | **SEARCH HIGH AND LOW! **[one-action]** TO **[two-actions] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/39` | 0.729687 | **KEEP ON KEEPING ON!** [one-action]** TO **[two-actions] |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/5` | 0.723523 | **COORDINATED AMBUSH! **[one-action]** TO **[two-actions] |

### Query 144
- Text: What is the rule about Scent involves sensing creatures or objects by smell, and is  usually a vague sense. The range is listed in the ability, and it  functions only if the creature or object being detected emits  an aroma. If a creature emits a heavy aroma or is upwind, the  GM can double or even triple the range of scent abilities used  to detect that creature, and the GM can reduce the range if a  creature is downwind.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `33`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/5` | 0.952098 | Scent involves sensing creatures or objects by smell, and is  usually a vague sense. The range is listed in the ability, and it  functions only if the creature or object being detected emits  an aroma |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/23` | 0.681512 | A character also has many vague senses—ones that can alert  you that something is there but aren't useful for zeroing in on  it to determine exactly what it is. The most useful of these  for a typical |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/16` | 0.676735 | Most abilities that designate "a creature you can see"  or the like function just as well if the user can precisely  sense the subject with a different sense. If a monster  uses a sense other than vis |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/7` | 0.675647 | Tremorsense allows a creature to feel the vibrations through  a solid surface caused by movement. It's usually an imprecise  sense with a limited range (listed in the ability). Tremorsense  functions |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/11` | 0.673076 | Typically, the GM tracks how well creatures detect each  other since neither party has perfect information. For  example, you might think a creature is in the last place  you sensed it, but it was abl |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.661827 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.649395 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.647157 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/24` | 0.640427 | When one creature might detect another, the GM almost  always uses the most precise sense available. |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 0.638244 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |

### Query 145
- Text: Summarize SPECIAL SENSES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `17`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/25` | 0.836069 | SPECIAL SENSES |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/20` | 0.752168 | IMPRECISE SENSES |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/17` | 0.724314 | PRECISE SENSES |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/15` | 0.689832 | SENSES |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/SectionHeader/22` | 0.654241 | VAGUE SENSES |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/15` | 0.628328 | **DETECTING WITH OTHER SENSES** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/10/SectionHeader/15` | 0.617789 | SPECIAL CIRCUMSTANCES |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/SectionHeader/17` | 0.602403 | **Using Stealth with Other Senses** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/4/SectionHeader/24` | 0.591266 | SPECIALTY BASIC ACTIONS |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/9/SectionHeader/34` | 0.573352 | INCREDIBLE SENSES 17TH |

### Query 146
- Text: Summarize **MOVE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/2/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `41`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/23` | 0.859825 | **MOVE** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/16` | 0.859825 | **MOVE** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/2` | 0.859825 | **MOVE** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/7` | 0.859825 | **MOVE** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/32` | 0.859825 | **MOVE** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/11` | 0.859825 | **MOVE** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/4` | 0.859825 | **MOVE** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/23` | 0.859825 | **MOVE** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/4` | 0.859825 | **MOVE** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/12` | 0.859825 | **MOVE** |

### Query 147
- Text: What is the rule about An archetype feat is subject to any restrictions on the class  feat it replaces. For example, if you had an ability at 6th level  that granted you a bonus class feat, but that class feat had to  be 4th level or lower and have the vesk trait, you could use  that class feat to take an archetype class feat, but only one of  4th level or lower with the vesk trait.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `27`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/5` | 0.977195 | An archetype feat is subject to any restrictions on the class  feat it replaces. For example, if you had an ability at 6th level  that granted you a bonus class feat, but that class feat had to  be 4t |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` | 0.731259 | Some archetypes include a list of "Additional Feats" that  appear in other sources. The list includes each feat's level,  which might be different than normal when gained from the  archetype. You can |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.731107 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.724962 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/4` | 0.679286 | You gain an archetype by selecting archetype feats instead  of your normal feats. First, find the archetype that best  fits your character concept. Then select that archetype's  dedication feat, using |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/22` | 0.647109 | For instance, you can't replace a skill feat you chose at 2nd  level for a 4th-level one, or for one that requires prerequisites  you didn't meet at the time you took the original feat. If you  don't |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/7` | 0.622333 | Each archetype's dedication feat represents your character's  dedicated effort learning a new set of abilities, making it  impossible to split your focus and pursue another archetype  at the same time |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/17` | 0.622275 | **Basic Spellcasting Feat:** Usually available at 4th level,  these feats grant a 1st-rank spell slot. At 6th level, they  grant you a 2nd-rank spell slot, and if you have a spell  repertoire, you can |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.618161 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.616423 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |

### Query 148
- Text: What are the requirements for **READY TO ROLL **[free-action] **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44` | 0.851694 | **READY TO ROLL **[free-action] **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/35` | 0.622612 | **SAW IT COMING **[free-action] **FEAT 4** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/10` | 0.602656 | **RELEASE **[free-action] |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49` | 0.602475 | **YOU CAN DO IT **[one-action] **FEAT 14** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/2` | 0.593248 | **EXTEND DIRECTIVE **[free-action] **FEAT 16** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/12` | 0.589830 | **Requirements** You have a fly Speed. |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/32` | 0.589830 | **Requirements** You have a fly Speed. |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/6` | 0.588328 | **READY **[two-actions] |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/34` | 0.587505 | **DOWN TO THE WIRE **[reaction] **FEAT 14** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/8` | 0.581466 | **Requirements** Your Speed is at least 10 feet. |

### Query 149
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `21`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/21` | 0.883367 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/20` | 0.883367 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/47` | 0.883367 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/34` | 0.883367 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/23` | 0.883367 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/27` | 0.883367 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/30` | 0.883367 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/31` | 0.863367 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/56` | 0.863367 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/31` | 0.863367 | **INTRODUCTION** |

### Query 150
- Text: What is the rule about There are only a few basic reactions and free actions that  all characters can use. You're more likely to gain actions with  triggers from your class, feats, and magic items.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `24`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/28` | 0.921834 | There are only a few basic reactions and free actions that  all characters can use. You're more likely to gain actions with  triggers from your class, feats, and magic items. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/10` | 0.690311 | **Reactions** have triggers, which must be met for you to use  the reaction. You can use a reaction anytime its trigger is met,  whether it's your turn or not. Outside of encounters, your use  of reac |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/1` | 0.688412 | free actions limit when you can use those actions. You can use  only one action in response to a given trigger. For example, if  you had a reaction and a free action that both had a trigger  of "your |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/27` | 0.678348 | You can use free actions that have triggers and reactions only  in response to certain events. Each such reaction and free  action lists the trigger that must happen for you to perform it.  When its t |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/8/Text/2` | 0.676900 | Some reactions and free actions are triggered by a  creature using an action with the move trait. The most  notable example is Reactive Strike (reproduced below).  Actions with the move trait can trig |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/2` | 0.674299 | This limitation of one action per trigger is per creature;  more than one creature can use a reaction or free action  in response to a given trigger. If multiple actions would be  occurring at the sam |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/11` | 0.673163 | **Free actions** don't cost you any of your actions per turn,  nor do they cost your reaction. A free action with no trigger  follows the same rules as a single action (except the action  cost). It mu |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/2` | 0.668244 | Basic actions represent common tasks like moving around,  attacking, and helping others. As such, every creature can  use basic actions except in some extreme circumstances,  and many of those actions |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/26` | 0.667202 | Your reactions let you respond immediately to what's  happening around you. The GM determines whether you can  use reactions before your first turn begins, depending on the  situation in which the enc |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/13` | 0.657674 | You can use actions in any order you wish during your  turn, but you have to complete one action or activity before  beginning another; for example, you can't use a single action in  the middle of per |

### Query 151
- Text: Summarize **Immunity, ** **Weakness, & ** **Resistance**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/32']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `28`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/57` | 0.934897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/38` | 0.934897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/44` | 0.934897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/23` | 0.934897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/33` | 0.934897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/30` | 0.934897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/32` | 0.934897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/44` | 0.914897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/35` | 0.914897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/37` | 0.914897 | **Immunity, ** **Weakness, & ** **Resistance** |

### Query 152
- Text: Summarize **MANIPULATE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `27`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/11` | 0.867105 | **MANIPULATE** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/32` | 0.867105 | **MANIPULATE** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/15` | 0.867105 | **MANIPULATE** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/7/SectionHeader/14` | 0.769994 | **EXPLORATION** **MANIPULATE** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/7/SectionHeader/10` | 0.769994 | **EXPLORATION** **MANIPULATE** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/8/SectionHeader/3` | 0.769994 | **EXPLORATION** **MANIPULATE** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/28` | 0.733032 | **AUDITORY** **MANIPULATE** **VISUAL** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/27` | 0.637886 | **POINT OUT **[one-action] |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/8` | 0.628502 | **CONCENTRATE** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/5/SectionHeader/40` | 0.628502 | **CONCENTRATE** |

### Query 153
- Text: What is the rule about Tremorsense allows a creature to feel the vibrations through  a solid surface caused by movement. It's usually an imprecise  sense with a limited range (listed in the ability). Tremorsense  functions only if the detecting creature is on the same surface  as the subject, and only if the subject is moving along (or  burrowing through) the surface.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/7` | 0.957607 | Tremorsense allows a creature to feel the vibrations through  a solid surface caused by movement. It's usually an imprecise  sense with a limited range (listed in the ability). Tremorsense  functions |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/5` | 0.676503 | Scent involves sensing creatures or objects by smell, and is  usually a vague sense. The range is listed in the ability, and it  functions only if the creature or object being detected emits  an aroma |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.655655 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/6/Text/15` | 0.652801 | A burrow Speed lets you tunnel through solids. You can use  the Burrow action (page 411) if you have a burrow Speed.  Burrowing doesn't normally leave behind a tunnel unless the  ability specifically |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 0.638863 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.635255 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.629952 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/16` | 0.615966 | Most abilities that designate "a creature you can see"  or the like function just as well if the user can precisely  sense the subject with a different sense. If a monster  uses a sense other than vis |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.615260 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/9` | 0.613578 | Three conditions measure the degree to which you can sense  a creature: observed, hidden, and undetected. However, the  concealed and invisible conditions can partially mask a  creature, and the unnot |

### Query 154
- Text: Summarize **Immunity, ** **Weakness, & ** **Resistance**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/37']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `19`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/35` | 0.934897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/37` | 0.934897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/56` | 0.934897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/39` | 0.934897 | **Immunity, ** **Weakness, & ** **Resistance** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/44` | 0.934897 | **Immunity, ** **Weakness, & ** **Resistance** |
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
- Graph boosted count: `49`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/23` | 0.857823 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/54` | 0.857823 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/59` | 0.857823 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/64` | 0.857823 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/18` | 0.857823 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/44` | 0.857823 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/39` | 0.857823 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/49` | 0.857823 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/30` | 0.857823 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/35` | 0.857823 | **ARCHETYPE** |

### Query 156
- Text: What is the rule about **Checks**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `17`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/35` | 0.791192 | **Checks** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/33` | 0.791192 | **Checks** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/54` | 0.791192 | **Checks** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/37` | 0.791192 | **Checks** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/42` | 0.791192 | **Checks** |
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
- Graph boosted count: `36`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/19` | 0.897387 | **Prerequisites** Envoy Dedication |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/24` | 0.897387 | **Prerequisites** Envoy Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/34` | 0.897387 | **Prerequisites** Envoy Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/39` | 0.897387 | **Prerequisites** Envoy Dedication |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/18` | 0.734548 | **Prerequisites** Soldier Dedication |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/39` | 0.734548 | **Prerequisites** Soldier Dedication |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/34` | 0.734548 | **Prerequisites** Soldier Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.715225 | **Prerequisites** Operative Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.715225 | **Prerequisites** Operative Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.715225 | **Prerequisites** Operative Dedication |

### Query 158
- Text: What is the rule about Effects can change the number of actions you can use on  your turn, or whether you can use actions at all. The slowed  condition, for example, causes you to lose actions, while the  quickened condition causes you to gain them. Conditions are  detailed in the appendix on pages 435–441. Whenever you  lose a number of actions—whether from these conditions or  in any other way—you choose which to lose if there's any  difference between them. For instance, the *haste* spell makes  you quickened, but it limits what you can use your extra  action to do. If you lost an action while *haste* was active, you  might want to lose the action from *haste* first since it's more  limited than your normal actions.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/6` | 0.998423 | Effects can change the number of actions you can use on  your turn, or whether you can use actions at all. The slowed  condition, for example, causes you to lose actions, while the  quickened conditio |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/15` | 0.861745 | Quickened, slowed, and stunned are the primary  ways you can gain or lose actions on a turn. The rules  for how this works appear on page 407. In brief, these  conditions alter how many actions you re |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` | 0.779891 | Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or S |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/15/Text/9` | 0.776870 | You're able to act more quickly. You gain 1 additional action  at the start of your turn each round. Many effects that make  you quickened require you use this extra action only in certain  ways. If y |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/4/Text/11` | 0.776789 | • Regain your 3 actions and 1 reaction. If you haven't spent  your reaction from your last turn, you lose it—you can't  "save" actions or reactions from one turn to use during the  next turn. Some abi |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.750496 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/16/Text/1` | 0.750146 | Stunned overrides slowed. If the duration of your  stunned condition ends while you're slowed, you count the  actions lost to the stunned condition toward those lost to  being slowed. So, if you were |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/7` | 0.749866 | Some effects are even more restrictive. Certain abilities,  instead of or in addition to changing the number of actions  you can use, say specifically that you can't use reactions.  The most restricti |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/58` | 0.743719 | Some effects apply conditions to a creature or item. These change your state of being in some way. Conditions are  persistent, lasting until the stated duration ends, the condition is removed, or term |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/18` | 0.742432 | case of an activity, you usually lose all actions spent for the  activity up through the end of that turn. For instance, if you  began to Cast a Spell requiring 3 actions and the first action  was dis |

### Query 159
- Text: Summarize You issue directives to your allies, granting benefits and letting you take the lead.  Your words and deeds bolster your allies or harry your foes, and your cunning can  get you and your team out of danger.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `42`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/11` | 0.979160 | You issue directives to your allies, granting benefits and letting you take the lead.  Your words and deeds bolster your allies or harry your foes, and your cunning can  get you and your team out of d |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/9` | 0.777325 | Envoys encourage their allies with directives. A directive is  an order that benefits allies who follow it. Envoy directives  include a way for the envoy to lead by example by spending  more actions f |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/54` | 0.761181 | You provide a quick follow-up to your ongoing directive,  encouraging your ally when they successfully hit your |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/19` | 0.757589 | You're most comfortable leading your allies from the front lines  of battle while you fight alongside them. You might raise a  shield to help weather the storm of incoming gunfire or simply  lead with |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/48` | 0.754613 | You instinctively react to trouble by directing your allies to  act at the exact moment their intervention would matter  most. Issue a 1-action directive. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/3` | 0.751534 | **Directive**: Actions with this trait are special orders  that provide benefits for your allies if they follow  them. Your allies must be able to sense you to benefit  from your directives. This acti |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/36` | 0.749549 | You step up to lead during difficult times. You might have  experienced a traumatic event, perhaps escaping a pirate ship  during a mutiny, or you fought in some notorious battle. Your  allies trust y |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/15` | 0.737203 | People follow your lead because you help push them to  their ultimate potential. Each of your allies gain a second  reaction if they start their turn within 100 feet of you and  can perceive you. This |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/4` | 0.736300 | The envoy is a plucky leader who supports their  allies with battlefield directives, social savviness, and  a suite of skills. Envoys call out directives to their  allies, granting powerful boons that |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/2` | 0.728987 | You prefer to direct your allies in subtle ways, without drawing  much attention from foes. You might sneak in behind your  bodyguards or support your team from a safe distance. |

### Query 160
- Text: Summarize You increase your maximum number  of HP by this number at 1st level and  every level thereafter.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/9` | 0.954135 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 0.720500 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/16` | 0.680018 | You gain a vitality network with 10 Hit Points and can  use Transfer Vitality to transfer up to 10 HP. Increase the  maximum capacity of your vitality network by 10 at 10th,  15th, and 20th-level. Inc |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/1` | 0.665109 | rush into battle with weapons raised gain a higher number  of Hit Points each level, while characters who cast spells or  engage in trickery gain fewer. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/5` | 0.663089 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/3` | 0.662523 | You gain more skill increases than members of other classes.  At 2nd level and every level thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you' |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/6` | 0.660410 | At 1st level, your class gives you  an attribute boost to Charisma. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/42` | 0.659836 | Increase the number of spells in your repertoire and number  of spell slots you gain from mystic archetype feats by 1 for  each spell rank other than your two highest mystic spell slots. |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/51` | 0.656851 | You gain a 1st- or 2nd-level operative feat. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/14` | 0.656042 | In addition to the initial ancestry feat you started with, you  gain an ancestry feat at 5th level and every 4 levels thereafter. |

### Query 161
- Text: What are the requirements for **ADVANCED MYSTICISM** **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `30`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/27` | 0.756218 | **ADVANCED MYSTICISM** **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/17` | 0.661681 | **ADVANCED GUNNER** **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/31` | 0.660593 | **ADVANCED STELLAR ATTUNEMENT** **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/30` | 0.659199 | **ADVANCED DISTORTION** **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/25` | 0.658552 | **ADVANCED SOLDIER TRAINING** **FEAT 6** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/10` | 0.650838 | **ADVANCED LEADERSHIP** **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/40` | 0.627931 | 6TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/25` | 0.613326 | **Prerequisites** Mystic Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/15` | 0.613326 | **Prerequisites** Mystic Dedication |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/20` | 0.613326 | **Prerequisites** Mystic Dedication |

### Query 162
- Text: What are the requirements for **CUT 'EM DEEP** **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `9`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/43` | 0.729269 | **CUT 'EM DEEP** **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/7/TableCell/561` | 0.628078 | 10 feet |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/7/TableCell/562` | 0.628078 | 10 feet |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/6/TableCell/352` | 0.628078 | 10 feet |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/7/TableCell/567` | 0.628078 | 10 feet |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/550` | 0.625740 | Cut 'Em Deep |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/36` | 0.611565 | **PRIMARY TARGET** **FEAT 10** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/8` | 0.611251 | **Requirements** Your Speed is at least 10 feet. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/49` | 0.601325 | **GOT 'EM **[free-action] **FEAT 10** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/7/TableCell/569` | 0.588705 | 20 feet or more |

### Query 163
- Text: What is the rule about Some archetypes grant you a substantial degree of  spellcasting, albeit delayed compared to a character from a  spellcasting class. The spellcasting ability from a spellcasting  archetype also allows you to use Cast a Spell activations of  items (such as spell chips and spell gems).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/15` | 0.955048 | Some archetypes grant you a substantial degree of  spellcasting, albeit delayed compared to a character from a  spellcasting class. The spellcasting ability from a spellcasting  archetype also allows |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.762467 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.717090 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/5` | 0.694827 | An archetype feat is subject to any restrictions on the class  feat it replaces. For example, if you had an ability at 6th level  that granted you a bonus class feat, but that class feat had to  be 4t |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/2` | 0.687064 | Archetypes allow you to further customize your character concepts by taking more than one class. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` | 0.686461 | Some archetypes include a list of "Additional Feats" that  appear in other sources. The list includes each feat's level,  which might be different than normal when gained from the  archetype. You can |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.667585 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/10` | 0.667473 | You cast spells like a witchwarper. You gain access to the Cast  a Spell activity. You gain a spell repertoire with two common  cantrips from the spell list associated with your paradox, from  the spe |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/10` | 0.664618 | You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by you |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.663105 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |

### Query 164
- Text: Summarize **Soldier**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `24`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/28` | 0.827669 | **Soldier** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/38` | 0.827669 | **Soldier** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/33` | 0.827669 | **Soldier** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/36` | 0.827669 | **Soldier** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/55` | 0.827669 | **Soldier** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/63` | 0.827669 | **Soldier** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/45` | 0.827669 | **Soldier** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/50` | 0.807669 | **Soldier** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/54` | 0.807669 | **Soldier** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/44` | 0.807669 | **Soldier** |

### Query 165
- Text: What is the rule about Solarian envoys are beacons of hope amid a chaotic  battlefield leading the charge with feats like Pardon  Me and Get in There! A solarian envoy can use Adaptive  Talent to choose different Athletics feats based on the  terrain they expect to encounter.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/7` | 0.940184 | Solarian envoys are beacons of hope amid a chaotic  battlefield leading the charge with feats like Pardon  Me and Get in There! A solarian envoy can use Adaptive  Talent to choose different Athletics |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/4/ListItem/5` | 0.655547 | Envoy solarians can rush into close quarters to  properly assess an enemy's abilities and positioning  when determining what directives to use. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/4` | 0.608847 | The solarian archetype allows characters to wield powerful  solar weapons and engage in melee combat. |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/426` | 0.593924 | Adaptive talent, ancestry feat, envoy expertise, hidden agenda, skill increase |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/8` | 0.593225 | As your envoy level increases, so does your ability to adapt  to new situations. At 9th level and 15th level, increase the  number of skill feats you gain this way by 1. You can use  feats that you te |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/ListItem/8` | 0.588736 | Soldier envoys make natural commanders who can  use their defensive capabilities to keep the bonuses  of their directive's active against powerful enemies  while clearing out weaker foes with area fir |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/ListItem/5` | 0.587674 | Envoy soldiers are natural tacticians who use directives to  position enemies and allies to optimize their area attacks. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/4` | 0.578356 | The envoy archetype allows you to take on a leadership role  by giving out directives that can support allies or hinder  enemies. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/4` | 0.577061 | The envoy is a plucky leader who supports their  allies with battlefield directives, social savviness, and  a suite of skills. Envoys call out directives to their  allies, granting powerful boons that |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/11` | 0.575002 | The solarian is a warrior who channels the  cosmic cycle. Every solarian creates weapons of pure  stellar energy that they can manifest at will. Cycling  between graviton and photon attunement, a sola |

### Query 166
- Text: What is the rule about **Activities** usually take longer and require using multiple  actions, which must be spent in succession. Strike is a single  action, but Double Tap is an activity in which you use both  the Aim and Strike actions to generate its effect.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/9` | 0.950780 | **Activities** usually take longer and require using multiple  actions, which must be spent in succession. Strike is a single  action, but Double Tap is an activity in which you use both  the Aim and |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/13` | 0.802368 | You can use only one single action, activity, or free action  that doesn't have a trigger at a time. You must complete  one before beginning another. For example, the Double  Tap activity states you m |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/17` | 0.718394 | Using an activity isn't the same as using any of  its subordinate actions. For example, the quickened  condition you get from the *haste* spell lets you spend  an extra action each turn to Stride or S |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/2` | 0.675543 | Basic actions represent common tasks like moving around,  attacking, and helping others. As such, every creature can  use basic actions except in some extreme circumstances,  and many of those actions |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/20` | 0.670237 | An activity typically involves using multiple actions to create  an effect greater than you can produce with a single action,  or combining multiple single actions to produce an effect  that's differe |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/9` | 0.667151 | Various abilities and conditions, such as a Reactive Strike,  can disrupt an action. When an action is disrupted, you still  use the actions or reactions you committed, and you still  expend any costs |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.662782 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` | 0.653372 | Sometimes you need to attempt something not already  covered by defined actions in the game. When this happens,  the rules tell you how many actions you need to spend as  well as any traits your actio |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/12` | 0.634498 | You seize the opening your ally has provided, quickly  attacking your foe. Make a Strike against the triggering  creature. If it's a ranged Strike, it must be in your weapon's  first range increment. |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/20` | 0.634100 | **Long Tasks:** For a task that takes longer than a  round, you often need to spend more than one action  preparing to help, as determined by the GM. |

### Query 167
- Text: Summarize **Movement**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/37']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `38`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/28` | 0.838841 | **Movement** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/49` | 0.838841 | **Movement** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/62` | 0.838841 | **Movement** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/38` | 0.838841 | **Movement** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/35` | 0.838841 | **Movement** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/43` | 0.838841 | **Movement** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/37` | 0.838841 | **Movement** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/45` | 0.838841 | **Movement** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/49` | 0.818841 | **Movement** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/42` | 0.818841 | **Movement** |

### Query 168
- Text: What is the rule about **Actions**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/41']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `12`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/48` | 0.737762 | **Actions** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/39` | 0.737762 | **Actions** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/41` | 0.737762 | **Actions** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/60` | 0.737762 | **Actions** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/43` | 0.737762 | **Actions** |
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
- Graph boosted count: `35`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/18` | 0.976444 | The Stealth skill is designed to use Hide for avoiding  visual detection and Avoid Notice and Sneak to avoid  being both seen and heard. For many special senses,  a player can describe how they're avo |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/19` | 0.776948 | In some cases, rolling a Dexterity-based Stealth  skill check to Sneak doesn't make the most sense.  For example, a PC trying to avoid being detected by  a creature that senses heartbeats might medita |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/12` | 0.770915 | You can attempt to avoid detection by using the Stealth  skill (page 207) to Avoid Notice, Hide, or Sneak, or by using  Deception to Create a Diversion (page 198). |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/6/Text/21` | 0.755000 | You attempt a Stealth check to avoid notice while traveling  at half speed. If you're Avoiding Notice at the start of an  encounter, you usually roll a Stealth check instead of a  Perception check bot |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.713818 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/18` | 0.711772 | You can't be seen. You're undetected to everyone. Creatures  can Seek to detect you; if a creature succeeds at its Perception  check against your Stealth DC, you become hidden to that  creature until |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.705817 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.697194 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/20` | 0.684971 | Anything in plain view is observed by you. If a creature takes  measures to avoid detection, such as by using Stealth to Hide,  it can become hidden or undetected instead of observed. If you |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/19` | 0.681319 | a creature without having drawbacks is to use a precise  sense. You can usually detect a creature automatically with  a precise sense unless that creature is hiding or obscured by  the environment, in |

### Query 170
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/59']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `7`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/65` | 0.899439 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/59` | 0.899439 | **GLOSSARY & ** **INDEX** |
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
- Graph boosted count: `21`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/53` | 0.926238 | **Rules Overview** |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/34` | 0.926238 | **Rules Overview** |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/32` | 0.926238 | **Rules Overview** |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/36` | 0.926238 | **Rules Overview** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/5/Text/41` | 0.926238 | **Rules Overview** |
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
- Graph boosted count: `11`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/6/TableCell/349` | 0.697223 | Feet per Minute |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/6/Table/8` | 0.672784 | SpeedFeet per MinuteMiles per HourMiles per Day10 feet1001815 feet1501-1/21220 feet20021625 feet2502-1/22030 feet30032435 feet3503-1/22840 feet40043250 feet50054060 feet600648 |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/6/TableCell/348` | 0.636698 | Speed |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/6/TableCell/350` | 0.611636 | Miles per Hour |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/6/SectionHeader/7` | 0.602344 | **TRAVEL SPEED** |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/6/TableCell/351` | 0.593524 | Miles per Day |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/6/SectionHeader/10` | 0.590614 | SPEED |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/6/SectionHeader/24` | 0.586568 | SWIM SPEED |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/8/Text/13` | 0.584696 | You Seek meticulously for hidden doors, concealed hazards,  and so on. You can usually make an educated guess as to which  locations are best to check and move at half speed, but if you  want to be th |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/4/Text/8` | 0.582032 | **Requirements** Your Speed is at least 10 feet. |

### Query 173
- Text: Summarize Three conditions measure the degree to which you can sense  a creature: observed, hidden, and undetected. However, the  concealed and invisible conditions can partially mask a  creature, and the unnoticed condition indicates you have no  idea a creature is around. You can find these conditions in  the Conditions Appendix on pages 435–441.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/1/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `33`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/9` | 1.010904 | Three conditions measure the degree to which you can sense  a creature: observed, hidden, and undetected. However, the  concealed and invisible conditions can partially mask a  creature, and the unnot |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.826386 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.805906 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/24` | 0.799653 | If a creature is undetected, you don't know what space it  occupies and you're off-guard to it. The Seek basic action can  help you find an undetected creature, usually making it hidden  from you inst |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/4` | 0.772990 | If you have no idea a creature is even present, that creature  is unnoticed by you. A creature that's undetected might also  be unnoticed. This condition usually matters for abilities  that can be use |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/8` | 0.768656 | A creature with the invisible condition (by way of an  *invisibility* spell, for example) is automatically undetected  to any creatures relying on sight as their only precise  sense. Precise senses ot |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.766404 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/20` | 0.759917 | Anything in plain view is observed by you. If a creature takes  measures to avoid detection, such as by using Stealth to Hide,  it can become hidden or undetected instead of observed. If you |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/10` | 0.753344 | With the exception of invisible, these conditions are  relative to the viewer—it's possible for a creature to be  observed to you but hidden from your ally. Most of these  rules apply to objects as we |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/23` | 0.747552 | A character also has many vague senses—ones that can alert  you that something is there but aren't useful for zeroing in on  it to determine exactly what it is. The most useful of these  for a typical |

### Query 174
- Text: What are the requirements for **Prerequisites** Size Up?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `13`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17` | 0.890795 | **Prerequisites** Size Up |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/7` | 0.890795 | **Prerequisites** Size Up |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/612` | 0.721945 | Size Up |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/30` | 0.677186 | **SIZE UP** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34` | 0.657380 | **Prerequisites** Watch Out |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/26` | 0.657380 | **Prerequisites** Watch Out |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/13/SectionHeader/57` | 0.610752 | **CONDITIONS** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/63` | 0.601687 | **CONDITIONS ** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/27` | 0.601687 | **CONDITIONS ** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.600369 | **Prerequisites** trained in Intimidation |

### Query 175
- Text: Summarize **AID DETAILS**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/18` | 0.901891 | **AID DETAILS** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/7` | 0.711094 | **AID **[reaction] |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/31` | 0.696373 | **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/56` | 0.676373 | **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/44` | 0.676373 | **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/67` | 0.676373 | **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/58` | 0.676373 | **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/44` | 0.667715 | **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/54` | 0.667715 | **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/4` | 0.667279 | **KEY ATTRIBUTE** |

### Query 176
- Text: Summarize Average vision is a precise sense—a sense that can be used to  perceive the world in nuanced detail. The only way to target
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/18` | 0.984171 | Average vision is a precise sense—a sense that can be used to  perceive the world in nuanced detail. The only way to target |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/10` | 0.682359 | In bright light, such as sunlight, creatures and objects can  be observed clearly by anyone with average vision or better. |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.676608 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/12/Text/14` | 0.674569 | Your eyes are overstimulated or your vision is swimming. If  vision is your only precise sense, all creatures and objects are  concealed from you. |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.671181 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/14` | 0.641885 | In most circumstances, you can sense creatures without  difficulty and target them normally. Creatures in this state  are observed. Observing requires a precise sense, which for  most creatures means |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.629604 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 8 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/2` | 0.605095 | Your Perception measures your ability to notice things, search for what's hidden, and tell whether  something about a situation is suspicious. |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/1` | 0.601448 | such vision is in black and white only. Some forms of magical  darkness, such as a 4th-rank *darkness* spell, block normal  darkvision. A creature with greater darkvision, however, can  see through ev |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/12/Text/3` | 0.600708 | **Detection**: Observed, hidden, undetected, unnoticed **Senses**: Blinded, concealed, dazzled, deafened,  invisible |

### Query 177
- Text: What is the rule about You affect the world around you primarily by using actions, which produce effects. Actions are most  closely measured and restricted during the encounter mode of play, but even when it isn't important for  you to keep strict track of actions, they remain the way in which you interact with the game world.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `27`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/2` | 0.936674 | You affect the world around you primarily by using actions, which produce effects. Actions are most  closely measured and restricted during the encounter mode of play, but even when it isn't important |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/6/Text/2` | 0.745689 | Your movement and position determine how you interact with the world. Moving in exploration and  downtime modes is relatively fluid. Movement in encounter mode follows additional rules explained in  T |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/1` | 0.672977 | When every individual action counts, you enter the encounter mode of play. In this mode, time  is divided into rounds, each of which is 6 seconds of time in the game world. Every round, each  particip |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/2/Text/33` | 0.671179 | You use your hand or hands to manipulate an object or the  terrain. You can grab an unattended or stored object, draw  a weapon, swap a held item for another (see the Changing  Equipment table on page |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/22` | 0.669194 | You have to spend all the actions of an activity at once  to gain its effects. In an encounter, this means you must  complete it during your turn. If an activity gets interrupted or  disrupted in an e |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/14/Text/1` | 0.668611 | An area always has a point of origin and extends out from that  point. There are four types of areas: bursts, cones, emanations,  and lines. When you're playing in encounter mode and using a  grid, ar |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/4` | 0.663899 | An encounter is played out in a series of rounds, during which  the player characters, adversaries, and other participants in the  encounter act in sequence. You roll initiative to determine this  ord |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/2` | 0.661811 | Anything you do in the game has an effect. Many of these outcomes are easy to adjudicate during the  game. If you tell the GM that you draw your laser pistol, no check is needed. Other times, the spec |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/13` | 0.657860 | Your movement during encounter mode—and at other times  where precise movement matters—depends on the actions  and other abilities you use. Whether you Stride, Step, Swim,  or Climb, the maximum dista |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/82` | 0.655560 | effect, though the GM makes the final call. In an area effect, creatures or targets must have line of  effect to the point of origin to be affected. If there's no line  of effect between the origin of |

### Query 178
- Text: Summarize **ARCHETYPE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/50']
- Expected found: `True`
- Expected rank: `28`
- Graph boost applied: `True`
- Graph boosted count: `49`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/23` | 0.857823 | **ARCHETYPE** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/54` | 0.857823 | **ARCHETYPE** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/59` | 0.857823 | **ARCHETYPE** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/64` | 0.857823 | **ARCHETYPE** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/18` | 0.857823 | **ARCHETYPE** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/44` | 0.857823 | **ARCHETYPE** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/39` | 0.857823 | **ARCHETYPE** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/49` | 0.857823 | **ARCHETYPE** |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/30` | 0.857823 | **ARCHETYPE** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/35` | 0.857823 | **ARCHETYPE** |

### Query 179
- Text: What are the requirements for **EXTEND DIRECTIVE **[free-action] **FEAT 16**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `32`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/2` | 0.885106 | **EXTEND DIRECTIVE **[free-action] **FEAT 16** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/566` | 0.693117 | Extend Directive |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44` | 0.650054 | **READY TO ROLL **[free-action] **FEAT 14** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/14` | 0.642796 | **SECONDARY DIRECTIVE **[one-action] **FEAT 12** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/18` | 0.624530 | **DELAY **[free-action] |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/16` | 0.618777 | **IMPROVISED LEGEND **[free-action] **FEAT 18** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/28` | 0.613016 | **UNSTOPPABLE DIRECTIVES** **FEAT 12** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/7` | 0.602100 | **GET THEM!** **FEAT 16** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/55` | 0.600617 | **EFFORTLESS INFLUENCER** **FEAT 16** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/3/SectionHeader/10` | 0.598857 | **RELEASE **[free-action] |

### Query 180
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/40']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `19`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/28` | 0.908832 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/36` | 0.908832 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/26` | 0.908832 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/29` | 0.908832 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/34` | 0.908832 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/53` | 0.908832 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/40` | 0.908832 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/45` | 0.888833 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/69` | 0.888833 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/57` | 0.888833 | **PLAYING THE ** **GAME** |

### Query 181
- Text: What is the rule about You gain an archetype by selecting archetype feats instead  of your normal feats. First, find the archetype that best  fits your character concept. Then select that archetype's  dedication feat, using one of your class feat choices. Once  you've taken the dedication feat, you can select any feat from  that archetype, as long as you meet its prerequisites. Most  archetype feats are taken in place of class feats, and so these  are called archetype class feats.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/4` | 0.969521 | You gain an archetype by selecting archetype feats instead  of your normal feats. First, find the archetype that best  fits your character concept. Then select that archetype's  dedication feat, using |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` | 0.836757 | Some archetypes include a list of "Additional Feats" that  appear in other sources. The list includes each feat's level,  which might be different than normal when gained from the  archetype. You can |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.818760 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.811906 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/7` | 0.807092 | Each archetype's dedication feat represents your character's  dedicated effort learning a new set of abilities, making it  impossible to split your focus and pursue another archetype  at the same time |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/5` | 0.767286 | An archetype feat is subject to any restrictions on the class  feat it replaces. For example, if you had an ability at 6th level  that granted you a bonus class feat, but that class feat had to  be 4t |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.751217 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/16` | 0.740416 | class feat you have. As you continue selecting operative  archetype class feats, you continue to gain additional Hit Points  in this way. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.709193 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.696656 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |

### Query 182
- Text: Summarize **Rules Overview**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/29` | 0.926238 | **Rules Overview** |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/27` | 0.926238 | **Rules Overview** |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/54` | 0.926238 | **Rules Overview** |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/37` | 0.926238 | **Rules Overview** |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/9/Text/30` | 0.926238 | **Rules Overview** |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/15/Text/20` | 0.926238 | **Rules Overview** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/41` | 0.926238 | **Rules Overview** |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/7/Text/35` | 0.926238 | **Rules Overview** |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/7/Text/53` | 0.906238 | **Rules Overview** |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/36` | 0.906238 | **Rules Overview** |

### Query 183
- Text: Summarize **Witchwarper**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/51']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `21`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/7/Text/45` | 0.825156 | **Witchwarper** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/55` | 0.825156 | **Witchwarper** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/51` | 0.825156 | **Witchwarper** |
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
- Graph boosted count: `32`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16` | 0.791981 | Skill Feats |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.648628 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/45` | 0.610010 | SKILL FEATS 2ND |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/42` | 0.608669 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/15` | 0.608669 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/66` | 0.608669 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/58` | 0.608669 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/31` | 0.608669 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/48` | 0.608669 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.589124 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |

### Query 185
- Text: What are the requirements for **Prerequisites** Operative Dedication?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/3/Text/50']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `41`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/60` | 0.904207 | **Prerequisites** Operative Dedication |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/55` | 0.904207 | **Prerequisites** Operative Dedication |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/50` | 0.904207 | **Prerequisites** Operative Dedication |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/31` | 0.785465 | **Prerequisites** Operative Dedication, expert in any kind of  weapon or unarmed attack |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/36` | 0.771529 | **Prerequisites** Operative Dedication, expert in Perception |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/39` | 0.755639 | **Prerequisites** Soldier Dedication |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/18` | 0.755639 | **Prerequisites** Soldier Dedication |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/34` | 0.755639 | **Prerequisites** Soldier Dedication |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/65` | 0.739997 | **Prerequisites** Operative Dedication, class granting no more Hit  Points per level than 6 + your Constitution |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/45` | 0.717047 | **Prerequisites** Solarian Dedication |

### Query 186
- Text: Summarize Your Perception measures your ability to notice things, search for what's hidden, and tell whether  something about a situation is suspicious.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/0/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/2` | 0.981810 | Your Perception measures your ability to notice things, search for what's hidden, and tell whether  something about a situation is suspicious. |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/16` | 0.705412 | The ways a creature can use Perception depend on what  senses it has. The primary concepts you need to know for  understanding senses are precise senses, imprecise senses,  and the three states of det |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/23` | 0.689558 | You have a keen eye for details and always manage to  remain alert to threats around you. Your proficiency rank for  Perception increases to expert. |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.683885 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/12/Text/3` | 0.679724 | **Detection**: Observed, hidden, undetected, unnoticed **Senses**: Blinded, concealed, dazzled, deafened,  invisible |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/9` | 0.673669 | Three conditions measure the degree to which you can sense  a creature: observed, hidden, and undetected. However, the  concealed and invisible conditions can partially mask a  creature, and the unnot |
| 7 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.665447 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/31` | 0.662699 | **Failure** You detect what a deceptive creature wants you to  believe. If they're not being deceptive, you believe they're  behaving normally. |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/3/Text/7` | 0.660806 | Typically, you'll roll a Perception check to determine your  initiative—the more aware you are of your surroundings,  the more quickly you can respond. Sometimes, though, the  GM might call on you to |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/20` | 0.657069 | Anything in plain view is observed by you. If a creature takes  measures to avoid detection, such as by using Stealth to Hide,  it can become hidden or undetected instead of observed. If you |

### Query 187
- Text: What is the rule about Targeting an undetected creature is difficult. If you suspect  there's a creature around, you can pick a square and attempt  an attack. This works like targeting a hidden creature, but the  flat check and attack roll are both rolled in secret by the GM.  The GM won't tell you why you missed—whether it was due  to failing the flat check, rolling an insufficient attack roll, or  choosing the wrong square. The GM might allow you to try  targeting an undetected creature with some spells or other  abilities in a similar fashion. Undetected creatures are subject  to area effects normally.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 424-441::/page/2/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/1` | 0.989255 | Targeting an undetected creature is difficult. If you suspect  there's a creature around, you can pick a square and attempt  an attack. This works like targeting a hidden creature, but the  flat check |
| 2 | `PZO22001 Starfinder Player Core 424-441::/page/17/Text/3` | 0.887205 | A creature you're undetected by can guess which square  you're in to try targeting you. It must pick a square and  attempt an attack. This works like targeting a hidden  creature (requiring a DC 11 fl |
| 3 | `PZO22001 Starfinder Player Core 424-441::/page/1/Text/22` | 0.793652 | When targeting a hidden creature, before you roll to  determine your effect, you must attempt a DC 11 flat check.  If you fail, you don't affect the creature, though the actions  you used are still ex |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/11/Text/17` | 0.764294 | You're difficult for one or more creatures to see due to thick  fog or some other obscuring feature. You can be concealed  to some creatures but not others. While concealed, you can  still be observed |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/13/Text/23` | 0.752833 | While you're hidden from a creature, that creature knows  the space you're in but can't tell precisely where you are.  You typically become hidden by using Stealth to Hide. When  Seeking a creature us |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/2` | 0.727211 | For instance, suppose an enemy witchwarper cast  *invisibility* and then Sneaked away. You suspect that with  the witchwarper's Speed of 25 feet, they probably moved 15  feet toward an open door. You |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/25` | 0.722252 | **Success** Any undetected creature you succeeded against  becomes hidden from you instead of undetected, and  any hidden creature you succeeded against becomes  observed by you. You learn the locatio |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/17` | 0.719247 | Some effects require you to choose specific targets.  Targeting can be difficult or impossible if your chosen  creature is undetected by you, if the creature doesn't match  restrictions on who you can |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/17` | 0.714437 | The GM attempts a single secret Perception check for  you and compares the result to the Stealth DCs of any  undetected or hidden creatures in the area, or the DC to  detect each object in the area (a |
| 10 | `PZO22001 Starfinder Player Core 424-441::/page/2/Text/6` | 0.713806 | A concealed creature is in mist, within dim light, or amid  something else that obscures sight but isn't a physical  barrier. When you target a creature that's concealed  from you, you must attempt a |

### Query 188
- Text: What are the requirements for **BASIC EPIPHANY** **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/33']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/33` | 0.778248 | **BASIC EPIPHANY** **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/17` | 0.600931 | **ADVANCED GUNNER** **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/25` | 0.600061 | **ADVANCED SOLDIER TRAINING** **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/31` | 0.582034 | **ADVANCED STELLAR ATTUNEMENT** **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/65` | 0.577548 | **Prerequisites** Operative Dedication, class granting no more Hit  Points per level than 6 + your Constitution |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/5/SectionHeader/31` | 0.577155 | **SUPPRESSING FIRE** **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/36` | 0.571675 | **ADAPTIVE TALENT** **FEAT 6** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/40` | 0.571539 | 6TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/4/SectionHeader/37` | 0.566190 | **SOLAR FLARE** **FEAT 6** |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/10` | 0.565589 | **ADVANCED LEADERSHIP** **FEAT 6** |

### Query 189
- Text: Summarize ENVOY
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `49`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/1` | 0.837912 | ENVOY |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/1/SectionHeader/1` | 0.817912 | ENVOY |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/43` | 0.758983 | ENVOY FEATS |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/14` | 0.758983 | ENVOY FEATS |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/39` | 0.745760 | **ENVOY** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/46` | 0.745760 | **ENVOY** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/4` | 0.745760 | **ENVOY** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/3` | 0.745760 | **ENVOY** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/43` | 0.745760 | **ENVOY** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/9` | 0.745760 | **ENVOY** |

### Query 190
- Text: Summarize if you're using an imprecise sense or if an effect (such as  *invisibility*) prevents the subject from being observed.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/3/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `29`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/23` | 0.958307 | if you're using an imprecise sense or if an effect (such as  *invisibility*) prevents the subject from being observed. |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/89` | 0.719735 | strong opinion about you. **Invisible:** Creatures can't see you. **Observed:** You're in plain view. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/62` | 0.694433 | **Concealed:** Fog or similar obscuration makes you difficult  to see and target. |
| 4 | `PZO22001 Starfinder Player Core 424-441::/page/12/Text/3` | 0.660579 | **Detection**: Observed, hidden, undetected, unnoticed **Senses**: Blinded, concealed, dazzled, deafened,  invisible |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/0/Text/21` | 0.652498 | Average hearing is an imprecise sense—it can't detect the  full range of detail that a precise sense can. You can usually  sense a creature automatically with an imprecise sense, but  it has the hidde |
| 6 | `PZO22001 Starfinder Player Core 424-441::/page/14/Text/21` | 0.647642 | have another precise sense besides sight, you might be able  to observe a creature or object using that sense instead. You  can observe a creature with only your precise senses. When  Seeking a creatu |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/59` | 0.647221 | **Blinded:** You're unable to see. |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/103` | 0.628206 | **Suppressed: **You're in a dangerous situation that forces |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/106` | 0.627845 | **Undetected:** A creature you're undetected by doesn't |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/16/Text/18` | 0.626438 | an effect followed by an interval in parentheses. When you  reach a given stage of an affliction, you're subjected to the  effects listed for that stage. |

### Query 191
- Text: What is the rule about Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the dedication. There are also class archetypes that can  modify your class's abilities as soon as 1st level. You can  never have more than one class archetype.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/21` | 0.977474 | Some archetype feats in other books have the skill trait,  allowing you to take them in place of a skill feat rather than  a class feat. A skill feat still counts to satisfy the requirement  of the de |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/11` | 0.819417 | Some archetypes include a list of "Additional Feats" that  appear in other sources. The list includes each feat's level,  which might be different than normal when gained from the  archetype. You can |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/13` | 0.802655 | Sometimes an archetype feat lets you select another feat,  such as a class feat of a lower level. You must always meet  any prerequisites of the feat you gain in this way. These  always count as only |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/9` | 0.800917 | Most archetypes in this book have the multiclass trait.  These allow you to diversify your training into another  class's specialties. You can't select a multiclass archetype's  dedication feat if you |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/4` | 0.784502 | You gain an archetype by selecting archetype feats instead  of your normal feats. First, find the archetype that best  fits your character concept. Then select that archetype's  dedication feat, using |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/5` | 0.781268 | An archetype feat is subject to any restrictions on the class  feat it replaces. For example, if you had an ability at 6th level  that granted you a bonus class feat, but that class feat had to  be 4t |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/7` | 0.760833 | Each archetype's dedication feat represents your character's  dedicated effort learning a new set of abilities, making it  impossible to split your focus and pursue another archetype  at the same time |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.714134 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 9 | `PZO22001 Starfinder Player Core 424-441::/page/9/Text/22` | 0.700338 | For instance, you can't replace a skill feat you chose at 2nd  level for a 4th-level one, or for one that requires prerequisites  you didn't meet at the time you took the original feat. If you  don't |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/7` | 0.695251 | **Archetypes** on page 174 gives you thematic options  that allow you to further customize your character's  abilities. Though these rules are not recommended for  beginners, the archetypes in this bo |

### Query 192
- Text: What is the rule about Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. These feats share their name with the  archetype; for instance, the witchwarper's master spellcasting  feat is called Master Witchwarper Spellcasting. All spell slots  you gain from spellcasting archetypes are subject to the  restrictions within the archetype. For instance, the mystic  archetype allows you to pick a connection when you take  its dedication feat. If you pick a connection granting divine  spells, the archetype then grants you spell slots you can use  only to cast divine spells you prepare as a mystic, even if you  are a witchwarper with occult spells in your repertoire.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/0/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `33`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/16` | 0.988128 | Spellcasting archetypes always grant the ability to cast  cantrips in their dedication, and then they have a basic  spellcasting feat, an expert spellcasting feat, and a master  spellcasting feat. The |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/10` | 0.778843 | You cast spells like a mystic and gain the Cast a Spell  activity. You gain a spell repertoire with two common cantrips  from the spell list granted by your connection, from the spells  granted by you |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/10` | 0.771622 | You cast spells like a witchwarper. You gain access to the Cast  a Spell activity. You gain a spell repertoire with two common  cantrips from the spell list associated with your paradox, from  the spe |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/15` | 0.744817 | Some archetypes grant you a substantial degree of  spellcasting, albeit delayed compared to a character from a  spellcasting class. The spellcasting ability from a spellcasting  archetype also allows |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/21` | 0.737542 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the mystic archetype,  add a spell of the appropriate spell rank to your repertoire: a  common |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/29` | 0.711981 | You gain the basic spellcasting benefits (page 174). Each time  you gain a spell slot of a new rank from the witchwarper  archetype, add a spell of the appropriate spell rank to your  repertoire: a co |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/17` | 0.681703 | **Basic Spellcasting Feat:** Usually available at 4th level,  these feats grant a 1st-rank spell slot. At 6th level, they  grant you a 2nd-rank spell slot, and if you have a spell  repertoire, you can |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/19` | 0.676586 | **Master Spellcasting Feat:** Usually found at 18th level, these  feats make you a master in spell attack modifiers and spell  DCs and grant you a 7th-rank spell slot. If you have a spell  repertoire, |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/44` | 0.676372 | **Prerequisites** Basic Witchwarper Spellcasting; master in Arcana  or Occultism, depending on paradox |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/5` | 0.672327 | An archetype feat is subject to any restrictions on the class  feat it replaces. For example, if you had an ability at 6th level  that granted you a bonus class feat, but that class feat had to  be 4t |

### Query 193
- Text: What is the rule about ACTIONS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `30`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/SectionHeader/1` | 0.747995 | ACTIONS |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/17/Text/39` | 0.667915 | Actions |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/11` | 0.660043 | These rules clarify some of the specifics of using actions. |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/1` | 0.643445 | BASIC ACTIONS |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/2/SectionHeader/6` | 0.643445 | BASIC ACTIONS |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/10` | 0.609055 | **IN-DEPTH ACTION RULES** |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/1/SectionHeader/5` | 0.602902 | GAINING AND LOSING  ACTIONS |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/5/Text/61` | 0.592595 | **Actions** |
| 9 | `PZO22001 Starfinder Player Core 406-423::/page/3/Text/48` | 0.592595 | **Actions** |
| 10 | `PZO22001 Starfinder Player Core 406-423::/page/11/Text/34` | 0.592595 | **Actions** |

### Query 194
- Text: What is the rule about You gain a 1st- or 2nd-level envoy feat of your choice.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `17`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/35` | 0.889381 | You gain a 1st- or 2nd-level envoy feat of your choice. |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/19` | 0.769455 | You gain a 1st- or 2nd-level soldier feat. |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/26` | 0.730895 | You gain a 1st- or 2nd-level mystic feat. |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/51` | 0.729038 | You gain a 1st- or 2nd-level operative feat. |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/14` | 0.722403 | You gain one envoy feat. For the purpose of meeting its  prerequisites, your envoy level is equal to half your character  level. |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/15` | 0.706331 | **Special** You can select this feat more than once. Each time  you select it, you gain another envoy feat. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/15` | 0.696639 | At every level that you gain an envoy feat, you can select  one of the following feats. You must satisfy any prerequisites  before selecting the feat. |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/20` | 0.687376 | You gain a 1st- or 2nd-level solarian feat. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/444` | 0.678153 | Envoy feat, skill feat, skill increase |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/440` | 0.678153 | Envoy feat, skill feat, skill increase |

### Query 195
- Text: Summarize **Navasi**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `16`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/6` | 0.828894 | **Navasi** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/31` | 0.594164 | **Obozaya** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/7` | 0.592998 | **Navasi**, the human envoy, is a former space  pirate with a heart of gold. She's got a witty  remark for every occasion and a bullet for  anyone who would hurt one of her friends. |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7` | 0.583887 | **HIT POINTS** |
| 5 | `PZO22001 Starfinder Player Core 424-441::/page/6/SectionHeader/15` | 0.583530 | **ANALYZE ENVIRONMENT ** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/10` | 0.581086 | **Feats** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/44` | 0.581061 | **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/56` | 0.581061 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/67` | 0.581061 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/34` | 0.575493 | **Operative ** |

### Query 196
- Text: What are the requirements for **DOWN TO THE WIRE **[reaction] **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/34` | 0.815001 | **DOWN TO THE WIRE **[reaction] **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44` | 0.653881 | **READY TO ROLL **[free-action] **FEAT 14** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.615150 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.610072 | **WATCH OUT **[reaction] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49` | 0.608143 | **YOU CAN DO IT **[one-action] **FEAT 14** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.600325 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/33` | 0.589256 | 14TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/26` | 0.585827 | **QUIP **[reaction] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/19` | 0.583365 | **NOT IN THE FACE **[reaction] **FEAT 4** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.573476 | **READY ARMS! **[one-action]** TO **[two-actions] |

### Query 197
- Text: What is the rule about These icons appear in stat blocks as shorthand for each  type of action. As a player, you'll usually see the icon in  an action's header (such as in a basic action, skill action,  feat, or spell). In a creature stat block, or a feat that  gives you a new action in addition to other benefits, the  icon will appear in the running text. For examples, see  the formatting of rules on page 15.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 406-423::/page/0/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `21`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/13` | 0.985800 | These icons appear in stat blocks as shorthand for each  type of action. As a player, you'll usually see the icon in  an action's header (such as in a basic action, skill action,  feat, or spell). In |
| 2 | `PZO22001 Starfinder Player Core 406-423::/page/16/Text/5` | 0.675333 | Whether appearing in a spell, as an item, or within a creature's  stat block, afflictions appear in the following format. |
| 3 | `PZO22001 Starfinder Player Core 406-423::/page/13/Text/58` | 0.625913 | Some effects apply conditions to a creature or item. These change your state of being in some way. Conditions are  persistent, lasting until the stated duration ends, the condition is removed, or term |
| 4 | `PZO22001 Starfinder Player Core 406-423::/page/1/Text/4` | 0.606410 | Sometimes you need to attempt something not already  covered by defined actions in the game. When this happens,  the rules tell you how many actions you need to spend as  well as any traits your actio |
| 5 | `PZO22001 Starfinder Player Core 406-423::/page/6/Text/11` | 0.604972 | Most characters and monsters have a Speed statistic that  indicates how quickly they can move on a solid surface. This  statistic is referred to as land Speed when it's necessary to  differentiate it |
| 6 | `PZO22001 Starfinder Player Core 406-423::/page/12/Text/7` | 0.603347 | Most effects are discrete, creating an instantaneous effect  when you let the GM know what actions you're going to use.  Firing a gun, moving to a new space, or taking something  out of your pack all |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/0/Text/6` | 0.601302 | You'll need to track your actions carefully in an encounter. At  the start of each turn you take in an encounter, you regain 3  actions and 1 reaction to spend that round. (Regaining your  actions is |
| 8 | `PZO22001 Starfinder Player Core 406-423::/page/16/Text/7` | 0.600141 | The affliction's name is given first, followed by its traits in  parentheses—including the trait for the type of affliction  (curse, disease, poison, and so forth). If the affliction needs  to have a |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.596350 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.595143 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |

### Query 198
- Text: What are the requirements for **Prerequisites** Wisdom +2?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `29`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/8` | 0.897407 | **Prerequisites** Wisdom +2 |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/6/Text/8` | 0.754266 | **Prerequisites** Intelligence +2 |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/1/Text/29` | 0.733181 | **Prerequisites** Charisma +2 |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/3/Text/13` | 0.721798 | **Prerequisites** Dexterity +2 |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/12` | 0.684555 | **Prerequisites** Constitution +2 |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/4/Text/13` | 0.613861 | **Prerequisites** Strength +2 You gain the stellar attunement class feature (page 140), but |
| 7 | `PZO22001 Starfinder Player Core 406-423::/page/10/TableCell/309` | 0.569933 | +2 to AC, Reflex, Stealth |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/58` | 0.569240 | Trained in a number of additional  skills equal to 6 plus your Intelligence  modifier |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/26` | 0.564008 | You gain a 1st- or 2nd-level mystic feat. |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/5/Text/45` | 0.563073 | Your proficiency rank in Fortitude saves increases to master. |

### Query 199
- Text: What are the requirements for **EXPERT MYSTIC SPELLCASTING** **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `32`

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/43` | 0.818416 | **EXPERT MYSTIC SPELLCASTING** **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 174-181::/page/6/SectionHeader/41` | 0.719871 | **EXPERT WITCHWARPER SPELLCASTING** **FEAT 12** |
| 3 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/51` | 0.690623 | **Prerequisites** Expert Mystic Spellcasting; legendary in  connection skill |
| 4 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/48` | 0.645479 | **MASTER MYSTIC SPELLCASTING** **FEAT 18** |
| 5 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/33` | 0.634985 | **MASTER SPY** **FEAT 12** |
| 6 | `PZO22001 Starfinder Player Core 174-181::/page/3/SectionHeader/28` | 0.624809 | **GUN EXPERT** **FEAT 12** |
| 7 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/17` | 0.618182 | **BASIC MYSTIC SPELLCASTING** **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 174-181::/page/2/Text/46` | 0.615210 | **Prerequisites** Basic Mystic Spellcasting; master in  connection skill |
| 9 | `PZO22001 Starfinder Player Core 174-181::/page/2/SectionHeader/41` | 0.598641 | **Prerequisites** Basic Mystic Spellcasting |
| 10 | `PZO22001 Starfinder Player Core 174-181::/page/0/Text/18` | 0.585940 | **Expert Spellcasting Feat:** Typically taken at 12th level,  these feats make you an expert in spell attack modifiers  and spell DCs and grant you a 4th-rank spell slot. If you  have a spell repertoi |
