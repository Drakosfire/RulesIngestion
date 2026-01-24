# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `1320`
- Query count: `108`
- Evaluated queries: `108`
- Coverage: `1.0000`
- MRR: `0.8219`
- hit@1: `0.7500`
- hit@3: `0.8796`
- hit@5: `0.9074`
- hit@10: `0.9907`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

### Expanded Gold Metrics
- Coverage: `1.0000`
- MRR: `0.8459`
- hit@1: `0.7778`
- hit@3: `0.9074`
- hit@5: `0.9352`
- hit@10: `0.9907`

### Expanded Gold Expansion Stats
- Queries with additions: `108`
- Avg added per query: `2.24`
- Max added: `11`
- Addition reasons:
  - graph_depth_1: `242`

### Expanded Gold Delta (Expanded - Strict)
- Coverage Δ: `0.0000`
- MRR Δ: `0.0240`
- hit@1 Δ: `0.0278`
- hit@3 Δ: `0.0278`
- hit@5 Δ: `0.0278`
- hit@10 Δ: `0.0000`

## Timings (ms)
- Embedding (chunks): `19655`
- Embedding (queries): `3382`
- Evaluation (strict): `101`
- Evaluation (expanded): `85`
- Total: `27561`

### Timing Estimates (ms)
- Evaluation (strict): `75`
- Evaluation (expanded): `75`
- Total: `23187`

## Query Details
### Query 0
- Text: What is the rule about CHAPTER 4: SKILLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 182-209::/page/10/SectionHeader/1', 'PZO22001 Starfinder Player Core 182-209::/page/3/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/1` | 0.853141 | CHAPTER 4: SKILLS |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/10/SectionHeader/1` | 0.665296 | SKILLS |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/3/Text/10` | 0.665296 | SKILLS |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/11/SectionHeader/37` | 0.562553 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/38` | 0.550553 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/29` | 0.550553 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/22` | 0.550553 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/15/Text/29` | 0.550553 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/5/Text/23` | 0.550553 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/43` | 0.550553 | **SKILLS** |

### Query 1
- Text: What is the rule about While your character's attributes represent their raw talent and potential, skills represent their  training and experience at performing certain tasks. Each skill is keyed to one of your character's  attributes and used for an array of related actions. Your character's expertise in a skill comes from  several sources, including their background and class. In this chapter, you'll learn about new skill  options in Starfinder, with new skills and updated uses for existing skills.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/2', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/9', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/2', 'PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/2` | 1.005800 | While your character's attributes represent their raw talent and potential, skills represent their  training and experience at performing certain tasks. Each skill is keyed to one of your character's |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/9` | 0.745442 | Each skill is tied to a key attribute. You add your modifier for  this attribute to checks and DCs when using that skill. For  example, skulking about the shadowy corridors of a derelict  starship wit |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/6` | 0.738735 | A character's acumen in skills can come from all sorts of  training, from piloting starships to researching a topic on  an infosphere to rehearsing a performing art. When you  create your character an |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/7` | 0.667448 | A character gains training in certain skills at 1st level:  typically two from their background, a small number of  predetermined skills from their class, and several skills of  your choice granted by |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/4` | 0.662061 | A brief description of the skill is followed by a list of actions  anyone can use, and then the actions you can perform only  if you are trained in that skill. Some actions list sample tasks  for each |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/2` | 0.640759 | The following entries describe the skills in the game. The heading for each entry provides the skill's  name, with that skill's key attribute in parentheses. |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/12` | 0.639401 | The actions you can perform with a given skill are sorted into  those you can use untrained and those that require you to be  trained in the skill, as shown on the Skills, Key Attributes, and  Actions |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/14` | 0.625671 | As your character advances in level, there are two  main ways their skills improve: skill increases and skill  feats. Your class lists the levels at which you gain each  of these improvements. |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/15` | 0.625582 | When you're actively using a skill, often by performing one  of its actions, you might attempt a skill check: rolling a d20  and adding your skill modifier. To determine this modifier,  add your attri |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/18` | 0.616549 | Skill feats are a type of general feat that often grant  you a new way to use a skill or make you better at  using a skill in a particular way. Skill feats always have  the skill trait. These feats ap |

### Query 2
- Text: What is the rule about A character's acumen in skills can come from all sorts of  training, from piloting starships to researching a topic on  an infosphere to rehearsing a performing art. When you  create your character and as they advance in level, you  have flexibility as to which skills they become better at  and when. Some classes benefit more from improving  certain skills—such as the envoy's focus on their leadership  skill—but for most classes, you can choose whichever  skills make the most sense for your character's theme  and backstory at 1st level, then use their adventure and  downtime experiences to inform how their skills should  improve as your character levels up.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/6', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/7', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/6', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/2', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/6` | 1.009137 | A character's acumen in skills can come from all sorts of  training, from piloting starships to researching a topic on  an infosphere to rehearsing a performing art. When you  create your character an |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/7` | 0.746968 | A character gains training in certain skills at 1st level:  typically two from their background, a small number of  predetermined skills from their class, and several skills of  your choice granted by |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/14` | 0.725676 | As your character advances in level, there are two  main ways their skills improve: skill increases and skill  feats. Your class lists the levels at which you gain each  of these improvements. |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/2` | 0.685763 | While your character's attributes represent their raw talent and potential, skills represent their  training and experience at performing certain tasks. Each skill is keyed to one of your character's |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/16` | 0.638425 | Skill increases improve your proficiency in skills of your  choice. You can use these increases to become trained  in new skills or increase your proficiency rank in skills  you're trained in (from tr |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/2` | 0.627227 | typically just your attribute modifier and proficiency bonus  at 1st level. At higher levels, you may wear or use items to  improve your skills with item bonuses pretty much all the  time; you should |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/4/Text/24` | 0.608555 | You can use a skill to earn money during downtime. You must be  trained in the skill to do so. This takes time to set up, and your  income depends on your proficiency rank and how lucrative a  task yo |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/4` | 0.599304 | A brief description of the skill is followed by a list of actions  anyone can use, and then the actions you can perform only  if you are trained in that skill. Some actions list sample tasks  for each |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/18/Text/24` | 0.594286 | Most backgrounds make you trained in a specific  subcategory of the Lore skill. The GM determines what  other subcategories they'll allow as Lore skills, though  these categories are always less broad |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/9` | 0.589348 | Each skill is tied to a key attribute. You add your modifier for  this attribute to checks and DCs when using that skill. For  example, skulking about the shadowy corridors of a derelict  starship wit |

### Query 3
- Text: What is the rule about A character gains training in certain skills at 1st level:  typically two from their background, a small number of  predetermined skills from their class, and several skills of  your choice granted by their class. This training increases  your proficiency ranks for those skills to trained instead  of untrained and lets you use more of the skills' actions.  Sometimes you might become trained in the same skill  from multiple sources, such as if your background granted  training in Athletics and you took the solarian class, which  also grants training in Athletics. Each time after the first  that you'd become trained in a given skill, you instead  allocate the trained proficiency to any other skill of your  choice—though if the skill is a Lore skill, the new skill must  also be a Lore skill.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/7', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/16', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/7', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/6', 'PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/7` | 1.011263 | A character gains training in certain skills at 1st level:  typically two from their background, a small number of  predetermined skills from their class, and several skills of  your choice granted by |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/16` | 0.747119 | Skill increases improve your proficiency in skills of your  choice. You can use these increases to become trained  in new skills or increase your proficiency rank in skills  you're trained in (from tr |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/6` | 0.702289 | A character's acumen in skills can come from all sorts of  training, from piloting starships to researching a topic on  an infosphere to rehearsing a performing art. When you  create your character an |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/18/Text/24` | 0.657178 | Most backgrounds make you trained in a specific  subcategory of the Lore skill. The GM determines what  other subcategories they'll allow as Lore skills, though  these categories are always less broad |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/13` | 0.654153 | Anyone can use a skill's untrained actions, but you can  use trained actions only if you have a proficiency rank of  trained or better in that skill. A circumstance, condition, or  effect might bar yo |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/18/Text/23` | 0.631399 | You have specialized information on a narrow topic. Lore  features many subcategories. You might have Corporate  Lore, Piracy Lore, Necrovite Lore, or any similar subcategory  of the skill. Each subca |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/2` | 0.621392 | While your character's attributes represent their raw talent and potential, skills represent their  training and experience at performing certain tasks. Each skill is keyed to one of your character's |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/14` | 0.614578 | As your character advances in level, there are two  main ways their skills improve: skill increases and skill  feats. Your class lists the levels at which you gain each  of these improvements. |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/2` | 0.610737 | typically just your attribute modifier and proficiency bonus  at 1st level. At higher levels, you may wear or use items to  improve your skills with item bonuses pretty much all the  time; you should |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/4` | 0.607219 | A brief description of the skill is followed by a list of actions  anyone can use, and then the actions you can perform only  if you are trained in that skill. Some actions list sample tasks  for each |

### Query 4
- Text: Summarize KEY ATTRIBUTE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/8', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/91', 'PZO22001 Starfinder Player Core 182-209::/page/3/SectionHeader/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/8', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/9', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/8` | 0.938889 | KEY ATTRIBUTE |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/91` | 0.684792 | Key Attribute |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/3/SectionHeader/1` | 0.567400 | **SKILLS, KEY ATTRIBUTES, AND ACTIONS ** |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/9` | 0.432269 | Each skill is tied to a key attribute. You add your modifier for  this attribute to checks and DCs when using that skill. For  example, skulking about the shadowy corridors of a derelict  starship wit |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/16` | 0.410637 | **Skill modifier = skill's key attribute modifier + ** **proficiency bonus + other bonuses + penalties** |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/17` | 0.348565 | **Skill Feats** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/2` | 0.347507 | The following entries describe the skills in the game. The heading for each entry provides the skill's  name, with that skill's key attribute in parentheses. |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/12` | 0.327304 | The actions you can perform with a given skill are sorted into  those you can use untrained and those that require you to be  trained in the skill, as shown on the Skills, Key Attributes, and  Actions |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/3/Table/2` | 0.323092 | SkillPageKey AttributeUntrained ActionsTrained ActionsAcrobatics192-193DexterityBalance ❖ Tumble Through ❖Maneuver in Flight ❖ SqueezeEArcana193IntelligenceRecall Knowledgec ❖ (page 190)Borrow an Arca |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/2` | 0.320192 | While your character's attributes represent their raw talent and potential, skills represent their  training and experience at performing certain tasks. Each skill is keyed to one of your character's |

### Query 5
- Text: What is the rule about Each skill is tied to a key attribute. You add your modifier for  this attribute to checks and DCs when using that skill. For  example, skulking about the shadowy corridors of a derelict  starship with Stealth uses your Dexterity modifier, navigating  the fickle personalities and treacherous power plays of  interstellar politics with Society uses your Intelligence  modifier, and so on. The key attribute for each skill is listed  on the Skills, Key Attributes, and Actions table on page 185  and also appears in parentheses following the skill's name  in the descriptions on the following pages. If the GM deems  it appropriate for a certain situation, however, they might?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/9', 'PZO22001 Starfinder Player Core 182-209::/page/10/Text/4', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/9', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/10', 'PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/9` | 0.985541 | Each skill is tied to a key attribute. You add your modifier for  this attribute to checks and DCs when using that skill. For  example, skulking about the shadowy corridors of a derelict  starship wit |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/4` | 0.719150 | A brief description of the skill is followed by a list of actions  anyone can use, and then the actions you can perform only  if you are trained in that skill. Some actions list sample tasks  for each |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/10` | 0.700174 | have you use a different attribute modifier for a skill check or  when determining your skill DC. |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/2` | 0.663963 | The following entries describe the skills in the game. The heading for each entry provides the skill's  name, with that skill's key attribute in parentheses. |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/15` | 0.657573 | When you're actively using a skill, often by performing one  of its actions, you might attempt a skill check: rolling a d20  and adding your skill modifier. To determine this modifier,  add your attri |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/8/Text/15` | 0.653371 | but related skill, usually against a higher DC than normal.  The GM might allow checks to Recall Knowledge using  other skills. For example, you might assess the skill of a star  athlete using Athleti |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/16` | 0.639030 | **Skill modifier = skill's key attribute modifier + ** **proficiency bonus + other bonuses + penalties** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/2` | 0.628589 | While your character's attributes represent their raw talent and potential, skills represent their  training and experience at performing certain tasks. Each skill is keyed to one of your character's |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/12` | 0.611023 | The actions you can perform with a given skill are sorted into  those you can use untrained and those that require you to be  trained in the skill, as shown on the Skills, Key Attributes, and  Actions |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/4/Text/2` | 0.603302 | General skill actions are skill actions that can be used with multiple different skills. When you use a  general skill action, you might use your modifier from any skill that lists it as one of the sk |

### Query 6
- Text: What is the rule about have you use a different attribute modifier for a skill check or  when determining your skill DC.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/10', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/5', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/10', 'PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/10` | 0.983373 | have you use a different attribute modifier for a skill check or  when determining your skill DC. |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/5` | 0.736437 | When someone or something tests your skill, they attempt  a check against your skill DC, which is equal to 10 plus your  skill modifier. A skill DC works like any other DC to determine  the effect of |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/15` | 0.727478 | When you're actively using a skill, often by performing one  of its actions, you might attempt a skill check: rolling a d20  and adding your skill modifier. To determine this modifier,  add your attri |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/9` | 0.660947 | Each skill is tied to a key attribute. You add your modifier for  this attribute to checks and DCs when using that skill. For  example, skulking about the shadowy corridors of a derelict  starship wit |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/16` | 0.625958 | **Skill modifier = skill's key attribute modifier + ** **proficiency bonus + other bonuses + penalties** |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/8/Text/15` | 0.622379 | but related skill, usually against a higher DC than normal.  The GM might allow checks to Recall Knowledge using  other skills. For example, you might assess the skill of a star  athlete using Athleti |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/2` | 0.591048 | typically just your attribute modifier and proficiency bonus  at 1st level. At higher levels, you may wear or use items to  improve your skills with item bonuses pretty much all the  time; you should |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/4/Text/2` | 0.532723 | General skill actions are skill actions that can be used with multiple different skills. When you use a  general skill action, you might use your modifier from any skill that lists it as one of the sk |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/8` | 0.531465 | Some armor imposes a penalty on specific skill checks and  DCs. If a creature is wearing armor that imparts a skill  penalty, that penalty is applied to the creature's Strengthand Dexterity-based skil |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/3` | 0.524032 | The GM sets the DC of a skill check, using the guidelines  in *Starfinder GM Core*. The DCs you're most likely  to encounter frequently are the five simple skill  DCs below, which are presented here t |

### Query 7
- Text: What is the rule about SKILL ACTIONS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 182-209::/page/4/SectionHeader/1', 'PZO22001 Starfinder Player Core 182-209::/page/3/Text/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/12', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/11` | 0.880040 | SKILL ACTIONS |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/4/SectionHeader/1` | 0.786425 | GENERAL SKILL  ACTIONS |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/3/Text/12` | 0.743816 | General Skill Actions |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/349` | 0.683077 | General Skill Action |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/11/Text/39` | 0.627175 | **General Skill ** **Actions** |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/7/Text/32` | 0.627175 | **General Skill ** **Actions** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/40` | 0.627175 | **General Skill ** **Actions** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/24` | 0.627175 | **General Skill ** **Actions** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/27/Text/41` | 0.627175 | **General Skill ** **Actions** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/5/Text/25` | 0.627175 | **General Skill ** **Actions** |

### Query 8
- Text: What is the rule about The actions you can perform with a given skill are sorted into  those you can use untrained and those that require you to be  trained in the skill, as shown on the Skills, Key Attributes, and  Actions table (page 185). The untrained and trained actions  of each skill appear in separate sections within the skill's  description.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/12', 'PZO22001 Starfinder Player Core 182-209::/page/10/Text/4', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/12', 'PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/12` | 0.971927 | The actions you can perform with a given skill are sorted into  those you can use untrained and those that require you to be  trained in the skill, as shown on the Skills, Key Attributes, and  Actions |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/4` | 0.731217 | A brief description of the skill is followed by a list of actions  anyone can use, and then the actions you can perform only  if you are trained in that skill. Some actions list sample tasks  for each |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/13` | 0.678923 | Anyone can use a skill's untrained actions, but you can  use trained actions only if you have a proficiency rank of  trained or better in that skill. A circumstance, condition, or  effect might bar yo |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/3/Footnote/5` | 0.624007 | G This is a general skill action, with a description appearing on the listed page number instead of in the skill's entry. |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/4/Text/2` | 0.596089 | General skill actions are skill actions that can be used with multiple different skills. When you use a  general skill action, you might use your modifier from any skill that lists it as one of the sk |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/7` | 0.587938 | A character gains training in certain skills at 1st level:  typically two from their background, a small number of  predetermined skills from their class, and several skills of  your choice granted by |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/9` | 0.583159 | Each skill is tied to a key attribute. You add your modifier for  this attribute to checks and DCs when using that skill. For  example, skulking about the shadowy corridors of a derelict  starship wit |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/2` | 0.582027 | The following entries describe the skills in the game. The heading for each entry provides the skill's  name, with that skill's key attribute in parentheses. |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/14/Text/18` | 0.560943 | You must be trained in Computers to use it for the following  general skill actions. |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/4/Table/6` | 0.560560 | General Skill ActionProficiencyPageDecipher WritingTrained186Earn IncomeTrained186–188Identify MagicTrained188Learn a SpellTrained189–190Recall Knowledge [one-action]Untrained190–191SubsistUntrained19 |

