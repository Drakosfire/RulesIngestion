# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `726`
- Query count: `154`
- Evaluated queries: `154`
- Coverage: `1.0000`
- MRR: `0.9122`
- hit@1: `0.8636`
- hit@3: `0.9481`
- hit@5: `0.9675`
- hit@10: `1.0000`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

### Expanded Gold Metrics
- Coverage: `1.0000`
- MRR: `0.9242`
- hit@1: `0.8831`
- hit@3: `0.9545`
- hit@5: `0.9740`
- hit@10: `1.0000`

### Expanded Gold Expansion Stats
- Queries with additions: `154`
- Avg added per query: `2.17`
- Max added: `9`
- Addition reasons:
  - graph_depth_1: `334`

### Expanded Gold Delta (Expanded - Strict)
- Coverage Δ: `0.0000`
- MRR Δ: `0.0121`
- hit@1 Δ: `0.0195`
- hit@3 Δ: `0.0065`
- hit@5 Δ: `0.0065`
- hit@10 Δ: `0.0000`

## Timings (ms)
- Embedding (chunks): `11253`
- Embedding (queries): `3397`
- Evaluation (strict): `122`
- Evaluation (expanded): `51`
- Total: `19228`

### Timing Estimates (ms)
- Evaluation (strict): `462`
- Evaluation (expanded): `169`
- Total: `15281`

## Query Details
### Query 0
- Text: Summarize CHAPTER 3: CLASSES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/23', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/28']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/1` | 1.005200 | CHAPTER 3: CLASSES |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/23` | 0.813608 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/28` | 0.813608 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/50` | 0.783608 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/58` | 0.783608 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/33` | 0.783608 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/40` | 0.783608 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/32` | 0.783608 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11` | 0.571962 | CLASS FEATURES |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26` | 0.571962 | CLASS FEATURES |

### Query 1
- Text: What is the rule about Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  character's class is perhaps the most important decision you will make for them. Groups of players  often create characters whose skills and abilities complement each other mechanically—for example,  ensuring your party includes a healer, a combat-oriented character, a stealthy character, and someone  with command over magic—so you may wish to discuss options with your group before deciding!?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/2', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/4', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/2', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/4', 'PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` | 1.007842 | Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  char |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 0.719096 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/12` | 0.687225 | The first section of each class describes the interests and  tendencies typical of that class, as well as information  on how others view them. This can help inspire you as  you determine your charact |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.624727 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/10` | 0.615710 | from their class features; and more. Your character's class  entry also provides the information needed when they  gain levels, so it will be a vital reference throughout the  course of your campaign. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.599500 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.563717 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.563675 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/5` | 0.558596 | The entries on the pages that follow describe six classes  in Starfinder. Each entry contains the information you  need to play a character of that class, as well as how to  develop them from their hu |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/16` | 0.552617 | Most classes are associated with one key attribute  modifier, but some allow you to choose from two options.  For instance, if you're a witchwarper, you can choose  either Intelligence or Charisma as |

### Query 2
- Text: What is the rule about The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't follow the instructions to bake  them a cake. Or perhaps you want your character to be a  bullet-spewing veteran who shrugs off bullets when she  activates her force field. Maybe they'll be a cool-headed  witchwarper whose far-off gaze seems to look past our  reality into potential timelines long lost. The choices you  make for your character within their class—such as a  mystic's choice of connection, a soldier's choice of fighting  style, or a witchwarper's anchor—bring these visions to life  within the context of the rules and the world.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/4', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/2', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/41']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/4', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/5', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 0.995207 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` | 0.661750 | Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  char |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/41` | 0.645541 | A witchwarper alters reality by drawing on the  infinite possibilities of other universes and timelines.  Every witchwarper is influenced by an event, and they  can harness paradoxical powers to creat |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/12` | 0.599460 | The first section of each class describes the interests and  tendencies typical of that class, as well as information  on how others view them. This can help inspire you as  you determine your charact |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/46` | 0.553791 | **INTRODUCTION** **ANCESTRIES & ** **BACKGROUNDS** **CLASSES** **Envoy** **Mystic** **Operative ** **Solarian** **Soldier** **Witchwarper** **Archetypes** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.551093 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.535603 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/7` | 0.509780 | **Archetypes** on page 174 gives you thematic options  that allow you to further customize your character's  abilities. Though these rules are not recommended for  beginners, the archetypes in this bo |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/16` | 0.507227 | Most classes are associated with one key attribute  modifier, but some allow you to choose from two options.  For instance, if you're a witchwarper, you can choose  either Intelligence or Charisma as |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/11` | 0.506814 | You issue directives to your allies, granting benefits and letting you take the lead.  Your words and deeds bolster your allies or harry your foes, and your cunning can  get you and your team out of d |

### Query 3
- Text: What is the rule about The entries on the pages that follow describe six classes  in Starfinder. Each entry contains the information you  need to play a character of that class, as well as how to  develop them from their humble beginnings at 1st level to  the dizzying heights of power at 20th level. In addition to  the class entries, you might need to reference the following  sections, which detail additional character options and  how to advance your character in level.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/5', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/10', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/5', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/4', 'PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/5` | 0.955700 | The entries on the pages that follow describe six classes  in Starfinder. Each entry contains the information you  need to play a character of that class, as well as how to  develop them from their hu |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/10` | 0.688042 | from their class features; and more. Your character's class  entry also provides the information needed when they  gain levels, so it will be a vital reference throughout the  course of your campaign. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.682937 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/12` | 0.625631 | The first section of each class describes the interests and  tendencies typical of that class, as well as information  on how others view them. This can help inspire you as  you determine your charact |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.601079 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.595938 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.584570 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 0.576315 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` | 0.562030 | Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  char |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.558097 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |

### Query 4
- Text: What is the rule about **Leveling Up **on page 29 tells you how to make your  character stronger when you get enough Experience  Points to reach a new level.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/6', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/21', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/22']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/6', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/5', 'PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/6` | 0.968391 | **Leveling Up **on page 29 tells you how to make your  character stronger when you get enough Experience  Points to reach a new level. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.623275 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/22` | 0.611129 | If your character is at least 7th level, they can use a  skill increase to become a master of a skill in which they're  already an expert. If they're at least 15th level, they can use  an increase to |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 0.553878 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/4` | 0.552909 | At 7th level, you can use skill increases to become a master  in a skill in which you're already an expert, and at 15th level,  you can use them to become legendary in a skill in which  you're already |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/3` | 0.537875 | You gain more skill increases than members of other classes.  At 2nd level and every level thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you' |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.531102 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/9` | 0.524204 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.515301 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/8` | 0.510462 | As your envoy level increases, so does your ability to adapt  to new situations. At 9th level and 15th level, increase the  number of skill feats you gain this way by 1. You can use  feats that you te |

### Query 5
- Text: What is the rule about **Archetypes** on page 174 gives you thematic options  that allow you to further customize your character's  abilities. Though these rules are not recommended for  beginners, the archetypes in this book allow you to  gain abilities from other classes starting at 2nd level.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/7', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/13', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/35']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/7', 'PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/8', 'PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/7` | 0.963864 | **Archetypes** on page 174 gives you thematic options  that allow you to further customize your character's  abilities. Though these rules are not recommended for  beginners, the archetypes in this bo |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.641020 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/35` | 0.620172 | **Archetypes** **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/65` | 0.574257 | **Archetypes** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/41` | 0.574257 | **Archetypes** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/57` | 0.574257 | **Archetypes** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/30` | 0.574257 | **Archetypes** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/38` | 0.574257 | **Archetypes** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/47` | 0.574257 | **Archetypes** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 0.573807 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |

### Query 6
- Text: Summarize READING CLASS ENTRIES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/8', 'PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/8', 'PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/7', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/8` | 0.974172 | READING CLASS ENTRIES |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/1` | 0.495248 | CHAPTER 3: CLASSES |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26` | 0.490100 | CLASS FEATURES |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11` | 0.460100 | CLASS FEATURES |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/11` | 0.418990 | PLAYING THE CLASS |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/50` | 0.414020 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/23` | 0.414020 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/58` | 0.414020 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/28` | 0.414020 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/32` | 0.414020 | **CLASSES** |

### Query 7
- Text: What is the rule about Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each class provides your character  with an attribute boost to a key attribute; a number of  Hit Points they receive at each level; proficiency ranks for  various abilities, equipment, and skills; special abilities?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/9', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/10', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/9', 'PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/8', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.935519 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/10` | 0.748673 | from their class features; and more. Your character's class  entry also provides the information needed when they  gain levels, so it will be a vital reference throughout the  course of your campaign. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.698661 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.645243 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.641422 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` | 0.632844 | This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chos |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.632192 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 0.625163 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/12` | 0.622947 | The first section of each class describes the interests and  tendencies typical of that class, as well as information  on how others view them. This can help inspire you as  you determine your charact |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.617680 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |

### Query 8
- Text: What is the rule about from their class features; and more. Your character's class  entry also provides the information needed when they  gain levels, so it will be a vital reference throughout the  course of your campaign.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/10', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/9', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/10', 'PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/10` | 0.968937 | from their class features; and more. Your character's class  entry also provides the information needed when they  gain levels, so it will be a vital reference throughout the  course of your campaign. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.729217 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.725346 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.639432 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` | 0.622568 | Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  char |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 0.608666 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.596182 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.584404 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/5` | 0.581060 | The entries on the pages that follow describe six classes  in Starfinder. Each entry contains the information you  need to play a character of that class, as well as how to  develop them from their hu |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.569052 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |

### Query 9
- Text: Summarize PLAYING THE CLASS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/10', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/11` | 0.927446 | PLAYING THE CLASS |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/1` | 0.573919 | CHAPTER 3: CLASSES |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/23` | 0.564721 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/58` | 0.534721 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/50` | 0.534721 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/28` | 0.534721 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/33` | 0.534721 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/32` | 0.534721 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/40` | 0.534721 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/19` | 0.499634 | **PLAYING THE ** **GAME** |

### Query 10
- Text: What is the rule about The first section of each class describes the interests and  tendencies typical of that class, as well as information  on how others view them. This can help inspire you as  you determine your character's actions and define their  personality, but you aren't obligated to play your character  as this section describes.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/12', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/4', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/12', 'PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/12` | 0.959872 | The first section of each class describes the interests and  tendencies typical of that class, as well as information  on how others view them. This can help inspire you as  you determine your charact |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 0.633221 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` | 0.626363 | Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  char |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.571030 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.554280 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/5` | 0.549945 | The entries on the pages that follow describe six classes  in Starfinder. Each entry contains the information you  need to play a character of that class, as well as how to  develop them from their hu |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 0.532720 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/7` | 0.528974 | At 1st level, you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start  of this class. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/7` | 0.521456 | **Archetypes** on page 174 gives you thematic options  that allow you to further customize your character's  abilities. Though these rules are not recommended for  beginners, the archetypes in this bo |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/10` | 0.520162 | from their class features; and more. Your character's class  entry also provides the information needed when they  gain levels, so it will be a vital reference throughout the  course of your campaign. |

### Query 11
- Text: Summarize KEY ATTRIBUTE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/4', 'PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/14', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/13` | 0.938890 | KEY ATTRIBUTE |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/4` | 0.838687 | **KEY ATTRIBUTE** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/1` | 0.497346 | **KEY TERMS** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/4` | 0.441379 | **Attributes** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/16` | 0.402352 | Most classes are associated with one key attribute  modifier, but some allow you to choose from two options.  For instance, if you're a witchwarper, you can choose  either Intelligence or Charisma as |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.400890 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/3` | 0.396989 | ATTRIBUTE BOOSTS |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/14` | 0.379011 | This is the attribute modifier that a member of your class  cares about the most. Many of your most useful and  powerful abilities are tied to this attribute in some way. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11` | 0.372758 | CLASS FEATURES |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26` | 0.372758 | CLASS FEATURES |

### Query 12
- Text: What is the rule about This is the attribute modifier that a member of your class  cares about the most. Many of your most useful and  powerful abilities are tied to this attribute in some way.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/14', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/15', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/14', 'PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/14` | 0.970824 | This is the attribute modifier that a member of your class  cares about the most. Many of your most useful and  powerful abilities are tied to this attribute in some way. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/15` | 0.697439 | For instance, this is the attribute modifier you'll use to  determine the Difficulty Class (DC) associated with your  character's class features and feats. This is called your  class DC. If your chara |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.685417 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/24` | 0.634935 | At 5th level and every 5 levels thereafter, your character  boosts four different attribute modifiers. This is described  briefly in the class. For the full details on attribute  modifiers and applyin |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/16` | 0.602614 | Most classes are associated with one key attribute  modifier, but some allow you to choose from two options.  For instance, if you're a witchwarper, you can choose  either Intelligence or Charisma as |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.584889 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 0.575572 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/4` | 0.559843 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/5` | 0.554859 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/27` | 0.524092 | You gain these abilities as an envoy. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |

### Query 13
- Text: What is the rule about For instance, this is the attribute modifier you'll use to  determine the Difficulty Class (DC) associated with your  character's class features and feats. This is called your  class DC. If your character is a member of a spellcasting  class, this key attribute is used to calculate spell DCs and  similar values.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/15', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/17', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/15', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/14', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/15` | 0.977187 | For instance, this is the attribute modifier you'll use to  determine the Difficulty Class (DC) associated with your  character's class features and feats. This is called your  class DC. If your chara |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.707048 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/14` | 0.706899 | This is the attribute modifier that a member of your class  cares about the most. Many of your most useful and  powerful abilities are tied to this attribute in some way. |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/7` | 0.638470 | Spellcasting classes grant a proficiency rank for spell  attacks and DCs, which are further detailed in each class's  entry. These classes rarely use their class DC. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/24` | 0.604918 | At 5th level and every 5 levels thereafter, your character  boosts four different attribute modifiers. This is described  briefly in the class. For the full details on attribute  modifiers and applyin |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/16` | 0.580695 | Most classes are associated with one key attribute  modifier, but some allow you to choose from two options.  For instance, if you're a witchwarper, you can choose  either Intelligence or Charisma as |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.557818 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.542584 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.537778 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 0.537669 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |

### Query 14
- Text: What is the rule about Most classes are associated with one key attribute  modifier, but some allow you to choose from two options.  For instance, if you're a witchwarper, you can choose  either Intelligence or Charisma as your key attribute.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/16', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/17', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/16', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/15', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/16` | 1.003147 | Most classes are associated with one key attribute  modifier, but some allow you to choose from two options.  For instance, if you're a witchwarper, you can choose  either Intelligence or Charisma as |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.694206 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.660708 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/14` | 0.618297 | This is the attribute modifier that a member of your class  cares about the most. Many of your most useful and  powerful abilities are tied to this attribute in some way. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/15` | 0.588343 | For instance, this is the attribute modifier you'll use to  determine the Difficulty Class (DC) associated with your  character's class features and feats. This is called your  class DC. If your chara |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/18` | 0.567898 | You're an efficient multitasker, and you always have more  than one goal in mind or scheme on the go. You can maintain  twice your Charisma modifier of assets. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/24` | 0.548530 | At 5th level and every 5 levels thereafter, your character  boosts four different attribute modifiers. This is described  briefly in the class. For the full details on attribute  modifiers and applyin |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` | 0.548319 | Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  char |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/6` | 0.547970 | At 1st level, your class gives you  an attribute boost to Charisma. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/36` | 0.540197 | You can maintain a number of assets equal to your Charisma  modifier. If you Size Up other assets after that, your new asset  replaces a previous one. |

### Query 15
- Text: What is the rule about Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see page 23.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/17', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/24', 'PZO22001 Starfinder Player Core 098-113::/page/6/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/17', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/16', 'PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.950790 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/24` | 0.797959 | At 5th level and every 5 levels thereafter, your character  boosts four different attribute modifiers. This is described  briefly in the class. For the full details on attribute  modifiers and applyin |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/5` | 0.767857 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/4` | 0.679488 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/14` | 0.627966 | This is the attribute modifier that a member of your class  cares about the most. Many of your most useful and  powerful abilities are tied to this attribute in some way. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/16` | 0.610116 | Most classes are associated with one key attribute  modifier, but some allow you to choose from two options.  For instance, if you're a witchwarper, you can choose  either Intelligence or Charisma as |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/15` | 0.604455 | For instance, this is the attribute modifier you'll use to  determine the Difficulty Class (DC) associated with your  character's class features and feats. This is called your  class DC. If your chara |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 0.581762 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.579547 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.579371 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |

### Query 16
- Text: What is the rule about HIT POINTS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/19', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/18` | 0.872808 | HIT POINTS |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7` | 0.824706 | **HIT POINTS** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 0.565096 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` | 0.509874 | This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chos |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/32` | 0.500582 | increase the temporary Hit Points by your level. When you  use a directive that doesn't grant temporary Hit Points, you  can grant one ally affected by that directive temporary Hit  Points equal to ha |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/1` | 0.485734 | rush into battle with weapons raised gain a higher number  of Hit Points each level, while characters who cast spells or  engage in trickery gain fewer. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/11` | 0.479537 | **Trigger** The target of your Get 'Em! is reduced to 0 Hit Points. **Requirements** You used Get 'Em! against a creature on your  last turn. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/11` | 0.471265 | **Success** The target gains temporary Hit Points equal to their  level plus your Charisma modifier. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/31` | 0.458022 | Your confidence is a battery that keeps your allies going.  When you use a directive that grants temporary Hit Points, |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/10` | 0.448749 | **Critical Success** The target gains temporary Hit Points equal  to double their level plus your Charisma modifier. |

### Query 17
- Text: What is the rule about This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chose their ancestry and the amount  listed in this entry, which equals your Constitution modifier  plus a fixed number. Classes that intend for characters to?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/19', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/2', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/19', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/21', 'PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` | 0.995273 | This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chos |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 0.862713 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/26` | 0.662604 | This section serves as a reminder of the ancestry feats your  character gains at 5th, 9th, 13th, and 17th levels. Ancestry  feats are detailed in each ancestry entry in Chapter 2, which  begins on pag |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.615393 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.605045 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.586592 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.584731 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/24` | 0.583681 | At 5th level and every 5 levels thereafter, your character  boosts four different attribute modifiers. This is described  briefly in the class. For the full details on attribute  modifiers and applyin |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.580873 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 0.565852 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |

### Query 18
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/21']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/31', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/56', 'PZO22001 Starfinder Player Core 098-113::/page/15/Text/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/21', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/19', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/31` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/56` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/31` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/21` | 0.838541 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/56` | 0.569679 | **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/67` | 0.569679 | **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/44` | 0.569679 | **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/64` | 0.524467 | **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/47` | 0.524467 | **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/39` | 0.495539 | **INTRODUCTION** **ANCESTRIES & ** |

### Query 19
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/22', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/57', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/32']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/22', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/23', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/21', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/57', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/32']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/13/Text/57` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/5/Text/32` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/22` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/57` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/32` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/28` | 0.726682 | ANCESTRY AND BACKGROUND |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/39` | 0.672101 | **INTRODUCTION** **ANCESTRIES & ** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/49` | 0.672101 | **INTRODUCTION** **ANCESTRIES & ** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/27` | 0.672101 | **INTRODUCTION** **ANCESTRIES & ** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/44` | 0.594354 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/56` | 0.594354 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/67` | 0.594354 | **BACKGROUNDS** |

### Query 20
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/23', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/33', 'PZO22001 Starfinder Player Core 098-113::/page/7/Text/50']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/23', 'PZO22001 Starfinder Player Core 098-113::/page/15/Text/32', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/24', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/22', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/28', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/33', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/58', 'PZO22001 Starfinder Player Core 098-113::/page/7/Text/50', 'PZO22001 Starfinder Player Core 098-113::/page/9/Text/40']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/15/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/11/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/5/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/13/Text/58` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/7/Text/50` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/9/Text/40` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/23` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/33` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/50` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/28` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/58` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/40` | 0.910061 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/32` | 0.910061 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/1` | 0.799617 | CHAPTER 3: CLASSES |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11` | 0.573477 | CLASS FEATURES |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26` | 0.573477 | CLASS FEATURES |

### Query 21
- Text: Summarize **Envoy**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/24']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/34', 'PZO22001 Starfinder Player Core 098-113::/page/7/Text/51', 'PZO22001 Starfinder Player Core 098-113::/page/9/Text/41']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/24', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/23', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/25']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/34` | 0.951326 | **Envoy** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/51` | 0.951326 | **Envoy** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/41` | 0.951326 | **Envoy** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/24` | 0.909326 | **Envoy** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/59` | 0.909326 | **Envoy** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/29` | 0.909326 | **Envoy** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/33` | 0.909326 | **Envoy** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/1` | 0.794388 | **Sample Envoy** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/3` | 0.666050 | **Envoy** **Page 102** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/30` | 0.643351 | **ENVOY** |

### Query 22
- Text: Summarize **Mystic**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/25']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/Text/60', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/25', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/35']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/25', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/26', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/24']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/60` | 0.959379 | **Mystic** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/25` | 0.959378 | **Mystic** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/35` | 0.959378 | **Mystic** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/30` | 0.917378 | **Mystic** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/42` | 0.917378 | **Mystic** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/52` | 0.917378 | **Mystic** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/23` | 0.686393 | **Mystic** **Page 114** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/24` | 0.603558 | The mystic is a spellcaster with a connection  to a divine, occult, or primal aspect of the universe. A  mystic casts powerful spells, learning new epiphanies  based on their chosen connection, and he |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/46` | 0.451174 | **INTRODUCTION** **ANCESTRIES & ** **BACKGROUNDS** **CLASSES** **Envoy** **Mystic** **Operative ** **Solarian** **Soldier** **Witchwarper** **Archetypes** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/27` | 0.415853 | The shirren mystic **Chk Chk** worships Zon-Shelyn, the god of creating art from suffering.  He enjoys creatively expressing himself by  writing poetry and dueling enemies with his painglaive. |

### Query 23
- Text: Summarize **Operative **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/26']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/9/Text/43', 'PZO22001 Starfinder Player Core 098-113::/page/7/Text/53', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/61']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/26', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/27', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/25']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/43` | 0.958402 | **Operative ** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/53` | 0.958402 | **Operative ** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/61` | 0.958402 | **Operative ** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/31` | 0.916402 | **Operative ** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/36` | 0.916402 | **Operative ** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/26` | 0.916402 | **Operative ** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/34` | 0.916402 | **Operative ** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/35` | 0.472364 | The operative brings precision and tactical  training to any situation. In battle, they use the Aim  action to reduce enemy cover and deal extra precision  damage. Some operatives are snipers shooting |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22` | 0.378336 | **SEARCH HIGH AND LOW! **[one-action]** TO **[two-actions] **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.372248 | **INTO POSITION! **[one-action]** TO **[two-actions] |

### Query 24
- Text: Summarize **Solarian**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/27', 'PZO22001 Starfinder Player Core 098-113::/page/7/Text/54', 'PZO22001 Starfinder Player Core 098-113::/page/15/Text/35']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/27', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/28', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/27` | 0.974700 | **Solarian** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/54` | 0.974700 | **Solarian** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/35` | 0.974700 | **Solarian** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/62` | 0.932700 | **Solarian** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/37` | 0.932700 | **Solarian** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/44` | 0.932700 | **Solarian** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/32` | 0.932700 | **Solarian** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/10` | 0.732177 | **Solarian** **Page 138** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/11` | 0.563437 | The solarian is a warrior who channels the  cosmic cycle. Every solarian creates weapons of pure  stellar energy that they can manifest at will. Cycling  between graviton and photon attunement, a sola |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/36` | 0.471086 | **Soldier** |

### Query 25
- Text: Summarize **Soldier**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/28', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/63', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/33']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/28', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/27', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/28` | 0.953061 | **Soldier** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/63` | 0.953061 | **Soldier** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/33` | 0.953061 | **Soldier** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/55` | 0.911061 | **Soldier** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/36` | 0.911061 | **Soldier** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/38` | 0.911061 | **Soldier** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/45` | 0.911061 | **Soldier** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/29` | 0.554730 | The soldier is a weapons expert with a mountain  of Hit Points who isn't afraid to get between their allies  and danger. They unleash suppressing attacks with  area weapons that pin foes. They designa |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/6` | 0.463308 | **Skills** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/32` | 0.459034 | **Obozaya** the vesk soldier doesn't back down,  she opens fire. With big guns, bigger armor,  and her trusty doshko, she becomes a wall of  bulk and bullets in combat. |

### Query 26
- Text: Summarize **Witchwarper**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/15/Text/37', 'PZO22001 Starfinder Player Core 098-113::/page/9/Text/46', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/29', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/28', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/37` | 0.988715 | **Witchwarper** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/46` | 0.988715 | **Witchwarper** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/29` | 0.988715 | **Witchwarper** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/34` | 0.946715 | **Witchwarper** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/40` | 0.946715 | **Witchwarper** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/64` | 0.946715 | **Witchwarper** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/56` | 0.946715 | **Witchwarper** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/39` | 0.718207 | **Witchwarper** **Page 162** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/41` | 0.573378 | A witchwarper alters reality by drawing on the  infinite possibilities of other universes and timelines.  Every witchwarper is influenced by an event, and they  can harness paradoxical powers to creat |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/44` | 0.535521 | **Zemir** the human witchwarper jumps between  realities and timelines, trusting his uncanny  luck and years of experience to keep him  anchored while searching for the loved ones he  lost years ago t |

### Query 27
- Text: Summarize **Archetypes**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/30', 'PZO22001 Starfinder Player Core 098-113::/page/9/Text/47', 'PZO22001 Starfinder Player Core 098-113::/page/7/Text/57']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/30', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/31', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/30` | 0.973323 | **Archetypes** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/47` | 0.973323 | **Archetypes** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/57` | 0.973323 | **Archetypes** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/41` | 0.931323 | **Archetypes** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/38` | 0.931323 | **Archetypes** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/65` | 0.931323 | **Archetypes** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/35` | 0.748593 | **Archetypes** **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/7` | 0.639470 | **Archetypes** on page 174 gives you thematic options  that allow you to further customize your character's  abilities. Though these rules are not recommended for  beginners, the archetypes in this bo |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/46` | 0.523637 | **INTRODUCTION** **ANCESTRIES & ** **BACKGROUNDS** **CLASSES** **Envoy** **Mystic** **Operative ** **Solarian** **Soldier** **Witchwarper** **Archetypes** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/4` | 0.431887 | **Attributes** |

### Query 28
- Text: What is the rule about **SKILLS** **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/31']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/9/Text/48', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/66', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/42']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/31', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/32', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/48` | 0.909736 | **SKILLS** **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/66` | 0.909736 | **SKILLS** **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/42` | 0.909736 | **SKILLS** **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/15` | 0.867736 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/58` | 0.867736 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/31` | 0.867736 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/55` | 0.656535 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/36` | 0.613813 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/39` | 0.613813 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16` | 0.593275 | Skill Feats |

### Query 29
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/32', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/17', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/43']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/32', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/31', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/33']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/33` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/32` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/17` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/43` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/49` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/67` | 0.902726 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/40` | 0.902726 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/37` | 0.902726 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/59` | 0.902726 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/64` | 0.421643 | **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/47` | 0.421643 | **INDEX** |

### Query 30
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/33']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/11/Text/38', 'PZO22001 Starfinder Player Core 098-113::/page/9/Text/50', 'PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/33', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/32', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/34']
- Expanded expected found: `True`
- Expanded expected rank: `8`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/34` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/38` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/50` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/18` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/68` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/41` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/44` | 0.847304 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/60` | 0.847304 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/33` | 0.847304 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/55` | 0.388254 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/15` | 0.332025 | **SKILLS** **FEATS** |

### Query 31
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/34']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/15/Text/42', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/19', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/69']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/34', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/35', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/33']
- Expanded expected found: `True`
- Expanded expected rank: `8`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/35` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/33` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/42` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/19` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/69` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/51` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/39` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/45` | 0.923000 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/61` | 0.923000 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/34` | 0.923000 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.432722 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44` | 0.426089 | **READY TO ROLL **[free-action] **FEAT 14** |

### Query 32
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/46', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/20', 'PZO22001 Starfinder Player Core 098-113::/page/9/Text/52']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/35', 'PZO22001 Starfinder Player Core 098-113::/page/7/Text/62', 'PZO22001 Starfinder Player Core 098-113::/page/15/Text/43', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/20', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/34', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/36', 'PZO22001 Starfinder Player Core 098-113::/page/9/Text/52', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/70', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/46', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/40']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/7/Text/62` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/15/Text/43` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/9/Text/52` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/13/Text/70` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/5/Text/46` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/11/Text/40` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/46` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/20` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/52` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/62` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/43` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/40` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/35` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/70` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/4` | 0.463693 | **Attributes** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/1` | 0.439047 | **KEY TERMS** |

### Query 33
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/36']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/15/Text/44', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/36', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/71']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/36', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/1', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/35']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/35` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/44` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/36` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/71` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/47` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/53` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/41` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/21` | 0.804819 | **GLOSSARY & ** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/63` | 0.804819 | **GLOSSARY & ** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/64` | 0.618357 | **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/47` | 0.618357 | **INDEX** |

### Query 34
- Text: What is the rule about rush into battle with weapons raised gain a higher number  of Hit Points each level, while characters who cast spells or  engage in trickery gain fewer.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/1', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/2', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/1', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/36', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/1` | 0.935922 | rush into battle with weapons raised gain a higher number  of Hit Points each level, while characters who cast spells or  engage in trickery gain fewer. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 0.627273 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` | 0.573486 | This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chos |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/10` | 0.524021 | **Critical Success** The target gains temporary Hit Points equal  to double their level plus your Charisma modifier. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/11` | 0.520472 | **Success** The target gains temporary Hit Points equal to their  level plus your Charisma modifier. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.519904 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/15` | 0.518650 | **Lead by Example** If you used two actions, Strike the target.  You gain a status bonus to the damage roll equal to your  Charisma modifier. Regardless of whether the Strike hits, you  and your allie |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/3` | 0.509218 | You gain more skill increases than members of other classes.  At 2nd level and every level thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you' |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/9` | 0.498830 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/32` | 0.485539 | increase the temporary Hit Points by your level. When you  use a directive that doesn't grant temporary Hit Points, you  can grant one ally affected by that directive temporary Hit  Points equal to ha |

### Query 35
- Text: What is the rule about Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining their Hit Points, see page 21.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/2', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/19', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/2', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/1', 'PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 0.992198 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` | 0.864490 | This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chos |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/9` | 0.674061 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/1` | 0.611020 | rush into battle with weapons raised gain a higher number  of Hit Points each level, while characters who cast spells or  engage in trickery gain fewer. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.610402 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/24` | 0.608420 | At 5th level and every 5 levels thereafter, your character  boosts four different attribute modifiers. This is described  briefly in the class. For the full details on attribute  modifiers and applyin |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/11` | 0.587175 | **Success** The target gains temporary Hit Points equal to their  level plus your Charisma modifier. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.571709 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.570628 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/5` | 0.567755 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |

### Query 36
- Text: Summarize INITIAL PROFICIENCIES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/3', 'PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/6', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/49']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/3', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/4', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/3` | 0.983481 | INITIAL PROFICIENCIES |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/6` | 0.983481 | INITIAL PROFICIENCIES |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/49` | 0.863677 | **INITIAL PROFICIENCIES** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/7` | 0.576327 | At 1st level, you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start  of this class. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/50` | 0.411825 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.400838 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/410` | 0.390711 | Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/31` | 0.385817 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/31` | 0.385817 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/21` | 0.385817 | **INTRODUCTION** |

### Query 37
- Text: What is the rule about When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency ranks range from trained to legendary.  For instance, a character trained with a battle ribbon can  use it effectively to dispatch foes, while a character who  is legendary with the weapon might be able to spell out  their name in decorative cursive script with just a flick of  their wrist!?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/4', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/5', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/4', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/5', 'PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.984974 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.806856 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 0.779747 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.657033 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/8` | 0.655384 | If something isn't listed in your character's class entry,  their proficiency rank in that statistic is untrained unless  they gain training from another source. If your character  is untrained in som |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/25` | 0.648408 | You know your weapons like you know yourself. Your  proficiency ranks for simple and martial weapons and  unarmed attacks increase to master. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.627031 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` | 0.617448 | Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  char |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/25` | 0.616531 | You've learned a few tricks with your weapons. Your  proficiency ranks for simple weapons, martial weapons, and  unarmed attacks increase to expert. Whenever you attack  the target of your Get 'Em!, y |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/7` | 0.610972 | Spellcasting classes grant a proficiency rank for spell  attacks and DCs, which are further detailed in each class's  entry. These classes rarely use their class DC. |

### Query 38
- Text: What is the rule about Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exact number depends on your  class, and some classes specify certain additional skills  that you're trained in. If your class would make you  trained in a skill you're already trained in (typically due to  your background), you can select another skill to become  trained in.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/5', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/6', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/5', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/4', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.980254 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 0.790453 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.747846 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/8` | 0.694632 | If something isn't listed in your character's class entry,  their proficiency rank in that statistic is untrained unless  they gain training from another source. If your character  is untrained in som |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.674216 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/3` | 0.656466 | You gain more skill increases than members of other classes.  At 2nd level and every level thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you' |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/50` | 0.646283 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.636527 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/7` | 0.605168 | Spellcasting classes grant a proficiency rank for spell  attacks and DCs, which are further detailed in each class's  entry. These classes rarely use their class DC. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/7` | 0.604427 | At 1st level, you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start  of this class. |

### Query 39
- Text: What is the rule about A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is trained in Perception, a saving throw,  or another statistic, they gain a proficiency bonus equal to  their level + 2, while if they have expert proficiency, they  gain a proficiency bonus equal to their level + 4. For more  about proficiency ranks, see page 24.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/6', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/5', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/6', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/7', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 1.005996 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.812945 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/8` | 0.783834 | If something isn't listed in your character's class entry,  their proficiency rank in that statistic is untrained unless  they gain training from another source. If your character  is untrained in som |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.729337 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.700341 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/50` | 0.668095 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/7` | 0.622263 | Spellcasting classes grant a proficiency rank for spell  attacks and DCs, which are further detailed in each class's  entry. These classes rarely use their class DC. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/3` | 0.617725 | You gain more skill increases than members of other classes.  At 2nd level and every level thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you' |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/25` | 0.609892 | You've learned a few tricks with your weapons. Your  proficiency ranks for simple weapons, martial weapons, and  unarmed attacks increase to expert. Whenever you attack  the target of your Get 'Em!, y |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.607487 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |

### Query 40
- Text: What is the rule about Spellcasting classes grant a proficiency rank for spell  attacks and DCs, which are further detailed in each class's  entry. These classes rarely use their class DC.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/7', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/6', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/7', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/8', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/7` | 0.988933 | Spellcasting classes grant a proficiency rank for spell  attacks and DCs, which are further detailed in each class's  entry. These classes rarely use their class DC. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 0.693566 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.689863 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/15` | 0.641872 | For instance, this is the attribute modifier you'll use to  determine the Difficulty Class (DC) associated with your  character's class features and feats. This is called your  class DC. If your chara |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/8` | 0.637980 | If something isn't listed in your character's class entry,  their proficiency rank in that statistic is untrained unless  they gain training from another source. If your character  is untrained in som |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.605274 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.548541 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.523433 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/50` | 0.519693 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/11` | 0.491947 | You've come a long way, and your hands-on experience has  improved your skills. Your proficiency rank for your envoy  class DC increases to expert. |

