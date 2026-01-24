# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `1558`
- Query count: `161`
- Evaluated queries: `161`
- Coverage: `1.0000`
- MRR: `0.7764`
- hit@1: `0.7267`
- hit@3: `0.8012`
- hit@5: `0.8323`
- hit@10: `0.8758`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

## Timings (ms)
- Embedding (chunks): `18880`
- Embedding (queries): `2803`
- Evaluation (strict): `149`
- Evaluation (expanded): `0`
- Total: `26263`

### Timing Estimates (ms)
- Evaluation (strict): `547`
- Evaluation (expanded): `None`
- Total: `22230`

## Query Details
### Query 0
- Text: What is the rule about CHAPTER 5: FEATS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 210-231::/page/13/Text/63', 'PZO22001 Starfinder Player Core 210-231::/page/5/Text/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/SectionHeader/1` | 0.914492 | CHAPTER 5: FEATS |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/29` | 0.681942 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/63` | 0.681942 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/65` | 0.639942 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/56` | 0.639942 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/71` | 0.639942 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/17` | 0.639942 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/58` | 0.639942 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/3/Text/7` | 0.639942 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/1/SectionHeader/8` | 0.534593 | **GENERAL FEATS** |

### Query 1
- Text: What is the rule about All kinds of experiences and training can shape your character beyond what you learn by advancing in  your class. Abilities that require a degree of training but can be learned by anyone—not only members  of certain ancestries or classes—are called general feats.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/Text/2', 'PZO22001 Starfinder Player Core 210-231::/page/1/Text/5', 'PZO22001 Starfinder Player Core 210-231::/page/1/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/2` | 0.995882 | All kinds of experiences and training can shape your character beyond what you learn by advancing in  your class. Abilities that require a degree of training but can be learned by anyone—not only memb |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/5` | 0.751447 | General feats also include a subcategory of skill feats,  which expand on what you can accomplish via skills.  These feats also have the skill trait. Most characters gain  skill feats at 2nd level and |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/4` | 0.716572 | For most classes, you gain a general feat when you reach  3rd level and every 4 levels thereafter. Each time you gain  a general feat, you can select any feat with the general  trait whose prerequisit |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/6` | 0.646613 | you gain a skill feat, you must select a general feat with  the skill trait; you can't select a general feat that lacks the  skill trait. The level of a skill feat is typically the minimum  level at w |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/7` | 0.637432 | In addition to the skill feats specifically associated with  each skill, there are some that can be taken with various  skills or even all skills, like Assurance. |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/Table/9` | 0.585586 | Non-Skill FeatsLevelPrerequisitesBenefitsAdopted Ancestry1—Gain access to ancestry feats from another ancestryArmor Proficiency1—Become trained in a type of armorAugmented Body1—Gain a free augmentati |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/14` | 0.583871 | long as the ancestry feats don't require any physiological  feature that you lack, as determined by the GM. |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/13` | 0.553468 | You're fully immersed in another ancestry's culture and  traditions, whether born into them, earned through a rite of  passage, or bonded through a deep friendship or romance.  Choose a common ancestr |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/21/Text/20` | 0.542628 | **Special** You can select this feat more than once. Each time  you do, you become trained in an advanced weapon. |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/15` | 0.541237 | **Special** You can select this feat multiple times, choosing a new  skill to become trained in each time. |

### Query 2
- Text: What is the rule about For most classes, you gain a general feat when you reach  3rd level and every 4 levels thereafter. Each time you gain  a general feat, you can select any feat with the general  trait whose prerequisites you satisfy.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/Text/4', 'PZO22001 Starfinder Player Core 210-231::/page/1/Text/6', 'PZO22001 Starfinder Player Core 210-231::/page/1/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/4` | 0.986683 | For most classes, you gain a general feat when you reach  3rd level and every 4 levels thereafter. Each time you gain  a general feat, you can select any feat with the general  trait whose prerequisit |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/6` | 0.787992 | you gain a skill feat, you must select a general feat with  the skill trait; you can't select a general feat that lacks the  skill trait. The level of a skill feat is typically the minimum  level at w |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/5` | 0.748482 | General feats also include a subcategory of skill feats,  which expand on what you can accomplish via skills.  These feats also have the skill trait. Most characters gain  skill feats at 2nd level and |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/2` | 0.645559 | All kinds of experiences and training can shape your character beyond what you learn by advancing in  your class. Abilities that require a degree of training but can be learned by anyone—not only memb |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/31` | 0.639730 | **Special** You can select this feat multiple times. Each time,  choose a different skill and gain the benefits for that skill. |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/9` | 0.627177 | **Special** You can select this feat more than once. Each time  you must select a new subcategory of Lore, and you gain  the additional skill increases to that subcategory for the  listed levels. |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/15` | 0.612071 | **Special** You can select this feat multiple times, choosing a new  skill to become trained in each time. |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/21/Text/20` | 0.601587 | **Special** You can select this feat more than once. Each time  you do, you become trained in an advanced weapon. |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/25` | 0.593348 | **Special** You can select this feat more than once. Each time, you  become trained in the next type of armor, as detailed above. |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/33` | 0.570737 | **Special** You can select this feat multiple times. Each time, you  learn additional languages. |

### Query 3
- Text: What is the rule about General feats also include a subcategory of skill feats,  which expand on what you can accomplish via skills.  These feats also have the skill trait. Most characters gain  skill feats at 2nd level and every 2 levels thereafter. When?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/Text/5', 'PZO22001 Starfinder Player Core 210-231::/page/1/Text/6', 'PZO22001 Starfinder Player Core 210-231::/page/1/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/5` | 0.987761 | General feats also include a subcategory of skill feats,  which expand on what you can accomplish via skills.  These feats also have the skill trait. Most characters gain  skill feats at 2nd level and |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/6` | 0.774849 | you gain a skill feat, you must select a general feat with  the skill trait; you can't select a general feat that lacks the  skill trait. The level of a skill feat is typically the minimum  level at w |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/4` | 0.764604 | For most classes, you gain a general feat when you reach  3rd level and every 4 levels thereafter. Each time you gain  a general feat, you can select any feat with the general  trait whose prerequisit |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/2` | 0.656657 | All kinds of experiences and training can shape your character beyond what you learn by advancing in  your class. Abilities that require a degree of training but can be learned by anyone—not only memb |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/9` | 0.610884 | **Special** You can select this feat more than once. Each time  you must select a new subcategory of Lore, and you gain  the additional skill increases to that subcategory for the  listed levels. |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/7` | 0.603504 | In addition to the skill feats specifically associated with  each skill, there are some that can be taken with various  skills or even all skills, like Assurance. |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/413` | 0.541430 | Varying Skill Feats |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/482` | 0.541430 | Varying Skill Feats |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/31` | 0.536819 | **Special** You can select this feat multiple times. Each time,  choose a different skill and gain the benefits for that skill. |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/24` | 0.535757 | is equal to your level –2. This improves to your level –1 at 5th  level and your full level at 7th level. This doesn't allow you to  use the skill's trained actions. |

### Query 4
- Text: What is the rule about you gain a skill feat, you must select a general feat with  the skill trait; you can't select a general feat that lacks the  skill trait. The level of a skill feat is typically the minimum  level at which a character could meet its proficiency  prerequisite.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/Text/6', 'PZO22001 Starfinder Player Core 210-231::/page/1/Text/4', 'PZO22001 Starfinder Player Core 210-231::/page/1/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/6` | 1.002903 | you gain a skill feat, you must select a general feat with  the skill trait; you can't select a general feat that lacks the  skill trait. The level of a skill feat is typically the minimum  level at w |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/4` | 0.777562 | For most classes, you gain a general feat when you reach  3rd level and every 4 levels thereafter. Each time you gain  a general feat, you can select any feat with the general  trait whose prerequisit |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/5` | 0.761284 | General feats also include a subcategory of skill feats,  which expand on what you can accomplish via skills.  These feats also have the skill trait. Most characters gain  skill feats at 2nd level and |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/2` | 0.613374 | All kinds of experiences and training can shape your character beyond what you learn by advancing in  your class. Abilities that require a degree of training but can be learned by anyone—not only memb |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/9` | 0.584762 | **Special** You can select this feat more than once. Each time  you must select a new subcategory of Lore, and you gain  the additional skill increases to that subcategory for the  listed levels. |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/31` | 0.583125 | **Special** You can select this feat multiple times. Each time,  choose a different skill and gain the benefits for that skill. |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/15` | 0.576917 | **Special** You can select this feat multiple times, choosing a new  skill to become trained in each time. |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/24` | 0.573785 | is equal to your level –2. This improves to your level –1 at 5th  level and your full level at 7th level. This doesn't allow you to  use the skill's trained actions. |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/30` | 0.573404 | Even in the worst circumstances, you can perform basic tasks.  Choose a skill you're trained in. You can forgo rolling a skill check  for that skill to instead receive a result of 10 + your proficienc |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/16` | 0.558542 | You can find ways to craft just about anything, despite  restrictions. As long as you have the appropriate Crafting  skill feat (such as Magical Crafting for magic items) and meet  the item's level an |

### Query 5
- Text: What is the rule about In addition to the skill feats specifically associated with  each skill, there are some that can be taken with various  skills or even all skills, like Assurance.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/Text/7', 'PZO22001 Starfinder Player Core 210-231::/page/1/Text/5', 'PZO22001 Starfinder Player Core 210-231::/page/6/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/7` | 0.946052 | In addition to the skill feats specifically associated with  each skill, there are some that can be taken with various  skills or even all skills, like Assurance. |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/5` | 0.707605 | General feats also include a subcategory of skill feats,  which expand on what you can accomplish via skills.  These feats also have the skill trait. Most characters gain  skill feats at 2nd level and |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/42` | 0.660161 | You know basic facts off the top of your head. Choose a skill  you're an expert in that has the Recall Knowledge action and  for which you have the Assurance feat. You can use the Recall  Knowledge ac |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/2` | 0.616516 | All kinds of experiences and training can shape your character beyond what you learn by advancing in  your class. Abilities that require a degree of training but can be learned by anyone—not only memb |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/6` | 0.611354 | you gain a skill feat, you must select a general feat with  the skill trait; you can't select a general feat that lacks the  skill trait. The level of a skill feat is typically the minimum  level at w |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/43` | 0.546392 | **Special** You can select this feat multiple times, choosing a  different skill each time. You can use Automatic Knowledge  with any skills you have chosen, but you can still use  Automatic Knowledge |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/482` | 0.537161 | Varying Skill Feats |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/413` | 0.537161 | Varying Skill Feats |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/4` | 0.536509 | For most classes, you gain a general feat when you reach  3rd level and every 4 levels thereafter. Each time you gain  a general feat, you can select any feat with the general  trait whose prerequisit |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/31` | 0.530889 | **Special** You can select this feat multiple times. Each time,  choose a different skill and gain the benefits for that skill. |

### Query 6
- Text: What is the rule about **GENERAL FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/SectionHeader/8', 'PZO22001 Starfinder Player Core 210-231::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 210-231::/page/1/SectionHeader/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/SectionHeader/8` | 0.872572 | **GENERAL FEATS** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/SectionHeader/10` | 0.726560 | **GENERAL SKILL FEATS** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/SectionHeader/1` | 0.654140 | CHAPTER 5: FEATS |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/21/Text/18` | 0.561155 | **GENERAL** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/19` | 0.561155 | **GENERAL** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/43` | 0.561155 | **GENERAL** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/23` | 0.561155 | **GENERAL** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/44` | 0.561155 | **GENERAL** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/34` | 0.561155 | **GENERAL** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/22` | 0.561155 | **GENERAL** |

### Query 7
- Text: Lookup values for Non-Skill FeatsLevelPrerequisitesBenefitsAdopted Ancestry1—Gain access to ancestry feats from another ancestryArmor Proficiency1—Become trained in a type of armorAugmented Body1—Gain a free augmentationBarricade1—Create fragile cover from nearby junkBreath Control1—Hold your breath longer and gain other benefitsCanny Acumen1—Become an expert in a saving throw or PerceptionDiehard1—Die at dying 5, rather than dying 4Fast Recovery1Constitution +2Regain more HP from rest, recover faster from diseaseFeather Step1Dexterity +2Step into difficult terrainFleet1—Increase your Speed by 5 feetIncredible Initiative1—+2 to initiative rollsRide1—Automatically succeed at commanding your mount to moveShield Block1—Ward off a blow with your shieldToughness1—Increase your maximum HP and reduce the DCs of
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/Table/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/Table/9', 'PZO22001 Starfinder Player Core 210-231::/page/4/Table/1', 'PZO22001 Starfinder Player Core 210-231::/page/2/Table/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/Table/9` | 0.979906 | Non-Skill FeatsLevelPrerequisitesBenefitsAdopted Ancestry1—Gain access to ancestry feats from another ancestryArmor Proficiency1—Become trained in a type of armorAugmented Body1—Gain a free augmentati |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/4/Table/1` | 0.750930 | Lore Skill FeatsLevelPrerequisitesBenefitsLegendary Professional15Legendary in LoreGain renown for your LoreMedicine Skill FeatsLevelPrerequisitesBenefitsBattle Medicine1Trained in MedicineHeal yourse |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/2/Table/1` | 0.735302 | Varying Skill FeatsLevelPrerequisitesBenefitsRecognize Spell1Trained in Arcana, Nature, Occultism, or ReligionIdentify a spell as a reaction as it's being castSeasoned1Trained in Alcohol Lore, Cooking |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/5/Table/3` | 0.638006 | Survival Skill FeatsLevelPrerequisitesBenefitsExperienced Tracker1Trained in SurvivalTrack at your full Speed at a –5 penaltySurvey Wildlife1Trained in SurvivalIdentify nearby creatures through signs |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/3/Table/1` | 0.624867 | Crafting Skill FeatsLevelPrerequisitesBenefitsQuick Install1Trained in CraftingInstall upgrades quicklyQuick Repair1Trained in CraftingRepair items quicklySerum Crafting1Trained in CraftingCraft serum |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/398` | 0.604975 | Non-Skill Feats |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/14` | 0.604127 | long as the ancestry feats don't require any physiological  feature that you lack, as determined by the GM. |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/2` | 0.603954 | All kinds of experiences and training can shape your character beyond what you learn by advancing in  your class. Abilities that require a degree of training but can be learned by anyone—not only memb |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/5/Table/2` | 0.599799 | Stealth Skill FeatsLevelPrerequisitesBenefitsExperienced Smuggler1Trained in StealthConceal items from observers more effectivelyTerrain Stalker1Trained in StealthSneak in certain terrain without atte |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/1/Table/11` | 0.596944 | Varying Skill FeatsLevelPrerequisitesBenefitsAssurance1Trained in at least one skillReceive a fixed result on a skill checkDubious Knowledge1Trained in a skill with the Recall Knowledge actionLearn tr |

### Query 8
- Text: What is the rule about Non-Skill Feats?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/398']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/398', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/545', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/413']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/398` | 0.901206 | Non-Skill Feats |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/545` | 0.648967 | Computers Skill Feats |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/413` | 0.641425 | Varying Skill Feats |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/482` | 0.599425 | Varying Skill Feats |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/550` | 0.590050 | Society Skill Feats |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/504` | 0.590050 | Society Skill Feats |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/6` | 0.584845 | you gain a skill feat, you must select a general feat with  the skill trait; you can't select a general feat that lacks the  skill trait. The level of a skill feat is typically the minimum  level at w |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/497` | 0.580521 | Athletics Skill Feats |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/5` | 0.577605 | General feats also include a subcategory of skill feats,  which expand on what you can accomplish via skills.  These feats also have the skill trait. Most characters gain  skill feats at 2nd level and |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/474` | 0.576803 | Performance Skill Feats |

### Query 9
- Text: Summarize Level
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/399']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/399', 'PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/439', 'PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/499']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/399` | 0.767709 | Level |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/439` | 0.767709 | Level |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/499` | 0.767709 | Level |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/483` | 0.725709 | Level |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/399` | 0.725709 | Level |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/531` | 0.725709 | Level |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/614` | 0.725709 | Level |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/686` | 0.725709 | Level |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/650` | 0.725709 | Level |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/505` | 0.725709 | Level |

### Query 10
- Text: What is the rule about Prerequisites?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/400']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/400', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/484', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/575']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/400` | 0.784633 | Prerequisites |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/484` | 0.784633 | Prerequisites |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/575` | 0.784633 | Prerequisites |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/547` | 0.742633 | Prerequisites |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/451` | 0.742633 | Prerequisites |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/499` | 0.742633 | Prerequisites |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/415` | 0.742633 | Prerequisites |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/483` | 0.742633 | Prerequisites |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/651` | 0.742633 | Prerequisites |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/687` | 0.742633 | Prerequisites |

### Query 11
- Text: Summarize Benefits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/401']
- Expected found: `True`
- Expected rank: `19`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/484', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/485', 'PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/533']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/484` | 0.806099 | Benefits |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/485` | 0.806099 | Benefits |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/533` | 0.806099 | Benefits |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/560` | 0.764099 | Benefits |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/501` | 0.764099 | Benefits |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/512` | 0.764099 | Benefits |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/688` | 0.764099 | Benefits |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/548` | 0.764099 | Benefits |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/576` | 0.764099 | Benefits |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/401` | 0.764099 | Benefits |

### Query 12
- Text: Summarize Adopted Ancestry
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/402']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/402', 'PZO22001 Starfinder Player Core 210-231::/page/5/SectionHeader/10', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/405']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/402` | 0.949640 | Adopted Ancestry |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/5/SectionHeader/10` | 0.574714 | **ADOPTED ANCESTRY FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/405` | 0.481200 | Gain access to ancestry feats from another ancestry |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/465` | 0.428253 | Gain a 1st-level ancestry feat |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/1/Table/9` | 0.417465 | Non-Skill FeatsLevelPrerequisitesBenefitsAdopted Ancestry1—Gain access to ancestry feats from another ancestryArmor Proficiency1—Become trained in a type of armorAugmented Body1—Gain a free augmentati |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/13` | 0.406603 | You're fully immersed in another ancestry's culture and  traditions, whether born into them, earned through a rite of  passage, or bonded through a deep friendship or romance.  Choose a common ancestr |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/14` | 0.379488 | Whether through instinct, study, or magic, you feel a deeper  connection to your ancestry. You gain a 1st-level ancestry feat. |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/14` | 0.365638 | long as the ancestry feats don't require any physiological  feature that you lack, as determined by the GM. |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/14/SectionHeader/45` | 0.340092 | **ODDITY IDENTIFICATION** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/454` | 0.326664 | Oddity Identification |

### Query 13
- Text: Summarize 1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/403']
- Expected found: `True`
- Expected rank: `60`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/490', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/502']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626` | 0.669108 | 1 |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/502` | 0.669108 | 1 |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/490` | 0.669108 | 1 |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/562` | 0.627108 | 1 |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/526` | 0.627108 | 1 |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/510` | 0.627108 | 1 |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/419` | 0.627108 | 1 |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/518` | 0.627108 | 1 |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/514` | 0.627108 | 1 |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/549` | 0.627108 | 1 |

### Query 14
- Text: Summarize —
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/404']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/691', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/404', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/472']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/691` | 0.572766 | — |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/404` | 0.572766 | — |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/472` | 0.572766 | — |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/428` | 0.530766 | — |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/440` | 0.530766 | — |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/460` | 0.530766 | — |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/464` | 0.530766 | — |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/468` | 0.530766 | — |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/444` | 0.530766 | — |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/452` | 0.530766 | — |

### Query 15
- Text: What is the rule about Gain access to ancestry feats from another ancestry?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/405']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/405', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/465', 'PZO22001 Starfinder Player Core 210-231::/page/5/Text/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/405` | 0.930986 | Gain access to ancestry feats from another ancestry |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/465` | 0.682254 | Gain a 1st-level ancestry feat |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/13` | 0.663215 | You're fully immersed in another ancestry's culture and  traditions, whether born into them, earned through a rite of  passage, or bonded through a deep friendship or romance.  Choose a common ancestr |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/14` | 0.627802 | long as the ancestry feats don't require any physiological  feature that you lack, as determined by the GM. |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/14` | 0.568690 | Whether through instinct, study, or magic, you feel a deeper  connection to your ancestry. You gain a 1st-level ancestry feat. |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/Table/9` | 0.522549 | Non-Skill FeatsLevelPrerequisitesBenefitsAdopted Ancestry1—Gain access to ancestry feats from another ancestryArmor Proficiency1—Become trained in a type of armorAugmented Body1—Gain a free augmentati |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/2` | 0.501914 | All kinds of experiences and training can shape your character beyond what you learn by advancing in  your class. Abilities that require a degree of training but can be learned by anyone—not only memb |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/4` | 0.477130 | For most classes, you gain a general feat when you reach  3rd level and every 4 levels thereafter. Each time you gain  a general feat, you can select any feat with the general  trait whose prerequisit |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/5` | 0.449831 | General feats also include a subcategory of skill feats,  which expand on what you can accomplish via skills.  These feats also have the skill trait. Most characters gain  skill feats at 2nd level and |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/31` | 0.442159 | **Special** You can select this feat multiple times. Each time,  choose a different skill and gain the benefits for that skill. |