### Query 9
- Text: What is the rule about Anyone can use a skill's untrained actions, but you can  use trained actions only if you have a proficiency rank of  trained or better in that skill. A circumstance, condition, or  effect might bar you from a skill action regardless of your  proficiency rank, and sometimes using a skill in a specific  situation might require you to have a higher proficiency rank  than what is listed on the table. For instance, even though a  soldier untrained in Occultism could identify an extraplanar  or eldritch being with a lucky roll using Occultism to Recall  Knowledge, the GM might decide that Recalling Knowledge  to determine the spells used to summon and control such  a creature is beyond the scope of the soldier's anecdotal  knowledge. The GM decides whether a task requires a  particular proficiency rank.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/13', 'PZO22001 Starfinder Player Core 182-209::/page/10/Text/4', 'PZO22001 Starfinder Player Core 182-209::/page/7/Text/24']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/13', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/12', 'PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/13` | 1.019482 | Anyone can use a skill's untrained actions, but you can  use trained actions only if you have a proficiency rank of  trained or better in that skill. A circumstance, condition, or  effect might bar yo |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/4` | 0.723006 | A brief description of the skill is followed by a list of actions  anyone can use, and then the actions you can perform only  if you are trained in that skill. Some actions list sample tasks  for each |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/7/Text/24` | 0.711641 | Each magical tradition has a corresponding skill,  as shown on the table below. You must have the  trained proficiency rank in a skill to use it to Identify  Magic or Learn a Spell. Something without |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/12` | 0.679869 | The actions you can perform with a given skill are sorted into  those you can use untrained and those that require you to be  trained in the skill, as shown on the Skills, Key Attributes, and  Actions |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/16` | 0.655956 | Skill increases improve your proficiency in skills of your  choice. You can use these increases to become trained  in new skills or increase your proficiency rank in skills  you're trained in (from tr |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/7` | 0.648471 | A character gains training in certain skills at 1st level:  typically two from their background, a small number of  predetermined skills from their class, and several skills of  your choice granted by |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/21/Text/5` | 0.646842 | You must be trained in Occultism to use it for the following  general skill actions. |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/8/Text/15` | 0.642376 | but related skill, usually against a higher DC than normal.  The GM might allow checks to Recall Knowledge using  other skills. For example, you might assess the skill of a star  athlete using Athleti |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/10` | 0.625565 | Sometimes you won't know whether you have succeeded  at a skill check. If an action has the secret trait, the GM  rolls the check for you and informs you of the effect  without revealing the result of |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/18/Text/25` | 0.619581 | If you're making a check and multiple subcategories of  Lore could apply, or a non-Lore skill could apply, you can  use whichever skill you prefer. If there's any doubt whether  a Lore skill applies t |

### Query 10
- Text: What is the rule about SKILL CHECKS AND DCS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/5', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/13', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/14` | 0.917173 | SKILL CHECKS AND DCS |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/5` | 0.592359 | When someone or something tests your skill, they attempt  a check against your skill DC, which is equal to 10 plus your  skill modifier. A skill DC works like any other DC to determine  the effect of |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/10` | 0.584277 | have you use a different attribute modifier for a skill check or  when determining your skill DC. |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/8/Text/15` | 0.536620 | but related skill, usually against a higher DC than normal.  The GM might allow checks to Recall Knowledge using  other skills. For example, you might assess the skill of a star  athlete using Athleti |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/8` | 0.534869 | Some armor imposes a penalty on specific skill checks and  DCs. If a creature is wearing armor that imparts a skill  penalty, that penalty is applied to the creature's Strengthand Dexterity-based skil |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/3` | 0.534158 | The GM sets the DC of a skill check, using the guidelines  in *Starfinder GM Core*. The DCs you're most likely  to encounter frequently are the five simple skill  DCs below, which are presented here t |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/5` | 0.528942 | You attempt a skill check to try to remember a bit of  knowledge regarding a topic related to that skill. Suggest  which skill you'd like to use and ask the GM one question.  The GM determines the DC. |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/1` | 0.519060 | CHAPTER 4: SKILLS |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/9` | 0.513404 | Each skill is tied to a key attribute. You add your modifier for  this attribute to checks and DCs when using that skill. For  example, skulking about the shadowy corridors of a derelict  starship wit |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/10/SectionHeader/1` | 0.486660 | SKILLS |

### Query 11
- Text: What is the rule about When you're actively using a skill, often by performing one  of its actions, you might attempt a skill check: rolling a d20  and adding your skill modifier. To determine this modifier,  add your attribute modifier for the skill's key attribute, your  proficiency bonus for the skill, and any other bonuses and  penalties.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/15', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/16', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/15', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/16', 'PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/15` | 0.990763 | When you're actively using a skill, often by performing one  of its actions, you might attempt a skill check: rolling a d20  and adding your skill modifier. To determine this modifier,  add your attri |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/16` | 0.749627 | **Skill modifier = skill's key attribute modifier + ** **proficiency bonus + other bonuses + penalties** |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/2` | 0.735032 | typically just your attribute modifier and proficiency bonus  at 1st level. At higher levels, you may wear or use items to  improve your skills with item bonuses pretty much all the  time; you should |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/10` | 0.688803 | have you use a different attribute modifier for a skill check or  when determining your skill DC. |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/9` | 0.681696 | Each skill is tied to a key attribute. You add your modifier for  this attribute to checks and DCs when using that skill. For  example, skulking about the shadowy corridors of a derelict  starship wit |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/4` | 0.672946 | A brief description of the skill is followed by a list of actions  anyone can use, and then the actions you can perform only  if you are trained in that skill. Some actions list sample tasks  for each |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/5` | 0.630490 | When someone or something tests your skill, they attempt  a check against your skill DC, which is equal to 10 plus your  skill modifier. A skill DC works like any other DC to determine  the effect of |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/4/Text/2` | 0.597581 | General skill actions are skill actions that can be used with multiple different skills. When you use a  general skill action, you might use your modifier from any skill that lists it as one of the sk |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/6` | 0.596524 | See page 392 in Chapter 8: Playing the Game for more  information about modifiers, bonuses, and penalties. |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/8/Text/15` | 0.593074 | but related skill, usually against a higher DC than normal.  The GM might allow checks to Recall Knowledge using  other skills. For example, you might assess the skill of a star  athlete using Athleti |

### Query 12
- Text: What is the rule about **Skill modifier = skill's key attribute modifier + ** **proficiency bonus + other bonuses + penalties**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/16', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/15', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/16', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/17', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/16` | 0.956782 | **Skill modifier = skill's key attribute modifier + ** **proficiency bonus + other bonuses + penalties** |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/15` | 0.737278 | When you're actively using a skill, often by performing one  of its actions, you might attempt a skill check: rolling a d20  and adding your skill modifier. To determine this modifier,  add your attri |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/2` | 0.701186 | typically just your attribute modifier and proficiency bonus  at 1st level. At higher levels, you may wear or use items to  improve your skills with item bonuses pretty much all the  time; you should |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/9` | 0.656725 | Each skill is tied to a key attribute. You add your modifier for  this attribute to checks and DCs when using that skill. For  example, skulking about the shadowy corridors of a derelict  starship wit |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/6` | 0.641395 | See page 392 in Chapter 8: Playing the Game for more  information about modifiers, bonuses, and penalties. |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/10` | 0.630427 | have you use a different attribute modifier for a skill check or  when determining your skill DC. |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/16` | 0.565846 | Skill increases improve your proficiency in skills of your  choice. You can use these increases to become trained  in new skills or increase your proficiency rank in skills  you're trained in (from tr |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/4/Text/2` | 0.561370 | General skill actions are skill actions that can be used with multiple different skills. When you use a  general skill action, you might use your modifier from any skill that lists it as one of the sk |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/8/Text/15` | 0.548402 | but related skill, usually against a higher DC than normal.  The GM might allow checks to Recall Knowledge using  other skills. For example, you might assess the skill of a star  athlete using Athleti |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/4` | 0.528733 | A brief description of the skill is followed by a list of actions  anyone can use, and then the actions you can perform only  if you are trained in that skill. Some actions list sample tasks  for each |

### Query 13
- Text: What is the rule about When noting the modifier on your character sheet, you  should write down only the numbers that always apply—?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/17', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/6', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/17', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/16', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/17` | 0.992015 | When noting the modifier on your character sheet, you  should write down only the numbers that always apply— |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/6` | 0.567744 | See page 392 in Chapter 8: Playing the Game for more  information about modifiers, bonuses, and penalties. |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/10` | 0.556803 | have you use a different attribute modifier for a skill check or  when determining your skill DC. |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/9` | 0.504589 | Each skill is tied to a key attribute. You add your modifier for  this attribute to checks and DCs when using that skill. For  example, skulking about the shadowy corridors of a derelict  starship wit |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/15` | 0.490303 | When you're actively using a skill, often by performing one  of its actions, you might attempt a skill check: rolling a d20  and adding your skill modifier. To determine this modifier,  add your attri |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/16` | 0.454714 | **Skill modifier = skill's key attribute modifier + ** **proficiency bonus + other bonuses + penalties** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/2` | 0.454631 | typically just your attribute modifier and proficiency bonus  at 1st level. At higher levels, you may wear or use items to  improve your skills with item bonuses pretty much all the  time; you should |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/21/Text/14` | 0.414103 | Some performances require you to be more than just  charismatic, and if you don't meet the demands of the  art form or the audience, the GM might apply a penalty  based on the relevant attribute. For |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/8/Text/24` | 0.400317 | If you have a spell repertoire, such as the mystic or  witchwarper do, a spell you learn isn't automatically added  since you can only know a limited number of spells. Instead,  you can select it when |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/5` | 0.395237 | When someone or something tests your skill, they attempt  a check against your skill DC, which is equal to 10 plus your  skill modifier. A skill DC works like any other DC to determine  the effect of |

### Query 14
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/19', 'PZO22001 Starfinder Player Core 182-209::/page/19/Text/59', 'PZO22001 Starfinder Player Core 182-209::/page/17/Text/40']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/19', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/20', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/19` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/19/Text/59` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/40` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/27/Text/36` | 0.838541 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/7/Text/27` | 0.838541 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/35` | 0.838541 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/11/Text/34` | 0.838541 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/13/Text/41` | 0.838541 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/15/Text/26` | 0.838541 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/26` | 0.838541 | **INTRODUCTION** |

### Query 15
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/20']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/15/Text/27', 'PZO22001 Starfinder Player Core 182-209::/page/17/Text/41', 'PZO22001 Starfinder Player Core 182-209::/page/13/Text/42']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/20', 'PZO22001 Starfinder Player Core 182-209::/page/19/Text/60', 'PZO22001 Starfinder Player Core 182-209::/page/25/Text/27', 'PZO22001 Starfinder Player Core 182-209::/page/17/Text/41', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/19', 'PZO22001 Starfinder Player Core 182-209::/page/27/Text/37', 'PZO22001 Starfinder Player Core 182-209::/page/13/Text/42', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/21', 'PZO22001 Starfinder Player Core 182-209::/page/15/Text/27', 'PZO22001 Starfinder Player Core 182-209::/page/7/Text/28', 'PZO22001 Starfinder Player Core 182-209::/page/9/Text/36', 'PZO22001 Starfinder Player Core 182-209::/page/11/Text/35']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/19/Text/60` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/25/Text/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/17/Text/41` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/27/Text/37` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/13/Text/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/15/Text/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/7/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/9/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/11/Text/35` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/15/Text/27` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/13/Text/42` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/41` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/27` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/7/Text/28` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/19/Text/60` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/20` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/27/Text/37` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/36` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/11/Text/35` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 16
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/21']
- Expected found: `True`
- Expected rank: `10`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/7/Text/29', 'PZO22001 Starfinder Player Core 182-209::/page/9/Text/37', 'PZO22001 Starfinder Player Core 182-209::/page/27/Text/38']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/21', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/22', 'PZO22001 Starfinder Player Core 182-209::/page/17/Text/42', 'PZO22001 Starfinder Player Core 182-209::/page/25/Text/28', 'PZO22001 Starfinder Player Core 182-209::/page/7/Text/29', 'PZO22001 Starfinder Player Core 182-209::/page/19/Text/61', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/20', 'PZO22001 Starfinder Player Core 182-209::/page/15/Text/28', 'PZO22001 Starfinder Player Core 182-209::/page/5/Text/22', 'PZO22001 Starfinder Player Core 182-209::/page/11/Text/36', 'PZO22001 Starfinder Player Core 182-209::/page/9/Text/37', 'PZO22001 Starfinder Player Core 182-209::/page/13/Text/43']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/17/Text/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/25/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/7/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/19/Text/61` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/15/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/5/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/11/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/9/Text/37` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/13/Text/43` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/7/Text/29` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/27/Text/38` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/37` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/11/Text/36` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/15/Text/28` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/19/Text/61` | 0.910061 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/42` | 0.910061 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/28` | 0.910061 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/13/Text/43` | 0.910061 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/21` | 0.910061 | **CLASSES** |

### Query 17
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/22']
- Expected found: `True`
- Expected rank: `9`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/9/Text/38', 'PZO22001 Starfinder Player Core 182-209::/page/25/Text/29', 'PZO22001 Starfinder Player Core 182-209::/page/13/Text/44']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/22', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/23', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `9`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/38` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/29` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/13/Text/44` | 0.864442 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/11/SectionHeader/37` | 0.822442 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/27/Text/39` | 0.822442 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/7/Text/30` | 0.822442 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/19/Text/62` | 0.822442 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/15/Text/29` | 0.822442 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/22` | 0.822442 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/43` | 0.822442 | **SKILLS** |

### Query 18
- Text: What is the rule about **Skills Table**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/23']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/27/Text/40', 'PZO22001 Starfinder Player Core 182-209::/page/15/Text/30', 'PZO22001 Starfinder Player Core 182-209::/page/19/Text/63']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/23', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/22', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/24']
- Expanded expected found: `True`
- Expanded expected rank: `8`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/27/Text/40` | 0.873821 | **Skills Table** |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/15/Text/30` | 0.873821 | **Skills Table** |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/19/Text/63` | 0.873821 | **Skills Table** |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/44` | 0.831821 | **Skills Table** |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/11/Text/38` | 0.831821 | **Skills Table** |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/7/Text/31` | 0.831821 | **Skills Table** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/30` | 0.831821 | **Skills Table** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/23` | 0.831821 | **Skills Table** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/39` | 0.831821 | **Skills Table** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/13/Text/45` | 0.831821 | **Skills Table** |

### Query 19
- Text: What is the rule about **General Skill ** **Actions**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/24']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/9/Text/40', 'PZO22001 Starfinder Player Core 182-209::/page/5/Text/25', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/24']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/24', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/23', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/25']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/40` | 0.885852 | **General Skill ** **Actions** |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/5/Text/25` | 0.885852 | **General Skill ** **Actions** |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/24` | 0.885852 | **General Skill ** **Actions** |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/15/Text/31` | 0.843852 | **General Skill ** **Actions** |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/31` | 0.843852 | **General Skill ** **Actions** |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/45` | 0.843852 | **General Skill ** **Actions** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/27/Text/41` | 0.843852 | **General Skill ** **Actions** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/19/Text/64` | 0.843852 | **General Skill ** **Actions** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/13/Text/46` | 0.843852 | **General Skill ** **Actions** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/11/Text/39` | 0.843851 | **General Skill ** **Actions** |

### Query 20
- Text: What is the rule about **Skills**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/25']
- Expected found: `True`
- Expected rank: `14`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/9/Text/38', 'PZO22001 Starfinder Player Core 182-209::/page/25/Text/29', 'PZO22001 Starfinder Player Core 182-209::/page/19/Text/62']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/25', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/24', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `14`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/38` | 0.749788 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/29` | 0.749788 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/19/Text/62` | 0.749788 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/5/Text/23` | 0.707788 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/22` | 0.707788 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/43` | 0.707788 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/15/Text/29` | 0.707788 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/7/Text/30` | 0.707788 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/13/Text/44` | 0.707788 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/11/SectionHeader/37` | 0.707788 | **SKILLS** |

### Query 21
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/26']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/9/Text/42', 'PZO22001 Starfinder Player Core 182-209::/page/7/Text/34', 'PZO22001 Starfinder Player Core 182-209::/page/5/Text/27']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/26', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/27', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/25']
- Expanded expected found: `True`
- Expanded expected rank: `7`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/42` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/7/Text/34` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/5/Text/27` | 0.871817 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/13/Text/48` | 0.829817 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/47` | 0.829817 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/19/Text/66` | 0.829817 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/26` | 0.829817 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/11/Text/41` | 0.702296 | **FEATS** **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/33` | 0.702296 | **FEATS** **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/27/Text/43` | 0.702296 | **FEATS** **EQUIPMENT** |

### Query 22
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/27']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/19/Text/67', 'PZO22001 Starfinder Player Core 182-209::/page/17/Text/48', 'PZO22001 Starfinder Player Core 182-209::/page/5/Text/28']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/27', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/28', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/19/Text/67` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/48` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/5/Text/28` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/7/Text/35` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/43` | 0.902726 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/27` | 0.902726 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/3/Text/15` | 0.824254 | EQUIPMENT |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/11/Text/41` | 0.627947 | **FEATS** **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/27/Text/43` | 0.627947 | **FEATS** **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/33` | 0.627947 | **FEATS** **EQUIPMENT** |

### Query 23
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/28', 'PZO22001 Starfinder Player Core 182-209::/page/11/Text/42', 'PZO22001 Starfinder Player Core 182-209::/page/25/Text/34']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/28', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/29', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/28` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/11/Text/42` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/34` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/15/Text/34` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/44` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/27/Text/44` | 0.847304 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/49` | 0.847304 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/7/Text/36` | 0.847304 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/5/Text/29` | 0.847304 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/19/Text/68` | 0.847303 | **SPELLS** |

### Query 24
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `9`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/27/Text/45', 'PZO22001 Starfinder Player Core 182-209::/page/15/Text/35', 'PZO22001 Starfinder Player Core 182-209::/page/17/Text/50']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/29', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/28', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `9`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/27/Text/45` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/15/Text/35` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/50` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/45` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/11/Text/43` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/19/Text/69` | 0.923000 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/5/Text/30` | 0.923000 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/35` | 0.923000 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/29` | 0.923000 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/7/Text/37` | 0.923000 | **PLAYING THE ** **GAME** |

### Query 25
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/30']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/11/Text/44', 'PZO22001 Starfinder Player Core 182-209::/page/13/Text/52', 'PZO22001 Starfinder Player Core 182-209::/page/27/Text/46']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/30', 'PZO22001 Starfinder Player Core 182-209::/page/7/Text/38', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/29', 'PZO22001 Starfinder Player Core 182-209::/page/5/Text/31', 'PZO22001 Starfinder Player Core 182-209::/page/9/Text/46', 'PZO22001 Starfinder Player Core 182-209::/page/11/Text/44', 'PZO22001 Starfinder Player Core 182-209::/page/15/Text/36', 'PZO22001 Starfinder Player Core 182-209::/page/19/Text/70', 'PZO22001 Starfinder Player Core 182-209::/page/17/Text/51', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/31', 'PZO22001 Starfinder Player Core 182-209::/page/27/Text/46', 'PZO22001 Starfinder Player Core 182-209::/page/13/Text/52']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/7/Text/38` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/5/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/9/Text/46` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/11/Text/44` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/15/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/19/Text/70` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/17/Text/51` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/27/Text/46` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/13/Text/52` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/11/Text/44` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/13/Text/52` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/27/Text/46` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/15/Text/36` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/36` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/30` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/7/Text/38` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/5/Text/31` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/19/Text/70` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/51` | 0.953498 | **CONDITIONS ** **APPENDIX** |

