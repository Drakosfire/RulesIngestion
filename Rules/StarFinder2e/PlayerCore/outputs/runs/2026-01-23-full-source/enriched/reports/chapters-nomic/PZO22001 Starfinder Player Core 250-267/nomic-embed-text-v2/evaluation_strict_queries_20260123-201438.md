# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `1652`
- Query count: `113`
- Evaluated queries: `113`
- Coverage: `1.0000`
- MRR: `0.7751`
- hit@1: `0.6903`
- hit@3: `0.8407`
- hit@5: `0.8938`
- hit@10: `0.9381`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

## Timings (ms)
- Embedding (chunks): `17406`
- Embedding (queries): `2702`
- Evaluation (strict): `262`
- Evaluation (expanded): `0`
- Total: `24901`

### Timing Estimates (ms)
- Evaluation (strict): `418`
- Evaluation (expanded): `None`
- Total: `20526`

## Query Details
### Query 0
- Text: Summarize SHIELDS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 250-267::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 250-267::/page/13/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/1` | 0.915132 | SHIELDS |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/SectionHeader/1` | 0.823940 | **SHIELDS** |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/13/Text/10` | 0.813244 | **Shields** |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/11/Text/43` | 0.771244 | **Shields** |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/7/Text/10` | 0.771244 | **Shields** |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/9/Text/49` | 0.771244 | **Shields** |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/34` | 0.771244 | **Shields** |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/5/Text/34` | 0.771244 | **Shields** |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/28` | 0.771244 | **Shields** |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/SectionHeader/11` | 0.751808 | SHIELD DESCRIPTIONS |

### Query 1
- Text: What is the rule about A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only  if they use an action to Raise a Shield. This action grants the shield's bonus to AC as a circumstance  bonus until their next turn starts. A shield's Speed penalty applies whenever your character is holding  the shield, whether they have raised it or not.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/2', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/10', 'PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 1.002907 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/10` | 0.815304 | A shield grants a circumstance bonus to AC, but only when  the shield is raised. This requires using the Raise a Shield  action, found on page 411. |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/3` | 0.782090 | 1 Gaining a shield's circumstance bonus to AC requires using the Raise a Shield action (found on page 411). |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/8` | 0.698628 | bonus to your AC, the shield upgrade emits an inertial  dampening barrier, and you automatically Raise a Shield.  You can't Raise a Shield installed as a weapon upgrade any  other way. If you use the |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/4` | 0.687926 | Raise a Shield is the action most commonly used with shields.  Most shields must be held in one hand, so you can't hold  anything with that hand and Raise a Shield, and you lose its  benefits if that |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/6` | 0.651673 | If you have access to the Shield Block reaction (from your  class or from a feat), you can use it while Raising your Shield  to reduce the damage you take by an amount equal to the  shield's Hardness. |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/5` | 0.614648 | When you have a riot shield or mobile bulwark raised,  you can use the Take Cover action (page 410) to increase the  circumstance bonus to AC to +4. This lasts until the shield is  no longer raised or |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/12` | 0.605977 | Whenever a shield takes damage, the amount of damage it  takes is reduced by this amount. This number is particularly  relevant for shields because of the Shield Block feat (page  228). The rules for |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/21` | 0.595184 | **Compact:** You can Raise a Shield with your compact shield  as long as you have that hand free or are holding, but not  wielding, a light object in that hand. |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/23` | 0.585708 | **Installed:** Some shields aren't held but are installed  as armor or weapon upgrades. You can Raise a Shield  installed as an armor upgrade as normal. Shields can be  installed only into weapons wit |

### Query 2
- Text: What is the rule about Raise a Shield is the action most commonly used with shields.  Most shields must be held in one hand, so you can't hold  anything with that hand and Raise a Shield, and you lose its  benefits if that hand is no longer free. A compact shield and an  irising shield don't take up your hand, so you can Raise a Shield  with a compact shield or irising shield if the hand is free or if it's  holding a light object that's not a weapon. You lose the benefits  of Raise a Shield if that hand no longer meets these conditions.  Irising shields and phase shields only count as a shield when  deployed, as noted in their description. You can't Raise a Shield  with an irising shield or phase shield unless it's deployed.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/4', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/21', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/4` | 1.016789 | Raise a Shield is the action most commonly used with shields.  Most shields must be held in one hand, so you can't hold  anything with that hand and Raise a Shield, and you lose its  benefits if that |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/21` | 0.797293 | **Compact:** You can Raise a Shield with your compact shield  as long as you have that hand free or are holding, but not  wielding, a light object in that hand. |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/10` | 0.724215 | A shield grants a circumstance bonus to AC, but only when  the shield is raised. This requires using the Raise a Shield  action, found on page 411. |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/8` | 0.676389 | bonus to your AC, the shield upgrade emits an inertial  dampening barrier, and you automatically Raise a Shield.  You can't Raise a Shield installed as a weapon upgrade any  other way. If you use the |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 0.676102 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/23` | 0.650625 | **Installed:** Some shields aren't held but are installed  as armor or weapon upgrades. You can Raise a Shield  installed as an armor upgrade as normal. Shields can be  installed only into weapons wit |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/9` | 0.639223 | **Retractable:** This shield can collapse into a smaller form  attached to an armguard, gauntlet, glove, or jewelry for  ease of travel and to free up hands. You can use an Interact  action to deploy |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/3` | 0.619620 | 1 Gaining a shield's circumstance bonus to AC requires using the Raise a Shield action (found on page 411). |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/6` | 0.584889 | If you have access to the Shield Block reaction (from your  class or from a feat), you can use it while Raising your Shield  to reduce the damage you take by an amount equal to the  shield's Hardness. |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/22` | 0.564824 | **Hefty:** This shield is so heavy that raising it takes more  effort. Raising a Shield with the hefty trait is a 2-action  activity unless your Strength modifier equals or exceeds  the number with th |

### Query 3
- Text: What is the rule about When you have a riot shield or mobile bulwark raised,  you can use the Take Cover action (page 410) to increase the  circumstance bonus to AC to +4. This lasts until the shield is  no longer raised or until any of the normal conditions that  end Take Cover occur, whichever comes first. If you would  provide lesser cover against an attack, having your riot shield  or mobile bulwark raised provides standard cover against  it (and other creatures can Take Cover as normal using the  cover from your shield).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/5', 'PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/4', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/5` | 1.005428 | When you have a riot shield or mobile bulwark raised,  you can use the Take Cover action (page 410) to increase the  circumstance bonus to AC to +4. This lasts until the shield is  no longer raised or |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/4` | 0.877625 | 2 Getting the higher bonus for a mobile bulwark or riot shield requires using the Take Cover action (page 410) while the  shield is raised. |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/10` | 0.731778 | A shield grants a circumstance bonus to AC, but only when  the shield is raised. This requires using the Raise a Shield  action, found on page 411. |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/3` | 0.679985 | 1 Gaining a shield's circumstance bonus to AC requires using the Raise a Shield action (found on page 411). |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 0.643774 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/8` | 0.599082 | bonus to your AC, the shield upgrade emits an inertial  dampening barrier, and you automatically Raise a Shield.  You can't Raise a Shield installed as a weapon upgrade any  other way. If you use the |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/4` | 0.593446 | Raise a Shield is the action most commonly used with shields.  Most shields must be held in one hand, so you can't hold  anything with that hand and Raise a Shield, and you lose its  benefits if that |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/6` | 0.546937 | If you have access to the Shield Block reaction (from your  class or from a feat), you can use it while Raising your Shield  to reduce the damage you take by an amount equal to the  shield's Hardness. |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/21` | 0.504005 | **Compact:** You can Raise a Shield with your compact shield  as long as you have that hand free or are holding, but not  wielding, a light object in that hand. |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/23` | 0.490521 | **Installed:** Some shields aren't held but are installed  as armor or weapon upgrades. You can Raise a Shield  installed as an armor upgrade as normal. Shields can be  installed only into weapons wit |

### Query 4
- Text: What is the rule about If you have access to the Shield Block reaction (from your  class or from a feat), you can use it while Raising your Shield  to reduce the damage you take by an amount equal to the  shield's Hardness. Both you and the shield then take any  remaining damage.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/6', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/12', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/6` | 0.990183 | If you have access to the Shield Block reaction (from your  class or from a feat), you can use it while Raising your Shield  to reduce the damage you take by an amount equal to the  shield's Hardness. |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/12` | 0.742019 | Whenever a shield takes damage, the amount of damage it  takes is reduced by this amount. This number is particularly  relevant for shields because of the Shield Block feat (page  228). The rules for |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 0.719696 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/4` | 0.636303 | Raise a Shield is the action most commonly used with shields.  Most shields must be held in one hand, so you can't hold  anything with that hand and Raise a Shield, and you lose its  benefits if that |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/8` | 0.635323 | bonus to your AC, the shield upgrade emits an inertial  dampening barrier, and you automatically Raise a Shield.  You can't Raise a Shield installed as a weapon upgrade any  other way. If you use the |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/10` | 0.619484 | A shield grants a circumstance bonus to AC, but only when  the shield is raised. This requires using the Raise a Shield  action, found on page 411. |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/14` | 0.576584 | This column lists the shield's Hit Points (HP) and Broken  Threshold (BT). These measure how much damage the shield  can take before it's destroyed (its total HP) and how much it  can take before bein |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/3` | 0.564107 | 1 Gaining a shield's circumstance bonus to AC requires using the Raise a Shield action (found on page 411). |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/5` | 0.546198 | When you have a riot shield or mobile bulwark raised,  you can use the Take Cover action (page 410) to increase the  circumstance bonus to AC to +4. This lasts until the shield is  no longer raised or |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/21` | 0.546106 | **Compact:** You can Raise a Shield with your compact shield  as long as you have that hand free or are holding, but not  wielding, a light object in that hand. |

### Query 5
- Text: Summarize SHIELD STATISTICS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/7', 'PZO22001 Starfinder Player Core 250-267::/page/9/Text/49', 'PZO22001 Starfinder Player Core 250-267::/page/7/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/7` | 1.002266 | SHIELD STATISTICS |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/9/Text/49` | 0.675088 | **Shields** |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/7/Text/10` | 0.675088 | **Shields** |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/34` | 0.633088 | **Shields** |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/5/Text/34` | 0.633088 | **Shields** |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/28` | 0.633088 | **Shields** |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/13/Text/10` | 0.633088 | **Shields** |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/11/Text/43` | 0.633088 | **Shields** |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/SectionHeader/11` | 0.625981 | SHIELD DESCRIPTIONS |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/1` | 0.623332 | SHIELDS |

### Query 6
- Text: Summarize Shields have statistics that follow the same rules as armor:  Price, Speed Penalty, and Bulk. See page 245 for the rules  for those statistics. Their other statistics are described here.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/8', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/12', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/8` | 1.043606 | Shields have statistics that follow the same rules as armor:  Price, Speed Penalty, and Bulk. See page 245 for the rules  for those statistics. Their other statistics are described here. |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/12` | 0.670105 | Whenever a shield takes damage, the amount of damage it  takes is reduced by this amount. This number is particularly  relevant for shields because of the Shield Block feat (page  228). The rules for |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 0.621301 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/7` | 0.585885 | SHIELD STATISTICS |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/18` | 0.546579 | Shields can have the following traits. |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/14` | 0.544086 | This column lists the shield's Hit Points (HP) and Broken  Threshold (BT). These measure how much damage the shield  can take before it's destroyed (its total HP) and how much it  can take before bein |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/23` | 0.536949 | **Installed:** Some shields aren't held but are installed  as armor or weapon upgrades. You can Raise a Shield  installed as an armor upgrade as normal. Shields can be  installed only into weapons wit |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/1/Table/2` | 0.535849 | ShieldLevelPriceAC Bonus1Speed PenaltyBulkHardnessHP (BT)TraitsCarbon shield, commercial025+2—1520 (10)AnalogCompact shield, commercial015+1—L48 (4)Analog, compactDeflecting field, commercial010+1——24 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/16` | 0.513170 | A shield can be used as a martial weapon for attacks, using  the statistics listed for a shield bash on the Martial Melee  Weapons table (page 264). The shield bash is an option only  for shields that |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/7` | 0.511434 | 1 Total value does not include the price of the base commercial shield. |

### Query 7
- Text: What is the rule about AC BONUS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/9', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/624', 'PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/9` | 0.838019 | AC BONUS |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/624` | 0.748819 | AC Bonus1 |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/3` | 0.598809 | 1 Gaining a shield's circumstance bonus to AC requires using the Raise a Shield action (found on page 411). |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/10` | 0.536457 | A shield grants a circumstance bonus to AC, but only when  the shield is raised. This requires using the Raise a Shield  action, found on page 411. |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/8` | 0.488212 | bonus to your AC, the shield upgrade emits an inertial  dampening barrier, and you automatically Raise a Shield.  You can't Raise a Shield installed as a weapon upgrade any  other way. If you use the |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 0.438117 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/5` | 0.397185 | When you have a riot shield or mobile bulwark raised,  you can use the Take Cover action (page 410) to increase the  circumstance bonus to AC to +4. This lasts until the shield is  no longer raised or |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/6/Text/18` | 0.367073 | **Parry:** This weapon can be used defensively to block  attacks. While wielding this weapon, if your proficiency  with it is trained or better, you can spend a single action to  position your weapon |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/12` | 0.363918 | When the result of your attack roll with a weapon or unarmed  attack equals or exceeds your target's AC, you hit your target!  Roll the weapon or unarmed attack's damage die and add  the relevant modi |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/8/Text/21` | 0.362660 | **Axe:** Choose one creature adjacent to the initial target and  within reach. If its AC is lower than your attack roll result for  the critical hit, you deal damage to that creature equal to the  res |

### Query 8
- Text: What is the rule about A shield grants a circumstance bonus to AC, but only when  the shield is raised. This requires using the Raise a Shield  action, found on page 411.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/10', 'PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/3', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/10` | 1.011764 | A shield grants a circumstance bonus to AC, but only when  the shield is raised. This requires using the Raise a Shield  action, found on page 411. |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/3` | 0.938695 | 1 Gaining a shield's circumstance bonus to AC requires using the Raise a Shield action (found on page 411). |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 0.814879 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/8` | 0.765869 | bonus to your AC, the shield upgrade emits an inertial  dampening barrier, and you automatically Raise a Shield.  You can't Raise a Shield installed as a weapon upgrade any  other way. If you use the |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/4` | 0.694014 | Raise a Shield is the action most commonly used with shields.  Most shields must be held in one hand, so you can't hold  anything with that hand and Raise a Shield, and you lose its  benefits if that |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/5` | 0.672312 | When you have a riot shield or mobile bulwark raised,  you can use the Take Cover action (page 410) to increase the  circumstance bonus to AC to +4. This lasts until the shield is  no longer raised or |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/4` | 0.604663 | 2 Getting the higher bonus for a mobile bulwark or riot shield requires using the Take Cover action (page 410) while the  shield is raised. |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/6` | 0.594116 | If you have access to the Shield Block reaction (from your  class or from a feat), you can use it while Raising your Shield  to reduce the damage you take by an amount equal to the  shield's Hardness. |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/21` | 0.576193 | **Compact:** You can Raise a Shield with your compact shield  as long as you have that hand free or are holding, but not  wielding, a light object in that hand. |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/23` | 0.566517 | **Installed:** Some shields aren't held but are installed  as armor or weapon upgrades. You can Raise a Shield  installed as an armor upgrade as normal. Shields can be  installed only into weapons wit |

### Query 9
- Text: Summarize HARDNESS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/11', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/697', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/627']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/11` | 0.948501 | HARDNESS |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/697` | 0.788844 | Hardness |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/627` | 0.788844 | Hardness |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/12` | 0.528008 | Whenever a shield takes damage, the amount of damage it  takes is reduced by this amount. This number is particularly  relevant for shields because of the Shield Block feat (page  228). The rules for |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/22` | 0.387632 | **Hefty:** This shield is so heavy that raising it takes more  effort. Raising a Shield with the hefty trait is a 2-action  activity unless your Strength modifier equals or exceeds  the number with th |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/14` | 0.356432 | This column lists the shield's Hit Points (HP) and Broken  Threshold (BT). These measure how much damage the shield  can take before it's destroyed (its total HP) and how much it  can take before bein |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/6/Text/9` | 0.334246 | **Forceful:** This weapon becomes more dangerous as you  build momentum. When you attack with it more than once  on your turn, the second attack gains a circumstance bonus  to damage equal to the numb |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/1/Table/6` | 0.325522 | GradeLevelUpgrade PriceTotal Value1HardnessHPBTCommercial0—————Tactical5+750 credits750 credits+3+46+23Advanced8+2,250 credits3,000 credits+3+56+28Superior11+6,000 credits9,000 credits+3+68+34Elite14+ |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/Table/2` | 0.322888 | ShieldLevelPriceAC Bonus1Speed PenaltyBulkHardnessHP (BT)TraitsCarbon shield, commercial025+2—1520 (10)AnalogCompact shield, commercial015+1—L48 (4)Analog, compactDeflecting field, commercial010+1——24 |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/8/Text/22` | 0.315852 | **Brawling:** The target must succeed at a Fortitude save against  your class DC or be slowed 1 until the end of your next turn. |

### Query 10
- Text: What is the rule about Whenever a shield takes damage, the amount of damage it  takes is reduced by this amount. This number is particularly  relevant for shields because of the Shield Block feat (page  228). The rules for Hardness appear on page 236.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/12', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/6', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/12` | 1.010400 | Whenever a shield takes damage, the amount of damage it  takes is reduced by this amount. This number is particularly  relevant for shields because of the Shield Block feat (page  228). The rules for |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/6` | 0.700682 | If you have access to the Shield Block reaction (from your  class or from a feat), you can use it while Raising your Shield  to reduce the damage you take by an amount equal to the  shield's Hardness. |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/14` | 0.669725 | This column lists the shield's Hit Points (HP) and Broken  Threshold (BT). These measure how much damage the shield  can take before it's destroyed (its total HP) and how much it  can take before bein |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/8` | 0.611432 | Shields have statistics that follow the same rules as armor:  Price, Speed Penalty, and Bulk. See page 245 for the rules  for those statistics. Their other statistics are described here. |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 0.584553 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/22` | 0.526338 | **Hefty:** This shield is so heavy that raising it takes more  effort. Raising a Shield with the hefty trait is a 2-action  activity unless your Strength modifier equals or exceeds  the number with th |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/9/Text/15` | 0.514166 | **Shield:** You knock the target back from you 5 feet. This is  forced movement (page 414). |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/16` | 0.501190 | A shield can be used as a martial weapon for attacks, using  the statistics listed for a shield bash on the Martial Melee  Weapons table (page 264). The shield bash is an option only  for shields that |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/20` | 0.499510 | This entry gives the weapon's Bulk. A weapon's Bulk is  increased or decreased if it's sized for creatures that aren't  Small or Medium size, following the rules on page 235. |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/5/Text/3` | 0.484663 | This indicates how much ammunition is consumed with each  ranged Strike you make with the weapon. Anytime the weapon  is fired, the ammunition in its magazine is lowered by the  number indicated. Othe |