### Query 16
- Text: What is the rule about Armor Proficiency?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/406']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/406', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/458', 'PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/406` | 0.883090 | Armor Proficiency |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/458` | 0.696000 | Weapon Proficiency |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/21` | 0.673107 | **ARMOR PROFICIENCY FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/24` | 0.543551 | You become trained in light armor. If you already were trained  in light armor, you gain training in medium armor. If you were  trained in both, you become trained in heavy armor. If you are  at least |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/409` | 0.528954 | Become trained in a type of armor |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/25` | 0.515088 | **Special** You can select this feat more than once. Each time, you  become trained in the next type of armor, as detailed above. |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/21/SectionHeader/16` | 0.489313 | **WEAPON PROFICIENCY** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/6` | 0.481160 | you gain a skill feat, you must select a general feat with  the skill trait; you can't select a general feat that lacks the  skill trait. The level of a skill feat is typically the minimum  level at w |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/1` | 0.469604 | they're trained. The skill must be Crafting or another skill  relevant to the item, as determined by the GM. For example,  a PC might use Religion to help you Craft an item with the  divine trait or W |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/6` | 0.456844 | If you activate a magic item that requires a spell attack  modifier or spell DC and you don't have proficiency in the  relevant statistic, use your level as your proficiency bonus  and the highest of |

### Query 17
- Text: Summarize 1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/407']
- Expected found: `True`
- Expected rank: `59`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626', 'PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/455', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/419']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626` | 0.669108 | 1 |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/455` | 0.669108 | 1 |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/419` | 0.669108 | 1 |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/518` | 0.627108 | 1 |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/514` | 0.627108 | 1 |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/510` | 0.627108 | 1 |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/506` | 0.627108 | 1 |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/622` | 0.627108 | 1 |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/553` | 0.627108 | 1 |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/549` | 0.627108 | 1 |

### Query 18
- Text: Summarize —
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/408']
- Expected found: `True`
- Expected rank: `12`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/404', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/472', 'PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/691']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/404` | 0.572766 | — |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/472` | 0.572766 | — |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/691` | 0.572766 | — |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/428` | 0.530766 | — |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/440` | 0.530766 | — |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/468` | 0.530766 | — |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/444` | 0.530766 | — |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/460` | 0.530766 | — |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/448` | 0.530766 | — |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/456` | 0.530766 | — |

### Query 19
- Text: Summarize Become trained in a type of armor
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/409']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/409', 'PZO22001 Starfinder Player Core 210-231::/page/6/Text/24', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/461']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/409` | 1.006275 | Become trained in a type of armor |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/24` | 0.783594 | You become trained in light armor. If you already were trained  in light armor, you gain training in medium armor. If you were  trained in both, you become trained in heavy armor. If you are  at least |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/461` | 0.774754 | Become trained in a weapon type |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/25` | 0.692472 | **Special** You can select this feat more than once. Each time, you  become trained in the next type of armor, as detailed above. |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/428` | 0.592562 | Become trained in a skill |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/406` | 0.572725 | Armor Proficiency |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/692` | 0.549225 | Become trained in another Lore subcategory |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/18/TableCell/427` | 0.523373 | Clothing, leather, and polymer armor |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/29` | 0.516674 | **Prerequisites** trained in at least one skill |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/21/Text/19` | 0.511755 | You become trained in all martial weapons. If you were  already trained in all martial weapons, you become trained  in one advanced weapon of your choice. If you are at least  11th level, you also bec |

### Query 20
- Text: Summarize Augmented Body
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/410']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/410', 'PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/32', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/413']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/410` | 0.936204 | Augmented Body |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/32` | 0.717601 | **AUGMENTED BODY** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/413` | 0.428736 | Gain a free augmentation |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/35` | 0.386604 | You implant one augmentation with an item level equal to  your character level or lower. This augmentation doesn't  count against your total implant limit. The first time you take  this feat, the augm |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/1/Table/9` | 0.360903 | Non-Skill FeatsLevelPrerequisitesBenefitsAdopted Ancestry1—Gain access to ancestry feats from another ancestryArmor Proficiency1—Become trained in a type of armorAugmented Body1—Gain a free augmentati |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/18/TableCell/409` | 0.355846 | Armor, shields and upgrades |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/37` | 0.339542 | **Special** You can select this feat multiple times, choosing a  different augmentation each time. Retraining this feat  requires paying the cost of the original augmentation. |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/36` | 0.331467 | swapping it out with another augmentation when you gain a  level or by spending downtime replacing the augmentation  as though changing out a feat. When you swap out the  augmentation, you must pay th |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/18/TableCell/421` | 0.329890 | Firearms and firearm upgrades |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/18/Table/25` | 0.322419 | SpecialtyApplicable ItemsArmorsmithingArmor, shields and upgradesArtistryFine art, including jewelry and solarian crystalsAutomotivesVehicles, including spaceshipsChemicalsAlcohol, ammunition, explosi |

### Query 21
- Text: Summarize 1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/411']
- Expected found: `True`
- Expected rank: `51`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626', 'PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/455', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/419']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626` | 0.669108 | 1 |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/455` | 0.669108 | 1 |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/419` | 0.669108 | 1 |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/518` | 0.627108 | 1 |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/514` | 0.627108 | 1 |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/510` | 0.627108 | 1 |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/506` | 0.627108 | 1 |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/622` | 0.627108 | 1 |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/553` | 0.627108 | 1 |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/549` | 0.627108 | 1 |

### Query 22
- Text: Summarize —
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/412']
- Expected found: `True`
- Expected rank: `13`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/404', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/472', 'PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/691']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/404` | 0.572766 | — |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/472` | 0.572766 | — |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/691` | 0.572766 | — |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/428` | 0.530766 | — |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/440` | 0.530766 | — |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/468` | 0.530766 | — |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/444` | 0.530766 | — |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/460` | 0.530766 | — |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/448` | 0.530766 | — |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/456` | 0.530766 | — |

### Query 23
- Text: Summarize Gain a free augmentation
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/413']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/413', 'PZO22001 Starfinder Player Core 210-231::/page/6/Text/35', 'PZO22001 Starfinder Player Core 210-231::/page/6/Text/36']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/413` | 0.994713 | Gain a free augmentation |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/35` | 0.683552 | You implant one augmentation with an item level equal to  your character level or lower. This augmentation doesn't  count against your total implant limit. The first time you take  this feat, the augm |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/36` | 0.608718 | swapping it out with another augmentation when you gain a  level or by spending downtime replacing the augmentation  as though changing out a feat. When you swap out the  augmentation, you must pay th |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/37` | 0.510033 | **Special** You can select this feat multiple times, choosing a  different augmentation each time. Retraining this feat  requires paying the cost of the original augmentation. |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/18/TableCell/421` | 0.398237 | Firearms and firearm upgrades |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/448` | 0.397216 | Identify spells as a free action |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/18/TableCell/409` | 0.394409 | Armor, shields and upgrades |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/528` | 0.380547 | Gain bonuses to Craft certain items |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/48` | 0.370016 | You can Earn Income (page 186) using Diplomacy, spending  your days hunting for bargains and reselling at a profit. You  can also spend time specifically seeking a great bargain on  an item; this work |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/1/Table/9` | 0.363883 | Non-Skill FeatsLevelPrerequisitesBenefitsAdopted Ancestry1—Gain access to ancestry feats from another ancestryArmor Proficiency1—Become trained in a type of armorAugmented Body1—Gain a free augmentati |

### Query 24
- Text: Summarize Barricade
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/414']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/414', 'PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/49', 'PZO22001 Starfinder Player Core 210-231::/page/6/Text/52']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/414` | 0.927840 | Barricade |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/49` | 0.675197 | **BARRICADE **[one-action] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/52` | 0.574594 | You hastily create a barricade using nearby items, junk, or  debris. The barricade provides lesser cover for you and one  other ally, though you can Take Cover to increase this benefit  to standard co |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/441` | 0.337311 | Break Curse |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/12` | 0.296195 | **BREAK CURSE** **FEAT 7** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/25` | 0.291264 | **Failure** The crowd doesn't move, but you can continue moving. **Critical Failure** The crowd forcefully resists you and disrupts  your Stride. |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/38` | 0.289584 | **SEASONED** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/20/TableCell/420` | 0.286306 | Dance |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/44` | 0.285384 | **BARGAIN HUNTER** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/446` | 0.273976 | Ride |

### Query 25
- Text: Summarize 1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/415']
- Expected found: `True`
- Expected rank: `52`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626', 'PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/455', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/419']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626` | 0.669108 | 1 |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/455` | 0.669108 | 1 |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/419` | 0.669108 | 1 |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/518` | 0.627108 | 1 |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/514` | 0.627108 | 1 |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/510` | 0.627108 | 1 |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/506` | 0.627108 | 1 |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/622` | 0.627108 | 1 |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/553` | 0.627108 | 1 |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/549` | 0.627108 | 1 |

### Query 26
- Text: Summarize —
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/416']
- Expected found: `True`
- Expected rank: `14`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/404', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/472', 'PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/691']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/404` | 0.572766 | — |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/472` | 0.572766 | — |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/691` | 0.572766 | — |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/428` | 0.530766 | — |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/440` | 0.530766 | — |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/468` | 0.530766 | — |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/444` | 0.530766 | — |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/460` | 0.530766 | — |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/448` | 0.530766 | — |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/456` | 0.530766 | — |

### Query 27
- Text: Summarize Create fragile cover from nearby junk
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/417']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/417', 'PZO22001 Starfinder Player Core 210-231::/page/6/Text/52', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/472']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/417` | 1.010619 | Create fragile cover from nearby junk |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/52` | 0.695228 | You hastily create a barricade using nearby items, junk, or  debris. The barricade provides lesser cover for you and one  other ally, though you can Take Cover to increase this benefit  to standard co |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/472` | 0.506197 | Quickly get prone and take cover |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/9/Text/6` | 0.429102 | When threatened, you can quickly take a dive and find  somewhere to hunker down. You Leap, land prone, and  immediately Take Cover, which allows you to hunker down  and gain greater cover against rang |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/26` | 0.425346 | You know how to get lost in a crowd. You can use cover  from crowds to Hide and Sneak, gaining a +2 circumstance |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/55` | 0.415443 | You try to repair an item by smashing it against a hard surface.  Attempt a DC 10 flat check. |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/469` | 0.411740 | Dive for Cover |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/436` | 0.408595 | Clean up a crime scene or cover your tracks |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/42` | 0.378945 | Select one type of difficult terrain from the following list:  rubble, snow, or underbrush. While undetected by all nonallies in that type of terrain, you can Sneak without attempting  a Stealth check |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/583` | 0.373013 | Identify nearby creatures through signs and clues |

### Query 28
- Text: Summarize Breath Control
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/418']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/418', 'PZO22001 Starfinder Player Core 210-231::/page/7/Text/17', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/421']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/418` | 0.931456 | Breath Control |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/17` | 0.679040 | **BREATH CONTROL** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/421` | 0.534081 | Hold your breath longer and gain other benefits |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/20` | 0.428263 | You can breathe even in hazardous or sparse air. You can hold  your breath for 25 times as long as usual before suffocating. You  gain a +1 circumstance bonus to saving throws against inhaled  threats |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/17` | 0.405369 | **CROWD CONTROL** **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/25` | 0.370875 | You Board and Take Control of an adjacent vehicle. |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/520` | 0.305945 | Expert in Piloting |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/508` | 0.305945 | Expert in Piloting |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/516` | 0.305945 | Expert in Piloting |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/58` | 0.296366 | **BATTLE MEDICINE **[one-action] **FEAT 1** |

### Query 29
- Text: Summarize 1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/419']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626', 'PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/455', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/419']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626` | 0.669108 | 1 |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/455` | 0.669108 | 1 |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/419` | 0.669108 | 1 |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/518` | 0.627108 | 1 |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/514` | 0.627108 | 1 |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/510` | 0.627108 | 1 |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/506` | 0.627108 | 1 |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/622` | 0.627108 | 1 |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/553` | 0.627108 | 1 |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/549` | 0.627108 | 1 |

### Query 30
- Text: Summarize —
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/420']
- Expected found: `True`
- Expected rank: `15`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/404', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/472', 'PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/691']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/404` | 0.572766 | — |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/472` | 0.572766 | — |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/691` | 0.572766 | — |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/428` | 0.530766 | — |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/440` | 0.530766 | — |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/468` | 0.530766 | — |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/444` | 0.530766 | — |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/460` | 0.530766 | — |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/448` | 0.530766 | — |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/456` | 0.530766 | — |

### Query 31
- Text: Summarize Hold your breath longer and gain other benefits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/421']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/421', 'PZO22001 Starfinder Player Core 210-231::/page/7/Text/20', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/418']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/421` | 1.013851 | Hold your breath longer and gain other benefits |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/20` | 0.627333 | You can breathe even in hazardous or sparse air. You can hold  your breath for 25 times as long as usual before suffocating. You  gain a +1 circumstance bonus to saving throws against inhaled  threats |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/418` | 0.472462 | Breath Control |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/533` | 0.415348 | Benefits |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/484` | 0.415348 | Benefits |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/485` | 0.415348 | Benefits |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/501` | 0.415348 | Benefits |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/560` | 0.415348 | Benefits |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/652` | 0.415348 | Benefits |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/548` | 0.415348 | Benefits |

### Query 32
- Text: What is the rule about Canny Acumen?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/422']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/422', 'PZO22001 Starfinder Player Core 210-231::/page/7/Text/21', 'PZO22001 Starfinder Player Core 210-231::/page/1/Table/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/422` | 0.837250 | Canny Acumen |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/21` | 0.614397 | **CANNY ACUMEN** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/Table/9` | 0.360829 | Non-Skill FeatsLevelPrerequisitesBenefitsAdopted Ancestry1—Gain access to ancestry feats from another ancestryArmor Proficiency1—Become trained in a type of armorAugmented Body1—Gain a free augmentati |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/34` | 0.314726 | In situations where you can physically menace the target when  you Coerce or Demoralize, you gain a +1 circumstance bonus  to your Intimidation check and you ignore the penalty for not |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/534` | 0.313399 | Student of the Canon |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/6` | 0.308227 | **Critical Success** You correctly recognize the spell and gain a  +1 circumstance bonus to your saving throw or your AC  against it. |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/2/Table/1` | 0.303654 | Varying Skill FeatsLevelPrerequisitesBenefitsRecognize Spell1Trained in Arcana, Nature, Occultism, or ReligionIdentify a spell as a reaction as it's being castSeasoned1Trained in Alcohol Lore, Cooking |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/35` | 0.301724 | You implant one augmentation with an item level equal to  your character level or lower. This augmentation doesn't  count against your total implant limit. The first time you take  this feat, the augm |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/10` | 0.295786 | You can Steal or Palm an Object that's closely guarded,  such as in a pocket, without taking the –5 penalty. You can't  steal objects that would be extremely noticeable or time  consuming to remove (l |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/18/SectionHeader/35` | 0.294460 | **STUDENT OF THE CANON** **FEAT 1** |

### Query 33
- Text: Summarize 1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/423']
- Expected found: `True`
- Expected rank: `76`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/455', 'PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/518']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/455` | 0.669108 | 1 |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626` | 0.669108 | 1 |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/518` | 0.669108 | 1 |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/514` | 0.627108 | 1 |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/510` | 0.627108 | 1 |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/506` | 0.627108 | 1 |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/622` | 0.627108 | 1 |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/553` | 0.627108 | 1 |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/549` | 0.627108 | 1 |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/618` | 0.627108 | 1 |

### Query 34
- Text: Summarize —
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/424']
- Expected found: `True`
- Expected rank: `14`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/416', 'PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/691', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/448']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/416` | 0.572766 | — |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/691` | 0.572766 | — |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/448` | 0.572766 | — |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/456` | 0.530766 | — |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/452` | 0.530766 | — |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/412` | 0.530766 | — |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/428` | 0.530766 | — |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/440` | 0.530766 | — |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/444` | 0.530766 | — |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/460` | 0.530766 | — |

### Query 35
- Text: What is the rule about Become an expert in a saving throw or Perception?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/425']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/425', 'PZO22001 Starfinder Player Core 210-231::/page/7/Text/24', 'PZO22001 Starfinder Player Core 210-231::/page/17/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/425` | 0.943385 | Become an expert in a saving throw or Perception |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/24` | 0.615807 | Your avoidance or observation is beyond the ken of most in  your profession. Choose Fortitude saves, Reflex saves, Will  saves, or Perception. You become an expert in your choice. At  17th level, you |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/6` | 0.565768 | **Critical Success** You correctly recognize the spell and gain a  +1 circumstance bonus to your saving throw or your AC  against it. |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/476` | 0.461177 | Master in Perception |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/23` | 0.456267 | circumstance bonus granted on a success to +4, and if the  result of the patient's saving throw is a success, the patient  gets a critical success. |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/9/Text/25` | 0.439217 | **Prerequisites** master in Perception |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/439` | 0.426172 | Expert in Recall Knowledge, Assurance in the relevant skill action |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/42` | 0.426124 | You know basic facts off the top of your head. Choose a skill  you're an expert in that has the Recall Knowledge action and  for which you have the Assurance feat. You can use the Recall  Knowledge ac |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/1/Table/9` | 0.423503 | Non-Skill FeatsLevelPrerequisitesBenefitsAdopted Ancestry1—Gain access to ancestry feats from another ancestryArmor Proficiency1—Become trained in a type of armorAugmented Body1—Gain a free augmentati |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/33` | 0.422259 | If you're an expert in Performance, you can fascinate up  to four observers; if you're a master, you can fascinate up to  10 observers; and if you're legendary, you can fascinate any  number of observ |

### Query 36
- Text: Summarize Diehard
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/426']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/426', 'PZO22001 Starfinder Player Core 210-231::/page/8/Text/41', 'PZO22001 Starfinder Player Core 210-231::/page/8/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/426` | 0.907921 | Diehard |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/41` | 0.606221 | **DIEHARD** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/31` | 0.340588 | **DEADLIFT **[one-action] **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/437` | 0.275730 | Remove disease, blinded, deafened, doomed, or drained |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/573` | 0.275674 | Lengthy Diversion |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/421` | 0.260334 | Seasoned |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/21/Text/11` | 0.260130 | **WARY DISARMAMENT** **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/616` | 0.258190 | Wary Disarmament |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/520` | 0.255623 | Disarm, Grapple, Shove, or Trip larger creatures |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/414` | 0.251831 | Barricade |

### Query 37
- Text: Summarize 1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/427']
- Expected found: `True`
- Expected rank: `54`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/455', 'PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/518']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/455` | 0.669108 | 1 |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626` | 0.669108 | 1 |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/518` | 0.669108 | 1 |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/514` | 0.627108 | 1 |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/510` | 0.627108 | 1 |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/506` | 0.627108 | 1 |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/622` | 0.627108 | 1 |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/553` | 0.627108 | 1 |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/549` | 0.627108 | 1 |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/618` | 0.627108 | 1 |

### Query 38
- Text: Summarize —
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/428']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/416', 'PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/691', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/448']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/416` | 0.572766 | — |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/691` | 0.572766 | — |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/448` | 0.572766 | — |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/456` | 0.530766 | — |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/452` | 0.530766 | — |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/412` | 0.530766 | — |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/428` | 0.530766 | — |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/440` | 0.530766 | — |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/444` | 0.530766 | — |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/460` | 0.530766 | — |

### Query 39
- Text: Summarize Die at dying 5, rather than dying 4
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/429']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/429', 'PZO22001 Starfinder Player Core 210-231::/page/8/Text/44', 'PZO22001 Starfinder Player Core 210-231::/page/19/Text/66']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/429` | 1.008892 | Die at dying 5, rather than dying 4 |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/44` | 0.847392 | It takes more to kill you than most. You die from the dying  condition at dying 5, rather than dying 4. |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/66` | 0.544194 | 5 |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/60` | 0.502194 | 5 |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/53` | 0.502194 | 5 |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/51` | 0.502194 | 5 |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/58` | 0.502194 | 5 |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/58` | 0.405752 | Your body can withstand more punishment than most before  succumbing. Increase your maximum Hit Points by your level.  You reduce the DC of recovery checks by 1 (page 403). |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/38` | 0.396248 | Your body quickly bounces back from afflictions. You regain  twice as many Hit Points from resting. Each time you succeed  at a Fortitude save against an ongoing disease or poison, you  reduce its sta |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/588` | 0.392510 | Pretend to die |

### Query 40
- Text: Summarize Fast Recovery
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/430']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/430', 'PZO22001 Starfinder Player Core 210-231::/page/10/SectionHeader/34', 'PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/418']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/430` | 0.931665 | Fast Recovery |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/10/SectionHeader/34` | 0.782739 | **FAST RECOVERY** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/418` | 0.688074 | Robust Recovery |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/414` | 0.599125 | Continual Recovery |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/433` | 0.545124 | Regain more HP from rest, recover faster from disease |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/16/SectionHeader/36` | 0.514617 | **QUICK REPAIR** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/18` | 0.504581 | **ROBUST RECOVERY** **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/8/SectionHeader/8` | 0.499982 | **CONTINUAL RECOVERY** **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/457` | 0.490783 | Increase your maximum HP and reduce the DCs of recovery checks |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/517` | 0.475396 | Quick Repair |

### Query 41
- Text: Summarize 1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/431']
- Expected found: `True`
- Expected rank: `53`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/490', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/502']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626` | 0.669108 | 1 |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/502` | 0.669108 | 1 |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/490` | 0.669108 | 1 |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/562` | 0.627108 | 1 |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/526` | 0.627108 | 1 |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/510` | 0.627108 | 1 |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/419` | 0.627108 | 1 |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/518` | 0.627108 | 1 |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/514` | 0.627108 | 1 |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/549` | 0.627108 | 1 |

### Query 42
- Text: Summarize Constitution +2
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/432']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/432', 'PZO22001 Starfinder Player Core 210-231::/page/10/Text/37', 'PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/530']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/432` | 0.921185 | Constitution +2 |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/37` | 0.823673 | **Prerequisites** Constitution +2 |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/530` | 0.509149 | 2 |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/617` | 0.467149 | 2 |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/522` | 0.467149 | 2 |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/427` | 0.467149 | 2 |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/538` | 0.467149 | 2 |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/534` | 0.467149 | 2 |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/419` | 0.467149 | 2 |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/526` | 0.467149 | 2 |

### Query 43
- Text: Summarize Regain more HP from rest, recover faster from disease
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/433']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/433', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/457', 'PZO22001 Starfinder Player Core 210-231::/page/10/Text/38']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/433` | 1.027614 | Regain more HP from rest, recover faster from disease |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/457` | 0.669118 | Increase your maximum HP and reduce the DCs of recovery checks |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/38` | 0.616881 | Your body quickly bounces back from afflictions. You regain  twice as many Hit Points from resting. Each time you succeed  at a Fortitude save against an ongoing disease or poison, you  reduce its sta |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/430` | 0.521713 | Fast Recovery |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/58` | 0.499588 | Your body can withstand more punishment than most before  succumbing. Increase your maximum Hit Points by your level.  You reduce the DC of recovery checks by 1 (page 403). |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/22` | 0.472302 | You learned folk medicine to help recover from diseases  and poisons, and using it diligently has made you especially  resilient. When you Treat a Disease or a Poison, or someone  else uses one of the |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/414` | 0.434993 | Continual Recovery |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/10/SectionHeader/34` | 0.429117 | **FAST RECOVERY** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/20` | 0.413458 | You've discovered medical breakthroughs or techniques that  achieve miraculous results. Once per day for each target, you  can spend 1 hour treating that target and attempt a Medicine  check to remove |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/418` | 0.410396 | Robust Recovery |