### Query 26
- Text: Summarize **GLOSSARY & **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/31', 'PZO22001 Starfinder Player Core 182-209::/page/9/Text/47', 'PZO22001 Starfinder Player Core 182-209::/page/7/Text/39']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/31', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/34', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/31` | 0.986628 | **GLOSSARY & ** |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/47` | 0.986628 | **GLOSSARY & ** |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/7/Text/39` | 0.872894 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/5/Text/32` | 0.830894 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/52` | 0.830894 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/13/Text/53` | 0.830894 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/37` | 0.830894 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/19/Text/71` | 0.830894 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/15/Text/37` | 0.830894 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/27/Text/47` | 0.830894 | **GLOSSARY & ** **INDEX** |

### Query 27
- Text: Summarize **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/34', 'PZO22001 Starfinder Player Core 182-209::/page/19/Text/71', 'PZO22001 Starfinder Player Core 182-209::/page/17/Text/52']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/1/Text/34', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/2', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/31']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/34` | 0.897726 | **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/19/Text/71` | 0.648125 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/52` | 0.648125 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/13/Text/53` | 0.606125 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/15/Text/37` | 0.606125 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/7/Text/39` | 0.606125 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/37` | 0.606125 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/5/Text/32` | 0.606125 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/27/Text/47` | 0.606125 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/3/Text/20` | 0.527899 | GLOSSARY & INDEX |

### Query 28
- Text: What is the rule about typically just your attribute modifier and proficiency bonus  at 1st level. At higher levels, you may wear or use items to  improve your skills with item bonuses pretty much all the  time; you should include those in your calculation, too.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/2', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/15', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/2', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/3', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/34']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/1/Text/34` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/2` | 0.991317 | typically just your attribute modifier and proficiency bonus  at 1st level. At higher levels, you may wear or use items to  improve your skills with item bonuses pretty much all the  time; you should |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/15` | 0.705538 | When you're actively using a skill, often by performing one  of its actions, you might attempt a skill check: rolling a d20  and adding your skill modifier. To determine this modifier,  add your attri |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/16` | 0.690976 | **Skill modifier = skill's key attribute modifier + ** **proficiency bonus + other bonuses + penalties** |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/10` | 0.611597 | have you use a different attribute modifier for a skill check or  when determining your skill DC. |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/16` | 0.611072 | Skill increases improve your proficiency in skills of your  choice. You can use these increases to become trained  in new skills or increase your proficiency rank in skills  you're trained in (from tr |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/14` | 0.593872 | As your character advances in level, there are two  main ways their skills improve: skill increases and skill  feats. Your class lists the levels at which you gain each  of these improvements. |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/7` | 0.586707 | A character gains training in certain skills at 1st level:  typically two from their background, a small number of  predetermined skills from their class, and several skills of  your choice granted by |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/6` | 0.586177 | See page 392 in Chapter 8: Playing the Game for more  information about modifiers, bonuses, and penalties. |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/9` | 0.564749 | Each skill is tied to a key attribute. You add your modifier for  this attribute to checks and DCs when using that skill. For  example, skulking about the shadowy corridors of a derelict  starship wit |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/6` | 0.549777 | A character's acumen in skills can come from all sorts of  training, from piloting starships to researching a topic on  an infosphere to rehearsing a performing art. When you  create your character an |

### Query 29
- Text: What is the rule about The GM sets the DC of a skill check, using the guidelines  in *Starfinder GM Core*. The DCs you're most likely  to encounter frequently are the five simple skill  DCs below, which are presented here to give you  a sense of what number you'll need to roll to  succeed at most tasks.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/3', 'PZO22001 Starfinder Player Core 182-209::/page/7/ListItem/12', 'PZO22001 Starfinder Player Core 182-209::/page/4/Text/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/3', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/2', 'PZO22001 Starfinder Player Core 182-209::/page/2/Table/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/Table/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/3` | 1.017003 | The GM sets the DC of a skill check, using the guidelines  in *Starfinder GM Core*. The DCs you're most likely  to encounter frequently are the five simple skill  DCs below, which are presented here t |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/7/ListItem/12` | 0.809203 | Attempt a skill check for the skill corresponding to your  tradition (DC determined by the GM, often close to the  DC on the Learning a Spell Table). Uncommon or rare  spells have higher DCs; full gui |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/4/Text/17` | 0.675417 | The DC is determined by the GM based on the state or  complexity of the document. The GM might have you roll one  check for a short text or a check for each section of a larger text. **Critical Succes |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/5` | 0.631881 | You attempt a skill check to try to remember a bit of  knowledge regarding a topic related to that skill. Suggest  which skill you'd like to use and ask the GM one question.  The GM determines the DC. |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/9` | 0.628613 | Each skill is tied to a key attribute. You add your modifier for  this attribute to checks and DCs when using that skill. For  example, skulking about the shadowy corridors of a derelict  starship wit |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/5` | 0.623597 | When someone or something tests your skill, they attempt  a check against your skill DC, which is equal to 10 plus your  skill modifier. A skill DC works like any other DC to determine  the effect of |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/22/Text/33` | 0.609119 | You plan a short journey. While this is most often used when  traveling with a mech, vehicle, or starship, the same skill can  be used to determine the optimal route to take while traveling  on foot. |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/4` | 0.604426 | A brief description of the skill is followed by a list of actions  anyone can use, and then the actions you can perform only  if you are trained in that skill. Some actions list sample tasks  for each |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/4/Text/33` | 0.604216 | When you take on a job, the GM secretly sets the DC of  your skill check. After your first day of work, you roll to  determine your earnings. You gain an amount of income |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/15/Text/9` | 0.590847 | You attempt a Crafting check after you spend 2 days of  work setting up, or 1 day if you have the item's formula. The  GM determines the DC to Craft the item based on its level,  rarity, and other cir |

### Query 30
- Text: Lookup values for Task DifficultySimple DCUntrained10Trained15Expert20Master30Legendary40
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/Table/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/2/Table/4', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/247', 'PZO22001 Starfinder Player Core 182-209::/page/5/Table/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/Table/4', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/3', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/247']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/247` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/2/Table/4` | 0.946331 | Task DifficultySimple DCUntrained10Trained15Expert20Master30Legendary40 |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/247` | 0.641921 | Task Difficulty |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/5/Table/2` | 0.616075 | Task LevelFailureTrainedExpertMasterLegendary01 credit1 credit1 credit1 credit1 credit11 credit2 credits2 credits2 credits2 credits21 credit3 credits3 credits3 credits3 credits31 credit5 credits5 cred |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/4/Table/6` | 0.519479 | General Skill ActionProficiencyPageDecipher WritingTrained186Earn IncomeTrained186–188Identify MagicTrained188Learn a SpellTrained189–190Recall Knowledge [one-action]Untrained190–191SubsistUntrained19 |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/3` | 0.484586 | The GM sets the DC of a skill check, using the guidelines  in *Starfinder GM Core*. The DCs you're most likely  to encounter frequently are the five simple skill  DCs below, which are presented here t |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/3/Table/2` | 0.481109 | SkillPageKey AttributeUntrained ActionsTrained ActionsAcrobatics192-193DexterityBalance ❖ Tumble Through ❖Maneuver in Flight ❖ SqueezeEArcana193IntelligenceRecall Knowledgec ❖ (page 190)Borrow an Arca |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/5/Text/3` | 0.465398 | based on your result, the task's level, and your proficiency  rank (as listed on the Income Earned table). |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/7/Table/17` | 0.465161 | Spell RankPriceTypical DC1st or cantrip20 credits152nd60 credits183rd160 credits204th360 credits235th700 credits266th1,400 credits287th3,000 credits318th6,500 credits349th15,000 credits3610th70,000 cr |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/20/Text/15` | 0.439666 | The Medicine check DC is usually 15, though the GM  might adjust it based on the circumstances, such as treating  a patient outside in a storm, or treating magically cursed  wounds. If you're an exper |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/579` | 0.437808 | Task Level |

### Query 31
- Text: Summarize Task Difficulty
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/247']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/247', 'PZO22001 Starfinder Player Core 182-209::/page/2/Table/4', 'PZO22001 Starfinder Player Core 182-209::/page/22/SectionHeader/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/247', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/248', 'PZO22001 Starfinder Player Core 182-209::/page/2/Table/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/248` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/Table/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/247` | 0.876163 | Task Difficulty |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/2/Table/4` | 0.615712 | Task DifficultySimple DCUntrained10Trained15Expert20Master30Legendary40 |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/22/SectionHeader/11` | 0.538102 | **SAMPLE PERFORM TASKS** |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/11/SectionHeader/2` | 0.480966 | **SAMPLE SQUEEZE TASKS** |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/9/SectionHeader/28` | 0.461438 | **SAMPLE SUBSIST TASKS** |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/4/SectionHeader/20` | 0.436003 | **SAMPLE DECIPHER TASKS** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/10/SectionHeader/16` | 0.431230 | **SAMPLE BALANCE TASKS** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/579` | 0.427281 | Task Level |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/11/SectionHeader/28` | 0.423491 | **SAMPLE CLIMB TASKS** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/14/SectionHeader/13` | 0.421133 | **SAMPLE OPERATE DEVICE TASKS** |

### Query 32
- Text: What is the rule about Simple DC?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/248']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/248', 'PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/463', 'PZO22001 Starfinder Player Core 182-209::/page/18/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/248', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/247', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/249']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/247` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/249` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/248` | 0.789070 | Simple DC |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/463` | 0.613029 | Typical DC |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/18/Text/3` | 0.508680 | GM sets the DC based on the difficulty of the request. Some  requests are unsavory or impossible, and even a helpful NPC  would never agree to them. |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/3` | 0.443006 | The GM sets the DC of a skill check, using the guidelines  in *Starfinder GM Core*. The DCs you're most likely  to encounter frequently are the five simple skill  DCs below, which are presented here t |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/4/Text/17` | 0.414802 | The DC is determined by the GM based on the state or  complexity of the document. The GM might have you roll one  check for a short text or a check for each section of a larger text. **Critical Succes |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/14/Text/8` | 0.409082 | You perform a basic task using a digital device, such as  operating a basic program or playing a vidgame. You might  also use this if the device you're using has a physical  component, such as 3D-trac |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/10` | 0.406936 | have you use a different attribute modifier for a skill check or  when determining your skill DC. |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/6/Text/21` | 0.404142 | Magic of a tradition other than your own at a higher DC. The  GM determines whether you can do this and what the DC is. |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/22` | 0.402450 | You try to provide food and shelter for yourself, and  possibly others as well, with a standard of living described  on page 243. The GM determines the DC based on the  nature of the place where you'r |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/27/Text/15` | 0.394542 | Attempt a Thievery check to determine if you successfully  Steal the object. The DC is usually the Perception DC of the  creature wearing the object. It's easiest to steal an object  that is worn but |

### Query 33
- Text: Summarize Untrained
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/249']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/368', 'PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/365', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/249']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/249', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/248', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/250']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/248` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/250` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/368` | 0.917852 | Untrained |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/365` | 0.917852 | Untrained |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/249` | 0.917852 | Untrained |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/92` | 0.672199 | Untrained Actions |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/22/Text/12` | 0.614503 | **Untrained** casual audience |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/27` | 0.593261 | **Untrained** talk of the town |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/26/Text/26` | 0.582643 | **Untrained** determine a cardinal direction **Trained** find an overgrown path in a forest |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/9/SectionHeader/17` | 0.579592 | SUBSIST (UNTRAINED) |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/8/SectionHeader/25` | 0.577433 | RECALL KNOWLEDGE  (UNTRAINED) |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/581` | 0.560466 | Trained |

### Query 34
- Text: Summarize 10
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/250']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/645', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/250', 'PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/491']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/250', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/251', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/249']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/251` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/249` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/645` | 0.782219 | 10 |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/250` | 0.782219 | 10 |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/491` | 0.677691 | 10th |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/620` | 0.608774 | 10 credits |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/618` | 0.608774 | 10 credits |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/664` | 0.608774 | 10 credits |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/619` | 0.608774 | 10 credits |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/651` | 0.492929 | 11 |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/639` | 0.454273 | 9 |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/705` | 0.403151 | 20 |

### Query 35
- Text: Summarize Trained
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/251']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/353', 'PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/359', 'PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/581']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/251', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/252', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/250']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/252` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/250` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/353` | 0.823461 | Trained |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/359` | 0.823461 | Trained |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/581` | 0.823461 | Trained |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/251` | 0.781461 | Trained |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/356` | 0.781461 | Trained |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/362` | 0.781461 | Trained |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/4/SectionHeader/22` | 0.554292 | EARN INCOME (TRAINED) |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/93` | 0.550392 | Trained Actions |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/9/SectionHeader/17` | 0.506057 | SUBSIST (UNTRAINED) |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/24/SectionHeader/21` | 0.500098 | SOCIETY TRAINED ACTIONS |

### Query 36
- Text: Summarize 15
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/252']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/252', 'PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/675', 'PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/466']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/252', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/251', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/253']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/251` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/253` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/252` | 0.777005 | 15 |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/675` | 0.777005 | 15 |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/466` | 0.777004 | 15 |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/670` | 0.618349 | 15 credits |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/623` | 0.618349 | 15 credits |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/681` | 0.572131 | 16 |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/669` | 0.530305 | 14 |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/687` | 0.501762 | 17 |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/489` | 0.451578 | 15,000 credits |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/663` | 0.438149 | 13 |

### Query 37
- Text: Summarize Expert
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/253']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/582', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/253', 'PZO22001 Starfinder Player Core 182-209::/page/17/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/253', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/252', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/254']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/252` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/254` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/582` | 0.686190 | Expert |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/253` | 0.686190 | Expert |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/29` | 0.450031 | **Expert** obscure rumor, poorly guarded secret |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/14` | 0.404231 | **Expert** hierarchy of a company's  employees, teachings of an ancient  religious sect |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/26/Text/27` | 0.381799 | **Expert** navigate a simple maze |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/5/Table/2` | 0.370563 | Task LevelFailureTrainedExpertMasterLegendary01 credit1 credit1 credit1 credit1 credit11 credit2 credits2 credits2 credits2 credits21 credit3 credits3 credits3 credits3 credits31 credit5 credits5 cred |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/11/SectionHeader/2` | 0.361927 | **SAMPLE SQUEEZE TASKS** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/9/SectionHeader/28` | 0.360430 | **SAMPLE SUBSIST TASKS** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/38` | 0.352790 | **Expert** fly against the wind |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/9/SectionHeader/20` | 0.349402 | **SUBSIST** |

### Query 38
- Text: Summarize 20
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/254']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/254', 'PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/705', 'PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/472']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/254', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/253', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/255']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/253` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/255` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/254` | 0.769982 | 20 |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/705` | 0.769982 | 20 |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/472` | 0.769981 | 20 |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/676` | 0.617489 | 20 credits |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/624` | 0.617489 | 20 credits |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/465` | 0.617489 | 20 credits |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/626` | 0.617489 | 20 credits |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/625` | 0.617489 | 20 credits |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/629` | 0.617489 | 20 credits |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/711` | 0.613208 | 20 (critical) |

### Query 39
- Text: Summarize Master
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/255']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/255', 'PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/583', 'PZO22001 Starfinder Player Core 182-209::/page/17/Text/30']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/255', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/256', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/254']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/256` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/254` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/255` | 0.749916 | Master |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/583` | 0.749916 | Master |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/30` | 0.466629 | **Master** well-guarded or esoteric information **Legendary** information known only to an incredibly  select few, or only to extraordinary beings |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/5/Text/13` | 0.410449 | **Master** pilot a large research vessel or freighter,  present important court cases |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/5/Table/2` | 0.400892 | Task LevelFailureTrainedExpertMasterLegendary01 credit1 credit1 credit1 credit1 credit11 credit2 credits2 credits2 credits2 credits21 credit3 credits3 credits3 credits3 credits31 credit5 credits5 cred |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/39` | 0.391351 | **Master** reverse direction |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/22/Text/15` | 0.383300 | **Master** audience of discerning industry pros |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/12/Text/14` | 0.364097 | **Master** sturdy wooden door or basic plastic, iron gate,  metal bar |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/26/Text/28` | 0.362404 | **Master** navigate a relatively featureless moon |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/11/Text/3` | 0.348140 | **Trained** space barely fitting your shoulders **Master** space barely fitting your head |

### Query 40
- Text: Summarize 30
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/256']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/256', 'PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/688', 'PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/641']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/256', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/255', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/257']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/255` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/257` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/256` | 0.759036 | 30 |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/688` | 0.616081 | 30 credits |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/641` | 0.616081 | 30 credits |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/637` | 0.574081 | 30 credits |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/638` | 0.574081 | 30 credits |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/636` | 0.574081 | 30 credits |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/484` | 0.542528 | 31 |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/481` | 0.489677 | 28 |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/478` | 0.456051 | 26 |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/475` | 0.414254 | 23 |

### Query 41
- Text: Summarize Legendary
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/257']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/584', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/257', 'PZO22001 Starfinder Player Core 182-209::/page/26/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/257', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/258', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/256']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/258` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/256` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/584` | 0.892285 | Legendary |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/257` | 0.892285 | Legendary |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/26/Text/29` | 0.612157 | **Legendary** navigate an ever-changing occult realm |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/33` | 0.557951 | **Legendary** subsist on a barren  asteroid, toxic or irradiated  planet, or a city undergoing  orbital bombardment |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/14/Text/16` | 0.513110 | **Legendary** play games at a galactic competitive level,  manage interplanetary networks using Drift beacons |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/16` | 0.511866 | **Legendary** black site of an elusive  bioweapons manufacturer, secret  doctrines of a religion, remote holy sites  in the Vast |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/40` | 0.496756 | **Legendary** fly through gale force winds |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/30` | 0.472805 | **Master** well-guarded or esoteric information **Legendary** information known only to an incredibly  select few, or only to extraordinary beings |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/5/Text/14` | 0.421274 | **Legendary** run an interplanetary pilot training  program, argue a case against an Embri Speaker and  their coterie in their own court |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/5/Table/2` | 0.415092 | Task LevelFailureTrainedExpertMasterLegendary01 credit1 credit1 credit1 credit1 credit11 credit2 credits2 credits2 credits2 credits21 credit3 credits3 credits3 credits3 credits31 credit5 credits5 cred |

### Query 42
- Text: Summarize 40
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/258']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/258', 'PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/642', 'PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/643']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/258', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/5', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/257']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/Text/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/257` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/258` | 0.766281 | 40 |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/642` | 0.644261 | 40 credits |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/643` | 0.644261 | 40 credits |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/644` | 0.614261 | 40 credits |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/647` | 0.602261 | 40 credits |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/694` | 0.602261 | 40 credits |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/493` | 0.547520 | 41 |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/487` | 0.451566 | 34 |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/490` | 0.451209 | 36 |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/256` | 0.422573 | 30 |