### Query 11
- Text: Summarize HP (BT)
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/13']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/628', 'PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/13', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/698']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/628` | 0.945073 | HP (BT) |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/13` | 0.945073 | HP (BT) |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/698` | 0.683690 | HP |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/699` | 0.571162 | BT |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/14` | 0.531955 | This column lists the shield's Hit Points (HP) and Broken  Threshold (BT). These measure how much damage the shield  can take before it's destroyed (its total HP) and how much it  can take before bein |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/Table/2` | 0.441034 | ShieldLevelPriceAC Bonus1Speed PenaltyBulkHardnessHP (BT)TraitsCarbon shield, commercial025+2—1520 (10)AnalogCompact shield, commercial015+1—L48 (4)Analog, compactDeflecting field, commercial010+1——24 |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/Table/6` | 0.440628 | GradeLevelUpgrade PriceTotal Value1HardnessHPBTCommercial0—————Tactical5+750 credits750 credits+3+46+23Advanced8+2,250 credits3,000 credits+3+56+28Superior11+6,000 credits9,000 credits+3+68+34Elite14+ |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/101` | 0.310336 | Agile, finesse, powered, tech, versatile P |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/110` | 0.310336 | Agile, finesse, powered, tech, versatile P |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/329` | 0.306605 | Battery, commercial Battery, tactical |

### Query 12
- Text: What is the rule about This column lists the shield's Hit Points (HP) and Broken  Threshold (BT). These measure how much damage the shield  can take before it's destroyed (its total HP) and how much it  can take before being broken and unusable (its BT). These  matter primarily for the Shield Block reaction.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/14', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/12', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/14` | 0.993303 | This column lists the shield's Hit Points (HP) and Broken  Threshold (BT). These measure how much damage the shield  can take before it's destroyed (its total HP) and how much it  can take before bein |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/12` | 0.720187 | Whenever a shield takes damage, the amount of damage it  takes is reduced by this amount. This number is particularly  relevant for shields because of the Shield Block feat (page  228). The rules for |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/6` | 0.623049 | If you have access to the Shield Block reaction (from your  class or from a feat), you can use it while Raising your Shield  to reduce the damage you take by an amount equal to the  shield's Hardness. |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/8` | 0.555748 | Shields have statistics that follow the same rules as armor:  Price, Speed Penalty, and Bulk. See page 245 for the rules  for those statistics. Their other statistics are described here. |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/1/Table/2` | 0.509506 | ShieldLevelPriceAC Bonus1Speed PenaltyBulkHardnessHP (BT)TraitsCarbon shield, commercial025+2—1520 (10)AnalogCompact shield, commercial015+1—L48 (4)Analog, compactDeflecting field, commercial010+1——24 |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 0.500314 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/12` | 0.481469 | When the result of your attack roll with a weapon or unarmed  attack equals or exceeds your target's AC, you hit your target!  Roll the weapon or unarmed attack's damage die and add  the relevant modi |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/16` | 0.472908 | A shield can be used as a martial weapon for attacks, using  the statistics listed for a shield bash on the Martial Melee  Weapons table (page 264). The shield bash is an option only  for shields that |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/22` | 0.464581 | **Hefty:** This shield is so heavy that raising it takes more  effort. Raising a Shield with the hefty trait is a 2-action  activity unless your Strength modifier equals or exceeds  the number with th |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/4` | 0.459822 | Raise a Shield is the action most commonly used with shields.  Most shields must be held in one hand, so you can't hold  anything with that hand and Raise a Shield, and you lose its  benefits if that |

### Query 13
- Text: What is the rule about ATTACKING WITH A  SHIELD?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/15', 'PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/15` | 0.895483 | ATTACKING WITH A  SHIELD |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/1` | 0.627401 | SHIELDS |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/4` | 0.592653 | Raise a Shield is the action most commonly used with shields.  Most shields must be held in one hand, so you can't hold  anything with that hand and Raise a Shield, and you lose its  benefits if that |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 0.558260 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/16` | 0.536420 | A shield can be used as a martial weapon for attacks, using  the statistics listed for a shield bash on the Martial Melee  Weapons table (page 264). The shield bash is an option only  for shields that |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/SectionHeader/1` | 0.521580 | **SHIELDS** |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/7/Text/10` | 0.516709 | **Shields** |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/5/Text/34` | 0.516709 | **Shields** |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/34` | 0.516709 | **Shields** |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/9/Text/49` | 0.516709 | **Shields** |

### Query 14
- Text: What is the rule about A shield can be used as a martial weapon for attacks, using  the statistics listed for a shield bash on the Martial Melee  Weapons table (page 264). The shield bash is an option only  for shields that weren't designed to be used as weapons.  A shield can't have armor or weapon upgrades added to it.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/16', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/23', 'PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/291']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/16` | 1.001042 | A shield can be used as a martial weapon for attacks, using  the statistics listed for a shield bash on the Martial Melee  Weapons table (page 264). The shield bash is an option only  for shields that |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/23` | 0.681847 | **Installed:** Some shields aren't held but are installed  as armor or weapon upgrades. You can Raise a Shield  installed as an armor upgrade as normal. Shields can be  installed only into weapons wit |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/291` | 0.625048 | Shield bash |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/8` | 0.580749 | bonus to your AC, the shield upgrade emits an inertial  dampening barrier, and you automatically Raise a Shield.  You can't Raise a Shield installed as a weapon upgrade any  other way. If you use the |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/4` | 0.562407 | Raise a Shield is the action most commonly used with shields.  Most shields must be held in one hand, so you can't hold  anything with that hand and Raise a Shield, and you lose its  benefits if that |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 0.558468 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/5/Text/5` | 0.524779 | Weapons can be customized with upgrades, which include  technological weapon modifications and magical weapon  fusions. This indicates how many upgrades the weapon can  utilize. You can find more abou |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/8` | 0.519220 | Shields have statistics that follow the same rules as armor:  Price, Speed Penalty, and Bulk. See page 245 for the rules  for those statistics. Their other statistics are described here. |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/12` | 0.516783 | Whenever a shield takes damage, the amount of damage it  takes is reduced by this amount. This number is particularly  relevant for shields because of the Shield Block feat (page  228). The rules for |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/6/Text/20` | 0.505108 | **Professional:** A weapon with this trait can be used as a  toolkit for the listed skill. Add the weapon's item bonus to  attack rolls as an item bonus to skill checks using the listed  skill. For pu |

### Query 15
- Text: What is the rule about SHIELD TRAITS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/17', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/18', 'PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/17` | 0.881473 | SHIELD TRAITS |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/18` | 0.730465 | Shields can have the following traits. |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/1` | 0.640763 | SHIELDS |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/SectionHeader/11` | 0.569479 | SHIELD DESCRIPTIONS |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/629` | 0.558234 | Traits |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/242` | 0.558234 | Traits |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/241` | 0.543348 | Weapon Traits |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/137` | 0.543348 | Weapon Traits |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/33` | 0.543348 | Weapon Traits |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/187` | 0.543348 | Weapon Traits |

### Query 16
- Text: What is the rule about Shields can have the following traits.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/18', 'PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/17', 'PZO22001 Starfinder Player Core 250-267::/page/17/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/18` | 0.925281 | Shields can have the following traits. |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/17` | 0.701703 | SHIELD TRAITS |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/17/Text/15` | 0.695282 | Shields |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/15/Text/15` | 0.653281 | Shields |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/298` | 0.592609 | Shield |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/621` | 0.592609 | Shield |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/8` | 0.582248 | Shields have statistics that follow the same rules as armor:  Price, Speed Penalty, and Bulk. See page 245 for the rules  for those statistics. Their other statistics are described here. |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 0.569318 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/22` | 0.561767 | **Hefty:** This shield is so heavy that raising it takes more  effort. Raising a Shield with the hefty trait is a 2-action  activity unless your Strength modifier equals or exceeds  the number with th |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/23` | 0.553831 | **Installed:** Some shields aren't held but are installed  as armor or weapon upgrades. You can Raise a Shield  installed as an armor upgrade as normal. Shields can be  installed only into weapons wit |

### Query 17
- Text: What is the rule about **Analog:** This shield eschews advanced electronics,  computers systems, and electric power sources, but was  manufactured and calibrated using advanced technology.  This shield is immune to abilities that target technology.  Shield runes (*Pathfinder* *GM Core* 232) don't function on this  shield unless this shield also has the archaic trait.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/19', 'PZO22001 Starfinder Player Core 250-267::/page/5/Text/14', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/19` | 0.962741 | **Analog:** This shield eschews advanced electronics,  computers systems, and electric power sources, but was  manufactured and calibrated using advanced technology.  This shield is immune to abilitie |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/5/Text/14` | 0.879230 | **Analog:** This weapon eschews advanced electronics,  computers systems, and electric power sources but was  manufactured and calibrated using advanced technology.  This weapon is immune to abilities |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/20` | 0.750918 | **Archaic:** This shield is crafted using traditional methods  and materials but isn't suitable for withstanding attacks  from modern weapons. All shields from Pathfinder have the  archaic trait. Shie |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/10` | 0.617378 | **Tech:** This shield incorporates electronics, computer  systems, and integrated power sources. |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/5/Text/16` | 0.585191 | **Archaic:** This trait is applied to weapons crafted using  traditional methods and materials. All weapons from the  Pathfinder Roleplaying Game have the archaic trait. Weapon  runes (see *Pathfinder |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/8/Text/8` | 0.514040 | **Tech:** Weapons with the tech trait incorporate electronics,  computer systems, and power sources. Usually the weapons  rely on integrated power sources (such as melee weapons  that don't have the p |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/23` | 0.479676 | **Installed:** Some shields aren't held but are installed  as armor or weapon upgrades. You can Raise a Shield  installed as an armor upgrade as normal. Shields can be  installed only into weapons wit |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/1/Table/2` | 0.473557 | ShieldLevelPriceAC Bonus1Speed PenaltyBulkHardnessHP (BT)TraitsCarbon shield, commercial025+2—1520 (10)AnalogCompact shield, commercial015+1—L48 (4)Analog, compactDeflecting field, commercial010+1——24 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/8/Text/9` | 0.459908 | **Thought:** Weapons with this trait are bioengineered with  neuroreceptors allowing them to be controlled with telepathy.  When you wield this weapon and have limited telepathy or  telepathy, you can |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/22` | 0.459905 | **Hefty:** This shield is so heavy that raising it takes more  effort. Raising a Shield with the hefty trait is a 2-action  activity unless your Strength modifier equals or exceeds  the number with th |

### Query 18
- Text: What is the rule about **Archaic:** This shield is crafted using traditional methods  and materials but isn't suitable for withstanding attacks  from modern weapons. All shields from Pathfinder have the  archaic trait. Shield runes (*Pathfinder* *GM Core* 232) function  normally with archaic shields.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/20', 'PZO22001 Starfinder Player Core 250-267::/page/5/Text/16', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/20` | 0.980595 | **Archaic:** This shield is crafted using traditional methods  and materials but isn't suitable for withstanding attacks  from modern weapons. All shields from Pathfinder have the  archaic trait. Shie |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/5/Text/16` | 0.815488 | **Archaic:** This trait is applied to weapons crafted using  traditional methods and materials. All weapons from the  Pathfinder Roleplaying Game have the archaic trait. Weapon  runes (see *Pathfinder |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/19` | 0.743109 | **Analog:** This shield eschews advanced electronics,  computers systems, and electric power sources, but was  manufactured and calibrated using advanced technology.  This shield is immune to abilitie |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/5/Text/14` | 0.595374 | **Analog:** This weapon eschews advanced electronics,  computers systems, and electric power sources but was  manufactured and calibrated using advanced technology.  This weapon is immune to abilities |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/16` | 0.512585 | A shield can be used as a martial weapon for attacks, using  the statistics listed for a shield bash on the Martial Melee  Weapons table (page 264). The shield bash is an option only  for shields that |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/23` | 0.507403 | **Installed:** Some shields aren't held but are installed  as armor or weapon upgrades. You can Raise a Shield  installed as an armor upgrade as normal. Shields can be  installed only into weapons wit |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 0.491893 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/22` | 0.476487 | **Hefty:** This shield is so heavy that raising it takes more  effort. Raising a Shield with the hefty trait is a 2-action  activity unless your Strength modifier equals or exceeds  the number with th |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/16` | 0.474906 | **Irising** **Shield:** An irising shield is made of flexible  polycarbon with a retractable design. When retracted,  an irising shield looks like a decorative bangle, gauntlet,  or glove. When deploy |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/12` | 0.470187 | Each type of shield is described in more detail below.  Designer versions of even the most basic shields are  available, often tailored to match a wielder's aesthetic irising shields molded to look li |

### Query 19
- Text: What is the rule about **Compact:** You can Raise a Shield with your compact shield  as long as you have that hand free or are holding, but not  wielding, a light object in that hand.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/21', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/4', 'PZO22001 Starfinder Player Core 250-267::/page/1/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/21` | 0.966150 | **Compact:** You can Raise a Shield with your compact shield  as long as you have that hand free or are holding, but not  wielding, a light object in that hand. |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/4` | 0.770685 | Raise a Shield is the action most commonly used with shields.  Most shields must be held in one hand, so you can't hold  anything with that hand and Raise a Shield, and you lose its  benefits if that |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/9` | 0.647739 | **Retractable:** This shield can collapse into a smaller form  attached to an armguard, gauntlet, glove, or jewelry for  ease of travel and to free up hands. You can use an Interact  action to deploy |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 0.557168 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/6/Text/10` | 0.545383 | **Free-Hand:** This weapon doesn't take up your hand, usually  because it's built into your armor. A free-hand weapon can't  be Disarmed. You can use the hand covered by your free-hand  weapon to wiel |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/14` | 0.542360 | **Compact** **Shield:** This sleek shield is a favorite of  operatives and other mobile combatants. It's most common  design is a polycarbon panel contoured to fit snugly over a  forearm or other limb |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/8` | 0.539619 | bonus to your AC, the shield upgrade emits an inertial  dampening barrier, and you automatically Raise a Shield.  You can't Raise a Shield installed as a weapon upgrade any  other way. If you use the |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/23` | 0.535852 | **Installed:** Some shields aren't held but are installed  as armor or weapon upgrades. You can Raise a Shield  installed as an armor upgrade as normal. Shields can be  installed only into weapons wit |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/22` | 0.533636 | **Hefty:** This shield is so heavy that raising it takes more  effort. Raising a Shield with the hefty trait is a 2-action  activity unless your Strength modifier equals or exceeds  the number with th |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/6/Text/11` | 0.526324 | the hand, you can use abilities that require you to have a  hand free as well as those that require you to be wielding a  weapon in that hand. Each of your hands can have only one  free-hand weapon on |

### Query 20
- Text: What is the rule about **Hefty:** This shield is so heavy that raising it takes more  effort. Raising a Shield with the hefty trait is a 2-action  activity unless your Strength modifier equals or exceeds  the number with the trait. A hefty shield grants its wielder  standard cover.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/22', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/4', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/22` | 1.001122 | **Hefty:** This shield is so heavy that raising it takes more  effort. Raising a Shield with the hefty trait is a 2-action  activity unless your Strength modifier equals or exceeds  the number with th |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/4` | 0.621417 | Raise a Shield is the action most commonly used with shields.  Most shields must be held in one hand, so you can't hold  anything with that hand and Raise a Shield, and you lose its  benefits if that |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 0.620640 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/21` | 0.573583 | **Compact:** You can Raise a Shield with your compact shield  as long as you have that hand free or are holding, but not  wielding, a light object in that hand. |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/23` | 0.555385 | **Installed:** Some shields aren't held but are installed  as armor or weapon upgrades. You can Raise a Shield  installed as an armor upgrade as normal. Shields can be  installed only into weapons wit |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/12` | 0.544151 | Whenever a shield takes damage, the amount of damage it  takes is reduced by this amount. This number is particularly  relevant for shields because of the Shield Block feat (page  228). The rules for |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/10` | 0.529654 | A shield grants a circumstance bonus to AC, but only when  the shield is raised. This requires using the Raise a Shield  action, found on page 411. |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/9` | 0.506947 | **Retractable:** This shield can collapse into a smaller form  attached to an armguard, gauntlet, glove, or jewelry for  ease of travel and to free up hands. You can use an Interact  action to deploy |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/3` | 0.506884 | 1 Gaining a shield's circumstance bonus to AC requires using the Raise a Shield action (found on page 411). |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/8` | 0.506343 | bonus to your AC, the shield upgrade emits an inertial  dampening barrier, and you automatically Raise a Shield.  You can't Raise a Shield installed as a weapon upgrade any  other way. If you use the |

### Query 21
- Text: What is the rule about **Installed:** Some shields aren't held but are installed  as armor or weapon upgrades. You can Raise a Shield  installed as an armor upgrade as normal. Shields can be  installed only into weapons with the parry trait. When  you use a parry weapon with a shield upgrade to get a?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/0/Text/23', 'PZO22001 Starfinder Player Core 250-267::/page/1/Text/8', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/23` | 0.970067 | **Installed:** Some shields aren't held but are installed  as armor or weapon upgrades. You can Raise a Shield  installed as an armor upgrade as normal. Shields can be  installed only into weapons wit |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/8` | 0.723094 | bonus to your AC, the shield upgrade emits an inertial  dampening barrier, and you automatically Raise a Shield.  You can't Raise a Shield installed as a weapon upgrade any  other way. If you use the |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/4` | 0.701289 | Raise a Shield is the action most commonly used with shields.  Most shields must be held in one hand, so you can't hold  anything with that hand and Raise a Shield, and you lose its  benefits if that |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/16` | 0.598917 | A shield can be used as a martial weapon for attacks, using  the statistics listed for a shield bash on the Martial Melee  Weapons table (page 264). The shield bash is an option only  for shields that |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 0.594967 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/21` | 0.587714 | **Compact:** You can Raise a Shield with your compact shield  as long as you have that hand free or are holding, but not  wielding, a light object in that hand. |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/10` | 0.560999 | A shield grants a circumstance bonus to AC, but only when  the shield is raised. This requires using the Raise a Shield  action, found on page 411. |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/22` | 0.551603 | **Hefty:** This shield is so heavy that raising it takes more  effort. Raising a Shield with the hefty trait is a 2-action  activity unless your Strength modifier equals or exceeds  the number with th |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/9` | 0.551415 | **Retractable:** This shield can collapse into a smaller form  attached to an armguard, gauntlet, glove, or jewelry for  ease of travel and to free up hands. You can use an Interact  action to deploy |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/15` | 0.542418 | **Deflecting** **Field:** This shield isn't held—instead, it's  installed as an armor or weapon upgrade. A deflecting  field appears as a translucent panel integrated into  the upgraded item and creat |

### Query 22
- Text: Summarize **SHIELDS**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 250-267::/page/5/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/SectionHeader/1` | 0.969682 | **SHIELDS** |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/1` | 0.843406 | SHIELDS |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/5/Text/34` | 0.807573 | **Shields** |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/13/Text/10` | 0.765573 | **Shields** |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/34` | 0.765573 | **Shields** |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/7/Text/10` | 0.765573 | **Shields** |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/9/Text/49` | 0.765573 | **Shields** |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/11/Text/43` | 0.765573 | **Shields** |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/28` | 0.765573 | **Shields** |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/SectionHeader/5` | 0.691771 | **SHIELD IMPROVEMENTS** |

### Query 23
- Text: Lookup values for ShieldLevelPriceAC Bonus1Speed PenaltyBulkHardnessHP (BT)TraitsCarbon shield, commercial025+2—1520 (10)AnalogCompact shield, commercial015+1—L48 (4)Analog, compactDeflecting field, commercial010+1——24 (2)Installed, techIrising shield, commercial010+1—L36 (3)Retractable, techMobile bulwark, commercial0200+3/+42–10 ft.4624 (12)Analog, hefty +2Phase shield, commercial020+2——510 (5)Retractable, techRiot shield, commercial0100+2/+42–5 ft.2520 (10)Analog
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/Table/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/Table/2', 'PZO22001 Starfinder Player Core 250-267::/page/15/Table/3', 'PZO22001 Starfinder Player Core 250-267::/page/1/Table/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/Table/2` | 1.036904 | ShieldLevelPriceAC Bonus1Speed PenaltyBulkHardnessHP (BT)TraitsCarbon shield, commercial025+2—1520 (10)AnalogCompact shield, commercial015+1—L48 (4)Analog, compactDeflecting field, commercial010+1——24 |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/15/Table/3` | 0.653088 | Simple RangSimple Ranged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsAcid dart rifle0401d8 A80 ft.1125 projectiles11CorrosiveAnalogArc pi |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/Table/6` | 0.652491 | GradeLevelUpgrade PriceTotal Value1HardnessHPBTCommercial0—————Tactical5+750 credits750 credits+3+46+23Advanced8+2,250 credits3,000 credits+3+56+28Superior11+6,000 credits9,000 credits+3+68+34Elite14+ |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/17/Table/0` | 0.607934 | Advanced RangedWeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsCard slinger0261d4 P30 ft.1L17 projectiles11DartAgile, concealable, deadly d8, |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/16/Table/1` | 0.602387 | Martial Rangged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsAssassin rifle01001d10 P120 ft.1121 projectile11SniperAnalog, backstabber, fa |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/639` | 0.578309 | Compact shield, commercial |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/14` | 0.569776 | This column lists the shield's Hit Points (HP) and Broken  Threshold (BT). These measure how much damage the shield  can take before it's destroyed (its total HP) and how much it  can take before bein |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/14/Table/4` | 0.568496 | Simple Melee VVeaporารWeapon (Commercial)Item LevelPriceDamageBulkHandsUpgradesGroupWeapon TraitsBaton021d6 BL11ClubAnalog, finesse, nonlethal, parryBattleglove031d4 B-11BrawlingAgile, analog, free-ha |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/14/Table/5` | 0.564022 | Zero knife0121d4 CL11 |CryoAgile, finesse, powered, tech, versatile PMartial MeleeWeapoinsWeapon (Commercial)Item LevelPriceDamageBulkHandsUpgradesGroupWeapon TraitsAucturnite chakram0151d6 SL11KnifeA |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/7` | 0.554301 | 1 Total value does not include the price of the base commercial shield. |

### Query 24
- Text: Summarize Shield
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/621']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/298', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/621', 'PZO22001 Starfinder Player Core 250-267::/page/17/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/298` | 0.839074 | Shield |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/621` | 0.839074 | Shield |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/17/Text/15` | 0.833303 | Shields |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/15/Text/15` | 0.791303 | Shields |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/34` | 0.658570 | **Shields** |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/9/Text/49` | 0.658570 | **Shields** |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/11/Text/43` | 0.658570 | **Shields** |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/5/Text/34` | 0.658570 | **Shields** |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/28` | 0.658570 | **Shields** |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/13/Text/10` | 0.658570 | **Shields** |

### Query 25
- Text: Summarize Level
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/622']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/694', 'PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/237', 'PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/320']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/694` | 0.767709 | Level |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/237` | 0.767709 | Level |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/320` | 0.767709 | Level |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/125` | 0.725709 | Level |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/622` | 0.725709 | Level |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/176` | 0.626678 | Item Level |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/373` | 0.626678 | Item Level |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/230` | 0.626678 | Item Level |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/350` | 0.626678 | Item Level |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/126` | 0.626678 | Item Level |