### Query 44
- Text: What is the rule about Feather Step?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/434']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/434', 'PZO22001 Starfinder Player Core 210-231::/page/10/SectionHeader/44', 'PZO22001 Starfinder Player Core 210-231::/page/1/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/434` | 0.862718 | Feather Step |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/10/SectionHeader/44` | 0.573234 | **FEATHER STEP** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/6` | 0.397919 | you gain a skill feat, you must select a general feat with  the skill trait; you can't select a general feat that lacks the  skill trait. The level of a skill feat is typically the minimum  level at w |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/5` | 0.359639 | General feats also include a subcategory of skill feats,  which expand on what you can accomplish via skills.  These feats also have the skill trait. Most characters gain  skill feats at 2nd level and |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/24` | 0.341951 | is equal to your level –2. This improves to your level –1 at 5th  level and your full level at 7th level. This doesn't allow you to  use the skill's trained actions. |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/4` | 0.341706 | For most classes, you gain a general feat when you reach  3rd level and every 4 levels thereafter. Each time you gain  a general feat, you can select any feat with the general  trait whose prerequisit |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/48` | 0.334336 | You step carefully and quickly. You can Step into difficult terrain. |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/9` | 0.334287 | **Special** You can select this feat more than once. Each time  you must select a new subcategory of Lore, and you gain  the additional skill increases to that subcategory for the  listed levels. |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/1/Table/9` | 0.330382 | Non-Skill FeatsLevelPrerequisitesBenefitsAdopted Ancestry1—Gain access to ancestry feats from another ancestryArmor Proficiency1—Become trained in a type of armorAugmented Body1—Gain a free augmentati |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/25` | 0.326334 | **Special** You can select this feat more than once. Each time, you  become trained in the next type of armor, as detailed above. |

### Query 45
- Text: Summarize 1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/435']
- Expected found: `True`
- Expected rank: `58`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/490', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/502']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626` | 0.669108 | 1 |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/502` | 0.669108 | 1 |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/490` | 0.669108 | 1 |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/562` | 0.627108 | 1 |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/526` | 0.627108 | 1 |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/510` | 0.627108 | 1 |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/419` | 0.627108 | 1 |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/518` | 0.627108 | 1 |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/514` | 0.627108 | 1 |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/549` | 0.627108 | 1 |

### Query 46
- Text: Summarize Dexterity +2
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/436']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/436', 'PZO22001 Starfinder Player Core 210-231::/page/10/Text/47', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/427']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/436` | 0.969327 | Dexterity +2 |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/47` | 0.876378 | **Prerequisites** Dexterity +2 |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/427` | 0.475288 | Intelligence +1 |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/432` | 0.427512 | Constitution +2 |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/557` | 0.406505 | Deception Skill Feats |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/37` | 0.404042 | **Prerequisites** Constitution +2 |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/617` | 0.389807 | 2 |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/534` | 0.389807 | 2 |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/538` | 0.389807 | 2 |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/542` | 0.389807 | 2 |

### Query 47
- Text: Summarize Step into difficult terrain
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/437']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/437', 'PZO22001 Starfinder Player Core 210-231::/page/10/Text/48', 'PZO22001 Starfinder Player Core 210-231::/page/19/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/437` | 0.953148 | Step into difficult terrain |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/48` | 0.826806 | You step carefully and quickly. You can Step into difficult terrain. |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/42` | 0.534751 | Select one type of difficult terrain from the following list:  rubble, snow, or underbrush. While undetected by all nonallies in that type of terrain, you can Sneak without attempting  a Stealth check |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/30` | 0.452157 | You move through crowds without slowing down. You can  move at full Speed in crowds. Treat areas truly packed with  people as difficult terrain instead of greater difficult terrain. |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/35` | 0.444194 | Your experience in navigating a certain type of terrain makes you  supremely confident while doing so. You gain a +1 circumstance  bonus to Survival checks in one of the following types of terrain, |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/44` | 0.438996 | **Special** You can select this feat multiple times. Each time,  choose a different type of terrain. |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/37` | 0.422789 | **Special** You can select this feat more than once, choosing a  different type of terrain each time. |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/555` | 0.418779 | Sneak in certain terrain without attempting a check |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/584` | 0.413622 | Terrain Expertise |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/587` | 0.406964 | +1 to Survival checks in certain terrain |

### Query 48
- Text: Summarize Fleet
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/438']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/438', 'PZO22001 Starfinder Player Core 210-231::/page/11/Text/3', 'PZO22001 Starfinder Player Core 210-231::/page/18/TableCell/413']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/438` | 0.862148 | Fleet |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/11/Text/3` | 0.557402 | **FLEET** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/18/TableCell/413` | 0.402599 | Vehicles, including spaceships |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/SectionHeader/1` | 0.359933 | CHAPTER 5: FEATS |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/20/TableCell/435` | 0.334334 | Horn, flute, pipes |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/498` | 0.329931 | Piloting Skill Feats |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/30` | 0.329253 | **Feats Table** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/59` | 0.329253 | **Feats Table** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/18` | 0.329253 | **Feats Table** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/57` | 0.329253 | **Feats Table** |

### Query 49
- Text: Summarize 1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/439']
- Expected found: `True`
- Expected rank: `57`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626', 'PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/455', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/419']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626` | 0.669108 | 1 |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/455` | 0.669108 | 1 |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/419` | 0.669108 | 1 |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/518` | 0.627108 | 1 |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/514` | 0.627108 | 1 |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/510` | 0.627108 | 1 |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/506` | 0.627108 | 1 |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/622` | 0.627108 | 1 |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/553` | 0.627108 | 1 |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/549` | 0.627108 | 1 |

### Query 50
- Text: Summarize —
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/440']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/404', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/472', 'PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/691']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/404` | 0.572766 | — |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/472` | 0.572766 | — |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/691` | 0.572766 | — |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/428` | 0.530766 | — |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/440` | 0.530766 | — |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/468` | 0.530766 | — |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/444` | 0.530766 | — |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/460` | 0.530766 | — |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/448` | 0.530766 | — |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/456` | 0.530766 | — |

### Query 51
- Text: Summarize Increase your Speed by 5 feet
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/441']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/441', 'PZO22001 Starfinder Player Core 210-231::/page/11/Text/5', 'PZO22001 Starfinder Player Core 210-231::/page/16/Text/50']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/441` | 1.004249 | Increase your Speed by 5 feet |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/11/Text/5` | 0.844836 | You move more quickly on foot. Your Speed increases by 5 feet. |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/50` | 0.617274 | You Swim 5 feet farther on a success and 10 feet farther  on a critical success, to a maximum of your Speed. If you're  legendary in Athletics, you gain a swim Speed equal to your  Speed. |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/579` | 0.567886 | Track at your full Speed at a –5 penalty |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/6` | 0.567029 | When Climbing, you move 5 more feet on a success and 10  more feet on a critical success, up to your Speed. If you're  legendary in Athletics, you gain a climb Speed equal to your  Speed. |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/41` | 0.556718 | You can jump a distance greater than your Speed by spending  additional actions when you Long Jump or High Jump. For each  additional action spent, add your Speed to the distance limit. |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/1` | 0.546040 | piloting gains a +10-foot circumstance bonus to all its Speeds  until the end of your turn. If you critically succeed, this bonus  increases to +15 feet. |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/45` | 0.542791 | You Squeeze 5 feet per round (10 feet on a critical success).  If you're legendary in Acrobatics, you Squeeze at full Speed. |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/525` | 0.528871 | Make a vehicle go faster |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/31` | 0.521716 | You can jump 5 feet up with a vertical Leap without making a  High Jump. You also increase the horizontal distance when you  Leap, including as part of a High Jump or Long Jump, by 5 feet. |

### Query 52
- Text: What is the rule about Incredible Initiative?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/442']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/442', 'PZO22001 Starfinder Player Core 210-231::/page/12/SectionHeader/21', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/445']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/442` | 0.858246 | Incredible Initiative |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/12/SectionHeader/21` | 0.532012 | **INCREDIBLE INITIATIVE** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/445` | 0.488474 | +2 to initiative rolls |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/57` | 0.431702 | When you roll initiative, you can yell a mighty battle cry and  Demoralize an observed foe as a free action. If you're legendary  in Intimidation, you can use a reaction to Demoralize your foe  when y |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/680` | 0.425441 | Demoralizes foes when you roll for initiative |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/24` | 0.400820 | You react more quickly than others can. You gain a +2  circumstance bonus to initiative rolls. |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/46` | 0.367069 | The GM might allow you to invent uncommon or rare  formulas, typically with an increased DC. You need the  Machine Magic feat to invent hybrid items and the Magical  Crafting feat to invent magical fo |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/60` | 0.363997 | You're skilled at moving with a group. When you are  Avoiding Notice and your allies Follow the Expert, you and  those allies can roll a single Stealth check, using the lowest  modifier, instead of ro |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/549` | 0.350021 | Impeccable Crafting |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/45` | 0.345012 | You are a genius at Crafting, easily able to determine how things  are made and create new inventions. You can spend downtime  to invent a common formula that you don't know. This works  just like the |

### Query 53
- Text: Summarize 1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/443']
- Expected found: `True`
- Expected rank: `71`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626', 'PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/455', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/419']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626` | 0.669108 | 1 |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/455` | 0.669108 | 1 |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/419` | 0.669108 | 1 |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/518` | 0.627108 | 1 |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/514` | 0.627108 | 1 |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/510` | 0.627108 | 1 |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/506` | 0.627108 | 1 |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/622` | 0.627108 | 1 |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/553` | 0.627108 | 1 |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/549` | 0.627108 | 1 |

### Query 54
- Text: Summarize —
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/444']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/404', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/472', 'PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/691']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/404` | 0.572766 | — |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/472` | 0.572766 | — |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/691` | 0.572766 | — |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/428` | 0.530766 | — |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/440` | 0.530766 | — |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/468` | 0.530766 | — |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/444` | 0.530766 | — |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/460` | 0.530766 | — |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/448` | 0.530766 | — |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/456` | 0.530766 | — |

### Query 55
- Text: What is the rule about +2 to initiative rolls?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/445']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/445', 'PZO22001 Starfinder Player Core 210-231::/page/12/Text/24', 'PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/680']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/445` | 0.885924 | +2 to initiative rolls |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/24` | 0.684753 | You react more quickly than others can. You gain a +2  circumstance bonus to initiative rolls. |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/680` | 0.627720 | Demoralizes foes when you roll for initiative |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/57` | 0.487605 | When you roll initiative, you can yell a mighty battle cry and  Demoralize an observed foe as a free action. If you're legendary  in Intimidation, you can use a reaction to Demoralize your foe  when y |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/60` | 0.485548 | You're skilled at moving with a group. When you are  Avoiding Notice and your allies Follow the Expert, you and  those allies can roll a single Stealth check, using the lowest  modifier, instead of ro |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/64` | 0.424331 | **Success** The animal learns the action. If it was an action the  animal already knew, you can Command the Animal to take  that action without attempting a Nature check. If it was a  new basic action |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/23` | 0.405854 | circumstance bonus granted on a success to +4, and if the  result of the patient's saving throw is a success, the patient  gets a critical success. |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/1` | 0.393695 | they're trained. The skill must be Crafting or another skill  relevant to the item, as determined by the GM. For example,  a PC might use Religion to help you Craft an item with the  divine trait or W |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/35` | 0.381261 | sharing a language. If your Strength modifier is +5 or higher and  you are a master in Intimidation, this bonus increases to +2. |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/41` | 0.377658 | You have exceptional talent with one type of performance.  You gain a +1 circumstance bonus when making a certain  type of performance. If you are a master in Performance, this  bonus increases to +2. |

### Query 56
- Text: Summarize Ride
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/446']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/446', 'PZO22001 Starfinder Player Core 210-231::/page/17/Text/14', 'PZO22001 Starfinder Player Core 210-231::/page/15/Text/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/446` | 0.866867 | Ride |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/14` | 0.536605 | **RIDE** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/26` | 0.386986 | You throw the vehicle into a barely controlled skid, turning  sharply to evade pursuit. You Drive with a –2 penalty to your  Piloting check, gaining the effects of the Drive action for the  same numbe |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/22` | 0.342375 | **POWER SLIDE **[one-action]** TO **[three-actions] **FEAT 3** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/510` | 0.320962 | Power Slide |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/518` | 0.317655 | Take the Wheel |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/25` | 0.299751 | **Failure** The crowd doesn't move, but you can continue moving. **Critical Failure** The crowd forcefully resists you and disrupts  your Stride. |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/20` | 0.286341 | You can move your full Speed when you Sneak. You can use Swift  Sneak while Burrowing, Climbing, Flying, or Swimming instead  of Striding if you have the corresponding movement type. |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/25` | 0.282200 | You Board and Take Control of an adjacent vehicle. |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/64` | 0.278350 | **Success** The animal learns the action. If it was an action the  animal already knew, you can Command the Animal to take  that action without attempting a Nature check. If it was a  new basic action |

### Query 57
- Text: Summarize 1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/447']
- Expected found: `True`
- Expected rank: `74`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626', 'PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/455', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/419']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626` | 0.669108 | 1 |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/455` | 0.669108 | 1 |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/419` | 0.669108 | 1 |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/518` | 0.627108 | 1 |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/514` | 0.627108 | 1 |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/510` | 0.627108 | 1 |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/506` | 0.627108 | 1 |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/622` | 0.627108 | 1 |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/553` | 0.627108 | 1 |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/549` | 0.627108 | 1 |

### Query 58
- Text: Summarize —
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/448']
- Expected found: `True`
- Expected rank: `9`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/404', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/472', 'PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/691']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/404` | 0.572766 | — |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/472` | 0.572766 | — |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/691` | 0.572766 | — |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/428` | 0.530766 | — |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/440` | 0.530766 | — |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/468` | 0.530766 | — |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/444` | 0.530766 | — |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/460` | 0.530766 | — |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/448` | 0.530766 | — |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/456` | 0.530766 | — |

### Query 59
- Text: Summarize Automatically succeed at commanding your mount to move
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/449']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/449', 'PZO22001 Starfinder Player Core 210-231::/page/17/Text/17', 'PZO22001 Starfinder Player Core 210-231::/page/19/Text/64']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/449` | 1.004295 | Automatically succeed at commanding your mount to move |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/17` | 0.582608 | When you Command an Animal you're mounted on to take  a move action (such as Stride), you automatically succeed  instead of needing to attempt a check. Any animal you're  mounted on acts on your turn, |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/64` | 0.445501 | **Success** The animal learns the action. If it was an action the  animal already knew, you can Command the Animal to take  that action without attempting a Nature check. If it was a  new basic action |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/6` | 0.390361 | When Climbing, you move 5 more feet on a success and 10  more feet on a critical success, up to your Speed. If you're  legendary in Athletics, you gain a climb Speed equal to your  Speed. |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/521` | 0.383928 | Wrest control of a moving vehicle |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/26` | 0.379508 | You throw the vehicle into a barely controlled skid, turning  sharply to evade pursuit. You Drive with a –2 penalty to your  Piloting check, gaining the effects of the Drive action for the  same numbe |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/65` | 0.377831 | You easily pull yourself onto ledges. When you Grab an Edge,  you can pull yourself onto that surface and stand. You can  use Athletics instead of a Reflex save to Grab an Edge. If you  Climb or Leap |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/20` | 0.373520 | You can move your full Speed when you Sneak. You can use Swift  Sneak while Burrowing, Climbing, Flying, or Swimming instead  of Striding if you have the corresponding movement type. |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/1` | 0.366041 | you can move while ensuring you've Searched an area before  walking into it (up to half your Speed). If you're legendary in  Perception, you instead Search areas four times as quickly. |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/506` | 0.363610 | Stunt Maneuver |

### Query 60
- Text: Summarize Shield Block
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/450']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/450', 'PZO22001 Starfinder Player Core 210-231::/page/18/Text/2', 'PZO22001 Starfinder Player Core 210-231::/page/18/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/450` | 0.921519 | Shield Block |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/2` | 0.630315 | **SHIELD BLOCK **[reaction] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/5` | 0.514032 | You snap your shield in place to ward off a blow. Your shield  prevents you from taking an amount of damage up to the  shield's Hardness. You and the shield each take any remaining  damage, possibly b |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/453` | 0.465551 | Ward off a blow with your shield |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/18/TableCell/409` | 0.436462 | Armor, shields and upgrades |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/4` | 0.369506 | **Trigger** While you have your shield raised, you would take  physical damage (bludgeoning, piercing, or slashing) from  an attack. |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/620` | 0.287634 | Quick Unlock |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/544` | 0.285814 | Stealth Skill Feats |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/536` | 0.285814 | Stealth Skill Feats |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/5/Table/2` | 0.280517 | Stealth Skill FeatsLevelPrerequisitesBenefitsExperienced Smuggler1Trained in StealthConceal items from observers more effectivelyTerrain Stalker1Trained in StealthSneak in certain terrain without atte |

### Query 61
- Text: Summarize 1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/451']
- Expected found: `True`
- Expected rank: `73`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626', 'PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/455', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/419']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626` | 0.669108 | 1 |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/455` | 0.669108 | 1 |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/419` | 0.669108 | 1 |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/518` | 0.627108 | 1 |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/514` | 0.627108 | 1 |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/510` | 0.627108 | 1 |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/506` | 0.627108 | 1 |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/622` | 0.627108 | 1 |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/553` | 0.627108 | 1 |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/549` | 0.627108 | 1 |

### Query 62
- Text: Summarize —
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/452']
- Expected found: `True`
- Expected rank: `16`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/404', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/472', 'PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/691']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/404` | 0.572766 | — |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/472` | 0.572766 | — |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/691` | 0.572766 | — |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/428` | 0.530766 | — |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/440` | 0.530766 | — |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/468` | 0.530766 | — |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/444` | 0.530766 | — |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/460` | 0.530766 | — |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/448` | 0.530766 | — |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/456` | 0.530766 | — |

### Query 63
- Text: Summarize Ward off a blow with your shield
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/453']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/453', 'PZO22001 Starfinder Player Core 210-231::/page/18/Text/5', 'PZO22001 Starfinder Player Core 210-231::/page/18/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/453` | 1.000155 | Ward off a blow with your shield |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/5` | 0.731124 | You snap your shield in place to ward off a blow. Your shield  prevents you from taking an amount of damage up to the  shield's Hardness. You and the shield each take any remaining  damage, possibly b |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/4` | 0.538306 | **Trigger** While you have your shield raised, you would take  physical damage (bludgeoning, piercing, or slashing) from  an attack. |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/426` | 0.458053 | Ward Medic |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/18/TableCell/409` | 0.405955 | Armor, shields and upgrades |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/21/Text/7` | 0.388935 | **WARD MEDIC** **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/1` | 0.372147 | Attempt a Deception check against the Will DC of a target within  60 feet. On a success, the target is off-guard for 1 round, and on  a critical success, it's confused for 1 round. The target's reacti |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/450` | 0.371315 | Shield Block |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/2` | 0.366655 | **SHIELD BLOCK **[reaction] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/540` | 0.366343 | Jump off walls |

### Query 64
- Text: Summarize Toughness
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/454']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/454', 'PZO22001 Starfinder Player Core 210-231::/page/19/SectionHeader/55', 'PZO22001 Starfinder Player Core 210-231::/page/10/Text/48']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/454` | 0.937453 | Toughness |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/19/SectionHeader/55` | 0.573924 | **TOUGHNESS** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/48` | 0.412933 | You step carefully and quickly. You can Step into difficult terrain. |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/58` | 0.348756 | Your body can withstand more punishment than most before  succumbing. Increase your maximum Hit Points by your level.  You reduce the DC of recovery checks by 1 (page 403). |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/437` | 0.333706 | Step into difficult terrain |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/11/Text/28` | 0.319642 | You can strong-arm people effectively, even when you don't  have them isolated. When you Coerce, you can compare  your Intimidation check result to the Will DCs of up to five  targets instead of one. |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/11/SectionHeader/1` | 0.309449 | **Trigger** You take damage. |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/30` | 0.302670 | You move through crowds without slowing down. You can  move at full Speed in crowds. Treat areas truly packed with  people as difficult terrain instead of greater difficult terrain. |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/5` | 0.302628 | You snap your shield in place to ward off a blow. Your shield  prevents you from taking an amount of damage up to the  shield's Hardness. You and the shield each take any remaining  damage, possibly b |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/33` | 0.300619 | **Prerequisites** Strength +3, expert in Intimidation |

### Query 65
- Text: Summarize 1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/455']
- Expected found: `True`
- Expected rank: `24`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/490', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/502']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/626` | 0.669108 | 1 |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/502` | 0.669108 | 1 |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/490` | 0.669108 | 1 |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/562` | 0.627108 | 1 |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/526` | 0.627108 | 1 |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/510` | 0.627108 | 1 |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/419` | 0.627108 | 1 |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/518` | 0.627108 | 1 |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/514` | 0.627108 | 1 |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/549` | 0.627108 | 1 |

### Query 66
- Text: Summarize —
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/456']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/440', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/452', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/456']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/440` | 0.572766 | — |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/452` | 0.572766 | — |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/456` | 0.572766 | — |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/444` | 0.530766 | — |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/416` | 0.530766 | — |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/412` | 0.530766 | — |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/428` | 0.530766 | — |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/691` | 0.530766 | — |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/404` | 0.530766 | — |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/424` | 0.530766 | — |