### Query 43
- Text: What is the rule about When someone or something tests your skill, they attempt  a check against your skill DC, which is equal to 10 plus your  skill modifier. A skill DC works like any other DC to determine  the effect of an opposing creature's skill action.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/5', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/10', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/5', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/6', 'PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/258']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/258` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/5` | 1.001140 | When someone or something tests your skill, they attempt  a check against your skill DC, which is equal to 10 plus your  skill modifier. A skill DC works like any other DC to determine  the effect of |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/10` | 0.735660 | have you use a different attribute modifier for a skill check or  when determining your skill DC. |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/8` | 0.690804 | Some armor imposes a penalty on specific skill checks and  DCs. If a creature is wearing armor that imparts a skill  penalty, that penalty is applied to the creature's Strengthand Dexterity-based skil |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/15` | 0.611838 | When you're actively using a skill, often by performing one  of its actions, you might attempt a skill check: rolling a d20  and adding your skill modifier. To determine this modifier,  add your attri |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/8/Text/15` | 0.597607 | but related skill, usually against a higher DC than normal.  The GM might allow checks to Recall Knowledge using  other skills. For example, you might assess the skill of a star  athlete using Athleti |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/9` | 0.587458 | Each skill is tied to a key attribute. You add your modifier for  this attribute to checks and DCs when using that skill. For  example, skulking about the shadowy corridors of a derelict  starship wit |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/3` | 0.584535 | The GM sets the DC of a skill check, using the guidelines  in *Starfinder GM Core*. The DCs you're most likely  to encounter frequently are the five simple skill  DCs below, which are presented here t |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/16/Text/17` | 0.580320 | In most cases, creatures have a chance to detect your  deception only if they use the Seek action to attempt  Perception checks against your Deception DC. If you attempt  to directly interact with som |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/4/Text/33` | 0.556902 | When you take on a job, the GM secretly sets the DC of  your skill check. After your first day of work, you roll to  determine your earnings. You gain an amount of income |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/6/Text/24` | 0.551380 | Once you discover that an item, location, or ongoing effect  is magical, you can spend 10 minutes to try to identify the  particulars of its magic. If your attempt is interrupted, you  must start over |

### Query 44
- Text: What is the rule about See page 392 in Chapter 8: Playing the Game for more  information about modifiers, bonuses, and penalties.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/6', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/16', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/6', 'PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/7', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/6` | 0.929134 | See page 392 in Chapter 8: Playing the Game for more  information about modifiers, bonuses, and penalties. |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/16` | 0.603848 | **Skill modifier = skill's key attribute modifier + ** **proficiency bonus + other bonuses + penalties** |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/2` | 0.593270 | typically just your attribute modifier and proficiency bonus  at 1st level. At higher levels, you may wear or use items to  improve your skills with item bonuses pretty much all the  time; you should |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/15` | 0.557860 | When you're actively using a skill, often by performing one  of its actions, you might attempt a skill check: rolling a d20  and adding your skill modifier. To determine this modifier,  add your attri |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/17` | 0.543289 | When noting the modifier on your character sheet, you  should write down only the numbers that always apply— |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/9` | 0.543174 | Each skill is tied to a key attribute. You add your modifier for  this attribute to checks and DCs when using that skill. For  example, skulking about the shadowy corridors of a derelict  starship wit |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/21/Text/14` | 0.480875 | Some performances require you to be more than just  charismatic, and if you don't meet the demands of the  art form or the audience, the GM might apply a penalty  based on the relevant attribute. For |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/14/Text/11` | 0.480644 | **Failure **You can't understand the program or game and take  a –2 circumstance penalty to further attempts to access or  play it for the next day. |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/8/Text/15` | 0.468475 | but related skill, usually against a higher DC than normal.  The GM might allow checks to Recall Knowledge using  other skills. For example, you might assess the skill of a star  athlete using Athleti |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/11/Text/19` | 0.466679 | **Escape:** When you use the Escape basic action (page 408),  you can use your Athletics modifier instead of your unarmed  attack modifier. |

### Query 45
- Text: What is the rule about ARMOR AND SKILLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/7', 'PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/7', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/6', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/7` | 0.885447 | ARMOR AND SKILLS |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/1` | 0.630700 | CHAPTER 4: SKILLS |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/8` | 0.620240 | Some armor imposes a penalty on specific skill checks and  DCs. If a creature is wearing armor that imparts a skill  penalty, that penalty is applied to the creature's Strengthand Dexterity-based skil |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/10/SectionHeader/1` | 0.567087 | SKILLS |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/3/Text/10` | 0.567087 | SKILLS |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/3/Text/13` | 0.520342 | Skills |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/13/Text/44` | 0.499059 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/11/SectionHeader/37` | 0.499059 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/38` | 0.499059 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/29` | 0.499059 | **SKILLS** |

### Query 46
- Text: What is the rule about Some armor imposes a penalty on specific skill checks and  DCs. If a creature is wearing armor that imparts a skill  penalty, that penalty is applied to the creature's Strengthand Dexterity-based skill checks and skill DCs, unless the  action has the attack trait. Check penalties from armor are  detailed on page 245 in Chapter 6: Equipment.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/8', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/5', 'PZO22001 Starfinder Player Core 182-209::/page/12/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/8', 'PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/7', 'PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/8` | 1.019007 | Some armor imposes a penalty on specific skill checks and  DCs. If a creature is wearing armor that imparts a skill  penalty, that penalty is applied to the creature's Strengthand Dexterity-based skil |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/5` | 0.681457 | When someone or something tests your skill, they attempt  a check against your skill DC, which is equal to 10 plus your  skill modifier. A skill DC works like any other DC to determine  the effect of |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/12/Text/5` | 0.601327 | Some weapon traits allow you to take these actions  using a weapon, in which case the penalty might be –5  or –10 if the weapon doesn't have the agile trait. Some  characters can get unarmed attacks w |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/27/Text/16` | 0.524785 | You might also need to compare your Thievery check  result against the Perception DCs of observers other than  the person wearing the object. The GM might impose a  circumstance penalty to the DCs of |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/9` | 0.524182 | Each skill is tied to a key attribute. You add your modifier for  this attribute to checks and DCs when using that skill. For  example, skulking about the shadowy corridors of a derelict  starship wit |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/15` | 0.517539 | When you're actively using a skill, often by performing one  of its actions, you might attempt a skill check: rolling a d20  and adding your skill modifier. To determine this modifier,  add your attri |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/7` | 0.517249 | ARMOR AND SKILLS |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/8/Text/15` | 0.515412 | but related skill, usually against a higher DC than normal.  The GM might allow checks to Recall Knowledge using  other skills. For example, you might assess the skill of a star  athlete using Athleti |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/21/Text/14` | 0.511864 | Some performances require you to be more than just  charismatic, and if you don't meet the demands of the  art form or the audience, the GM might apply a penalty  based on the relevant attribute. For |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/10` | 0.507174 | have you use a different attribute modifier for a skill check or  when determining your skill DC. |

### Query 47
- Text: What is the rule about SECRET CHECKS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/9', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/10', 'PZO22001 Starfinder Player Core 182-209::/page/25/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/9', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/10', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/9` | 0.847331 | SECRET CHECKS |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/10` | 0.647350 | Sometimes you won't know whether you have succeeded  at a skill check. If an action has the secret trait, the GM  rolls the check for you and informs you of the effect  without revealing the result of |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/16` | 0.545645 | At the end of your movement, the GM rolls your Stealth  check in secret and compares the result to the Perception |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/9` | 0.497509 | You huddle behind cover or greater cover or deeper into  concealment to become hidden, rather than observed.  The GM rolls your Stealth check in secret and compares  the result to the Perception DC of |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/3` | 0.450087 | You hide a small object on your person (such as a weapon  of light Bulk). When you try to sneak a concealed object  past someone who might notice it, the GM rolls your  Stealth check and compares it t |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/16/Text/17` | 0.442485 | In most cases, creatures have a chance to detect your  deception only if they use the Seek action to attempt  Perception checks against your Deception DC. If you attempt  to directly interact with som |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/18` | 0.441400 | A creature on the lookout for forgeries, even one  who was fooled on a passive glance, can take time  to closely examine a document to see if it's a forgery.  They apply different techniques and analy |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/25/SectionHeader/8` | 0.434887 | **SECRET** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/26/ListItem/3` | 0.428023 | First, **Hide** behind something (either by taking  advantage of cover or having the concealed  condition due to fog, a spell, or a similar effect). A  successful Stealth check makes you hidden, thoug |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/24/Text/27` | 0.427861 | You create a forged document, usually over the course of a  day or a week. The GM rolls a secret DC 20 Society check.  If you need to forge a specific person's writing, you need a  sample of that pers |

### Query 48
- Text: What is the rule about Sometimes you won't know whether you have succeeded  at a skill check. If an action has the secret trait, the GM  rolls the check for you and informs you of the effect  without revealing the result of the roll or the degree of  success. The GM rolls secret checks when your knowledge  about the outcome is imperfect, like when you're searching  for a hidden creature or object, attempting to deceive  someone, translating a complex alien language, or decoding  encrypted data. This way, you as the player don't know  things that your character wouldn't. This rule is the default  for actions with the secret trait, but the GM can choose not  to use secret checks if they would rather some or all rolls  be public.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/10', 'PZO22001 Starfinder Player Core 182-209::/page/16/Text/18', 'PZO22001 Starfinder Player Core 182-209::/page/10/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/10', 'PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/11', 'PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/10` | 1.015766 | Sometimes you won't know whether you have succeeded  at a skill check. If an action has the secret trait, the GM  rolls the check for you and informs you of the effect  without revealing the result of |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/16/Text/18` | 0.678843 | If you're disguised as a specific individual, the GM might  give creatures you interact with a circumstance bonus based  on how well they know the person you're imitating, or the GM  might roll a secr |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/4` | 0.668273 | A brief description of the skill is followed by a list of actions  anyone can use, and then the actions you can perform only  if you are trained in that skill. Some actions list sample tasks  for each |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/16/Text/17` | 0.623266 | In most cases, creatures have a chance to detect your  deception only if they use the Seek action to attempt  Perception checks against your Deception DC. If you attempt  to directly interact with som |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/13` | 0.622574 | Anyone can use a skill's untrained actions, but you can  use trained actions only if you have a proficiency rank of  trained or better in that skill. A circumstance, condition, or  effect might bar yo |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/16` | 0.592131 | At the end of your movement, the GM rolls your Stealth  check in secret and compares the result to the Perception |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/3` | 0.591630 | You hide a small object on your person (such as a weapon  of light Bulk). When you try to sneak a concealed object  past someone who might notice it, the GM rolls your  Stealth check and compares it t |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/18/Text/25` | 0.585384 | If you're making a check and multiple subcategories of  Lore could apply, or a non-Lore skill could apply, you can  use whichever skill you prefer. If there's any doubt whether  a Lore skill applies t |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/8/Text/15` | 0.583505 | but related skill, usually against a higher DC than normal.  The GM might allow checks to Recall Knowledge using  other skills. For example, you might assess the skill of a star  athlete using Athleti |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/26/Text/38` | 0.578165 | In some cases, you might Track in an encounter. In this  case, Track is a single action and doesn't have the exploration  trait, but you might need to roll more often because you're  in a tense situat |

### Query 49
- Text: What is the rule about EXPLORATION AND DOWNTIME  ACTIVITIES?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/11', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/12', 'PZO22001 Starfinder Player Core 182-209::/page/14/SectionHeader/22']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/11', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/10', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/11` | 0.888749 | EXPLORATION AND DOWNTIME  ACTIVITIES |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/12` | 0.683598 | Some skill activities have the exploration or downtime trait.  Exploration activities usually take a minute or more, while  downtime activities may take a day or more. They usually  can't be used duri |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/14/SectionHeader/22` | 0.552060 | **EXPLORATION** |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/3/Footnote/4` | 0.509549 | E This skill action is used during exploration. |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/22` | 0.496173 | You try to provide food and shelter for yourself, and  possibly others as well, with a standard of living described  on page 243. The GM determines the DC based on the  nature of the place where you'r |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/10/SectionHeader/42` | 0.444303 | **EXPLORATION** **MOVE** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/4/SectionHeader/31` | 0.441233 | **DOWNTIME** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/9/SectionHeader/21` | 0.441233 | **DOWNTIME** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/26/Text/38` | 0.421797 | In some cases, you might Track in an encounter. In this  case, Track is a single action and doesn't have the exploration  trait, but you might need to roll more often because you're  in a tense situat |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/26/SectionHeader/21` | 0.418103 | **EXPLORATION** **SECRET** |

### Query 50
- Text: What is the rule about Some skill activities have the exploration or downtime trait.  Exploration activities usually take a minute or more, while  downtime activities may take a day or more. They usually  can't be used during an encounter, though the GM might  bend this restriction. If you're not sure whether you have the  time to use one of these activities, ask your GM.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/12', 'PZO22001 Starfinder Player Core 182-209::/page/26/Text/38', 'PZO22001 Starfinder Player Core 182-209::/page/4/Text/24']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/12', 'PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/13', 'PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/12` | 1.018181 | Some skill activities have the exploration or downtime trait.  Exploration activities usually take a minute or more, while  downtime activities may take a day or more. They usually  can't be used duri |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/26/Text/38` | 0.678883 | In some cases, you might Track in an encounter. In this  case, Track is a single action and doesn't have the exploration  trait, but you might need to roll more often because you're  in a tense situat |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/4/Text/24` | 0.673377 | You can use a skill to earn money during downtime. You must be  trained in the skill to do so. This takes time to set up, and your  income depends on your proficiency rank and how lucrative a  task yo |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/3/Footnote/3` | 0.619041 | D This skill action is used during downtime. |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/4/Text/32` | 0.605808 | You use one of your skills to make money during downtime.  The GM assigns a task level representing the most lucrative  job available. You can search for lower-level tasks, with the  GM determining wh |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/22` | 0.599939 | You try to provide food and shelter for yourself, and  possibly others as well, with a standard of living described  on page 243. The GM determines the DC based on the  nature of the place where you'r |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/3/Footnote/4` | 0.590447 | E This skill action is used during exploration. |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/5` | 0.582391 | You attempt a skill check to try to remember a bit of  knowledge regarding a topic related to that skill. Suggest  which skill you'd like to use and ask the GM one question.  The GM determines the DC. |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/11` | 0.577796 | EXPLORATION AND DOWNTIME  ACTIVITIES |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/7/Text/19` | 0.567575 | When Earning Income, you might be able to spend  days of downtime to prepare for your task and  lower the DC of the skill check. This might involve  rehearsing a performance set list, studying a topic |

### Query 51
- Text: What is the rule about **IMPROVING SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/13', 'PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/15', 'PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/13', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/14', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/13` | 0.866921 | **IMPROVING SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/15` | 0.619047 | **Skill Increases** |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/1` | 0.605867 | CHAPTER 4: SKILLS |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/16` | 0.543458 | Skill increases improve your proficiency in skills of your  choice. You can use these increases to become trained  in new skills or increase your proficiency rank in skills  you're trained in (from tr |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/3/Text/10` | 0.537518 | SKILLS |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/10/SectionHeader/1` | 0.537518 | SKILLS |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/38` | 0.533985 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/29` | 0.533985 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/11/SectionHeader/37` | 0.533985 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/15/Text/29` | 0.533985 | **SKILLS** |