### Query 26
- Text: Summarize Price
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/623']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/374', 'PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/23', 'PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/231']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/374` | 0.746623 | Price |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/23` | 0.746623 | Price |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/231` | 0.746623 | Price |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/127` | 0.704623 | Price |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/177` | 0.704623 | Price |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/623` | 0.704623 | Price |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/316` | 0.704623 | Price |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/301` | 0.704623 | Price |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/41` | 0.704623 | Price |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/122` | 0.704623 | Price |

### Query 27
- Text: What is the rule about AC Bonus1?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/624']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/624', 'PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/9', 'PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/624` | 0.871695 | AC Bonus1 |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/9` | 0.702510 | AC BONUS |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/3` | 0.585743 | 1 Gaining a shield's circumstance bonus to AC requires using the Raise a Shield action (found on page 411). |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/10` | 0.507421 | A shield grants a circumstance bonus to AC, but only when  the shield is raised. This requires using the Raise a Shield  action, found on page 411. |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/8` | 0.464837 | bonus to your AC, the shield upgrade emits an inertial  dampening barrier, and you automatically Raise a Shield.  You can't Raise a Shield installed as a weapon upgrade any  other way. If you use the |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 0.451520 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/8/Text/21` | 0.403905 | **Axe:** Choose one creature adjacent to the initial target and  within reach. If its AC is lower than your attack roll result for  the critical hit, you deal damage to that creature equal to the  res |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/5` | 0.403424 | When you have a riot shield or mobile bulwark raised,  you can use the Take Cover action (page 410) to increase the  circumstance bonus to AC to +4. This lasts until the shield is  no longer raised or |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/205` | 0.372886 | 1 |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/66` | 0.372886 | 1 |

### Query 28
- Text: Summarize Speed Penalty
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/625']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/625', 'PZO22001 Starfinder Player Core 250-267::/page/4/Text/15', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/625` | 0.969945 | Speed Penalty |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/15` | 0.508450 | For example, a commercial semi-auto pistol takes no  penalty against a target up to 60 feet away, a –2 penalty  against a target beyond 60 feet but up to 120 feet away, a –4  penalty against a target |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/8` | 0.491297 | Shields have statistics that follow the same rules as armor:  Price, Speed Penalty, and Bulk. See page 245 for the rules  for those statistics. Their other statistics are described here. |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/3/SectionHeader/8` | 0.435626 | MULTIPLE ATTACK PENALTY |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/14` | 0.389029 | **Ranged damage roll = damage die of weapon (+ ** **Strength modifier for a thrown weapon or half ** **Strength modifier for a propulsive weapon) + ** **other bonuses + penalties** |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/5/Text/13` | 0.383585 | **Agile:** The multiple attack penalty you take with this weapon  on the second attack on your turn is –4 instead of –5, and –8  instead of –10 on the third and subsequent attacks in the turn. |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 0.382095 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/9` | 0.368909 | If you use an action with the attack trait more than once  on the same turn, your attacks after the first take a penalty  called a multiple attack penalty. Your second attack  takes a –5 penalty, and |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/8/Text/18` | 0.368726 | **Volley:** This ranged weapon is less effective at close  distances. Your attacks against targets that are within the  range listed take a –2 penalty. |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/Table/2` | 0.362187 | ShieldLevelPriceAC Bonus1Speed PenaltyBulkHardnessHP (BT)TraitsCarbon shield, commercial025+2—1520 (10)AnalogCompact shield, commercial015+1—L48 (4)Analog, compactDeflecting field, commercial010+1——24 |

### Query 29
- Text: Summarize Bulk
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/626']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/626', 'PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/131', 'PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/27']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/626` | 0.845513 | Bulk |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/131` | 0.845513 | Bulk |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/27` | 0.845513 | Bulk |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/318` | 0.803513 | Bulk |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/303` | 0.803513 | Bulk |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/235` | 0.803513 | Bulk |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/378` | 0.803513 | Bulk |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/19` | 0.803513 | Bulk |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/124` | 0.803513 | Bulk |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/128` | 0.803513 | Bulk |

### Query 30
- Text: Summarize Hardness
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/627']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/697', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/627', 'PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/697` | 0.944006 | Hardness |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/627` | 0.944006 | Hardness |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/11` | 0.790622 | HARDNESS |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/12` | 0.539590 | Whenever a shield takes damage, the amount of damage it  takes is reduced by this amount. This number is particularly  relevant for shields because of the Shield Block feat (page  228). The rules for |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/22` | 0.327946 | **Hefty:** This shield is so heavy that raising it takes more  effort. Raising a Shield with the hefty trait is a 2-action  activity unless your Strength modifier equals or exceeds  the number with th |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/14` | 0.314584 | This column lists the shield's Hit Points (HP) and Broken  Threshold (BT). These measure how much damage the shield  can take before it's destroyed (its total HP) and how much it  can take before bein |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/202` | 0.313572 | Area (cone), tech, unwieldy |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/6/Text/9` | 0.312350 | **Forceful:** This weapon becomes more dangerous as you  build momentum. When you attack with it more than once  on your turn, the second attack gains a circumstance bonus  to damage equal to the numb |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/317` | 0.303585 | Analog, area (cone), concussive, unwieldy |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/215` | 0.299326 | Area (line), tech, unwieldy |

### Query 31
- Text: Summarize HP (BT)
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/628']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/628', 'PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/13', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/698']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/628` | 0.945073 | HP (BT) |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/0/SectionHeader/13` | 0.945073 | HP (BT) |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/698` | 0.683690 | HP |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/699` | 0.571162 | BT |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/14` | 0.531955 | This column lists the shield's Hit Points (HP) and Broken  Threshold (BT). These measure how much damage the shield  can take before it's destroyed (its total HP) and how much it  can take before bein |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/Table/2` | 0.441034 | ShieldLevelPriceAC Bonus1Speed PenaltyBulkHardnessHP (BT)TraitsCarbon shield, commercial025+2—1520 (10)AnalogCompact shield, commercial015+1—L48 (4)Analog, compactDeflecting field, commercial010+1——24 |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/Table/6` | 0.440628 | GradeLevelUpgrade PriceTotal Value1HardnessHPBTCommercial0—————Tactical5+750 credits750 credits+3+46+23Advanced8+2,250 credits3,000 credits+3+56+28Superior11+6,000 credits9,000 credits+3+68+34Elite14+ |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/101` | 0.310336 | Agile, finesse, powered, tech, versatile P |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/110` | 0.310336 | Agile, finesse, powered, tech, versatile P |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/329` | 0.306605 | Battery, commercial Battery, tactical |

### Query 32
- Text: What is the rule about Traits?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/629']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/242', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/629', 'PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/242` | 0.807186 | Traits |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/629` | 0.807186 | Traits |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/22` | 0.655879 | Weapon Traits |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/241` | 0.613879 | Weapon Traits |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/384` | 0.613879 | Weapon Traits |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/137` | 0.613879 | Weapon Traits |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/187` | 0.613879 | Weapon Traits |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/128` | 0.613879 | Weapon Traits |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/33` | 0.613879 | Weapon Traits |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/132` | 0.613879 | Weapon Traits |

### Query 33
- Text: Summarize Carbon shield, commercial
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/630']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/630', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/639', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/675']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/630` | 1.001868 | Carbon shield, commercial |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/639` | 0.780089 | Compact shield, commercial |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/675` | 0.735759 | Phase shield, commercial |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/657` | 0.668509 | Irising shield, commercial |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/684` | 0.658180 | Riot shield, commercial |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/13` | 0.584039 | **Carbon** **Shield:** This durable yet lightweight defensive  plate comes in a variety of shapes and sizes, and it's often  customized with LED displays that broadcast personal  insignia or an organi |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/Table/2` | 0.559039 | ShieldLevelPriceAC Bonus1Speed PenaltyBulkHardnessHP (BT)TraitsCarbon shield, commercial025+2—1520 (10)AnalogCompact shield, commercial015+1—L48 (4)Analog, compactDeflecting field, commercial010+1——24 |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/15/Text/15` | 0.529965 | Shields |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/17/Text/15` | 0.529965 | Shields |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/298` | 0.511516 | Shield |

### Query 34
- Text: Summarize 0
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/631']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/631', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/685', 'PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/152']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/631` | 0.737785 | 0 |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/685` | 0.737785 | 0 |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/152` | 0.737785 | 0 |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/701` | 0.695785 | 0 |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/139` | 0.695785 | 0 |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/676` | 0.695785 | 0 |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/319` | 0.695785 | 0 |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/332` | 0.695785 | 0 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/243` | 0.695785 | 0 |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/252` | 0.695785 | 0 |

### Query 35
- Text: Summarize 25
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/632']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/212', 'PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/142', 'PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/203']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/212` | 0.761392 | 25 |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/142` | 0.761392 | 25 |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/203` | 0.761392 | 25 |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/632` | 0.719392 | 25 |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/242` | 0.719392 | 25 |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/140` | 0.559660 | 26 |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/185` | 0.492328 | 27 |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/88` | 0.480198 | 75 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/387` | 0.437817 | 95 |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/266` | 0.431365 | 20 |

### Query 36
- Text: Summarize +2
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/633']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/633', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/678', 'PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/282']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/633` | 0.804657 | +2 |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/678` | 0.804657 | +2 |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/282` | 0.804657 | +2 |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/275` | 0.762657 | +2 |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/711` | 0.682396 | +3 |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/718` | 0.682396 | +3 |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/725` | 0.682396 | +3 |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/289` | 0.682396 | +3 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/660` | 0.639189 | +1 |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/651` | 0.639189 | +1 |

### Query 37
- Text: Summarize —
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/634']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/661', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/634', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/643']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/661` | 0.572766 | — |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/634` | 0.572766 | — |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/643` | 0.572766 | — |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/679` | 0.530766 | — |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/704` | 0.530766 | — |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/706` | 0.530766 | — |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/705` | 0.530766 | — |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/652` | 0.530766 | — |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/702` | 0.530766 | — |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/680` | 0.530766 | — |

### Query 38
- Text: Summarize 1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/635']
- Expected found: `True`
- Expected rank: `24`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/182', 'PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/174', 'PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/205']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/182` | 0.669108 | 1 |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/174` | 0.669108 | 1 |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/205` | 0.669108 | 1 |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/315` | 0.627108 | 1 |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/160` | 0.627108 | 1 |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/157` | 0.627108 | 1 |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/341` | 0.627108 | 1 |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/174` | 0.627108 | 1 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/210` | 0.627108 | 1 |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/173` | 0.627108 | 1 |

### Query 39
- Text: Summarize 5
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/636']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/690', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/708', 'PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/356']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/690` | 0.772788 | 5 |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/708` | 0.772788 | 5 |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/356` | 0.772788 | 5 |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/212` | 0.730788 | 5 |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/149` | 0.730788 | 5 |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/140` | 0.730788 | 5 |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/681` | 0.730788 | 5 |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/636` | 0.730788 | 5 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/166` | 0.730788 | 5 |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/186` | 0.730788 | 5 |

### Query 40
- Text: Summarize 20 (10)
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/637']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/637', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/691', 'PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/341']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/637` | 0.808550 | 20 (10) |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/691` | 0.808550 | 20 (10) |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/341` | 0.727927 | 10 20 |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/342` | 0.697927 | 10 20 |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/366` | 0.639757 | 20 |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/311` | 0.639757 | 20 |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/167` | 0.639757 | 20 |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/743` | 0.639757 | 20 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/677` | 0.639757 | 20 |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/266` | 0.639757 | 20 |

### Query 41
- Text: Summarize Analog
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/638']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/343', 'PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/200', 'PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/252']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/343` | 0.832477 | Analog |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/252` | 0.832477 | Analog |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/200` | 0.832477 | Analog |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/638` | 0.790477 | Analog |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/692` | 0.790477 | Analog |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/176` | 0.595009 | Analog, automatic |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/111` | 0.595009 | Analog, automatic |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/239` | 0.595009 | Analog, automatic |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/647` | 0.565855 | Analog, compact |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/674` | 0.563947 | Analog, hefty +2 |

### Query 42
- Text: What is the rule about Compact shield, commercial?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/639']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/639', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/630', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/675']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/639` | 0.885116 | Compact shield, commercial |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/630` | 0.677946 | Carbon shield, commercial |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/675` | 0.639536 | Phase shield, commercial |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/657` | 0.590149 | Irising shield, commercial |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/21` | 0.587917 | **Compact:** You can Raise a Shield with your compact shield  as long as you have that hand free or are holding, but not  wielding, a light object in that hand. |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/684` | 0.560633 | Riot shield, commercial |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/14` | 0.537941 | **Compact** **Shield:** This sleek shield is a favorite of  operatives and other mobile combatants. It's most common  design is a polycarbon panel contoured to fit snugly over a  forearm or other limb |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/1/Table/2` | 0.511432 | ShieldLevelPriceAC Bonus1Speed PenaltyBulkHardnessHP (BT)TraitsCarbon shield, commercial025+2—1520 (10)AnalogCompact shield, commercial015+1—L48 (4)Analog, compactDeflecting field, commercial010+1——24 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/4` | 0.502468 | Raise a Shield is the action most commonly used with shields.  Most shields must be held in one hand, so you can't hold  anything with that hand and Raise a Shield, and you lose its  benefits if that |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/7` | 0.478555 | 1 Total value does not include the price of the base commercial shield. |

### Query 43
- Text: Summarize 0
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/640']
- Expected found: `True`
- Expected rank: `85`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/631', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/685', 'PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/152']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/631` | 0.737785 | 0 |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/685` | 0.737785 | 0 |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/152` | 0.737785 | 0 |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/701` | 0.695785 | 0 |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/139` | 0.695785 | 0 |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/676` | 0.695785 | 0 |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/319` | 0.695785 | 0 |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/332` | 0.695785 | 0 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/243` | 0.695785 | 0 |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/252` | 0.695785 | 0 |

### Query 44
- Text: Summarize 15
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/641']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/131', 'PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/77', 'PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/194']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/131` | 0.777005 | 15 |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/194` | 0.777005 | 15 |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/77` | 0.777005 | 15 |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/203` | 0.735005 | 15 |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/275` | 0.735005 | 15 |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/257` | 0.735004 | 15 |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/158` | 0.735004 | 15 |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/641` | 0.735004 | 15 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/362` | 0.572131 | 16 |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/284` | 0.572131 | 16 |

### Query 45
- Text: Summarize +1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/642']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/642', 'PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/261', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/660']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/642` | 0.764275 | +1 |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/261` | 0.764275 | +1 |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/660` | 0.764275 | +1 |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/268` | 0.722275 | +1 |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/651` | 0.722275 | +1 |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/718` | 0.649232 | +3 |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/711` | 0.649232 | +3 |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/289` | 0.649232 | +3 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/725` | 0.649232 | +3 |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/732` | 0.634751 | +5 |

### Query 46
- Text: Summarize —
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/643']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/661', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/634', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/643']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/661` | 0.572766 | — |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/634` | 0.572766 | — |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/643` | 0.572766 | — |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/679` | 0.530766 | — |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/704` | 0.530766 | — |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/706` | 0.530766 | — |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/705` | 0.530766 | — |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/652` | 0.530766 | — |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/702` | 0.530766 | — |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/680` | 0.530766 | — |

### Query 47
- Text: Summarize L
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/644']
- Expected found: `True`
- Expected rank: `20`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/133', 'PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/142', 'PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/70']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/133` | 0.710471 | L |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/142` | 0.710471 | L |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/70` | 0.710471 | L |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/662` | 0.668471 | L |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/151` | 0.668471 | L |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/286` | 0.668471 | L |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/304` | 0.668471 | L |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/223` | 0.668471 | L |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/160` | 0.668471 | L |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/131` | 0.668471 | L |

### Query 48
- Text: Summarize 4
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/645']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/645', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/671', 'PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/365']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/645` | 0.774878 | 4 |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/671` | 0.774877 | 4 |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/365` | 0.774877 | 4 |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/258` | 0.732877 | 4 |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/290` | 0.732877 | 4 |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/655` | 0.555380 | 4 (2) |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/646` | 0.500966 | 8 (4) |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/276` | 0.459139 | 3 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/59` | 0.459139 | 3 |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/283` | 0.459139 | 3 |

### Query 49
- Text: Summarize 8 (4)
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/646']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/646', 'PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/357', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/715']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/646` | 0.858921 | 8 (4) |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/357` | 0.670451 | 8 |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/715` | 0.670451 | 8 |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/645` | 0.635595 | 4 |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/365` | 0.623595 | 4 |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/258` | 0.623595 | 4 |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/671` | 0.623595 | 4 |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/290` | 0.623595 | 4 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/655` | 0.586498 | 4 (2) |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/664` | 0.465203 | 6 (3) |

### Query 50
- Text: What is the rule about Analog, compact?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/647']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/647', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/692', 'PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/343']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/647` | 0.845356 | Analog, compact |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/692` | 0.614730 | Analog |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/343` | 0.614730 | Analog |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/200` | 0.572730 | Analog |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/638` | 0.572730 | Analog |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/252` | 0.572730 | Analog |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/239` | 0.501775 | Analog, automatic |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/176` | 0.501775 | Analog, automatic |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/111` | 0.501775 | Analog, automatic |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/317` | 0.448103 | Analog, area (cone), concussive, unwieldy |

### Query 51
- Text: Summarize Deflecting field, commercial
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/648']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/648', 'PZO22001 Starfinder Player Core 250-267::/page/1/Text/15', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/639']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/648` | 1.004907 | Deflecting field, commercial |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/15` | 0.588418 | **Deflecting** **Field:** This shield isn't held—instead, it's  installed as an armor or weapon upgrade. A deflecting  field appears as a translucent panel integrated into  the upgraded item and creat |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/639` | 0.497006 | Compact shield, commercial |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/675` | 0.444297 | Phase shield, commercial |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/630` | 0.423005 | Carbon shield, commercial |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/243` | 0.409629 | Commercial |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/700` | 0.409629 | Commercial |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/657` | 0.409292 | Irising shield, commercial |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/150` | 0.398364 | Agile, concealable, deadly d8, professional (Deception), tech |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/324` | 0.393356 | Battery, commercial |

### Query 52
- Text: Summarize 0
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/649']
- Expected found: `True`
- Expected rank: `84`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/631', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/685', 'PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/152']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/631` | 0.737785 | 0 |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/685` | 0.737785 | 0 |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/152` | 0.737785 | 0 |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/701` | 0.695785 | 0 |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/139` | 0.695785 | 0 |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/676` | 0.695785 | 0 |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/319` | 0.695785 | 0 |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/332` | 0.695785 | 0 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/243` | 0.695785 | 0 |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/252` | 0.695785 | 0 |

### Query 53
- Text: Summarize 10
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/650']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/370', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/659', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/650']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/370` | 0.782219 | 10 |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/659` | 0.782219 | 10 |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/650` | 0.782219 | 10 |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/361` | 0.740219 | 10 |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/327` | 0.740219 | 10 |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/336` | 0.740219 | 10 |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/337` | 0.740219 | 10 |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/176` | 0.740219 | 10 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/221` | 0.740219 | 10 |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/320` | 0.740219 | 10 |

### Query 54
- Text: Summarize +1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/651']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/642', 'PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/261', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/660']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/642` | 0.764275 | +1 |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/261` | 0.764275 | +1 |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/660` | 0.764275 | +1 |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/268` | 0.722275 | +1 |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/651` | 0.722275 | +1 |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/718` | 0.649232 | +3 |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/711` | 0.649232 | +3 |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/289` | 0.649232 | +3 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/725` | 0.649232 | +3 |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/732` | 0.634751 | +5 |

### Query 55
- Text: Summarize —
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/652']
- Expected found: `True`
- Expected rank: `10`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/634', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/643', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/704']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/634` | 0.572766 | — |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/643` | 0.572766 | — |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/704` | 0.572766 | — |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/705` | 0.542766 | — |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/703` | 0.542766 | — |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/706` | 0.530766 | — |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/661` | 0.530766 | — |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/680` | 0.530766 | — |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/679` | 0.530766 | — |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/652` | 0.530766 | — |

### Query 56
- Text: Summarize —
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/653']
- Expected found: `True`
- Expected rank: `12`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/634', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/643', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/704']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/634` | 0.572766 | — |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/643` | 0.572766 | — |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/704` | 0.572766 | — |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/705` | 0.542766 | — |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/703` | 0.542766 | — |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/706` | 0.530766 | — |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/661` | 0.530766 | — |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/680` | 0.530766 | — |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/679` | 0.530766 | — |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/652` | 0.530766 | — |

### Query 57
- Text: Summarize 2
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/654']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/67', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/689', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/654']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/67` | 0.689465 | 2 |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/654` | 0.689465 | 2 |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/689` | 0.689465 | 2 |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/50` | 0.647465 | 2 |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/80` | 0.647465 | 2 |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/68` | 0.647465 | 2 |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/170` | 0.647465 | 2 |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/188` | 0.647465 | 2 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/206` | 0.647465 | 2 |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/161` | 0.647465 | 2 |

### Query 58
- Text: Summarize 4 (2)
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/655']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/655', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/645', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/671']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/655` | 0.775182 | 4 (2) |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/645` | 0.654328 | 4 |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/671` | 0.654328 | 4 |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/365` | 0.612328 | 4 |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/258` | 0.612328 | 4 |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/290` | 0.612328 | 4 |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/654` | 0.595066 | 2 |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/689` | 0.583066 | 2 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/50` | 0.583066 | 2 |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/170` | 0.583066 | 2 |

### Query 59
- Text: Summarize Installed, tech
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/656']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/656', 'PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/278', 'PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/369']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/656` | 0.938176 | Installed, tech |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/369` | 0.586095 | Tech |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/278` | 0.586095 | Tech |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/265` | 0.544095 | Tech |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/150` | 0.484141 | Automatic, tech |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/226` | 0.471405 | Arc, tech |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/213` | 0.471405 | Arc, tech |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/10` | 0.455668 | **Tech:** This shield incorporates electronics, computer  systems, and integrated power sources. |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/8/Text/8` | 0.451189 | **Tech:** Weapons with the tech trait incorporate electronics,  computer systems, and power sources. Usually the weapons  rely on integrated power sources (such as melee weapons  that don't have the p |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/263` | 0.450506 | Critical (plasma), powered, tech |

### Query 60
- Text: Summarize Irising shield, commercial
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/657']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/657', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/639', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/684']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/657` | 1.004242 | Irising shield, commercial |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/639` | 0.726565 | Compact shield, commercial |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/684` | 0.694251 | Riot shield, commercial |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/630` | 0.651428 | Carbon shield, commercial |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/675` | 0.629206 | Phase shield, commercial |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/16` | 0.612065 | **Irising** **Shield:** An irising shield is made of flexible  polycarbon with a retractable design. When retracted,  an irising shield looks like a decorative bangle, gauntlet,  or glove. When deploy |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/7` | 0.500592 | 1 Total value does not include the price of the base commercial shield. |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/15/Text/15` | 0.485403 | Shields |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/17/Text/15` | 0.485403 | Shields |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/Table/2` | 0.480619 | ShieldLevelPriceAC Bonus1Speed PenaltyBulkHardnessHP (BT)TraitsCarbon shield, commercial025+2—1520 (10)AnalogCompact shield, commercial015+1—L48 (4)Analog, compactDeflecting field, commercial010+1——24 |