### Query 67
- Text: What is the rule about Increase your maximum HP and reduce the DCs of?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/457']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/457', 'PZO22001 Starfinder Player Core 210-231::/page/19/Text/58', 'PZO22001 Starfinder Player Core 210-231::/page/10/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/457` | 0.699202 | Increase your maximum HP and reduce the DCs of recovery checks |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/58` | 0.554534 | Your body can withstand more punishment than most before  succumbing. Increase your maximum Hit Points by your level.  You reduce the DC of recovery checks by 1 (page 403). |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/21` | 0.495983 | You know how to get there fast. When calculating your travel  Speed for the day while piloting a vehicle, you can attempt  a Piloting check to increase your vehicle's travel Speed for  long-term overl |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/25` | 0.451762 | You can negotiate incredibly quickly in adverse situations.  You attempt to Make an Impression and then Request  your opponent cease their current activity and engage in  negotiations. You take a –5 p |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/6` | 0.442184 | If you activate a magic item that requires a spell attack  modifier or spell DC and you don't have proficiency in the  relevant statistic, use your level as your proficiency bonus  and the highest of |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/19` | 0.438044 | You use your medical training to ameliorate sickness or  assuage fears. When you use Medicine to Administer First  Aid, instead of Stabilizing a character or Stopping Bleeding,  you can reduce an ally |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/52` | 0.435961 | Attempt a Computers check to Hack an adjacent creature,  hazard, or item with the tech trait. The DC is equal to the  creature, item, or hazard's Fortitude DC, or the Fortitude  DC of the creature att |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/35` | 0.433791 | You implant one augmentation with an item level equal to  your character level or lower. This augmentation doesn't  count against your total implant limit. The first time you take  this feat, the augm |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/22` | 0.432682 | crowd out of your way. A GM might use a different DC under  certain circumstances, such as when the crowd has a level or  set DC to disperse. |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/20` | 0.431322 | You've discovered medical breakthroughs or techniques that  achieve miraculous results. Once per day for each target, you  can spend 1 hour treating that target and attempt a Medicine  check to remove |

### Query 68
- Text: What is the rule about Weapon Proficiency?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/458']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/458', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/406', 'PZO22001 Starfinder Player Core 210-231::/page/21/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/458` | 0.887186 | Weapon Proficiency |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/406` | 0.672874 | Armor Proficiency |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/21/SectionHeader/16` | 0.672424 | **WEAPON PROFICIENCY** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/21/Text/19` | 0.507435 | You become trained in all martial weapons. If you were  already trained in all martial weapons, you become trained  in one advanced weapon of your choice. If you are at least  11th level, you also bec |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/461` | 0.502288 | Become trained in a weapon type |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/6` | 0.495248 | you gain a skill feat, you must select a general feat with  the skill trait; you can't select a general feat that lacks the  skill trait. The level of a skill feat is typically the minimum  level at w |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/6` | 0.491751 | If you activate a magic item that requires a spell attack  modifier or spell DC and you don't have proficiency in the  relevant statistic, use your level as your proficiency bonus  and the highest of |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/1` | 0.490435 | they're trained. The skill must be Crafting or another skill  relevant to the item, as determined by the GM. For example,  a PC might use Religion to help you Craft an item with the  divine trait or W |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/21/Text/20` | 0.466213 | **Special** You can select this feat more than once. Each time  you do, you become trained in an advanced weapon. |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/21` | 0.447857 | **ARMOR PROFICIENCY FEAT 1** |

### Query 69
- Text: What is the rule about Gain a 1st-level ancestry feat?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/465']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/465', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/405', 'PZO22001 Starfinder Player Core 210-231::/page/6/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/465` | 0.920093 | Gain a 1st-level ancestry feat |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/405` | 0.707229 | Gain access to ancestry feats from another ancestry |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/14` | 0.691032 | Whether through instinct, study, or magic, you feel a deeper  connection to your ancestry. You gain a 1st-level ancestry feat. |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/14` | 0.605820 | long as the ancestry feats don't require any physiological  feature that you lack, as determined by the GM. |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/1/Table/9` | 0.587506 | Non-Skill FeatsLevelPrerequisitesBenefitsAdopted Ancestry1—Gain access to ancestry feats from another ancestryArmor Proficiency1—Become trained in a type of armorAugmented Body1—Gain a free augmentati |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/4` | 0.566698 | For most classes, you gain a general feat when you reach  3rd level and every 4 levels thereafter. Each time you gain  a general feat, you can select any feat with the general  trait whose prerequisit |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/6` | 0.531943 | you gain a skill feat, you must select a general feat with  the skill trait; you can't select a general feat that lacks the  skill trait. The level of a skill feat is typically the minimum  level at w |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/13` | 0.530330 | You're fully immersed in another ancestry's culture and  traditions, whether born into them, earned through a rite of  passage, or bonded through a deep friendship or romance.  Choose a common ancestr |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/35` | 0.497855 | You implant one augmentation with an item level equal to  your character level or lower. This augmentation doesn't  count against your total implant limit. The first time you take  this feat, the augm |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/5` | 0.475937 | General feats also include a subcategory of skill feats,  which expand on what you can accomplish via skills.  These feats also have the skill trait. Most characters gain  skill feats at 2nd level and |

### Query 70
- Text: What is the rule about Become more adept at using untrained skills?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/473']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/473', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/428', 'PZO22001 Starfinder Player Core 210-231::/page/20/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/473` | 0.902534 | Become more adept at using untrained skills |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/428` | 0.598062 | Become trained in a skill |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/23` | 0.594910 | You've learned how to handle situations when you're out of  your depth. Your proficiency bonus to untrained skill checks |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/14` | 0.520793 | You become trained in the skill of your choice. |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/24` | 0.490512 | is equal to your level –2. This improves to your level –1 at 5th  level and your full level at 7th level. This doesn't allow you to  use the skill's trained actions. |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/488` | 0.484219 | Trained in at least one skill |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/8` | 0.480642 | Your knowledge has expanded to encompass a new field.  Choose a Lore skill subcategory. You become trained in it. At  3rd, 7th, and 15th levels, you gain an additional skill increase  you can apply on |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/6` | 0.463546 | If you activate a magic item that requires a spell attack  modifier or spell DC and you don't have proficiency in the  relevant statistic, use your level as your proficiency bonus  and the highest of |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/21/Text/19` | 0.454450 | You become trained in all martial weapons. If you were  already trained in all martial weapons, you become trained  in one advanced weapon of your choice. If you are at least  11th level, you also bec |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/6` | 0.453281 | you gain a skill feat, you must select a general feat with  the skill trait; you can't select a general feat that lacks the  skill trait. The level of a skill feat is typically the minimum  level at w |

### Query 71
- Text: What is the rule about **GENERAL SKILL FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/SectionHeader/10', 'PZO22001 Starfinder Player Core 210-231::/page/1/SectionHeader/8', 'PZO22001 Starfinder Player Core 210-231::/page/9/Text/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/SectionHeader/10` | 0.907389 | **GENERAL SKILL FEATS** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/SectionHeader/8` | 0.701525 | **GENERAL FEATS** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/9/Text/19` | 0.659671 | **GENERAL** **SKILL** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/9/Text/14` | 0.617671 | **GENERAL** **SKILL** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/14` | 0.617671 | **GENERAL** **SKILL** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/39` | 0.617671 | **GENERAL** **SKILL** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/9/Text/9` | 0.617671 | **GENERAL** **SKILL** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/9/Text/4` | 0.617671 | **GENERAL** **SKILL** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/50` | 0.617671 | **GENERAL** **SKILL** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/34` | 0.617671 | **GENERAL** **SKILL** |

### Query 72
- Text: Lookup values for Varying Skill FeatsLevelPrerequisitesBenefitsAssurance1Trained in at least one skillReceive a fixed result on a skill checkDubious Knowledge1Trained in a skill with the
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/Table/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/Table/11', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/482', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/413']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/Table/11` | 0.775766 | Varying Skill FeatsLevelPrerequisitesBenefitsAssurance1Trained in at least one skillReceive a fixed result on a skill checkDubious Knowledge1Trained in a skill with the Recall Knowledge actionLearn tr |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/482` | 0.676365 | Varying Skill Feats |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/413` | 0.676365 | Varying Skill Feats |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/7` | 0.595049 | In addition to the skill feats specifically associated with  each skill, there are some that can be taken with various  skills or even all skills, like Assurance. |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/2/Table/1` | 0.585880 | Varying Skill FeatsLevelPrerequisitesBenefitsRecognize Spell1Trained in Arcana, Nature, Occultism, or ReligionIdentify a spell as a reaction as it's being castSeasoned1Trained in Alcohol Lore, Cooking |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/489` | 0.583024 | Receive a fixed result on a skill check |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/42` | 0.575269 | You know basic facts off the top of your head. Choose a skill  you're an expert in that has the Recall Knowledge action and  for which you have the Assurance feat. You can use the Recall  Knowledge ac |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/6` | 0.571364 | you gain a skill feat, you must select a general feat with  the skill trait; you can't select a general feat that lacks the  skill trait. The level of a skill feat is typically the minimum  level at w |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/4/Table/1` | 0.549373 | Lore Skill FeatsLevelPrerequisitesBenefitsLegendary Professional15Legendary in LoreGain renown for your LoreMedicine Skill FeatsLevelPrerequisitesBenefitsBattle Medicine1Trained in MedicineHeal yourse |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/5` | 0.548435 | General feats also include a subcategory of skill feats,  which expand on what you can accomplish via skills.  These feats also have the skill trait. Most characters gain  skill feats at 2nd level and |

### Query 73
- Text: What is the rule about Varying Skill Feats?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/482']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/413', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/482', 'PZO22001 Starfinder Player Core 210-231::/page/1/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/413` | 0.888428 | Varying Skill Feats |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/482` | 0.888428 | Varying Skill Feats |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/6` | 0.638234 | you gain a skill feat, you must select a general feat with  the skill trait; you can't select a general feat that lacks the  skill trait. The level of a skill feat is typically the minimum  level at w |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/5` | 0.601296 | General feats also include a subcategory of skill feats,  which expand on what you can accomplish via skills.  These feats also have the skill trait. Most characters gain  skill feats at 2nd level and |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/398` | 0.582881 | Non-Skill Feats |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/545` | 0.576026 | Computers Skill Feats |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/474` | 0.572713 | Performance Skill Feats |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/398` | 0.569938 | Lore Skill Feats |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/7` | 0.559890 | In addition to the skill feats specifically associated with  each skill, there are some that can be taken with various  skills or even all skills, like Assurance. |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/573` | 0.557983 | Crafting Skill Feats |

### Query 74
- Text: What is the rule about Prerequisites?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/484']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/400', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/484', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/575']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/400` | 0.784633 | Prerequisites |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/484` | 0.784633 | Prerequisites |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/575` | 0.784633 | Prerequisites |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/547` | 0.742633 | Prerequisites |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/451` | 0.742633 | Prerequisites |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/499` | 0.742633 | Prerequisites |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/415` | 0.742633 | Prerequisites |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/483` | 0.742633 | Prerequisites |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/651` | 0.742633 | Prerequisites |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/687` | 0.742633 | Prerequisites |

### Query 75
- Text: What is the rule about Trained in at least one skill?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/488']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/488', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/428', 'PZO22001 Starfinder Player Core 210-231::/page/6/Text/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/488` | 0.837647 | Trained in at least one skill |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/428` | 0.712664 | Become trained in a skill |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/29` | 0.697461 | **Prerequisites** trained in at least one skill |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/14` | 0.568139 | You become trained in the skill of your choice. |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/21/Text/19` | 0.534190 | You become trained in all martial weapons. If you were  already trained in all martial weapons, you become trained  in one advanced weapon of your choice. If you are at least  11th level, you also bec |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/425` | 0.523480 | Skill Training |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/492` | 0.503716 | Trained in Performance |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/488` | 0.503716 | Trained in Performance |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/484` | 0.503716 | Trained in Performance |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/480` | 0.503716 | Trained in Performance |

### Query 76
- Text: What is the rule about Receive a fixed result on a skill check?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/489']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/489', 'PZO22001 Starfinder Player Core 210-231::/page/6/Text/30', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/493']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/489` | 0.916472 | Receive a fixed result on a skill check |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/30` | 0.619113 | Even in the worst circumstances, you can perform basic tasks.  Choose a skill you're trained in. You can forgo rolling a skill check  for that skill to instead receive a result of 10 + your proficienc |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/493` | 0.606767 | Learn true and erroneous knowledge on failed check Knowledge skill |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/6` | 0.472529 | you gain a skill feat, you must select a general feat with  the skill trait; you can't select a general feat that lacks the  skill trait. The level of a skill feat is typically the minimum  level at w |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/41` | 0.472173 | You have exceptional talent with one type of performance.  You gain a +1 circumstance bonus when making a certain  type of performance. If you are a master in Performance, this  bonus increases to +2. |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/42` | 0.471669 | You know basic facts off the top of your head. Choose a skill  you're an expert in that has the Recall Knowledge action and  for which you have the Assurance feat. You can use the Recall  Knowledge ac |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/1/Table/11` | 0.469809 | Varying Skill FeatsLevelPrerequisitesBenefitsAssurance1Trained in at least one skillReceive a fixed result on a skill checkDubious Knowledge1Trained in a skill with the Recall Knowledge actionLearn tr |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/23` | 0.454299 | You've learned how to handle situations when you're out of  your depth. Your proficiency bonus to untrained skill checks |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/6` | 0.453759 | You carefully safeguard your professional endeavors to  prevent disaster. When you use Lore to Earn Income, if you roll  a critical failure, you instead get a failure. If you're an expert  in Lore, yo |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/49` | 0.444918 | As long as you're using a comm unit, datapad, or computer  to communicate, when you attempt to use a skill action with  the linguistic trait on a creature that doesn't understand the  language you're |

### Query 77
- Text: What is the rule about Trained in a skill with the?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/492']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/428', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/488', 'PZO22001 Starfinder Player Core 210-231::/page/18/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/428` | 0.750078 | Become trained in a skill |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/488` | 0.672779 | Trained in at least one skill |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/14` | 0.636271 | You become trained in the skill of your choice. |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/425` | 0.548508 | Skill Training |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/29` | 0.526903 | **Prerequisites** trained in at least one skill |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/24` | 0.499599 | is equal to your level –2. This improves to your level –1 at 5th  level and your full level at 7th level. This doesn't allow you to  use the skill's trained actions. |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/492` | 0.496422 | Trained in a skill with the Recall Knowledge action |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/24` | 0.489224 | You become trained in light armor. If you already were trained  in light armor, you gain training in medium armor. If you were  trained in both, you become trained in heavy armor. If you are  at least |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/480` | 0.487896 | Trained in Performance |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/484` | 0.487896 | Trained in Performance |

### Query 78
- Text: What is the rule about Learn true and erroneous knowledge on failed check?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/493']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/493', 'PZO22001 Starfinder Player Core 210-231::/page/9/Text/16', 'PZO22001 Starfinder Player Core 210-231::/page/6/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/493` | 0.902559 | Learn true and erroneous knowledge on failed check Knowledge skill |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/9/Text/16` | 0.646212 | You're a treasure trove of information, but not all of it comes  from reputable sources. When you fail (but don't critically fail)  a Recall Knowledge check using any skill, you learn the correct  ans |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/4` | 0.616456 | **Failure** You gain a piece of information or context and two  pieces of erroneous information. |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/3` | 0.546565 | **Success** You recall accurately and gain two pieces of  information or context and a piece of erroneous information,  but you don't have any way to differentiate which is which. |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/39` | 0.538219 | You've researched many faiths enough to recognize notions  about them that are unlikely to be true. If you roll a critical  failure at a Religion check to Decipher Writing of a religious  nature or to |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/5` | 0.529938 | **Critical Failure **You gain three pieces of erroneous information. |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/1/Table/11` | 0.495188 | Varying Skill FeatsLevelPrerequisitesBenefitsAssurance1Trained in at least one skillReceive a fixed result on a skill checkDubious Knowledge1Trained in a skill with the Recall Knowledge actionLearn tr |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/6` | 0.493231 | You carefully safeguard your professional endeavors to  prevent disaster. When you use Lore to Earn Income, if you roll  a critical failure, you instead get a failure. If you're an expert  in Lore, yo |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/64` | 0.484604 | **Success** The animal learns the action. If it was an action the  animal already knew, you can Command the Animal to take  that action without attempting a Nature check. If it was a  new basic action |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/490` | 0.483226 | Dubious Knowledge |

### Query 79
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/Text/14', 'PZO22001 Starfinder Player Core 210-231::/page/13/Text/60', 'PZO22001 Starfinder Player Core 210-231::/page/3/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/14` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/60` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/3/Text/4` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/55` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/68` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/53` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/26` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/62` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/5/SectionHeader/10` | 0.374501 | **ADOPTED ANCESTRY FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/13` | 0.346623 | You're fully immersed in another ancestry's culture and  traditions, whether born into them, earned through a rite of  passage, or bonded through a deep friendship or romance.  Choose a common ancestr |

### Query 80
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/Text/16', 'PZO22001 Starfinder Player Core 210-231::/page/13/Text/62', 'PZO22001 Starfinder Player Core 210-231::/page/3/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/16` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/62` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/3/Text/6` | 0.864442 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/70` | 0.822442 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/64` | 0.822442 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/55` | 0.822442 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/57` | 0.822442 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/28` | 0.822442 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/34` | 0.671444 | **GENERAL** **SKILL** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/27` | 0.671444 | **GENERAL** **SKILL** |

### Query 81
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/Text/17']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/17/Text/56', 'PZO22001 Starfinder Player Core 210-231::/page/5/Text/29', 'PZO22001 Starfinder Player Core 210-231::/page/19/Text/71']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/56` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/29` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/71` | 0.871817 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/63` | 0.829817 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/65` | 0.829817 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/17` | 0.829817 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/58` | 0.829817 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/3/Text/7` | 0.829817 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/1/SectionHeader/1` | 0.701414 | CHAPTER 5: FEATS |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/67` | 0.496910 | **Feats** |

### Query 82
- Text: What is the rule about **Feats Table**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/Text/18']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/66', 'PZO22001 Starfinder Player Core 210-231::/page/13/Text/64', 'PZO22001 Starfinder Player Core 210-231::/page/15/Text/59']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/66` | 0.853515 | **Feats Table** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/64` | 0.853515 | **Feats Table** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/59` | 0.853515 | **Feats Table** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/3/Text/8` | 0.811515 | **Feats Table** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/30` | 0.811515 | **Feats Table** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/18` | 0.811515 | **Feats Table** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/72` | 0.811515 | **Feats Table** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/57` | 0.811515 | **Feats Table** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/65` | 0.610461 | **Feats** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/67` | 0.610461 | **Feats** |

### Query 83
- Text: What is the rule about **Feats**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/Text/19']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/5/Text/31', 'PZO22001 Starfinder Player Core 210-231::/page/7/Text/67', 'PZO22001 Starfinder Player Core 210-231::/page/19/Text/73']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/31` | 0.776381 | **Feats** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/67` | 0.776381 | **Feats** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/73` | 0.776381 | **Feats** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/58` | 0.734381 | **Feats** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/19` | 0.734381 | **Feats** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/60` | 0.734381 | **Feats** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/3/Text/9` | 0.734381 | **Feats** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/65` | 0.734381 | **Feats** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/65` | 0.659229 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/63` | 0.659229 | **FEATS** |

### Query 84
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/1/Text/21']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/13/Text/67', 'PZO22001 Starfinder Player Core 210-231::/page/17/Text/60', 'PZO22001 Starfinder Player Core 210-231::/page/15/Text/62']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/62` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/67` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/60` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/21` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/3/Text/11` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/33` | 0.847304 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/75` | 0.847304 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/69` | 0.847304 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/1` | 0.558497 | **RECOGNIZE SPELL **[reaction] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/70` | 0.388254 | **SKILLS** |

### Query 85
- Text: Lookup values for Varying Skill FeatsLevelPrerequisitesBenefitsRecognize Spell1Trained in Arcana, Nature,
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/2/Table/1']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/Table/11', 'PZO22001 Starfinder Player Core 210-231::/page/2/Table/1', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/481']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/Table/11` | 0.799650 | Varying Skill FeatsLevelPrerequisitesBenefitsAssurance1Trained in at least one skillReceive a fixed result on a skill checkDubious Knowledge1Trained in a skill with the Recall Knowledge actionLearn tr |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/2/Table/1` | 0.768286 | Varying Skill FeatsLevelPrerequisitesBenefitsRecognize Spell1Trained in Arcana, Nature, Occultism, or ReligionIdentify a spell as a reaction as it's being castSeasoned1Trained in Alcohol Lore, Cooking |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/481` | 0.662514 | Arcana Skill Feats |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/482` | 0.617295 | Varying Skill Feats |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/413` | 0.617295 | Varying Skill Feats |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/4/Table/1` | 0.612480 | Lore Skill FeatsLevelPrerequisitesBenefitsLegendary Professional15Legendary in LoreGain renown for your LoreMedicine Skill FeatsLevelPrerequisitesBenefitsBattle Medicine1Trained in MedicineHeal yourse |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/34` | 0.610888 | **Prerequisites** master in Arcana, Nature, Occultism, or Religion;  Recognize Spell |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/447` | 0.598087 | Master in Arcana, Nature, Occultism, or Religion; Recognize Spell |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/1/Table/9` | 0.589975 | Non-Skill FeatsLevelPrerequisitesBenefitsAdopted Ancestry1—Gain access to ancestry feats from another ancestryArmor Proficiency1—Become trained in a type of armorAugmented Body1—Gain a free augmentati |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/5` | 0.568286 | Attempt a check using the skill matching the item's magic  tradition, or matching a tradition that has the spell on its list,  if you're trying to cast a spell from the item. The relevant skills  are |

### Query 86
- Text: What is the rule about Varying Skill Feats?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/413']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/413', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/482', 'PZO22001 Starfinder Player Core 210-231::/page/1/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/413` | 0.888428 | Varying Skill Feats |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/482` | 0.888428 | Varying Skill Feats |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/6` | 0.638234 | you gain a skill feat, you must select a general feat with  the skill trait; you can't select a general feat that lacks the  skill trait. The level of a skill feat is typically the minimum  level at w |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/5` | 0.601296 | General feats also include a subcategory of skill feats,  which expand on what you can accomplish via skills.  These feats also have the skill trait. Most characters gain  skill feats at 2nd level and |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/398` | 0.582882 | Non-Skill Feats |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/545` | 0.576026 | Computers Skill Feats |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/474` | 0.572713 | Performance Skill Feats |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/398` | 0.569938 | Lore Skill Feats |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/1/Text/7` | 0.559890 | In addition to the skill feats specifically associated with  each skill, there are some that can be taken with various  skills or even all skills, like Assurance. |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/573` | 0.557983 | Crafting Skill Feats |