### Query 41
- Text: What is the rule about If something isn't listed in your character's class entry,  their proficiency rank in that statistic is untrained unless  they gain training from another source. If your character  is untrained in something, you add a proficiency bonus of  +0 when attempting a check or calculating a DC related to  that statistic.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/8', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/50', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/8', 'PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/9', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/8` | 1.002201 | If something isn't listed in your character's class entry,  their proficiency rank in that statistic is untrained unless  they gain training from another source. If your character  is untrained in som |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/50` | 0.769787 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 0.742504 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.656935 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.600027 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/3` | 0.578775 | You gain more skill increases than members of other classes.  At 2nd level and every level thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you' |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.566871 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/7` | 0.558255 | Spellcasting classes grant a proficiency rank for spell  attacks and DCs, which are further detailed in each class's  entry. These classes rarely use their class DC. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/20` | 0.534136 | **Trigger** You're about to attempt a skill check using a skill  that you don't have master proficiency in, and you  haven't rolled yet. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/21` | 0.490680 | You've learned how to dodge while wearing light or no armor.  Your proficiency ranks for light armor and unarmored defense  increase to expert. |

### Query 42
- Text: Summarize ADVANCEMENT TABLE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/9', 'PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/1', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/9', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/8', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/9` | 0.964256 | ADVANCEMENT TABLE |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/1` | 0.564202 | **ENVOY ADVANCEMENT** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.473436 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/Table/2` | 0.333643 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat2Envoy feat, skill feat, skill increase3Adaptive talent, genera |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/426` | 0.322692 | Adaptive talent, ancestry feat, envoy expertise, hidden agenda, skill increase |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/438` | 0.319209 | Adaptive talent, attribute boosts, general feat, greater weapon specialization, legendary improvisation, reflex mastery, skill increase |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 0.316734 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/8/SectionHeader/5` | 0.313982 | ADAPTIVE TALENT 3RD |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/26` | 0.304934 | This section serves as a reminder of the ancestry feats your  character gains at 5th, 9th, 13th, and 17th levels. Ancestry  feats are detailed in each ancestry entry in Chapter 2, which  begins on pag |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/58` | 0.299362 | Trained in a number of additional  skills equal to 6 plus your Intelligence  modifier |

### Query 43
- Text: What is the rule about This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the second column lists each feature  your character receives when they reach that level. The  1st-level entry includes a reminder to select your ancestry  and background.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/10', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/26', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/10', 'PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/9', 'PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.973487 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/26` | 0.767574 | This section serves as a reminder of the ancestry feats your  character gains at 5th, 9th, 13th, and 17th levels. Ancestry  feats are detailed in each ancestry entry in Chapter 2, which  begins on pag |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.720631 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/29` | 0.674877 | In addition to what you get from your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 0.672910 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.670720 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/10` | 0.665983 | from their class features; and more. Your character's class  entry also provides the information needed when they  gain levels, so it will be a vital reference throughout the  course of your campaign. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.652592 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/Table/2` | 0.625982 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat2Envoy feat, skill feat, skill increase3Adaptive talent, genera |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.625159 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |

### Query 44
- Text: What is the rule about CLASS FEATURES?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26', 'PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/408']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/12', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11` | 0.841653 | CLASS FEATURES |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26` | 0.841653 | CLASS FEATURES |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/408` | 0.758361 | Class Features |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/14` | 0.639023 | Class Feats |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.563562 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/1` | 0.542771 | CHAPTER 3: CLASSES |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/11` | 0.524692 | PLAYING THE CLASS |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.520470 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/2` | 0.499688 | You'll see the following terms in envoy class features. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/23` | 0.495843 | **CLASSES** |

### Query 45
- Text: What is the rule about This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/12', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/27', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/12', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/13', 'PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 0.903864 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/27` | 0.718206 | You gain these abilities as an envoy. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.696657 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.665570 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.649843 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.635599 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.605505 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.604718 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.587159 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/24` | 0.573598 | At 5th level and every 5 levels thereafter, your character  boosts four different attribute modifiers. This is described  briefly in the class. For the full details on attribute  modifiers and applyin |

### Query 46
- Text: What is the rule about required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to choose between options. Unless the specific  ability states otherwise, such decisions can't be changed  without retraining (as explained on page 433).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/13', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/12', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/13', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/12', 'PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.962475 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 0.645830 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.637914 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/27` | 0.570225 | You gain these abilities as an envoy. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.555502 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/24` | 0.555408 | At 5th level and every 5 levels thereafter, your character  boosts four different attribute modifiers. This is described  briefly in the class. For the full details on attribute  modifiers and applyin |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.551080 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/16` | 0.549397 | Most classes are associated with one key attribute  modifier, but some allow you to choose from two options.  For instance, if you're a witchwarper, you can choose  either Intelligence or Charisma as |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.548793 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/3` | 0.545448 | You gain more skill increases than members of other classes.  At 2nd level and every level thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you' |

### Query 47
- Text: What is the rule about Class Feats?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/14', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/15', 'PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/408']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/14', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/13', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/14` | 0.849715 | Class Feats |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.696168 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/408` | 0.621449 | Class Features |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11` | 0.573995 | CLASS FEATURES |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26` | 0.573995 | CLASS FEATURES |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/18` | 0.557205 | General Feats |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/590` | 0.552682 | Feat |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/540` | 0.552682 | Feat |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16` | 0.545795 | Skill Feats |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.527608 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |

### Query 48
- Text: What is the rule about This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, depending on the class. Specific class feats are  detailed at the end of each class entry.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/15', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/19', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/15', 'PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16', 'PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.961669 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.817545 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.764367 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.664635 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/26` | 0.659420 | This section serves as a reminder of the ancestry feats your  character gains at 5th, 9th, 13th, and 17th levels. Ancestry  feats are detailed in each ancestry entry in Chapter 2, which  begins on pag |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/10` | 0.649676 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 0.643714 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.633807 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.604276 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.595542 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |

### Query 49
- Text: What is the rule about Skill Feats?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/17', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/17', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16` | 0.845901 | Skill Feats |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.723207 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/15` | 0.678197 | **SKILLS** **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/66` | 0.636197 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/31` | 0.636197 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/42` | 0.636197 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/48` | 0.636197 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/58` | 0.636197 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/18` | 0.628760 | General Feats |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.610604 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |

### Query 50
- Text: What is the rule about This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every two levels thereafter, most classes gain a skill feat,  though some classes may get them at different levels, like the  envoy using adaptive talent. Your character must be trained  in the corresponding skill to take a skill feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/17', 'PZO22001 Starfinder Player Core 098-113::/page/7/Text/47', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/17', 'PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.997786 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.817370 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.811306 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.743867 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.741732 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/8` | 0.709045 | As your envoy level increases, so does your ability to adapt  to new situations. At 9th level and 15th level, increase the  number of skill feats you gain this way by 1. You can use  feats that you te |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/10` | 0.679876 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/26` | 0.640419 | This section serves as a reminder of the ancestry feats your  character gains at 5th, 9th, 13th, and 17th levels. Ancestry  feats are detailed in each ancestry entry in Chapter 2, which  begins on pag |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/3` | 0.636659 | You gain more skill increases than members of other classes.  At 2nd level and every level thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you' |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/15` | 0.636449 | At every level that you gain an envoy feat, you can select  one of the following feats. You must satisfy any prerequisites  before selecting the feat. |

### Query 51
- Text: What is the rule about General Feats?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/8/Text/10', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/540']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/19', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/18` | 0.832014 | General Feats |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/10` | 0.679129 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/540` | 0.640738 | Feat |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.604975 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/590` | 0.598738 | Feat |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16` | 0.563530 | Skill Feats |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/25` | 0.538368 | Ancestry Feats |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/14` | 0.527944 | Class Feats |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/8/SectionHeader/9` | 0.508844 | GENERAL FEATS 3RD |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/36` | 0.495038 | **FEATS** |

### Query 52
- Text: What is the rule about This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select any general feat (including skill feats) as long  as your character qualifies for it. More information can be  found in Chapter 5 (page 210).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/19', 'PZO22001 Starfinder Player Core 098-113::/page/8/Text/10', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/15']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/19', 'PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.988415 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/10` | 0.878945 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.824147 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.757938 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.716251 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.647255 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/26` | 0.645087 | This section serves as a reminder of the ancestry feats your  character gains at 5th, 9th, 13th, and 17th levels. Ancestry  feats are detailed in each ancestry entry in Chapter 2, which  begins on pag |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.638088 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/15` | 0.621600 | At every level that you gain an envoy feat, you can select  one of the following feats. You must satisfy any prerequisites  before selecting the feat. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 0.618631 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |

### Query 53
- Text: What is the rule about Skill Increases?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/20', 'PZO22001 Starfinder Player Core 098-113::/page/8/Text/3', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/21']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/20', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/21', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/20` | 0.743958 | Skill Increases |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/3` | 0.623543 | You gain more skill increases than members of other classes.  At 2nd level and every level thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you' |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.622157 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/8/SectionHeader/1` | 0.564176 | SKILL INCREASES 2ND |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/4` | 0.535254 | At 7th level, you can use skill increases to become a master  in a skill in which you're already an expert, and at 15th level,  you can use them to become legendary in a skill in which  you're already |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/22` | 0.528728 | If your character is at least 7th level, they can use a  skill increase to become a master of a skill in which they're  already an expert. If they're at least 15th level, they can use  an increase to |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/440` | 0.521566 | Envoy feat, skill feat, skill increase |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/424` | 0.521566 | Envoy feat, skill feat, skill increase |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/444` | 0.521566 | Envoy feat, skill feat, skill increase |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/432` | 0.521566 | Envoy feat, skill feat, skill increase |

### Query 54
- Text: What is the rule about This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though envoys gain them earlier and more often.  Your character can use a skill increase to either become  trained in one skill in which they're untrained, or to become  an expert in one skill in which they're already trained.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/21', 'PZO22001 Starfinder Player Core 098-113::/page/8/Text/3', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/21', 'PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/20', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.993109 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/3` | 0.842170 | You gain more skill increases than members of other classes.  At 2nd level and every level thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you' |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.775465 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/22` | 0.716687 | If your character is at least 7th level, they can use a  skill increase to become a master of a skill in which they're  already an expert. If they're at least 15th level, they can use  an increase to |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/4` | 0.712623 | At 7th level, you can use skill increases to become a master  in a skill in which you're already an expert, and at 15th level,  you can use them to become legendary in a skill in which  you're already |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/8` | 0.685487 | As your envoy level increases, so does your ability to adapt  to new situations. At 9th level and 15th level, increase the  number of skill feats you gain this way by 1. You can use  feats that you te |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 0.680629 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.677956 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/50` | 0.670465 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.659939 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |

### Query 55
- Text: What is the rule about If your character is at least 7th level, they can use a  skill increase to become a master of a skill in which they're  already an expert. If they're at least 15th level, they can use  an increase to become legendary in a skill in which they're  already a master.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/22', 'PZO22001 Starfinder Player Core 098-113::/page/8/Text/4', 'PZO22001 Starfinder Player Core 098-113::/page/8/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/22', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/21', 'PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/22` | 0.989375 | If your character is at least 7th level, they can use a  skill increase to become a master of a skill in which they're  already an expert. If they're at least 15th level, they can use  an increase to |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/4` | 0.950527 | At 7th level, you can use skill increases to become a master  in a skill in which you're already an expert, and at 15th level,  you can use them to become legendary in a skill in which  you're already |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/3` | 0.743640 | You gain more skill increases than members of other classes.  At 2nd level and every level thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you' |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.702650 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/9` | 0.595941 | You've learned how to inflict greater injuries with the  weapons you know best. You deal 2 additional damage with  weapons and unarmed attacks in which you're an expert.  This damage increases to 3 da |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/8` | 0.563462 | As your envoy level increases, so does your ability to adapt  to new situations. At 9th level and 15th level, increase the  number of skill feats you gain this way by 1. You can use  feats that you te |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/29` | 0.561747 | Your improvisation skills have dramatically improved.  Improvised Mastery triggers on skill checks using a skill that  you don't have legendary proficiency in, rather than master  proficiency, and it |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.542959 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.536278 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.527552 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |

### Query 56
- Text: Summarize Attribute Boosts
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/23', 'PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/448', 'PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/428']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/23', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/22', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/23` | 0.931734 | Attribute Boosts |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/448` | 0.660373 | Attribute boosts, envoy feat, skill feat, skill increase |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/428` | 0.660373 | Attribute boosts, envoy feat, skill feat, skill increase |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/3` | 0.628838 | ATTRIBUTE BOOSTS |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.595513 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/5` | 0.587015 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/24` | 0.585041 | At 5th level and every 5 levels thereafter, your character  boosts four different attribute modifiers. This is described  briefly in the class. For the full details on attribute  modifiers and applyin |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/4` | 0.567872 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/418` | 0.523609 | Ancestry feat, attribute boosts, improvised mastery, perception expertise, skill increase, weapon expertise |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/438` | 0.510543 | Adaptive talent, attribute boosts, general feat, greater weapon specialization, legendary improvisation, reflex mastery, skill increase |

### Query 57
- Text: What is the rule about At 5th level and every 5 levels thereafter, your character  boosts four different attribute modifiers. This is described  briefly in the class. For the full details on attribute  modifiers and applying them during character creation,  see page 23.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/24', 'PZO22001 Starfinder Player Core 098-113::/page/6/Text/5', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/24', 'PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/25', 'PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/24` | 0.996876 | At 5th level and every 5 levels thereafter, your character  boosts four different attribute modifiers. This is described  briefly in the class. For the full details on attribute  modifiers and applyin |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/5` | 0.871960 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.799586 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/4` | 0.727531 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/14` | 0.611428 | This is the attribute modifier that a member of your class  cares about the most. Many of your most useful and  powerful abilities are tied to this attribute in some way. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.600549 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.586391 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 0.582950 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/15` | 0.582900 | For instance, this is the attribute modifier you'll use to  determine the Difficulty Class (DC) associated with your  character's class features and feats. This is called your  class DC. If your chara |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 0.577391 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |

### Query 58
- Text: What is the rule about Ancestry Feats?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/25', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/26', 'PZO22001 Starfinder Player Core 098-113::/page/8/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/25', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/26', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/25` | 0.883515 | Ancestry Feats |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/26` | 0.687185 | This section serves as a reminder of the ancestry feats your  character gains at 5th, 9th, 13th, and 17th levels. Ancestry  feats are detailed in each ancestry entry in Chapter 2, which  begins on pag |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/14` | 0.642420 | In addition to the initial ancestry feat you started with, you  gain an ancestry feat at 5th level and every 4 levels thereafter. |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/18` | 0.562622 | General Feats |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/540` | 0.541824 | Feat |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/590` | 0.541824 | Feat |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/418` | 0.531421 | Ancestry feat, attribute boosts, improvised mastery, perception expertise, skill increase, weapon expertise |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/434` | 0.526222 | Ancestry feat, light armor expertise, skill increase, tactician, weapon mastery |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/442` | 0.519568 | Ancestry feat, greater resolve, incredible senses, inscrutable, skill increase |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/8/SectionHeader/13` | 0.512561 | ANCESTRY FEATS 5TH |

### Query 59
- Text: What is the rule about This section serves as a reminder of the ancestry feats your  character gains at 5th, 9th, 13th, and 17th levels. Ancestry  feats are detailed in each ancestry entry in Chapter 2, which  begins on page 40.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/26', 'PZO22001 Starfinder Player Core 098-113::/page/8/Text/14', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/26', 'PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/3', 'PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/25']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/26` | 0.971642 | This section serves as a reminder of the ancestry feats your  character gains at 5th, 9th, 13th, and 17th levels. Ancestry  feats are detailed in each ancestry entry in Chapter 2, which  begins on pag |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/14` | 0.757589 | In addition to the initial ancestry feat you started with, you  gain an ancestry feat at 5th level and every 4 levels thereafter. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.742748 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.661243 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.660191 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.650118 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/10` | 0.642824 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/25` | 0.621563 | Ancestry Feats |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` | 0.612065 | This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chos |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/Table/2` | 0.572492 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat2Envoy feat, skill feat, skill increase3Adaptive talent, genera |

### Query 60
- Text: Summarize **Envoy** **Page 102**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/3', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/34', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/59']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/3', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/26', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/2/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/3` | 0.996127 | **Envoy** **Page 102** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/34` | 0.760519 | **Envoy** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/59` | 0.760519 | **Envoy** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/51` | 0.718519 | **Envoy** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/41` | 0.718519 | **Envoy** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/24` | 0.718519 | **Envoy** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/33` | 0.718519 | **Envoy** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/29` | 0.718519 | **Envoy** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/1` | 0.629206 | **Sample Envoy** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/30` | 0.519481 | **ENVOY** |