### Query 61
- Text: Summarize 0
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/658']
- Expected found: `True`
- Expected rank: `83`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/631', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/685', 'PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/152']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/631` | 0.737785 | 0 |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/685` | 0.737785 | 0 |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/152` | 0.737785 | 0 |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/701` | 0.695785 | 0 |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/139` | 0.695785 | 0 |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/676` | 0.695785 | 0 |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/319` | 0.695785 | 0 |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/332` | 0.695785 | 0 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/243` | 0.695785 | 0 |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/252` | 0.695785 | 0 |

### Query 62
- Text: Summarize 10
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/659']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/370', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/659', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/650']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/370` | 0.782219 | 10 |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/659` | 0.782219 | 10 |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/650` | 0.782219 | 10 |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/361` | 0.740219 | 10 |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/327` | 0.740219 | 10 |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/336` | 0.740219 | 10 |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/337` | 0.740219 | 10 |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/176` | 0.740219 | 10 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/221` | 0.740219 | 10 |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/320` | 0.740219 | 10 |

### Query 63
- Text: Summarize +1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/660']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/642', 'PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/261', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/660']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/642` | 0.764275 | +1 |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/261` | 0.764275 | +1 |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/660` | 0.764275 | +1 |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/268` | 0.722275 | +1 |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/651` | 0.722275 | +1 |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/718` | 0.649232 | +3 |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/711` | 0.649232 | +3 |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/289` | 0.649232 | +3 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/725` | 0.649232 | +3 |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/732` | 0.634751 | +5 |

### Query 64
- Text: Summarize —
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/661']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/661', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/634', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/643']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/661` | 0.572766 | — |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/634` | 0.572766 | — |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/643` | 0.572766 | — |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/679` | 0.530766 | — |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/704` | 0.530766 | — |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/706` | 0.530766 | — |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/705` | 0.530766 | — |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/652` | 0.530766 | — |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/702` | 0.530766 | — |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/680` | 0.530766 | — |

### Query 65
- Text: Summarize L
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/662']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/133', 'PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/151', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/662']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/133` | 0.710471 | L |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/151` | 0.710471 | L |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/662` | 0.710471 | L |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/223` | 0.668471 | L |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/160` | 0.668471 | L |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/286` | 0.668471 | L |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/304` | 0.668471 | L |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/144` | 0.668471 | L |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/170` | 0.668471 | L |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/131` | 0.668471 | L |

### Query 66
- Text: Summarize 3
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/663']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/59', 'PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/276', 'PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/283']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/59` | 0.731895 | 3 |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/276` | 0.731895 | 3 |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/283` | 0.731895 | 3 |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/663` | 0.689895 | 3 |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/50` | 0.516533 | 2 |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/68` | 0.516533 | 2 |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/689` | 0.516533 | 2 |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/654` | 0.516533 | 2 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/170` | 0.516533 | 2 |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/188` | 0.516533 | 2 |

### Query 67
- Text: Summarize 6 (3)
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/664']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/664', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/672', 'PZO22001 Starfinder Player Core 250-267::/page/17/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/664` | 0.831344 | 6 (3) |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/672` | 0.679604 | 6 |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/17/Text/6` | 0.679604 | 6 |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/663` | 0.594886 | 3 |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/59` | 0.582887 | 3 |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/283` | 0.582886 | 3 |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/276` | 0.582886 | 3 |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/739` | 0.465456 | +6 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/655` | 0.458929 | 4 (2) |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/646` | 0.444907 | 8 (4) |

### Query 68
- Text: What is the rule about Retractable, tech?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/665']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/665', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/683', 'PZO22001 Starfinder Player Core 250-267::/page/1/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/665` | 0.885265 | Retractable, tech |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/683` | 0.885265 | Retractable, tech |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/9` | 0.485978 | **Retractable:** This shield can collapse into a smaller form  attached to an armguard, gauntlet, glove, or jewelry for  ease of travel and to free up hands. You can use an Interact  action to deploy |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/278` | 0.415615 | Tech |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/369` | 0.415615 | Tech |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/265` | 0.415615 | Tech |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/291` | 0.409639 | Nonlethal, tech |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/176` | 0.397726 | Agile, tech, thrown, recovery |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/8/Text/8` | 0.386083 | **Tech:** Weapons with the tech trait incorporate electronics,  computer systems, and power sources. Usually the weapons  rely on integrated power sources (such as melee weapons  that don't have the p |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/656` | 0.371695 | Installed, tech |

### Query 69
- Text: Summarize Mobile bulwark, commercial
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/666']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/666', 'PZO22001 Starfinder Player Core 250-267::/page/1/Text/17', 'PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/324']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/666` | 1.013866 | Mobile bulwark, commercial |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/17` | 0.689068 | **Mobile** **Bulwark:** This bulky shield is advertised as the  ultimate protection in battle for those strong enough to  hoist them. Mobile bulwarks create an iconic rectangular  silhouette and are p |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/324` | 0.562151 | Battery, commercial |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/639` | 0.457732 | Compact shield, commercial |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/243` | 0.450305 | Commercial |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/700` | 0.450305 | Commercial |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/684` | 0.441719 | Riot shield, commercial |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/120` | 0.430406 | Weapon (Commercial) |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/372` | 0.430406 | Weapon (Commercial) |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/229` | 0.430406 | Weapon (Commercial) |

### Query 70
- Text: Summarize 0
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/667']
- Expected found: `True`
- Expected rank: `36`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/103', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/685', 'PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/252']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/103` | 0.737786 | 0 |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/685` | 0.737785 | 0 |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/252` | 0.737785 | 0 |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/94` | 0.695785 | 0 |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/243` | 0.695785 | 0 |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/631` | 0.695785 | 0 |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/85` | 0.695785 | 0 |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/166` | 0.695785 | 0 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/256` | 0.695785 | 0 |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/676` | 0.695785 | 0 |

### Query 71
- Text: Summarize 200
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/668']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/668', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/740', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/686']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/668` | 0.803099 | 200 |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/740` | 0.500807 | +100 |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/686` | 0.500719 | 100 |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/36` | 0.458719 | 100 |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/75` | 0.458719 | 100 |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/274` | 0.422967 | 20,000 credits |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/158` | 0.408558 | 20 |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/311` | 0.408558 | 20 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/366` | 0.408558 | 20 |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/167` | 0.408558 | 20 |

### Query 72
- Text: Summarize +3/+42
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/669']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/669', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/687', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/734']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/669` | 0.936975 | +3/+42 |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/687` | 0.825643 | +2/+42 |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/734` | 0.582538 | +40 |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/711` | 0.501552 | +3 |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/718` | 0.501552 | +3 |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/725` | 0.501552 | +3 |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/289` | 0.501552 | +3 |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/727` | 0.498850 | +34 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/712` | 0.468780 | +46 |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/719` | 0.450872 | +56 |

### Query 73
- Text: What is the rule about Retractable, tech?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/683']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/665', 'PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/683', 'PZO22001 Starfinder Player Core 250-267::/page/1/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/665` | 0.885265 | Retractable, tech |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/683` | 0.885265 | Retractable, tech |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/9` | 0.485978 | **Retractable:** This shield can collapse into a smaller form  attached to an armguard, gauntlet, glove, or jewelry for  ease of travel and to free up hands. You can use an Interact  action to deploy |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/278` | 0.415615 | Tech |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/369` | 0.415615 | Tech |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/265` | 0.415615 | Tech |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/291` | 0.409639 | Nonlethal, tech |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/176` | 0.397726 | Agile, tech, thrown, recovery |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/8/Text/8` | 0.386083 | **Tech:** Weapons with the tech trait incorporate electronics,  computer systems, and power sources. Usually the weapons  rely on integrated power sources (such as melee weapons  that don't have the p |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/656` | 0.371695 | Installed, tech |

### Query 74
- Text: What is the rule about 1 Gaining a shield's circumstance bonus to AC requires using the Raise a Shield action (found on page 411).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/3', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/10', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/3` | 0.992584 | 1 Gaining a shield's circumstance bonus to AC requires using the Raise a Shield action (found on page 411). |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/10` | 0.944520 | A shield grants a circumstance bonus to AC, but only when  the shield is raised. This requires using the Raise a Shield  action, found on page 411. |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 0.803133 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/8` | 0.731589 | bonus to your AC, the shield upgrade emits an inertial  dampening barrier, and you automatically Raise a Shield.  You can't Raise a Shield installed as a weapon upgrade any  other way. If you use the |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/5` | 0.669972 | When you have a riot shield or mobile bulwark raised,  you can use the Take Cover action (page 410) to increase the  circumstance bonus to AC to +4. This lasts until the shield is  no longer raised or |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/4` | 0.665007 | Raise a Shield is the action most commonly used with shields.  Most shields must be held in one hand, so you can't hold  anything with that hand and Raise a Shield, and you lose its  benefits if that |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/4` | 0.626987 | 2 Getting the higher bonus for a mobile bulwark or riot shield requires using the Take Cover action (page 410) while the  shield is raised. |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/6` | 0.562333 | If you have access to the Shield Block reaction (from your  class or from a feat), you can use it while Raising your Shield  to reduce the damage you take by an amount equal to the  shield's Hardness. |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/21` | 0.531218 | **Compact:** You can Raise a Shield with your compact shield  as long as you have that hand free or are holding, but not  wielding, a light object in that hand. |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/23` | 0.529579 | **Installed:** Some shields aren't held but are installed  as armor or weapon upgrades. You can Raise a Shield  installed as an armor upgrade as normal. Shields can be  installed only into weapons wit |