### Query 87
- Text: What is the rule about Prerequisites?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/415']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/400', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/484', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/575']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/400` | 0.784633 | Prerequisites |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/484` | 0.784633 | Prerequisites |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/575` | 0.784633 | Prerequisites |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/547` | 0.742633 | Prerequisites |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/451` | 0.742633 | Prerequisites |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/499` | 0.742633 | Prerequisites |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/415` | 0.742633 | Prerequisites |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/483` | 0.742633 | Prerequisites |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/651` | 0.742633 | Prerequisites |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/687` | 0.742633 | Prerequisites |

### Query 88
- Text: What is the rule about Recognize Spell?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/417']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/417', 'PZO22001 Starfinder Player Core 210-231::/page/16/Text/35', 'PZO22001 Starfinder Player Core 210-231::/page/17/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/417` | 0.888192 | Recognize Spell |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/35` | 0.701373 | You Recognize Spells swiftly. Once per round, you can  Recognize a Spell using a skill in which you're a master as a  free action. |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/7` | 0.630273 | **Success** You correctly recognize the spell. |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/8` | 0.546891 | **Failure** You fail to recognize the spell. |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/447` | 0.519854 | Master in Arcana, Nature, Occultism, or Religion; Recognize Spell |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/445` | 0.518694 | Quick Recognition |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/1` | 0.518346 | **RECOGNIZE SPELL **[reaction] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/5` | 0.488031 | If you are trained in the appropriate skill for the spell's  tradition and it's a common spell of 2nd rank or lower, you  automatically identify it (you still roll to attempt to get a  critical succes |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/15` | 0.477036 | You can spend 10 minutes assessing the area around you for  signs of creatures. Attempt a Survival check against a DC  determined by the GM based on how obvious the signs are.  On a success, you can a |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/6` | 0.464791 | You can draw upon strange variations in your spellcasting,  whether or not you can cast occult spells. The DCs to Recognize  Spells you cast and Identify Magic you use increase by 5. |

### Query 89
- Text: What is the rule about Identify a spell as a reaction as it's being cast?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/420']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/420', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/448', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/417']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/420` | 0.936863 | Identify a spell as a reaction as it's being cast |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/448` | 0.593864 | Identify spells as a free action |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/417` | 0.577501 | Recognize Spell |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/35` | 0.525259 | You Recognize Spells swiftly. Once per round, you can  Recognize a Spell using a skill in which you're a master as a  free action. |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/7` | 0.520443 | **Success** You correctly recognize the spell. |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/6` | 0.511581 | You can draw upon strange variations in your spellcasting,  whether or not you can cast occult spells. The DCs to Recognize  Spells you cast and Identify Magic you use increase by 5. |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/5` | 0.506245 | If you are trained in the appropriate skill for the spell's  tradition and it's a common spell of 2nd rank or lower, you  automatically identify it (you still roll to attempt to get a  critical succes |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/4` | 0.497040 | **Prerequisites** trained in Arcana, Nature, Occultism, or Religion **Trigger** A creature within line of sight casts a spell that you  don't have prepared or in your spell repertoire, or a trap or  s |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/5` | 0.494137 | Attempt a check using the skill matching the item's magic  tradition, or matching a tradition that has the spell on its list,  if you're trying to cast a spell from the item. The relevant skills  are |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/49` | 0.492715 | When you become aware of a magical effect or see a spell  being cast, you can immediately determine if it twists minds  (with the mental trait), fights against fortune (with the fortune  or misfortune |

### Query 90
- Text: What is the rule about +1 to Craft food and drink, including serums and spell?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/424']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/424', 'PZO22001 Starfinder Player Core 210-231::/page/17/Text/41', 'PZO22001 Starfinder Player Core 210-231::/page/17/Text/46']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/424` | 0.845477 | +1 to Craft food and drink, including serums and spell ampoules |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/41` | 0.744088 | **Prerequisites** trained in Alcohol Lore, Cooking Lore, or Crafting You've mastered the preparation of many types of food and  drink. You gain a +1 circumstance bonus to checks to Craft  food and dri |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/46` | 0.650559 | You can Craft serums and medical items with the consumable  trait (page 197), though some have other requirements. When  you select this feat, you gain formulas for four common  serums of 2nd level or |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/524` | 0.583963 | Craft serums |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/521` | 0.528340 | Serum Crafting |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/528` | 0.524695 | Gain bonuses to Craft certain items |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/23` | 0.516466 | Your training focused on Crafting one particular kind of  item. Select one of the specialties listed below; you gain a +1  circumstance bonus to Crafting checks to Craft items of that  type. If you ar |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/42` | 0.493568 | **SERUM CRAFTING** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/16` | 0.486883 | You can find ways to craft just about anything, despite  restrictions. As long as you have the appropriate Crafting  skill feat (such as Magical Crafting for magic items) and meet  the item's level an |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/16` | 0.473327 | You can Craft magic items (page 197), though some have  other requirements. When you select this feat, you gain  formulas for four common magic items of 2nd level or lower. |

### Query 91
- Text: What is the rule about Skill Training?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/425']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/425', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/428', 'PZO22001 Starfinder Player Core 210-231::/page/18/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/425` | 0.798795 | Skill Training |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/428` | 0.655805 | Become trained in a skill |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/14` | 0.580585 | You become trained in the skill of your choice. |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/488` | 0.528965 | Trained in at least one skill |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/11` | 0.512760 | **SKILL TRAINING** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/29` | 0.492383 | **Prerequisites** trained in at least one skill |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/70` | 0.486108 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/57` | 0.486108 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/62` | 0.486108 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/3/Text/6` | 0.486108 | **SKILLS** |

### Query 92
- Text: What is the rule about Become trained in a skill?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/428']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/428', 'PZO22001 Starfinder Player Core 210-231::/page/18/Text/14', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/488']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/428` | 0.850527 | Become trained in a skill |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/14` | 0.712908 | You become trained in the skill of your choice. |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/488` | 0.676078 | Trained in at least one skill |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/425` | 0.572229 | Skill Training |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/29` | 0.570326 | **Prerequisites** trained in at least one skill |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/473` | 0.532399 | Become more adept at using untrained skills |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/15` | 0.521270 | **Special** You can select this feat multiple times, choosing a new  skill to become trained in each time. |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/24` | 0.513587 | You become trained in light armor. If you already were trained  in light armor, you gain training in medium armor. If you were  trained in both, you become trained in heavy armor. If you are  at least |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/24` | 0.512892 | is equal to your level –2. This improves to your level –1 at 5th  level and your full level at 7th level. This doesn't allow you to  use the skill's trained actions. |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/8` | 0.511122 | Your knowledge has expanded to encompass a new field.  Choose a Lore skill subcategory. You become trained in it. At  3rd, 7th, and 15th levels, you gain an additional skill increase  you can apply on |

### Query 93
- Text: What is the rule about Activate a magic item you normally can't activate?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/432']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/432', 'PZO22001 Starfinder Player Core 210-231::/page/20/Text/4', 'PZO22001 Starfinder Player Core 210-231::/page/20/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/432` | 0.934604 | Activate a magic item you normally can't activate |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/4` | 0.674769 | **Prerequisites** trained in Arcana, Nature, Occultism, or Religion You examine a magic item you normally couldn't use in an  effort to fool it and activate it temporarily. For example,  this might al |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/7` | 0.634197 | **Success** For the rest of the current turn, you can spend  actions to activate the item as if you could normally use it. **Failure** You can't use the item or try to trick it again this turn, |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/16` | 0.529627 | You can find ways to craft just about anything, despite  restrictions. As long as you have the appropriate Crafting  skill feat (such as Magical Crafting for magic items) and meet  the item's level an |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/16` | 0.511230 | You can Craft magic items (page 197), though some have  other requirements. When you select this feat, you gain  formulas for four common magic items of 2nd level or lower. |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/46` | 0.479427 | The GM might allow you to invent uncommon or rare  formulas, typically with an increased DC. You need the  Machine Magic feat to invent hybrid items and the Magical  Crafting feat to invent magical fo |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/540` | 0.477092 | Craft magic items |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/5` | 0.470211 | Attempt a check using the skill matching the item's magic  tradition, or matching a tradition that has the spell on its list,  if you're trying to cast a spell from the item. The relevant skills  are |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/6` | 0.467899 | If you activate a magic item that requires a spell attack  modifier or spell DC and you don't have proficiency in the  relevant statistic, use your level as your proficiency bonus  and the highest of |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/14` | 0.463136 | You understand the common underpinnings of the four  traditions of magic and magical essences,. Whenever you use  a skill action or a skill feat that requires a Nature, Occultism,  or Religion check, |

### Query 94
- Text: What is the rule about Without a Trace?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/433']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/433', 'PZO22001 Starfinder Player Core 210-231::/page/21/Text/21', 'PZO22001 Starfinder Player Core 210-231::/page/10/Text/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/433` | 0.863648 | Without a Trace |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/21/Text/21` | 0.687538 | **WITHOUT A TRACE** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/16` | 0.478373 | Tracking is second nature to you, and when necessary you can  follow a trail without pause. You can Track while moving at full  Speed by taking a –5 penalty to your Survival check. If you're  a master |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/42` | 0.424002 | You're always sneaking unless you choose to be seen, even  when there's nowhere to hide. You can Hide and Sneak even  without cover or being concealed. When you employ an  exploration tactic other tha |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/60` | 0.371315 | You're skilled at moving with a group. When you are  Avoiding Notice and your allies Follow the Expert, you and  those allies can roll a single Stealth check, using the lowest  modifier, instead of ro |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/10/SectionHeader/12` | 0.361828 | **EXPERIENCED TRACKER** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/21/Text/25` | 0.355083 | You're an expert at destroying or removing incriminating  evidence from a crime scene. When using the Cover Tracks  exploration activity, an yone tracking you must succeed  at a Perception check again |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/16` | 0.345808 | You can find ways to craft just about anything, despite  restrictions. As long as you have the appropriate Crafting  skill feat (such as Magical Crafting for magic items) and meet  the item's level an |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/571` | 0.345265 | Hide and Sneak without cover or being concealed |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/576` | 0.339728 | Experienced Tracker |

### Query 95
- Text: What is the rule about Clean up a crime scene or cover your tracks?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/436']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/436', 'PZO22001 Starfinder Player Core 210-231::/page/21/Text/25', 'PZO22001 Starfinder Player Core 210-231::/page/6/Text/52']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/436` | 0.926250 | Clean up a crime scene or cover your tracks |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/21/Text/25` | 0.615301 | You're an expert at destroying or removing incriminating  evidence from a crime scene. When using the Cover Tracks  exploration activity, an yone tracking you must succeed  at a Perception check again |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/52` | 0.444807 | You hastily create a barricade using nearby items, junk, or  debris. The barricade provides lesser cover for you and one  other ally, though you can Take Cover to increase this benefit  to standard co |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/16` | 0.366843 | Tracking is second nature to you, and when necessary you can  follow a trail without pause. You can Track while moving at full  Speed by taking a –5 penalty to your Survival check. If you're  a master |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/26` | 0.365241 | You know how to get lost in a crowd. You can use cover  from crowds to Hide and Sneak, gaining a +2 circumstance |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/42` | 0.362741 | You're always sneaking unless you choose to be seen, even  when there's nowhere to hide. You can Hide and Sneak even  without cover or being concealed. When you employ an  exploration tactic other tha |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/15` | 0.345565 | You can spend 10 minutes assessing the area around you for  signs of creatures. Attempt a Survival check against a DC  determined by the GM based on how obvious the signs are.  On a success, you can a |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/11` | 0.339287 | You often smuggle things past the authorities. When the GM  rolls your Stealth check to see if a passive observer notices a  small item you've concealed, the GM uses the number rolled  or 10—whichever |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/469` | 0.337821 | Dive for Cover |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/52` | 0.336951 | Your ability to Steal defies belief. You can attempt to Steal  something that is actively wielded or that would be extremely  noticeable or time consuming to remove (like worn shoes or  armor). You mu |

### Query 96
- Text: What is the rule about Expert in Recall Knowledge,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/439']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/439', 'PZO22001 Starfinder Player Core 210-231::/page/6/Text/41', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/492']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/439` | 0.798004 | Expert in Recall Knowledge, Assurance in the relevant skill action |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/41` | 0.758413 | **Prerequisites** expert in a skill with the Recall Knowledge  action, Assurance in that skill |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/492` | 0.713205 | Trained in a skill with the Recall Knowledge action |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/9/Text/15` | 0.656544 | **Prerequisites** trained in a skill with the Recall Knowledge action |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/42` | 0.632799 | You know basic facts off the top of your head. Choose a skill  you're an expert in that has the Recall Knowledge action and  for which you have the Assurance feat. You can use the Recall  Knowledge ac |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/440` | 0.562237 | Recall Knowledge as a free action once per round |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/19` | 0.551262 | You never get information about your areas of expertise wrong.  When you Recall Knowledge using any Lore subcategory in  which you're trained, if you roll a critical failure, you get a  failure instea |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/1` | 0.543716 | You can briefly connect to the Akashic Records. You Recall  Knowledge using Occultism instead of any other skill  as though Occultism were applicable to perform Recall  Knowledge for that topic. |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/9/Text/16` | 0.519718 | You're a treasure trove of information, but not all of it comes  from reputable sources. When you fail (but don't critically fail)  a Recall Knowledge check using any skill, you learn the correct  ans |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/527` | 0.490146 | Use Society to Gather Information and Recall Knowledge |

### Query 97
- Text: What is the rule about Recall Knowledge as a free action once per round?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/440']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/440', 'PZO22001 Starfinder Player Core 210-231::/page/6/Text/42', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/492']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/440` | 0.966176 | Recall Knowledge as a free action once per round |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/42` | 0.752732 | You know basic facts off the top of your head. Choose a skill  you're an expert in that has the Recall Knowledge action and  for which you have the Assurance feat. You can use the Recall  Knowledge ac |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/492` | 0.742140 | Trained in a skill with the Recall Knowledge action |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/9/Text/15` | 0.664910 | **Prerequisites** trained in a skill with the Recall Knowledge action |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/41` | 0.622651 | **Prerequisites** expert in a skill with the Recall Knowledge  action, Assurance in that skill |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/439` | 0.606457 | Expert in Recall Knowledge, Assurance in the relevant skill action |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/34` | 0.540554 | You know about life on the streets and feel the pulse of your  local settlement. You can use your Society modifier instead  of your Diplomacy modifier to Gather Information. In any  settlement you fre |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/1` | 0.537385 | You can briefly connect to the Akashic Records. You Recall  Knowledge using Occultism instead of any other skill  as though Occultism were applicable to perform Recall  Knowledge for that topic. |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/35` | 0.533242 | You Recognize Spells swiftly. Once per round, you can  Recognize a Spell using a skill in which you're a master as a  free action. |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/527` | 0.519405 | Use Society to Gather Information and Recall Knowledge |

### Query 98
- Text: What is the rule about Master in Arcana, Nature,?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/447']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/448', 'PZO22001 Starfinder Player Core 210-231::/page/16/Text/34', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/447']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/448` | 0.725563 | Master in Nature |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/34` | 0.717456 | **Prerequisites** master in Arcana, Nature, Occultism, or Religion;  Recognize Spell |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/447` | 0.712342 | Master in Arcana, Nature, Occultism, or Religion; Recognize Spell |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/35` | 0.648457 | **Prerequisites** master in Nature |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/431` | 0.632093 | Trained in Arcana, Nature, Occultism, or Religion |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/496` | 0.632093 | Trained in Arcana, Nature, Occultism, or Religion |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/419` | 0.632093 | Trained in Arcana, Nature, Occultism, or Religion |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/491` | 0.588532 | Trained in Arcana |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/14` | 0.571204 | You understand the common underpinnings of the four  traditions of magic and magical essences,. Whenever you use  a skill action or a skill feat that requires a Nature, Occultism,  or Religion check, |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/19` | 0.567061 | **Prerequisites** trained in Arcana |

### Query 99
- Text: What is the rule about Identify spells as a free action?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/448']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/448', 'PZO22001 Starfinder Player Core 210-231::/page/16/Text/35', 'PZO22001 Starfinder Player Core 210-231::/page/16/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/448` | 0.925071 | Identify spells as a free action |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/35` | 0.647451 | You Recognize Spells swiftly. Once per round, you can  Recognize a Spell using a skill in which you're a master as a  free action. |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/20` | 0.559311 | **Prerequisites** trained in Arcana, Nature, Occultism or Religion You can Identify Magic swiftly. You take only 1 minute when  using Identify Magic to determine the properties of an item,  ongoing ef |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/417` | 0.513902 | Recognize Spell |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/57` | 0.486157 | When you roll initiative, you can yell a mighty battle cry and  Demoralize an observed foe as a free action. If you're legendary  in Intimidation, you can use a reaction to Demoralize your foe  when y |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/420` | 0.483217 | Identify a spell as a reaction as it's being cast |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/5` | 0.461863 | If you are trained in the appropriate skill for the spell's  tradition and it's a common spell of 2nd rank or lower, you  automatically identify it (you still roll to attempt to get a  critical succes |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/14` | 0.458377 | You understand the common underpinnings of the four  traditions of magic and magical essences,. Whenever you use  a skill action or a skill feat that requires a Nature, Occultism,  or Religion check, |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/440` | 0.457763 | Recall Knowledge as a free action once per round |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/9` | 0.443767 | **Critical Failure** You misidentify the spell as another spell  entirely, of the GM's choice. |

### Query 100
- Text: What is the rule about Acrobatics Skill Feats?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/449']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/449', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/497', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/475']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/449` | 0.898150 | Acrobatics Skill Feats |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/497` | 0.727127 | Athletics Skill Feats |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/475` | 0.704583 | Expert in Acrobatics |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/471` | 0.662583 | Expert in Acrobatics |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/37` | 0.655363 | **Prerequisites** expert in Acrobatics |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/9/Text/5` | 0.655363 | **Prerequisites** expert in Acrobatics |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/455` | 0.634275 | Trained in Acrobatics |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/459` | 0.634275 | Trained in Acrobatics |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/463` | 0.634275 | Trained in Acrobatics |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/467` | 0.634275 | Trained in Acrobatics |

### Query 101
- Text: What is the rule about Prerequisites?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/451']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/400', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/484', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/575']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/400` | 0.784633 | Prerequisites |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/484` | 0.784633 | Prerequisites |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/575` | 0.784633 | Prerequisites |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/547` | 0.742633 | Prerequisites |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/451` | 0.742633 | Prerequisites |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/499` | 0.742633 | Prerequisites |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/415` | 0.742633 | Prerequisites |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/483` | 0.742633 | Prerequisites |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/651` | 0.742633 | Prerequisites |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/687` | 0.742633 | Prerequisites |

### Query 102
- Text: What is the rule about Trained in Acrobatics?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/455']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/459', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/455', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/467']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/459` | 0.851272 | Trained in Acrobatics |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/455` | 0.851272 | Trained in Acrobatics |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/467` | 0.851272 | Trained in Acrobatics |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/463` | 0.809272 | Trained in Acrobatics |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/29` | 0.759012 | **Prerequisites** trained in Acrobatics |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/44` | 0.759012 | **Prerequisites** trained in Acrobatics |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/28` | 0.759012 | **Prerequisites** trained in Acrobatics |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/29` | 0.759012 | **Prerequisites** trained in Acrobatics |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/475` | 0.667903 | Expert in Acrobatics |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/471` | 0.667903 | Expert in Acrobatics |

### Query 103
- Text: Lookup values for Crafting Skill FeatsLevelPrerequisitesBenefitsQuick Install1Trained in CraftingInstall upgrades quicklyQuick Repair1Trained in CraftingRepair items quicklySerum Crafting1Trained in CraftingCraft serumsSpecialty Crafting1Trained in CraftingGain bonuses to Craft certain itemsCommunal Crafting2Expert in CraftingOther PCs can help you CraftInventor2Expert in CraftingUse Crafting to create item formulasMagical Crafting2Expert in CraftingCraft magic itemsPercussive Maintenance2Expert in CraftingFix a glitching tech itemTech Crafting2Expert in CraftingCraft technological itemsImpeccable Crafting7Master in Crafting,
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/3/Table/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/3/Table/1', 'PZO22001 Starfinder Player Core 210-231::/page/19/Text/30', 'PZO22001 Starfinder Player Core 210-231::/page/7/Text/58']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/3/Table/1` | 0.852753 | Crafting Skill FeatsLevelPrerequisitesBenefitsQuick Install1Trained in CraftingInstall upgrades quicklyQuick Repair1Trained in CraftingRepair items quicklySerum Crafting1Trained in CraftingCraft serum |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/30` | 0.697808 | You can Craft level 1 or higher tech items (page 197), though  some have other requirements, as listed in Chapter 6:  Equipment. When you select this feat, you gain formulas for  four common tech item |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/58` | 0.691954 | **Prerequisites** expert in Crafting |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/29` | 0.661954 | **Prerequisites** expert in Crafting |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/53` | 0.649954 | **Prerequisites** expert in Crafting |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/15` | 0.649954 | **Prerequisites** expert in Crafting |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/44` | 0.649954 | **Prerequisites** expert in Crafting |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/23` | 0.633325 | Your training focused on Crafting one particular kind of  item. Select one of the specialties listed below; you gain a +1  circumstance bonus to Crafting checks to Craft items of that  type. If you ar |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/509` | 0.631445 | Crafting Skill Feats |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/535` | 0.628855 | Expert in Crafting |