### Query 61
- Text: What is the rule about The envoy is a plucky leader who supports their  allies with battlefield directives, social savviness, and  a suite of skills. Envoys call out directives to their  allies, granting powerful boons that improve if the  envoy performs an action to lead by example. Envoys  are full of sassy quips and always have useful tricks  up their sleeves. Play the envoy if you want to be a  smooth talker with a plethora of skills who helps your  allies win battles and acts as the "face" of the party.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/4', 'PZO22001 Starfinder Player Core 098-113::/page/6/Text/9', 'PZO22001 Starfinder Player Core 098-113::/page/6/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/4', 'PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/3', 'PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/4` | 0.993030 | The envoy is a plucky leader who supports their  allies with battlefield directives, social savviness, and  a suite of skills. Envoys call out directives to their  allies, granting powerful boons that |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/9` | 0.757305 | Envoys encourage their allies with directives. A directive is  an order that benefits allies who follow it. Envoy directives  include a way for the envoy to lead by example by spending  more actions f |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/10` | 0.719824 | You begin with one envoy directive. You can learn more  directives through the envoy class, envoy class feats, and your  leadership style. You can issue one directive a round. Unless  otherwise stated |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/11` | 0.611877 | You issue directives to your allies, granting benefits and letting you take the lead.  Your words and deeds bolster your allies or harry your foes, and your cunning can  get you and your team out of d |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/410` | 0.601567 | Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/27` | 0.593994 | You gain these abilities as an envoy. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/29` | 0.580832 | You've worked with a team for so long that you've learned  to convey orders with a glance, a single word, or the tiniest  flick of your hand (or suitable appendage, depending on  ancestry). Once per t |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/23` | 0.580339 | When you aren't directing allies, you focus on a situation's  shifting circumstances, readying to react. At the end of each of  your turns, you gain one additional reaction, which you can use  before |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/Table/2` | 0.575562 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat2Envoy feat, skill feat, skill increase3Adaptive talent, genera |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/2` | 0.570243 | You'll see the following terms in envoy class features. |

### Query 62
- Text: Summarize **Navasi**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/6', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/7', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/34']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/6', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/4', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/6` | 0.972853 | **Navasi** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/7` | 0.681940 | **Navasi**, the human envoy, is a former space  pirate with a heart of gold. She's got a witty  remark for every occasion and a bullet for  anyone who would hurt one of her friends. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/34` | 0.411305 | **Envoy** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/29` | 0.369304 | **Envoy** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/51` | 0.369304 | **Envoy** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/24` | 0.369304 | **Envoy** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/33` | 0.369304 | **Envoy** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/41` | 0.369304 | **Envoy** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/59` | 0.369304 | **Envoy** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/4` | 0.324019 | **ENVOY** |

### Query 63
- Text: What is the rule about **Navasi**, the human envoy, is a former space  pirate with a heart of gold. She's got a witty  remark for every occasion and a bullet for  anyone who would hurt one of her friends.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/7', 'PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/6', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/7', 'PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/10', 'PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/7` | 0.981583 | **Navasi**, the human envoy, is a former space  pirate with a heart of gold. She's got a witty  remark for every occasion and a bullet for  anyone who would hurt one of her friends. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/6` | 0.597671 | **Navasi** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/4` | 0.558943 | The envoy is a plucky leader who supports their  allies with battlefield directives, social savviness, and  a suite of skills. Envoys call out directives to their  allies, granting powerful boons that |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/9` | 0.448741 | Envoys encourage their allies with directives. A directive is  an order that benefits allies who follow it. Envoy directives  include a way for the envoy to lead by example by spending  more actions f |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/2` | 0.437279 | You'll see the following terms in envoy class features. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/15` | 0.433134 | At every level that you gain an envoy feat, you can select  one of the following feats. You must satisfy any prerequisites  before selecting the feat. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/27` | 0.432535 | You gain these abilities as an envoy. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/41` | 0.431193 | **Envoy** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/51` | 0.431193 | **Envoy** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/33` | 0.431193 | **Envoy** |

### Query 64
- Text: Summarize **Solarian** **Page 138**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/10', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/27', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/37']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/10', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/11', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/10` | 0.995677 | **Solarian** **Page 138** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/27` | 0.811040 | **Solarian** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/37` | 0.811040 | **Solarian** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/62` | 0.769040 | **Solarian** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/32` | 0.769040 | **Solarian** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/44` | 0.769040 | **Solarian** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/54` | 0.769040 | **Solarian** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/35` | 0.769040 | **Solarian** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/11` | 0.503145 | The solarian is a warrior who channels the  cosmic cycle. Every solarian creates weapons of pure  stellar energy that they can manifest at will. Cycling  between graviton and photon attunement, a sola |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/14` | 0.415564 | The pahtra solarian **Dae** loves showing off  by combining their flashy dance moves with  solar flares or turning their battle ribbon into  a electrotether or a whip of solar fire. |

### Query 65
- Text: What is the rule about The solarian is a warrior who channels the  cosmic cycle. Every solarian creates weapons of pure  stellar energy that they can manifest at will. Cycling  between graviton and photon attunement, a solarian's  abilities gain different effects based on their current  state, allowing them to execute incredible combination  attacks. Play the solarian if you want to dash into  close combat and cycle your attacks between powerful  control and damage abilities.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/11', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/46', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/11', 'PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/10', 'PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/11` | 0.976509 | The solarian is a warrior who channels the  cosmic cycle. Every solarian creates weapons of pure  stellar energy that they can manifest at will. Cycling  between graviton and photon attunement, a sola |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/46` | 0.558215 | **INTRODUCTION** **ANCESTRIES & ** **BACKGROUNDS** **CLASSES** **Envoy** **Mystic** **Operative ** **Solarian** **Soldier** **Witchwarper** **Archetypes** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 0.550214 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/35` | 0.499231 | **Solarian** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/54` | 0.499231 | **Solarian** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/44` | 0.499231 | **Solarian** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/62` | 0.499231 | **Solarian** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/32` | 0.499231 | **Solarian** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/27` | 0.499231 | **Solarian** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/37` | 0.499231 | **Solarian** |

### Query 66
- Text: Summarize **Dae**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/13', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/14', 'PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/13', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/11', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/13` | 0.942742 | **Dae** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/14` | 0.581547 | The pahtra solarian **Dae** loves showing off  by combining their flashy dance moves with  solar flares or turning their battle ribbon into  a electrotether or a whip of solar fire. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/10` | 0.417734 | **Feats** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/4` | 0.347542 | **Attributes** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/6` | 0.340903 | **Skills** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/31` | 0.336983 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/56` | 0.336983 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/21` | 0.336983 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/31` | 0.336983 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/1` | 0.336672 | **KEY TERMS** |

### Query 67
- Text: Summarize The pahtra solarian **Dae** loves showing off  by combining their flashy dance moves with  solar flares or turning their battle ribbon into  a electrotether or a whip of solar fire.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/14', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/11', 'PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/14', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/15', 'PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/14` | 1.039924 | The pahtra solarian **Dae** loves showing off  by combining their flashy dance moves with  solar flares or turning their battle ribbon into  a electrotether or a whip of solar fire. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/11` | 0.547232 | The solarian is a warrior who channels the  cosmic cycle. Every solarian creates weapons of pure  stellar energy that they can manifest at will. Cycling  between graviton and photon attunement, a sola |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/13` | 0.539450 | **Dae** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/38` | 0.409588 | The android operative **Iseph** has modified their  body into a perfect weapon, and their gun is an  extension of their hard-earned power and grace. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/35` | 0.397493 | **Solarian** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/37` | 0.397493 | **Solarian** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/62` | 0.397493 | **Solarian** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/44` | 0.397493 | **Solarian** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/54` | 0.397493 | **Solarian** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/32` | 0.397493 | **Solarian** |

### Query 68
- Text: What is the rule about **SKILLS** **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/15']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/9/Text/48', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/66', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/42']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/15', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/17', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/48` | 0.909736 | **SKILLS** **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/66` | 0.909736 | **SKILLS** **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/42` | 0.909736 | **SKILLS** **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/15` | 0.867736 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/58` | 0.867736 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/31` | 0.867736 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/55` | 0.656535 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/36` | 0.613813 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/39` | 0.613813 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16` | 0.593275 | Skill Feats |

### Query 69
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/17']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/32', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/17', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/43']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/17', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/46', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/46` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/32` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/17` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/43` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/49` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/67` | 0.902726 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/40` | 0.902726 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/37` | 0.902726 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/59` | 0.902726 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/64` | 0.421643 | **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/47` | 0.421643 | **INDEX** |

### Query 70
- Text: What is the rule about **INTRODUCTION** **ANCESTRIES & ** **BACKGROUNDS** **CLASSES** **Envoy** **Mystic** **Operative ** **Solarian** **Soldier** **Witchwarper** **Archetypes**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/46']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/46', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/4', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/46', 'PZO22001 Starfinder Player Core 098-113::/page/7/Text/49', 'PZO22001 Starfinder Player Core 098-113::/page/9/Text/39', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/27', 'PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/7/Text/49` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/9/Text/39` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/11/Text/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/46` | 0.863859 | **INTRODUCTION** **ANCESTRIES & ** **BACKGROUNDS** **CLASSES** **Envoy** **Mystic** **Operative ** **Solarian** **Soldier** **Witchwarper** **Archetypes** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 0.644345 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` | 0.599526 | Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  char |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/7` | 0.531567 | **Archetypes** on page 174 gives you thematic options  that allow you to further customize your character's  abilities. Though these rules are not recommended for  beginners, the archetypes in this bo |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/35` | 0.530081 | **Archetypes** **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/22` | 0.527563 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/57` | 0.527563 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/32` | 0.527563 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/65` | 0.518559 | **Archetypes** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/38` | 0.518559 | **Archetypes** |

### Query 71
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/18']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/11/Text/38', 'PZO22001 Starfinder Player Core 098-113::/page/9/Text/50', 'PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/19', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/46']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/46` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/38` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/50` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/18` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/68` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/41` | 0.847304 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/44` | 0.847304 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/60` | 0.847304 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/33` | 0.847304 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/55` | 0.388254 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/15` | 0.332025 | **SKILLS** **FEATS** |

### Query 72
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/19']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/15/Text/42', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/19', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/69']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/19', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/20', 'PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/18']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/42` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/19` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/69` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/51` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/39` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/45` | 0.923000 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/61` | 0.923000 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/34` | 0.923000 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.432722 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44` | 0.426089 | **READY TO ROLL **[free-action] **FEAT 14** |

### Query 73
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/20']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/46', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/20', 'PZO22001 Starfinder Player Core 098-113::/page/9/Text/52']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/20', 'PZO22001 Starfinder Player Core 098-113::/page/7/Text/62', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/19', 'PZO22001 Starfinder Player Core 098-113::/page/15/Text/43', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/21', 'PZO22001 Starfinder Player Core 098-113::/page/9/Text/52', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/35', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/70', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/46', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/40']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/7/Text/62` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/15/Text/43` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/9/Text/52` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/1/Text/35` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/13/Text/70` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/5/Text/46` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/11/Text/40` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/46` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/20` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/52` | 0.983499 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/62` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/43` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/40` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/35` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/70` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/4` | 0.463693 | **Attributes** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/1` | 0.439047 | **KEY TERMS** |

### Query 74
- Text: Summarize **GLOSSARY & **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/21', 'PZO22001 Starfinder Player Core 098-113::/page/7/Text/63', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/36']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/21', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/20', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/47']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/47` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/21` | 0.986628 | **GLOSSARY & ** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/63` | 0.986628 | **GLOSSARY & ** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/36` | 0.872894 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/44` | 0.830894 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/71` | 0.830894 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/47` | 0.830894 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/53` | 0.830894 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/41` | 0.830894 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/32` | 0.373615 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/40` | 0.373615 | **CLASSES** |

### Query 75
- Text: Summarize **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/47']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/7/Text/64', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/47', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/47']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/47', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/22', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/64` | 0.897726 | **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/47` | 0.897726 | **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/47` | 0.648125 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/53` | 0.606125 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/36` | 0.606125 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/41` | 0.606125 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/71` | 0.606125 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/44` | 0.606125 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/31` | 0.449260 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/56` | 0.449260 | **INTRODUCTION** |

### Query 76
- Text: What is the rule about **CHARACTER ** **SHEET**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/22', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/48', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/35']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/22', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/47', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/22` | 0.859300 | **CHARACTER ** **SHEET** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/48` | 0.859300 | **CHARACTER ** **SHEET** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/35` | 0.448576 | **Archetypes** **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 0.394547 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` | 0.394424 | This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chos |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/30` | 0.392353 | **Archetypes** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/65` | 0.392353 | **Archetypes** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/57` | 0.392353 | **Archetypes** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/38` | 0.392353 | **Archetypes** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/47` | 0.392353 | **Archetypes** |

### Query 77
- Text: Summarize **Mystic** **Page 114**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/23', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/25', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/35']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/23', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/24', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/23` | 0.995442 | **Mystic** **Page 114** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/25` | 0.769161 | **Mystic** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/35` | 0.769161 | **Mystic** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/60` | 0.727161 | **Mystic** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/42` | 0.727161 | **Mystic** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/52` | 0.727161 | **Mystic** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/30` | 0.727161 | **Mystic** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/24` | 0.508740 | The mystic is a spellcaster with a connection  to a divine, occult, or primal aspect of the universe. A  mystic casts powerful spells, learning new epiphanies  based on their chosen connection, and he |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/3` | 0.451350 | **Envoy** **Page 102** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/46` | 0.434869 | **INTRODUCTION** **ANCESTRIES & ** **BACKGROUNDS** **CLASSES** **Envoy** **Mystic** **Operative ** **Solarian** **Soldier** **Witchwarper** **Archetypes** |

### Query 78
- Text: What is the rule about The mystic is a spellcaster with a connection  to a divine, occult, or primal aspect of the universe. A  mystic casts powerful spells, learning new epiphanies  based on their chosen connection, and heals allies  using a vitality network that acts as a floating pool of  Hit Points. Play the mystic if you want to be a powerful  spellcaster who also heals your allies through your  supernatural bonds while casting powerful spells.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/24', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/4', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/60']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/24', 'PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/26', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/24` | 0.979827 | The mystic is a spellcaster with a connection  to a divine, occult, or primal aspect of the universe. A  mystic casts powerful spells, learning new epiphanies  based on their chosen connection, and he |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 0.618591 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/60` | 0.581443 | **Mystic** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/35` | 0.539443 | **Mystic** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/25` | 0.539443 | **Mystic** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/42` | 0.539443 | **Mystic** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/52` | 0.539443 | **Mystic** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/30` | 0.539443 | **Mystic** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/41` | 0.496376 | A witchwarper alters reality by drawing on the  infinite possibilities of other universes and timelines.  Every witchwarper is influenced by an event, and they  can harness paradoxical powers to creat |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/46` | 0.472648 | **INTRODUCTION** **ANCESTRIES & ** **BACKGROUNDS** **CLASSES** **Envoy** **Mystic** **Operative ** **Solarian** **Soldier** **Witchwarper** **Archetypes** |

### Query 79
- Text: Summarize **Chk Chk**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/26', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/27', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/56']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/26', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/24', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/26` | 0.943385 | **Chk Chk** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/27` | 0.528501 | The shirren mystic **Chk Chk** worships Zon-Shelyn, the god of creating art from suffering.  He enjoys creatively expressing himself by  writing poetry and dueling enemies with his painglaive. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/56` | 0.421319 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/31` | 0.379319 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/21` | 0.379319 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/31` | 0.379319 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/64` | 0.377511 | **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/47` | 0.377511 | **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/6` | 0.370050 | **Skills** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/36` | 0.354231 | **ENVOY** |

### Query 80
- Text: Summarize The shirren mystic **Chk Chk** worships Zon-Shelyn, the god of creating art from suffering.  He enjoys creatively expressing himself by  writing poetry and dueling enemies with his painglaive.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/27', 'PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/26', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/24']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/27', 'PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/26', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/27` | 1.042959 | The shirren mystic **Chk Chk** worships Zon-Shelyn, the god of creating art from suffering.  He enjoys creatively expressing himself by  writing poetry and dueling enemies with his painglaive. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/26` | 0.517762 | **Chk Chk** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/24` | 0.486968 | The mystic is a spellcaster with a connection  to a divine, occult, or primal aspect of the universe. A  mystic casts powerful spells, learning new epiphanies  based on their chosen connection, and he |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/44` | 0.412462 | **Zemir** the human witchwarper jumps between  realities and timelines, trusting his uncanny  luck and years of experience to keep him  anchored while searching for the loved ones he  lost years ago t |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 0.396665 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/60` | 0.389148 | **Mystic** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/30` | 0.389148 | **Mystic** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/25` | 0.389148 | **Mystic** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/35` | 0.389148 | **Mystic** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/42` | 0.389148 | **Mystic** |

### Query 81
- Text: What is the rule about The soldier is a weapons expert with a mountain  of Hit Points who isn't afraid to get between their allies  and danger. They unleash suppressing attacks with  area weapons that pin foes. They designate a primary  target within their area attacks, granting them extra  shots while firing their heavy weapons. Play a soldier  if you want to control the battlefield with area-of-effect?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/29', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/35', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/29', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/48', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/48` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/29` | 0.985841 | The soldier is a weapons expert with a mountain  of Hit Points who isn't afraid to get between their allies  and danger. They unleash suppressing attacks with  area weapons that pin foes. They designa |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/35` | 0.659201 | The operative brings precision and tactical  training to any situation. In battle, they use the Aim  action to reduce enemy cover and deal extra precision  damage. Some operatives are snipers shooting |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/4` | 0.573228 | The envoy is a plucky leader who supports their  allies with battlefield directives, social savviness, and  a suite of skills. Envoys call out directives to their  allies, granting powerful boons that |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/19` | 0.524822 | You're most comfortable leading your allies from the front lines  of battle while you fight alongside them. You might raise a  shield to help weather the storm of incoming gunfire or simply  lead with |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 0.520601 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/8` | 0.513492 | You assess a foe while in the thick of battle by observing  their reactions to your attack. Make a melee or ranged Strike  against a creature that isn't your asset. On a hit, your target  becomes your |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/10` | 0.509970 | You lead your team by making an impression with firepower.  Your bombastic personality has a barrage of gunfire to back it  up, and you always shoot first. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/11` | 0.502913 | You issue directives to your allies, granting benefits and letting you take the lead.  Your words and deeds bolster your allies or harry your foes, and your cunning can  get you and your team out of d |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/4` | 0.499545 | You're an incredible actor, and you can use your over-thetop bits and dramatic gestures to throw a foe off its game.  If you're wielding a ranged weapon, you can Feint against  an opponent at a range |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/25` | 0.499165 | You call on allies to get out of a threat's area or close on a threat.  Select an enemy within 60 feet. Allies within the target's reach  can Step as a reaction. Allies within 30 feet of you and not |