### Query 75
- Text: What is the rule about 2 Getting the higher bonus for a mobile bulwark or riot shield requires using the Take Cover action (page 410) while the  shield is raised.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/4', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/5', 'PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/4` | 0.994527 | 2 Getting the higher bonus for a mobile bulwark or riot shield requires using the Take Cover action (page 410) while the  shield is raised. |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/5` | 0.882611 | When you have a riot shield or mobile bulwark raised,  you can use the Take Cover action (page 410) to increase the  circumstance bonus to AC to +4. This lasts until the shield is  no longer raised or |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/3` | 0.645669 | 1 Gaining a shield's circumstance bonus to AC requires using the Raise a Shield action (found on page 411). |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/10` | 0.601759 | A shield grants a circumstance bonus to AC, but only when  the shield is raised. This requires using the Raise a Shield  action, found on page 411. |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/4` | 0.587801 | Raise a Shield is the action most commonly used with shields.  Most shields must be held in one hand, so you can't hold  anything with that hand and Raise a Shield, and you lose its  benefits if that |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 0.554350 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/8` | 0.550556 | bonus to your AC, the shield upgrade emits an inertial  dampening barrier, and you automatically Raise a Shield.  You can't Raise a Shield installed as a weapon upgrade any  other way. If you use the |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/22` | 0.502983 | **Hefty:** This shield is so heavy that raising it takes more  effort. Raising a Shield with the hefty trait is a 2-action  activity unless your Strength modifier equals or exceeds  the number with th |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/21` | 0.492410 | **Compact:** You can Raise a Shield with your compact shield  as long as you have that hand free or are holding, but not  wielding, a light object in that hand. |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/6` | 0.489917 | If you have access to the Shield Block reaction (from your  class or from a feat), you can use it while Raising your Shield  to reduce the damage you take by an amount equal to the  shield's Hardness. |

### Query 76
- Text: Lookup values for GradeLevelUpgrade PriceTotal Value1HardnessHPBTCommercial0—————Tactical5+750 credits750 credits+3+46+23Advanced8+2,250 credits3,000 credits+3+56+28Superior11+6,000 credits9,000 credits+3+68+34Elite14+16,000 credits25,000 credits+5+80+40Ultimate18+55,000 credits80,000 credits+6+100+50Paragon20+240,000 credits320,000 credits+7+120+60
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/Table/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/Table/6', 'PZO22001 Starfinder Player Core 250-267::/page/17/Table/1', 'PZO22001 Starfinder Player Core 250-267::/page/1/Table/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/Table/6` | 1.028927 | GradeLevelUpgrade PriceTotal Value1HardnessHPBTCommercial0—————Tactical5+750 credits750 credits+3+46+23Advanced8+2,250 credits3,000 credits+3+56+28Superior11+6,000 credits9,000 credits+3+68+34Elite14+ |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/17/Table/1` | 0.792634 | Weapon ImprovvementsGradeLevelUpgrade PriceTotal Value1UpgradesDamage DiceTraitsCommercial0--+01-Tactical2+350 credits350 credits+01Tracking +1Advanced4+650 credits1,000 credits+12Tracking +1Superior1 |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/Table/2` | 0.637462 | ShieldLevelPriceAC Bonus1Speed PenaltyBulkHardnessHP (BT)TraitsCarbon shield, commercial025+2—1520 (10)AnalogCompact shield, commercial015+1—L48 (4)Analog, compactDeflecting field, commercial010+1——24 |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/15/Table/3` | 0.547459 | Simple RangSimple Ranged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsAcid dart rifle0401d8 A80 ft.1125 projectiles11CorrosiveAnalogArc pi |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/17/Table/0` | 0.534899 | Advanced RangedWeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsCard slinger0261d4 P30 ft.1L17 projectiles11DartAgile, concealable, deadly d8, |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/16/Table/1` | 0.531491 | Martial Rangged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsAssassin rifle01001d10 P120 ft.1121 projectile11SniperAnalog, backstabber, fa |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/14/Table/4` | 0.518737 | Simple Melee VVeaporารWeapon (Commercial)Item LevelPriceDamageBulkHandsUpgradesGroupWeapon TraitsBaton021d6 BL11ClubAnalog, finesse, nonlethal, parryBattleglove031d4 B-11BrawlingAgile, analog, free-ha |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/15/Table/1` | 0.509904 | ItemPriceAdvanced Melee WeaponsLevelTHILEDamageBulkHandsUpgradesGroupWeapon Traits0321d6 AL11CorrosiveDisarm, finesse, powered, razing, reach, tech0251d8 S111SwordAnalog, critical (knife), fatal d1203 |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/14/Table/5` | 0.504206 | Zero knife0121d4 CL11 |CryoAgile, finesse, powered, tech, versatile PMartial MeleeWeapoinsWeapon (Commercial)Item LevelPriceDamageBulkHandsUpgradesGroupWeapon TraitsAucturnite chakram0151d6 SL11KnifeA |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/238` | 0.501781 | Upgrade Price |

### Query 77
- Text: What is the rule about Tactical?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/707']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/707', 'PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/250', 'PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/339']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/707` | 0.818735 | Tactical |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/250` | 0.818735 | Tactical |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/339` | 0.720023 | Battery, tactical |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/359` | 0.554770 | Chem tank, tactical |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/329` | 0.530551 | Battery, commercial Battery, tactical |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/8/Text/2` | 0.409392 | **Ranged Trip:** The weapon can be used to Trip with the  Athletics skill within the weapon's first range increment. The  skill check takes a –2 circumstance penalty. You can add the  weapon's item bo |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/8/Text/12` | 0.393355 | **Trip:** You can use this weapon to Trip with the Athletics  skill even if you don't have a free hand. This uses the  weapon's reach (if different from your own) and adds the  weapon's item bonus to |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/27` | 0.391487 | Many ranged weapons have magazines (or take batteries)  to allow for multiple shots in rapid succession without the  need to reload. The magazine of a weapon indicates how  much ammunition it can hold |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/5` | 0.386902 | Bonuses and penalties apply to these rolls, just like with  other types of checks. Weapons with the tracking trait (page  258) add an item bonus to your attack rolls, improving your  ability to hit ta |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/8` | 0.382623 | Shields have statistics that follow the same rules as armor:  Price, Speed Penalty, and Bulk. See page 245 for the rules  for those statistics. Their other statistics are described here. |

### Query 78
- Text: What is the rule about bonus to your AC, the shield upgrade emits an inertial  dampening barrier, and you automatically Raise a Shield.  You can't Raise a Shield installed as a weapon upgrade any  other way. If you use the weapon for any other purpose,  the shield is no longer raised, and you no longer receive a  bonus to your AC.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/Text/8', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/10', 'PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/8` | 1.009412 | bonus to your AC, the shield upgrade emits an inertial  dampening barrier, and you automatically Raise a Shield.  You can't Raise a Shield installed as a weapon upgrade any  other way. If you use the |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/10` | 0.808290 | A shield grants a circumstance bonus to AC, but only when  the shield is raised. This requires using the Raise a Shield  action, found on page 411. |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/3` | 0.771066 | 1 Gaining a shield's circumstance bonus to AC requires using the Raise a Shield action (found on page 411). |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 0.712341 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/23` | 0.654566 | **Installed:** Some shields aren't held but are installed  as armor or weapon upgrades. You can Raise a Shield  installed as an armor upgrade as normal. Shields can be  installed only into weapons wit |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/4` | 0.641016 | Raise a Shield is the action most commonly used with shields.  Most shields must be held in one hand, so you can't hold  anything with that hand and Raise a Shield, and you lose its  benefits if that |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/6` | 0.592016 | If you have access to the Shield Block reaction (from your  class or from a feat), you can use it while Raising your Shield  to reduce the damage you take by an amount equal to the  shield's Hardness. |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/5` | 0.585612 | When you have a riot shield or mobile bulwark raised,  you can use the Take Cover action (page 410) to increase the  circumstance bonus to AC to +4. This lasts until the shield is  no longer raised or |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/ListItem/4` | 0.550987 | 2 Getting the higher bonus for a mobile bulwark or riot shield requires using the Take Cover action (page 410) while the  shield is raised. |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/21` | 0.547882 | **Compact:** You can Raise a Shield with your compact shield  as long as you have that hand free or are holding, but not  wielding, a light object in that hand. |

### Query 79
- Text: What is the rule about **Retractable:** This shield can collapse into a smaller form  attached to an armguard, gauntlet, glove, or jewelry for  ease of travel and to free up hands. You can use an Interact  action to deploy or retract the shield. You can't Raise a  Shield if the shield is retracted. While the shield is deployed,  it has the compact trait.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/Text/9', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/21', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/9` | 0.980586 | **Retractable:** This shield can collapse into a smaller form  attached to an armguard, gauntlet, glove, or jewelry for  ease of travel and to free up hands. You can use an Interact  action to deploy |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/21` | 0.705469 | **Compact:** You can Raise a Shield with your compact shield  as long as you have that hand free or are holding, but not  wielding, a light object in that hand. |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/4` | 0.692578 | Raise a Shield is the action most commonly used with shields.  Most shields must be held in one hand, so you can't hold  anything with that hand and Raise a Shield, and you lose its  benefits if that |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/16` | 0.588776 | **Irising** **Shield:** An irising shield is made of flexible  polycarbon with a retractable design. When retracted,  an irising shield looks like a decorative bangle, gauntlet,  or glove. When deploy |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/23` | 0.559329 | **Installed:** Some shields aren't held but are installed  as armor or weapon upgrades. You can Raise a Shield  installed as an armor upgrade as normal. Shields can be  installed only into weapons wit |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/22` | 0.550269 | **Hefty:** This shield is so heavy that raising it takes more  effort. Raising a Shield with the hefty trait is a 2-action  activity unless your Strength modifier equals or exceeds  the number with th |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 0.520348 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/18` | 0.517371 | An item with an entry of "—" must be drawn to be thrown,  which usually takes an Interact action just like drawing any  other weapon. Reloading a ranged weapon and drawing a  thrown weapon both requir |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/8` | 0.516101 | bonus to your AC, the shield upgrade emits an inertial  dampening barrier, and you automatically Raise a Shield.  You can't Raise a Shield installed as a weapon upgrade any  other way. If you use the |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/665` | 0.511930 | Retractable, tech |

### Query 80
- Text: What is the rule about Each type of shield is described in more detail below.  Designer versions of even the most basic shields are  available, often tailored to match a wielder's aesthetic irising shields molded to look like flowers or sunbursts,  deflecting shields with a kaleidoscope effect, phase shields  that project custom images, and decorated riot shields are  some of the most popular custom options.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/Text/12', 'PZO22001 Starfinder Player Core 250-267::/page/1/Text/18', 'PZO22001 Starfinder Player Core 250-267::/page/2/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/12` | 0.986733 | Each type of shield is described in more detail below.  Designer versions of even the most basic shields are  available, often tailored to match a wielder's aesthetic irising shields molded to look li |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/18` | 0.710503 | **Phase** **Shield:** A phase shield is an intricate but durable  technological device often worn strapped to a limb or belt  that projects a protective hardlight barrier when deployed.  Phase shields |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/2/Text/2` | 0.669104 | **Riot** **Shield:** Riot shields are constructed from sheets of  transparent aluminum reinforced with nanocarbon panels  layered over polymers or resins. These sleek but sturdy  shields are designed |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/16` | 0.608341 | **Irising** **Shield:** An irising shield is made of flexible  polycarbon with a retractable design. When retracted,  an irising shield looks like a decorative bangle, gauntlet,  or glove. When deploy |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/20` | 0.570843 | **Archaic:** This shield is crafted using traditional methods  and materials but isn't suitable for withstanding attacks  from modern weapons. All shields from Pathfinder have the  archaic trait. Shie |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/14` | 0.555844 | **Compact** **Shield:** This sleek shield is a favorite of  operatives and other mobile combatants. It's most common  design is a polycarbon panel contoured to fit snugly over a  forearm or other limb |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/16` | 0.550545 | A shield can be used as a martial weapon for attacks, using  the statistics listed for a shield bash on the Martial Melee  Weapons table (page 264). The shield bash is an option only  for shields that |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/18` | 0.536301 | Shields can have the following traits. |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/23` | 0.530645 | **Installed:** Some shields aren't held but are installed  as armor or weapon upgrades. You can Raise a Shield  installed as an armor upgrade as normal. Shields can be  installed only into weapons wit |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/4` | 0.523878 | Raise a Shield is the action most commonly used with shields.  Most shields must be held in one hand, so you can't hold  anything with that hand and Raise a Shield, and you lose its  benefits if that |

### Query 81
- Text: What is the rule about **Carbon** **Shield:** This durable yet lightweight defensive  plate comes in a variety of shapes and sizes, and it's often  customized with LED displays that broadcast personal  insignia or an organization's colors and symbols.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/Text/13', 'PZO22001 Starfinder Player Core 250-267::/page/1/Text/14', 'PZO22001 Starfinder Player Core 250-267::/page/1/Text/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/13` | 0.974580 | **Carbon** **Shield:** This durable yet lightweight defensive  plate comes in a variety of shapes and sizes, and it's often  customized with LED displays that broadcast personal  insignia or an organi |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/14` | 0.631103 | **Compact** **Shield:** This sleek shield is a favorite of  operatives and other mobile combatants. It's most common  design is a polycarbon panel contoured to fit snugly over a  forearm or other limb |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/16` | 0.630043 | **Irising** **Shield:** An irising shield is made of flexible  polycarbon with a retractable design. When retracted,  an irising shield looks like a decorative bangle, gauntlet,  or glove. When deploy |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/18` | 0.562995 | **Phase** **Shield:** A phase shield is an intricate but durable  technological device often worn strapped to a limb or belt  that projects a protective hardlight barrier when deployed.  Phase shields |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/630` | 0.540470 | Carbon shield, commercial |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/2/Text/2` | 0.537459 | **Riot** **Shield:** Riot shields are constructed from sheets of  transparent aluminum reinforced with nanocarbon panels  layered over polymers or resins. These sleek but sturdy  shields are designed |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/10` | 0.530624 | **Tech:** This shield incorporates electronics, computer  systems, and integrated power sources. |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/15` | 0.506796 | **Deflecting** **Field:** This shield isn't held—instead, it's  installed as an armor or weapon upgrade. A deflecting  field appears as a translucent panel integrated into  the upgraded item and creat |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/12/Text/17` | 0.503843 | **Stellar** **Cannon:** The rounds of this portable cannon are  loaded with carefully positioned mini-missiles packed with  flechettes that shred anyone too close to the blast. |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/17` | 0.502442 | **Mobile** **Bulwark:** This bulky shield is advertised as the  ultimate protection in battle for those strong enough to  hoist them. Mobile bulwarks create an iconic rectangular  silhouette and are p |

### Query 82
- Text: What is the rule about **Compact** **Shield:** This sleek shield is a favorite of  operatives and other mobile combatants. It's most common  design is a polycarbon panel contoured to fit snugly over a  forearm or other limb.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/Text/14', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/21', 'PZO22001 Starfinder Player Core 250-267::/page/1/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/14` | 0.963398 | **Compact** **Shield:** This sleek shield is a favorite of  operatives and other mobile combatants. It's most common  design is a polycarbon panel contoured to fit snugly over a  forearm or other limb |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/21` | 0.699449 | **Compact:** You can Raise a Shield with your compact shield  as long as you have that hand free or are holding, but not  wielding, a light object in that hand. |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/17` | 0.627785 | **Mobile** **Bulwark:** This bulky shield is advertised as the  ultimate protection in battle for those strong enough to  hoist them. Mobile bulwarks create an iconic rectangular  silhouette and are p |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/16` | 0.591112 | **Irising** **Shield:** An irising shield is made of flexible  polycarbon with a retractable design. When retracted,  an irising shield looks like a decorative bangle, gauntlet,  or glove. When deploy |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/18` | 0.568828 | **Phase** **Shield:** A phase shield is an intricate but durable  technological device often worn strapped to a limb or belt  that projects a protective hardlight barrier when deployed.  Phase shields |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/13` | 0.565646 | **Carbon** **Shield:** This durable yet lightweight defensive  plate comes in a variety of shapes and sizes, and it's often  customized with LED displays that broadcast personal  insignia or an organi |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/639` | 0.555193 | Compact shield, commercial |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/9` | 0.549550 | **Retractable:** This shield can collapse into a smaller form  attached to an armguard, gauntlet, glove, or jewelry for  ease of travel and to free up hands. You can use an Interact  action to deploy |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/22` | 0.539685 | **Hefty:** This shield is so heavy that raising it takes more  effort. Raising a Shield with the hefty trait is a 2-action  activity unless your Strength modifier equals or exceeds  the number with th |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/9/Text/36` | 0.531871 | **Laser** **Pistol:** This compact pistol is the most popular  sidearm in the Pact Worlds thanks to its reliability, durability,  and affordability. Most common laser pistols have a  lightweight polyc |

### Query 83
- Text: What is the rule about **Deflecting** **Field:** This shield isn't held—instead, it's  installed as an armor or weapon upgrade. A deflecting  field appears as a translucent panel integrated into  the upgraded item and creates a temporary protective  hardlight barrier when activated.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/Text/15', 'PZO22001 Starfinder Player Core 250-267::/page/1/Text/18', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/15` | 0.984393 | **Deflecting** **Field:** This shield isn't held—instead, it's  installed as an armor or weapon upgrade. A deflecting  field appears as a translucent panel integrated into  the upgraded item and creat |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/18` | 0.607841 | **Phase** **Shield:** A phase shield is an intricate but durable  technological device often worn strapped to a limb or belt  that projects a protective hardlight barrier when deployed.  Phase shields |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/23` | 0.604266 | **Installed:** Some shields aren't held but are installed  as armor or weapon upgrades. You can Raise a Shield  installed as an armor upgrade as normal. Shields can be  installed only into weapons wit |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/8` | 0.531109 | bonus to your AC, the shield upgrade emits an inertial  dampening barrier, and you automatically Raise a Shield.  You can't Raise a Shield installed as a weapon upgrade any  other way. If you use the |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/9` | 0.511203 | **Retractable:** This shield can collapse into a smaller form  attached to an armguard, gauntlet, glove, or jewelry for  ease of travel and to free up hands. You can use an Interact  action to deploy |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/648` | 0.504858 | Deflecting field, commercial |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/2/Text/3` | 0.503499 | body when raised while allowing them to march in tight  tactical formations. Sometimes they're transparent to allow  inexperienced wielders to see the other side while the shield  is raised, but most |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/4` | 0.501832 | Raise a Shield is the action most commonly used with shields.  Most shields must be held in one hand, so you can't hold  anything with that hand and Raise a Shield, and you lose its  benefits if that |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/16` | 0.493029 | **Irising** **Shield:** An irising shield is made of flexible  polycarbon with a retractable design. When retracted,  an irising shield looks like a decorative bangle, gauntlet,  or glove. When deploy |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/21` | 0.488305 | **Compact:** You can Raise a Shield with your compact shield  as long as you have that hand free or are holding, but not  wielding, a light object in that hand. |