### Query 104
- Text: Lookup values for Lore Skill FeatsLevelPrerequisitesBenefitsLegendary Professional15Legendary in LoreGain renown for your LoreMedicine Skill FeatsLevelPrerequisitesBenefitsBattle Medicine1Trained in MedicineHeal yourself or an ally in battleContinual Recovery2Expert in MedicineTreat Wounds on a patient more oftenRobust Recovery2Expert in MedicineGreater benefits from Treat Disease and Treat PoisonUnusual Treatment2Expert in MedicineTreat Wounds tends to additional conditionsWard Medic2Expert in MedicineTreat several patients at onceAdvanced First Aid7Master in MedicineUse First Aid to reduce frightened and sickened condition
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/4/Table/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/4/Table/1', 'PZO22001 Starfinder Player Core 210-231::/page/1/Table/9', 'PZO22001 Starfinder Player Core 210-231::/page/2/Table/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/4/Table/1` | 0.914869 | Lore Skill FeatsLevelPrerequisitesBenefitsLegendary Professional15Legendary in LoreGain renown for your LoreMedicine Skill FeatsLevelPrerequisitesBenefitsBattle Medicine1Trained in MedicineHeal yourse |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/Table/9` | 0.720358 | Non-Skill FeatsLevelPrerequisitesBenefitsAdopted Ancestry1—Gain access to ancestry feats from another ancestryArmor Proficiency1—Become trained in a type of armorAugmented Body1—Gain a free augmentati |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/2/Table/1` | 0.695480 | Varying Skill FeatsLevelPrerequisitesBenefitsRecognize Spell1Trained in Arcana, Nature, Occultism, or ReligionIdentify a spell as a reaction as it's being castSeasoned1Trained in Alcohol Lore, Cooking |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/3/Table/1` | 0.641242 | Crafting Skill FeatsLevelPrerequisitesBenefitsQuick Install1Trained in CraftingInstall upgrades quicklyQuick Repair1Trained in CraftingRepair items quicklySerum Crafting1Trained in CraftingCraft serum |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/5/Table/3` | 0.605237 | Survival Skill FeatsLevelPrerequisitesBenefitsExperienced Tracker1Trained in SurvivalTrack at your full Speed at a –5 penaltySurvey Wildlife1Trained in SurvivalIdentify nearby creatures through signs |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/398` | 0.603159 | Lore Skill Feats |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/21/Text/10` | 0.592173 | You've studied in large medical wards, treating several  patients at once and tending to all their needs. When you  use Treat Disease or Treat Wounds, you can treat up to two  targets. If you're a mas |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/18` | 0.570989 | **Prerequisites** expert in Lore |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/406` | 0.566753 | Medicine Skill Feats |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/19` | 0.566315 | **Prerequisites** legendary in Medicine |

### Query 105
- Text: Lookup values for Society Skill FeatsLevelPrerequisitesBenefitsMultilingual1Trained in SocietyLearn two new languagesPlant Rumor1Trained in SocietyArgue by damaging reputationRead Lips1Trained in SocietyRead the lips of people you can seeSign Language1Trained in SocietyLearn sign languagesStreetwise1Trained in SocietyUse Society to Gather Information and Recall KnowledgeLegendary Codebreaker15Legendary in SocietyQuickly Decipher Writing using SocietyLegendary Linguist15Legendary in Society,
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/5/Table/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/5/Table/1', 'PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/531', 'PZO22001 Starfinder Player Core 210-231::/page/13/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/5/Table/1` | 0.969277 | Society Skill FeatsLevelPrerequisitesBenefitsMultilingual1Trained in SocietyLearn two new languagesPlant Rumor1Trained in SocietyArgue by damaging reputationRead Lips1Trained in SocietyRead the lips o |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/531` | 0.693952 | Quickly Decipher Writing using Society |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/10` | 0.667899 | Your skill with languages and codes is so great you can  decipher information with little more than a quick read  through a text. You can Decipher Writing using Society while  reading at normal speed. |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/14` | 0.610924 | **Prerequisites** legendary in Society, Multilingual |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/4/Table/1` | 0.598992 | Lore Skill FeatsLevelPrerequisitesBenefitsLegendary Professional15Legendary in LoreGain renown for your LoreMedicine Skill FeatsLevelPrerequisitesBenefitsBattle Medicine1Trained in MedicineHeal yourse |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/3/Table/1` | 0.597543 | Crafting Skill FeatsLevelPrerequisitesBenefitsQuick Install1Trained in CraftingInstall upgrades quicklyQuick Repair1Trained in CraftingRepair items quicklySerum Crafting1Trained in CraftingCraft serum |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/534` | 0.593727 | Legendary in Society, Multilingual |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/32` | 0.586550 | You easily pick up new languages. You learn two new  languages, chosen from common languages, uncommon  languages, and any others you have access to. You learn an  additional language if you are or be |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/504` | 0.582272 | Society Skill Feats |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/70` | 0.581415 | You can read lips of others nearby who you can clearly see.  The language read must be one that you know. When you're  at your leisure, you can do this automatically. In encounter  mode or when attemp |

### Query 106
- Text: Lookup values for Stealth Skill FeatsLevelPrerequisitesBenefitsExperienced Smuggler1Trained in StealthConceal items from observers more effectivelyTerrain Stalker1Trained in StealthSneak in certain terrain without attempting a checkQuiet Allies2Expert in StealthRoll a single Stealth check when sneaking with alliesFoil Senses7Master in StealthTake precautions against special sensesSwift Sneak7Master in StealthMove your full Speed while you SneakLegendary Sneak15Legendary in Stealth, Swift
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/5/Table/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/5/Table/2', 'PZO22001 Starfinder Player Core 210-231::/page/5/Table/1', 'PZO22001 Starfinder Player Core 210-231::/page/13/Text/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/5/Table/2` | 0.995059 | Stealth Skill FeatsLevelPrerequisitesBenefitsExperienced Smuggler1Trained in StealthConceal items from observers more effectivelyTerrain Stalker1Trained in StealthSneak in certain terrain without atte |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/5/Table/1` | 0.713616 | Society Skill FeatsLevelPrerequisitesBenefitsMultilingual1Trained in SocietyLearn two new languagesPlant Rumor1Trained in SocietyArgue by damaging reputationRead Lips1Trained in SocietyRead the lips o |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/41` | 0.711360 | **Prerequisites** legendary in Stealth, Swift Sneak |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/544` | 0.666724 | Stealth Skill Feats |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/5/Table/3` | 0.665331 | Survival Skill FeatsLevelPrerequisitesBenefitsExperienced Tracker1Trained in SurvivalTrack at your full Speed at a –5 penaltySurvey Wildlife1Trained in SurvivalIdentify nearby creatures through signs |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/536` | 0.654724 | Stealth Skill Feats |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/5/Table/4` | 0.652543 | Thievery Skill FeatsLevelPrerequisitesBenefitsPickpocket1Trained in ThieverySteal or Palm an Object more effectivelySubtle Theft1Trained in ThieveryYour thefts are harder to noticeWary Disarmament2Exp |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/570` | 0.633331 | Legendary in Stealth, Swift Sneak |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/2/Table/1` | 0.630912 | Varying Skill FeatsLevelPrerequisitesBenefitsRecognize Spell1Trained in Arcana, Nature, Occultism, or ReligionIdentify a spell as a reaction as it's being castSeasoned1Trained in Alcohol Lore, Cooking |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/3/Table/1` | 0.626844 | Crafting Skill FeatsLevelPrerequisitesBenefitsQuick Install1Trained in CraftingInstall upgrades quicklyQuick Repair1Trained in CraftingRepair items quicklySerum Crafting1Trained in CraftingCraft serum |

### Query 107
- Text: Lookup values for Survival Skill FeatsLevelPrerequisitesBenefitsExperienced Tracker1Trained in SurvivalTrack at your full Speed at a –5 penaltySurvey Wildlife1Trained in SurvivalIdentify nearby creatures through signs and cluesTerrain Expertise1Trained in Survival+1 to Survival checks in certain terrainUrban Survivalist1Trained in SurvivalUse Survival to navigate and forage for supplies in citiesMonster Crafting7Master in SurvivalCraft items using monster partsPlanar Survival7Master in SurvivalUse Survival to Subsist on different planesLegendary Survivalist15Legendary in SurvivalSurvive extreme conditions
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/5/Table/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/5/Table/3', 'PZO22001 Starfinder Player Core 210-231::/page/1/Table/9', 'PZO22001 Starfinder Player Core 210-231::/page/2/Table/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/5/Table/3` | 1.019610 | Survival Skill FeatsLevelPrerequisitesBenefitsExperienced Tracker1Trained in SurvivalTrack at your full Speed at a –5 penaltySurvey Wildlife1Trained in SurvivalIdentify nearby creatures through signs |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/Table/9` | 0.712572 | Non-Skill FeatsLevelPrerequisitesBenefitsAdopted Ancestry1—Gain access to ancestry feats from another ancestryArmor Proficiency1—Become trained in a type of armorAugmented Body1—Gain a free augmentati |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/2/Table/1` | 0.687121 | Varying Skill FeatsLevelPrerequisitesBenefitsRecognize Spell1Trained in Arcana, Nature, Occultism, or ReligionIdentify a spell as a reaction as it's being castSeasoned1Trained in Alcohol Lore, Cooking |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/4/Table/1` | 0.642874 | Lore Skill FeatsLevelPrerequisitesBenefitsLegendary Professional15Legendary in LoreGain renown for your LoreMedicine Skill FeatsLevelPrerequisitesBenefitsBattle Medicine1Trained in MedicineHeal yourse |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/5/Table/2` | 0.632545 | Stealth Skill FeatsLevelPrerequisitesBenefitsExperienced Smuggler1Trained in StealthConceal items from observers more effectivelyTerrain Stalker1Trained in StealthSneak in certain terrain without atte |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/572` | 0.631699 | Survival Skill Feats |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/3/Table/1` | 0.607419 | Crafting Skill FeatsLevelPrerequisitesBenefitsQuick Install1Trained in CraftingInstall upgrades quicklyQuick Repair1Trained in CraftingRepair items quicklySerum Crafting1Trained in CraftingCraft serum |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/5/Table/1` | 0.589581 | Society Skill FeatsLevelPrerequisitesBenefitsMultilingual1Trained in SocietyLearn two new languagesPlant Rumor1Trained in SocietyArgue by damaging reputationRead Lips1Trained in SocietyRead the lips o |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/15` | 0.588424 | You can spend 10 minutes assessing the area around you for  signs of creatures. Attempt a Survival check against a DC  determined by the GM based on how obvious the signs are.  On a success, you can a |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/16` | 0.588020 | Tracking is second nature to you, and when necessary you can  follow a trail without pause. You can Track while moving at full  Speed by taking a –5 penalty to your Survival check. If you're  a master |

### Query 108
- Text: Lookup values for Thievery Skill FeatsLevelPrerequisitesBenefitsPickpocket1Trained in ThieverySteal or Palm an Object more effectivelySubtle Theft1Trained in ThieveryYour thefts are harder to noticeWary Disarmament2Expert in Thievery+2 to AC or saves against devices or traps while disarmingQuick Unlock7Master in ThieveryPick a Lock with 1 actionLegendary Thief15Legendary in Thievery,
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/5/Table/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/5/Table/4', 'PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/604', 'PZO22001 Starfinder Player Core 210-231::/page/15/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/5/Table/4` | 1.001443 | Thievery Skill FeatsLevelPrerequisitesBenefitsPickpocket1Trained in ThieverySteal or Palm an Object more effectivelySubtle Theft1Trained in ThieveryYour thefts are harder to noticeWary Disarmament2Exp |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/604` | 0.741603 | Thievery Skill Feats |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/10` | 0.738373 | You can Steal or Palm an Object that's closely guarded,  such as in a pocket, without taking the –5 penalty. You can't  steal objects that would be extremely noticeable or time  consuming to remove (l |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/5/Table/2` | 0.675199 | Stealth Skill FeatsLevelPrerequisitesBenefitsExperienced Smuggler1Trained in StealthConceal items from observers more effectivelyTerrain Stalker1Trained in StealthSneak in certain terrain without atte |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/626` | 0.669966 | Legendary in Thievery, Pickpocket |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/9` | 0.661329 | **Prerequisites** trained in Thievery |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/51` | 0.659289 | **Prerequisites** legendary in Thievery, Pickpocket |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/21/Text/14` | 0.653523 | **Prerequisites** expert in Thievery |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/9` | 0.649329 | **Prerequisites** trained in Thievery |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/610` | 0.628535 | Trained in Thievery |

### Query 109
- Text: What are the requirements for **ADVANCED FIRST AID** **FEAT 7**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/5/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/5/SectionHeader/15', 'PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/430', 'PZO22001 Starfinder Player Core 210-231::/page/16/SectionHeader/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/5/SectionHeader/15` | 0.924996 | **ADVANCED FIRST AID** **FEAT 7** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/430` | 0.655783 | Advanced First Aid |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/16/SectionHeader/31` | 0.564011 | **QUICK RECOGNITION** **FEAT 7** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/9/SectionHeader/22` | 0.485095 | **EXPEDITIOUS SEARCH** **FEAT 7** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/26` | 0.479085 | **ASSURANCE FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/47` | 0.478581 | **SHAMELESS REQUEST** **FEAT 7** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/11` | 0.466249 | **PLANAR SURVIVAL** **FEAT 7** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/49` | 0.464364 | **PUSH IT** **FEAT 7** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/2` | 0.449294 | **QUICK CLIMB** **FEAT 7** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/11/SectionHeader/14` | 0.447577 | **FOOL THE CAMERA** **FEAT 7** |

### Query 110
- Text: What are the requirements for **Prerequisites** master in Medicine?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/5/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/5/Text/18', 'PZO22001 Starfinder Player Core 210-231::/page/20/Text/28', 'PZO22001 Starfinder Player Core 210-231::/page/21/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/18` | 0.925374 | **Prerequisites** master in Medicine |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/28` | 0.787722 | **Prerequisites** expert in Medicine |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/21/Text/9` | 0.787722 | **Prerequisites** expert in Medicine |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/11` | 0.745722 | **Prerequisites** expert in Medicine |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/21` | 0.745722 | **Prerequisites** expert in Medicine |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/61` | 0.736122 | **Prerequisites** trained in Medicine |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/432` | 0.657005 | Master in Medicine |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/19` | 0.644295 | **Prerequisites** legendary in Medicine |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/11/Text/17` | 0.596190 | **Prerequisites** master in Computers |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/35` | 0.588818 | **Prerequisites** master in Nature |

### Query 111
- Text: What are the requirements for **AKASHIC SYNC **[one-action] **FEAT 7**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/5/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/5/SectionHeader/20', 'PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/6', 'PZO22001 Starfinder Player Core 210-231::/page/6/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/5/SectionHeader/20` | 0.906925 | **AKASHIC SYNC **[one-action] **FEAT 7** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/6` | 0.565585 | **AKASHIC TRANSCENDENCE** **FEAT 15** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/9` | 0.541158 | **Prerequisites** legendary in Occultism, Akashic Sync |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/5/SectionHeader/15` | 0.463345 | **ADVANCED FIRST AID** **FEAT 7** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/9/SectionHeader/22` | 0.459653 | **EXPEDITIOUS SEARCH** **FEAT 7** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/47` | 0.459344 | **COMBAT HACK **[one-action] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/16/SectionHeader/31` | 0.457739 | **QUICK RECOGNITION** **FEAT 7** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/47` | 0.457206 | **SHAMELESS REQUEST** **FEAT 7** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/12/SectionHeader/53` | 0.449604 | **KIP UP **[free-action] **FEAT 7** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/37` | 0.447295 | **DEIFIC OBEDIENCE** **FEAT 7** |

### Query 112
- Text: What are the requirements for **Prerequisites** master in Occultism **Frequency** once per 10 minutes?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/5/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/5/Text/23', 'PZO22001 Starfinder Player Core 210-231::/page/7/Text/5', 'PZO22001 Starfinder Player Core 210-231::/page/14/Text/48']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/23` | 0.974714 | **Prerequisites** master in Occultism **Frequency** once per 10 minutes |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/5` | 0.829761 | **Prerequisites** master in Occultism |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/48` | 0.778983 | **Prerequisites** trained in Occultism |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/35` | 0.736983 | **Prerequisites** trained in Occultism |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/15` | 0.732295 | **Prerequisites** master in Occultism or Religion |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/468` | 0.684970 | Master in Occultism |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/464` | 0.684970 | Master in Occultism |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/460` | 0.624061 | Trained in Occultism |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/456` | 0.624061 | Trained in Occultism |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/443` | 0.599590 | Master in Occultism or Religion |

### Query 113
- Text: What are the requirements for **AKASHIC TRANSCENDENCE** **FEAT 15**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/6', 'PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/470', 'PZO22001 Starfinder Player Core 210-231::/page/13/SectionHeader/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/6` | 0.913262 | **AKASHIC TRANSCENDENCE** **FEAT 15** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/470` | 0.623863 | Akashic Transcendence U |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/13/SectionHeader/26` | 0.555215 | **LEGENDARY PERFORMER** **FEAT 15** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/5/SectionHeader/20` | 0.498297 | **AKASHIC SYNC **[one-action] **FEAT 7** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/9/Text/7` | 0.472609 | **DIVINE GUIDANCE FEAT 15** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/9` | 0.470490 | **Prerequisites** legendary in Occultism, Akashic Sync |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/13/SectionHeader/11` | 0.466843 | **LEGENDARY LINGUIST** **FEAT 15** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/13/SectionHeader/16` | 0.463404 | **LEGENDARY MEDIC** **FEAT 15** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/11/Text/6` | 0.459663 | **FLY ANYTHING** **FEAT 15** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/20/SectionHeader/10` | 0.459184 | **UNIFIED THEORY** **FEAT 15** |

### Query 114
- Text: What are the requirements for **Prerequisites** legendary in Occultism, Akashic Sync?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/6/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/6/Text/9', 'PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/472', 'PZO22001 Starfinder Player Core 210-231::/page/9/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/9` | 0.971832 | **Prerequisites** legendary in Occultism, Akashic Sync |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/472` | 0.818015 | Legendary in Occultism, Akashic Sync |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/9/Text/10` | 0.731854 | **Prerequisites** legendary in Religion |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/35` | 0.659622 | **Prerequisites** legendary in Lore |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/15` | 0.645611 | **Prerequisites** legendary in Crafting |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/19` | 0.632114 | **Prerequisites** legendary in Medicine |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/13` | 0.627180 | **Prerequisites** legendary in Arcana |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/46` | 0.623121 | **Prerequisites** legendary in Survival |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/9` | 0.608271 | **Prerequisites** legendary in Society |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/48` | 0.600362 | **Prerequisites** trained in Occultism |