### Query 52
- Text: What is the rule about As your character advances in level, there are two  main ways their skills improve: skill increases and skill  feats. Your class lists the levels at which you gain each  of these improvements.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/14', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/6', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/14', 'PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/13', 'PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/14` | 0.955007 | As your character advances in level, there are two  main ways their skills improve: skill increases and skill  feats. Your class lists the levels at which you gain each  of these improvements. |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/6` | 0.716289 | A character's acumen in skills can come from all sorts of  training, from piloting starships to researching a topic on  an infosphere to rehearsing a performing art. When you  create your character an |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/18` | 0.714958 | Skill feats are a type of general feat that often grant  you a new way to use a skill or make you better at  using a skill in a particular way. Skill feats always have  the skill trait. These feats ap |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/2` | 0.672768 | typically just your attribute modifier and proficiency bonus  at 1st level. At higher levels, you may wear or use items to  improve your skills with item bonuses pretty much all the  time; you should |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/7` | 0.649385 | A character gains training in certain skills at 1st level:  typically two from their background, a small number of  predetermined skills from their class, and several skills of  your choice granted by |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/16` | 0.644104 | Skill increases improve your proficiency in skills of your  choice. You can use these increases to become trained  in new skills or increase your proficiency rank in skills  you're trained in (from tr |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/4` | 0.619851 | A brief description of the skill is followed by a list of actions  anyone can use, and then the actions you can perform only  if you are trained in that skill. Some actions list sample tasks  for each |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/2` | 0.587731 | While your character's attributes represent their raw talent and potential, skills represent their  training and experience at performing certain tasks. Each skill is keyed to one of your character's |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/15` | 0.565982 | When you're actively using a skill, often by performing one  of its actions, you might attempt a skill check: rolling a d20  and adding your skill modifier. To determine this modifier,  add your attri |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/12` | 0.555095 | The actions you can perform with a given skill are sorted into  those you can use untrained and those that require you to be  trained in the skill, as shown on the Skills, Key Attributes, and  Actions |

### Query 53
- Text: What is the rule about **Skill Increases**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/15', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/16', 'PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/15', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/14', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/15` | 0.845625 | **Skill Increases** |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/16` | 0.636331 | Skill increases improve your proficiency in skills of your  choice. You can use these increases to become trained  in new skills or increase your proficiency rank in skills  you're trained in (from tr |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/13` | 0.622258 | **IMPROVING SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/1` | 0.516961 | CHAPTER 4: SKILLS |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/14` | 0.514071 | As your character advances in level, there are two  main ways their skills improve: skill increases and skill  feats. Your class lists the levels at which you gain each  of these improvements. |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/16` | 0.501679 | **Skill modifier = skill's key attribute modifier + ** **proficiency bonus + other bonuses + penalties** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/38` | 0.500763 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/19/Text/62` | 0.500763 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/7/Text/30` | 0.500763 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/43` | 0.500763 | **SKILLS** |

### Query 54
- Text: What is the rule about Skill increases improve your proficiency in skills of your  choice. You can use these increases to become trained  in new skills or increase your proficiency rank in skills  you're trained in (from trained to expert at any level,  expert to master at 7th level or higher, and master to  legendary at 15th level or higher). Unlike when you  first become trained at a skill, if two different abilities  would make you an expert, master, or legendary in a  skill, you don't get to choose a second skill to become  expert in—the redundant benefit simply has no effect.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/16', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/7', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/16', 'PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/17', 'PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/16` | 1.008257 | Skill increases improve your proficiency in skills of your  choice. You can use these increases to become trained  in new skills or increase your proficiency rank in skills  you're trained in (from tr |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/7` | 0.730829 | A character gains training in certain skills at 1st level:  typically two from their background, a small number of  predetermined skills from their class, and several skills of  your choice granted by |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/13` | 0.690129 | Anyone can use a skill's untrained actions, but you can  use trained actions only if you have a proficiency rank of  trained or better in that skill. A circumstance, condition, or  effect might bar yo |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/14` | 0.632664 | As your character advances in level, there are two  main ways their skills improve: skill increases and skill  feats. Your class lists the levels at which you gain each  of these improvements. |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/2` | 0.626411 | typically just your attribute modifier and proficiency bonus  at 1st level. At higher levels, you may wear or use items to  improve your skills with item bonuses pretty much all the  time; you should |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/15` | 0.593268 | **Skill Increases** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/6` | 0.589403 | A character's acumen in skills can come from all sorts of  training, from piloting starships to researching a topic on  an infosphere to rehearsing a performing art. When you  create your character an |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/4` | 0.584767 | A brief description of the skill is followed by a list of actions  anyone can use, and then the actions you can perform only  if you are trained in that skill. Some actions list sample tasks  for each |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/18` | 0.583200 | Skill feats are a type of general feat that often grant  you a new way to use a skill or make you better at  using a skill in a particular way. Skill feats always have  the skill trait. These feats ap |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/15` | 0.570289 | When you're actively using a skill, often by performing one  of its actions, you might attempt a skill check: rolling a d20  and adding your skill modifier. To determine this modifier,  add your attri |

### Query 55
- Text: What is the rule about **Skill Feats**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/17', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/18', 'PZO22001 Starfinder Player Core 182-209::/page/15/SectionHeader/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/17', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/18', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/2/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/17` | 0.845162 | **Skill Feats** |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/18` | 0.755140 | Skill feats are a type of general feat that often grant  you a new way to use a skill or make you better at  using a skill in a particular way. Skill feats always have  the skill trait. These feats ap |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/15/SectionHeader/19` | 0.654483 | Crafting Skill Feats |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/1` | 0.568446 | CHAPTER 4: SKILLS |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/16` | 0.561920 | **Skill modifier = skill's key attribute modifier + ** **proficiency bonus + other bonuses + penalties** |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/29` | 0.552105 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/38` | 0.552105 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/43` | 0.552105 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/5/Text/23` | 0.552105 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/19/Text/62` | 0.552105 | **SKILLS** |

### Query 56
- Text: What is the rule about Skill feats are a type of general feat that often grant  you a new way to use a skill or make you better at  using a skill in a particular way. Skill feats always have  the skill trait. These feats appear in Chapter 5.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/18', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/14', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/2/Text/18', 'PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/17', 'PZO22001 Starfinder Player Core 182-209::/page/3/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/18` | 0.989775 | Skill feats are a type of general feat that often grant  you a new way to use a skill or make you better at  using a skill in a particular way. Skill feats always have  the skill trait. These feats ap |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/14` | 0.707696 | As your character advances in level, there are two  main ways their skills improve: skill increases and skill  feats. Your class lists the levels at which you gain each  of these improvements. |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/12` | 0.630486 | The actions you can perform with a given skill are sorted into  those you can use untrained and those that require you to be  trained in the skill, as shown on the Skills, Key Attributes, and  Actions |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/2/Text/16` | 0.588004 | Skill increases improve your proficiency in skills of your  choice. You can use these increases to become trained  in new skills or increase your proficiency rank in skills  you're trained in (from tr |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/2` | 0.580281 | While your character's attributes represent their raw talent and potential, skills represent their  training and experience at performing certain tasks. Each skill is keyed to one of your character's |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/17` | 0.579674 | **Skill Feats** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/7` | 0.566331 | A character gains training in certain skills at 1st level:  typically two from their background, a small number of  predetermined skills from their class, and several skills of  your choice granted by |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/21/Text/16` | 0.565359 | When you use an action that utilizes the Performance  skill, it gains one or more traits relevant to the type of  performance. The GM might change these depending on  the circumstances, but the most c |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/15/SectionHeader/19` | 0.561454 | Crafting Skill Feats |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/4/Text/2` | 0.559043 | General skill actions are skill actions that can be used with multiple different skills. When you use a  general skill action, you might use your modifier from any skill that lists it as one of the sk |

### Query 57
- Text: What is the rule about **SKILLS, KEY ATTRIBUTES, AND ACTIONS **?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/SectionHeader/1', 'PZO22001 Starfinder Player Core 182-209::/page/7/Text/32', 'PZO22001 Starfinder Player Core 182-209::/page/19/Text/64']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/SectionHeader/1', 'PZO22001 Starfinder Player Core 182-209::/page/2/Text/18', 'PZO22001 Starfinder Player Core 182-209::/page/3/Table/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/2/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/Table/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/SectionHeader/1` | 0.910808 | **SKILLS, KEY ATTRIBUTES, AND ACTIONS ** |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/7/Text/32` | 0.665418 | **General Skill ** **Actions** |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/19/Text/64` | 0.665418 | **General Skill ** **Actions** |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/45` | 0.623418 | **General Skill ** **Actions** |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/5/Text/25` | 0.623418 | **General Skill ** **Actions** |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/11/Text/39` | 0.623418 | **General Skill ** **Actions** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/40` | 0.623418 | **General Skill ** **Actions** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/31` | 0.623418 | **General Skill ** **Actions** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/27/Text/41` | 0.623418 | **General Skill ** **Actions** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/13/Text/46` | 0.623418 | **General Skill ** **Actions** |

### Query 58
- Text: Lookup values for SkillPageKey AttributeUntrained ActionsTrained ActionsAcrobatics192-193DexterityBalance ❖
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/Table/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/Table/2', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/12', 'PZO22001 Starfinder Player Core 182-209::/page/4/Table/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/Table/2', 'PZO22001 Starfinder Player Core 182-209::/page/3/SectionHeader/1', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/89']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/89` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/Table/2` | 0.683737 | SkillPageKey AttributeUntrained ActionsTrained ActionsAcrobatics192-193DexterityBalance ❖ Tumble Through ❖Maneuver in Flight ❖ SqueezeEArcana193IntelligenceRecall Knowledgec ❖ (page 190)Borrow an Arca |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/12` | 0.677663 | The actions you can perform with a given skill are sorted into  those you can use untrained and those that require you to be  trained in the skill, as shown on the Skills, Key Attributes, and  Actions |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/4/Table/6` | 0.661890 | General Skill ActionProficiencyPageDecipher WritingTrained186Earn IncomeTrained186–188Identify MagicTrained188Learn a SpellTrained189–190Recall Knowledge [one-action]Untrained190–191SubsistUntrained19 |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/7` | 0.521397 | Acrobatics measures your ability to perform tasks requiring  coordination and grace. When you use the Escape basic  action (page 408), you can use your Acrobatics modifier  instead of your unarmed att |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/4` | 0.514824 | A brief description of the skill is followed by a list of actions  anyone can use, and then the actions you can perform only  if you are trained in that skill. Some actions list sample tasks  for each |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/9` | 0.506970 | Each skill is tied to a key attribute. You add your modifier for  this attribute to checks and DCs when using that skill. For  example, skulking about the shadowy corridors of a derelict  starship wit |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/2/Table/4` | 0.497259 | Task DifficultySimple DCUntrained10Trained15Expert20Master30Legendary40 |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/40` | 0.496693 | **General Skill ** **Actions** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/5/Text/25` | 0.496693 | **General Skill ** **Actions** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/31` | 0.496693 | **General Skill ** **Actions** |

### Query 59
- Text: What is the rule about Skill?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/89']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/89', 'PZO22001 Starfinder Player Core 182-209::/page/3/Text/13', 'PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/89', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/90', 'PZO22001 Starfinder Player Core 182-209::/page/3/Table/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/90` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/Table/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/89` | 0.731439 | Skill |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/3/Text/13` | 0.719710 | Skills |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/1` | 0.694650 | CHAPTER 4: SKILLS |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/10/SectionHeader/1` | 0.612799 | SKILLS |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/3/Text/10` | 0.612799 | SKILLS |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/38` | 0.577629 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/29` | 0.577629 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/15/Text/29` | 0.577629 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/5/Text/23` | 0.577629 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/43` | 0.577629 | **SKILLS** |

### Query 60
- Text: Summarize Page
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/90']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/351', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/90', 'PZO22001 Starfinder Player Core 182-209::/page/4/Table/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/90', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/91', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/89']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/91` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/89` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/351` | 0.663920 | Page |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/90` | 0.663920 | Page |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/4/Table/6` | 0.416605 | General Skill ActionProficiencyPageDecipher WritingTrained186Earn IncomeTrained186–188Identify MagicTrained188Learn a SpellTrained189–190Recall Knowledge [one-action]Untrained190–191SubsistUntrained19 |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/153` | 0.356480 | Decipher WritingE, G (page 186) Identify MagicE, G (page 188) Learn a SpellE, G (page 189) |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/168` | 0.356480 | Decipher WritingE, G (page 186) Identify MagicE, G (page 188) Learn a SpellE, G (page 189) |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/11/SectionHeader/2` | 0.350715 | **SAMPLE SQUEEZE TASKS** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/22/Text/19` | 0.345157 | • **Earn Income** (page 186) by staging a performance. |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/148` | 0.341572 | Identify MagicE, G (page 188), Learn a SpellE, G (page 189) |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/3/Table/2` | 0.329980 | SkillPageKey AttributeUntrained ActionsTrained ActionsAcrobatics192-193DexterityBalance ❖ Tumble Through ❖Maneuver in Flight ❖ SqueezeEArcana193IntelligenceRecall Knowledgec ❖ (page 190)Borrow an Arca |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/14/ListItem/19` | 0.325607 | **Decipher Writing** (page 186) that's programming. |

### Query 61
- Text: Summarize Key Attribute
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/91']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/91', 'PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/8', 'PZO22001 Starfinder Player Core 182-209::/page/3/SectionHeader/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/91', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/92', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/90']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/92` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/90` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/91` | 0.853979 | Key Attribute |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/8` | 0.758709 | KEY ATTRIBUTE |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/3/SectionHeader/1` | 0.550792 | **SKILLS, KEY ATTRIBUTES, AND ACTIONS ** |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/9` | 0.494745 | Each skill is tied to a key attribute. You add your modifier for  this attribute to checks and DCs when using that skill. For  example, skulking about the shadowy corridors of a derelict  starship wit |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/16` | 0.443181 | **Skill modifier = skill's key attribute modifier + ** **proficiency bonus + other bonuses + penalties** |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/2` | 0.440272 | The following entries describe the skills in the game. The heading for each entry provides the skill's  name, with that skill's key attribute in parentheses. |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/17` | 0.427611 | **Skill Feats** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/2` | 0.381244 | While your character's attributes represent their raw talent and potential, skills represent their  training and experience at performing certain tasks. Each skill is keyed to one of your character's |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/10` | 0.369207 | have you use a different attribute modifier for a skill check or  when determining your skill DC. |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/22/TableCell/398` | 0.360767 | Additional Traits |

### Query 62
- Text: What is the rule about Untrained Actions?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/92']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/92', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/12', 'PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/368']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/92', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/93', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/91']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/93` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/91` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/92` | 0.880267 | Untrained Actions |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/12` | 0.695872 | The actions you can perform with a given skill are sorted into  those you can use untrained and those that require you to be  trained in the skill, as shown on the Skills, Key Attributes, and  Actions |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/368` | 0.691725 | Untrained |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/365` | 0.649725 | Untrained |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/2/TableCell/249` | 0.649725 | Untrained |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/93` | 0.621076 | Trained Actions |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/13` | 0.580138 | Anyone can use a skill's untrained actions, but you can  use trained actions only if you have a proficiency rank of  trained or better in that skill. A circumstance, condition, or  effect might bar yo |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/26/Text/26` | 0.508307 | **Untrained** determine a cardinal direction **Trained** find an overgrown path in a forest |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/14/SectionHeader/17` | 0.501558 | COMPUTERS TRAINED ACTIONS |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/14/SectionHeader/39` | 0.493474 | CRAFTING TRAINED ACTIONS |

### Query 63
- Text: What is the rule about Trained Actions?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/93']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/93', 'PZO22001 Starfinder Player Core 182-209::/page/14/SectionHeader/39', 'PZO22001 Starfinder Player Core 182-209::/page/19/SectionHeader/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/93', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/92', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/94']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/92` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/94` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/93` | 0.862792 | Trained Actions |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/14/SectionHeader/39` | 0.684781 | CRAFTING TRAINED ACTIONS |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/19/SectionHeader/13` | 0.684665 | MEDICINE TRAINED ACTIONS |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/92` | 0.645102 | Untrained Actions |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/14/SectionHeader/17` | 0.642505 | COMPUTERS TRAINED ACTIONS |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/22/SectionHeader/17` | 0.636948 | PERFORMANCE TRAINED ACTION |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/24/SectionHeader/21` | 0.632837 | SOCIETY TRAINED ACTIONS |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/27/SectionHeader/21` | 0.619441 | THIEVERY TRAINED ACTIONS |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/24/SectionHeader/12` | 0.617462 | RELIGION TRAINED ACTIONS |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/26/SectionHeader/30` | 0.616494 | SURVIVAL TRAINED ACTIONS |

### Query 64
- Text: What is the rule about Acrobatics?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/94']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/94', 'PZO22001 Starfinder Player Core 182-209::/page/10/Text/7', 'PZO22001 Starfinder Player Core 182-209::/page/10/Text/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/94', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/95', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/93']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/95` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/93` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/94` | 0.834082 | Acrobatics |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/7` | 0.604254 | Acrobatics measures your ability to perform tasks requiring  coordination and grace. When you use the Escape basic  action (page 408), you can use your Acrobatics modifier  instead of your unarmed att |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/11` | 0.532602 | You move across a narrow surface or uneven ground,  attempting an Acrobatics check against its Balance DC. You  are off-guard while on a narrow surface or uneven ground. |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/11/Text/1` | 0.486063 | Acrobatics check at the same DC. Any result on that  check other than a critical failure causes you to become  unstuck. |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/10/SectionHeader/6` | 0.474665 | ACROBATICS (DEX) |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/10/SectionHeader/28` | 0.465238 | ACROBATICS TRAINED ACTIONS |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/32` | 0.464606 | You try a difficult maneuver while flying. Attempt an Acrobatics  check. The GM determines what maneuvers are possible, but  they rarely allow you to move farther than your fly Speed. |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/11/Text/18` | 0.462927 | Athletics allows you to perform deeds of physical prowess.  Most Athletics actions let you move about the environment  (Climb, High Jump, Long Jump, Swim) or control your  opponent's movement in comba |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/25` | 0.445830 | can try to move through the space of one enemy. Attempt  an Acrobatics check against the enemy's Reflex DC as soon  as you try to enter its space. You can Tumble Through using  Climb, Fly, Swim, or an |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/12/Text/4` | 0.437190 | Several Athletics actions have the attack trait, meaning  that using them more than once in the same turn  makes them less accurate. Since these actions use  your free hand, you use the traits for you |

### Query 65
- Text: Summarize 192-193
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/95']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/95', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/105', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/115']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/95', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/96', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/94']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/96` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/94` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/95` | 0.921349 | 192-193 |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/105` | 0.649710 | 193-195 |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/115` | 0.643508 | 196-198 |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/140` | 0.579397 | 201-202 |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/120` | 0.575640 | 198-199 |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/110` | 0.571266 | 195-196 |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/363` | 0.547238 | 189–190 |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/100` | 0.527784 | 193 |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/155` | 0.497503 | 203-204 |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/145` | 0.486620 | 202 |

### Query 66
- Text: Summarize Dexterity
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/96']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/176', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/161', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/96']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/96', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/95', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/97']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/95` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/97` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/176` | 0.942310 | Dexterity |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/161` | 0.942310 | Dexterity |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/96` | 0.942310 | Dexterity |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/186` | 0.900310 | Dexterity |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/4/SectionHeader/14` | 0.444157 | **DECIPHER WRITING** |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/24/SectionHeader/30` | 0.422964 | STEALTH (DEX) |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/9` | 0.416464 | Each skill is tied to a key attribute. You add your modifier for  this attribute to checks and DCs when using that skill. For  example, skulking about the shadowy corridors of a derelict  starship wit |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/119` | 0.399336 | Deception |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/4/SectionHeader/20` | 0.391211 | **SAMPLE DECIPHER TASKS** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/14/ListItem/19` | 0.371877 | **Decipher Writing** (page 186) that's programming. |

### Query 67
- Text: Summarize Balance ❖
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/97']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/10/SectionHeader/16', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/97', 'PZO22001 Starfinder Player Core 182-209::/page/10/SectionHeader/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/97', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/96', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/98']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/96` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/98` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/10/SectionHeader/16` | 0.673010 | **SAMPLE BALANCE TASKS** |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/97` | 0.624894 | Balance ❖ Tumble Through ❖ |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/10/SectionHeader/8` | 0.592092 | **BALANCE **[one-action] |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/13/Text/25` | 0.404828 | **Critical Failure** You lose your balance and become off-guard  until the start of your next turn. |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/13/Text/3` | 0.400214 | **Critical Failure** You lose your balance, fall, and land prone. |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/13/Text/17` | 0.400214 | **Critical Failure** You lose your balance, fall, and land prone. |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/14` | 0.393749 | **Failure** You must remain stationary to keep your balance  (wasting the action) or you fall. If you fall, your turn ends. |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/3/Table/2` | 0.366828 | SkillPageKey AttributeUntrained ActionsTrained ActionsAcrobatics192-193DexterityBalance ❖ Tumble Through ❖Maneuver in Flight ❖ SqueezeEArcana193IntelligenceRecall Knowledgec ❖ (page 190)Borrow an Arca |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/11/SectionHeader/2` | 0.357530 | **SAMPLE SQUEEZE TASKS** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/108` | 0.348354 | Disarm ❖ |

### Query 68
- Text: Summarize Maneuver in Flight ❖
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/98']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/98', 'PZO22001 Starfinder Player Core 182-209::/page/10/SectionHeader/36', 'PZO22001 Starfinder Player Core 182-209::/page/10/SectionHeader/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/98', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/99', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/97']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/99` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/97` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/98` | 0.795881 | Maneuver in Flight ❖ SqueezeE |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/10/SectionHeader/36` | 0.763333 | **SAMPLE MANEUVER IN FLIGHT TASKS** |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/10/SectionHeader/29` | 0.734289 | **MANEUVER IN FLIGHT **[one-action] |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/33` | 0.571212 | **Success** You succeed at the maneuver. |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/32` | 0.557533 | You try a difficult maneuver while flying. Attempt an Acrobatics  check. The GM determines what maneuvers are possible, but  they rarely allow you to move farther than your fly Speed. |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/34` | 0.543628 | **Failure** Your maneuver fails. The GM chooses if you simply  can't move or if some other detrimental effect happens.  The outcome should be appropriate for the maneuver you  attempted (for instance, |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/163` | 0.470920 | Drive ❖ to ❖❖❖ NavigateE Plot CourseE Run Over ❖❖❖ Stop ❖ Stunt ❖ Take Control ❖ |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/22/ListItem/28` | 0.459989 | [one-action] Attempt a Piloting check. On a success, the vehicle moves  up to its Speed and can turn normally. On a failure, the  vehicle moves its Speed in a straight line. On a critical  failure, th |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/22/ListItem/30` | 0.447166 | [three-actions] (reckless) You take a –5 penalty on your Piloting check  to maintain control of the vehicle. The vehicle moves up  to three times its Speed in a straight line at the vehicle's  current |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/23/Text/8` | 0.444662 | **Requirements** You are piloting a vehicle in motion. |