### Query 84
- Text: What is the rule about **Irising** **Shield:** An irising shield is made of flexible  polycarbon with a retractable design. When retracted,  an irising shield looks like a decorative bangle, gauntlet,  or glove. When deployed, its panels flare out and form a  miniature circular shield.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/Text/16', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/4', 'PZO22001 Starfinder Player Core 250-267::/page/1/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/16` | 0.961457 | **Irising** **Shield:** An irising shield is made of flexible  polycarbon with a retractable design. When retracted,  an irising shield looks like a decorative bangle, gauntlet,  or glove. When deploy |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/4` | 0.657121 | Raise a Shield is the action most commonly used with shields.  Most shields must be held in one hand, so you can't hold  anything with that hand and Raise a Shield, and you lose its  benefits if that |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/9` | 0.647299 | **Retractable:** This shield can collapse into a smaller form  attached to an armguard, gauntlet, glove, or jewelry for  ease of travel and to free up hands. You can use an Interact  action to deploy |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/14` | 0.530114 | **Compact** **Shield:** This sleek shield is a favorite of  operatives and other mobile combatants. It's most common  design is a polycarbon panel contoured to fit snugly over a  forearm or other limb |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/23` | 0.526682 | **Installed:** Some shields aren't held but are installed  as armor or weapon upgrades. You can Raise a Shield  installed as an armor upgrade as normal. Shields can be  installed only into weapons wit |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/12` | 0.524028 | Each type of shield is described in more detail below.  Designer versions of even the most basic shields are  available, often tailored to match a wielder's aesthetic irising shields molded to look li |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/657` | 0.523081 | Irising shield, commercial |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/21` | 0.522423 | **Compact:** You can Raise a Shield with your compact shield  as long as you have that hand free or are holding, but not  wielding, a light object in that hand. |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/15` | 0.516539 | **Deflecting** **Field:** This shield isn't held—instead, it's  installed as an armor or weapon upgrade. A deflecting  field appears as a translucent panel integrated into  the upgraded item and creat |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/2/Text/2` | 0.504091 | **Riot** **Shield:** Riot shields are constructed from sheets of  transparent aluminum reinforced with nanocarbon panels  layered over polymers or resins. These sleek but sturdy  shields are designed |

### Query 85
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/Text/21', 'PZO22001 Starfinder Player Core 250-267::/page/9/Text/41', 'PZO22001 Starfinder Player Core 250-267::/page/3/Text/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/21` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/26` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/9/Text/41` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/11/Text/35` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/13/Text/3` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/7/Text/3` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/5/Text/27` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/17/Text/8` | 0.822421 | ANCESTRIES & BACKGROUNDS |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/15/Text/7` | 0.822421 | ANCESTRIES & BACKGROUNDS |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/13/Text/21` | 0.390721 | **CONDITIONS ** |

### Query 86
- Text: What is the rule about **SKILLS** **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/1/Text/23', 'PZO22001 Starfinder Player Core 250-267::/page/7/Text/5', 'PZO22001 Starfinder Player Core 250-267::/page/5/Text/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/23` | 0.909736 | **SKILLS** **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/7/Text/5` | 0.909736 | **SKILLS** **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/5/Text/29` | 0.909736 | **SKILLS** **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/11/Text/37` | 0.656535 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/28` | 0.656535 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/9/Text/43` | 0.656535 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/13/Text/5` | 0.656535 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/11/Text/38` | 0.613813 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/9/Text/44` | 0.613813 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/29` | 0.613813 | **FEATS** |

### Query 87
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/1/Text/36']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/9/Text/57', 'PZO22001 Starfinder Player Core 250-267::/page/3/Text/42', 'PZO22001 Starfinder Player Core 250-267::/page/5/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/9/Text/57` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/42` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/5/Text/42` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/7/Text/18` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/11/Text/50` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/13/Text/19` | 0.847304 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/36` | 0.847303 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/17/Text/22` | 0.776591 | SPELLS |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/15/Text/23` | 0.776591 | SPELLS |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/28` | 0.388254 | **SKILLS** |

### Query 88
- Text: What is the rule about body when raised while allowing them to march in tight  tactical formations. Sometimes they're transparent to allow  inexperienced wielders to see the other side while the shield  is raised, but most experienced warriors have no problem  seeing around these shields, and the transparent material  quickly becomes too scuffed to see through after a few hits.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/2/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/2/Text/3', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/21', 'PZO22001 Starfinder Player Core 250-267::/page/0/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/2/Text/3` | 0.951915 | body when raised while allowing them to march in tight  tactical formations. Sometimes they're transparent to allow  inexperienced wielders to see the other side while the shield  is raised, but most |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/21` | 0.584481 | **Compact:** You can Raise a Shield with your compact shield  as long as you have that hand free or are holding, but not  wielding, a light object in that hand. |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/4` | 0.571794 | Raise a Shield is the action most commonly used with shields.  Most shields must be held in one hand, so you can't hold  anything with that hand and Raise a Shield, and you lose its  benefits if that |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/2` | 0.522958 | A shield can increase your character's defense beyond the protection their armor provides. Your  character must be wielding a shield in one hand to make use of it, and it grants its bonus to AC only |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/10` | 0.487209 | A shield grants a circumstance bonus to AC, but only when  the shield is raised. This requires using the Raise a Shield  action, found on page 411. |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/8` | 0.485426 | bonus to your AC, the shield upgrade emits an inertial  dampening barrier, and you automatically Raise a Shield.  You can't Raise a Shield installed as a weapon upgrade any  other way. If you use the |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/23` | 0.484423 | **Installed:** Some shields aren't held but are installed  as armor or weapon upgrades. You can Raise a Shield  installed as an armor upgrade as normal. Shields can be  installed only into weapons wit |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/9` | 0.468078 | **Retractable:** This shield can collapse into a smaller form  attached to an armguard, gauntlet, glove, or jewelry for  ease of travel and to free up hands. You can use an Interact  action to deploy |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/1/Text/15` | 0.459567 | **Deflecting** **Field:** This shield isn't held—instead, it's  installed as an armor or weapon upgrade. A deflecting  field appears as a translucent panel integrated into  the upgraded item and creat |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/0/Text/22` | 0.459121 | **Hefty:** This shield is so heavy that raising it takes more  effort. Raising a Shield with the hefty trait is a 2-action  activity unless your Strength modifier equals or exceeds  the number with th |

### Query 89
- Text: What is the rule about Most characters in Starfinder carry weapons, ranging from simple sidearms and tactical rifles to  powered tri-bladed axes called doshkos. Full details on how you calculate the bonuses, modifiers,  and penalties for attack rolls and damage rolls are given on pages 392–394 and 398–399, but they're  summarized here, followed by the rules for weapons and dozens of weapon choices.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/3/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/3/Text/1', 'PZO22001 Starfinder Player Core 250-267::/page/3/Text/14', 'PZO22001 Starfinder Player Core 250-267::/page/3/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/1` | 1.022816 | Most characters in Starfinder carry weapons, ranging from simple sidearms and tactical rifles to  powered tri-bladed axes called doshkos. Full details on how you calculate the bonuses, modifiers,  and |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/14` | 0.614617 | **Ranged damage roll = damage die of weapon (+ ** **Strength modifier for a thrown weapon or half ** **Strength modifier for a propulsive weapon) + ** **other bonuses + penalties** |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/5` | 0.601694 | Bonuses and penalties apply to these rolls, just like with  other types of checks. Weapons with the tracking trait (page  258) add an item bonus to your attack rolls, improving your  ability to hit ta |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/15` | 0.561711 | Ranged weapons don't normally add an attribute modifier  to the damage roll, though thrown weapons add your full  Strength modifier. At higher levels, most characters also gain  extra damage from weap |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/9/Text/22` | 0.555727 | Each of the weapons listed in the weapon tables (pages 264– 267) are described in more detail below. |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/6/Text/15` | 0.552652 | **Kickback:** A kickback weapon is extra powerful and difficult  to use. A kickback weapon deals 1 additional damage with all  attacks. Firing a kickback weapon give a –2 circumstance penalty  to the |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/6` | 0.540976 | **Melee attack roll result = d20 roll + Strength ** **modifier (or optionally Dexterity modifier for ** **a finesse weapon) + proficiency bonus + other ** **bonuses + penalties** |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/8/Text/11` | 0.540427 | **Tracking:** This weapon has been developed with several  integrated targeting, stabilizing, and homing systems.  Attack rolls with this weapon gain an item bonus equal to  the listed value. Area att |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/4` | 0.529917 | When making an attack roll, determine the result by rolling  1d20 and adding your attack modifier for the weapon or  unarmed attack you're using. Modifiers for melee and ranged  attacks are calculated |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/8` | 0.529881 | with an improvised weapon. Improvised weapons are simple  weapons. You take a –2 item penalty to attack rolls with an  improvised weapon. The GM determines the amount and type  of damage the attack de |

### Query 90
- Text: What is the rule about ATTACK ROLLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/3/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/3/SectionHeader/3', 'PZO22001 Starfinder Player Core 250-267::/page/3/SectionHeader/11', 'PZO22001 Starfinder Player Core 250-267::/page/3/Text/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/3/SectionHeader/3` | 0.903165 | ATTACK ROLLS |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/3/SectionHeader/11` | 0.655802 | DAMAGE ROLLS |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/12` | 0.559846 | When the result of your attack roll with a weapon or unarmed  attack equals or exceeds your target's AC, you hit your target!  Roll the weapon or unarmed attack's damage die and add  the relevant modi |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/4` | 0.511309 | When making an attack roll, determine the result by rolling  1d20 and adding your attack modifier for the weapon or  unarmed attack you're using. Modifiers for melee and ranged  attacks are calculated |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/14` | 0.481054 | Ranged and thrown weapons have a range increment.  Attacks with these weapons work normally up to that  distance. Attack rolls beyond a weapon's range increment  take a –2 penalty for each additional |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/5` | 0.460925 | Bonuses and penalties apply to these rolls, just like with  other types of checks. Weapons with the tracking trait (page  258) add an item bonus to your attack rolls, improving your  ability to hit ta |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/8` | 0.453386 | with an improvised weapon. Improvised weapons are simple  weapons. You take a –2 item penalty to attack rolls with an  improvised weapon. The GM determines the amount and type  of damage the attack de |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/3/SectionHeader/19` | 0.438740 | UNARMED ATTACKS |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/7` | 0.424333 | **Ranged attack roll result = d20 roll + Dexterity ** **modifier + proficiency bonus + other bonuses + ** **penalties** |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/13` | 0.418871 | **Melee damage roll = damage die of weapon or ** **unarmed attack + Strength modifier + bonuses ** **+ penalties** |

### Query 91
- Text: What is the rule about When making an attack roll, determine the result by rolling  1d20 and adding your attack modifier for the weapon or  unarmed attack you're using. Modifiers for melee and ranged  attacks are calculated differently.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/3/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/3/Text/4', 'PZO22001 Starfinder Player Core 250-267::/page/3/Text/12', 'PZO22001 Starfinder Player Core 250-267::/page/3/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/4` | 0.983174 | When making an attack roll, determine the result by rolling  1d20 and adding your attack modifier for the weapon or  unarmed attack you're using. Modifiers for melee and ranged  attacks are calculated |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/12` | 0.732686 | When the result of your attack roll with a weapon or unarmed  attack equals or exceeds your target's AC, you hit your target!  Roll the weapon or unarmed attack's damage die and add  the relevant modi |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/6` | 0.678737 | **Melee attack roll result = d20 roll + Strength ** **modifier (or optionally Dexterity modifier for ** **a finesse weapon) + proficiency bonus + other ** **bonuses + penalties** |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/7` | 0.644793 | **Ranged attack roll result = d20 roll + Dexterity ** **modifier + proficiency bonus + other bonuses + ** **penalties** |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/14` | 0.624886 | Ranged and thrown weapons have a range increment.  Attacks with these weapons work normally up to that  distance. Attack rolls beyond a weapon's range increment  take a –2 penalty for each additional |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/14` | 0.620789 | **Ranged damage roll = damage die of weapon (+ ** **Strength modifier for a thrown weapon or half ** **Strength modifier for a propulsive weapon) + ** **other bonuses + penalties** |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/15` | 0.614720 | Ranged weapons don't normally add an attribute modifier  to the damage roll, though thrown weapons add your full  Strength modifier. At higher levels, most characters also gain  extra damage from weap |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/13` | 0.592791 | **Melee damage roll = damage die of weapon or ** **unarmed attack + Strength modifier + bonuses ** **+ penalties** |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/8` | 0.592414 | with an improvised weapon. Improvised weapons are simple  weapons. You take a –2 item penalty to attack rolls with an  improvised weapon. The GM determines the amount and type  of damage the attack de |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/8/Text/10` | 0.570582 | **Thrown:** You can throw this weapon as a ranged attack;  it's a ranged weapon when thrown. You add your Strength  modifier to damage as you would for a melee weapon. When  this trait appears on a me |

### Query 92
- Text: What is the rule about Bonuses and penalties apply to these rolls, just like with  other types of checks. Weapons with the tracking trait (page  258) add an item bonus to your attack rolls, improving your  ability to hit targets.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/3/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/3/Text/5', 'PZO22001 Starfinder Player Core 250-267::/page/8/Text/11', 'PZO22001 Starfinder Player Core 250-267::/page/6/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/5` | 0.988761 | Bonuses and penalties apply to these rolls, just like with  other types of checks. Weapons with the tracking trait (page  258) add an item bonus to your attack rolls, improving your  ability to hit ta |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/8/Text/11` | 0.694380 | **Tracking:** This weapon has been developed with several  integrated targeting, stabilizing, and homing systems.  Attack rolls with this weapon gain an item bonus equal to  the listed value. Area att |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/6/Text/20` | 0.673917 | **Professional:** A weapon with this trait can be used as a  toolkit for the listed skill. Add the weapon's item bonus to  attack rolls as an item bonus to skill checks using the listed  skill. For pu |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/6/Text/15` | 0.595949 | **Kickback:** A kickback weapon is extra powerful and difficult  to use. A kickback weapon deals 1 additional damage with all  attacks. Firing a kickback weapon give a –2 circumstance penalty  to the |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/14` | 0.587175 | **Ranged damage roll = damage die of weapon (+ ** **Strength modifier for a thrown weapon or half ** **Strength modifier for a propulsive weapon) + ** **other bonuses + penalties** |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/8/Text/2` | 0.584635 | **Ranged Trip:** The weapon can be used to Trip with the  Athletics skill within the weapon's first range increment. The  skill check takes a –2 circumstance penalty. You can add the  weapon's item bo |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/8/Text/12` | 0.583794 | **Trip:** You can use this weapon to Trip with the Athletics  skill even if you don't have a free hand. This uses the  weapon's reach (if different from your own) and adds the  weapon's item bonus to |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/5/Text/23` | 0.575565 | **Boost:** You can charge up a weapon with this special  property with an Interact action to add an additional damage  die of the listed size to the next attack you make with the  weapon. The damage f |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/8` | 0.568946 | with an improvised weapon. Improvised weapons are simple  weapons. You take a –2 item penalty to attack rolls with an  improvised weapon. The GM determines the amount and type  of damage the attack de |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/6` | 0.559033 | **Melee attack roll result = d20 roll + Strength ** **modifier (or optionally Dexterity modifier for ** **a finesse weapon) + proficiency bonus + other ** **bonuses + penalties** |

### Query 93
- Text: What is the rule about **Melee attack roll result = d20 roll + Strength ** **modifier (or optionally Dexterity modifier for ** **a finesse weapon) + proficiency bonus + other ** **bonuses + penalties**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/3/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/3/Text/6', 'PZO22001 Starfinder Player Core 250-267::/page/3/Text/7', 'PZO22001 Starfinder Player Core 250-267::/page/3/Text/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/6` | 0.963403 | **Melee attack roll result = d20 roll + Strength ** **modifier (or optionally Dexterity modifier for ** **a finesse weapon) + proficiency bonus + other ** **bonuses + penalties** |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/7` | 0.798608 | **Ranged attack roll result = d20 roll + Dexterity ** **modifier + proficiency bonus + other bonuses + ** **penalties** |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/13` | 0.752945 | **Melee damage roll = damage die of weapon or ** **unarmed attack + Strength modifier + bonuses ** **+ penalties** |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/14` | 0.658347 | **Ranged damage roll = damage die of weapon (+ ** **Strength modifier for a thrown weapon or half ** **Strength modifier for a propulsive weapon) + ** **other bonuses + penalties** |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/6/Text/8` | 0.652282 | **Finesse:** You can use your Dexterity modifier instead of  your Strength modifier on attack rolls using this melee  weapon. You still calculate damage using Strength. |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/4` | 0.643769 | When making an attack roll, determine the result by rolling  1d20 and adding your attack modifier for the weapon or  unarmed attack you're using. Modifiers for melee and ranged  attacks are calculated |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/5` | 0.563140 | Bonuses and penalties apply to these rolls, just like with  other types of checks. Weapons with the tracking trait (page  258) add an item bonus to your attack rolls, improving your  ability to hit ta |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/6/Text/20` | 0.562645 | **Professional:** A weapon with this trait can be used as a  toolkit for the listed skill. Add the weapon's item bonus to  attack rolls as an item bonus to skill checks using the listed  skill. For pu |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/15` | 0.545357 | Ranged weapons don't normally add an attribute modifier  to the damage roll, though thrown weapons add your full  Strength modifier. At higher levels, most characters also gain  extra damage from weap |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/8` | 0.544706 | with an improvised weapon. Improvised weapons are simple  weapons. You take a –2 item penalty to attack rolls with an  improvised weapon. The GM determines the amount and type  of damage the attack de |