### Query 82
- Text: What is the rule about attacks while soaking attacks from enemies.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/48']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/48', 'PZO22001 Starfinder Player Core 098-113::/page/7/Text/8', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/27']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/48', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/29', 'PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/31']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/48` | 0.892914 | attacks while soaking attacks from enemies. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/8` | 0.533094 | **Lead by Example** If you used two actions, Hide or Sneak.  Until the start of your next turn, you can Strike the enemy  target as a reaction the first time the ally you targeted attacks  your design |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/27` | 0.515929 | When you warn an ally of an attack, you follow up with a  shot at your enemy. The first time each round you use your  Watch Out reaction, you can make a melee or ranged Strike  against the triggering |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/39` | 0.467482 | You urge your allies to take down your enemies without  incurring any loss of life. Until the beginning of your next  turn, you and your allies can add the nonlethal trait (page  399) to your attacks |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/26` | 0.457511 | **Success** Your attacker is thrown off. It takes a –1 status  penalty to attack rolls against you until the start of its  next turn. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/12` | 0.450628 | You seize the opening your ally has provided, quickly  attacking your foe. Make a Strike against the triggering  creature. If it's a ranged Strike, it must be in your weapon's  first range increment. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/25` | 0.449537 | **Critical Success** Your attacker has second thoughts about  harming you and is thoroughly thrown off. It takes a –2  status penalty to attack and damage rolls against you  until the start of its nex |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/26` | 0.439309 | **Lead by Example** If you used two actions, Strike the target to  focus their attention on you. The target takes a –1 circumstance  penalty on attacks made against other creatures until the start  of |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/14` | 0.437335 | You single out an enemy for you and your allies to focus your  attacks on. Select an enemy within 60 feet that you can see.  You and your allies gain a +1 status bonus to attacks against  that target |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/25` | 0.434374 | You call on allies to get out of a threat's area or close on a threat.  Select an enemy within 60 feet. Allies within the target's reach  can Step as a reaction. Allies within 30 feet of you and not |

### Query 83
- Text: Summarize **Obozaya**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/31', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/32', 'PZO22001 Starfinder Player Core 098-113::/page/7/Text/64']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/31', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/48', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/32']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/48` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/32` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/31` | 0.966083 | **Obozaya** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/32` | 0.661500 | **Obozaya** the vesk soldier doesn't back down,  she opens fire. With big guns, bigger armor,  and her trusty doshko, she becomes a wall of  bulk and bullets in combat. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/64` | 0.335084 | **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/47` | 0.293083 | **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/56` | 0.292910 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/31` | 0.292910 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/21` | 0.292910 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/31` | 0.292910 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/34` | 0.292545 | **Envoy** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/24` | 0.292545 | **Envoy** |

### Query 84
- Text: Summarize **Iseph**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/37', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/38', 'PZO22001 Starfinder Player Core 098-113::/page/7/Text/64']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/37', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/38', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/35']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/38` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/35` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/37` | 0.955016 | **Iseph** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/38` | 0.641189 | The android operative **Iseph** has modified their  body into a perfect weapon, and their gun is an  extension of their hard-earned power and grace. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/64` | 0.398519 | **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/47` | 0.356519 | **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/27` | 0.355471 | Infosphere Director |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/9` | 0.355471 | Infosphere Director |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/65` | 0.338450 | **Archetypes** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/30` | 0.338450 | **Archetypes** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/57` | 0.338450 | **Archetypes** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/41` | 0.338450 | **Archetypes** |

### Query 85
- Text: Summarize **Witchwarper** **Page 162**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/39', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/64', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/39', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/38', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/41']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/38` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/41` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/39` | 1.005718 | **Witchwarper** **Page 162** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/64` | 0.792066 | **Witchwarper** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/29` | 0.792066 | **Witchwarper** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/46` | 0.750066 | **Witchwarper** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/37` | 0.750066 | **Witchwarper** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/34` | 0.750066 | **Witchwarper** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/40` | 0.750066 | **Witchwarper** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/56` | 0.750066 | **Witchwarper** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/46` | 0.483562 | **INTRODUCTION** **ANCESTRIES & ** **BACKGROUNDS** **CLASSES** **Envoy** **Mystic** **Operative ** **Solarian** **Soldier** **Witchwarper** **Archetypes** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/41` | 0.480025 | A witchwarper alters reality by drawing on the  infinite possibilities of other universes and timelines.  Every witchwarper is influenced by an event, and they  can harness paradoxical powers to creat |

### Query 86
- Text: Summarize **Zemir**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/42']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/42', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/44', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/28']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/42', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/41', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/44']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/41` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/44` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/42` | 0.979426 | **Zemir** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/44` | 0.666443 | **Zemir** the human witchwarper jumps between  realities and timelines, trusting his uncanny  luck and years of experience to keep him  anchored while searching for the loved ones he  lost years ago t |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/28` | 0.381292 | **Soldier** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/63` | 0.339292 | **Soldier** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/38` | 0.339292 | **Soldier** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/45` | 0.339292 | **Soldier** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/55` | 0.339292 | **Soldier** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/36` | 0.339292 | **Soldier** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/33` | 0.339292 | **Soldier** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/31` | 0.298040 | **INTRODUCTION** |

### Query 87
- Text: Summarize **Zemir** the human witchwarper jumps between  realities and timelines, trusting his uncanny  luck and years of experience to keep him  anchored while searching for the loved ones he  lost years ago to the perils of infinite worlds.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/44', 'PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/42', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/41']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/44', 'PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/42', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/42` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/44` | 1.039175 | **Zemir** the human witchwarper jumps between  realities and timelines, trusting his uncanny  luck and years of experience to keep him  anchored while searching for the loved ones he  lost years ago t |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/42` | 0.645113 | **Zemir** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/41` | 0.628857 | A witchwarper alters reality by drawing on the  infinite possibilities of other universes and timelines.  Every witchwarper is influenced by an event, and they  can harness paradoxical powers to creat |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 0.518197 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/46` | 0.499090 | **Witchwarper** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/37` | 0.499090 | **Witchwarper** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/29` | 0.499090 | **Witchwarper** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/64` | 0.499090 | **Witchwarper** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/40` | 0.499090 | **Witchwarper** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/34` | 0.499090 | **Witchwarper** |

### Query 88
- Text: Summarize ENVOY
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/1', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/30', 'PZO22001 Starfinder Player Core 098-113::/page/15/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/1', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/44', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/3/Text/44` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/5/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/1` | 0.877104 | ENVOY |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/30` | 0.741586 | **ENVOY** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/14` | 0.741586 | **ENVOY** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/48` | 0.699586 | **ENVOY** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/46` | 0.699586 | **ENVOY** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/41` | 0.699586 | **ENVOY** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/36` | 0.699586 | **ENVOY** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/57` | 0.699586 | **ENVOY** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/9` | 0.699586 | **ENVOY** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/18` | 0.699586 | **ENVOY** |

### Query 89
- Text: Summarize **KEY ATTRIBUTE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/4', 'PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/1']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/4', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/5', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/5/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/4` | 0.948607 | **KEY ATTRIBUTE** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/13` | 0.892782 | KEY ATTRIBUTE |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/1` | 0.665018 | **KEY TERMS** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/4` | 0.557101 | **Attributes** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/10` | 0.471900 | **Feats** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/67` | 0.437617 | **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/44` | 0.437617 | **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/56` | 0.437617 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/64` | 0.407698 | **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/47` | 0.407698 | **INDEX** |

### Query 90
- Text: Summarize **Charisma**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/5', 'PZO22001 Starfinder Player Core 098-113::/page/12/Text/5', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/5', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/6', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/5/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/5` | 0.950174 | **Charisma** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/5` | 0.635784 | Prioritize Charisma. Dexterity, Intelligence, and  Constitution round out your abilities and defenses. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/6` | 0.633154 | At 1st level, your class gives you  an attribute boost to Charisma. |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/18` | 0.500815 | You're an efficient multitasker, and you always have more  than one goal in mind or scheme on the go. You can maintain  twice your Charisma modifier of assets. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/36` | 0.489076 | You can maintain a number of assets equal to your Charisma  modifier. If you Size Up other assets after that, your new asset  replaces a previous one. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/11` | 0.487820 | **Success** The target gains temporary Hit Points equal to their  level plus your Charisma modifier. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/53` | 0.483357 | You motivate an ally within 60 feet to lead by example. As  a free action, that ally can immediately perform the lead  by example actions of your last action, gaining any benefits  and using any abili |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/15` | 0.481397 | **Lead by Example** If you used two actions, Strike the target.  You gain a status bonus to the damage roll equal to your  Charisma modifier. Regardless of whether the Strike hits, you  and your allie |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/40` | 0.480241 | **Lead by Example** If you used two actions, Strike a target with  a nonlethal attack. On a success, you gain a status bonus  to damage equal to your Charisma modifier. On a critical  success, an ally |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/1` | 0.475432 | designated target. Your ally gains a status bonus to damage  equal to your Charisma modifier. |

### Query 91
- Text: Summarize At 1st level, your class gives you  an attribute boost to Charisma.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/6', 'PZO22001 Starfinder Player Core 098-113::/page/6/Text/4', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/6', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/5', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/6` | 1.036234 | At 1st level, your class gives you  an attribute boost to Charisma. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/4` | 0.746204 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.687744 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.641117 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 0.624907 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/15` | 0.614661 | **Lead by Example** If you used two actions, Strike the target.  You gain a status bonus to the damage roll equal to your  Charisma modifier. Regardless of whether the Strike hits, you  and your allie |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/24` | 0.613600 | At 5th level and every 5 levels thereafter, your character  boosts four different attribute modifiers. This is described  briefly in the class. For the full details on attribute  modifiers and applyin |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/29` | 0.609644 | In addition to what you get from your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/7` | 0.600917 | At 1st level, you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start  of this class. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/16` | 0.593469 | Most classes are associated with one key attribute  modifier, but some allow you to choose from two options.  For instance, if you're a witchwarper, you can choose  either Intelligence or Charisma as |

### Query 92
- Text: Summarize You increase your maximum number  of HP by this number at 1st level and  every level thereafter.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/9', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/2', 'PZO22001 Starfinder Player Core 098-113::/page/8/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/9', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/9` | 1.031874 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 0.684095 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/3` | 0.622228 | You gain more skill increases than members of other classes.  At 2nd level and every level thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you' |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.568684 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` | 0.566391 | This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chos |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/5` | 0.562495 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/6` | 0.547775 | **Leveling Up **on page 29 tells you how to make your  character stronger when you get enough Experience  Points to reach a new level. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/24` | 0.543121 | At 5th level and every 5 levels thereafter, your character  boosts four different attribute modifiers. This is described  briefly in the class. For the full details on attribute  modifiers and applyin |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.538297 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.531560 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |

### Query 93
- Text: Summarize DURING COMBAT ENCOUNTERS...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/12', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/11', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/5/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/5/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10` | 0.983036 | DURING COMBAT ENCOUNTERS... |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/12` | 0.745777 | DURING SOCIAL ENCOUNTERS... |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/14` | 0.434305 | WHILE EXPLORING... |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/16` | 0.337787 | IN DOWNTIME... |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/46` | 0.334433 | **INTRODUCTION** **ANCESTRIES & ** **BACKGROUNDS** **CLASSES** **Envoy** **Mystic** **Operative ** **Solarian** **Soldier** **Witchwarper** **Archetypes** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/55` | 0.333292 | **Soldier** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/33` | 0.333292 | **Soldier** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/63` | 0.333292 | **Soldier** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/36` | 0.333292 | **Soldier** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/28` | 0.333292 | **Soldier** |

### Query 94
- Text: Summarize You issue directives to your allies, granting benefits and letting you take the lead.  Your words and deeds bolster your allies or harry your foes, and your cunning can  get you and your team out of danger.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/11', 'PZO22001 Starfinder Player Core 098-113::/page/6/Text/19', 'PZO22001 Starfinder Player Core 098-113::/page/7/Text/36']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/11', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/11` | 1.035962 | You issue directives to your allies, granting benefits and letting you take the lead.  Your words and deeds bolster your allies or harry your foes, and your cunning can  get you and your team out of d |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/19` | 0.761544 | You're most comfortable leading your allies from the front lines  of battle while you fight alongside them. You might raise a  shield to help weather the storm of incoming gunfire or simply  lead with |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/36` | 0.728814 | You step up to lead during difficult times. You might have  experienced a traumatic event, perhaps escaping a pirate ship  during a mutiny, or you fought in some notorious battle. Your  allies trust y |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/9` | 0.672162 | Envoys encourage their allies with directives. A directive is  an order that benefits allies who follow it. Envoy directives  include a way for the envoy to lead by example by spending  more actions f |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/13` | 0.663187 | You're often the face for your team, whether you use diplomacy, lies, threats, or  whatever words it takes to get your way. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/3` | 0.662953 | **Directive**: Actions with this trait are special orders  that provide benefits for your allies if they follow  them. Your allies must be able to sense you to benefit  from your directives. This acti |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/2` | 0.654674 | You prefer to direct your allies in subtle ways, without drawing  much attention from foes. You might sneak in behind your  bodyguards or support your team from a safe distance. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/15` | 0.633358 | People follow your lead because you help push them to  their ultimate potential. Each of your allies gain a second  reaction if they start their turn within 100 feet of you and  can perceive you. This |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/54` | 0.621957 | You provide a quick follow-up to your ongoing directive,  encouraging your ally when they successfully hit your |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/48` | 0.608408 | You instinctively react to trouble by directing your allies to  act at the exact moment their intervention would matter  most. Issue a 1-action directive. |

### Query 95
- Text: Summarize DURING SOCIAL ENCOUNTERS...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/12', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/12', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/13', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/5/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/5/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/12` | 0.977694 | DURING SOCIAL ENCOUNTERS... |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10` | 0.728104 | DURING COMBAT ENCOUNTERS... |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/14` | 0.408727 | WHILE EXPLORING... |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/ListItem/24` | 0.318637 | Ask for your help navigating complex social situations. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/1` | 0.316759 | **Sample Envoy** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/16` | 0.315217 | IN DOWNTIME... |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/410` | 0.290848 | Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/22` | 0.286287 | OTHERS PROBABLY... |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/18` | 0.285896 | YOU MIGHT... |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/2` | 0.285324 | You'll see the following terms in envoy class features. |

### Query 96
- Text: Summarize WHILE EXPLORING...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/14', 'PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/31', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/14', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/15', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/5/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/5/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/14` | 0.945993 | WHILE EXPLORING... |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/31` | 0.498237 | **CONCENTRATE** **ENVOY** **EXPLORATION** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/12` | 0.439598 | DURING SOCIAL ENCOUNTERS... |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10` | 0.395469 | DURING COMBAT ENCOUNTERS... |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/16` | 0.348777 | IN DOWNTIME... |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/69` | 0.330508 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/34` | 0.330508 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/19` | 0.330508 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/39` | 0.330508 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/61` | 0.330508 | **PLAYING THE ** **GAME** |

### Query 97
- Text: Summarize IN DOWNTIME...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/16', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/16', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/15', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/5/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/5/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/16` | 0.786911 | IN DOWNTIME... |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/18` | 0.405938 | YOU MIGHT... |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/12` | 0.367088 | DURING SOCIAL ENCOUNTERS... |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/14` | 0.322232 | WHILE EXPLORING... |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10` | 0.314851 | DURING COMBAT ENCOUNTERS... |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/31` | 0.312555 | **DIGITAL ASSESSMENT! **[one-action]** TO **[two-actions] |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Table/3` | 0.304774 | FeatLevelAcquire Asset2Change of Plans2Cheer Up8Confounding Disquisition8Cut 'Em Deep10Dirty Retort6Distant Feint6Diverse Schemes4Don't You Die on Me2Down to the Wire14Effortless Influencer16Endlessly |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/22` | 0.302606 | OTHERS PROBABLY... |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/1` | 0.290227 | **Sample Envoy** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/1` | 0.287179 | **KEY TERMS** |

### Query 98
- Text: Summarize You look for new opportunities to make a name for yourself, work your way up  through the ranks of an organization, or establish an enterprise of your own.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/17', 'PZO22001 Starfinder Player Core 098-113::/page/5/ListItem/19', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/17', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/17` | 1.026414 | You look for new opportunities to make a name for yourself, work your way up  through the ranks of an organization, or establish an enterprise of your own. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/ListItem/19` | 0.596417 | Aspire to lead a business or military organization, or captain a starship. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/13` | 0.539362 | You're often the face for your team, whether you use diplomacy, lies, threats, or  whatever words it takes to get your way. |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/11` | 0.492895 | You issue directives to your allies, granting benefits and letting you take the lead.  Your words and deeds bolster your allies or harry your foes, and your cunning can  get you and your team out of d |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/2` | 0.483847 | You're a master influencer. You make your way in the universe with a charming smile, quick wit, and keen  sense of self-preservation. You're a leader who motivates your teammates, pushes them past the |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/17` | 0.464412 | Whether it comes naturally, or you trained for it, you've  developed a personal style of leading others. At 1st level,  select a leadership style. You become trained in the indicated  leadership skill |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/8` | 0.458498 | Your savvy and skill are unparalleled. No matter the situation,  you quickly course correct to set the tone you need to succeed.  You gain the following action. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/18` | 0.447905 | Whether through conversation, clever lies, dazzling  performances, or threats, you rely on charm and cunning to  influence others. You crave being in the spotlight. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/33` | 0.445462 | You spend 1 minute observing a specific individual, 10 minutes  researching a specific individual on the infosphere, or 1 hour  networking and gathering information. This subject is your  asset. If yo |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` | 0.438485 | Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  char |