### Query 69
- Text: Summarize Arcana
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/99']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/99', 'PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/497', 'PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/496']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/99', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/98', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/100']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/98` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/100` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/99` | 0.877426 | Arcana |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/497` | 0.877425 | Arcana |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/496` | 0.725319 | Arcane |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/8/ListItem/3` | 0.631623 | **Arcana:** arcane theories, magical traditions, creatures of  arcane significance, and the Elemental, Astral, and Void  planes |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/4/ListItem/9` | 0.619570 | Arcana for writing about arcane theory, including arcane  spells and rituals |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/11/Text/8` | 0.600264 | You must be trained in Arcana to use it for the following  general skill actions. |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/11/SectionHeader/4` | 0.585260 | ARCANA (INT) |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/7/Text/3` | 0.564269 | **Skills:** Arcana, Nature, Occultism, Religion |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/6/Text/19` | 0.564269 | **Skills:** Arcana, Nature, Occultism, Religion |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/11/Text/5` | 0.562306 | Arcana measures how much you know about arcane magic and  creatures. Even if you're untrained, you can Recall Knowledge. |

### Query 70
- Text: Summarize 193
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/100']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/100', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/105', 'PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/369']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/100', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/101', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/99']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/101` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/99` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/100` | 0.795028 | 193 |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/105` | 0.731287 | 193-195 |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/369` | 0.641535 | 191 |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/120` | 0.578991 | 198-199 |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/360` | 0.563579 | 188 |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/150` | 0.549981 | 203 |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/95` | 0.532971 | 192-193 |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/115` | 0.522764 | 196-198 |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/363` | 0.518258 | 189–190 |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/354` | 0.515700 | 186 |

### Query 71
- Text: Summarize Intelligence
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/101']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/101', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/111', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/116']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/101', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/102', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/100']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/102` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/100` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/101` | 0.760807 | Intelligence |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/111` | 0.760807 | Intelligence |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/116` | 0.760807 | Intelligence |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/136` | 0.718807 | Intelligence |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/151` | 0.718807 | Intelligence |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/171` | 0.718807 | Intelligence |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/8/Text/15` | 0.375757 | but related skill, usually against a higher DC than normal.  The GM might allow checks to Recall Knowledge using  other skills. For example, you might assess the skill of a star  athlete using Athleti |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/1` | 0.374075 | CHAPTER 4: SKILLS |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/13/SectionHeader/33` | 0.367990 | COMPUTERS (INT) |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/3/Table/2` | 0.367766 | SkillPageKey AttributeUntrained ActionsTrained ActionsAcrobatics192-193DexterityBalance ❖ Tumble Through ❖Maneuver in Flight ❖ SqueezeEArcana193IntelligenceRecall Knowledgec ❖ (page 190)Borrow an Arca |

### Query 72
- Text: Summarize Recall Knowledgec ❖ (page 190)
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/102']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/102', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/152', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/162']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/102', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/103', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/101']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/103` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/101` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/102` | 1.007873 | Recall Knowledgec ❖ (page 190) |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/152` | 1.007873 | Recall Knowledgec ❖ (page 190) |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/162` | 1.007873 | Recall Knowledgec ❖ (page 190) |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/167` | 0.911591 | Recall KnowledgeG ❖ (page 190) |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/157` | 0.897060 | Perform ❖ Recall KnowledgeG ❖ (page 190) |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/137` | 0.889142 | Recall KnowledgeG ◆ (page 190) |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/117` | 0.824489 | Recall KnowledgeG ❖ (page 190) RepairE |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/147` | 0.806229 | Command an Animal ❖ Recall KnowledgeG ❖ (page 190) |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/172` | 0.803771 | Recall Knowledgec ◆ (page 190) Subsistp. c (page 191) |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/142` | 0.767204 | Administer First Aid ❖❖ Recall KnowledgeG ❖ (page 190) |

### Query 73
- Text: What is the rule about Borrow an Arcane SpellE?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/103']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/103', 'PZO22001 Starfinder Player Core 182-209::/page/11/ListItem/11', 'PZO22001 Starfinder Player Core 182-209::/page/11/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/103', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/102', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/104']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/102` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/104` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/103` | 0.649566 | Borrow an Arcane SpellE Decipher WritingE, G (page 186) Identify MagicE, G (page 188) Learn a SpellE, G (page 189) |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/11/ListItem/11` | 0.629655 | **Learn a Spell** (page 189) from the arcane tradition. |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/11/Text/15` | 0.572269 | **Success** You prepare the borrowed spell as part of  your normal spell preparation. |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/11/SectionHeader/12` | 0.533105 | **BORROW AN ARCANE SPELL** |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/11/Text/14` | 0.518082 | If you're an arcane spellcaster who prepares spells, you  can attempt to prepare a spell from someone else's arcane  spellbook or the like. The GM sets the DC for the check based  on the spell's rank |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/7/Text/8` | 0.509649 | You can gain access to a new spell of your tradition from  someone who knows that spell or from magical writing like a  spellbook or scroll. If you can cast spells of multiple traditions,  you can Lea |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/496` | 0.487047 | Arcane |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/11/Text/5` | 0.485135 | Arcana measures how much you know about arcane magic and  creatures. Even if you're untrained, you can Recall Knowledge. |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/4/ListItem/9` | 0.483735 | Arcana for writing about arcane theory, including arcane  spells and rituals |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/361` | 0.482469 | Learn a Spell |

### Query 74
- Text: Summarize Athletics
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/104']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/104', 'PZO22001 Starfinder Player Core 182-209::/page/11/Text/18', 'PZO22001 Starfinder Player Core 182-209::/page/12/SectionHeader/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/104', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/103', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/105']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/103` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/105` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/104` | 0.853437 | Athletics |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/11/Text/18` | 0.612440 | Athletics allows you to perform deeds of physical prowess.  Most Athletics actions let you move about the environment  (Climb, High Jump, Long Jump, Swim) or control your  opponent's movement in comba |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/12/SectionHeader/3` | 0.591600 | **MULTIPLE ATTACKS WITH ATHLETICS** |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/11/SectionHeader/17` | 0.533135 | ATHLETICS (STR) |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/13/SectionHeader/18` | 0.492209 | ATHLETICS TRAINED ACTION |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/94` | 0.487693 | Acrobatics |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/13/SectionHeader/29` | 0.460247 | **ATHLETICS IN LOW GRAVITY** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/19/ListItem/45` | 0.431837 | Sports Lore |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/11/Text/19` | 0.429753 | **Escape:** When you use the Escape basic action (page 408),  you can use your Athletics modifier instead of your unarmed  attack modifier. |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/12/Text/4` | 0.399669 | Several Athletics actions have the attack trait, meaning  that using them more than once in the same turn  makes them less accurate. Since these actions use  your free hand, you use the traits for you |

### Query 75
- Text: Summarize 193-195
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/105']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/105', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/120', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/100']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/105', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/106', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/104']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/106` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/104` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/105` | 0.908798 | 193-195 |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/120` | 0.713778 | 198-199 |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/100` | 0.675999 | 193 |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/363` | 0.630546 | 189–190 |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/110` | 0.604533 | 195-196 |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/95` | 0.569997 | 192-193 |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/115` | 0.554351 | 196-198 |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/369` | 0.553857 | 191 |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/360` | 0.525854 | 188 |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/140` | 0.525170 | 201-202 |

### Query 76
- Text: Summarize Strength
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/106']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/106', 'PZO22001 Starfinder Player Core 182-209::/page/12/Text/37', 'PZO22001 Starfinder Player Core 182-209::/page/11/Text/38']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/106', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/105', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/107']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/105` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/107` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/106` | 0.897161 | Strength |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/12/Text/37` | 0.455421 | You muscle a creature or object around. Attempt an Athletics  check against the target's Fortitude DC. |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/11/Text/38` | 0.426032 | **Skills Table** |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/30` | 0.384032 | **Skills Table** |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/5/Text/24` | 0.384032 | **Skills Table** |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/19/Text/63` | 0.384032 | **Skills Table** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/44` | 0.384032 | **Skills Table** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/7/Text/31` | 0.384032 | **Skills Table** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/15/Text/30` | 0.384032 | **Skills Table** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/13/Text/45` | 0.384032 | **Skills Table** |

### Query 77
- Text: Summarize Climb  Force Open  Grapple  High Jump  Long Jump  Reposition  Shove  Swim  Trip
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/107']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/107', 'PZO22001 Starfinder Player Core 182-209::/page/11/Text/18', 'PZO22001 Starfinder Player Core 182-209::/page/13/Text/30']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/107', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/106', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/108']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/106` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/108` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/107` | 1.014552 | Climb  Force Open  Grapple  High Jump  Long Jump  Reposition  Shove  Swim  Trip |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/11/Text/18` | 0.578857 | Athletics allows you to perform deeds of physical prowess.  Most Athletics actions let you move about the environment  (Climb, High Jump, Long Jump, Swim) or control your  opponent's movement in comba |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/13/Text/30` | 0.553421 | Various Athletics actions function differently in zero  gravity. Leap allows you to move in any direction  twice the distance you would move if you had Leaped  in normal gravity (up to twice your Spee |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/13/Text/27` | 0.472402 | The Leap basic action is used for High Jump and Long  Jump. A **horizontal** Leap lets you jump up to 10 feet  horizontally if your Speed is at least 15 feet, or up to  15 feet horizontally if your Sp |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/12/SectionHeader/24` | 0.460255 | **HIGH JUMP **[two-actions] |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/11/SectionHeader/28` | 0.451413 | **SAMPLE CLIMB TASKS** |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/13/Text/32` | 0.446815 | Reposition and Shove force a creature to move. When  an effect forces you to move, or if you start falling,  the distance you move is defined by the effect that  moved you, not by your Speed. Because |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/13/Text/28` | 0.445020 | A **vertical** Leap lets you jump up to 3 feet vertically  and 5 feet horizontally onto an elevated surface. |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/25` | 0.443043 | can try to move through the space of one enemy. Attempt  an Acrobatics check against the enemy's Reflex DC as soon  as you try to enter its space. You can Tumble Through using  Climb, Fly, Swim, or an |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/11/SectionHeader/20` | 0.442493 | **CLIMB **[one-action] |

### Query 78
- Text: Summarize Disarm ❖
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/108']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/108', 'PZO22001 Starfinder Player Core 182-209::/page/13/SectionHeader/19', 'PZO22001 Starfinder Player Core 182-209::/page/27/Text/24']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/108', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/109', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/107']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/109` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/107` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/108` | 0.963502 | Disarm ❖ |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/13/SectionHeader/19` | 0.686502 | **DISARM **[one-action] |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/27/Text/24` | 0.482146 | This action allows you to disarm a trap or another complex  device. Often, a device requires numerous successes before  becoming disabled, depending on its construction and  complexity. An infiltrator |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/13/Text/24` | 0.438683 | **Success** You weaken your target's grasp on the item.  Further attempts to Disarm the target of that item gain  a +2 circumstance bonus, and the target takes a –2  circumstance penalty to attacks wi |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/18/SectionHeader/18` | 0.407178 | **DEMORALIZE **[one-action] |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/132` | 0.404628 | CoerceE, Demoralize ❖ |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/27/Text/26` | 0.398911 | **Critical Success** You disable the device, or you achieve two  successes toward disabling a device requiring more than one  success. You leave no trace of your tampering, and you can  rearm the devi |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/27/SectionHeader/22` | 0.372856 | **DISABLE A DEVICE **[two-actions] |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/3/Table/2` | 0.365846 | SkillPageKey AttributeUntrained ActionsTrained ActionsAcrobatics192-193DexterityBalance ❖ Tumble Through ❖Maneuver in Flight ❖ SqueezeEArcana193IntelligenceRecall Knowledgec ❖ (page 190)Borrow an Arca |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/113` | 0.347705 | Decipher WritingE, G (page 186) Disable a Device ** HackE |

### Query 79
- Text: Summarize Computers
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/109']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/109', 'PZO22001 Starfinder Player Core 182-209::/page/8/ListItem/4', 'PZO22001 Starfinder Player Core 182-209::/page/13/Text/34']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/109', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/110', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/108']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/110` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/108` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/109` | 0.815528 | Computers |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/8/ListItem/4` | 0.609676 | **Computers:** digital and virtual equipment, computer  programs, vidgames, and fabrication programs |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/13/Text/34` | 0.587932 | Computers is your ability to work with computer systems  and some technological equipment. Even if you're untrained  in Computers, you can use it for the following general skill  actions. |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/4/ListItem/10` | 0.520312 | Computers for programming or other computer languages |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/14/ListItem/20` | 0.491482 | **Disable a Device** (page 209) that's computerized. |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/13/SectionHeader/33` | 0.469750 | COMPUTERS (INT) |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/14/Text/18` | 0.449338 | You must be trained in Computers to use it for the following  general skill actions. |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/14/Text/7` | 0.442763 | **Requirements** You are using a computer or similar device. |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/13/Text/35` | 0.439726 | • **Recall Knowledge** (page 190) about digital and virtual  equipment, digital hazards, computer programs, and  vidgames. |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/14/Text/24` | 0.405340 | You try to access, control, or change an active secured system.  In most cases, this attempt is made against a local computer  system that you access directly or indirectly through use of  a hacking t |

### Query 80
- Text: Summarize 195-196
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/110']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/110', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/115', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/105']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/110', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/111', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/109']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/111` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/109` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/110` | 0.911642 | 195-196 |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/115` | 0.722095 | 196-198 |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/105` | 0.674293 | 193-195 |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/95` | 0.574586 | 192-193 |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/120` | 0.570452 | 198-199 |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/354` | 0.537850 | 186 |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/360` | 0.527040 | 188 |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/100` | 0.523799 | 193 |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/363` | 0.521002 | 189–190 |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/357` | 0.520951 | 186–188 |

### Query 81
- Text: Summarize Intelligence
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/111']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/101', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/111', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/116']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/111', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/112', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/110']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/112` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/110` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/101` | 0.760807 | Intelligence |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/111` | 0.760807 | Intelligence |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/116` | 0.760807 | Intelligence |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/136` | 0.718807 | Intelligence |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/151` | 0.718807 | Intelligence |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/171` | 0.718807 | Intelligence |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/8/Text/15` | 0.375757 | but related skill, usually against a higher DC than normal.  The GM might allow checks to Recall Knowledge using  other skills. For example, you might assess the skill of a star  athlete using Athleti |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/1` | 0.374075 | CHAPTER 4: SKILLS |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/13/SectionHeader/33` | 0.367990 | COMPUTERS (INT) |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/3/Table/2` | 0.367766 | SkillPageKey AttributeUntrained ActionsTrained ActionsAcrobatics192-193DexterityBalance ❖ Tumble Through ❖Maneuver in Flight ❖ SqueezeEArcana193IntelligenceRecall Knowledgec ❖ (page 190)Borrow an Arca |

### Query 82
- Text: What is the rule about Access InfosphereE?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/112']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/13/Text/38', 'PZO22001 Starfinder Player Core 182-209::/page/19/ListItem/31', 'PZO22001 Starfinder Player Core 182-209::/page/13/SectionHeader/36']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/112', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/111', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/113']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/111` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/113` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/13/Text/38` | 0.671127 | **Requirements** You are using a device with infosphere  access. |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/19/ListItem/31` | 0.621309 | Infosphere Lore |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/13/SectionHeader/36` | 0.558889 | **ACCESS INFOSPHERE** |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/17/SectionHeader/11` | 0.506564 | **INFOSPHERE REPUTATION** |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/112` | 0.496053 | Access InfosphereE Recall KnowledgeG ◆ (page 190) Operate DeviceE |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/13/Text/39` | 0.477539 | You attempt to access a local network, known as an  infosphere, to come up with information on a topic. This  typically takes 10 minutes of research to find information,  with results like Recalling K |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/18/SectionHeader/1` | 0.449009 | **INFOSPHERE ANONYMITY** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/12` | 0.434588 | Your influence on an infosphere is measured using the same  attitudes as NPCs your character knows offline (*GM Core*).  However, your character's activities and other people's  attitudes toward your |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/14/Text/1` | 0.409934 | single-word answers of information common to that  settlement's infosphere may only take a minute, based on  the GM's discretion. Significant and longer investigations  should use the research subsyst |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/18/Text/2` | 0.406309 | Checks using Deception, Diplomacy, and Intimidation  are more difficult when posting anonymously on  an infosphere. In most cases, treat all checks made  using these skills on an infosphere as one deg |

### Query 83
- Text: What is the rule about Decipher WritingE, G (page 186)?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/113']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/173', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/153', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/168']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/113', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/112', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/114']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/112` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/114` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/173` | 0.823315 | Create ForgeryD Decipher WritingE, G (page 186) |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/153` | 0.745817 | Decipher WritingE, G (page 186) Identify MagicE, G (page 188) Learn a SpellE, G (page 189) |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/168` | 0.745817 | Decipher WritingE, G (page 186) Identify MagicE, G (page 188) Learn a SpellE, G (page 189) |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/14/ListItem/19` | 0.699666 | **Decipher Writing** (page 186) that's programming. |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/113` | 0.678665 | Decipher WritingE, G (page 186) Disable a Device ** HackE |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/352` | 0.602307 | Decipher Writing |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/103` | 0.601232 | Borrow an Arcane SpellE Decipher WritingE, G (page 186) Identify MagicE, G (page 188) Learn a SpellE, G (page 189) |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/24/Text/23` | 0.596184 | • **Decipher Writing** (page 186) that's a coded message,  text written in an incomplete or archaic form, or in  some cases, text in a language you don't know. |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/11/ListItem/9` | 0.578477 | **Decipher Writing** (page 186) about arcane theory. |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/21/ListItem/6` | 0.563202 | **Decipher Writing** (page 186) on occult topics, including  complex metaphysical systems, syncretic principles,  obscure philosophies, and incoherent ramblings. |