### Query 94
- Text: What is the rule about **Ranged attack roll result = d20 roll + Dexterity ** **modifier + proficiency bonus + other bonuses + ** **penalties**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/3/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/3/Text/7', 'PZO22001 Starfinder Player Core 250-267::/page/3/Text/6', 'PZO22001 Starfinder Player Core 250-267::/page/3/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/7` | 0.950954 | **Ranged attack roll result = d20 roll + Dexterity ** **modifier + proficiency bonus + other bonuses + ** **penalties** |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/6` | 0.768365 | **Melee attack roll result = d20 roll + Strength ** **modifier (or optionally Dexterity modifier for ** **a finesse weapon) + proficiency bonus + other ** **bonuses + penalties** |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/4` | 0.694912 | When making an attack roll, determine the result by rolling  1d20 and adding your attack modifier for the weapon or  unarmed attack you're using. Modifiers for melee and ranged  attacks are calculated |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/14` | 0.609893 | **Ranged damage roll = damage die of weapon (+ ** **Strength modifier for a thrown weapon or half ** **Strength modifier for a propulsive weapon) + ** **other bonuses + penalties** |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/5` | 0.551042 | Bonuses and penalties apply to these rolls, just like with  other types of checks. Weapons with the tracking trait (page  258) add an item bonus to your attack rolls, improving your  ability to hit ta |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/6/Text/20` | 0.527240 | **Professional:** A weapon with this trait can be used as a  toolkit for the listed skill. Add the weapon's item bonus to  attack rolls as an item bonus to skill checks using the listed  skill. For pu |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/12` | 0.526067 | When the result of your attack roll with a weapon or unarmed  attack equals or exceeds your target's AC, you hit your target!  Roll the weapon or unarmed attack's damage die and add  the relevant modi |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/6/Text/8` | 0.520752 | **Finesse:** You can use your Dexterity modifier instead of  your Strength modifier on attack rolls using this melee  weapon. You still calculate damage using Strength. |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/15` | 0.515726 | Ranged weapons don't normally add an attribute modifier  to the damage roll, though thrown weapons add your full  Strength modifier. At higher levels, most characters also gain  extra damage from weap |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/8` | 0.511790 | with an improvised weapon. Improvised weapons are simple  weapons. You take a –2 item penalty to attack rolls with an  improvised weapon. The GM determines the amount and type  of damage the attack de |

### Query 95
- Text: What is the rule about MULTIPLE ATTACK PENALTY?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/3/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/3/SectionHeader/8', 'PZO22001 Starfinder Player Core 250-267::/page/3/Text/9', 'PZO22001 Starfinder Player Core 250-267::/page/3/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/3/SectionHeader/8` | 0.928067 | MULTIPLE ATTACK PENALTY |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/9` | 0.696985 | If you use an action with the attack trait more than once  on the same turn, your attacks after the first take a penalty  called a multiple attack penalty. Your second attack  takes a –5 penalty, and |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/10` | 0.641059 | The multiple attack penalty doesn't apply to attacks you  make when it isn't your turn (such as attacks made as part of  a reaction). You can use a weapon with the agile trait (page  255) to reduce yo |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/5/Text/13` | 0.538282 | **Agile:** The multiple attack penalty you take with this weapon  on the second attack on your turn is –4 instead of –5, and –8  instead of –10 on the third and subsequent attacks in the turn. |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/14` | 0.483556 | Ranged and thrown weapons have a range increment.  Attacks with these weapons work normally up to that  distance. Attack rolls beyond a weapon's range increment  take a –2 penalty for each additional |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/15` | 0.443414 | For example, a commercial semi-auto pistol takes no  penalty against a target up to 60 feet away, a –2 penalty  against a target beyond 60 feet but up to 120 feet away, a –4  penalty against a target |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/1/TableCell/625` | 0.426973 | Speed Penalty |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/18` | 0.408006 | If you critically succeed at a Strike, your attack deals  double damage (page 410). Other attacks, such as spell attack  rolls and some uses of the Athletics skill, describe the specific  effects that |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/6/Text/17` | 0.396861 | **Nonlethal:** Attacks with this weapon are nonlethal (page  399) and are used to knock creatures unconscious instead of  kill them. You can use a nonlethal weapon to make a lethal  attack with a –2 c |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/7` | 0.393702 | **Ranged attack roll result = d20 roll + Dexterity ** **modifier + proficiency bonus + other bonuses + ** **penalties** |

### Query 96
- Text: What is the rule about If you use an action with the attack trait more than once  on the same turn, your attacks after the first take a penalty  called a multiple attack penalty. Your second attack  takes a –5 penalty, and any subsequent attacks take a  –10 penalty.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/3/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/3/Text/9', 'PZO22001 Starfinder Player Core 250-267::/page/3/Text/10', 'PZO22001 Starfinder Player Core 250-267::/page/5/Text/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/9` | 0.996467 | If you use an action with the attack trait more than once  on the same turn, your attacks after the first take a penalty  called a multiple attack penalty. Your second attack  takes a –5 penalty, and |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/10` | 0.764983 | The multiple attack penalty doesn't apply to attacks you  make when it isn't your turn (such as attacks made as part of  a reaction). You can use a weapon with the agile trait (page  255) to reduce yo |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/5/Text/13` | 0.723359 | **Agile:** The multiple attack penalty you take with this weapon  on the second attack on your turn is –4 instead of –5, and –8  instead of –10 on the third and subsequent attacks in the turn. |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/3/SectionHeader/8` | 0.559587 | MULTIPLE ATTACK PENALTY |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/18` | 0.540661 | If you critically succeed at a Strike, your attack deals  double damage (page 410). Other attacks, such as spell attack  rolls and some uses of the Athletics skill, describe the specific  effects that |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/8/Text/13` | 0.519460 | **Twin:** These weapons are used as a pair. When you attack  with a twin weapon, you add a circumstance bonus to the  damage roll equal to the weapon's number of damage dice  if you have previously at |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/14` | 0.515697 | Ranged and thrown weapons have a range increment.  Attacks with these weapons work normally up to that  distance. Attack rolls beyond a weapon's range increment  take a –2 penalty for each additional |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/5` | 0.470867 | Bonuses and penalties apply to these rolls, just like with  other types of checks. Weapons with the tracking trait (page  258) add an item bonus to your attack rolls, improving your  ability to hit ta |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/6/Text/15` | 0.464755 | **Kickback:** A kickback weapon is extra powerful and difficult  to use. A kickback weapon deals 1 additional damage with all  attacks. Firing a kickback weapon give a –2 circumstance penalty  to the |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/8` | 0.457816 | with an improvised weapon. Improvised weapons are simple  weapons. You take a –2 item penalty to attack rolls with an  improvised weapon. The GM determines the amount and type  of damage the attack de |

### Query 97
- Text: What is the rule about The multiple attack penalty doesn't apply to attacks you  make when it isn't your turn (such as attacks made as part of  a reaction). You can use a weapon with the agile trait (page  255) to reduce your multiple attack penalty.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/3/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/3/Text/10', 'PZO22001 Starfinder Player Core 250-267::/page/5/Text/13', 'PZO22001 Starfinder Player Core 250-267::/page/3/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/10` | 1.017090 | The multiple attack penalty doesn't apply to attacks you  make when it isn't your turn (such as attacks made as part of  a reaction). You can use a weapon with the agile trait (page  255) to reduce yo |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/5/Text/13` | 0.832628 | **Agile:** The multiple attack penalty you take with this weapon  on the second attack on your turn is –4 instead of –5, and –8  instead of –10 on the third and subsequent attacks in the turn. |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/9` | 0.788021 | If you use an action with the attack trait more than once  on the same turn, your attacks after the first take a penalty  called a multiple attack penalty. Your second attack  takes a –5 penalty, and |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/14` | 0.547485 | Ranged and thrown weapons have a range increment.  Attacks with these weapons work normally up to that  distance. Attack rolls beyond a weapon's range increment  take a –2 penalty for each additional |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/5` | 0.545946 | Bonuses and penalties apply to these rolls, just like with  other types of checks. Weapons with the tracking trait (page  258) add an item bonus to your attack rolls, improving your  ability to hit ta |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/3/SectionHeader/8` | 0.531641 | MULTIPLE ATTACK PENALTY |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/8/Text/13` | 0.530536 | **Twin:** These weapons are used as a pair. When you attack  with a twin weapon, you add a circumstance bonus to the  damage roll equal to the weapon's number of damage dice  if you have previously at |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/6/Text/15` | 0.527401 | **Kickback:** A kickback weapon is extra powerful and difficult  to use. A kickback weapon deals 1 additional damage with all  attacks. Firing a kickback weapon give a –2 circumstance penalty  to the |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/5/Text/9` | 0.526306 | The traits a weapon or unarmed attack has are listed in this  entry. Any trait that refers to a "weapon" can also apply to an  unarmed attack that has that trait. |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/20` | 0.523814 | Almost all characters start out trained in unarmed attacks.  You can Strike with your fist or another body part, calculating  your attack and damage rolls in the same way you would with  a weapon. Una |

### Query 98
- Text: What is the rule about DAMAGE ROLLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/3/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/3/SectionHeader/11', 'PZO22001 Starfinder Player Core 250-267::/page/3/SectionHeader/3', 'PZO22001 Starfinder Player Core 250-267::/page/3/Text/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/3/SectionHeader/11` | 0.902659 | DAMAGE ROLLS |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/3/SectionHeader/3` | 0.662047 | ATTACK ROLLS |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/12` | 0.568037 | When the result of your attack roll with a weapon or unarmed  attack equals or exceeds your target's AC, you hit your target!  Roll the weapon or unarmed attack's damage die and add  the relevant modi |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/4/SectionHeader/11` | 0.503116 | DAMAGE |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/13` | 0.500045 | **Melee damage roll = damage die of weapon or ** **unarmed attack + Strength modifier + bonuses ** **+ penalties** |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/4/SectionHeader/1` | 0.490092 | **DAMAGE DICE** |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/14` | 0.481301 | **Ranged damage roll = damage die of weapon (+ ** **Strength modifier for a thrown weapon or half ** **Strength modifier for a propulsive weapon) + ** **other bonuses + penalties** |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/8` | 0.478752 | with an improvised weapon. Improvised weapons are simple  weapons. You take a –2 item penalty to attack rolls with an  improvised weapon. The GM determines the amount and type  of damage the attack de |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/375` | 0.474893 | Damage |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/18` | 0.474893 | Damage |

### Query 99
- Text: What is the rule about When the result of your attack roll with a weapon or unarmed  attack equals or exceeds your target's AC, you hit your target!  Roll the weapon or unarmed attack's damage die and add  the relevant modifiers, bonuses, and penalties to determine  the amount of damage you deal. Calculate a damage roll as  follows (full details are on page 398).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/3/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/3/Text/12', 'PZO22001 Starfinder Player Core 250-267::/page/3/Text/4', 'PZO22001 Starfinder Player Core 250-267::/page/3/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/12` | 1.002384 | When the result of your attack roll with a weapon or unarmed  attack equals or exceeds your target's AC, you hit your target!  Roll the weapon or unarmed attack's damage die and add  the relevant modi |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/4` | 0.763219 | When making an attack roll, determine the result by rolling  1d20 and adding your attack modifier for the weapon or  unarmed attack you're using. Modifiers for melee and ranged  attacks are calculated |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/14` | 0.696018 | **Ranged damage roll = damage die of weapon (+ ** **Strength modifier for a thrown weapon or half ** **Strength modifier for a propulsive weapon) + ** **other bonuses + penalties** |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/13` | 0.640846 | **Melee damage roll = damage die of weapon or ** **unarmed attack + Strength modifier + bonuses ** **+ penalties** |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/8/Text/21` | 0.629374 | **Axe:** Choose one creature adjacent to the initial target and  within reach. If its AC is lower than your attack roll result for  the critical hit, you deal damage to that creature equal to the  res |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/8` | 0.598905 | with an improvised weapon. Improvised weapons are simple  weapons. You take a –2 item penalty to attack rolls with an  improvised weapon. The GM determines the amount and type  of damage the attack de |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/2` | 0.597654 | Each weapon lists the damage die used for its damage  roll. Improved versions of a weapon can deal multiple  dice of damage. |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/5` | 0.593020 | Bonuses and penalties apply to these rolls, just like with  other types of checks. Weapons with the tracking trait (page  258) add an item bonus to your attack rolls, improving your  ability to hit ta |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/6/Text/5` | 0.583241 | **Deadly:** On a critical hit, the weapon adds a weapon damage  die of the listed size. Roll this after doubling the weapon's  damage. This increases to two dice for elite and ultimate grade  weapons |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/14` | 0.582379 | Ranged and thrown weapons have a range increment.  Attacks with these weapons work normally up to that  distance. Attack rolls beyond a weapon's range increment  take a –2 penalty for each additional |

### Query 100
- Text: What is the rule about **Melee damage roll = damage die of weapon or ** **unarmed attack + Strength modifier + bonuses ** **+ penalties**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/3/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/3/Text/13', 'PZO22001 Starfinder Player Core 250-267::/page/3/Text/6', 'PZO22001 Starfinder Player Core 250-267::/page/3/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/13` | 0.962765 | **Melee damage roll = damage die of weapon or ** **unarmed attack + Strength modifier + bonuses ** **+ penalties** |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/6` | 0.746254 | **Melee attack roll result = d20 roll + Strength ** **modifier (or optionally Dexterity modifier for ** **a finesse weapon) + proficiency bonus + other ** **bonuses + penalties** |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/14` | 0.702142 | **Ranged damage roll = damage die of weapon (+ ** **Strength modifier for a thrown weapon or half ** **Strength modifier for a propulsive weapon) + ** **other bonuses + penalties** |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/12` | 0.628156 | When the result of your attack roll with a weapon or unarmed  attack equals or exceeds your target's AC, you hit your target!  Roll the weapon or unarmed attack's damage die and add  the relevant modi |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/4` | 0.592384 | When making an attack roll, determine the result by rolling  1d20 and adding your attack modifier for the weapon or  unarmed attack you're using. Modifiers for melee and ranged  attacks are calculated |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/6/Text/8` | 0.546504 | **Finesse:** You can use your Dexterity modifier instead of  your Strength modifier on attack rolls using this melee  weapon. You still calculate damage using Strength. |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/8` | 0.540880 | with an improvised weapon. Improvised weapons are simple  weapons. You take a –2 item penalty to attack rolls with an  improvised weapon. The GM determines the amount and type  of damage the attack de |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/15` | 0.526359 | Ranged weapons don't normally add an attribute modifier  to the damage roll, though thrown weapons add your full  Strength modifier. At higher levels, most characters also gain  extra damage from weap |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/2` | 0.526052 | Each weapon lists the damage die used for its damage  roll. Improved versions of a weapon can deal multiple  dice of damage. |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/9/Text/4` | 0.526052 | **Dart:** The target takes 1d6 persistent bleed damage.  You gain an item bonus to this bleed damage equal to the  weapon's item bonus to attack rolls. |

### Query 101
- Text: What is the rule about **Ranged damage roll = damage die of weapon (+ ** **Strength modifier for a thrown weapon or half ** **Strength modifier for a propulsive weapon) + ** **other bonuses + penalties**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/3/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/3/Text/14', 'PZO22001 Starfinder Player Core 250-267::/page/3/Text/15', 'PZO22001 Starfinder Player Core 250-267::/page/3/Text/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/14` | 0.952583 | **Ranged damage roll = damage die of weapon (+ ** **Strength modifier for a thrown weapon or half ** **Strength modifier for a propulsive weapon) + ** **other bonuses + penalties** |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/15` | 0.693796 | Ranged weapons don't normally add an attribute modifier  to the damage roll, though thrown weapons add your full  Strength modifier. At higher levels, most characters also gain  extra damage from weap |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/13` | 0.672667 | **Melee damage roll = damage die of weapon or ** **unarmed attack + Strength modifier + bonuses ** **+ penalties** |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/8` | 0.620455 | with an improvised weapon. Improvised weapons are simple  weapons. You take a –2 item penalty to attack rolls with an  improvised weapon. The GM determines the amount and type  of damage the attack de |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/12` | 0.613546 | When the result of your attack roll with a weapon or unarmed  attack equals or exceeds your target's AC, you hit your target!  Roll the weapon or unarmed attack's damage die and add  the relevant modi |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/6` | 0.600880 | **Melee attack roll result = d20 roll + Strength ** **modifier (or optionally Dexterity modifier for ** **a finesse weapon) + proficiency bonus + other ** **bonuses + penalties** |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/6/Text/15` | 0.599479 | **Kickback:** A kickback weapon is extra powerful and difficult  to use. A kickback weapon deals 1 additional damage with all  attacks. Firing a kickback weapon give a –2 circumstance penalty  to the |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/14` | 0.587967 | Ranged and thrown weapons have a range increment.  Attacks with these weapons work normally up to that  distance. Attack rolls beyond a weapon's range increment  take a –2 penalty for each additional |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/4` | 0.585139 | When making an attack roll, determine the result by rolling  1d20 and adding your attack modifier for the weapon or  unarmed attack you're using. Modifiers for melee and ranged  attacks are calculated |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/4` | 0.576500 | Effects based on a weapon's number of damage dice  include only the weapon's damage die. They don't  count extra dice from abilities, critical specialization  effects, weapon fusions, weapon traits, o |

### Query 102
- Text: Lookup values for **Unarmed Attack**PriceDamageBulkHandsGroupWeapon TraitsFist_1d4 B_1BrawlingAgile, finesse, nonlethal, unarmed
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/14/Table/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/14/Table/2', 'PZO22001 Starfinder Player Core 250-267::/page/14/Table/4', 'PZO22001 Starfinder Player Core 250-267::/page/5/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/14/Table/2` | 1.000713 | **Unarmed Attack**PriceDamageBulkHandsGroupWeapon TraitsFist_1d4 B_1BrawlingAgile, finesse, nonlethal, unarmed |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/14/Table/4` | 0.697376 | Simple Melee VVeaporารWeapon (Commercial)Item LevelPriceDamageBulkHandsUpgradesGroupWeapon TraitsBaton021d6 BL11ClubAnalog, finesse, nonlethal, parryBattleglove031d4 B-11BrawlingAgile, analog, free-ha |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/5/Text/9` | 0.686912 | The traits a weapon or unarmed attack has are listed in this  entry. Any trait that refers to a "weapon" can also apply to an  unarmed attack that has that trait. |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/15/Table/3` | 0.621190 | Simple RangSimple Ranged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsAcid dart rifle0401d8 A80 ft.1125 projectiles11CorrosiveAnalogArc pi |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/8/Text/15` | 0.620929 | **Unarmed:** An unarmed attack uses your body rather  than a manufactured weapon. An unarmed attack isn't a  weapon, though it has a weapon group and might have  weapon traits. An unarmed attack can't |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/14/Table/5` | 0.615852 | Zero knife0121d4 CL11 |CryoAgile, finesse, powered, tech, versatile PMartial MeleeWeapoinsWeapon (Commercial)Item LevelPriceDamageBulkHandsUpgradesGroupWeapon TraitsAucturnite chakram0151d6 SL11KnifeA |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/3/Text/21` | 0.612019 | The unarmed attacks table (page 264) lists the statistics  for an unarmed attack with a fist, though you'll usually use  the same statistics for attacks made with any other parts of  your body. Certai |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/16` | 0.611525 | **Unarmed Attack** |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/15/Table/1` | 0.606817 | ItemPriceAdvanced Melee WeaponsLevelTHILEDamageBulkHandsUpgradesGroupWeapon Traits0321d6 AL11CorrosiveDisarm, finesse, powered, razing, reach, tech0251d8 S111SwordAnalog, critical (knife), fatal d1203 |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/16/Table/1` | 0.602722 | Martial Rangged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsAssassin rifle01001d10 P120 ft.1121 projectile11SniperAnalog, backstabber, fa |