### Query 115
- Text: What are the requirements for **ARCANE SENSE** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/6/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/6/Text/15', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/489', 'PZO22001 Starfinder Player Core 210-231::/page/6/Text/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/15` | 0.886377 | **ARCANE SENSE** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/489` | 0.649788 | Arcane Sense |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/19` | 0.596430 | **Prerequisites** trained in Arcana |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/481` | 0.532131 | Arcana Skill Feats |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/13` | 0.491159 | **Prerequisites** legendary in Arcana |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/11` | 0.487630 | **SKILL TRAINING** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/6` | 0.475657 | **SIGN LANGUAGE** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/21` | 0.469770 | **ARMOR PROFICIENCY FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/2/Table/1` | 0.461535 | Varying Skill FeatsLevelPrerequisitesBenefitsRecognize Spell1Trained in Arcana, Nature, Occultism, or ReligionIdentify a spell as a reaction as it's being castSeasoned1Trained in Alcohol Lore, Cooking |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/10/SectionHeader/44` | 0.458706 | **FEATHER STEP** **FEAT 1** |

### Query 116
- Text: What are the requirements for **Prerequisites** trained in Arcana?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/6/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/6/Text/19', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/491', 'PZO22001 Starfinder Player Core 210-231::/page/20/Text/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/19` | 0.954023 | **Prerequisites** trained in Arcana |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/491` | 0.811895 | Trained in Arcana |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/13` | 0.760180 | **Prerequisites** legendary in Arcana |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/34` | 0.595415 | **Prerequisites** master in Arcana, Nature, Occultism, or Religion;  Recognize Spell |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/495` | 0.572649 | Legendary in Arcana |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/481` | 0.569744 | Arcana Skill Feats |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/431` | 0.561294 | Trained in Arcana, Nature, Occultism, or Religion |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/496` | 0.561294 | Trained in Arcana, Nature, Occultism, or Religion |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/419` | 0.561294 | Trained in Arcana, Nature, Occultism, or Religion |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/14` | 0.555342 | You understand the common underpinnings of the four  traditions of magic and magical essences,. Whenever you use  a skill action or a skill feat that requires a Nature, Occultism,  or Religion check, |

### Query 117
- Text: What are the requirements for **Prerequisites** trained in at least one skill?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/6/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/6/Text/29', 'PZO22001 Starfinder Player Core 210-231::/page/14/Text/61', 'PZO22001 Starfinder Player Core 210-231::/page/15/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/29` | 0.874838 | **Prerequisites** trained in at least one skill |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/61` | 0.713236 | **Prerequisites** trained in Computers |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/4` | 0.713236 | **Prerequisites** trained in Computers |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/53` | 0.671236 | **Prerequisites** trained in Computers |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/9` | 0.671236 | **Prerequisites** trained in Computers |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/488` | 0.660236 | Trained in at least one skill |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/40` | 0.653264 | **Prerequisites** trained in Performance |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/31` | 0.653264 | **Prerequisites** trained in Performance |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/50` | 0.653264 | **Prerequisites** trained in Performance |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/19` | 0.653264 | **Prerequisites** trained in Performance |

### Query 118
- Text: What are the requirements for **AUGMENTED BODY** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/32', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/410', 'PZO22001 Starfinder Player Core 210-231::/page/18/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/32` | 0.871416 | **AUGMENTED BODY** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/410` | 0.647934 | Augmented Body |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/11` | 0.510637 | **SKILL TRAINING** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/14` | 0.459114 | **RIDE** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/26` | 0.452554 | **ASSURANCE FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/5/SectionHeader/10` | 0.442890 | **ADOPTED ANCESTRY FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/17` | 0.441944 | **BREATH CONTROL** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/10/SectionHeader/44` | 0.435734 | **FEATHER STEP** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/11/Text/3` | 0.431835 | **FLEET** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/35` | 0.431617 | You implant one augmentation with an item level equal to  your character level or lower. This augmentation doesn't  count against your total implant limit. The first time you take  this feat, the augm |

### Query 119
- Text: What are the requirements for **AUTOMATIC KNOWLEDGE** **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/38']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/38', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/437', 'PZO22001 Starfinder Player Core 210-231::/page/6/Text/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/38` | 0.901432 | **AUTOMATIC KNOWLEDGE** **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/437` | 0.618536 | Automatic Knowledge |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/43` | 0.569246 | **Special** You can select this feat multiple times, choosing a  different skill each time. You can use Automatic Knowledge  with any skills you have chosen, but you can still use  Automatic Knowledge |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/12/SectionHeader/41` | 0.524981 | **INVENTOR** **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/19/SectionHeader/26` | 0.510497 | **TECH CRAFTING** **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/9/SectionHeader/12` | 0.482932 | **DUBIOUS KNOWLEDGE** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/50` | 0.470557 | **Prerequisites** expert in Computers |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/21/SectionHeader/16` | 0.469647 | **WEAPON PROFICIENCY** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/11` | 0.461942 | **SKILL TRAINING** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/41` | 0.461081 | **Prerequisites** expert in a skill with the Recall Knowledge  action, Assurance in that skill |

### Query 120
- Text: What are the requirements for **Prerequisites** expert in a skill with the Recall Knowledge  action, Assurance in that skill?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/6/Text/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/6/Text/41', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/439', 'PZO22001 Starfinder Player Core 210-231::/page/9/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/41` | 0.985055 | **Prerequisites** expert in a skill with the Recall Knowledge  action, Assurance in that skill |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/439` | 0.872733 | Expert in Recall Knowledge, Assurance in the relevant skill action |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/9/Text/15` | 0.839121 | **Prerequisites** trained in a skill with the Recall Knowledge action |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/42` | 0.756311 | You know basic facts off the top of your head. Choose a skill  you're an expert in that has the Recall Knowledge action and  for which you have the Assurance feat. You can use the Recall  Knowledge ac |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/492` | 0.687531 | Trained in a skill with the Recall Knowledge action |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/Table/11` | 0.618650 | Varying Skill FeatsLevelPrerequisitesBenefitsAssurance1Trained in at least one skillReceive a fixed result on a skill checkDubious Knowledge1Trained in a skill with the Recall Knowledge actionLearn tr |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/21/Text/9` | 0.535919 | **Prerequisites** expert in Medicine |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/11` | 0.535919 | **Prerequisites** expert in Medicine |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/21` | 0.535919 | **Prerequisites** expert in Medicine |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/28` | 0.535919 | **Prerequisites** expert in Medicine |

### Query 121
- Text: What are the requirements for **BARGAIN HUNTER** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/44', 'PZO22001 Starfinder Player Core 210-231::/page/18/Text/11', 'PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/49']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/44` | 0.878155 | **BARGAIN HUNTER** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/11` | 0.517184 | **SKILL TRAINING** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/49` | 0.487338 | **BARRICADE **[one-action] **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/7` | 0.438691 | **BLEND IN** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/19/SectionHeader/59` | 0.433127 | **TRAIN ANIMAL** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/14` | 0.429476 | **RIDE** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/46` | 0.418612 | **Prerequisites** legendary in Survival |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/14/SectionHeader/58` | 0.413422 | **PHISHING EXPERTISE** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/29` | 0.409387 | **Prerequisites** trained in at least one skill |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/6` | 0.407491 | **SIGN LANGUAGE** **FEAT 1** |

### Query 122
- Text: What are the requirements for **Prerequisites** trained in Diplomacy?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/6/Text/47']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/6/Text/47', 'PZO22001 Starfinder Player Core 210-231::/page/12/Text/4', 'PZO22001 Starfinder Player Core 210-231::/page/14/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/47` | 0.932676 | **Prerequisites** trained in Diplomacy |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/42` | 0.932676 | **Prerequisites** trained in Diplomacy |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/4` | 0.932676 | **Prerequisites** trained in Diplomacy |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/11/Text/33` | 0.890676 | **Prerequisites** trained in Diplomacy |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/11/Text/22` | 0.780999 | **Prerequisites** expert in Diplomacy |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/20` | 0.780999 | **Prerequisites** expert in Diplomacy |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/50` | 0.755592 | **Requirements** master in Diplomacy |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/623` | 0.726617 | Trained in Diplomacy |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/631` | 0.726617 | Trained in Diplomacy |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/627` | 0.726617 | Trained in Diplomacy |

### Query 123
- Text: What are the requirements for **BARRICADE **[one-action] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/49']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/49', 'PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/58', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/414']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/49` | 0.909306 | **BARRICADE **[one-action] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/58` | 0.556812 | **BATTLE MEDICINE **[one-action] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/414` | 0.554479 | Barricade |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/14` | 0.507851 | **RIDE** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/22` | 0.485675 | **POWER SLIDE **[one-action]** TO **[three-actions] **FEAT 3** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/12/SectionHeader/36` | 0.481875 | **INTIMIDATING SHOT **[ONE-ACTION] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/11` | 0.477929 | **SKILL TRAINING** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/47` | 0.477677 | **COMBAT HACK **[one-action] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/17` | 0.471695 | **BREATH CONTROL** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/10/SectionHeader/28` | 0.461976 | **FASCINATING PERFORMANCE** **FEAT 1** |

### Query 124
- Text: What are the requirements for **BATTLE CRY** **FEAT 7**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/53']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/53', 'PZO22001 Starfinder Player Core 210-231::/page/7/Text/12', 'PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/47']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/53` | 0.899559 | **BATTLE CRY** **FEAT 7** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/12` | 0.602433 | **BREAK CURSE** **FEAT 7** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/47` | 0.559471 | **SHAMELESS REQUEST** **FEAT 7** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/16/SectionHeader/31` | 0.501286 | **QUICK RECOGNITION** **FEAT 7** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/14/SectionHeader/22` | 0.494484 | **MONSTER CRAFTING** **FEAT 7** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/49` | 0.494082 | **PUSH IT** **FEAT 7** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/5/SectionHeader/15` | 0.494050 | **ADVANCED FIRST AID** **FEAT 7** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/9/SectionHeader/22` | 0.477711 | **EXPEDITIOUS SEARCH** **FEAT 7** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/2` | 0.473966 | **QUICK CLIMB** **FEAT 7** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/2` | 0.472177 | **BIZARRE MAGIC** **FEAT 7** |

### Query 125
- Text: What are the requirements for **Prerequisites** master in Intimidation?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/6/Text/56']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/6/Text/56', 'PZO22001 Starfinder Player Core 210-231::/page/19/Text/48', 'PZO22001 Starfinder Player Core 210-231::/page/13/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/56` | 0.971270 | **Prerequisites** master in Intimidation |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/48` | 0.971270 | **Prerequisites** master in Intimidation |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/4` | 0.883528 | **Prerequisites** expert in Intimidation |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/39` | 0.837244 | **Prerequisites** trained in Intimidation |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/28` | 0.837244 | **Prerequisites** trained in Intimidation |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/11/Text/27` | 0.837244 | **Prerequisites** trained in Intimidation |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/10` | 0.837244 | **Prerequisites** trained in Intimidation |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/679` | 0.811800 | Master in Intimidation |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/663` | 0.732997 | Trained in Intimidation |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/655` | 0.732997 | Trained in Intimidation |

### Query 126
- Text: What are the requirements for **BATTLE MEDICINE **[one-action] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/58']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/58', 'PZO22001 Starfinder Player Core 210-231::/page/7/Text/47', 'PZO22001 Starfinder Player Core 210-231::/page/7/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/58` | 0.897665 | **BATTLE MEDICINE **[one-action] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/47` | 0.571095 | **COMBAT HACK **[one-action] **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/17` | 0.552477 | **BREATH CONTROL** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/49` | 0.503810 | **BARRICADE **[one-action] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/410` | 0.495566 | Battle Medicine |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/12/SectionHeader/36` | 0.481991 | **INTIMIDATING SHOT **[ONE-ACTION] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/53` | 0.479733 | **BATTLE CRY** **FEAT 7** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/20/SectionHeader/1` | 0.475731 | **TRICK MAGIC ITEM **[one-action] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/21/Text/9` | 0.472552 | **Prerequisites** expert in Medicine |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/21` | 0.472552 | **Prerequisites** expert in Medicine |

### Query 127
- Text: What are the requirements for **Prerequisites** trained in Medicine?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/6/Text/61']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/6/Text/61', 'PZO22001 Starfinder Player Core 210-231::/page/20/Text/28', 'PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/61` | 0.925383 | **Prerequisites** trained in Medicine |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/28` | 0.767904 | **Prerequisites** expert in Medicine |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/21` | 0.767904 | **Prerequisites** expert in Medicine |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/11` | 0.725904 | **Prerequisites** expert in Medicine |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/21/Text/9` | 0.725904 | **Prerequisites** expert in Medicine |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/18` | 0.709512 | **Prerequisites** master in Medicine |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/412` | 0.651139 | Trained in Medicine |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/38` | 0.640150 | **Prerequisites** trained in Religion |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/19` | 0.627084 | **Prerequisites** legendary in Medicine |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/61` | 0.613353 | **Prerequisites** trained in Computers |

### Query 128
- Text: What are the requirements for **BIZARRE MAGIC** **FEAT 7**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/2', 'PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/47', 'PZO22001 Starfinder Player Core 210-231::/page/14/SectionHeader/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/2` | 0.874885 | **BIZARRE MAGIC** **FEAT 7** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/47` | 0.620336 | **SHAMELESS REQUEST** **FEAT 7** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/14/SectionHeader/22` | 0.586147 | **MONSTER CRAFTING** **FEAT 7** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/9/SectionHeader/22` | 0.520465 | **EXPEDITIOUS SEARCH** **FEAT 7** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/12` | 0.510278 | **BREAK CURSE** **FEAT 7** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/14/SectionHeader/12` | 0.505889 | **MAGICAL CRAFTING** **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/49` | 0.504129 | **PUSH IT** **FEAT 7** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/53` | 0.501172 | **BATTLE CRY** **FEAT 7** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/12/SectionHeader/11` | 0.500150 | **IMPECCABLE CRAFTING** **FEAT 7** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/10` | 0.499199 | **RELIGIOUS TALISMAN** **FEAT 7** |

### Query 129
- Text: What are the requirements for **Prerequisites** master in Occultism?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/5', 'PZO22001 Starfinder Player Core 210-231::/page/7/Text/15', 'PZO22001 Starfinder Player Core 210-231::/page/17/Text/35']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/5` | 0.975065 | **Prerequisites** master in Occultism |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/15` | 0.922966 | **Prerequisites** master in Occultism or Religion |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/35` | 0.876369 | **Prerequisites** trained in Occultism |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/48` | 0.834369 | **Prerequisites** trained in Occultism |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/468` | 0.815879 | Master in Occultism |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/464` | 0.815879 | Master in Occultism |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/23` | 0.779828 | **Prerequisites** master in Occultism **Frequency** once per 10 minutes |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/443` | 0.735063 | Master in Occultism or Religion |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/456` | 0.721788 | Trained in Occultism |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/460` | 0.721788 | Trained in Occultism |

### Query 130
- Text: What are the requirements for **BLEND IN** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/7', 'PZO22001 Starfinder Player Core 210-231::/page/11/Text/3', 'PZO22001 Starfinder Player Core 210-231::/page/17/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/7` | 0.876011 | **BLEND IN** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/11/Text/3` | 0.604822 | **FLEET** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/14` | 0.590870 | **RIDE** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/11` | 0.538734 | **SKILL TRAINING** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/6` | 0.521677 | **SIGN LANGUAGE** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/14/SectionHeader/28` | 0.512067 | **MULTILINGUAL** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/554` | 0.494180 | Blend In |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/10/SectionHeader/44` | 0.491501 | **FEATHER STEP** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/11/SectionHeader/30` | 0.483770 | **GROUP IMPRESSION** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/17` | 0.472933 | **BREATH CONTROL** **FEAT 1** |

### Query 131
- Text: What are the requirements for **Prerequisites** trained in Society?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/10', 'PZO22001 Starfinder Player Core 210-231::/page/18/Text/33', 'PZO22001 Starfinder Player Core 210-231::/page/14/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/10` | 0.950716 | **Prerequisites** trained in Society |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/33` | 0.950716 | **Prerequisites** trained in Society |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/20` | 0.950716 | **Prerequisites** trained in Society |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/69` | 0.908716 | **Prerequisites** trained in Society |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/31` | 0.908716 | **Prerequisites** trained in Society |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/48` | 0.908716 | **Prerequisites** trained in Society |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/8` | 0.908716 | **Prerequisites** trained in Society |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/19` | 0.908716 | **Prerequisites** trained in Society |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/518` | 0.709660 | Trained in Society |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/5/TableCell/514` | 0.709660 | Trained in Society |

### Query 132
- Text: What are the requirements for **BREAK CURSE** **FEAT 7**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/12', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/441', 'PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/53']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/12` | 0.913757 | **BREAK CURSE** **FEAT 7** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/441` | 0.582110 | Break Curse |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/53` | 0.581865 | **BATTLE CRY** **FEAT 7** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/16/SectionHeader/31` | 0.520286 | **QUICK RECOGNITION** **FEAT 7** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/49` | 0.516756 | **PUSH IT** **FEAT 7** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/16/SectionHeader/51` | 0.510103 | **QUICK UNLOCK** **FEAT 7** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/2` | 0.490278 | **QUICK CLIMB** **FEAT 7** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/2` | 0.476338 | **BIZARRE MAGIC** **FEAT 7** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/47` | 0.474398 | **SHAMELESS REQUEST** **FEAT 7** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/11` | 0.471285 | **PLANAR SURVIVAL** **FEAT 7** |

### Query 133
- Text: What are the requirements for **Prerequisites** master in Occultism or Religion?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/15', 'PZO22001 Starfinder Player Core 210-231::/page/7/Text/5', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/443']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/15` | 0.982151 | **Prerequisites** master in Occultism or Religion |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/5` | 0.944460 | **Prerequisites** master in Occultism |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/443` | 0.878655 | Master in Occultism or Religion |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/35` | 0.816908 | **Prerequisites** trained in Occultism |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/48` | 0.816908 | **Prerequisites** trained in Occultism |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/468` | 0.790063 | Master in Occultism |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/464` | 0.790063 | Master in Occultism |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/23` | 0.749804 | **Prerequisites** master in Occultism **Frequency** once per 10 minutes |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/34` | 0.723362 | **Prerequisites** master in Arcana, Nature, Occultism, or Religion;  Recognize Spell |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/456` | 0.709238 | Trained in Occultism |

### Query 134
- Text: What are the requirements for **BREATH CONTROL** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/17', 'PZO22001 Starfinder Player Core 210-231::/page/8/Text/17', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/418']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/17` | 0.899824 | **BREATH CONTROL** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/17` | 0.599379 | **CROWD CONTROL** **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/418` | 0.552722 | Breath Control |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/11` | 0.509098 | **SKILL TRAINING** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/14` | 0.486955 | **RIDE** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/14/SectionHeader/17` | 0.478713 | **MANAGEMENT MATERIAL** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/11/Text/3` | 0.478420 | **FLEET** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/7` | 0.466196 | **BLEND IN** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/12` | 0.461416 | **BREAK CURSE** **FEAT 7** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/26` | 0.461010 | **STEADY BALANCE** **FEAT 1** |

### Query 135
- Text: What are the requirements for **CANNY ACUMEN** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/21', 'PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/422', 'PZO22001 Starfinder Player Core 210-231::/page/18/SectionHeader/35']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/21` | 0.859919 | **CANNY ACUMEN** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/422` | 0.577687 | Canny Acumen |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/18/SectionHeader/35` | 0.501998 | **STUDENT OF THE CANON** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/11` | 0.437916 | **SKILL TRAINING** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/5/SectionHeader/10` | 0.432024 | **ADOPTED ANCESTRY FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/26` | 0.423853 | **ASSURANCE FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/14` | 0.419074 | **RIDE** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/45` | 0.414500 | **DIGITAL AMBASSADOR** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/20` | 0.413491 | **SPECIALTY CRAFTING** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/11/Text/3` | 0.411100 | **FLEET** **FEAT 1** |

### Query 136
- Text: What are the requirements for **CAT FALL** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/25', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/453', 'PZO22001 Starfinder Player Core 210-231::/page/18/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/25` | 0.880512 | **CAT FALL** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/453` | 0.640076 | Cat Fall |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/11` | 0.584275 | **SKILL TRAINING** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/11/Text/3` | 0.512257 | **FLEET** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/6` | 0.485605 | **SIGN LANGUAGE** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/14` | 0.484617 | **RIDE** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/26` | 0.475639 | **ASSURANCE FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/21` | 0.475371 | **QUICK INSTALL** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/19/SectionHeader/59` | 0.473173 | **TRAIN ANIMAL** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/14/SectionHeader/28` | 0.461204 | **MULTILINGUAL** **FEAT 1** |

### Query 137
- Text: What are the requirements for **Prerequisites** trained in Acrobatics?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/28', 'PZO22001 Starfinder Player Core 210-231::/page/18/Text/29', 'PZO22001 Starfinder Player Core 210-231::/page/16/Text/44']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/28` | 0.941599 | **Prerequisites** trained in Acrobatics |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/29` | 0.941599 | **Prerequisites** trained in Acrobatics |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/44` | 0.941599 | **Prerequisites** trained in Acrobatics |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/29` | 0.899599 | **Prerequisites** trained in Acrobatics |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/9/Text/5` | 0.807312 | **Prerequisites** expert in Acrobatics |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/37` | 0.807312 | **Prerequisites** expert in Acrobatics |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/56` | 0.780226 | **Prerequisites** master in Acrobatics |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/463` | 0.742500 | Trained in Acrobatics |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/459` | 0.742500 | Trained in Acrobatics |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/455` | 0.742500 | Trained in Acrobatics |

### Query 138
- Text: What are the requirements for **CHARMING LIAR** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/31', 'PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/561', 'PZO22001 Starfinder Player Core 210-231::/page/14/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/31` | 0.874841 | **CHARMING LIAR** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/561` | 0.581491 | Charming Liar |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/7` | 0.501250 | **LIE TO ME** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/6` | 0.453288 | **SIGN LANGUAGE** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/11` | 0.448336 | **SKILL TRAINING** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/14` | 0.445908 | **RIDE** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/5/SectionHeader/5` | 0.434370 | **ADDITIONAL LORE FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/16/SectionHeader/66` | 0.426359 | **READ LIPS** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/35` | 0.421043 | Your charm allows you to win over those you lie to. When you  get a critical success using the Lie action, the target's attitude  toward you improves by one step, as though you'd succeeded  at using D |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/10/SectionHeader/44` | 0.416334 | **FEATHER STEP** **FEAT 1** |

### Query 139
- Text: What are the requirements for **Prerequisites** trained in Deception?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/34', 'PZO22001 Starfinder Player Core 210-231::/page/14/Text/10', 'PZO22001 Starfinder Player Core 210-231::/page/10/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/34` | 0.939915 | **Prerequisites** trained in Deception |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/42` | 0.939915 | **Prerequisites** trained in Deception |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/10` | 0.939915 | **Prerequisites** trained in Deception |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/25` | 0.897915 | **Prerequisites** trained in Deception |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/5` | 0.897915 | **Prerequisites** trained in Deception |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/6` | 0.814080 | **Prerequisites** expert in Deception |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/52` | 0.814080 | **Prerequisites** expert in Deception |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/15` | 0.814080 | **Prerequisites** expert in Deception |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/18` | 0.783207 | **Prerequisites** master in Deception |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/61` | 0.781271 | **Prerequisites **expert in Deception |

### Query 140
- Text: What are the requirements for **CLOUD JUMP** **FEAT 15**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/36']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/36', 'PZO22001 Starfinder Player Core 210-231::/page/16/Text/26', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/541']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/36` | 0.928688 | **CLOUD JUMP** **FEAT 15** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/26` | 0.584009 | **QUICK JUMP** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/541` | 0.560595 | Cloud Jump |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/11/Text/6` | 0.515913 | **FLY ANYTHING** **FEAT 15** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/21/Text/1` | 0.507551 | **WALL JUMP** **FEAT 7** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/13` | 0.485830 | **CRAFT ANYTHING** **FEAT 15** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/13/SectionHeader/26` | 0.459902 | **LEGENDARY PERFORMER** **FEAT 15** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/9/Text/7` | 0.423371 | **DIVINE GUIDANCE FEAT 15** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/13/SectionHeader/31` | 0.417119 | **LEGENDARY PROFESSIONAL** **FEAT 15** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/13/SectionHeader/6` | 0.416524 | **LEGENDARY CODEBREAKER** **FEAT 15** |

### Query 141
- Text: What are the requirements for **Prerequisites** legendary in Athletics?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/39', 'PZO22001 Starfinder Player Core 210-231::/page/13/Text/19', 'PZO22001 Starfinder Player Core 210-231::/page/16/Text/64']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/39` | 0.957338 | **Prerequisites** legendary in Athletics |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/19` | 0.753029 | **Prerequisites** legendary in Medicine |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/64` | 0.752823 | **Prerequisites** expert in Athletics |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/30` | 0.710823 | **Prerequisites** expert in Athletics |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/9/Text/10` | 0.708517 | **Prerequisites** legendary in Religion |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/46` | 0.685345 | **Prerequisites** legendary in Survival |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/543` | 0.680701 | Legendary in Athletics |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/34` | 0.668497 | **Prerequisites** trained in Athletics |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/53` | 0.668497 | **Prerequisites** trained in Athletics |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/29` | 0.668497 | **Prerequisites** trained in Athletics |

### Query 142
- Text: What are the requirements for **COMBAT CLIMBER** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/42']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/42', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/501', 'PZO22001 Starfinder Player Core 210-231::/page/16/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/42` | 0.880063 | **COMBAT CLIMBER** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/501` | 0.675603 | Combat Climber |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/2` | 0.545942 | **QUICK CLIMB** **FEAT 7** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/11` | 0.494301 | **SKILL TRAINING** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/504` | 0.480304 | Fight more effectively as you Climb |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/46` | 0.476274 | Your techniques allow you to fight as you climb. You're not  off-guard while Climbing and can Climb with a hand occupied.  You must still use another hand and both legs to Climb. |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/529` | 0.437547 | Quick Climb |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/47` | 0.431856 | **COMBAT HACK **[one-action] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/14` | 0.427085 | **RIDE** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/1/Table/9` | 0.426918 | Non-Skill FeatsLevelPrerequisitesBenefitsAdopted Ancestry1—Gain access to ancestry feats from another ancestryArmor Proficiency1—Become trained in a type of armorAugmented Body1—Gain a free augmentati |

### Query 143
- Text: What are the requirements for **Prerequisites** trained in Athletics?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/45']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/16/Text/29', 'PZO22001 Starfinder Player Core 210-231::/page/19/Text/53', 'PZO22001 Starfinder Player Core 210-231::/page/7/Text/45']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/29` | 0.930366 | **Prerequisites** trained in Athletics |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/53` | 0.930366 | **Prerequisites** trained in Athletics |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/45` | 0.930366 | **Prerequisites** trained in Athletics |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/34` | 0.888366 | **Prerequisites** trained in Athletics |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/11/Text/38` | 0.888366 | **Prerequisites** trained in Athletics |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/64` | 0.770184 | **Prerequisites** expert in Athletics |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/30` | 0.770184 | **Prerequisites** expert in Athletics |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/5` | 0.730661 | **Prerequisites** master in Athletics |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/21/Text/4` | 0.730661 | **Prerequisites** master in Athletics |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/49` | 0.730661 | **Prerequisites** master in Athletics |

### Query 144
- Text: What are the requirements for **COMBAT HACK **[one-action] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/47']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/47', 'PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/565', 'PZO22001 Starfinder Player Core 210-231::/page/15/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/47` | 0.893369 | **COMBAT HACK **[one-action] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/565` | 0.617007 | Combat Hack |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/6` | 0.603578 | **Special** If you have the Combat Hack or Digital Diversion  skill feat, you can use this feat to Combat Hack or Create a  Diversion without a hacking toolkit. |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/58` | 0.507012 | **BATTLE MEDICINE **[one-action] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/52` | 0.484541 | Attempt a Computers check to Hack an adjacent creature,  hazard, or item with the tech trait. The DC is equal to the  creature, item, or hazard's Fortitude DC, or the Fortitude  DC of the creature att |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/12/SectionHeader/36` | 0.467059 | **INTIMIDATING SHOT **[ONE-ACTION] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/54` | 0.465382 | **Requirements** You are holding or wearing a hacking toolkit and  have a free hand. |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/51` | 0.465382 | **Requirements** You are holding or wearing a hacking toolkit  and have a free hand. |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/14/SectionHeader/50` | 0.459243 | **PERCUSSIVE MAINTENANCE **[one-action] **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/9/Text/2` | 0.457789 | **DIVE FOR COVER **[ONE-ACTION] **FEAT 2** |