### Query 84
- Text: Summarize Crafting
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/114']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/114', 'PZO22001 Starfinder Player Core 182-209::/page/15/SectionHeader/19', 'PZO22001 Starfinder Player Core 182-209::/page/14/SectionHeader/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/114', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/113', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/115']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/113` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/115` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/114` | 0.870247 | Crafting |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/15/SectionHeader/19` | 0.686108 | Crafting Skill Feats |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/14/SectionHeader/29` | 0.683013 | CRAFTING (INT) |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/8/ListItem/5` | 0.640369 | **Crafting:** the value of items, tech gear, engineering,  unusual materials, and tech creatures |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/15/Text/12` | 0.635050 | **Success** Your attempt is successful. Each additional day spent  Crafting reduces the materials needed to complete the item  by an amount based on your level and your proficiency rank. |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/5/SectionHeader/15` | 0.630670 | Crafting Goods for the Market  (Crafting) |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/15/SectionHeader/21` | 0.618287 | **CRAFTING EXAMPLE** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/4/ListItem/26` | 0.617031 | Crafting goods for the market (Crafting) |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/4/Text/23` | 0.584717 | **Skills:** Crafting, Lore, Performance, others |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/5/Text/16` | 0.571729 | Using Crafting, you can work at producing common items for  the market. It's usually easy to find work making basic items  whose level is 1 or 2 below your settlement's level. |

### Query 85
- Text: Summarize 196-198
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/115']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/115', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/110', 'PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/357']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/115', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/116', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/114']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/116` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/114` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/115` | 0.898301 | 196-198 |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/110` | 0.667022 | 195-196 |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/357` | 0.643270 | 186–188 |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/175` | 0.587874 | 206-208 |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/95` | 0.582630 | 192-193 |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/120` | 0.570680 | 198-199 |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/360` | 0.556739 | 188 |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/105` | 0.525241 | 193-195 |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/140` | 0.521032 | 201-202 |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/354` | 0.506615 | 186 |

### Query 86
- Text: Summarize Intelligence
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/116']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/101', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/111', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/116']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/116', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/115', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/117']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/115` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/117` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/101` | 0.760807 | Intelligence |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/111` | 0.760807 | Intelligence |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/116` | 0.760807 | Intelligence |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/136` | 0.718807 | Intelligence |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/151` | 0.718807 | Intelligence |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/171` | 0.718807 | Intelligence |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/8/Text/15` | 0.375757 | but related skill, usually against a higher DC than normal.  The GM might allow checks to Recall Knowledge using  other skills. For example, you might assess the skill of a star  athlete using Athleti |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/1/SectionHeader/1` | 0.374075 | CHAPTER 4: SKILLS |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/13/SectionHeader/33` | 0.367990 | COMPUTERS (INT) |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/3/Table/2` | 0.367766 | SkillPageKey AttributeUntrained ActionsTrained ActionsAcrobatics192-193DexterityBalance ❖ Tumble Through ❖Maneuver in Flight ❖ SqueezeEArcana193IntelligenceRecall Knowledgec ❖ (page 190)Borrow an Arca |

### Query 87
- Text: Summarize Recall KnowledgeG ❖ (page 190)
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/117']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/167', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/157', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/137']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/117', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/118', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/116']
- Expanded expected found: `True`
- Expanded expected rank: `7`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/118` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/116` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/167` | 1.012161 | Recall KnowledgeG ❖ (page 190) |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/157` | 0.988924 | Perform ❖ Recall KnowledgeG ❖ (page 190) |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/137` | 0.986880 | Recall KnowledgeG ◆ (page 190) |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/162` | 0.899683 | Recall Knowledgec ❖ (page 190) |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/102` | 0.899683 | Recall Knowledgec ❖ (page 190) |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/152` | 0.899683 | Recall Knowledgec ❖ (page 190) |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/117` | 0.865092 | Recall KnowledgeG ❖ (page 190) RepairE |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/147` | 0.844457 | Command an Animal ❖ Recall KnowledgeG ❖ (page 190) |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/142` | 0.804791 | Administer First Aid ❖❖ Recall KnowledgeG ❖ (page 190) |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/172` | 0.770050 | Recall Knowledgec ◆ (page 190) Subsistp. c (page 191) |

### Query 88
- Text: Summarize CraftD, Earn IncomeD, G (page 186)
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/118']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/118', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/158', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/138']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/118', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/119', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/117']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/119` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/117` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/118` | 1.008519 | CraftD, Earn IncomeD, G (page 186) |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/158` | 0.907643 | Earn IncomeD, G (page 186) |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/138` | 0.907643 | Earn IncomeD, G (page 186) |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/14/Text/41` | 0.702184 | • **Earn Income **(page 186) by crafting goods for the market. |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/18/Text/30` | 0.589677 | • **Earn Income** (page 186) by using your knowledge to  practice a trade. |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/173` | 0.563494 | Create ForgeryD Decipher WritingE, G (page 186) |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/22/Text/19` | 0.561421 | • **Earn Income** (page 186) by staging a performance. |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/153` | 0.527126 | Decipher WritingE, G (page 186) Identify MagicE, G (page 188) Learn a SpellE, G (page 189) |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/168` | 0.527126 | Decipher WritingE, G (page 186) Identify MagicE, G (page 188) Learn a SpellE, G (page 189) |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/148` | 0.506275 | Identify MagicE, G (page 188), Learn a SpellE, G (page 189) |

### Query 89
- Text: Summarize Deception
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/119']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/119', 'PZO22001 Starfinder Player Core 182-209::/page/16/SectionHeader/5', 'PZO22001 Starfinder Player Core 182-209::/page/16/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/119', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/118', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/120']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/118` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/120` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/119` | 0.877873 | Deception |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/16/SectionHeader/5` | 0.604520 | DECEPTION (CHA) |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/16/Text/6` | 0.597528 | You can trick and mislead others using disguises, lies, and  other forms of subterfuge. Deception often has a drawback  if you get found out, and it's often best to catch a shuttle  offworld by the ti |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/16/SectionHeader/27` | 0.529401 | DECEPTION TRAINED ACTION |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/16/Text/17` | 0.498644 | In most cases, creatures have a chance to detect your  deception only if they use the Seek action to attempt  Perception checks against your Deception DC. If you attempt  to directly interact with som |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/16/Text/31` | 0.497451 | With a misleading flourish, you leave an opponent unprepared  for your real attack. Attempt a Deception check against your  target's Perception DC. |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/4/SectionHeader/14` | 0.459289 | **DECIPHER WRITING** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/96` | 0.458840 | Dexterity |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/161` | 0.458840 | Dexterity |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/186` | 0.458840 | Dexterity |

### Query 90
- Text: Summarize 198-199
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/120']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/120', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/105', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/125']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/120', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/119', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/121']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/119` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/121` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/120` | 0.878277 | 198-199 |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/105` | 0.722849 | 193-195 |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/125` | 0.683535 | 199-200 |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/140` | 0.634388 | 201-202 |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/115` | 0.616059 | 196-198 |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/363` | 0.599724 | 189–190 |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/95` | 0.586613 | 192-193 |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/110` | 0.582546 | 195-196 |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/155` | 0.565582 | 203-204 |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/699` | 0.558239 | 19 |

### Query 91
- Text: Summarize Charisma
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/121']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/121', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/156', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/126']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/121', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/122', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/120']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/122` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/120` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/121` | 0.928414 | Charisma |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/156` | 0.928414 | Charisma |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/126` | 0.928414 | Charisma |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/131` | 0.886414 | Charisma |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/21/Text/14` | 0.432800 | Some performances require you to be more than just  charismatic, and if you don't meet the demands of the  art form or the audience, the GM might apply a penalty  based on the relevant attribute. For |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/3/Table/2` | 0.362777 | SkillPageKey AttributeUntrained ActionsTrained ActionsAcrobatics192-193DexterityBalance ❖ Tumble Through ❖Maneuver in Flight ❖ SqueezeEArcana193IntelligenceRecall Knowledgec ❖ (page 190)Borrow an Arca |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/8/Text/21` | 0.318003 | **People:** "What's their personality like?" "What do they  look like?" "Do they have any notable talents?" "Do they  have notable allies and enemies?" "What kind of influence  do they have?" "Do they |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/33` | 0.317782 | With at least 1 minute of conversation, during which you  engage in charismatic overtures, flattery, and other acts of  goodwill, you seek to make a good impression on someone  to make them temporaril |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/21/SectionHeader/1` | 0.315857 | OCCULTISM (INT) |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/13/SectionHeader/19` | 0.314502 | **DISARM **[one-action] |

### Query 92
- Text: Summarize Create a Diversion ❖
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/122']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/122', 'PZO22001 Starfinder Player Core 182-209::/page/16/SectionHeader/7', 'PZO22001 Starfinder Player Core 182-209::/page/16/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/122', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/123', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/121']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/123` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/121` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/122` | 0.757854 | Create a Diversion ❖ ImpersonateE, Lie |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/16/SectionHeader/7` | 0.657122 | **CREATE A DIVERSION **[one-action] |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/16/Text/10` | 0.553275 | Attempt a single Deception check and compare it to the  Perception DCs of the creatures whose attention you're trying  to divert. Whether or not you succeed, creatures you attempt  to divert gain a +4 |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/16/Text/9` | 0.480904 | With a gesture, a trick, or some distracting words, you can  create a diversion that draws creatures' attention elsewhere.  If you use a gesture or trick, this action gains the manipulate  trait. If y |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/39` | 0.402361 | **Master** reverse direction |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/108` | 0.390893 | Disarm ❖ |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/163` | 0.358474 | Drive ❖ to ❖❖❖ NavigateE Plot CourseE Run Over ❖❖❖ Stop ❖ Stunt ❖ Take Control ❖ |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/15/SectionHeader/21` | 0.357179 | **CRAFTING EXAMPLE** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/13/SectionHeader/19` | 0.353434 | **DISARM **[one-action] |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/3/Table/2` | 0.339840 | SkillPageKey AttributeUntrained ActionsTrained ActionsAcrobatics192-193DexterityBalance ❖ Tumble Through ❖Maneuver in Flight ❖ SqueezeEArcana193IntelligenceRecall Knowledgec ❖ (page 190)Borrow an Arca |

### Query 93
- Text: Summarize Feint •
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/123']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/123', 'PZO22001 Starfinder Player Core 182-209::/page/16/SectionHeader/28', 'PZO22001 Starfinder Player Core 182-209::/page/16/Text/30']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/123', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/122', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/124']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/122` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/124` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/123` | 0.857842 | Feint • |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/16/SectionHeader/28` | 0.612638 | **FEINT **[one-action] |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/16/Text/30` | 0.536097 | **Requirements** You are within melee reach of the target you  attempt to Feint. |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/18` | 0.330252 | **Critical Failure** Your feint backfires. You are off-guard against  melee attacks the target attempts against you until the  end of your next turn. |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/2/SectionHeader/17` | 0.320540 | **Skill Feats** |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/712` | 0.315490 | — |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/5/Text/27` | 0.314641 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/9/Text/42` | 0.314641 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/47` | 0.314641 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/19/Text/66` | 0.314641 | **FEATS** |

### Query 94
- Text: What is the rule about Diplomacy?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/124']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/124', 'PZO22001 Starfinder Player Core 182-209::/page/17/Text/9', 'PZO22001 Starfinder Player Core 182-209::/page/17/SectionHeader/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/124', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/125', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/123']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/125` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/123` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/124` | 0.814591 | Diplomacy |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/9` | 0.539347 | No one can ever change the attitude of a player  character with these skills. You can roleplay  interactions with player characters, and even use  Diplomacy results if the player wants a mechanical  s |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/17/SectionHeader/19` | 0.519209 | DIPLOMACY (CHA) |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/33` | 0.471438 | With at least 1 minute of conversation, during which you  engage in charismatic overtures, flattery, and other acts of  goodwill, you seek to make a good impression on someone  to make them temporaril |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/4/Text/32` | 0.451779 | You use one of your skills to make money during downtime.  The GM assigns a task level representing the most lucrative  job available. You can search for lower-level tasks, with the  GM determining wh |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/18/Text/9` | 0.372754 | You bend others to your will using threats. Unlike Deception  or Diplomacy, Intimidation is typically a blunt instrument  with little room for nuance or care. |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/22/Text/6` | 0.356152 | When making a brief performance—one song, a quick dance, or a  few jokes—you use the Perform action. This action is most useful  when you want to prove your capability or impress someone  quickly. Per |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/20` | 0.338041 | You influence others through negotiation and flattery, or find  out information through friendly chats. |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/8/Text/21` | 0.333617 | **People:** "What's their personality like?" "What do they  look like?" "Do they have any notable talents?" "Do they  have notable allies and enemies?" "What kind of influence  do they have?" "Do they |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/20/Text/3` | 0.328418 | The animal does what you commanded as soon as  it can, usually as its first action on its next turn. If  you successfully commanded it multiple times, it does  what you said in order. It forgets all c |

### Query 95
- Text: Summarize 199-200
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/125']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/125', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/140', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/120']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/125', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/126', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/124']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/126` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/124` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/125` | 0.863228 | 199-200 |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/140` | 0.728429 | 201-202 |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/120` | 0.710645 | 198-199 |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/130` | 0.637220 | 200 |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/135` | 0.637220 | 200 |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/160` | 0.587237 | 204-206 |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/155` | 0.565651 | 203-204 |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/145` | 0.552022 | 202 |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/115` | 0.539323 | 196-198 |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/110` | 0.518648 | 195-196 |

### Query 96
- Text: Summarize Charisma
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/126']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/121', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/156', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/126']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/126', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/125', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/127']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/125` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/127` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/121` | 0.928414 | Charisma |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/156` | 0.928414 | Charisma |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/126` | 0.928414 | Charisma |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/131` | 0.886414 | Charisma |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/21/Text/14` | 0.432800 | Some performances require you to be more than just  charismatic, and if you don't meet the demands of the  art form or the audience, the GM might apply a penalty  based on the relevant attribute. For |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/3/Table/2` | 0.362777 | SkillPageKey AttributeUntrained ActionsTrained ActionsAcrobatics192-193DexterityBalance ❖ Tumble Through ❖Maneuver in Flight ❖ SqueezeEArcana193IntelligenceRecall Knowledgec ❖ (page 190)Borrow an Arca |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/8/Text/21` | 0.318003 | **People:** "What's their personality like?" "What do they  look like?" "Do they have any notable talents?" "Do they  have notable allies and enemies?" "What kind of influence  do they have?" "Do they |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/33` | 0.317782 | With at least 1 minute of conversation, during which you  engage in charismatic overtures, flattery, and other acts of  goodwill, you seek to make a good impression on someone  to make them temporaril |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/21/SectionHeader/1` | 0.315857 | OCCULTISM (INT) |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/13/SectionHeader/19` | 0.314502 | **DISARM **[one-action] |

### Query 97
- Text: Summarize Gather InformationE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/127']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/17/SectionHeader/26', 'PZO22001 Starfinder Player Core 182-209::/page/17/SectionHeader/21', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/127']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/127', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/128', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/126']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/128` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/126` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/17/SectionHeader/26` | 0.631564 | **SAMPLE GATHER INFORMATION TASKS** |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/17/SectionHeader/21` | 0.542205 | **GATHER INFORMATION** |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/127` | 0.511871 | Gather InformationE Make an ImpressionE Request ◆ |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/17/Text/24` | 0.407370 | **Success** You collect information about the individual or topic.  The GM determines the specifics. |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/14/Text/3` | 0.398884 | **Success** You find the information you were looking for. |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/112` | 0.397161 | Access InfosphereE Recall KnowledgeG ◆ (page 190) Operate DeviceE |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/153` | 0.397110 | Decipher WritingE, G (page 186) Identify MagicE, G (page 188) Learn a SpellE, G (page 189) |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/168` | 0.397110 | Decipher WritingE, G (page 186) Identify MagicE, G (page 188) Learn a SpellE, G (page 189) |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/3/Table/2` | 0.372224 | SkillPageKey AttributeUntrained ActionsTrained ActionsAcrobatics192-193DexterityBalance ❖ Tumble Through ❖Maneuver in Flight ❖ SqueezeEArcana193IntelligenceRecall Knowledgec ❖ (page 190)Borrow an Arca |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/148` | 0.366593 | Identify MagicE, G (page 188), Learn a SpellE, G (page 189) |

### Query 98
- Text: What is the rule about Identify MagicE, G (page 188), Learn a SpellE, G (page 189)?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/148']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/148', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/168', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/153']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/148', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/149', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/147']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/149` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/147` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/148` | 0.911919 | Identify MagicE, G (page 188), Learn a SpellE, G (page 189) |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/168` | 0.861461 | Decipher WritingE, G (page 186) Identify MagicE, G (page 188) Learn a SpellE, G (page 189) |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/153` | 0.861461 | Decipher WritingE, G (page 186) Identify MagicE, G (page 188) Learn a SpellE, G (page 189) |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/103` | 0.758058 | Borrow an Arcane SpellE Decipher WritingE, G (page 186) Identify MagicE, G (page 188) Learn a SpellE, G (page 189) |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/24/ListItem/15` | 0.597394 | **Identify Magic** (page 188), particularly magic of the  divine tradition. |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/21/ListItem/7` | 0.586711 | **Identify Magic** (page 188), particularly magic of the  occult tradition. |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/11/ListItem/10` | 0.585687 | **Identify Magic** (page 188), particularly arcane magic. |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/24/ListItem/16` | 0.581062 | **Learn a Spell** (page 189) from the divine tradition. |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/21/ListItem/8` | 0.580751 | **Learn a Spell** (page 189) from the occult tradition. |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/11/ListItem/11` | 0.578806 | **Learn a Spell** (page 189) from the arcane tradition. |

### Query 99
- Text: What is the rule about Decipher WritingE, G (page 186)?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/153']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/173', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/153', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/168']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/153', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/154', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/152']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/154` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/152` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/173` | 0.823315 | Create ForgeryD Decipher WritingE, G (page 186) |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/153` | 0.745817 | Decipher WritingE, G (page 186) Identify MagicE, G (page 188) Learn a SpellE, G (page 189) |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/168` | 0.745817 | Decipher WritingE, G (page 186) Identify MagicE, G (page 188) Learn a SpellE, G (page 189) |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/14/ListItem/19` | 0.699666 | **Decipher Writing** (page 186) that's programming. |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/113` | 0.678665 | Decipher WritingE, G (page 186) Disable a Device ** HackE |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/352` | 0.602307 | Decipher Writing |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/103` | 0.601232 | Borrow an Arcane SpellE Decipher WritingE, G (page 186) Identify MagicE, G (page 188) Learn a SpellE, G (page 189) |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/24/Text/23` | 0.596184 | • **Decipher Writing** (page 186) that's a coded message,  text written in an incomplete or archaic form, or in  some cases, text in a language you don't know. |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/11/ListItem/9` | 0.578477 | **Decipher Writing** (page 186) about arcane theory. |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/21/ListItem/6` | 0.563202 | **Decipher Writing** (page 186) on occult topics, including  complex metaphysical systems, syncretic principles,  obscure philosophies, and incoherent ramblings. |