### Query 103
- Text: Lookup values for Simple Melee VVeaporารWeapon
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/14/Table/4']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/30', 'PZO22001 Starfinder Player Core 250-267::/page/14/Table/4', 'PZO22001 Starfinder Player Core 250-267::/page/9/SectionHeader/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/30` | 0.715817 | Simple Melee V |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/14/Table/4` | 0.696986 | Simple Melee VVeaporารWeapon (Commercial)Item LevelPriceDamageBulkHandsUpgradesGroupWeapon TraitsBaton021d6 BL11ClubAnalog, finesse, nonlethal, parryBattleglove031d4 B-11BrawlingAgile, analog, free-ha |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/9/SectionHeader/23` | 0.656833 | SIMPLE MELEE WEAPONS |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/15/Table/3` | 0.542576 | Simple RangSimple Ranged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsAcid dart rifle0401d8 A80 ft.1125 projectiles11CorrosiveAnalogArc pi |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/14/SectionHeader/3` | 0.538991 | **MELEE WEAPONS ** |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/124` | 0.533922 | Advanced Melee Weapons |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/11/SectionHeader/7` | 0.525169 | MARTIAL MELEE WEAPONS |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/174` | 0.515408 | Simple Ranged Weapons |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/12/SectionHeader/19` | 0.505569 | ADVANCED MELEE WEAPONS |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/111` | 0.499261 | Martial Melee |

### Query 104
- Text: Lookup values for Zero knife0121d4 CL11 |CryoAgile, finesse, powered, tech, versatile PMartial MeleeWeapoinsWeapon
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/14/Table/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/14/Table/5', 'PZO22001 Starfinder Player Core 250-267::/page/14/Table/4', 'PZO22001 Starfinder Player Core 250-267::/page/15/Table/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/14/Table/5` | 0.810531 | Zero knife0121d4 CL11 |CryoAgile, finesse, powered, tech, versatile PMartial MeleeWeapoinsWeapon (Commercial)Item LevelPriceDamageBulkHandsUpgradesGroupWeapon TraitsAucturnite chakram0151d6 SL11KnifeA |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/14/Table/4` | 0.677141 | Simple Melee VVeaporารWeapon (Commercial)Item LevelPriceDamageBulkHandsUpgradesGroupWeapon TraitsBaton021d6 BL11ClubAnalog, finesse, nonlethal, parryBattleglove031d4 B-11BrawlingAgile, analog, free-ha |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/15/Table/1` | 0.645928 | ItemPriceAdvanced Melee WeaponsLevelTHILEDamageBulkHandsUpgradesGroupWeapon Traits0321d6 AL11CorrosiveDisarm, finesse, powered, razing, reach, tech0251d8 S111SwordAnalog, critical (knife), fatal d1203 |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/16/Table/1` | 0.536119 | Martial Rangged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsAssassin rifle01001d10 P120 ft.1121 projectile11SniperAnalog, backstabber, fa |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/15/Table/3` | 0.533617 | Simple RangSimple Ranged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsAcid dart rifle0401d8 A80 ft.1125 projectiles11CorrosiveAnalogArc pi |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/102` | 0.509560 | Zero knife |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/17/Table/0` | 0.503152 | Advanced RangedWeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsCard slinger0261d4 P30 ft.1L17 projectiles11DartAgile, concealable, deadly d8, |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/14/TableCell/93` | 0.497560 | Zero knife |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/14/Table/2` | 0.469484 | **Unarmed Attack**PriceDamageBulkHandsGroupWeapon TraitsFist_1d4 B_1BrawlingAgile, finesse, nonlethal, unarmed |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/15/Table/4` | 0.459586 | Martial RangMartial Ranged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsArc emitter0951d8 E20 ft.11210 charges21ShockArea (cone), nonletha |

### Query 105
- Text: Lookup values for ItemPriceAdvanced Melee WeaponsLevelTHILEDamageBulkHandsUpgradesGroupWeapon Traits0321d6 AL11CorrosiveDisarm, finesse, powered, razing, reach, tech0251d8 S111SwordAnalog, critical (knife), fatal d120301d8 F111FlameDeadly d8, two-hand d10, powered, tech0151d6
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/15/Table/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/15/Table/1', 'PZO22001 Starfinder Player Core 250-267::/page/14/Table/4', 'PZO22001 Starfinder Player Core 250-267::/page/14/Table/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/15/Table/1` | 0.975005 | ItemPriceAdvanced Melee WeaponsLevelTHILEDamageBulkHandsUpgradesGroupWeapon Traits0321d6 AL11CorrosiveDisarm, finesse, powered, razing, reach, tech0251d8 S111SwordAnalog, critical (knife), fatal d1203 |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/14/Table/4` | 0.822058 | Simple Melee VVeaporารWeapon (Commercial)Item LevelPriceDamageBulkHandsUpgradesGroupWeapon TraitsBaton021d6 BL11ClubAnalog, finesse, nonlethal, parryBattleglove031d4 B-11BrawlingAgile, analog, free-ha |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/14/Table/5` | 0.819021 | Zero knife0121d4 CL11 |CryoAgile, finesse, powered, tech, versatile PMartial MeleeWeapoinsWeapon (Commercial)Item LevelPriceDamageBulkHandsUpgradesGroupWeapon TraitsAucturnite chakram0151d6 SL11KnifeA |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/16/Table/1` | 0.740597 | Martial Rangged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsAssassin rifle01001d10 P120 ft.1121 projectile11SniperAnalog, backstabber, fa |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/15/Table/3` | 0.728226 | Simple RangSimple Ranged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsAcid dart rifle0401d8 A80 ft.1125 projectiles11CorrosiveAnalogArc pi |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/17/Table/0` | 0.725883 | Advanced RangedWeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsCard slinger0261d4 P30 ft.1L17 projectiles11DartAgile, concealable, deadly d8, |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/14/Table/2` | 0.613638 | **Unarmed Attack**PriceDamageBulkHandsGroupWeapon TraitsFist_1d4 B_1BrawlingAgile, finesse, nonlethal, unarmed |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/15/Table/4` | 0.607581 | Martial RangMartial Ranged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsArc emitter0951d8 E20 ft.11210 charges21ShockArea (cone), nonletha |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/17/Table/1` | 0.574440 | Weapon ImprovvementsGradeLevelUpgrade PriceTotal Value1UpgradesDamage DiceTraitsCommercial0--+01-Tactical2+350 credits350 credits+01Tracking +1Advanced4+650 credits1,000 credits+12Tracking +1Superior1 |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/124` | 0.565599 | Advanced Melee Weapons |

### Query 106
- Text: Lookup values for Simple RangSimple Ranged WeaponsWeapon
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/15/Table/3']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/174', 'PZO22001 Starfinder Player Core 250-267::/page/9/SectionHeader/30', 'PZO22001 Starfinder Player Core 250-267::/page/15/Table/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/174` | 0.799881 | Simple Ranged Weapons |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/9/SectionHeader/30` | 0.723642 | SIMPLE RANGED WEAPONS |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/15/Table/3` | 0.706465 | Simple RangSimple Ranged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsAcid dart rifle0401d8 A80 ft.1125 projectiles11CorrosiveAnalogArc pi |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/371` | 0.634067 | Martial Ranged Weapons |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/173` | 0.616994 | Simple Rang |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/15/SectionHeader/2` | 0.610449 | **RANGED WEAPONS ** |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/16/Table/1` | 0.594737 | Martial Rangged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsAssassin rifle01001d10 P120 ft.1121 projectile11SniperAnalog, backstabber, fa |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/17/Table/0` | 0.570912 | Advanced RangedWeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsCard slinger0261d4 P30 ft.1L17 projectiles11DartAgile, concealable, deadly d8, |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/14/Table/4` | 0.563658 | Simple Melee VVeaporารWeapon (Commercial)Item LevelPriceDamageBulkHandsUpgradesGroupWeapon TraitsBaton021d6 BL11ClubAnalog, finesse, nonlethal, parryBattleglove031d4 B-11BrawlingAgile, analog, free-ha |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/12/SectionHeader/3` | 0.551948 | MARTIAL RANGED WEAPONS |

### Query 107
- Text: Lookup values for Martial RangMartial Ranged WeaponsWeapon
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/15/Table/4']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/371', 'PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/370', 'PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/371` | 0.806401 | Martial Ranged Weapons |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/370` | 0.718846 | Martial Rang |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/8` | 0.718846 | Martial Rang |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/12/SectionHeader/3` | 0.668383 | MARTIAL RANGED WEAPONS |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/15/Table/4` | 0.663134 | Martial RangMartial Ranged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsArc emitter0951d8 E20 ft.11210 charges21ShockArea (cone), nonletha |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/16/Table/1` | 0.659176 | Martial Rangged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsAssassin rifle01001d10 P120 ft.1121 projectile11SniperAnalog, backstabber, fa |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/15/Table/3` | 0.626163 | Simple RangSimple Ranged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsAcid dart rifle0401d8 A80 ft.1125 projectiles11CorrosiveAnalogArc pi |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/174` | 0.616193 | Simple Ranged Weapons |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/17/Table/0` | 0.606447 | Advanced RangedWeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsCard slinger0261d4 P30 ft.1L17 projectiles11DartAgile, concealable, deadly d8, |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/15/SectionHeader/2` | 0.588335 | **RANGED WEAPONS ** |

### Query 108
- Text: Lookup values for Martial Rangged WeaponsWeapon
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/16/Table/1']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/371', 'PZO22001 Starfinder Player Core 250-267::/page/12/SectionHeader/3', 'PZO22001 Starfinder Player Core 250-267::/page/16/Table/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/371` | 0.791376 | Martial Ranged Weapons |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/12/SectionHeader/3` | 0.747487 | MARTIAL RANGED WEAPONS |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/16/Table/1` | 0.689922 | Martial Rangged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsAssassin rifle01001d10 P120 ft.1121 projectile11SniperAnalog, backstabber, fa |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/15/SectionHeader/2` | 0.630658 | **RANGED WEAPONS ** |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/174` | 0.620414 | Simple Ranged Weapons |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/9/SectionHeader/30` | 0.612016 | SIMPLE RANGED WEAPONS |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/12/SectionHeader/24` | 0.606337 | ADVANCED RANGED WEAPONS |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/15/Table/3` | 0.596550 | Simple RangSimple Ranged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsAcid dart rifle0401d8 A80 ft.1125 projectiles11CorrosiveAnalogArc pi |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/15/Table/4` | 0.591943 | Martial RangMartial Ranged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsArc emitter0951d8 E20 ft.11210 charges21ShockArea (cone), nonletha |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/370` | 0.590232 | Martial Rang |

### Query 109
- Text: Lookup values for Advanced RangedWeaponsWeapon
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/17/Table/0']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/12/SectionHeader/24', 'PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/371', 'PZO22001 Starfinder Player Core 250-267::/page/17/Table/0']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/12/SectionHeader/24` | 0.707757 | ADVANCED RANGED WEAPONS |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/371` | 0.677256 | Martial Ranged Weapons |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/17/Table/0` | 0.631714 | Advanced RangedWeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsCard slinger0261d4 P30 ft.1L17 projectiles11DartAgile, concealable, deadly d8, |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/124` | 0.588067 | Advanced Melee Weapons |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/174` | 0.587177 | Simple Ranged Weapons |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/15/SectionHeader/2` | 0.584643 | **RANGED WEAPONS ** |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/16/Table/1` | 0.572671 | Martial Rangged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsAssassin rifle01001d10 P120 ft.1121 projectile11SniperAnalog, backstabber, fa |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/12/SectionHeader/3` | 0.565878 | MARTIAL RANGED WEAPONS |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/15/Table/3` | 0.565716 | Simple RangSimple Ranged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsAcid dart rifle0401d8 A80 ft.1125 projectiles11CorrosiveAnalogArc pi |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/4/Text/10` | 0.535668 | Each of the weapons in the weapon tables (pages 264–267)  lists the statistics for various melee and ranged weapons that  you can purchase. The tables present the following statistics. |

### Query 110
- Text: Lookup values for Weapon ImprovvementsGradeLevelUpgrade PriceTotal Value1UpgradesDamage DiceTraitsCommercial0--+01-Tactical2+350 credits350 credits+01Tracking +1Advanced4+650 credits1,000 credits+12Tracking +1Superior10+9,000 credits10,000 credits+12Tracking +2Elite12+10,000 credits20,000 credits+23Tracking +2Ultimate16+80,000 credits100,000 credits+23Tracking +3Paragon19+300,000 credits400,000 credits+34Tracking +31 Total value doeTotal value doesn't include the price of the base commercial weapon.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/17/Table/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/17/Table/1', 'PZO22001 Starfinder Player Core 250-267::/page/1/Table/6', 'PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/293']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/17/Table/1` | 1.017163 | Weapon ImprovvementsGradeLevelUpgrade PriceTotal Value1UpgradesDamage DiceTraitsCommercial0--+01-Tactical2+350 credits350 credits+01Tracking +1Advanced4+650 credits1,000 credits+12Tracking +1Superior1 |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/1/Table/6` | 0.772333 | GradeLevelUpgrade PriceTotal Value1HardnessHPBTCommercial0—————Tactical5+750 credits750 credits+3+46+23Advanced8+2,250 credits3,000 credits+3+56+28Superior11+6,000 credits9,000 credits+3+68+34Elite14+ |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/293` | 0.703211 | Total value doesn't include the price of the base commercial weapon. |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/15/Table/3` | 0.632390 | Simple RangSimple Ranged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsAcid dart rifle0401d8 A80 ft.1125 projectiles11CorrosiveAnalogArc pi |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/16/Table/1` | 0.627685 | Martial Rangged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsAssassin rifle01001d10 P120 ft.1121 projectile11SniperAnalog, backstabber, fa |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/17/Table/0` | 0.610834 | Advanced RangedWeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsCard slinger0261d4 P30 ft.1L17 projectiles11DartAgile, concealable, deadly d8, |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/15/Table/1` | 0.604049 | ItemPriceAdvanced Melee WeaponsLevelTHILEDamageBulkHandsUpgradesGroupWeapon Traits0321d6 AL11CorrosiveDisarm, finesse, powered, razing, reach, tech0251d8 S111SwordAnalog, critical (knife), fatal d1203 |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/14/Table/4` | 0.593526 | Simple Melee VVeaporารWeapon (Commercial)Item LevelPriceDamageBulkHandsUpgradesGroupWeapon TraitsBaton021d6 BL11ClubAnalog, finesse, nonlethal, parryBattleglove031d4 B-11BrawlingAgile, analog, free-ha |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/14/Table/5` | 0.555532 | Zero knife0121d4 CL11 |CryoAgile, finesse, powered, tech, versatile PMartial MeleeWeapoinsWeapon (Commercial)Item LevelPriceDamageBulkHandsUpgradesGroupWeapon TraitsAucturnite chakram0151d6 SL11KnifeA |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/8/Text/11` | 0.548835 | **Tracking:** This weapon has been developed with several  integrated targeting, stabilizing, and homing systems.  Attack rolls with this weapon gain an item bonus equal to  the listed value. Area att |

### Query 111
- Text: Lookup values for Projectile AmmoAmmunitionItem
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/17/Table/4']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/294', 'PZO22001 Starfinder Player Core 250-267::/page/17/Table/4', 'PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/304']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/294` | 0.751145 | Projectile Ammo |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/17/Table/4` | 0.665328 | Projectile AmmoAmmunitionItem LevelPriceMagazineBulkProjectile ammo (10)01--BatteriesAmmunitionItemPriceMagazineBulkLevelMagazinioDuikBattery, commercialLevel 01010- JulikBattery, commercial Battery, |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/304` | 0.658855 | Projectile ammo (10) |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/5/Text/1` | 0.572431 | tanks and otherwise function as batteries. Chemicals can't be  recharged, and new chems must be purchased after a tank is  expended. Most projectile weapons have magazines that hold  a maximum number |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/15/Table/3` | 0.557508 | Simple RangSimple Ranged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsAcid dart rifle0401d8 A80 ft.1125 projectiles11CorrosiveAnalogArc pi |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/326` | 0.544019 | 1 projectiles |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/342` | 0.540358 | Projectile |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/16/TableCell/201` | 0.540358 | Projectile |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/303` | 0.540358 | Projectile |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/15/TableCell/316` | 0.540358 | Projectile |

### Query 112
- Text: Lookup values for Chem TanksAmmunitionItem
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 250-267::/page/17/Table/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 250-267::/page/17/Table/5', 'PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/344', 'PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/359']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 250-267::/page/17/Table/5` | 0.805506 | Chem TanksAmmunitionItem LevelPriceMagazineBulkChem tank, commercial058-Chem tank, tactical21016_Chem tank, advanced42040-Chem tank, superior103048LChem tank, elite125064L |
| 2 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/344` | 0.727122 | Chem Tanks |
| 3 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/359` | 0.659456 | Chem tank, tactical |
| 4 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/364` | 0.586863 | Chem tank, advanced |
| 5 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/354` | 0.578218 | Chem tank, commercial |
| 6 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/369` | 0.564328 | Chem tank, superior |
| 7 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/374` | 0.547259 | Chem tank, elite |
| 8 | `PZO22001 Starfinder Player Core 250-267::/page/15/Table/3` | 0.537098 | Simple RangSimple Ranged WeaponsWeapon (Commercial)Item LevelPriceDamageRangeReloadBulkHandsMagazineExpendUpgradesGroupWeapon TraitsAcid dart rifle0401d8 A80 ft.1125 projectiles11CorrosiveAnalogArc pi |
| 9 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/349` | 0.519524 | Ammunition |
| 10 | `PZO22001 Starfinder Player Core 250-267::/page/17/TableCell/314` | 0.507524 | Ammunition |