### Query 145
- Text: What are the requirements for **Prerequisites** expert in Computers?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/50']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/50', 'PZO22001 Starfinder Player Core 210-231::/page/12/Text/9', 'PZO22001 Starfinder Player Core 210-231::/page/8/Text/53']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/50` | 0.953612 | **Prerequisites** expert in Computers |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/9` | 0.795149 | **Prerequisites** trained in Computers |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/53` | 0.795149 | **Prerequisites** trained in Computers |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/4` | 0.753149 | **Prerequisites** trained in Computers |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/61` | 0.753149 | **Prerequisites** trained in Computers |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/11/Text/17` | 0.749319 | **Prerequisites** master in Computers |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/567` | 0.687458 | Expert in Computers |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/11` | 0.634520 | **Prerequisites** expert in Medicine |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/21` | 0.634520 | **Prerequisites** expert in Medicine |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/28` | 0.634520 | **Prerequisites** expert in Medicine |

### Query 146
- Text: What are the requirements for **COMMUNAL CRAFTING** **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/55']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/55', 'PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/529', 'PZO22001 Starfinder Player Core 210-231::/page/19/SectionHeader/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/55` | 0.902508 | **COMMUNAL CRAFTING** **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/529` | 0.724732 | Communal Crafting |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/19/SectionHeader/26` | 0.649786 | **TECH CRAFTING** **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/14/SectionHeader/12` | 0.591572 | **MAGICAL CRAFTING** **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/29` | 0.568177 | **Prerequisites** expert in Crafting |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/15` | 0.568177 | **Prerequisites** expert in Crafting |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/44` | 0.568177 | **Prerequisites** expert in Crafting |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/58` | 0.568177 | **Prerequisites** expert in Crafting |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/53` | 0.568177 | **Prerequisites** expert in Crafting |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/24` | 0.558271 | **Prerequisites** trained in Crafting |

### Query 147
- Text: What are the requirements for **Prerequisites** expert in Crafting?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/58']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/19/Text/29', 'PZO22001 Starfinder Player Core 210-231::/page/7/Text/58', 'PZO22001 Starfinder Player Core 210-231::/page/14/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/29` | 0.957044 | **Prerequisites** expert in Crafting |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/58` | 0.957044 | **Prerequisites** expert in Crafting |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/15` | 0.957044 | **Prerequisites** expert in Crafting |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/44` | 0.915044 | **Prerequisites** expert in Crafting |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/53` | 0.915044 | **Prerequisites** expert in Crafting |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/14` | 0.789304 | **Prerequisites** master in Crafting, Specialty Crafting |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/22` | 0.786995 | **Prerequisites** trained in Crafting |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/9/Text/20` | 0.786995 | **Prerequisites** trained in Crafting |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/45` | 0.786995 | **Prerequisites** trained in Crafting |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/24` | 0.786995 | **Prerequisites** trained in Crafting |

### Query 148
- Text: What are the requirements for **CONFABULATOR** **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/8/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/8/Text/4', 'PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/581', 'PZO22001 Starfinder Player Core 210-231::/page/12/SectionHeader/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/4` | 0.901162 | **CONFABULATOR** **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/581` | 0.623658 | Confabulator |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/12/SectionHeader/41` | 0.528727 | **INVENTOR** **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/19/SectionHeader/26` | 0.471916 | **TECH CRAFTING** **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/17` | 0.458789 | **CROWD CONTROL** **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/14/SectionHeader/34` | 0.430162 | **NIMBLE CRAWL** **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/10/SectionHeader/28` | 0.421494 | **FASCINATING PERFORMANCE** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/14/SectionHeader/12` | 0.408382 | **MAGICAL CRAFTING** **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/38` | 0.405788 | **AUTOMATIC KNOWLEDGE** **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/55` | 0.405702 | **COMMUNAL CRAFTING** **FEAT 2** |

### Query 149
- Text: What are the requirements for **Prerequisites** expert in Deception?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/8/Text/6']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/16/Text/15', 'PZO22001 Starfinder Player Core 210-231::/page/10/Text/52', 'PZO22001 Starfinder Player Core 210-231::/page/8/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/15` | 0.968956 | **Prerequisites** expert in Deception |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/52` | 0.968956 | **Prerequisites** expert in Deception |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/6` | 0.968956 | **Prerequisites** expert in Deception |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/61` | 0.895362 | **Prerequisites **expert in Deception |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/18` | 0.791315 | **Prerequisites** master in Deception |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/42` | 0.787135 | **Prerequisites** trained in Deception |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/25` | 0.787135 | **Prerequisites** trained in Deception |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/34` | 0.787135 | **Prerequisites** trained in Deception |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/5` | 0.787135 | **Prerequisites** trained in Deception |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/10` | 0.787135 | **Prerequisites** trained in Deception |

### Query 150
- Text: What are the requirements for **CONTINUAL RECOVERY** **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/8/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/8/SectionHeader/8', 'PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/18', 'PZO22001 Starfinder Player Core 210-231::/page/10/SectionHeader/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/8/SectionHeader/8` | 0.907693 | **CONTINUAL RECOVERY** **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/18` | 0.653082 | **ROBUST RECOVERY** **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/10/SectionHeader/34` | 0.603228 | **FAST RECOVERY** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/414` | 0.457326 | Continual Recovery |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/16/SectionHeader/36` | 0.453878 | **QUICK REPAIR** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/1/TableCell/430` | 0.430128 | Fast Recovery |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/17` | 0.418289 | **CROWD CONTROL** **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/418` | 0.417633 | Robust Recovery |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/4` | 0.410261 | **CONFABULATOR** **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/17` | 0.402976 | **BREATH CONTROL** **FEAT 1** |

### Query 151
- Text: What are the requirements for **Prerequisites** expert in Medicine?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/8/Text/11']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/20/Text/28', 'PZO22001 Starfinder Player Core 210-231::/page/8/Text/11', 'PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/28` | 0.954536 | **Prerequisites** expert in Medicine |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/11` | 0.954536 | **Prerequisites** expert in Medicine |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/17/SectionHeader/21` | 0.954536 | **Prerequisites** expert in Medicine |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/21/Text/9` | 0.912536 | **Prerequisites** expert in Medicine |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/61` | 0.724182 | **Prerequisites** trained in Medicine |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/5/Text/18` | 0.715641 | **Prerequisites** master in Medicine |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/19` | 0.664858 | **Prerequisites** legendary in Medicine |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/420` | 0.631245 | Expert in Medicine |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/424` | 0.631245 | Expert in Medicine |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/4/TableCell/428` | 0.631245 | Expert in Medicine |

### Query 152
- Text: What are the requirements for **CRAFT ANYTHING** **FEAT 15**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/8/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/8/Text/13', 'PZO22001 Starfinder Player Core 210-231::/page/11/Text/6', 'PZO22001 Starfinder Player Core 210-231::/page/14/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/13` | 0.904329 | **CRAFT ANYTHING** **FEAT 15** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/11/Text/6` | 0.732725 | **FLY ANYTHING** **FEAT 15** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/15` | 0.574207 | **Prerequisites** expert in Crafting |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/58` | 0.532207 | **Prerequisites** expert in Crafting |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/29` | 0.532207 | **Prerequisites** expert in Crafting |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/53` | 0.532207 | **Prerequisites** expert in Crafting |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/44` | 0.532207 | **Prerequisites** expert in Crafting |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/553` | 0.527466 | Craft Anything |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/556` | 0.513129 | Ignore most requirements for crafting items |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/9/Text/20` | 0.512976 | **Prerequisites** trained in Crafting |

### Query 153
- Text: What are the requirements for **Prerequisites** legendary in Crafting?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/8/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/8/Text/15', 'PZO22001 Starfinder Player Core 210-231::/page/13/Text/46', 'PZO22001 Starfinder Player Core 210-231::/page/13/Text/35']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/15` | 0.962916 | **Prerequisites** legendary in Crafting |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/46` | 0.782389 | **Prerequisites** legendary in Survival |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/35` | 0.772275 | **Prerequisites** legendary in Lore |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/9/Text/10` | 0.710963 | **Prerequisites** legendary in Religion |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/555` | 0.710661 | Legendary in Crafting |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/29` | 0.692027 | **Prerequisites** expert in Crafting |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/58` | 0.692027 | **Prerequisites** expert in Crafting |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/15` | 0.692027 | **Prerequisites** expert in Crafting |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/44` | 0.692027 | **Prerequisites** expert in Crafting |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/53` | 0.692027 | **Prerequisites** expert in Crafting |

### Query 154
- Text: What are the requirements for **CROWD CONTROL** **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/8/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/8/Text/17', 'PZO22001 Starfinder Player Core 210-231::/page/8/Text/26', 'PZO22001 Starfinder Player Core 210-231::/page/10/SectionHeader/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/17` | 0.919761 | **CROWD CONTROL** **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/26` | 0.634927 | **CROWD SURFING** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/10/SectionHeader/22` | 0.597567 | **FACE IN THE CROWD** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/17` | 0.543054 | **BREATH CONTROL** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/14/SectionHeader/34` | 0.541952 | **NIMBLE CRAWL** **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/19/SectionHeader/26` | 0.495994 | **TECH CRAFTING** **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/12/SectionHeader/41` | 0.481361 | **INVENTOR** **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/38` | 0.443813 | **AUTOMATIC KNOWLEDGE** **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/4` | 0.424933 | **CONFABULATOR** **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/14/SectionHeader/17` | 0.421531 | **MANAGEMENT MATERIAL** **FEAT 1** |

### Query 155
- Text: What are the requirements for **Prerequisites** expert in Diplomacy?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/8/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/8/Text/20', 'PZO22001 Starfinder Player Core 210-231::/page/11/Text/22', 'PZO22001 Starfinder Player Core 210-231::/page/6/Text/47']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/20` | 0.959466 | **Prerequisites** expert in Diplomacy |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/11/Text/22` | 0.959466 | **Prerequisites** expert in Diplomacy |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/6/Text/47` | 0.820765 | **Prerequisites** trained in Diplomacy |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/4` | 0.778765 | **Prerequisites** trained in Diplomacy |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/11/Text/33` | 0.778765 | **Prerequisites** trained in Diplomacy |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/42` | 0.778765 | **Prerequisites** trained in Diplomacy |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/17/Text/50` | 0.773121 | **Requirements** master in Diplomacy |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/635` | 0.721066 | Expert in Diplomacy |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/3/TableCell/639` | 0.721066 | Expert in Diplomacy |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/13/Text/24` | 0.714514 | **Prerequisites** legendary in Diplomacy |

### Query 156
- Text: What are the requirements for **CROWD SURFING** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/8/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/8/Text/26', 'PZO22001 Starfinder Player Core 210-231::/page/8/Text/17', 'PZO22001 Starfinder Player Core 210-231::/page/10/SectionHeader/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/26` | 0.891237 | **CROWD SURFING** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/17` | 0.660541 | **CROWD CONTROL** **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/10/SectionHeader/22` | 0.580831 | **FACE IN THE CROWD** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/457` | 0.513733 | Crowd Surfing |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/11` | 0.452223 | **SKILL TRAINING** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/14/SectionHeader/34` | 0.449475 | **NIMBLE CRAWL** **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/34` | 0.435237 | **Prerequisites** trained in Survival |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/10/Text/15` | 0.435237 | **Prerequisites** trained in Survival |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/20/Text/35` | 0.435237 | **Prerequisites** trained in Survival |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/19/Text/14` | 0.435237 | **Prerequisites** trained in Survival |

### Query 157
- Text: What are the requirements for **Prerequisites** trained in Acrobatics?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/8/Text/29']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/7/Text/28', 'PZO22001 Starfinder Player Core 210-231::/page/18/Text/29', 'PZO22001 Starfinder Player Core 210-231::/page/16/Text/44']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/28` | 0.941599 | **Prerequisites** trained in Acrobatics |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/29` | 0.941599 | **Prerequisites** trained in Acrobatics |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/16/Text/44` | 0.941599 | **Prerequisites** trained in Acrobatics |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/29` | 0.899599 | **Prerequisites** trained in Acrobatics |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/9/Text/5` | 0.807312 | **Prerequisites** expert in Acrobatics |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/37` | 0.807312 | **Prerequisites** expert in Acrobatics |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/56` | 0.780226 | **Prerequisites** master in Acrobatics |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/463` | 0.742500 | Trained in Acrobatics |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/459` | 0.742500 | Trained in Acrobatics |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/455` | 0.742500 | Trained in Acrobatics |

### Query 158
- Text: What are the requirements for **DEADLIFT **[one-action] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/8/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/8/Text/31', 'PZO22001 Starfinder Player Core 210-231::/page/15/Text/22', 'PZO22001 Starfinder Player Core 210-231::/page/12/SectionHeader/36']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/31` | 0.910768 | **DEADLIFT **[one-action] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/15/Text/22` | 0.524029 | **POWER SLIDE **[one-action]** TO **[three-actions] **FEAT 3** |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/12/SectionHeader/36` | 0.523080 | **INTIMIDATING SHOT **[ONE-ACTION] **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/11` | 0.470298 | **SKILL TRAINING** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/2/TableCell/505` | 0.465966 | Deadlift |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/9/Text/2` | 0.464280 | **DIVE FOR COVER **[ONE-ACTION] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/20/SectionHeader/1` | 0.462320 | **TRICK MAGIC ITEM **[one-action] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/6/SectionHeader/58` | 0.456360 | **BATTLE MEDICINE **[one-action] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/7/Text/47` | 0.455195 | **COMBAT HACK **[one-action] **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/8/Text/50` | 0.454166 | **DIGITAL DIVERSION** **FEAT 1** |

### Query 159
- Text: Lookup values for SpecialtyApplicable ItemsArmorsmithingArmor, shields and upgradesArtistryFine art, including jewelry and solarian
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/18/Table/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/18/Table/25', 'PZO22001 Starfinder Player Core 210-231::/page/18/TableCell/411', 'PZO22001 Starfinder Player Core 210-231::/page/18/TableCell/409']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/18/Table/25` | 0.832709 | SpecialtyApplicable ItemsArmorsmithingArmor, shields and upgradesArtistryFine art, including jewelry and solarian crystalsAutomotivesVehicles, including spaceshipsChemicalsAlcohol, ammunition, explosi |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/18/TableCell/411` | 0.604908 | Fine art, including jewelry and solarian crystals |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/18/TableCell/409` | 0.570695 | Armor, shields and upgrades |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/20/Table/42` | 0.502604 | SpecialtyExamplesActingDrama, live streams, reality showsComedyBuffoonery, joke telling, stand-up routinesDanceBallet, ballroom, interpretive, pop, traditionalKeyboardsKeytar, organ, pianoOratoryEpic, |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/24` | 0.499021 | example, if you were making an Abadarcorp travel suit and  had specialty in textiles, the GM might give you half your  bonus because the item requires both armorsmithing and  textiles to craft. |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/18/TableCell/408` | 0.491526 | Armorsmithing |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/18/Text/23` | 0.483469 | Your training focused on Crafting one particular kind of  item. Select one of the specialties listed below; you gain a +1  circumstance bonus to Crafting checks to Craft items of that  type. If you ar |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/15` | 0.474221 | You craft flawless creations with great efficiency. Whenever  you roll a success at a Crafting check to make an item of the  type you chose with Specialty Crafting, you get a critical  success instead |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/2/Table/1` | 0.473421 | Varying Skill FeatsLevelPrerequisitesBenefitsRecognize Spell1Trained in Arcana, Nature, Occultism, or ReligionIdentify a spell as a reaction as it's being castSeasoned1Trained in Alcohol Lore, Cooking |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/1/Table/9` | 0.471886 | Non-Skill FeatsLevelPrerequisitesBenefitsAdopted Ancestry1—Gain access to ancestry feats from another ancestryArmor Proficiency1—Become trained in a type of armorAugmented Body1—Gain a free augmentati |

### Query 160
- Text: Lookup values for SpecialtyExamplesActingDrama, live streams, reality showsComedyBuffoonery, joke telling, stand-up routinesDanceBallet, ballroom, interpretive, pop, traditionalKeyboardsKeytar, organ, pianoOratoryEpic, ode, poetry, storytellingPercussionBells, chimes, drum kit, xylophoneSingingBallad, chant, pop, rock, shantyStringsGuitar, singing coil, thereminSynthsSynth deck, turn tableWindsHorn, flute, pipes
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 210-231::/page/20/Table/42']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 210-231::/page/20/Table/42', 'PZO22001 Starfinder Player Core 210-231::/page/18/Table/25', 'PZO22001 Starfinder Player Core 210-231::/page/20/TableCell/421']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 210-231::/page/20/Table/42` | 0.985659 | SpecialtyExamplesActingDrama, live streams, reality showsComedyBuffoonery, joke telling, stand-up routinesDanceBallet, ballroom, interpretive, pop, traditionalKeyboardsKeytar, organ, pianoOratoryEpic, |
| 2 | `PZO22001 Starfinder Player Core 210-231::/page/18/Table/25` | 0.562716 | SpecialtyApplicable ItemsArmorsmithingArmor, shields and upgradesArtistryFine art, including jewelry and solarian crystalsAutomotivesVehicles, including spaceshipsChemicalsAlcohol, ammunition, explosi |
| 3 | `PZO22001 Starfinder Player Core 210-231::/page/20/TableCell/421` | 0.542087 | Ballet, ballroom, interpretive, pop, traditional |
| 4 | `PZO22001 Starfinder Player Core 210-231::/page/20/TableCell/429` | 0.486744 | Ballad, chant, pop, rock, shanty |
| 5 | `PZO22001 Starfinder Player Core 210-231::/page/4/Table/1` | 0.472977 | Lore Skill FeatsLevelPrerequisitesBenefitsLegendary Professional15Legendary in LoreGain renown for your LoreMedicine Skill FeatsLevelPrerequisitesBenefitsBattle Medicine1Trained in MedicineHeal yourse |
| 6 | `PZO22001 Starfinder Player Core 210-231::/page/12/Text/49` | 0.459829 | **AUDITORY** **EMOTION** **FORTUNE** **GENERAL** **LINGUISTIC** **MENTAL** **SKILL** |
| 7 | `PZO22001 Starfinder Player Core 210-231::/page/2/Table/1` | 0.453601 | Varying Skill FeatsLevelPrerequisitesBenefitsRecognize Spell1Trained in Arcana, Nature, Occultism, or ReligionIdentify a spell as a reaction as it's being castSeasoned1Trained in Alcohol Lore, Cooking |
| 8 | `PZO22001 Starfinder Player Core 210-231::/page/14/Text/41` | 0.443650 | **AUDITORY** **CONCENTRATE** **EMOTION** **GENERAL** **LINGUISTIC** **MENTAL** **SKILL** |
| 9 | `PZO22001 Starfinder Player Core 210-231::/page/5/Table/1` | 0.433939 | Society Skill FeatsLevelPrerequisitesBenefitsMultilingual1Trained in SocietyLearn two new languagesPlant Rumor1Trained in SocietyArgue by damaging reputationRead Lips1Trained in SocietyRead the lips o |
| 10 | `PZO22001 Starfinder Player Core 210-231::/page/20/TableCell/423` | 0.426898 | Keytar, organ, piano |