### Query 99
- Text: Summarize YOU MIGHT...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/22', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/632']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/5/ListItem/19', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/5/ListItem/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/5/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/18` | 0.903204 | YOU MIGHT... |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/22` | 0.522471 | OTHERS PROBABLY... |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/632` | 0.475669 | You Can Do It |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49` | 0.362140 | **YOU CAN DO IT **[one-action] **FEAT 14** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/ListItem/25` | 0.331310 | Assume you like being in charge. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/16` | 0.320798 | IN DOWNTIME... |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/14` | 0.315405 | WHILE EXPLORING... |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/Table/16` | 0.303640 | FeatLevelInfluence4Look Alive8Master Plan14Not in the Face4Pardon Me1Quip1Ready to Roll14Saw it Coming4Search High and Low!2Secondary Directive12Size Up1Sidestep8Situational Awareness12Smooth Diversio |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10` | 0.303473 | DURING COMBAT ENCOUNTERS... |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/25` | 0.299568 | **Lead by Example** If you used two actions, you and your  selected ally count any enemies that you both threaten as |

### Query 100
- Text: Lookup values for Your LevelClass Features1Ancestry and background, attribute boosts,
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/6/Table/2']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/10', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/29', 'PZO22001 Starfinder Player Core 098-113::/page/6/Table/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/6/Table/2', 'PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/1', 'PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/407']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/407` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.752424 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/29` | 0.671822 | In addition to what you get from your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/6/Table/2` | 0.656263 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat2Envoy feat, skill feat, skill increase3Adaptive talent, genera |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.606271 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.597046 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/24` | 0.583524 | At 5th level and every 5 levels thereafter, your character  boosts four different attribute modifiers. This is described  briefly in the class. For the full details on attribute  modifiers and applyin |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/4` | 0.582096 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/26` | 0.560513 | This section serves as a reminder of the ancestry feats your  character gains at 5th, 9th, 13th, and 17th levels. Ancestry  feats are detailed in each ancestry entry in Chapter 2, which  begins on pag |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/10` | 0.554157 | from their class features; and more. Your character's class  entry also provides the information needed when they  gain levels, so it will be a vital reference throughout the  course of your campaign. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.551533 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |

### Query 101
- Text: What are the requirements for **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17', 'PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17', 'PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/19', 'PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.924859 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.774382 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.696863 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22` | 0.645563 | **SEARCH HIGH AND LOW! **[one-action]** TO **[two-actions] **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12` | 0.641147 | **GET 'EM! **[one-action]** TO **[two-actions] |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.609156 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/22` | 0.599969 | **DANCE PARTNER! **[one-action]** TO **[two-actions] |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/39` | 0.583373 | **KEEP ON KEEPING ON!** [one-action]** TO **[two-actions] |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/9/SectionHeader/3` | 0.567084 | **STEEL YOURSELVES! **[one-action]** TO **[two-actions] |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.558932 | **READY ARMS! **[one-action]** TO **[two-actions] |

### Query 102
- Text: What are the requirements for **PARDON ME** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/21', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/600', 'PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/21', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/20', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/10/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/10/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/21` | 0.855293 | **PARDON ME** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/600` | 0.566357 | Pardon Me |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/13` | 0.459695 | **DON'T YOU DIE ON ME **[one-action] **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/30` | 0.413731 | **SIZE UP** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49` | 0.392815 | **YOU CAN DO IT **[one-action] **FEAT 14** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.391130 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.382128 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/15` | 0.379862 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/48` | 0.379862 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/42` | 0.379862 | **SKILLS** **FEATS** |

### Query 103
- Text: What are the requirements for **Prerequisites** trained in Deception?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/23', 'PZO22001 Starfinder Player Core 098-113::/page/12/Text/22', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/23', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/22', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/10/Text/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/10/Text/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/23` | 0.939915 | **Prerequisites** trained in Deception |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/22` | 0.939915 | **Prerequisites** trained in Deception |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/5` | 0.825207 | **Prerequisites** master in Deception |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25` | 0.781085 | **Prerequisites** trained in Deception or Diplomacy |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/56` | 0.614230 | Trained in one of the following skills  of your choice: Deception, Diplomacy,  Intimidation |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.540704 | **Prerequisites** trained in Intimidation |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/20` | 0.483588 | **Prerequisites** trained in Medicine |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/33` | 0.472149 | **Trigger** You're about to roll a Deception, Diplomacy, or  Intimidation check, but you haven't rolled yet. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/12` | 0.466712 | **Trigger** You roll a skill check for any of the following skills  you're legendary in: Deception, Diplomacy, Intimidation, or  your leadership skill. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/24` | 0.434834 | You distract your foes with a clever comment as you maneuver  around them. You can use Deception instead of Acrobatics to  Tumble Through using the target's Will DC instead of Reflex  DC. When you suc |

### Query 104
- Text: What are the requirements for **QUIP **[reaction] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/26', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/41', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/602']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/26', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/27', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/25']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/10/Text/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/10/Text/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/26` | 0.867703 | **QUIP **[reaction] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.544151 | **WATCH OUT **[reaction] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/602` | 0.505588 | Quip |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/30` | 0.424018 | **SIZE UP** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29` | 0.421499 | **INFLUENCE **[reaction] **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/8` | 0.419777 | **TAG TEAM **[reaction] **FEAT 10** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/15` | 0.419397 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/42` | 0.419397 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/66` | 0.419397 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/48` | 0.419397 | **SKILLS** **FEATS** |

### Query 105
- Text: What are the requirements for **Prerequisites** trained in Intimidation?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/28', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/46', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/56']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/28', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/29', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/10/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/10/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.969563 | **Prerequisites** trained in Intimidation |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/46` | 0.858302 | **Prerequisites** master in Intimidation |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/56` | 0.638324 | Trained in one of the following skills  of your choice: Deception, Diplomacy,  Intimidation |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/22` | 0.506454 | **Prerequisites** trained in Deception |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/23` | 0.506454 | **Prerequisites** trained in Deception |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/19` | 0.491412 | **Prerequisites **Improvised Mastery |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/20` | 0.479320 | **Prerequisites** trained in Medicine |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25` | 0.475416 | **Prerequisites** trained in Deception or Diplomacy |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/58` | 0.449717 | **Prerequisites** Influence |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/33` | 0.441632 | **Trigger** You're about to roll a Deception, Diplomacy, or  Intimidation check, but you haven't rolled yet. |

### Query 106
- Text: What are the requirements for **SIZE UP** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/30', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/7', 'PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/30', 'PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/31', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/10/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/30` | 0.847115 | **SIZE UP** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/7` | 0.731012 | **Prerequisites** Size Up |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17` | 0.731012 | **Prerequisites** Size Up |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/612` | 0.539422 | Size Up |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18` | 0.431322 | **CHEER UP **[one-action] **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.409369 | **WATCH OUT **[reaction] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/66` | 0.397664 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/42` | 0.397664 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/48` | 0.397664 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/15` | 0.397664 | **SKILLS** **FEATS** |

### Query 107
- Text: What are the requirements for **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37', 'PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12', 'PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/36', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/38']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/10/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/10/Text/38` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.918802 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12` | 0.731100 | **GET 'EM! **[one-action]** TO **[two-actions] |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.697598 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.598473 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.588249 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/39` | 0.578473 | **KEEP ON KEEPING ON!** [one-action]** TO **[two-actions] |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22` | 0.568748 | **SEARCH HIGH AND LOW! **[one-action]** TO **[two-actions] **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/622` | 0.567737 | Take 'Em Alive! |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.566464 | **READY ARMS! **[one-action]** TO **[two-actions] |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/9/SectionHeader/3` | 0.556465 | **STEEL YOURSELVES! **[one-action]** TO **[two-actions] |

### Query 108
- Text: What are the requirements for **WATCH OUT **[reaction] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/41', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/41', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/40', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/42']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/10/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/10/Text/42` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.853956 | **WATCH OUT **[reaction] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34` | 0.663665 | **Prerequisites** Watch Out |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/26` | 0.663665 | **Prerequisites** Watch Out |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/27` | 0.529816 | When you warn an ally of an attack, you follow up with a  shot at your enemy. The first time each round you use your  Watch Out reaction, you can make a melee or ranged Strike  against the triggering |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/630` | 0.518903 | Watch Out |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.509428 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/30` | 0.496593 | **SIZE UP** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/26` | 0.478866 | **QUIP **[reaction] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.475776 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29` | 0.453836 | **INFLUENCE **[reaction] **FEAT 4** |

### Query 109
- Text: Lookup values for FeatLevelAcquire Asset2Change of Plans2Cheer Up8Confounding Disquisition8Cut 'Em Deep10Dirty Retort6Distant Feint6Diverse Schemes4Don't You Die on Me2Down to the Wire14Effortless Influencer16Endlessly Adaptive20Extend Directive16Fast Synergy18Get in There!2Get Them!16Go to Ground!1Got 'Em!10Hang in There6Hurry6Improvised Legend18
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/Table/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/11/Table/3', 'PZO22001 Starfinder Player Core 098-113::/page/11/Table/16', 'PZO22001 Starfinder Player Core 098-113::/page/6/Table/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/Table/3', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/540', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/540` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/11/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/Table/3` | 0.991736 | FeatLevelAcquire Asset2Change of Plans2Cheer Up8Confounding Disquisition8Cut 'Em Deep10Dirty Retort6Distant Feint6Diverse Schemes4Don't You Die on Me2Down to the Wire14Effortless Influencer16Endlessly |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/Table/16` | 0.771192 | FeatLevelInfluence4Look Alive8Master Plan14Not in the Face4Pardon Me1Quip1Ready to Roll14Saw it Coming4Search High and Low!2Secondary Directive12Size Up1Sidestep8Situational Awareness12Smooth Diversio |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/6/Table/2` | 0.622419 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat2Envoy feat, skill feat, skill increase3Adaptive talent, genera |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/11` | 0.522497 | Size Up (1st), Acquire Asset (2nd), Influence (4th),  Smooth Diversions (10th) |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/2` | 0.513431 | Use this table to look up envoy feats by name. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.509774 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22` | 0.501426 | **SEARCH HIGH AND LOW! **[one-action]** TO **[two-actions] **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/10` | 0.497342 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/26` | 0.495178 | This section serves as a reminder of the ancestry feats your  character gains at 5th, 9th, 13th, and 17th levels. Ancestry  feats are detailed in each ancestry entry in Chapter 2, which  begins on pag |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/438` | 0.492423 | Adaptive talent, attribute boosts, general feat, greater weapon specialization, legendary improvisation, reflex mastery, skill increase |

### Query 110
- Text: Lookup values for 2ND LEVEL
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/Table/4']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/584', 'PZO22001 Starfinder Player Core 098-113::/page/11/Table/4', 'PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/Table/4', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/583', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/584']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/583` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/584` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/584` | 0.833333 | 2ND LEVEL |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/Table/4` | 0.833333 | 2ND LEVEL |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/13` | 0.579044 | 4TH LEVEL |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/541` | 0.530150 | Level |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/591` | 0.530150 | Level |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/13` | 0.520689 | 12TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/42` | 0.509256 | 10TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/21` | 0.504999 | 20TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/17` | 0.504040 | 8TH LEVEL |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/11` | 0.503436 | 18TH LEVEL |

### Query 111
- Text: What are the requirements for **ACQUIRE ASSET **[one-action] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/5', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/542', 'PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/5', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/6', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/584']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/11/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/584` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/5` | 0.927609 | **ACQUIRE ASSET **[one-action] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/542` | 0.665736 | Acquire Asset |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.621106 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/35` | 0.523173 | You gain the benefits of the 2-action Get 'Em! when using  1-action Get 'Em! on an asset. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12` | 0.522556 | **GET 'EM! **[one-action]** TO **[two-actions] |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22` | 0.503984 | **SEARCH HIGH AND LOW! **[one-action]** TO **[two-actions] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/31` | 0.499056 | **DIGITAL ASSESSMENT! **[one-action]** TO **[two-actions] |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.498641 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.483088 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.466870 | **READY ARMS! **[one-action]** TO **[two-actions] |

### Query 112
- Text: What are the requirements for **Prerequisites** Size Up?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/11/Text/7', 'PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/612']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/Text/7', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/6', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/11/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/11/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/7` | 0.944197 | **Prerequisites** Size Up |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17` | 0.944197 | **Prerequisites** Size Up |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/612` | 0.688560 | Size Up |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/30` | 0.516979 | **SIZE UP** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/26` | 0.452250 | **Prerequisites** Watch Out |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34` | 0.452250 | **Prerequisites** Watch Out |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/58` | 0.445625 | **Prerequisites** Influence |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/25` | 0.404944 | **Prerequisites** adaptive talent |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/20` | 0.385864 | **Prerequisites** trained in Medicine |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/6` | 0.381336 | **Leveling Up **on page 29 tells you how to make your  character stronger when you get enough Experience  Points to reach a new level. |

### Query 113
- Text: What are the requirements for **CHANGE OF PLANS **[reaction] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/9', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/544', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/39']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/9', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/8', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/11/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/11/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/9` | 0.900558 | **CHANGE OF PLANS **[reaction] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/544` | 0.626847 | Change of Plans |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/39` | 0.516779 | **MASTER PLAN** **FEAT 14** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.474739 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/43` | 0.469949 | **New Plan** [reaction] (fortune, linguistic) **Trigger** An ally you  reviewed stratagems with is about to attempt an attack  roll or skill check; **Effect** The ally rolls the triggering  check twic |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22` | 0.461718 | **SEARCH HIGH AND LOW! **[one-action]** TO **[two-actions] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.461283 | **WATCH OUT **[reaction] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/5` | 0.456277 | **ACQUIRE ASSET **[one-action] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/19` | 0.453066 | **SITUATIONAL AWARENESS **[two-actions] **FEAT 12** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29` | 0.446879 | **INFLUENCE **[reaction] **FEAT 4** |

### Query 114
- Text: What are the requirements for **DON'T YOU DIE ON ME **[one-action] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/13', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/558', 'PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/13', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/12', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/11/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/11/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/13` | 0.878931 | **DON'T YOU DIE ON ME **[one-action] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/558` | 0.656463 | Don't You Die on Me |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.586233 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.543597 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49` | 0.522325 | **YOU CAN DO IT **[one-action] **FEAT 14** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.484447 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/39` | 0.475836 | **KEEP ON KEEPING ON!** [one-action]** TO **[two-actions] |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/22` | 0.473733 | **DANCE PARTNER! **[one-action]** TO **[two-actions] |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22` | 0.471489 | **SEARCH HIGH AND LOW! **[one-action]** TO **[two-actions] **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/17` | 0.466213 | value to 0, they lose the dying condition, don't increase their  wounded condition, and remain unconscious. The targeted ally  then becomes temporarily immune to Don't You Die on Me for  1 hour. |

### Query 115
- Text: Lookup values for FeatLevelInfluence4Look Alive8Master Plan14Not in the Face4Pardon Me1Quip1Ready to Roll14Saw it Coming4Search High and Low!2Secondary Directive12Size Up1Sidestep8Situational Awareness12Smooth Diversions10Tag Team10Take 'Em Alive!1That'll Show 'Em12True Leader20Unstoppable Directives12Watch Out1You Can Do It14
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/Table/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/11/Table/16', 'PZO22001 Starfinder Player Core 098-113::/page/11/Table/3', 'PZO22001 Starfinder Player Core 098-113::/page/6/Table/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/Table/16', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/590', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/590` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/11/Text/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/Table/16` | 0.980709 | FeatLevelInfluence4Look Alive8Master Plan14Not in the Face4Pardon Me1Quip1Ready to Roll14Saw it Coming4Search High and Low!2Secondary Directive12Size Up1Sidestep8Situational Awareness12Smooth Diversio |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/Table/3` | 0.759963 | FeatLevelAcquire Asset2Change of Plans2Cheer Up8Confounding Disquisition8Cut 'Em Deep10Dirty Retort6Distant Feint6Diverse Schemes4Don't You Die on Me2Down to the Wire14Effortless Influencer16Endlessly |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/6/Table/2` | 0.592071 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat2Envoy feat, skill feat, skill increase3Adaptive talent, genera |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/2` | 0.512183 | Use this table to look up envoy feats by name. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22` | 0.486779 | **SEARCH HIGH AND LOW! **[one-action]** TO **[two-actions] **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/3` | 0.478051 | **Directive**: Actions with this trait are special orders  that provide benefits for your allies if they follow  them. Your allies must be able to sense you to benefit  from your directives. This acti |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/12` | 0.472576 | **Leadership Perk **You gain Incredible Initiative as a bonus feat. **Leadership Directive **Ready Arms! |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/10` | 0.472076 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.466593 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.461682 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |

### Query 116
- Text: What are the requirements for **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23', 'PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/19', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/11/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/11/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.925791 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.724304 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.723433 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12` | 0.680513 | **GET 'EM! **[one-action]** TO **[two-actions] |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22` | 0.660765 | **SEARCH HIGH AND LOW! **[one-action]** TO **[two-actions] **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.630355 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/39` | 0.594332 | **KEEP ON KEEPING ON!** [one-action]** TO **[two-actions] |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/22` | 0.578859 | **DANCE PARTNER! **[one-action]** TO **[two-actions] |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/9/SectionHeader/3` | 0.566249 | **STEEL YOURSELVES! **[one-action]** TO **[two-actions] |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.566106 | **READY ARMS! **[one-action]** TO **[two-actions] |

### Query 117
- Text: What are the requirements for **SEARCH HIGH AND LOW! **[one-action]** TO **[two-actions] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22', 'PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/608']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/21', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/11/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/11/Text/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22` | 0.932072 | **SEARCH HIGH AND LOW! **[one-action]** TO **[two-actions] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.692114 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/608` | 0.652233 | Search High and Low! |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.604428 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.584399 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12` | 0.580764 | **GET 'EM! **[one-action]** TO **[two-actions] |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/39` | 0.554754 | **KEEP ON KEEPING ON!** [one-action]** TO **[two-actions] |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/31` | 0.545921 | **DIGITAL ASSESSMENT! **[one-action]** TO **[two-actions] |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.541570 | **READY ARMS! **[one-action]** TO **[two-actions] |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/22` | 0.536952 | **DANCE PARTNER! **[one-action]** TO **[two-actions] |

### Query 118
- Text: What are the requirements for **DIVERSE SCHEMES** **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/14', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/556', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/66']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/14', 'PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/13', 'PZO22001 Starfinder Player Core 098-113::/page/12/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/12/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/14` | 0.882155 | **DIVERSE SCHEMES** **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/556` | 0.580472 | Diverse Schemes |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/66` | 0.451345 | **SKILLS** **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/48` | 0.409345 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/42` | 0.409345 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/15` | 0.409345 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/58` | 0.409345 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/31` | 0.409345 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29` | 0.404015 | **INFLUENCE **[reaction] **FEAT 4** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/10` | 0.400785 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |

### Query 119
- Text: What are the requirements for **Prerequisites** Size Up?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/11/Text/7', 'PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/612']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17', 'PZO22001 Starfinder Player Core 098-113::/page/12/Text/18', 'PZO22001 Starfinder Player Core 098-113::/page/12/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/12/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/12/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/7` | 0.944197 | **Prerequisites** Size Up |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17` | 0.944197 | **Prerequisites** Size Up |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/612` | 0.688560 | Size Up |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/30` | 0.516979 | **SIZE UP** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/26` | 0.452250 | **Prerequisites** Watch Out |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34` | 0.452250 | **Prerequisites** Watch Out |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/58` | 0.445625 | **Prerequisites** Influence |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/25` | 0.404944 | **Prerequisites** adaptive talent |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/20` | 0.385864 | **Prerequisites** trained in Medicine |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/6` | 0.381336 | **Leveling Up **on page 29 tells you how to make your  character stronger when you get enough Experience  Points to reach a new level. |

### Query 120
- Text: What are the requirements for **NOT IN THE FACE **[reaction] **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/19', 'PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/598']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/19', 'PZO22001 Starfinder Player Core 098-113::/page/12/Text/18', 'PZO22001 Starfinder Player Core 098-113::/page/12/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/12/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/12/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/19` | 0.883918 | **NOT IN THE FACE **[reaction] **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29` | 0.625156 | **INFLUENCE **[reaction] **FEAT 4** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/598` | 0.535038 | Not in the Face |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/35` | 0.469678 | **SAW IT COMING **[free-action] **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.457236 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/37` | 0.454525 | **SIDESTEP **[reaction] **FEAT 8** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.446622 | **WATCH OUT **[reaction] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/13` | 0.436045 | **DON'T YOU DIE ON ME **[one-action] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49` | 0.435712 | **YOU CAN DO IT **[one-action] **FEAT 14** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/34` | 0.435406 | **DOWN TO THE WIRE **[reaction] **FEAT 14** |

### Query 121
- Text: What are the requirements for **Prerequisites** trained in Deception?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/12/Text/22']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/23', 'PZO22001 Starfinder Player Core 098-113::/page/12/Text/22', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/12/Text/22', 'PZO22001 Starfinder Player Core 098-113::/page/12/Text/21', 'PZO22001 Starfinder Player Core 098-113::/page/12/Text/23']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/12/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/12/Text/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/23` | 0.939915 | **Prerequisites** trained in Deception |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/22` | 0.939915 | **Prerequisites** trained in Deception |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/5` | 0.825207 | **Prerequisites** master in Deception |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25` | 0.781085 | **Prerequisites** trained in Deception or Diplomacy |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/56` | 0.614230 | Trained in one of the following skills  of your choice: Deception, Diplomacy,  Intimidation |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.540704 | **Prerequisites** trained in Intimidation |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/20` | 0.483588 | **Prerequisites** trained in Medicine |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/33` | 0.472149 | **Trigger** You're about to roll a Deception, Diplomacy, or  Intimidation check, but you haven't rolled yet. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/12` | 0.466712 | **Trigger** You roll a skill check for any of the following skills  you're legendary in: Deception, Diplomacy, Intimidation, or  your leadership skill. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/24` | 0.434834 | You distract your foes with a clever comment as you maneuver  around them. You can use Deception instead of Acrobatics to  Tumble Through using the target's Will DC instead of Reflex  DC. When you suc |

### Query 122
- Text: What are the requirements for **INFLUENCE **[reaction] **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/58', 'PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29', 'PZO22001 Starfinder Player Core 098-113::/page/12/Text/28', 'PZO22001 Starfinder Player Core 098-113::/page/12/Text/31']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/12/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/12/Text/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29` | 0.912397 | **INFLUENCE **[reaction] **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/58` | 0.711999 | **Prerequisites** Influence |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/19` | 0.622960 | **NOT IN THE FACE **[reaction] **FEAT 4** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/2` | 0.543046 | **INFLUENCER** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/592` | 0.537341 | Influence |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/55` | 0.493386 | **EFFORTLESS INFLUENCER** **FEAT 16** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.456081 | **WATCH OUT **[reaction] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/35` | 0.446759 | **SAW IT COMING **[free-action] **FEAT 4** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/Table/16` | 0.445721 | FeatLevelInfluence4Look Alive8Master Plan14Not in the Face4Pardon Me1Quip1Ready to Roll14Saw it Coming4Search High and Low!2Secondary Directive12Size Up1Sidestep8Situational Awareness12Smooth Diversio |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/37` | 0.438741 | **SIDESTEP **[reaction] **FEAT 8** |

### Query 123
- Text: What are the requirements for **SAW IT COMING **[free-action] **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/35']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/35', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/35', 'PZO22001 Starfinder Player Core 098-113::/page/12/Text/34', 'PZO22001 Starfinder Player Core 098-113::/page/12/Text/37']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/12/Text/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/12/Text/37` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/35` | 0.890048 | **SAW IT COMING **[free-action] **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44` | 0.544293 | **READY TO ROLL **[free-action] **FEAT 14** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49` | 0.508338 | **YOU CAN DO IT **[one-action] **FEAT 14** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/49` | 0.449263 | **GOT 'EM **[free-action] **FEAT 10** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.446219 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/19` | 0.445372 | **NOT IN THE FACE **[reaction] **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29` | 0.434177 | **INFLUENCE **[reaction] **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.431641 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/Table/16` | 0.430134 | FeatLevelInfluence4Look Alive8Master Plan14Not in the Face4Pardon Me1Quip1Ready to Roll14Saw it Coming4Search High and Low!2Secondary Directive12Size Up1Sidestep8Situational Awareness12Smooth Diversio |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/606` | 0.425483 | Saw it Coming |

### Query 124
- Text: What are the requirements for **DIRTY RETORT **[reaction] **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/41', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/552', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/41', 'PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/40', 'PZO22001 Starfinder Player Core 098-113::/page/12/Text/43']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/12/Text/43` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/41` | 0.887243 | **DIRTY RETORT **[reaction] **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/552` | 0.580271 | Dirty Retort |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/14` | 0.519840 | **HURRY **[one-action] **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/2` | 0.457762 | **DISTANT FEINT** **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.444228 | **WATCH OUT **[reaction] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/37` | 0.442220 | **SIDESTEP **[reaction] **FEAT 8** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/19` | 0.434243 | **NOT IN THE FACE **[reaction] **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44` | 0.406656 | **READY TO ROLL **[free-action] **FEAT 14** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/8` | 0.400926 | **TAG TEAM **[reaction] **FEAT 10** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/5` | 0.398874 | **HANG IN THERE **[one-action] **FEAT 6** |

### Query 125
- Text: What are the requirements for **DISTANT FEINT** **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/2', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/554', 'PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/41']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/2', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/3', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/13/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/2` | 0.901171 | **DISTANT FEINT** **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/554` | 0.666106 | Distant Feint |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/41` | 0.483818 | **DIRTY RETORT **[reaction] **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/4` | 0.421490 | You're an incredible actor, and you can use your over-thetop bits and dramatic gestures to throw a foe off its game.  If you're wielding a ranged weapon, you can Feint against  an opponent at a range |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/14` | 0.420136 | **HURRY **[one-action] **FEAT 6** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/58` | 0.407731 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/31` | 0.407731 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/42` | 0.407731 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/66` | 0.407731 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/15` | 0.407731 | **SKILLS** **FEATS** |

### Query 126
- Text: What are the requirements for **HANG IN THERE **[one-action] **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/5', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/14', 'PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/5', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/4', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/13/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/5` | 0.900749 | **HANG IN THERE **[one-action] **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/14` | 0.671191 | **HURRY **[one-action] **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.607646 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/12` | 0.479530 | **Failure** The target is unaffected, and you can't use Hang in  There again for 1 minute. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49` | 0.478626 | **YOU CAN DO IT **[one-action] **FEAT 14** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.474558 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/13` | 0.469678 | **Critical Failure** The target is unaffected, and you can't use  Hang in There again for 1 hour. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/578` | 0.468504 | Hang in There |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18` | 0.465335 | **CHEER UP **[one-action] **FEAT 8** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.464677 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |

### Query 127
- Text: What are the requirements for **Prerequisites** expert in Diplomacy?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/8', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/56']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/8', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/9', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/13/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/8` | 0.959466 | **Prerequisites** expert in Diplomacy |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25` | 0.661583 | **Prerequisites** trained in Deception or Diplomacy |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/56` | 0.530643 | Trained in one of the following skills  of your choice: Deception, Diplomacy,  Intimidation |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/58` | 0.460957 | **Prerequisites** Influence |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/19` | 0.443977 | **Prerequisites **Improvised Mastery |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/20` | 0.431679 | **Prerequisites** trained in Medicine |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/9` | 0.422467 | You encourage yourself or an ally, psyching them up for a  coming challenge and granting them temporary Hit Points.  Choose yourself or an ally within 30 feet, then attempt a  DC 20 Diplomacy check. I |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.409605 | **Prerequisites** trained in Intimidation |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/23` | 0.393009 | **Prerequisites** trained in Deception |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/22` | 0.393009 | **Prerequisites** trained in Deception |

### Query 128
- Text: What are the requirements for **HURRY **[one-action] **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/14', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/5', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/14', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/13', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/13/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/14` | 0.884883 | **HURRY **[one-action] **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/5` | 0.614060 | **HANG IN THERE **[one-action] **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18` | 0.581961 | **CHEER UP **[one-action] **FEAT 8** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.502809 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.490463 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49` | 0.476203 | **YOU CAN DO IT **[one-action] **FEAT 14** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/5` | 0.473929 | **ACQUIRE ASSET **[one-action] **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.469492 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/14` | 0.449657 | **SECONDARY DIRECTIVE **[one-action] **FEAT 12** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/16` | 0.443608 | You urge an ally to pick up the pace and contribute more  to the events happening around them. One ally within 30  feet who can sense you becomes quickened for 1 round.  They can use the extra action |

### Query 129
- Text: What are the requirements for **CHEER UP **[one-action] **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/14', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/546']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/19', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18` | 0.882330 | **CHEER UP **[one-action] **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/14` | 0.589909 | **HURRY **[one-action] **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/546` | 0.561971 | Cheer Up |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49` | 0.490360 | **YOU CAN DO IT **[one-action] **FEAT 14** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/5` | 0.473905 | **ACQUIRE ASSET **[one-action] **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.473512 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/31` | 0.466858 | **LOOK ALIVE** **FEAT 8** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.461956 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/22` | 0.461935 | **CONFOUNDING DISQUISITION **[two-actions] **FEAT 8** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/30` | 0.454974 | **SIZE UP** **FEAT 1** |

### Query 130
- Text: What are the requirements for **Prerequisites** trained in Medicine?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/20', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/28', 'PZO22001 Starfinder Player Core 098-113::/page/7/Text/37']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/20', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/19', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/13/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/20` | 0.925383 | **Prerequisites** trained in Medicine |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.532206 | **Prerequisites** trained in Intimidation |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/37` | 0.513725 | **Leadership Skill **Medicine |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/22` | 0.448863 | **Prerequisites** trained in Deception |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/23` | 0.448863 | **Prerequisites** trained in Deception |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/19` | 0.447432 | **Prerequisites **Improvised Mastery |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/58` | 0.446067 | **Prerequisites** Influence |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25` | 0.437054 | **Prerequisites** trained in Deception or Diplomacy |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/8` | 0.430236 | **Prerequisites** expert in Diplomacy |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34` | 0.418516 | **Prerequisites** Watch Out |

### Query 131
- Text: What are the requirements for **CONFOUNDING DISQUISITION **[two-actions] **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/22', 'PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/22', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/24', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/21']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/13/Text/21` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/22` | 0.944931 | **CONFOUNDING DISQUISITION **[two-actions] **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.532199 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22` | 0.513354 | **SEARCH HIGH AND LOW! **[one-action]** TO **[two-actions] **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18` | 0.464798 | **CHEER UP **[one-action] **FEAT 8** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/17` | 0.454352 | **Requirements** Your last action this turn was issuing a  2-action directive. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.440778 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/19` | 0.430052 | **SITUATIONAL AWARENESS **[two-actions] **FEAT 12** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/39` | 0.427608 | **KEEP ON KEEPING ON!** [one-action]** TO **[two-actions] |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.425984 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.423349 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |

### Query 132
- Text: What are the requirements for **Prerequisites** trained in Deception or Diplomacy?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/23', 'PZO22001 Starfinder Player Core 098-113::/page/12/Text/22']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/24', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/13/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25` | 0.942315 | **Prerequisites** trained in Deception or Diplomacy |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/23` | 0.846816 | **Prerequisites** trained in Deception |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/22` | 0.846816 | **Prerequisites** trained in Deception |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/56` | 0.715335 | Trained in one of the following skills  of your choice: Deception, Diplomacy,  Intimidation |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/5` | 0.706455 | **Prerequisites** master in Deception |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/8` | 0.668939 | **Prerequisites** expert in Diplomacy |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/33` | 0.523760 | **Trigger** You're about to roll a Deception, Diplomacy, or  Intimidation check, but you haven't rolled yet. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.520537 | **Prerequisites** trained in Intimidation |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/7` | 0.512345 | Computers, Deception, Diplomacy, Society, Tech Lore |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/12` | 0.507069 | **Trigger** You roll a skill check for any of the following skills  you're legendary in: Deception, Diplomacy, Intimidation, or  your leadership skill. |

### Query 133
- Text: What are the requirements for **LOOK ALIVE** **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/31', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/594']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/31', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/33', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/13/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/31` | 0.859094 | **LOOK ALIVE** **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18` | 0.532835 | **CHEER UP **[one-action] **FEAT 8** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/594` | 0.524827 | Look Alive |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/37` | 0.469772 | **SIDESTEP **[reaction] **FEAT 8** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.445629 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/Table/16` | 0.434594 | FeatLevelInfluence4Look Alive8Master Plan14Not in the Face4Pardon Me1Quip1Ready to Roll14Saw it Coming4Search High and Low!2Secondary Directive12Size Up1Sidestep8Situational Awareness12Smooth Diversio |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/595` | 0.418908 | 8 |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/423` | 0.406908 | 8 |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/549` | 0.406908 | 8 |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/547` | 0.406908 | 8 |

### Query 134
- Text: What are the requirements for **Prerequisites** Watch Out?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/26', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/630']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/33', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/35']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/13/Text/35` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34` | 0.929420 | **Prerequisites** Watch Out |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/26` | 0.929420 | **Prerequisites** Watch Out |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/630` | 0.576909 | Watch Out |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/58` | 0.496741 | **Prerequisites** Influence |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/7` | 0.471426 | **Prerequisites** Size Up |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17` | 0.471426 | **Prerequisites** Size Up |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/20` | 0.436248 | **Prerequisites** trained in Medicine |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/27` | 0.414012 | When you warn an ally of an attack, you follow up with a  shot at your enemy. The first time each round you use your  Watch Out reaction, you can make a melee or ranged Strike  against the triggering |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/35` | 0.412648 | You warn your ally to move away from danger. You can use  Watch Out before an ally in range attempts a Reflex save in  addition to its original trigger. If you do, the circumstance  bonus applies to t |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.408473 | **Prerequisites** trained in Intimidation |