### Query 100
- Text: What is the rule about Decipher WritingE, G (page 186)?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/168']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/173', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/153', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/168']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/168', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/169', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/167']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/169` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/167` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/173` | 0.823315 | Create ForgeryD Decipher WritingE, G (page 186) |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/153` | 0.745817 | Decipher WritingE, G (page 186) Identify MagicE, G (page 188) Learn a SpellE, G (page 189) |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/168` | 0.745817 | Decipher WritingE, G (page 186) Identify MagicE, G (page 188) Learn a SpellE, G (page 189) |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/14/ListItem/19` | 0.699666 | **Decipher Writing** (page 186) that's programming. |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/113` | 0.678665 | Decipher WritingE, G (page 186) Disable a Device ** HackE |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/352` | 0.602307 | Decipher Writing |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/103` | 0.601232 | Borrow an Arcane SpellE Decipher WritingE, G (page 186) Identify MagicE, G (page 188) Learn a SpellE, G (page 189) |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/24/Text/23` | 0.596184 | • **Decipher Writing** (page 186) that's a coded message,  text written in an incomplete or archaic form, or in  some cases, text in a language you don't know. |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/11/ListItem/9` | 0.578477 | **Decipher Writing** (page 186) about arcane theory. |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/21/ListItem/6` | 0.563202 | **Decipher Writing** (page 186) on occult topics, including  complex metaphysical systems, syncretic principles,  obscure philosophies, and incoherent ramblings. |

### Query 101
- Text: What is the rule about Cover TracksE?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/183']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/183', 'PZO22001 Starfinder Player Core 182-209::/page/26/Text/34', 'PZO22001 Starfinder Player Core 182-209::/page/26/SectionHeader/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/183', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/182', 'PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/184']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/182` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/184` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/183` | 0.823876 | Cover TracksE TrackE |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/26/Text/34` | 0.702323 | In some cases, you might Cover Tracks in an encounter. In  this case, Cover Tracks is a single action and doesn't have the  exploration trait. |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/26/SectionHeader/31` | 0.647312 | **COVER TRACKS** |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/26/Text/33` | 0.585423 | You cover your tracks, moving up to half your travel Speed,  using the rules on page 430. You don't need to attempt a  Survival check to cover your tracks, but anyone tracking you  must succeed at a S |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/26/Text/37` | 0.444965 | You follow tracks, moving at up to half your travel Speed,  using the rules on page 430. After a successful check to  Track, you can continue following the tracks at half your  Speed without attemptin |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/26/Text/38` | 0.431425 | In some cases, you might Track in an encounter. In this  case, Track is a single action and doesn't have the exploration  trait, but you might need to roll more often because you're  in a tense situat |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/19` | 0.408917 | DC of each creature you were hidden from or undetected  by at the start of your movement. If you have cover or  greater cover from the creature throughout your Stride,  you gain the +2 circumstance bo |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/26/Text/39` | 0.378185 | You attempt your Survival check when you start  Tracking, once every hour you continue tracking, and any |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/25/Text/9` | 0.375976 | You huddle behind cover or greater cover or deeper into  concealment to become hidden, rather than observed.  The GM rolls your Stealth check in secret and compares  the result to the Perception DC of |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/26/SectionHeader/35` | 0.343235 | **TRACK** |

### Query 102
- Text: Lookup values for General Skill ActionProficiencyPageDecipher WritingTrained186Earn IncomeTrained186–188Identify MagicTrained188Learn a SpellTrained189–190Recall Knowledge [one-action]Untrained190–191SubsistUntrained191
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/4/Table/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/4/Table/6', 'PZO22001 Starfinder Player Core 182-209::/page/3/Table/2', 'PZO22001 Starfinder Player Core 182-209::/page/1/Text/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/4/Table/6', 'PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/349', 'PZO22001 Starfinder Player Core 182-209::/page/4/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/4/TableCell/349` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/4/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/4/Table/6` | 0.996294 | General Skill ActionProficiencyPageDecipher WritingTrained186Earn IncomeTrained186–188Identify MagicTrained188Learn a SpellTrained189–190Recall Knowledge [one-action]Untrained190–191SubsistUntrained19 |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/3/Table/2` | 0.755473 | SkillPageKey AttributeUntrained ActionsTrained ActionsAcrobatics192-193DexterityBalance ❖ Tumble Through ❖Maneuver in Flight ❖ SqueezeEArcana193IntelligenceRecall Knowledgec ❖ (page 190)Borrow an Arca |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/1/Text/12` | 0.659843 | The actions you can perform with a given skill are sorted into  those you can use untrained and those that require you to be  trained in the skill, as shown on the Skills, Key Attributes, and  Actions |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/153` | 0.610504 | Decipher WritingE, G (page 186) Identify MagicE, G (page 188) Learn a SpellE, G (page 189) |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/168` | 0.610504 | Decipher WritingE, G (page 186) Identify MagicE, G (page 188) Learn a SpellE, G (page 189) |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/103` | 0.595260 | Borrow an Arcane SpellE Decipher WritingE, G (page 186) Identify MagicE, G (page 188) Learn a SpellE, G (page 189) |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/3/Footnote/5` | 0.572417 | G This is a general skill action, with a description appearing on the listed page number instead of in the skill's entry. |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/10/Text/4` | 0.566327 | A brief description of the skill is followed by a list of actions  anyone can use, and then the actions you can perform only  if you are trained in that skill. Some actions list sample tasks  for each |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/148` | 0.555947 | Identify MagicE, G (page 188), Learn a SpellE, G (page 189) |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/27/Text/41` | 0.545423 | **General Skill ** **Actions** |

### Query 103
- Text: Lookup values for Task LevelFailureTrainedExpertMasterLegendary01 credit1 credit1 credit1 credit1 credit11 credit2 credits2 credits2 credits2 credits21 credit3 credits3 credits3 credits3 credits31 credit5 credits5 credits5 credits5 credits41 credit7 credits8 credits8 credits8 credits52 credits9 credits10 credits10 credits10 credits63 credits15 credits20 credits20 credits20 credits74 credits20 credits25 credits25 credits25 credits85 credits25 credits30 credits30 credits30 credits96 credits30 credits40 credits40 credits40 credits107 credits40 credits50 credits60 credits60 credits118 credits50 credits60 credits80 credits80 credits129 credits60 credits80 credits100 credits100 credits1310 credits70 credits100 credits150 credits150 credits1415 credits80 credits150 credits200 credits200 credits1520 credits100 credits200 credits280 credits280 credits1625 credits130 credits250 credits360 credits400 credits1730 credits150 credits300 credits450 credits550 credits1840 credits200 credits450 credits700 credits900 credits1960 credits300 credits600 credits1,000 credits1,300 credits2080 credits400 credits750 credits1,500 credits2,000 credits20 (critical)—500 credits900 credits1,750 credits3,000 credits
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/5/Table/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/5/Table/2', 'PZO22001 Starfinder Player Core 182-209::/page/2/Table/4', 'PZO22001 Starfinder Player Core 182-209::/page/3/Table/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/5/Table/2', 'PZO22001 Starfinder Player Core 182-209::/page/5/SectionHeader/1', 'PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/579']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/5/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/5/TableCell/579` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/5/Table/2` | 1.002182 | Task LevelFailureTrainedExpertMasterLegendary01 credit1 credit1 credit1 credit1 credit11 credit2 credits2 credits2 credits2 credits21 credit3 credits3 credits3 credits3 credits31 credit5 credits5 cred |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/2/Table/4` | 0.631107 | Task DifficultySimple DCUntrained10Trained15Expert20Master30Legendary40 |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/3/Table/2` | 0.628279 | SkillPageKey AttributeUntrained ActionsTrained ActionsAcrobatics192-193DexterityBalance ❖ Tumble Through ❖Maneuver in Flight ❖ SqueezeEArcana193IntelligenceRecall Knowledgec ❖ (page 190)Borrow an Arca |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/7/Table/17` | 0.568795 | Spell RankPriceTypical DC1st or cantrip20 credits152nd60 credits183rd160 credits204th360 credits235th700 credits266th1,400 credits287th3,000 credits318th6,500 credits349th15,000 credits3610th70,000 cr |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/4/Table/6` | 0.552630 | General Skill ActionProficiencyPageDecipher WritingTrained186Earn IncomeTrained186–188Identify MagicTrained188Learn a SpellTrained189–190Recall Knowledge [one-action]Untrained190–191SubsistUntrained19 |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/5/Text/7` | 0.522051 | **Failure** You do shoddy work and get paid the bare minimum  for your time. Gain the amount of currency listed in the  failure column for the task level. The GM will likely reduce  how long you can c |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/5/Text/5` | 0.499190 | **Critical Success** You do outstanding work. Gain the amount  of currency listed for the task level + 1 and your proficiency  rank. |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/5/Text/6` | 0.487735 | **Success** You do competent work. Gain the amount of currency  listed for the task level and your proficiency rank. |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/5/Text/3` | 0.473862 | based on your result, the task's level, and your proficiency  rank (as listed on the Income Earned table). |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/16/Text/4` | 0.468304 | If Iseph's Crafting check result were a 30 or higher,  they'd have gotten a critical success. In that case,  they'd reduce the remaining amount by 20 credits  per day (the amount for a 6th-level exper |

### Query 104
- Text: Lookup values for Spell RankPriceTypical DC1st or cantrip20 credits152nd60 credits183rd160 credits204th360 credits235th700 credits266th1,400 credits287th3,000 credits318th6,500 credits349th15,000 credits3610th70,000 credits41
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/7/Table/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/7/Table/17', 'PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/461', 'PZO22001 Starfinder Player Core 182-209::/page/5/Table/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/7/Table/17', 'PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/461', 'PZO22001 Starfinder Player Core 182-209::/page/7/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/461` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/7/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/7/Table/17` | 1.017515 | Spell RankPriceTypical DC1st or cantrip20 credits152nd60 credits183rd160 credits204th360 credits235th700 credits266th1,400 credits287th3,000 credits318th6,500 credits349th15,000 credits3610th70,000 cr |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/461` | 0.654372 | Spell Rank |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/5/Table/2` | 0.611071 | Task LevelFailureTrainedExpertMasterLegendary01 credit1 credit1 credit1 credit1 credit11 credit2 credits2 credits2 credits2 credits21 credit3 credits3 credits3 credits3 credits31 credit5 credits5 cred |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/4/Table/6` | 0.543389 | General Skill ActionProficiencyPageDecipher WritingTrained186Earn IncomeTrained186–188Identify MagicTrained188Learn a SpellTrained189–190Recall Knowledge [one-action]Untrained190–191SubsistUntrained19 |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/3/Table/2` | 0.526569 | SkillPageKey AttributeUntrained ActionsTrained ActionsAcrobatics192-193DexterityBalance ❖ Tumble Through ❖Maneuver in Flight ❖ SqueezeEArcana193IntelligenceRecall Knowledgec ❖ (page 190)Borrow an Arca |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/11/Text/14` | 0.491394 | If you're an arcane spellcaster who prepares spells, you  can attempt to prepare a spell from someone else's arcane  spellbook or the like. The GM sets the DC for the check based  on the spell's rank |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/7/ListItem/12` | 0.481614 | Attempt a skill check for the skill corresponding to your  tradition (DC determined by the GM, often close to the  DC on the Learning a Spell Table). Uncommon or rare  spells have higher DCs; full gui |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/3/TableCell/103` | 0.462093 | Borrow an Arcane SpellE Decipher WritingE, G (page 186) Identify MagicE, G (page 188) Learn a SpellE, G (page 189) |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/8/SectionHeader/23` | 0.461782 | Learned Spells |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/2/Table/4` | 0.452724 | Task DifficultySimple DCUntrained10Trained15Expert20Master30Legendary40 |

### Query 105
- Text: Lookup values for Magical TraditionCorresponding SkillArcaneArcanaDivineReligionOccultOccultismPrimalNature
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/7/Table/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/7/Table/25', 'PZO22001 Starfinder Player Core 182-209::/page/7/Text/3', 'PZO22001 Starfinder Player Core 182-209::/page/6/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/7/Table/25', 'PZO22001 Starfinder Player Core 182-209::/page/7/Text/24', 'PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/494']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/7/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/494` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/7/Table/25` | 0.985911 | Magical TraditionCorresponding SkillArcaneArcanaDivineReligionOccultOccultismPrimalNature |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/7/Text/3` | 0.704205 | **Skills:** Arcana, Nature, Occultism, Religion |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/6/Text/19` | 0.704205 | **Skills:** Arcana, Nature, Occultism, Religion |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/7/SectionHeader/23` | 0.622723 | **MAGICAL TRADITIONS AND SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/7/TableCell/494` | 0.618988 | Magical Tradition |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/7/Text/8` | 0.595567 | You can gain access to a new spell of your tradition from  someone who knows that spell or from magical writing like a  spellbook or scroll. If you can cast spells of multiple traditions,  you can Lea |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/7/Text/24` | 0.591573 | Each magical tradition has a corresponding skill,  as shown on the table below. You must have the  trained proficiency rank in a skill to use it to Identify  Magic or Learn a Spell. Something without |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/6/Text/20` | 0.590910 | Using the skill related to the appropriate tradition, as  explained in Magical Traditions and Skills on page 189, you  can attempt to identify a magical item, location, or ongoing  effect. In many cas |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/8/ListItem/3` | 0.581782 | **Arcana:** arcane theories, magical traditions, creatures of  arcane significance, and the Elemental, Astral, and Void  planes |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/4/ListItem/9` | 0.557813 | Arcana for writing about arcane theory, including arcane  spells and rituals |

### Query 106
- Text: Lookup values for PerformanceAdditional TraitsAct or perform comedyAuditory, linguistic, and visualDanceMove and visualPlay an instrumentAuditory and manipulateOrate or singAuditory and linguistic
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/22/Table/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/22/Table/3', 'PZO22001 Starfinder Player Core 182-209::/page/8/ListItem/10', 'PZO22001 Starfinder Player Core 182-209::/page/21/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/22/Table/3', 'PZO22001 Starfinder Player Core 182-209::/page/22/TableCell/397', 'PZO22001 Starfinder Player Core 182-209::/page/22/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/22/TableCell/397` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/22/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/22/Table/3` | 0.991021 | PerformanceAdditional TraitsAct or perform comedyAuditory, linguistic, and visualDanceMove and visualPlay an instrumentAuditory and manipulateOrate or singAuditory and linguistic |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/8/ListItem/10` | 0.645806 | **Performance:** impressive performances, specific songs  or media pieces, music groups, media personalities,  and creatures who use song or dance abilities (such as  magic songs or dances) |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/21/Text/16` | 0.605635 | When you use an action that utilizes the Performance  skill, it gains one or more traits relevant to the type of  performance. The GM might change these depending on  the circumstances, but the most c |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/21/Text/17` | 0.565203 | If you want to be particularly skilled with one type  of performance, you can select the Virtuosic Performer  skill feat (page 230). That feat breaks down some of the  performance listed above into sp |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/22/TableCell/400` | 0.541785 | Auditory, linguistic, and visual |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/21/SectionHeader/15` | 0.536477 | PERFORMANCE TRAITS |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/21/Text/12` | 0.518829 | • **Recall Knowledge** (page 190) about impressive  performances, specific songs or media pieces, music  groups, media personalities, and creatures who use song  or dance abilities (such as magic song |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/22/Text/6` | 0.510948 | When making a brief performance—one song, a quick dance, or a  few jokes—you use the Perform action. This action is most useful  when you want to prove your capability or impress someone  quickly. Per |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/22/TableCell/406` | 0.508284 | Auditory and linguistic |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/21/Text/10` | 0.495505 | You are skilled at a form of performance, using your talents to  impress a crowd or make a living. |

### Query 107
- Text: Lookup values for StuntPenaltyBenefitBack Off–1Move half Speed backwards.Evade–1Move half Speed to gain a +1
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/23/Table/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 182-209::/page/23/Table/14', 'PZO22001 Starfinder Player Core 182-209::/page/23/TableCell/290', 'PZO22001 Starfinder Player Core 182-209::/page/23/TableCell/296']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 182-209::/page/23/Table/14', 'PZO22001 Starfinder Player Core 182-209::/page/23/TableCell/285', 'PZO22001 Starfinder Player Core 182-209::/page/23/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 182-209::/page/23/TableCell/285` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 182-209::/page/23/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 182-209::/page/23/Table/14` | 0.864810 | StuntPenaltyBenefitBack Off–1Move half Speed backwards.Evade–1Move half Speed to gain a +1 status bonus to AC.Flip and Burn–1Move half Speed, then turn any direction.Barrel Roll–2Move half Speed to ga |
| 2 | `PZO22001 Starfinder Player Core 182-209::/page/23/TableCell/290` | 0.669352 | Move half Speed backwards. |
| 3 | `PZO22001 Starfinder Player Core 182-209::/page/23/TableCell/296` | 0.590176 | Move half Speed, then turn any direction. |
| 4 | `PZO22001 Starfinder Player Core 182-209::/page/26/Text/37` | 0.547369 | You follow tracks, moving at up to half your travel Speed,  using the rules on page 430. After a successful check to  Track, you can continue following the tracks at half your  Speed without attemptin |
| 5 | `PZO22001 Starfinder Player Core 182-209::/page/23/TableCell/293` | 0.546763 | Move half Speed to gain a +1 status bonus to AC. |
| 6 | `PZO22001 Starfinder Player Core 182-209::/page/23/TableCell/299` | 0.531304 | Move half Speed to gain a +2 status bonus to AC. |
| 7 | `PZO22001 Starfinder Player Core 182-209::/page/23/Text/12` | 0.521151 | You perform a stunt while Driving your vehicle, temporarily  improving its effective capabilities at the risk of losing control.  Drive your vehicle and choose a stunt. All Piloting checks |
| 8 | `PZO22001 Starfinder Player Core 182-209::/page/23/TableCell/302` | 0.520485 | Move half Speed through an enemy square. |
| 9 | `PZO22001 Starfinder Player Core 182-209::/page/23/Text/13` | 0.517658 | attempted as part of your Stunt receive the listed penalty,  including Piloting checks made to take a reckless action. If the  Drive action and Stunt are both reckless, you must attempt the  Piloting |
| 10 | `PZO22001 Starfinder Player Core 182-209::/page/23/TableCell/305` | 0.516525 | Move half Speed sideways without turning. |