### Query 135
- Text: What are the requirements for **SIDESTEP **[reaction] **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/37', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/614']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/37', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/39', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/36']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/39` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/13/Text/36` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/37` | 0.881137 | **SIDESTEP **[reaction] **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18` | 0.528246 | **CHEER UP **[one-action] **FEAT 8** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/614` | 0.525669 | Sidestep |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/31` | 0.482892 | **LOOK ALIVE** **FEAT 8** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/19` | 0.454255 | **NOT IN THE FACE **[reaction] **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/8` | 0.445769 | **TAG TEAM **[reaction] **FEAT 10** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29` | 0.439780 | **INFLUENCE **[reaction] **FEAT 4** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/26` | 0.435833 | **QUIP **[reaction] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/41` | 0.424338 | **DIRTY RETORT **[reaction] **FEAT 6** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.424087 | **WATCH OUT **[reaction] **FEAT 1** |

### Query 136
- Text: What are the requirements for **CUT 'EM DEEP** **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/43', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/49', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/550']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/43', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/45', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/42']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/45` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/42` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/43` | 0.878745 | **CUT 'EM DEEP** **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/49` | 0.613135 | **GOT 'EM **[free-action] **FEAT 10** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/550` | 0.585135 | Cut 'Em Deep |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/8` | 0.442396 | **TAG TEAM **[reaction] **FEAT 10** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/551` | 0.425003 | 10 |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/621` | 0.413003 | 10 |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/427` | 0.413003 | 10 |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/577` | 0.413003 | 10 |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/619` | 0.413003 | 10 |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/Table/3` | 0.408100 | FeatLevelAcquire Asset2Change of Plans2Cheer Up8Confounding Disquisition8Cut 'Em Deep10Dirty Retort6Distant Feint6Diverse Schemes4Don't You Die on Me2Down to the Wire14Effortless Influencer16Endlessly |

### Query 137
- Text: What are the requirements for **Prerequisites** master in Intimidation?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/46']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/46', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/28', 'PZO22001 Starfinder Player Core 098-113::/page/15/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/46', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/47', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/45']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/13/Text/47` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/45` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/46` | 0.971270 | **Prerequisites** master in Intimidation |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.879244 | **Prerequisites** trained in Intimidation |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/19` | 0.603526 | **Prerequisites **Improvised Mastery |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/56` | 0.526680 | Trained in one of the following skills  of your choice: Deception, Diplomacy,  Intimidation |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/5` | 0.491419 | **Prerequisites** master in Deception |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/19` | 0.450728 | You can use Improvised Mastery twice per day. Additionally,  the first time per day when you roll a natural 1 on a Deception,  Diplomacy, or Intimidation check, you don't automatically  reduce your de |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/58` | 0.439659 | **Prerequisites** Influence |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/23` | 0.411266 | **Prerequisites** trained in Deception |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/22` | 0.411266 | **Prerequisites** trained in Deception |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/20` | 0.401936 | **Prerequisites** trained in Medicine |

### Query 138
- Text: What are the requirements for **GOT 'EM **[free-action] **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/49']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/49', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/43', 'PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/49', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/48', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/51']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/13/Text/48` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/51` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/49` | 0.892401 | **GOT 'EM **[free-action] **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/43` | 0.557894 | **CUT 'EM DEEP** **FEAT 10** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12` | 0.552209 | **GET 'EM! **[one-action]** TO **[two-actions] |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/11` | 0.494006 | **Trigger** The target of your Get 'Em! is reduced to 0 Hit Points. **Requirements** You used Get 'Em! against a creature on your  last turn. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/8` | 0.492566 | **TAG TEAM **[reaction] **FEAT 10** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44` | 0.466573 | **READY TO ROLL **[free-action] **FEAT 14** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.459122 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/2` | 0.454548 | **EXTEND DIRECTIVE **[free-action] **FEAT 16** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/35` | 0.435420 | **SAW IT COMING **[free-action] **FEAT 4** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.424981 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |

### Query 139
- Text: What are the requirements for **SMOOTH DIVERSIONS** **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/2', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/618', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/49']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/2', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/4', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/14/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/14/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/2` | 0.914213 | **SMOOTH DIVERSIONS** **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/618` | 0.474795 | Smooth Diversions |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/49` | 0.444503 | **GOT 'EM **[free-action] **FEAT 10** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/619` | 0.405481 | 10 |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/8` | 0.395832 | **TAG TEAM **[reaction] **FEAT 10** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/621` | 0.393481 | 10 |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/577` | 0.393481 | 10 |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/427` | 0.393481 | 10 |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/551` | 0.393481 | 10 |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/43` | 0.388979 | **CUT 'EM DEEP** **FEAT 10** |

### Query 140
- Text: What are the requirements for **Prerequisites** master in Deception?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/14/Text/5', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/23', 'PZO22001 Starfinder Player Core 098-113::/page/12/Text/22']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/Text/5', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/6', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/14/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/14/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/5` | 0.952810 | **Prerequisites** master in Deception |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/23` | 0.845434 | **Prerequisites** trained in Deception |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/22` | 0.845434 | **Prerequisites** trained in Deception |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25` | 0.702913 | **Prerequisites** trained in Deception or Diplomacy |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/56` | 0.533471 | Trained in one of the following skills  of your choice: Deception, Diplomacy,  Intimidation |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/46` | 0.507371 | **Prerequisites** master in Intimidation |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/7` | 0.435207 | Computers, Deception, Diplomacy, Society, Tech Lore |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/19` | 0.434988 | **Prerequisites **Improvised Mastery |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/19` | 0.426415 | You can use Improvised Mastery twice per day. Additionally,  the first time per day when you roll a natural 1 on a Deception,  Diplomacy, or Intimidation check, you don't automatically  reduce your de |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.423184 | **Prerequisites** trained in Intimidation |

### Query 141
- Text: What are the requirements for **TAG TEAM **[reaction] **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/8', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/49', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/620']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/8', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/10', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/14/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/14/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/8` | 0.882642 | **TAG TEAM **[reaction] **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/49` | 0.564758 | **GOT 'EM **[free-action] **FEAT 10** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/620` | 0.556419 | Tag Team |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/43` | 0.423022 | **CUT 'EM DEEP** **FEAT 10** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/621` | 0.422857 | 10 |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/619` | 0.422857 | 10 |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/37` | 0.418413 | **SIDESTEP **[reaction] **FEAT 8** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/Table/16` | 0.417806 | FeatLevelInfluence4Look Alive8Master Plan14Not in the Face4Pardon Me1Quip1Ready to Roll14Saw it Coming4Search High and Low!2Secondary Directive12Size Up1Sidestep8Situational Awareness12Smooth Diversio |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/7` | 0.414792 | **GET THEM!** **FEAT 16** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/48` | 0.414181 | **SKILLS** **FEATS** |

### Query 142
- Text: What are the requirements for **SECONDARY DIRECTIVE **[one-action] **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/14', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/28', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/14', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/16', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/14/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/14` | 0.910580 | **SECONDARY DIRECTIVE **[one-action] **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/28` | 0.624238 | **UNSTOPPABLE DIRECTIVES** **FEAT 12** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/17` | 0.595175 | **Requirements** Your last action this turn was issuing a  2-action directive. |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/52` | 0.552085 | **Requirements** Your last action was a 1-action directive. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/610` | 0.531848 | Secondary Directive |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/2` | 0.512091 | **EXTEND DIRECTIVE **[free-action] **FEAT 16** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.496336 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/19` | 0.485007 | **SITUATIONAL AWARENESS **[two-actions] **FEAT 12** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49` | 0.474343 | **YOU CAN DO IT **[one-action] **FEAT 14** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/22` | 0.471344 | You Ready a directive. If the trigger you designated occurs  before the start of your next turn, you can use the 2-action  version of the directive instead of the 1-action. |

### Query 143
- Text: What are the requirements for **SITUATIONAL AWARENESS **[two-actions] **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/19', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/616', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/19', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/21', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/14/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/14/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/19` | 0.948320 | **SITUATIONAL AWARENESS **[two-actions] **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/616` | 0.638218 | Situational Awareness |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/14` | 0.564637 | **SECONDARY DIRECTIVE **[one-action] **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/5` | 0.494198 | **ACQUIRE ASSET **[one-action] **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.492540 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/31` | 0.482118 | **DIGITAL ASSESSMENT! **[one-action]** TO **[two-actions] |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.472303 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22` | 0.452457 | **SEARCH HIGH AND LOW! **[one-action]** TO **[two-actions] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.441404 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.437816 | **READY ARMS! **[one-action]** TO **[two-actions] |

### Query 144
- Text: What are the requirements for **THAT'LL SHOW 'EM** **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/23', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/624', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/49']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/23', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/25', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/14/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/14/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/23` | 0.870395 | **THAT'LL SHOW 'EM** **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/624` | 0.536456 | That'll Show 'Em |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/49` | 0.482922 | **GOT 'EM **[free-action] **FEAT 10** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/625` | 0.403426 | 12 |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/629` | 0.391426 | 12 |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/617` | 0.391426 | 12 |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/611` | 0.391426 | 12 |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/431` | 0.391426 | 12 |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/43` | 0.385321 | **CUT 'EM DEEP** **FEAT 10** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.380188 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |

### Query 145
- Text: What are the requirements for **Prerequisites** Watch Out?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/Text/26']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/26', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/630']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/Text/26', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/27', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/25']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/14/Text/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/14/Text/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34` | 0.929420 | **Prerequisites** Watch Out |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/26` | 0.929420 | **Prerequisites** Watch Out |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/630` | 0.576909 | Watch Out |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/58` | 0.496741 | **Prerequisites** Influence |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/7` | 0.471426 | **Prerequisites** Size Up |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17` | 0.471426 | **Prerequisites** Size Up |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/20` | 0.436248 | **Prerequisites** trained in Medicine |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/27` | 0.414012 | When you warn an ally of an attack, you follow up with a  shot at your enemy. The first time each round you use your  Watch Out reaction, you can make a melee or ranged Strike  against the triggering |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/35` | 0.412648 | You warn your ally to move away from danger. You can use  Watch Out before an ally in range attempts a Reflex save in  addition to its original trigger. If you do, the circumstance  bonus applies to t |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.408473 | **Prerequisites** trained in Intimidation |

### Query 146
- Text: What are the requirements for **UNSTOPPABLE DIRECTIVES** **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/28', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/628', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/28', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/27', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/14/Text/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/14/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/28` | 0.927316 | **UNSTOPPABLE DIRECTIVES** **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/628` | 0.650173 | Unstoppable Directives |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/14` | 0.620115 | **SECONDARY DIRECTIVE **[one-action] **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/8` | 0.460459 | ENVOY DIRECTIVES |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/Table/16` | 0.448123 | FeatLevelInfluence4Look Alive8Master Plan14Not in the Face4Pardon Me1Quip1Ready to Roll14Saw it Coming4Search High and Low!2Secondary Directive12Size Up1Sidestep8Situational Awareness12Smooth Diversio |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/2` | 0.416965 | **EXTEND DIRECTIVE **[free-action] **FEAT 16** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/22` | 0.415710 | **Leadership Directive **Into Position! |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/610` | 0.400170 | Secondary Directive |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/23` | 0.399103 | **THAT'LL SHOW 'EM** **FEAT 12** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/17` | 0.398053 | **Requirements** Your last action this turn was issuing a  2-action directive. |

### Query 147
- Text: What are the requirements for **DOWN TO THE WIRE **[reaction] **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/34', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/34', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/33', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/36']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/14/Text/36` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/34` | 0.890464 | **DOWN TO THE WIRE **[reaction] **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44` | 0.612739 | **READY TO ROLL **[free-action] **FEAT 14** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49` | 0.571523 | **YOU CAN DO IT **[one-action] **FEAT 14** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/560` | 0.520976 | Down to the Wire |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/19` | 0.458844 | **NOT IN THE FACE **[reaction] **FEAT 4** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.454458 | **WATCH OUT **[reaction] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/39` | 0.445985 | **MASTER PLAN** **FEAT 14** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.441291 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.437861 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/Table/3` | 0.437060 | FeatLevelAcquire Asset2Change of Plans2Cheer Up8Confounding Disquisition8Cut 'Em Deep10Dirty Retort6Distant Feint6Diverse Schemes4Don't You Die on Me2Down to the Wire14Effortless Influencer16Endlessly |

### Query 148
- Text: What are the requirements for **MASTER PLAN** **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/39', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/596', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/39', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/41', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/38']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/14/Text/41` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/14/Text/38` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/39` | 0.912946 | **MASTER PLAN** **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/596` | 0.576598 | Master Plan |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49` | 0.480853 | **YOU CAN DO IT **[one-action] **FEAT 14** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44` | 0.434798 | **READY TO ROLL **[free-action] **FEAT 14** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/33` | 0.431044 | 14TH LEVEL |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/9` | 0.422218 | **CHANGE OF PLANS **[reaction] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/19` | 0.417988 | **Prerequisites **Improvised Mastery |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/597` | 0.405522 | 14 |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/Table/16` | 0.395111 | FeatLevelInfluence4Look Alive8Master Plan14Not in the Face4Pardon Me1Quip1Ready to Roll14Saw it Coming4Search High and Low!2Secondary Directive12Size Up1Sidestep8Situational Awareness12Smooth Diversio |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/435` | 0.393522 | 14 |

### Query 149
- Text: What are the requirements for **READY TO ROLL **[free-action] **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49', 'PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/43', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/46']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/14/Text/43` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/14/Text/46` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44` | 0.910336 | **READY TO ROLL **[free-action] **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49` | 0.572896 | **YOU CAN DO IT **[one-action] **FEAT 14** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.540153 | **READY ARMS! **[one-action]** TO **[two-actions] |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/35` | 0.473631 | **SAW IT COMING **[free-action] **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/34` | 0.469289 | **DOWN TO THE WIRE **[reaction] **FEAT 14** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.463602 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/49` | 0.460293 | **GOT 'EM **[free-action] **FEAT 10** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/39` | 0.456944 | **MASTER PLAN** **FEAT 14** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/2` | 0.446761 | **EXTEND DIRECTIVE **[free-action] **FEAT 16** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/5` | 0.443730 | **ACQUIRE ASSET **[one-action] **FEAT 2** |

### Query 150
- Text: What are the requirements for **YOU CAN DO IT **[one-action] **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44', 'PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/48', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/51']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/14/Text/48` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/14/Text/51` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49` | 0.901733 | **YOU CAN DO IT **[one-action] **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44` | 0.602380 | **READY TO ROLL **[free-action] **FEAT 14** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.575531 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.510494 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/632` | 0.509251 | You Can Do It |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18` | 0.495567 | **CHEER UP **[one-action] **FEAT 8** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.495561 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/5` | 0.495321 | **ACQUIRE ASSET **[one-action] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/13` | 0.494154 | **DON'T YOU DIE ON ME **[one-action] **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/39` | 0.486328 | **MASTER PLAN** **FEAT 14** |

### Query 151
- Text: What are the requirements for **EFFORTLESS INFLUENCER** **FEAT 16**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/55']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/55', 'PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/2', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/562']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/55', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/54', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/57']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/54` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/14/Text/57` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/55` | 0.923877 | **EFFORTLESS INFLUENCER** **FEAT 16** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/2` | 0.627119 | **INFLUENCER** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/562` | 0.623765 | Effortless Influencer |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/58` | 0.549736 | **Prerequisites** Influence |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/7` | 0.494933 | **GET THEM!** **FEAT 16** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29` | 0.456871 | **INFLUENCE **[reaction] **FEAT 4** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Table/3` | 0.419097 | FeatLevelAcquire Asset2Change of Plans2Cheer Up8Confounding Disquisition8Cut 'Em Deep10Dirty Retort6Distant Feint6Diverse Schemes4Don't You Die on Me2Down to the Wire14Effortless Influencer16Endlessly |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/2` | 0.414424 | **EXTEND DIRECTIVE **[free-action] **FEAT 16** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/19` | 0.410277 | **Prerequisites **Improvised Mastery |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/66` | 0.405162 | **SKILLS** **FEATS** |

### Query 152
- Text: What are the requirements for **Prerequisites** Influence?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/Text/58']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/14/Text/58', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/592', 'PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/Text/58', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/59', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/57']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/14/Text/59` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/14/Text/57` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/58` | 0.937200 | **Prerequisites** Influence |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/592` | 0.637173 | Influence |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/2` | 0.590156 | **INFLUENCER** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29` | 0.488090 | **INFLUENCE **[reaction] **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/19` | 0.454474 | **Prerequisites **Improvised Mastery |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/26` | 0.444849 | **Prerequisites** Watch Out |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34` | 0.444849 | **Prerequisites** Watch Out |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/8` | 0.441599 | **Prerequisites** expert in Diplomacy |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/7` | 0.422467 | **Prerequisites** Size Up |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17` | 0.422467 | **Prerequisites** Size Up |

### Query 153
- Text: What are the requirements for **EXTEND DIRECTIVE **[free-action] **FEAT 16**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/2', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/14', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/566']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/2', 'PZO22001 Starfinder Player Core 098-113::/page/15/Text/1', 'PZO22001 Starfinder Player Core 098-113::/page/15/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 098-113::/page/15/Text/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 098-113::/page/15/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/2` | 0.908559 | **EXTEND DIRECTIVE **[free-action] **FEAT 16** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/14` | 0.593717 | **SECONDARY DIRECTIVE **[one-action] **FEAT 12** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/566` | 0.558655 | Extend Directive |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/7` | 0.503536 | **GET THEM!** **FEAT 16** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/17` | 0.498070 | **Requirements** Your last action this turn was issuing a  2-action directive. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/52` | 0.493202 | **Requirements** Your last action was a 1-action directive. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/28` | 0.483535 | **UNSTOPPABLE DIRECTIVES** **FEAT 12** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/49` | 0.480416 | **GOT 'EM **[free-action] **FEAT 10** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44` | 0.469302 | **READY TO ROLL **[free-action] **FEAT 14** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/16` | 0.458918 | **IMPROVISED LEGEND **[free-action] **FEAT 18** |
