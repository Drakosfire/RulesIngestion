# RulesLawyer Evaluation Report: nomic-embed-text-v2

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `370`
- Query count: `101`
- Evaluated queries: `101`
- Coverage: `1.0000`
- MRR: `0.9221`
- hit@1: `0.8911`
- hit@3: `0.9307`
- hit@5: `0.9901`
- hit@10: `1.0000`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

### Expanded Gold Metrics
- Coverage: `1.0000`
- MRR: `0.9454`
- hit@1: `0.9208`
- hit@3: `0.9604`
- hit@5: `0.9901`
- hit@10: `1.0000`

### Expanded Gold Expansion Stats
- Queries with additions: `101`
- Avg added per query: `2.25`
- Max added: `8`
- Addition reasons:
  - graph_depth_1: `227`

### Expanded Gold Delta (Expanded - Strict)
- Coverage Δ: `0.0000`
- MRR Δ: `0.0233`
- hit@1 Δ: `0.0297`
- hit@3 Δ: `0.0297`
- hit@5 Δ: `0.0000`
- hit@10 Δ: `0.0000`

## Timings (ms)
- Embedding (chunks): `6963`
- Embedding (queries): `2340`
- Evaluation (strict): `14`
- Evaluation (expanded): `14`
- Total: `13651`

### Timing Estimates (ms)
- Evaluation (strict): `10`
- Evaluation (expanded): `10`
- Total: `9323`

## Query Details
### Query 0
- Text: Summarize USING THIS BOOK
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/20', 'PZO22001 Starfinder Player Core 014-029::/page/4/Text/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/1` | 0.834024 | USING THIS BOOK |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/20` | 0.457985 | The back of this book has an  appendix with the rules for all of  the conditions that you will find  in the game. This section also  includes a blank character sheet,  and an index with a comprehensiv |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/5` | 0.434107 | their past, and think about how and why they adventure.  You'll want to peruse Starfinder's available ancestries,  backgrounds, and classes. The summaries on pages 27–28  might help you match your con |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/3` | 0.384909 | The summaries of the classes on page 28 list each  class's key attribute—the attribute modifier used to  calculate the potency of many of their class abilities.  Characters receive an attribute boost |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/17` | 0.370686 | Once you've developed your character's concept, jot  down a few sentences summarizing your ideas under  the Notes section on the third page of your character  sheet. Record any of the details you've a |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/2` | 0.362531 | Throughout this rulebook, you will see formatting  standards that might look a bit unusual at first. These  standards are in place to make the rules elements in this  book easier to recognize. |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.361090 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.355840 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/19` | 0.355352 | weapons, and other basic equipment. Your character's class  lists the types of weapons and armor with which they are  trained (or better!). Their weapons determine how much  damage they deal in combat |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/5` | 0.355267 | All the steps of character creation are detailed on  the following pages; each is marked with a number that  corresponds to the sample character sheet on pages 20–21,  showing you where the informatio |

### Query 1
- Text: What is the rule about While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy as possible. Rules are grouped  together in chapters, with the early chapters focusing on  character creation. The following is a summary of what  you can expect to find in each chapter.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/2', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/18', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/2', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 1.009658 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/18` | 0.853299 | This important chapter contains  the universal rules needed to play  Starfinder, including rules for the  various modes of play, the basic  actions that every character can  perform, the rules for com |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/4` | 0.826757 | This introduction is designed to help you understand the  basics of Starfinder. This chapter also includes the rules for  building and leveling up a character, as well as an example  of the character |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/3` | 0.772769 | This section provides a step-by-step guide for creating a  character using the Starfinder rules, preceded by a guide to  help you understand attribute modifiers. These modifiers are a  critical part o |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/5` | 0.707174 | their past, and think about how and why they adventure.  You'll want to peruse Starfinder's available ancestries,  backgrounds, and classes. The summaries on pages 27–28  might help you match your con |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/12/Text/2` | 0.688767 | This step-by-step example illustrates the process of  creating a Starfinder character. |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/1` | 0.688060 | Unless you're the GM, the first thing you need to do when playing Starfinder is create your character. It's  up to you to imagine your character's past experiences, personality, and view of the galaxy |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/15` | 0.686795 | You might want to coordinate with other players when  forming your character concept. Your characters could have  something in common already; perhaps they are travelers  from the same home world, or |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.643722 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.642490 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |

### Query 2
- Text: Summarize CHAPTER 1: INTRODUCTION
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/3', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/16', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/3', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/4', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/0/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/3` | 0.946038 | CHAPTER 1: INTRODUCTION |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/16` | 0.772755 | INTRODUCTION |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/18` | 0.707928 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/28` | 0.665928 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/24` | 0.665928 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/23` | 0.665928 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/27` | 0.665928 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/4` | 0.460077 | This introduction is designed to help you understand the  basics of Starfinder. This chapter also includes the rules for  building and leveling up a character, as well as an example  of the character |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.439330 | **OVERVIEW** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/5` | 0.437566 | CHAPTER 2: ANCESTRIES &  BACKGROUNDS |

### Query 3
- Text: What is the rule about This introduction is designed to help you understand the  basics of Starfinder. This chapter also includes the rules for  building and leveling up a character, as well as an example  of the character creation process. The chapter ends with  an introduction to the galaxy and its gods.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/4', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/2', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/4', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/5', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/4` | 0.994129 | This introduction is designed to help you understand the  basics of Starfinder. This chapter also includes the rules for  building and leveling up a character, as well as an example  of the character |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.849286 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/18` | 0.807065 | This important chapter contains  the universal rules needed to play  Starfinder, including rules for the  various modes of play, the basic  actions that every character can  perform, the rules for com |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/3` | 0.735756 | This section provides a step-by-step guide for creating a  character using the Starfinder rules, preceded by a guide to  help you understand attribute modifiers. These modifiers are a  critical part o |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/1` | 0.691980 | Unless you're the GM, the first thing you need to do when playing Starfinder is create your character. It's  up to you to imagine your character's past experiences, personality, and view of the galaxy |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/12/Text/2` | 0.686563 | This step-by-step example illustrates the process of  creating a Starfinder character. |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/5` | 0.678277 | their past, and think about how and why they adventure.  You'll want to peruse Starfinder's available ancestries,  backgrounds, and classes. The summaries on pages 27–28  might help you match your con |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/15` | 0.649009 | You might want to coordinate with other players when  forming your character concept. Your characters could have  something in common already; perhaps they are travelers  from the same home world, or |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/9` | 0.634979 | Write down the deity your character worships, if any.  Your character might worship several deities as part of a  personal pantheon. You might instead choose a philosophy  or decide your character is |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/13` | 0.609620 | Perhaps you'd like to play a character who is a devout  follower of a specific deity. The peoples of the galaxy follow  myriad faiths and philosophies spanning a wide pantheon,  from Damoritosh, the C |

### Query 4
- Text: What is the rule about CHAPTER 2: ANCESTRIES &  BACKGROUNDS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/5', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/21', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/23']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/5', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/6', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/0/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/0/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/5` | 0.859395 | CHAPTER 2: ANCESTRIES &  BACKGROUNDS |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/21` | 0.770706 | ANCESTRIES & BACKGROUNDS |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/23` | 0.753670 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/33` | 0.723670 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/29` | 0.723670 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/32` | 0.723670 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/7` | 0.723670 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/28` | 0.723670 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/8` | 0.610827 | ANCESTRY, BACKGROUND, CLASS,  OR DETAILS |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/13/SectionHeader/27` | 0.533575 | ANCESTRIES |

### Query 5
- Text: What is the rule about The rules for ancestries and heritages representing the  Pact Worlds are in this chapter, including their ancestry  feat options. Backgrounds are at the end of this chapter,  along with a section about languages, as these are often  influenced by your choice of ancestry.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/6', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/19', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/6', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/5', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/6` | 1.009842 | The rules for ancestries and heritages representing the  Pact Worlds are in this chapter, including their ancestry  feat options. Backgrounds are at the end of this chapter,  along with a section abou |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/19` | 0.662405 | Select an ancestry for your character. The ancestry  summaries on page 27 provide an overview of Starfinder's  core ancestry options, and each is fully detailed in Chapter  2. Ancestry determines your |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/3` | 0.660272 | **Ancestry:** Each ancestry provides attribute boosts, and sometimes an attribute flaw. If you're taking any voluntary  flaws, apply them in this step (see the sidebar on page 25). |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/6/Text/2` | 0.606429 | your character's ancestry provides them with special abilities, write them in the appropriate spaces, such as darkvision in the Senses section on the first page and innate spells on the fourth page. W |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` | 0.603050 | Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/16` | 0.593110 | Select feats as indicated on your class advancement  table. For ancestry feats, see Chapter 2. For class  feats, see your class entry in Chapter 3. For general  feats and skill feats, see Chapter 5. |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/20` | 0.591638 | You'll have four decisions to make when you choosing your  character's ancestry. |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/2` | 0.589748 | On pages 27–28, you'll see a visual representation  of ancestries and classes that provides at-a-glance  information for players looking to make the most of  their starting attribute modifiers. In the |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/10/Text/2` | 0.589317 | The attribute boosts and flaws listed in each ancestry  represent general trends or help guide players to  create the kinds of characters from that ancestry most  likely to pursue the life of an adven |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/21` | 0.579856 | Pick the ancestry itself. |

### Query 6
- Text: Summarize CHAPTER 3: CLASSES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/7', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/22', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/24']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/7', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/8', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/0/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/7` | 1.005200 | CHAPTER 3: CLASSES |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/22` | 0.814746 | CLASSES |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/24` | 0.813608 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/33` | 0.783608 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/8` | 0.783608 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/30` | 0.783608 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/29` | 0.783608 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/34` | 0.783608 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/6/Text/9` | 0.502004 | At this point, you need to decide your character's class. A class gives your character access to a suite of heroic abilities, determines how effectively they fight, and governs how easily they can sha |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/17` | 0.473052 | Add spells and spell slots if your class grants  spellcasting. See Chapter 7 for spells. |

### Query 7
- Text: What is the rule about This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the class feats available to members  of that class. At the end of this chapter are the rules for  archetypes—special options available to characters as they  increase in level. These rules allow a character to dabble in  the abilities of another class or concept.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/8', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/6', 'PZO22001 Starfinder Player Core 014-029::/page/15/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/8', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/7', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 1.018992 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.795805 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/7` | 0.753738 | You can find all the new abilities specific to your class,  including class feats, right in your class entry, though you  can also use class feats to take an archetype (page 174).  Your character's cl |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.710422 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/6/Text/9` | 0.705357 | At this point, you need to decide your character's class. A class gives your character access to a suite of heroic abilities, determines how effectively they fight, and governs how easily they can sha |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/16` | 0.676481 | This chapter starts with rules for casting spells,  determining their effects, and negating foes' spells  (called counteracting). After that, the spell lists for  each spellcasting tradition are inclu |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.651265 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.650856 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/12` | 0.646652 | As a character advances in level, they gain additional feats  to represent their growing abilities. General feats and skill  feats (which are a subset of general feats) are presented  in this chapter. |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` | 0.640454 | Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules |

### Query 8
- Text: What is the rule about CHAPTER 4: SKILLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/9', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/23', 'PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/9', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/8', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/9` | 0.853141 | CHAPTER 4: SKILLS |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/23` | 0.665296 | SKILLS |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/13` | 0.665296 | SKILLS |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.615121 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/25` | 0.550553 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/30` | 0.550553 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/35` | 0.550553 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/9` | 0.550553 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/34` | 0.550553 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/31` | 0.550553 | **SKILLS** |

### Query 9
- Text: What is the rule about The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can define some of a character's  skill proficiencies, and each character can also select a few  additional skills to reflect their personality and training.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/10', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/8', 'PZO22001 Starfinder Player Core 014-029::/page/7/ListItem/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/10', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/11', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 1.017881 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.742635 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/7/ListItem/13` | 0.709950 | The Initial Proficiencies section of your class entry indicates your character's starting proficiency ranks in a number of areas. Choose which skills your character is trained in and record those, alo |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/7` | 0.663599 | You can find all the new abilities specific to your class,  including class feats, right in your class entry, though you  can also use class feats to take an archetype (page 174).  Your character's cl |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.660192 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/6/Text/9` | 0.639908 | At this point, you need to decide your character's class. A class gives your character access to a suite of heroic abilities, determines how effectively they fight, and governs how easily they can sha |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/10/Text/14` | 0.638376 | In the second box to the right of each skill on your character  sheet, there's an abbreviation to remind you of the attribute  modifier for that skill. For each skill in which your character is  train |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/12` | 0.635296 | As a character advances in level, they gain additional feats  to represent their growing abilities. General feats and skill  feats (which are a subset of general feats) are presented  in this chapter. |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/16` | 0.620675 | This chapter starts with rules for casting spells,  determining their effects, and negating foes' spells  (called counteracting). After that, the spell lists for  each spellcasting tradition are inclu |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/10/Text/5` | 0.616127 | With most of the big decisions for your character made,  it's time to calculate the modifiers for each of the following  statistics. If your proficiency rank for a statistic is trained,  expert, maste |

### Query 10
- Text: What is the rule about CHAPTER 5: FEATS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/11', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/24', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/11', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/12', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/0/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/11` | 0.914492 | CHAPTER 5: FEATS |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/24` | 0.711147 | FEATS |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/10` | 0.681942 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/35` | 0.639942 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/31` | 0.639942 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/32` | 0.639942 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/26` | 0.639942 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/36` | 0.639942 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.563074 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/16` | 0.516715 | Select feats as indicated on your class advancement  table. For ancestry feats, see Chapter 2. For class  feats, see your class entry in Chapter 3. For general  feats and skill feats, see Chapter 5. |

### Query 11
- Text: What is the rule about As a character advances in level, they gain additional feats  to represent their growing abilities. General feats and skill  feats (which are a subset of general feats) are presented  in this chapter.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/12', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/6', 'PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/12', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/11', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/12` | 0.963040 | As a character advances in level, they gain additional feats  to represent their growing abilities. General feats and skill  feats (which are a subset of general feats) are presented  in this chapter. |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.730564 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/16` | 0.713112 | Select feats as indicated on your class advancement  table. For ancestry feats, see Chapter 2. For class  feats, see your class entry in Chapter 3. For general  feats and skill feats, see Chapter 5. |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.661980 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/7` | 0.655779 | You can find all the new abilities specific to your class,  including class feats, right in your class entry, though you  can also use class feats to take an archetype (page 174).  Your character's cl |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.655456 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.651378 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/20` | 0.601974 | modifier, recalculate their maximum Hit  Points using their new Constitution modifier  (typically, this adds 1 Hit Point per level). If  an attribute boost increases your character's  Intelligence mod |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/6` | 0.592887 | Next, return to your character's class entry. Increase  your character's total Hit Points by the number indicated  for your class. Then, take a look at the class advancement  table and find the row fo |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/7/ListItem/14` | 0.579052 | See the class advancement table in your class entry to learn the class features your character gains at 1st level. You have already chosen an ancestry, background, and free attribute boosts, but these |

### Query 12
- Text: Summarize CHAPTER 6: EQUIPMENT
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/13', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/25', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/37']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/13', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/14', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/0/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/0/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/13` | 1.014202 | CHAPTER 6: EQUIPMENT |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/25` | 0.823198 | EQUIPMENT |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/37` | 0.786040 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/27` | 0.744040 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/32` | 0.744040 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/33` | 0.744040 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/17` | 0.689028 | STEP 8: BUY EQUIPMENT |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/12/Text/18` | 0.549951 | Next up, Jessica turns to Chapter 6: Equipment. She's trained  in medium armor and chooses commercial freebooter  armor (which comes with a built-in comm unit, like most  armor). When it comes to weap |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/36` | 0.476528 | **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/11` | 0.476528 | **EQUIPMENT** **SPELLS** |

### Query 13
- Text: Summarize Armor, weapons, and other gear can all be found in this  chapter, along with the price for services, cost of living,  and transportation (such as hovercabs and gravtrains).
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/14', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/20', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/14', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/13', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/14` | 1.038238 | Armor, weapons, and other gear can all be found in this  chapter, along with the price for services, cost of living,  and transportation (such as hovercabs and gravtrains). |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/20` | 0.660508 | You'll also want equipment like cable line, flashlights,  toolkits, and other traveling gear, and maybe even a serum or  sprayflesh for emergency medical needs. Augmentations that  change your body, u |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/19` | 0.603321 | weapons, and other basic equipment. Your character's class  lists the types of weapons and armor with which they are  trained (or better!). Their weapons determine how much  damage they deal in combat |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/12/Text/18` | 0.501232 | Next up, Jessica turns to Chapter 6: Equipment. She's trained  in medium armor and chooses commercial freebooter  armor (which comes with a built-in comm unit, like most  armor). When it comes to weap |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/10/Text/3` | 0.457002 | first page, depending on the weapon, and the rest  of their equipment in the Inventory section on the  second page. You'll calculate specific numbers for  melee Strikes and ranged Strikes with the wea |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/22` | 0.455397 | Once you've spent your character's starting wealth,  calculate any remaining credits they might still have  and write those amounts in the Inventory section on  the second page. Record your character' |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/20` | 0.444141 | The back of this book has an  appendix with the rules for all of  the conditions that you will find  in the game. This section also  includes a blank character sheet,  and an index with a comprehensiv |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/13` | 0.437290 | CHAPTER 6: EQUIPMENT |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/18` | 0.433976 | At 1st level, your character has 150 credits to spend on armor, |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/6/Text/9` | 0.422912 | At this point, you need to decide your character's class. A class gives your character access to a suite of heroic abilities, determines how effectively they fight, and governs how easily they can sha |

### Query 14
- Text: What is the rule about CHAPTER 7: SPELLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/15', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/26', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/38']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/15', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/14', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/0/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/0/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/15` | 0.907264 | CHAPTER 7: SPELLS |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/26` | 0.749153 | SPELLS |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/38` | 0.707201 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/33` | 0.665201 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/34` | 0.665201 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/28` | 0.665201 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/11` | 0.613674 | **EQUIPMENT** **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/36` | 0.613674 | **EQUIPMENT** **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/11/SectionHeader/18` | 0.605955 | **SPELLS AND SPELLCASTING** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/17` | 0.492367 | Add spells and spell slots if your class grants  spellcasting. See Chapter 7 for spells. |

### Query 15
- Text: What is the rule about This chapter starts with rules for casting spells,  determining their effects, and negating foes' spells  (called counteracting). After that, the spell lists for  each spellcasting tradition are included, making it easy  to quickly find spells by their rank. Next are rules for  every spell, presented in alphabetical order. Following  the spell descriptions are all of the focus spells—special  spells granted by specific class abilities and feats. While  most spells appear on multiple spell lists, focus spells  are granted only to members of a specific class and are  grouped together by class for ease of reference. Finally,  at the end of the chapter are rules for rituals, complicated  and risky spells that any character can attempt.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/16', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/8', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/16', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/17', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/16` | 1.025954 | This chapter starts with rules for casting spells,  determining their effects, and negating foes' spells  (called counteracting). After that, the spell lists for  each spellcasting tradition are inclu |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.737594 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/19` | 0.734001 | Many characters can learn a few cantrips or focus spells,  but the mystic and witchwarper gain spellcasting—the  ability to cast a wide variety of spells. If your character's  class grants spells, you |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.647244 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.639161 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.636353 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/6/Text/9` | 0.633259 | At this point, you need to decide your character's class. A class gives your character access to a suite of heroic abilities, determines how effectively they fight, and governs how easily they can sha |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/17` | 0.627144 | Add spells and spell slots if your class grants  spellcasting. See Chapter 7 for spells. |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.626326 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/7` | 0.616963 | You can find all the new abilities specific to your class,  including class feats, right in your class entry, though you  can also use class feats to take an archetype (page 174).  Your character's cl |

### Query 16
- Text: Summarize CHAPTER 8:  PLAYING THE  GAME
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/17', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/27', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/35']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/17', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/16', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/0/Text/16` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/0/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/17` | 1.014311 | CHAPTER 8:  PLAYING THE  GAME |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/27` | 0.792822 | PLAYING THE GAME |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/35` | 0.719505 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/37` | 0.677505 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/34` | 0.677505 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/39` | 0.677505 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/29` | 0.677505 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.540953 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/12` | 0.538575 | **PLAYING THE ** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/63` | 0.490847 | **GAME** |

### Query 17
- Text: What is the rule about This important chapter contains  the universal rules needed to play  Starfinder, including rules for the  various modes of play, the basic  actions that every character can  perform, the rules for combat, and  the rules for death and dying. Every  player should be familiar with this  chapter, especially the GM.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/18', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/2', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/4']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/18', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/17', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/18` | 1.018524 | This important chapter contains  the universal rules needed to play  Starfinder, including rules for the  various modes of play, the basic  actions that every character can  perform, the rules for com |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.861295 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/4` | 0.764612 | This introduction is designed to help you understand the  basics of Starfinder. This chapter also includes the rules for  building and leveling up a character, as well as an example  of the character |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/1` | 0.700306 | Unless you're the GM, the first thing you need to do when playing Starfinder is create your character. It's  up to you to imagine your character's past experiences, personality, and view of the galaxy |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/3` | 0.670792 | This section provides a step-by-step guide for creating a  character using the Starfinder rules, preceded by a guide to  help you understand attribute modifiers. These modifiers are a  critical part o |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/5` | 0.667157 | their past, and think about how and why they adventure.  You'll want to peruse Starfinder's available ancestries,  backgrounds, and classes. The summaries on pages 27–28  might help you match your con |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/15` | 0.651836 | You might want to coordinate with other players when  forming your character concept. Your characters could have  something in common already; perhaps they are travelers  from the same home world, or |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/7` | 0.600935 | Characters and their adversaries affect the galaxy of  Starfinder by using actions and producing effects. This is  especially the case during encounters, when every action  counts. When you use an act |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/3` | 0.597621 | The names of specific statistics, skills, feats, actions,  and some other mechanical elements in Starfinder are  capitalized. This way, when you see the statement "a  Strike targets Armor Class," you |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.596066 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |

### Query 18
- Text: Summarize APPENDICES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/19', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/28', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/30']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/19', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/18', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/0/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/0/Text/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/19` | 0.934292 | APPENDICES |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/28` | 0.676924 | CONDITIONS APPENDIX |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/30` | 0.657947 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/40` | 0.627947 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/36` | 0.627947 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/13` | 0.627947 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/38` | 0.627947 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/35` | 0.627947 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/13/SectionHeader/27` | 0.333571 | ANCESTRIES |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/5` | 0.316108 | CHAPTER 2: ANCESTRIES &  BACKGROUNDS |

### Query 19
- Text: What is the rule about The back of this book has an  appendix with the rules for all of  the conditions that you will find  in the game. This section also  includes a blank character sheet,  and an index with a comprehensive  glossary of common terms and  traits that you'll encounter in  the game.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/20', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/7', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/20', 'PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/20` | 0.993533 | The back of this book has an  appendix with the rules for all of  the conditions that you will find  in the game. This section also  includes a blank character sheet,  and an index with a comprehensiv |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` | 0.733152 | Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.708064 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.629747 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.627289 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/4` | 0.620249 | Many of the steps on pages 18–25 instruct you to fill out  fields on your character sheet. The character sheet is shown  on pages 20–21; you can find a copy in the back of this  book or on **paizo.com |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/2` | 0.613883 | Throughout this rulebook, you will see formatting  standards that might look a bit unusual at first. These  standards are in place to make the rules elements in this  book easier to recognize. |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.612640 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.602906 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.590958 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |

### Query 20
- Text: Summarize FORMAT OF RULES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/2', 'PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/2', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/0/Text/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1` | 0.980772 | FORMAT OF RULES |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/2` | 0.621516 | Throughout this rulebook, you will see formatting  standards that might look a bit unusual at first. These  standards are in place to make the rules elements in this  book easier to recognize. |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5` | 0.593822 | READING RULES |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` | 0.489172 | Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.475242 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.468894 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.428064 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.390986 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.389608 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/20` | 0.381488 | The back of this book has an  appendix with the rules for all of  the conditions that you will find  in the game. This section also  includes a blank character sheet,  and an index with a comprehensiv |

### Query 21
- Text: What is the rule about Throughout this rulebook, you will see formatting  standards that might look a bit unusual at first. These  standards are in place to make the rules elements in this  book easier to recognize.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/2', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/17', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/2', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/3', 'PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/2` | 0.973918 | Throughout this rulebook, you will see formatting  standards that might look a bit unusual at first. These  standards are in place to make the rules elements in this  book easier to recognize. |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.659087 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` | 0.651874 | Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.597417 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1` | 0.570390 | FORMAT OF RULES |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/20` | 0.561269 | The back of this book has an  appendix with the rules for all of  the conditions that you will find  in the game. This section also  includes a blank character sheet,  and an index with a comprehensiv |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.539426 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.534135 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.533360 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5` | 0.509489 | READING RULES |

### Query 22
- Text: What is the rule about The names of specific statistics, skills, feats, actions,  and some other mechanical elements in Starfinder are  capitalized. This way, when you see the statement "a  Strike targets Armor Class," you know that both Strike and  Armor Class are referring to rules.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/3', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/5', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/3', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/4', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/3` | 1.014676 | The names of specific statistics, skills, feats, actions,  and some other mechanical elements in Starfinder are  capitalized. This way, when you see the statement "a  Strike targets Armor Class," you |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/5` | 0.656432 | Starfinder uses many terms that are typically expressed  as abbreviations, like AC for Armor Class, DC for Difficulty  Class, and HP for Hit Points. If you're ever confused about  a game term or an ab |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.630664 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/18` | 0.573724 | This important chapter contains  the universal rules needed to play  Starfinder, including rules for the  various modes of play, the basic  actions that every character can  perform, the rules for com |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/7` | 0.549289 | Characters and their adversaries affect the galaxy of  Starfinder by using actions and producing effects. This is  especially the case during encounters, when every action  counts. When you use an act |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/15` | 0.531521 | You might want to coordinate with other players when  forming your character concept. Your characters could have  something in common already; perhaps they are travelers  from the same home world, or |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/3` | 0.523567 | This section provides a step-by-step guide for creating a  character using the Starfinder rules, preceded by a guide to  help you understand attribute modifiers. These modifiers are a  critical part o |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/19` | 0.512463 | weapons, and other basic equipment. Your character's class  lists the types of weapons and armor with which they are  trained (or better!). Their weapons determine how much  damage they deal in combat |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/5` | 0.509290 | their past, and think about how and why they adventure.  You'll want to peruse Starfinder's available ancestries,  backgrounds, and classes. The summaries on pages 27–28  might help you match your con |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/4` | 0.508446 | This introduction is designed to help you understand the  basics of Starfinder. This chapter also includes the rules for  building and leveling up a character, as well as an example  of the character |

### Query 23
- Text: What is the rule about If a word or a phrase is italicized, it's describing a spell  or a magic item. This way, when you see the statement  "the radiation from an *atomic blast* lingers in the room",  you know that the words denote the *atomic blast* spell,  rather than a non-magical atomic blast.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/4', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/9', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/4', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/3', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/5']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/5` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/4` | 1.006747 | If a word or a phrase is italicized, it's describing a spell  or a magic item. This way, when you see the statement  "the radiation from an *atomic blast* lingers in the room",  you know that the word |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/9` | 0.549160 | Spells, tech items, and magic items use a similar format,  but their stat blocks contain a number of unique elements,  such as the possible magical traditions for a spell (see  Chapter 7 for more on r |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.532241 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/3` | 0.456951 | The names of specific statistics, skills, feats, actions,  and some other mechanical elements in Starfinder are  capitalized. This way, when you see the statement "a  Strike targets Armor Class," you |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/10/Text/21` | 0.441110 | You can choose to take on edicts and anathema to  reinforce your character's beliefs and guide how they'd  react in certain situations. **Edicts** are behaviors your  personal philosophy or code encou |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/3` | 0.435940 | Edicts and anathema can change during play as a character's  beliefs evolve, or as you realize that your character's actions  reflect a different set of values than you once thought.  In most cases, y |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/5` | 0.425509 | Starfinder uses many terms that are typically expressed  as abbreviations, like AC for Armor Class, DC for Difficulty  Class, and HP for Hit Points. If you're ever confused about  a game term or an ab |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.415258 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/12` | 0.408342 | Reactions use this symbol: [reaction]. These actions can be used even  when it's not your turn. You only get one reaction per encounter  round, and you can use it only when its specific trigger is  fu |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.402020 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |

### Query 24
- Text: What is the rule about Starfinder uses many terms that are typically expressed  as abbreviations, like AC for Armor Class, DC for Difficulty  Class, and HP for Hit Points. If you're ever confused about  a game term or an abbreviation, you can always turn to the  Glossary and Index, beginning on page 442, and look it up.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/5', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/3', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/5', 'PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/5` | 1.006913 | Starfinder uses many terms that are typically expressed  as abbreviations, like AC for Armor Class, DC for Difficulty  Class, and HP for Hit Points. If you're ever confused about  a game term or an ab |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/3` | 0.717146 | The names of specific statistics, skills, feats, actions,  and some other mechanical elements in Starfinder are  capitalized. This way, when you see the statement "a  Strike targets Armor Class," you |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/18` | 0.623988 | This important chapter contains  the universal rules needed to play  Starfinder, including rules for the  various modes of play, the basic  actions that every character can  perform, the rules for com |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.566486 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/5` | 0.550300 | their past, and think about how and why they adventure.  You'll want to peruse Starfinder's available ancestries,  backgrounds, and classes. The summaries on pages 27–28  might help you match your con |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/19` | 0.542975 | Select an ancestry for your character. The ancestry  summaries on page 27 provide an overview of Starfinder's  core ancestry options, and each is fully detailed in Chapter  2. Ancestry determines your |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/15` | 0.528216 | You might want to coordinate with other players when  forming your character concept. Your characters could have  something in common already; perhaps they are travelers  from the same home world, or |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/20` | 0.523224 | The back of this book has an  appendix with the rules for all of  the conditions that you will find  in the game. This section also  includes a blank character sheet,  and an index with a comprehensiv |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/4` | 0.507904 | This introduction is designed to help you understand the  basics of Starfinder. This chapter also includes the rules for  building and leveling up a character, as well as an example  of the character |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/3` | 0.503750 | This section provides a step-by-step guide for creating a  character using the Starfinder rules, preceded by a guide to  help you understand attribute modifiers. These modifiers are a  critical part o |

### Query 25
- Text: What is the rule about UNDERSTANDING ACTIONS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/16', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/5', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6` | 0.882417 | UNDERSTANDING ACTIONS |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/16` | 0.522488 | Activities are special tasks that you complete by spending  one or more of your actions together. Usually, an activity  uses two or more actions and lets you do more than a |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.516213 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/2` | 0.457762 | single action would allow. You have to spend all the actions  an activity requires for its effects to happen. Spellcasting  is one of the most common activities, as most spells take  more than a singl |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/8` | 0.452902 | Throughout this book, you will see special icons to  denote actions. |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.444586 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5` | 0.436688 | READING RULES |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/13` | 0.430477 | [free-action] Free Actions |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.425171 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/4` | 0.422298 | All tasks that take longer than a turn are activities. If an  activity is meant to be done during exploration, it has the  exploration trait. An activity that takes a day or more of  commitment and th |

### Query 26
- Text: What is the rule about Characters and their adversaries affect the galaxy of  Starfinder by using actions and producing effects. This is  especially the case during encounters, when every action  counts. When you use an action, you generate an effect.  This effect might be automatic, but sometimes actions  necessitate that you roll a die, and the effect is based on  what you rolled.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/7', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/18', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/7', 'PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/7` | 0.999977 | Characters and their adversaries affect the galaxy of  Starfinder by using actions and producing effects. This is  especially the case during encounters, when every action  counts. When you use an act |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/18` | 0.666931 | This important chapter contains  the universal rules needed to play  Starfinder, including rules for the  various modes of play, the basic  actions that every character can  perform, the rules for com |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.645562 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/1` | 0.601821 | Unless you're the GM, the first thing you need to do when playing Starfinder is create your character. It's  up to you to imagine your character's past experiences, personality, and view of the galaxy |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/15` | 0.597028 | You might want to coordinate with other players when  forming your character concept. Your characters could have  something in common already; perhaps they are travelers  from the same home world, or |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/3` | 0.585205 | The names of specific statistics, skills, feats, actions,  and some other mechanical elements in Starfinder are  capitalized. This way, when you see the statement "a  Strike targets Armor Class," you |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/3` | 0.570673 | This section provides a step-by-step guide for creating a  character using the Starfinder rules, preceded by a guide to  help you understand attribute modifiers. These modifiers are a  critical part o |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/4` | 0.570483 | This introduction is designed to help you understand the  basics of Starfinder. This chapter also includes the rules for  building and leveling up a character, as well as an example  of the character |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.555823 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/5` | 0.530978 | their past, and think about how and why they adventure.  You'll want to peruse Starfinder's available ancestries,  backgrounds, and classes. The summaries on pages 27–28  might help you match your con |

### Query 27
- Text: What is the rule about Throughout this book, you will see special icons to  denote actions.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/8', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/3', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/8', 'PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/9', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/8` | 0.930902 | Throughout this book, you will see special icons to  denote actions. |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.586495 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.563933 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.509021 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/10` | 0.465303 | Single actions use this symbol: [one-action]. They're the simplest,  most common type of action. You can use three single  actions on your turn in an encounter, in any order you see  fit. |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/14` | 0.465300 | Free actions use this symbol: [free-action]. Free actions don't require  you to spend any of your three single actions or your reaction.  A free action might have a trigger like a reaction does. If so |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.458245 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/2` | 0.451338 | Throughout this rulebook, you will see formatting  standards that might look a bit unusual at first. These  standards are in place to make the rules elements in this  book easier to recognize. |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` | 0.438923 | Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6` | 0.437384 | UNDERSTANDING ACTIONS |

### Query 28
- Text: What is the rule about [one-action] Single Actions?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/9', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/10', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/9', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/10', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/9` | 0.891407 | [one-action] Single Actions |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/10` | 0.738278 | Single actions use this symbol: [one-action]. They're the simplest,  most common type of action. You can use three single  actions on your turn in an encounter, in any order you see  fit. |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/2` | 0.613141 | single action would allow. You have to spend all the actions  an activity requires for its effects to happen. Spellcasting  is one of the most common activities, as most spells take  more than a singl |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.577862 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/16` | 0.559758 | Activities are special tasks that you complete by spending  one or more of your actions together. Usually, an activity  uses two or more actions and lets you do more than a |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.557530 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/10` | 0.553307 | **ACTION OR FEAT NAME **[one-action] **LEVEL** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/14` | 0.550700 | Free actions use this symbol: [free-action]. Free actions don't require  you to spend any of your three single actions or your reaction.  A free action might have a trigger like a reaction does. If so |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/13` | 0.507639 | [free-action] Free Actions |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6` | 0.498735 | UNDERSTANDING ACTIONS |

### Query 29
- Text: What is the rule about Single actions use this symbol: [one-action]. They're the simplest,  most common type of action. You can use three single  actions on your turn in an encounter, in any order you see  fit.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/10', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/3', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/10', 'PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/9', 'PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/10` | 0.989084 | Single actions use this symbol: [one-action]. They're the simplest,  most common type of action. You can use three single  actions on your turn in an encounter, in any order you see  fit. |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.745431 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/14` | 0.701759 | Free actions use this symbol: [free-action]. Free actions don't require  you to spend any of your three single actions or your reaction.  A free action might have a trigger like a reaction does. If so |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/9` | 0.663958 | [one-action] Single Actions |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/12` | 0.657592 | Reactions use this symbol: [reaction]. These actions can be used even  when it's not your turn. You only get one reaction per encounter  round, and you can use it only when its specific trigger is  fu |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/2` | 0.606849 | single action would allow. You have to spend all the actions  an activity requires for its effects to happen. Spellcasting  is one of the most common activities, as most spells take  more than a singl |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.600172 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/16` | 0.548928 | Activities are special tasks that you complete by spending  one or more of your actions together. Usually, an activity  uses two or more actions and lets you do more than a |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/18` | 0.503878 | Sometimes an ability will grant multiple actions or an  action in addition to other benefits. These are condensed  into a shorter format using the same categories, as seen  below. |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.493955 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |

### Query 30
- Text: What is the rule about [reaction] Reactions?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/12', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/10', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/11` | 0.785646 | [reaction] Reactions |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/12` | 0.649894 | Reactions use this symbol: [reaction]. These actions can be used even  when it's not your turn. You only get one reaction per encounter  round, and you can use it only when its specific trigger is  fu |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.514613 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.470325 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/14` | 0.451828 | Free actions use this symbol: [free-action]. Free actions don't require  you to spend any of your three single actions or your reaction.  A free action might have a trigger like a reaction does. If so |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.437313 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.432728 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.411415 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/10` | 0.408463 | Single actions use this symbol: [one-action]. They're the simplest,  most common type of action. You can use three single  actions on your turn in an encounter, in any order you see  fit. |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/13` | 0.406974 | [free-action] Free Actions |

### Query 31
- Text: What is the rule about Reactions use this symbol: [reaction]. These actions can be used even  when it's not your turn. You only get one reaction per encounter  round, and you can use it only when its specific trigger is  fulfilled. Often, the trigger is another creature's action.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/12', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/14', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/12', 'PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/12` | 0.983624 | Reactions use this symbol: [reaction]. These actions can be used even  when it's not your turn. You only get one reaction per encounter  round, and you can use it only when its specific trigger is  fu |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/14` | 0.769805 | Free actions use this symbol: [free-action]. Free actions don't require  you to spend any of your three single actions or your reaction.  A free action might have a trigger like a reaction does. If so |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/10` | 0.708040 | Single actions use this symbol: [one-action]. They're the simplest,  most common type of action. You can use three single  actions on your turn in an encounter, in any order you see  fit. |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.662452 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.614437 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.565227 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/14` | 0.536773 | **Frequency** The limit on how often you can use the ability. **Trigger** Reactions and some free actions have triggers that  must be met before they can be used. |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.505495 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/11` | 0.501462 | [reaction] Reactions |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.500608 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |

### Query 32
- Text: What is the rule about [free-action] Free Actions?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/14', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/14', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/13` | 0.874139 | [free-action] Free Actions |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/14` | 0.768934 | Free actions use this symbol: [free-action]. Free actions don't require  you to spend any of your three single actions or your reaction.  A free action might have a trigger like a reaction does. If so |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.644163 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.533683 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6` | 0.492455 | UNDERSTANDING ACTIONS |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.479032 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/14` | 0.473171 | **Frequency** The limit on how often you can use the ability. **Trigger** Reactions and some free actions have triggers that  must be met before they can be used. |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/16` | 0.465948 | Activities are special tasks that you complete by spending  one or more of your actions together. Usually, an activity  uses two or more actions and lets you do more than a |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/12` | 0.450334 | Reactions use this symbol: [reaction]. These actions can be used even  when it's not your turn. You only get one reaction per encounter  round, and you can use it only when its specific trigger is  fu |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/9` | 0.449317 | [one-action] Single Actions |

### Query 33
- Text: What is the rule about Free actions use this symbol: [free-action]. Free actions don't require  you to spend any of your three single actions or your reaction.  A free action might have a trigger like a reaction does. If so,  you can use it just like a reaction—even if it's not your turn.  However, you can use only one free action per trigger, so if  you have multiple free actions with the same trigger, you  have to decide which to use. If a free action doesn't have a  trigger, you use it like a single action, just without spending  any of your actions for the turn.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/14', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/3', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/12']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/14', 'PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/14` | 0.999778 | Free actions use this symbol: [free-action]. Free actions don't require  you to spend any of your three single actions or your reaction.  A free action might have a trigger like a reaction does. If so |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.763025 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/12` | 0.733411 | Reactions use this symbol: [reaction]. These actions can be used even  when it's not your turn. You only get one reaction per encounter  round, and you can use it only when its specific trigger is  fu |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/13` | 0.650392 | [free-action] Free Actions |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/10` | 0.647917 | Single actions use this symbol: [one-action]. They're the simplest,  most common type of action. You can use three single  actions on your turn in an encounter, in any order you see  fit. |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.635693 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/14` | 0.587252 | **Frequency** The limit on how often you can use the ability. **Trigger** Reactions and some free actions have triggers that  must be met before they can be used. |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/2` | 0.557552 | single action would allow. You have to spend all the actions  an activity requires for its effects to happen. Spellcasting  is one of the most common activities, as most spells take  more than a singl |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.557428 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/16` | 0.516431 | Activities are special tasks that you complete by spending  one or more of your actions together. Usually, an activity  uses two or more actions and lets you do more than a |

### Query 34
- Text: What is the rule about Activities?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/15', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/16', 'PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/15', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/14', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/15` | 0.699660 | Activities |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/16` | 0.678266 | Activities are special tasks that you complete by spending  one or more of your actions together. Usually, an activity  uses two or more actions and lets you do more than a |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6` | 0.551893 | UNDERSTANDING ACTIONS |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.506452 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.491706 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/2` | 0.480975 | single action would allow. You have to spend all the actions  an activity requires for its effects to happen. Spellcasting  is one of the most common activities, as most spells take  more than a singl |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/4` | 0.476690 | All tasks that take longer than a turn are activities. If an  activity is meant to be done during exploration, it has the  exploration trait. An activity that takes a day or more of  commitment and th |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1` | 0.454286 | FORMAT OF RULES |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.448508 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5` | 0.440854 | READING RULES |

### Query 35
- Text: What is the rule about Activities are special tasks that you complete by spending  one or more of your actions together. Usually, an activity  uses two or more actions and lets you do more than a?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/16', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/3', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/16', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/18', 'PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/15']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/15` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/16` | 0.953239 | Activities are special tasks that you complete by spending  one or more of your actions together. Usually, an activity  uses two or more actions and lets you do more than a |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.713514 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/2` | 0.705277 | single action would allow. You have to spend all the actions  an activity requires for its effects to happen. Spellcasting  is one of the most common activities, as most spells take  more than a singl |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/18` | 0.614925 | Sometimes an ability will grant multiple actions or an  action in addition to other benefits. These are condensed  into a shorter format using the same categories, as seen  below. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.581433 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.566939 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/4` | 0.549930 | All tasks that take longer than a turn are activities. If an  activity is meant to be done during exploration, it has the  exploration trait. An activity that takes a day or more of  commitment and th |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/10` | 0.544527 | Single actions use this symbol: [one-action]. They're the simplest,  most common type of action. You can use three single  actions on your turn in an encounter, in any order you see  fit. |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.543263 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/14` | 0.525016 | Free actions use this symbol: [free-action]. Free actions don't require  you to spend any of your three single actions or your reaction.  A free action might have a trigger like a reaction does. If so |

### Query 36
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/18', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/27', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/24']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/18', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/19', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/18` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/27` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/24` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/23` | 0.838541 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/28` | 0.838541 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/16` | 0.672734 | INTRODUCTION |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/3` | 0.646693 | CHAPTER 1: INTRODUCTION |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.608538 | **OVERVIEW** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/10` | 0.454028 | **Exploring the ** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/63` | 0.452320 | **GAME** |

### Query 37
- Text: What is the rule about **Character ** **Creation**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/19', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/25', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/28']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/19', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/20', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/19` | 0.851651 | **Character ** **Creation** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/25` | 0.851651 | **Character ** **Creation** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/28` | 0.851651 | **Character ** **Creation** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/3` | 0.809651 | **Character ** **Creation** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/29` | 0.809651 | **Character ** **Creation** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/24` | 0.809651 | **Character ** **Creation** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/17` | 0.669946 | Character Creation |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/6` | 0.546768 | Each player takes a different approach to creating a  character. Some want a character who will fit well into the  story, while others look for a combination of abilities that  complement each other m |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/3` | 0.539860 | This section provides a step-by-step guide for creating a  character using the Starfinder rules, preceded by a guide to  help you understand attribute modifiers. These modifiers are a  critical part o |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/10/Text/22` | 0.524572 | For most characters, these are entirely optional, though  it's best to consider taking some on as you create your |

### Query 38
- Text: Summarize **Leveling Up**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/20', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/30', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/20', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/21', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/20` | 0.970922 | **Leveling Up** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/30` | 0.970922 | **Leveling Up** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/29` | 0.970922 | **Leveling Up** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/4` | 0.928922 | **Leveling Up** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/25` | 0.928922 | **Leveling Up** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/26` | 0.928922 | **Leveling Up** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/SectionHeader/0` | 0.807826 | LEVELING UP |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/15/SectionHeader/11` | 0.661624 | **LEVELING-UP CHECKLIST** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/18` | 0.610760 | Leveling Up |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/10` | 0.369448 | **Exploring the ** |

### Query 39
- Text: Summarize **Exploring the ** **Galaxy**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/21', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/27', 'PZO22001 Starfinder Player Core 014-029::/page/15/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/21', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/20', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/21` | 0.993218 | **Exploring the ** **Galaxy** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/27` | 0.993218 | **Exploring the ** **Galaxy** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/26` | 0.993218 | **Exploring the ** **Galaxy** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/5` | 0.951218 | **Exploring the ** **Galaxy** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/30` | 0.951218 | **Exploring the ** **Galaxy** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/31` | 0.951218 | **Exploring the ** **Galaxy** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/19` | 0.802920 | Exploring the Galaxy |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/10` | 0.643308 | **Exploring the ** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/4` | 0.499391 | This introduction is designed to help you understand the  basics of Starfinder. This chapter also includes the rules for  building and leveling up a character, as well as an example  of the character |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/5` | 0.415618 | their past, and think about how and why they adventure.  You'll want to peruse Starfinder's available ancestries,  backgrounds, and classes. The summaries on pages 27–28  might help you match your con |

### Query 40
- Text: Summarize **Religion**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/22', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/28', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/32']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/22', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/21', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/22` | 0.921440 | **Religion** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/28` | 0.921440 | **Religion** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/32` | 0.921440 | **Religion** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/6` | 0.879440 | **Religion** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/31` | 0.879440 | **Religion** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/27` | 0.879440 | **Religion** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/20` | 0.661755 | Religion |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/9` | 0.438253 | **Constitution** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/11` | 0.391895 | **Intelligence** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/18` | 0.389000 | **INTRODUCTION** |

### Query 41
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/23']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/11/Text/32', 'PZO22001 Starfinder Player Core 014-029::/page/15/Text/28', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/23', 'PZO22001 Starfinder Player Core 014-029::/page/13/SectionHeader/27', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/24', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/33', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/29', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/7', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/32', 'PZO22001 Starfinder Player Core 014-029::/page/15/Text/28', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/22']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/13/SectionHeader/27` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/9/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/13/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/11/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/15/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/22` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/32` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/28` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/29` | 0.920820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/23` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/33` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/7` | 0.890820 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/21` | 0.822421 | ANCESTRIES & BACKGROUNDS |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/5` | 0.795553 | CHAPTER 2: ANCESTRIES &  BACKGROUNDS |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/8` | 0.683373 | ANCESTRY, BACKGROUND, CLASS,  OR DETAILS |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/13/SectionHeader/27` | 0.596190 | ANCESTRIES |

### Query 42
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/24', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/8', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/33']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/24', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/23', 'PZO22001 Starfinder Player Core 014-029::/page/15/Text/29', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/33', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/8', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/34', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/30', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/25']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/23` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/15/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/11/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/13/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/34` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/9/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/25` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/24` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/8` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/33` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/30` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/34` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/29` | 0.910061 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/7` | 0.799617 | CHAPTER 3: CLASSES |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/22` | 0.763092 | CLASSES |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.453104 | **OVERVIEW** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/10` | 0.444758 | STEP 7: RECORD CLASS DETAILS |

### Query 43
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/25', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/34', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/35']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/25', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/24', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/25` | 0.864442 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/34` | 0.864442 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/35` | 0.864442 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/9` | 0.822442 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/30` | 0.822442 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/31` | 0.822442 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/9` | 0.723723 | CHAPTER 4: SKILLS |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/23` | 0.712079 | SKILLS |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/13` | 0.712079 | SKILLS |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.553021 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |

### Query 44
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/26', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/35', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/32']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/26', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/25', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/25` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/26` | 0.871817 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/32` | 0.871817 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/35` | 0.871817 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/10` | 0.829817 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/36` | 0.829817 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/31` | 0.829817 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/11` | 0.701414 | CHAPTER 5: FEATS |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/24` | 0.651337 | FEATS |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.496661 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/12` | 0.464366 | FAITH |

### Query 45
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/27', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/37', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/33']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/27', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/28', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/28` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/27` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/37` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/33` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/32` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/13` | 0.829789 | CHAPTER 6: EQUIPMENT |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/25` | 0.824254 | EQUIPMENT |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/17` | 0.651834 | STEP 8: BUY EQUIPMENT |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/36` | 0.578761 | **EQUIPMENT** **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/11` | 0.578761 | **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/12/Text/18` | 0.462787 | Next up, Jessica turns to Chapter 6: Equipment. She's trained  in medium armor and chooses commercial freebooter  armor (which comes with a built-in comm unit, like most  armor). When it comes to weap |

### Query 46
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/28']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/15/Text/33', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/34', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/38']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/28', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/29', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/27']
- Expanded expected found: `True`
- Expanded expected rank: `4`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/27` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/33` | 0.889304 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/34` | 0.889304 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/38` | 0.889304 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/28` | 0.847304 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/26` | 0.776591 | SPELLS |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/15` | 0.771530 | CHAPTER 7: SPELLS |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/11` | 0.759411 | **EQUIPMENT** **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/36` | 0.759411 | **EQUIPMENT** **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/11/SectionHeader/18` | 0.687562 | **SPELLS AND SPELLCASTING** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/34` | 0.388254 | **SKILLS** |

### Query 47
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/29', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/37', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/39']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/29', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/30', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/28']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/28` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/29` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/37` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/39` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/35` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/34` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/12` | 0.811006 | **PLAYING THE ** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/27` | 0.749688 | PLAYING THE GAME |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/17` | 0.724027 | CHAPTER 8:  PLAYING THE  GAME |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/63` | 0.663024 | **GAME** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/10` | 0.482709 | **Exploring the ** |

### Query 48
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/30', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/36', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/30', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/29', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/31', 'PZO22001 Starfinder Player Core 014-029::/page/15/Text/35', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/40', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/36', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/38', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/15/Text/35` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/9/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/11/Text/38` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/13/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/30` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/13` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/36` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/38` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/40` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/35` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/28` | 0.837763 | CONDITIONS APPENDIX |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/19` | 0.570754 | APPENDICES |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/20` | 0.426695 | The back of this book has an  appendix with the rules for all of  the conditions that you will find  in the game. This section also  includes a blank character sheet,  and an index with a comprehensiv |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/7` | 0.416141 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 49
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/31', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/37', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/31', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/2', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/31` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/14` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/37` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/39` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/41` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/36` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/29` | 0.825490 | GLOSSARY & INDEX |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.427174 | **OVERVIEW** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/34` | 0.385404 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/24` | 0.385404 | **CLASSES** |

### Query 50
- Text: What is the rule about single action would allow. You have to spend all the actions  an activity requires for its effects to happen. Spellcasting  is one of the most common activities, as most spells take  more than a single action to cast.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/2', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/16', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/2', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/3', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/31']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/2` | 0.988889 | single action would allow. You have to spend all the actions  an activity requires for its effects to happen. Spellcasting  is one of the most common activities, as most spells take  more than a singl |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/16` | 0.677885 | Activities are special tasks that you complete by spending  one or more of your actions together. Usually, an activity  uses two or more actions and lets you do more than a |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.663086 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/10` | 0.604084 | Single actions use this symbol: [one-action]. They're the simplest,  most common type of action. You can use three single  actions on your turn in an encounter, in any order you see  fit. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/14` | 0.572004 | Free actions use this symbol: [free-action]. Free actions don't require  you to spend any of your three single actions or your reaction.  A free action might have a trigger like a reaction does. If so |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/16` | 0.563246 | This chapter starts with rules for casting spells,  determining their effects, and negating foes' spells  (called counteracting). After that, the spell lists for  each spellcasting tradition are inclu |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.562663 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/9` | 0.544940 | [one-action] Single Actions |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.513899 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/18` | 0.502394 | Sometimes an ability will grant multiple actions or an  action in addition to other benefits. These are condensed  into a shorter format using the same categories, as seen  below. |

### Query 51
- Text: What is the rule about Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you can cast in an instant, which use a free action  or a reaction.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/3', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/14', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/3', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/2', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.994963 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/14` | 0.756876 | Free actions use this symbol: [free-action]. Free actions don't require  you to spend any of your three single actions or your reaction.  A free action might have a trigger like a reaction does. If so |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/10` | 0.706017 | Single actions use this symbol: [one-action]. They're the simplest,  most common type of action. You can use three single  actions on your turn in an encounter, in any order you see  fit. |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/16` | 0.648220 | Activities are special tasks that you complete by spending  one or more of your actions together. Usually, an activity  uses two or more actions and lets you do more than a |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/2` | 0.623746 | single action would allow. You have to spend all the actions  an activity requires for its effects to happen. Spellcasting  is one of the most common activities, as most spells take  more than a singl |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/12` | 0.623564 | Reactions use this symbol: [reaction]. These actions can be used even  when it's not your turn. You only get one reaction per encounter  round, and you can use it only when its specific trigger is  fu |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.613613 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.560636 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.544331 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/18` | 0.543350 | Sometimes an ability will grant multiple actions or an  action in addition to other benefits. These are condensed  into a shorter format using the same categories, as seen  below. |

### Query 52
- Text: What is the rule about All tasks that take longer than a turn are activities. If an  activity is meant to be done during exploration, it has the  exploration trait. An activity that takes a day or more of  commitment and that can be done only during downtime  has the downtime trait.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/4', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/16', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/4', 'PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/4` | 1.004502 | All tasks that take longer than a turn are activities. If an  activity is meant to be done during exploration, it has the  exploration trait. An activity that takes a day or more of  commitment and th |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/16` | 0.575219 | Activities are special tasks that you complete by spending  one or more of your actions together. Usually, an activity  uses two or more actions and lets you do more than a |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.549839 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/2` | 0.477042 | single action would allow. You have to spend all the actions  an activity requires for its effects to happen. Spellcasting  is one of the most common activities, as most spells take  more than a singl |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.468291 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.459803 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/14` | 0.458213 | **Frequency** The limit on how often you can use the ability. **Trigger** Reactions and some free actions have triggers that  must be met before they can be used. |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.443956 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/18` | 0.439938 | Sometimes an ability will grant multiple actions or an  action in addition to other benefits. These are condensed  into a shorter format using the same categories, as seen  below. |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.439295 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |

### Query 53
- Text: Summarize READING RULES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5', 'PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/4', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/4` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5` | 0.944001 | READING RULES |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1` | 0.595311 | FORMAT OF RULES |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/2` | 0.532335 | Throughout this rulebook, you will see formatting  standards that might look a bit unusual at first. These  standards are in place to make the rules elements in this  book easier to recognize. |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.382932 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/20` | 0.370078 | The back of this book has an  appendix with the rules for all of  the conditions that you will find  in the game. This section also  includes a blank character sheet,  and an index with a comprehensiv |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` | 0.362944 | Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.345436 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.337578 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.334918 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/18` | 0.334150 | This important chapter contains  the universal rules needed to play  Starfinder, including rules for the  various modes of play, the basic  actions that every character can  perform, the rules for com |

### Query 54
- Text: What is the rule about This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an individual character often has special  rules that empower them to do things most other characters  can't. Most of these options are granted by feats, which are  gained by making certain choices at character creation or  when a character advances in level.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/6', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/8', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/6', 'PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.978253 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.763444 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.725492 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/12` | 0.675939 | As a character advances in level, they gain additional feats  to represent their growing abilities. General feats and skill  feats (which are a subset of general feats) are presented  in this chapter. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/6/Text/9` | 0.657254 | At this point, you need to decide your character's class. A class gives your character access to a suite of heroic abilities, determines how effectively they fight, and governs how easily they can sha |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.656515 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/20` | 0.638126 | The back of this book has an  appendix with the rules for all of  the conditions that you will find  in the game. This section also  includes a blank character sheet,  and an index with a comprehensiv |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.637833 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` | 0.637812 | Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.631724 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |

### Query 55
- Text: What is the rule about Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules element to life during play.  Where appropriate, rules presentations are introduced  with an explanation of their format. For example, the  Ancestry section of Chapter 2 contains rules for the ten  ancestries in this book, and an explanation of the ancestry  sections appears at the beginning of that chapter.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/7', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/8', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/7', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/8', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` | 1.008621 | Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.751545 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/20` | 0.702842 | The back of this book has an  appendix with the rules for all of  the conditions that you will find  in the game. This section also  includes a blank character sheet,  and an index with a comprehensiv |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/9` | 0.618077 | Spells, tech items, and magic items use a similar format,  but their stat blocks contain a number of unique elements,  such as the possible magical traditions for a spell (see  Chapter 7 for more on r |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/2` | 0.614107 | Throughout this rulebook, you will see formatting  standards that might look a bit unusual at first. These  standards are in place to make the rules elements in this  book easier to recognize. |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.611720 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.601994 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.594367 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.580615 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.576080 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |

### Query 56
- Text: What is the rule about The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, reactions, and free actions  each have the corresponding icon next to their name to  indicate their type. An activity that can be completed in  a single turn has a symbol indicating how many actions  are needed to complete it; activities that take longer to  perform omit these icons. If a character must attain a  certain level before accessing an ability, that level is  indicated to the right of the stat block's name. Rules also  often have traits associated with them (traits appear in the  Glossary and Index).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/8', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/7', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/8', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/7', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 1.008164 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` | 0.754058 | Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/9` | 0.642658 | Spells, tech items, and magic items use a similar format,  but their stat blocks contain a number of unique elements,  such as the possible magical traditions for a spell (see  Chapter 7 for more on r |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.593307 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.578145 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.577236 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.575828 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/20` | 0.573294 | The back of this book has an  appendix with the rules for all of  the conditions that you will find  in the game. This section also  includes a blank character sheet,  and an index with a comprehensiv |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.572658 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/14` | 0.563365 | Free actions use this symbol: [free-action]. Free actions don't require  you to spend any of your three single actions or your reaction.  A free action might have a trigger like a reaction does. If so |

### Query 57
- Text: What is the rule about Spells, tech items, and magic items use a similar format,  but their stat blocks contain a number of unique elements,  such as the possible magical traditions for a spell (see  Chapter 7 for more on reading spells).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/9', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/7', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/9', 'PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/10', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/9` | 0.988295 | Spells, tech items, and magic items use a similar format,  but their stat blocks contain a number of unique elements,  such as the possible magical traditions for a spell (see  Chapter 7 for more on r |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` | 0.681062 | Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.662831 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/16` | 0.550786 | This chapter starts with rules for casting spells,  determining their effects, and negating foes' spells  (called counteracting). After that, the spell lists for  each spellcasting tradition are inclu |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/2` | 0.533712 | Throughout this rulebook, you will see formatting  standards that might look a bit unusual at first. These  standards are in place to make the rules elements in this  book easier to recognize. |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/4` | 0.525226 | If a word or a phrase is italicized, it's describing a spell  or a magic item. This way, when you see the statement  "the radiation from an *atomic blast* lingers in the room",  you know that the word |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/19` | 0.516030 | Many characters can learn a few cantrips or focus spells,  but the mystic and witchwarper gain spellcasting—the  ability to cast a wide variety of spells. If your character's  class grants spells, you |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.514240 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/17` | 0.511165 | Add spells and spell slots if your class grants  spellcasting. See Chapter 7 for spells. |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.510507 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |

### Query 58
- Text: What is the rule about **ACTION OR FEAT NAME **[one-action] **LEVEL**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/10', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/19', 'PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/9']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/10', 'PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/12', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/10` | 0.942835 | **ACTION OR FEAT NAME **[one-action] **LEVEL** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.629955 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/9` | 0.604993 | [one-action] Single Actions |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/10` | 0.574642 | Single actions use this symbol: [one-action]. They're the simplest,  most common type of action. You can use three single  actions on your turn in an encounter, in any order you see  fit. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.546993 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.507652 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.488523 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/16` | 0.477643 | Activities are special tasks that you complete by spending  one or more of your actions together. Usually, an activity  uses two or more actions and lets you do more than a |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/14` | 0.476658 | Free actions use this symbol: [free-action]. Free actions don't require  you to spend any of your three single actions or your reaction.  A free action might have a trigger like a reaction does. If so |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/12` | 0.472929 | Reactions use this symbol: [reaction]. These actions can be used even  when it's not your turn. You only get one reaction per encounter  round, and you can use it only when its specific trigger is  fu |

### Query 59
- Text: What is the rule about **TRAITS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/12', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/17', 'PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/11']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/12', 'PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/10', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/10` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/12` | 0.859807 | **TRAITS** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.550153 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/11` | 0.535444 | **Attribute Flaws** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/13` | 0.478178 | **Prerequisites** Any minimum attributes, feats, proficiency  ranks, and so forth you must have to select this rules  element are here. Feats also have a level prerequisite,  listed above. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/25` | 0.458828 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/9` | 0.458828 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/31` | 0.458828 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/30` | 0.458828 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/34` | 0.458828 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/35` | 0.458828 | **SKILLS** |

### Query 60
- Text: What are the requirements for **Prerequisites** Any minimum attributes, feats, proficiency  ranks, and so forth you must have to select this rules  element are here. Feats also have a level prerequisite,  listed above.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/13', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/15', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/13', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/14', 'PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/12']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/12` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/13` | 0.980508 | **Prerequisites** Any minimum attributes, feats, proficiency  ranks, and so forth you must have to select this rules  element are here. Feats also have a level prerequisite,  listed above. |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/15` | 0.671962 | **Requirements** Sometimes you must have a certain item or  be in a certain circumstance to use an ability. |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.600743 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.548586 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/16` | 0.536226 | Select feats as indicated on your class advancement  table. For ancestry feats, see Chapter 2. For class  feats, see your class entry in Chapter 3. For general  feats and skill feats, see Chapter 5. |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/12` | 0.528779 | As a character advances in level, they gain additional feats  to represent their growing abilities. General feats and skill  feats (which are a subset of general feats) are presented  in this chapter. |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.522710 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/6/Text/10` | 0.516718 | You don't need to write down all of your character's class features yet. You simply need to know which class you want to play, which determines the attribute modifiers that will be most important for |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/19` | 0.505254 | At this point, you need to start building your character's  attribute modifiers. See the overview of attribute modifiers  on page 23 for more information about these important  aspects of your charact |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/19` | 0.492019 | Adjust bonuses from feats and other abilities that  are based on your level. |

### Query 61
- Text: What is the rule about **Frequency** The limit on how often you can use the ability. **Trigger** Reactions and some free actions have triggers that  must be met before they can be used.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/14', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/19', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/14', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/15', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/14` | 0.949598 | **Frequency** The limit on how often you can use the ability. **Trigger** Reactions and some free actions have triggers that  must be met before they can be used. |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.752749 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/14` | 0.623455 | Free actions use this symbol: [free-action]. Free actions don't require  you to spend any of your three single actions or your reaction.  A free action might have a trigger like a reaction does. If so |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/15` | 0.570590 | **Requirements** Sometimes you must have a certain item or  be in a certain circumstance to use an ability. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.550034 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/12` | 0.512844 | Reactions use this symbol: [reaction]. These actions can be used even  when it's not your turn. You only get one reaction per encounter  round, and you can use it only when its specific trigger is  fu |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.512010 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.500213 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/16` | 0.492160 | Activities are special tasks that you complete by spending  one or more of your actions together. Usually, an activity  uses two or more actions and lets you do more than a |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.490193 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |

### Query 62
- Text: What is the rule about **Requirements** Sometimes you must have a certain item or  be in a certain circumstance to use an ability.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/15', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/13', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/15', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/14', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/15` | 0.925922 | **Requirements** Sometimes you must have a certain item or  be in a certain circumstance to use an ability. |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/13` | 0.635971 | **Prerequisites** Any minimum attributes, feats, proficiency  ranks, and so forth you must have to select this rules  element are here. Feats also have a level prerequisite,  listed above. |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.598594 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/14` | 0.528843 | **Frequency** The limit on how often you can use the ability. **Trigger** Reactions and some free actions have triggers that  must be met before they can be used. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.523635 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.516582 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.494328 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.478402 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.476827 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.462494 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |

### Query 63
- Text: What is the rule about This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or grants a constant effect, the benefit is  explained here.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/16', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/17', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/19']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/16', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/15', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 1.003488 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.765987 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.628986 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/18` | 0.584970 | Sometimes an ability will grant multiple actions or an  action in addition to other benefits. These are condensed  into a shorter format using the same categories, as seen  below. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` | 0.576989 | Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.569709 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.568070 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.532524 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/20` | 0.528039 | modifier, recalculate their maximum Hit  Points using their new Constitution modifier  (typically, this adds 1 Hit Point per level). If  an attribute boost increases your character's  Intelligence mod |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.524073 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |

### Query 64
- Text: What is the rule about **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/17', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/16', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/17', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/18', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.979188 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.628392 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.595885 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/12` | 0.550555 | As a character advances in level, they gain additional feats  to represent their growing abilities. General feats and skill  feats (which are a subset of general feats) are presented  in this chapter. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/13` | 0.543851 | **Prerequisites** Any minimum attributes, feats, proficiency  ranks, and so forth you must have to select this rules  element are here. Feats also have a level prerequisite,  listed above. |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.534718 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/16` | 0.525023 | Select feats as indicated on your class advancement  table. For ancestry feats, see Chapter 2. For class  feats, see your class entry in Chapter 3. For general  feats and skill feats, see Chapter 5. |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/16` | 0.514065 | This chapter starts with rules for casting spells,  determining their effects, and negating foes' spells  (called counteracting). After that, the spell lists for  each spellcasting tradition are inclu |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.512779 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/15` | 0.509938 | **Requirements** Sometimes you must have a certain item or  be in a certain circumstance to use an ability. |

### Query 65
- Text: What is the rule about Sometimes an ability will grant multiple actions or an  action in addition to other benefits. These are condensed  into a shorter format using the same categories, as seen  below.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/18', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/16', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/18', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/19', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/18` | 0.984033 | Sometimes an ability will grant multiple actions or an  action in addition to other benefits. These are condensed  into a shorter format using the same categories, as seen  below. |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.664187 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/16` | 0.662630 | Activities are special tasks that you complete by spending  one or more of your actions together. Usually, an activity  uses two or more actions and lets you do more than a |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.625463 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.617830 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.581880 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.566346 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/14` | 0.525303 | Free actions use this symbol: [free-action]. Free actions don't require  you to spend any of your three single actions or your reaction.  A free action might have a trigger like a reaction does. If so |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/14` | 0.511236 | **Frequency** The limit on how often you can use the ability. **Trigger** Reactions and some free actions have triggers that  must be met before they can be used. |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/2` | 0.507302 | single action would allow. You have to spend all the actions  an activity requires for its effects to happen. Spellcasting  is one of the most common activities, as most spells take  more than a singl |

### Query 66
- Text: What is the rule about **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed here; **Effect** this section explains  how the ability changes the world.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/19', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/14', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/16']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/19', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/18', 'PZO22001 Starfinder Player Core 014-029::/page/3/Text/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/18` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/3/Text/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.941097 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/14` | 0.765257 | **Frequency** The limit on how often you can use the ability. **Trigger** Reactions and some free actions have triggers that  must be met before they can be used. |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.688759 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.647129 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.644687 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/14` | 0.637968 | Free actions use this symbol: [free-action]. Free actions don't require  you to spend any of your three single actions or your reaction.  A free action might have a trigger like a reaction does. If so |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/12` | 0.607107 | Reactions use this symbol: [reaction]. These actions can be used even  when it's not your turn. You only get one reaction per encounter  round, and you can use it only when its specific trigger is  fu |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.606035 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/15` | 0.585008 | **Requirements** Sometimes you must have a certain item or  be in a certain circumstance to use an ability. |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/18` | 0.578996 | Sometimes an ability will grant multiple actions or an  action in addition to other benefits. These are condensed  into a shorter format using the same categories, as seen  below. |

### Query 67
- Text: What is the rule about Unless you're the GM, the first thing you need to do when playing Starfinder is create your character. It's  up to you to imagine your character's past experiences, personality, and view of the galaxy, and this will  set the stage for your roleplaying during the game. You'll use the game's mechanics to determine your  character's ability to perform various tasks and use special abilities.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/3/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/3/Text/1', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/18', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/3/Text/1', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/19', 'PZO22001 Starfinder Player Core 014-029::/page/3/Text/3']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/3/Text/3` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/1` | 0.984092 | Unless you're the GM, the first thing you need to do when playing Starfinder is create your character. It's  up to you to imagine your character's past experiences, personality, and view of the galaxy |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/18` | 0.791093 | This important chapter contains  the universal rules needed to play  Starfinder, including rules for the  various modes of play, the basic  actions that every character can  perform, the rules for com |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.770033 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/3` | 0.731147 | This section provides a step-by-step guide for creating a  character using the Starfinder rules, preceded by a guide to  help you understand attribute modifiers. These modifiers are a  critical part o |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/15` | 0.713904 | You might want to coordinate with other players when  forming your character concept. Your characters could have  something in common already; perhaps they are travelers  from the same home world, or |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/4` | 0.711974 | This introduction is designed to help you understand the  basics of Starfinder. This chapter also includes the rules for  building and leveling up a character, as well as an example  of the character |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/12/Text/2` | 0.687651 | This step-by-step example illustrates the process of  creating a Starfinder character. |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/5` | 0.674620 | their past, and think about how and why they adventure.  You'll want to peruse Starfinder's available ancestries,  backgrounds, and classes. The summaries on pages 27–28  might help you match your con |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/7` | 0.641048 | Characters and their adversaries affect the galaxy of  Starfinder by using actions and producing effects. This is  especially the case during encounters, when every action  counts. When you use an act |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/9` | 0.567640 | Write down the deity your character worships, if any.  Your character might worship several deities as part of a  personal pantheon. You might instead choose a philosophy  or decide your character is |

### Query 68
- Text: What is the rule about This section provides a step-by-step guide for creating a  character using the Starfinder rules, preceded by a guide to  help you understand attribute modifiers. These modifiers are a  critical part of your character, and you will be asked to make  choices about them during many of the following steps. The  steps of character creation are presented in a suggested order,  but you can complete them in whatever order you prefer.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/3/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/3/Text/3', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/2', 'PZO22001 Starfinder Player Core 014-029::/page/12/Text/2']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/3/Text/3', 'PZO22001 Starfinder Player Core 014-029::/page/3/Text/1', 'PZO22001 Starfinder Player Core 014-029::/page/3/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/3/Text/1` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/3/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/3` | 1.010380 | This section provides a step-by-step guide for creating a  character using the Starfinder rules, preceded by a guide to  help you understand attribute modifiers. These modifiers are a  critical part o |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.854659 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/12/Text/2` | 0.813305 | This step-by-step example illustrates the process of  creating a Starfinder character. |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/4` | 0.748979 | This introduction is designed to help you understand the  basics of Starfinder. This chapter also includes the rules for  building and leveling up a character, as well as an example  of the character |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/19` | 0.745836 | At this point, you need to start building your character's  attribute modifiers. See the overview of attribute modifiers  on page 23 for more information about these important  aspects of your charact |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/1` | 0.720923 | Unless you're the GM, the first thing you need to do when playing Starfinder is create your character. It's  up to you to imagine your character's past experiences, personality, and view of the galaxy |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/18` | 0.710939 | This important chapter contains  the universal rules needed to play  Starfinder, including rules for the  various modes of play, the basic  actions that every character can  perform, the rules for com |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/15` | 0.690472 | You might want to coordinate with other players when  forming your character concept. Your characters could have  something in common already; perhaps they are travelers  from the same home world, or |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/2` | 0.672852 | One of the most important aspects of your character is their attribute modifiers. These numbers represent your  character's raw potential, and they influence nearly every other statistic on your chara |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/2` | 0.651187 | Each attribute modifier starts at +0, representing the average. As you make character choices, you'll adjust these  modifiers by applying attribute boosts, which increase an attribute modifier, and at |

### Query 69
- Text: Summarize STEP 1: CREATE A CONCEPT
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/3/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/3/SectionHeader/7', 'PZO22001 Starfinder Player Core 014-029::/page/4/Text/7', 'PZO22001 Starfinder Player Core 014-029::/page/4/Text/17']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/3/SectionHeader/7', 'PZO22001 Starfinder Player Core 014-029::/page/3/Text/6', 'PZO22001 Starfinder Player Core 014-029::/page/3/Text/8']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/3/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/3/Text/8` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/3/SectionHeader/7` | 0.997395 | STEP 1: CREATE A CONCEPT |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/7` | 0.531407 | Once you have a good idea of the character you'd like to  play, move on to Step 2 to start building your character. |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/17` | 0.529341 | Once you've developed your character's concept, jot  down a few sentences summarizing your ideas under  the Notes section on the third page of your character  sheet. Record any of the details you've a |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/3` | 0.471827 | STEPS 1 AND 2 |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/19` | 0.434387 | **Character ** **Creation** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/29` | 0.434387 | **Character ** **Creation** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/25` | 0.434387 | **Character ** **Creation** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/28` | 0.434387 | **Character ** **Creation** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/3` | 0.434387 | **Character ** **Creation** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/24` | 0.434387 | **Character ** **Creation** |

### Query 70
- Text: Summarize **Exploring the **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/3/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/3/Text/10', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/21', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/31']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/3/Text/10', 'PZO22001 Starfinder Player Core 014-029::/page/3/Text/8', 'PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/3/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/10` | 0.937169 | **Exploring the ** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/21` | 0.623010 | **Exploring the ** **Galaxy** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/31` | 0.623010 | **Exploring the ** **Galaxy** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/30` | 0.581010 | **Exploring the ** **Galaxy** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/5` | 0.581010 | **Exploring the ** **Galaxy** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/27` | 0.581010 | **Exploring the ** **Galaxy** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/26` | 0.581010 | **Exploring the ** **Galaxy** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/12` | 0.469192 | **PLAYING THE ** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/19` | 0.467474 | Exploring the Galaxy |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/18` | 0.452331 | **INTRODUCTION** |

### Query 71
- Text: Summarize **OVERVIEW**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/18', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/24']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1', 'PZO22001 Starfinder Player Core 014-029::/page/4/Text/2', 'PZO22001 Starfinder Player Core 014-029::/page/3/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/4/Text/2` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/3/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.817106 | **OVERVIEW** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/18` | 0.638354 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/24` | 0.638354 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/28` | 0.596354 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/27` | 0.596354 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/23` | 0.596354 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/33` | 0.433247 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/7` | 0.433247 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/29` | 0.433247 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/32` | 0.433247 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 72
- Text: Summarize FAITH
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/12', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/11', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/10']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/12', 'PZO22001 Starfinder Player Core 014-029::/page/4/Text/13', 'PZO22001 Starfinder Player Core 014-029::/page/4/Text/11']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/4/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/4/Text/11` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/12` | 0.916150 | FAITH |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/11` | 0.606646 | CHAPTER 5: FEATS |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/10` | 0.577047 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/26` | 0.535047 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/35` | 0.535047 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/36` | 0.535047 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/31` | 0.535047 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/32` | 0.535047 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/24` | 0.533550 | FEATS |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/10` | 0.353521 | **ACTION OR FEAT NAME **[one-action] **LEVEL** |

### Query 73
- Text: Summarize YOUR ALLIES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/14', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/19', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/14', 'PZO22001 Starfinder Player Core 014-029::/page/4/Text/15', 'PZO22001 Starfinder Player Core 014-029::/page/4/Text/13']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/4/Text/15` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/4/Text/13` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/14` | 0.905273 | YOUR ALLIES |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/19` | 0.432779 | Select an ancestry for your character. The ancestry  summaries on page 27 provide an overview of Starfinder's  core ancestry options, and each is fully detailed in Chapter  2. Ancestry determines your |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/6` | 0.408888 | The rules for ancestries and heritages representing the  Pact Worlds are in this chapter, including their ancestry  feat options. Backgrounds are at the end of this chapter,  along with a section abou |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/5` | 0.365447 | their past, and think about how and why they adventure.  You'll want to peruse Starfinder's available ancestries,  backgrounds, and classes. The summaries on pages 27–28  might help you match your con |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/21` | 0.344012 | Pick the ancestry itself. |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/22` | 0.342573 | Select a heritage from those available within that  ancestry, further defining the traits your character was  born with. |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/26` | 0.329020 | Write your character's ancestry and heritage in the  appropriate space at the top of your character sheet's  first page. Adjust your attribute modifiers, adding  1 to an attribute modifier if you gain |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/3` | 0.326986 | **Ancestry:** Each ancestry provides attribute boosts, and sometimes an attribute flaw. If you're taking any voluntary  flaws, apply them in this step (see the sidebar on page 25). |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/20` | 0.325983 | You'll have four decisions to make when you choosing your  character's ancestry. |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/5` | 0.315036 | CHAPTER 2: ANCESTRIES &  BACKGROUNDS |

### Query 74
- Text: Summarize **Strength**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/5', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/53', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/5', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/6', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/4']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/6` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/4` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/5` | 0.952973 | **Strength** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/53` | 0.587377 | Wisdom Strength |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/6` | 0.516744 | Strength measures your character's physical power, and  is important if your character plans to engage in hand-tohand combat. Your Strength modifier gets added to melee  damage rolls and determines ho |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/10/Text/12` | 0.423788 | Strength for melee Strikes and Dexterity for ranged  Strikes). You also add any item bonus from the weapon  and any other permanent bonuses or penalties. You also  need to calculate how much damage ea |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/7` | 0.401049 | **Dexterity** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/12/Text/10` | 0.399169 | Jessica writes "solarian" on the class line of her character  sheet and fills in the number 1 in the level box. The solarian  class grants an attribute boost to its key attribute, which is  Strength, |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/12/Text/12` | 0.396740 | Jessica applies four more attribute boosts to determine her  starting attribute modifiers. After giving it some thought,  she applies them to Strength (raising it to +4), since that's  the most import |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/11` | 0.381576 | **Intelligence** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/25` | 0.381376 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/35` | 0.381376 | **SKILLS** |

### Query 75
- Text: Summarize **Dexterity**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/7', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/26', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/8']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/7', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/8', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/6']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/6` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/7` | 0.967620 | **Dexterity** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/26` | 0.644378 | Charisma Dexterity — Charisma |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/8` | 0.539665 | Dexterity measures your character's agility, balance, and  reflexes, and is important if your character plans to make  attacks with ranged weapons or use stealth to surprise  foes. Your Dexterity modi |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/38` | 0.459595 | Charisma, Free Dexterity, Charisma, Free Constitution, Wisdom, Free Dexterity, Charisma, Free |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/5` | 0.416310 | **Strength** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/11/SectionHeader/8` | 0.385614 | DEITY |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/58` | 0.376706 | Constitution, Strength, Free Dexterity, Charisma, Free Borais are corpses reanimated  by their own souls, both living  and undead. Page 84. |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/22` | 0.370371 | Dexterity, Intelligence, Free Constitution, Wisdom, Free Two free attribute boosts Strength, Wisdom, Free |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/23` | 0.364608 | Your character's Armor Class represents how difficult they  are to hit in combat. To calculate your AC, add 10 plus your  character's Dexterity modifier (up to their armor's Dexterity  modifier cap; p |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.353222 | **OVERVIEW** |

### Query 76
- Text: Summarize **Constitution**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/9', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/10', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/22']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/9', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/8', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/9` | 0.919836 | **Constitution** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/10` | 0.482471 | Constitution measures your character's health and stamina,  and is important for all characters, especially those who  fight in close range. Your Constitution modifier is added to  your Hit Points and |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/22` | 0.482347 | **Religion** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/32` | 0.440347 | **Religion** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/6` | 0.440347 | **Religion** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/27` | 0.440347 | **Religion** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/31` | 0.440347 | **Religion** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/28` | 0.440347 | **Religion** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/42` | 0.409839 | — Constitution Charisma Wisdom |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/24` | 0.404615 | **INTRODUCTION** |

### Query 77
- Text: Summarize **Intelligence**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/11', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/12', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/34']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/11', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/12', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/10']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/10` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/11` | 0.938536 | **Intelligence** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/12` | 0.573012 | Intelligence measures how well your character can learn  and reason. A high Intelligence allows your character to  analyze situations and understand patterns, and it means  they can become trained in |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/34` | 0.496909 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/9` | 0.454909 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/25` | 0.454909 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/35` | 0.454909 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/30` | 0.454909 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/31` | 0.454909 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/9` | 0.452170 | CHAPTER 4: SKILLS |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/22` | 0.409405 | Dexterity, Intelligence, Free Constitution, Wisdom, Free Two free attribute boosts Strength, Wisdom, Free |

### Query 78
- Text: Summarize **Wisdom**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/13', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/53', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/42']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/13', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/12', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/14']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/14` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/13` | 0.928886 | **Wisdom** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/53` | 0.486797 | Wisdom Strength |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/42` | 0.478626 | — Constitution Charisma Wisdom |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/14` | 0.431488 | Wisdom measures your character's common sense,  awareness, and intuition. High Wisdom helps your  character detect hidden things and resist mental effects.  Your Wisdom modifier is added to your Perce |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/38` | 0.399524 | Charisma, Free Dexterity, Charisma, Free Constitution, Wisdom, Free Dexterity, Charisma, Free |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.388007 | **OVERVIEW** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/22` | 0.387192 | **Religion** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/32` | 0.387192 | **Religion** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/28` | 0.387192 | **Religion** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/6` | 0.387192 | **Religion** |

### Query 79
- Text: Summarize **Charisma**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/15', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/42', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/38']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/15', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/14', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/16']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/16` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/15` | 0.950174 | **Charisma** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/42` | 0.703456 | — Constitution Charisma Wisdom |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/38` | 0.652377 | Charisma, Free Dexterity, Charisma, Free Constitution, Wisdom, Free Dexterity, Charisma, Free |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/26` | 0.609900 | Charisma Dexterity — Charisma |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/16` | 0.588594 | Charisma measures your character's personal magnetism  and strength of personality. A high Charisma modifier  helps you build relationships and influence the thoughts  and moods of others with social |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/28` | 0.410541 | **Character ** **Creation** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/3` | 0.410541 | **Character ** **Creation** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/19` | 0.410541 | **Character ** **Creation** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/25` | 0.410541 | **Character ** **Creation** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/29` | 0.410541 | **Character ** **Creation** |

### Query 80
- Text: Summarize STEP 3: SELECT AN ANCESTRY
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/18', 'PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/8', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/5']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/18', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/17', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/17` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/18` | 1.001366 | STEP 3: SELECT AN ANCESTRY |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/8` | 0.638945 | ANCESTRY, BACKGROUND, CLASS,  OR DETAILS |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/5` | 0.599311 | CHAPTER 2: ANCESTRIES &  BACKGROUNDS |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/SectionHeader/27` | 0.553685 | ANCESTRIES |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/21` | 0.536619 | Pick the ancestry itself. |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/1` | 0.515710 | **ALTERNATE ANCESTRY BOOSTS** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/16` | 0.509084 | Select feats as indicated on your class advancement  table. For ancestry feats, see Chapter 2. For class  feats, see your class entry in Chapter 3. For general  feats and skill feats, see Chapter 5. |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/23` | 0.474961 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/7` | 0.474961 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/33` | 0.474961 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 81
- Text: Summarize Pick the ancestry itself.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/21', 'PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/22', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/20']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/21', 'PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/22', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/20']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/20` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/21` | 0.994717 | Pick the ancestry itself. |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/22` | 0.713339 | Select a heritage from those available within that  ancestry, further defining the traits your character was  born with. |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/20` | 0.691964 | You'll have four decisions to make when you choosing your  character's ancestry. |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/19` | 0.620191 | Select an ancestry for your character. The ancestry  summaries on page 27 provide an overview of Starfinder's  core ancestry options, and each is fully detailed in Chapter  2. Ancestry determines your |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/6` | 0.595334 | The rules for ancestries and heritages representing the  Pact Worlds are in this chapter, including their ancestry  feat options. Backgrounds are at the end of this chapter,  along with a section abou |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/3` | 0.579053 | **Ancestry:** Each ancestry provides attribute boosts, and sometimes an attribute flaw. If you're taking any voluntary  flaws, apply them in this step (see the sidebar on page 25). |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/24` | 0.575809 | Choose an ancestry feat, representing an ability your  hero learned at an early age. |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/55` | 0.569960 | VESK YSOKI These heritages can be chosen for a member of any ancestry. |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/18` | 0.554461 | STEP 3: SELECT AN ANCESTRY |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/10/Text/2` | 0.543137 | The attribute boosts and flaws listed in each ancestry  represent general trends or help guide players to  create the kinds of characters from that ancestry most  likely to pursue the life of an adven |

### Query 82
- Text: Summarize Assign any free attribute boosts and decide if you are  taking any voluntary flaws.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/23', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/6', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/3']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/23', 'PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/22', 'PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/22` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/23` | 1.030544 | Assign any free attribute boosts and decide if you are  taking any voluntary flaws. |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/6` | 0.722314 | **Four Free Boosts:** After the other steps, you apply four more attribute boosts to attributes of your choice to finalize  your starting attribute modifiers. |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/3` | 0.709498 | **Ancestry:** Each ancestry provides attribute boosts, and sometimes an attribute flaw. If you're taking any voluntary  flaws, apply them in this step (see the sidebar on page 25). |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Footnote/61` | 0.654016 | *Any character can choose to take two free boosts instead of the listed boosts and flaws (page 24). |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/9/ListItem/13` | 0.647371 | * Any character can choose to take two free boosts  instead of the listed boosts and flaws (page 24). |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/7/ListItem/6` | 0.645492 | Then, apply four free attribute boosts to your character's attribute modifiers. Choose a different attribute modifier for each and increase that attribute modifier by 1. |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/7/ListItem/5` | 0.629294 | First, make sure you've applied all the attribute boosts and attribute flaws you've noted in previous steps (from your ancestry, background, and class). |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/17` | 0.616747 | Sometimes, it's fun to play a character with a major  flaw regardless of your ancestry. You can elect to take  additional attribute flaws when applying the attribute  boosts and attribute flaws from y |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/9` | 0.605988 | Whenever your character receives an attribute  boost, the source indicates whether it must be applied  to a specific attribute modifier, to one in a limited list,  or whether it's a "free" boost that |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/2` | 0.604641 | Each attribute modifier starts at +0, representing the average. As you make character choices, you'll adjust these  modifiers by applying attribute boosts, which increase an attribute modifier, and at |

### Query 83
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/28']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/18', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/27', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/24']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/28', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/29', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/26']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/26` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/18` | 0.880541 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/27` | 0.880541 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/24` | 0.880541 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/23` | 0.838541 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/28` | 0.838541 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/16` | 0.672734 | INTRODUCTION |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/3` | 0.646693 | CHAPTER 1: INTRODUCTION |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.608538 | **OVERVIEW** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/10` | 0.454028 | **Exploring the ** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/63` | 0.452320 | **GAME** |

### Query 84
- Text: Summarize **Leveling Up**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/30']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/20', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/30', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/29']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/30', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/31', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/29']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/31` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/29` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/20` | 0.970922 | **Leveling Up** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/30` | 0.970922 | **Leveling Up** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/29` | 0.970922 | **Leveling Up** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/4` | 0.928922 | **Leveling Up** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/25` | 0.928922 | **Leveling Up** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/26` | 0.928922 | **Leveling Up** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/SectionHeader/0` | 0.807826 | LEVELING UP |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/15/SectionHeader/11` | 0.661624 | **LEVELING-UP CHECKLIST** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/18` | 0.610760 | Leveling Up |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/10` | 0.369448 | **Exploring the ** |

### Query 85
- Text: Summarize **Exploring the ** **Galaxy**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/31']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/21', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/27', 'PZO22001 Starfinder Player Core 014-029::/page/15/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/31', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/32', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/30']
- Expanded expected found: `True`
- Expanded expected rank: `6`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/32` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/30` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/21` | 0.993218 | **Exploring the ** **Galaxy** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/27` | 0.993218 | **Exploring the ** **Galaxy** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/26` | 0.993218 | **Exploring the ** **Galaxy** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/5` | 0.951218 | **Exploring the ** **Galaxy** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/30` | 0.951218 | **Exploring the ** **Galaxy** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/31` | 0.951218 | **Exploring the ** **Galaxy** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/19` | 0.802920 | Exploring the Galaxy |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/10` | 0.643308 | **Exploring the ** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/4` | 0.499391 | This introduction is designed to help you understand the  basics of Starfinder. This chapter also includes the rules for  building and leveling up a character, as well as an example  of the character |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/5` | 0.415618 | their past, and think about how and why they adventure.  You'll want to peruse Starfinder's available ancestries,  backgrounds, and classes. The summaries on pages 27–28  might help you match your con |

### Query 86
- Text: Summarize **Religion**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/32']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/22', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/28', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/32']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/32', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/33', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/31']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/31` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/22` | 0.921440 | **Religion** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/28` | 0.921440 | **Religion** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/32` | 0.921440 | **Religion** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/6` | 0.879440 | **Religion** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/31` | 0.879440 | **Religion** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/27` | 0.879440 | **Religion** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/20` | 0.661755 | Religion |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/9` | 0.438253 | **Constitution** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/11` | 0.391895 | **Intelligence** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/18` | 0.389000 | **INTRODUCTION** |

### Query 87
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/34']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/24', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/8', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/33']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/34', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/24', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/33', 'PZO22001 Starfinder Player Core 014-029::/page/15/Text/29', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/33', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/8', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/30', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/35']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/24` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/15/Text/29` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/11/Text/33` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/13/Text/8` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/9/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/35` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/24` | 0.940061 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/8` | 0.940061 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/33` | 0.940061 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/30` | 0.910061 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/34` | 0.910061 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/29` | 0.910061 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/7` | 0.799617 | CHAPTER 3: CLASSES |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/22` | 0.763092 | CLASSES |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.453104 | **OVERVIEW** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/10` | 0.444758 | STEP 7: RECORD CLASS DETAILS |

### Query 88
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/37']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/27', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/37', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/33']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/37', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/36', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/38']
- Expanded expected found: `True`
- Expanded expected rank: `2`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/38` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/27` | 0.944726 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/37` | 0.944726 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/33` | 0.944726 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/32` | 0.902726 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/13` | 0.829789 | CHAPTER 6: EQUIPMENT |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/25` | 0.824254 | EQUIPMENT |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/17` | 0.651834 | STEP 8: BUY EQUIPMENT |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/36` | 0.578761 | **EQUIPMENT** **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/11` | 0.578761 | **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/12/Text/18` | 0.462787 | Next up, Jessica turns to Chapter 6: Equipment. She's trained  in medium armor and chooses commercial freebooter  armor (which comes with a built-in comm unit, like most  armor). When it comes to weap |

### Query 89
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/39']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/29', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/37', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/39']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/39', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/40', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/38']
- Expanded expected found: `True`
- Expanded expected rank: `3`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/38` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/29` | 0.965000 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/37` | 0.965000 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/39` | 0.965000 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/35` | 0.923000 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/34` | 0.923000 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/12` | 0.811006 | **PLAYING THE ** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/27` | 0.749688 | PLAYING THE GAME |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/17` | 0.724027 | CHAPTER 8:  PLAYING THE  GAME |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/63` | 0.663024 | **GAME** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/10` | 0.482709 | **Exploring the ** |

### Query 90
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/40']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/30', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/36', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/13']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/40', 'PZO22001 Starfinder Player Core 014-029::/page/15/Text/35', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/41', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/30', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/36', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/38', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/13', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/39']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/15/Text/35` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/41` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/1/Text/30` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/9/Text/36` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/11/Text/38` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/13/Text/13` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/39` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/30` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/13` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/36` | 0.983498 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/38` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/40` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/35` | 0.953498 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/28` | 0.837763 | CONDITIONS APPENDIX |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/19` | 0.570754 | APPENDICES |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/20` | 0.426695 | The back of this book has an  appendix with the rules for all of  the conditions that you will find  in the game. This section also  includes a blank character sheet,  and an index with a comprehensiv |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/7` | 0.416141 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 91
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/41']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/31', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/37', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/14']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/41', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/40', 'PZO22001 Starfinder Player Core 014-029::/page/6/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `5`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/5/Text/40` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/6/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/31` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/14` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/37` | 0.993465 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/39` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/41` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/36` | 0.951465 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/29` | 0.825490 | GLOSSARY & INDEX |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.427174 | **OVERVIEW** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/34` | 0.385404 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/24` | 0.385404 | **CLASSES** |

### Query 92
- Text: Summarize STEP 5: CHOOSE \Delta CL\DeltaSS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/6/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/6/SectionHeader/8', 'PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/9', 'PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/7']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/6/SectionHeader/8', 'PZO22001 Starfinder Player Core 014-029::/page/6/Text/9', 'PZO22001 Starfinder Player Core 014-029::/page/6/Text/7']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/6/Text/9` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/6/Text/7` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/6/SectionHeader/8` | 1.022291 | STEP 5: CHOOSE \Delta CL\DeltaSS |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/9` | 0.533251 | STEP 5 |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/7` | 0.489638 | STEP 4 |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/18` | 0.446595 | STEP 10: FINISHING DETAILS |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/18` | 0.435606 | STEP 3: SELECT AN ANCESTRY |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/5` | 0.433248 | STEP 3 |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/3` | 0.422006 | STEPS 1 AND 2 |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/11` | 0.419311 | STEP 6 |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/17` | 0.413034 | STEP 8: BUY EQUIPMENT |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/13` | 0.396489 | STEP 7 |

### Query 93
- Text: Summarize PLAYER CORE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/0']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/0', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/17', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/27']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/0', 'PZO22001 Starfinder Player Core 014-029::/page/6/Text/12', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/2']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/6/Text/12` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/7/Text/2` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/0` | 0.957792 | PLAYER CORE |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/17` | 0.445642 | CHAPTER 8:  PLAYING THE  GAME |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/27` | 0.441410 | PLAYING THE GAME |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/29` | 0.388377 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/37` | 0.388377 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/34` | 0.388377 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/39` | 0.388377 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/35` | 0.388377 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/12` | 0.365139 | **PLAYING THE ** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/3` | 0.321458 | The summaries of the classes on page 28 list each  class's key attribute—the attribute modifier used to  calculate the potency of many of their class abilities.  Characters receive an attribute boost |

### Query 94
- Text: Summarize STEP 7: RECORD CLASS DETAILS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/10', 'PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/13', 'PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/10', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/11', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/9']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/7/Text/11` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/7/Text/9` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/10` | 1.014516 | STEP 7: RECORD CLASS DETAILS |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/13` | 0.667044 | STEP 7 |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/18` | 0.557024 | STEP 10: FINISHING DETAILS |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/17` | 0.505403 | STEP 8 |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/11` | 0.496648 | Your next step is to record all the benefits and class features that your character receives from the class you've chosen. You'll want to be sure to record the following class features. |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/7` | 0.496160 | STEP 4 |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/7` | 0.494506 | CHAPTER 3: CLASSES |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/11` | 0.494417 | STEP 6 |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/5` | 0.470830 | STEP 3 |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/19` | 0.470167 | STEP 9 |

### Query 95
- Text: Summarize INTRODUCTION
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/16', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/3', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/18']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/16', 'PZO22001 Starfinder Player Core 014-029::/page/7/ListItem/14', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/7/ListItem/14` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/7/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/16` | 0.783895 | INTRODUCTION |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/3` | 0.689276 | CHAPTER 1: INTRODUCTION |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/18` | 0.665574 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/28` | 0.623574 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/24` | 0.623574 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/27` | 0.623574 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/23` | 0.623574 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.382361 | **OVERVIEW** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/4` | 0.354729 | This introduction is designed to help you understand the  basics of Starfinder. This chapter also includes the rules for  building and leveling up a character, as well as an example  of the character |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/5` | 0.304930 | their past, and think about how and why they adventure.  You'll want to peruse Starfinder's available ancestries,  backgrounds, and classes. The summaries on pages 27–28  might help you match your con |

### Query 96
- Text: Summarize Leveling Up
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/18', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/20', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/26']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/18', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/19', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/17']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/7/Text/19` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/7/Text/17` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/18` | 0.908367 | Leveling Up |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/20` | 0.641604 | **Leveling Up** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/26` | 0.641604 | **Leveling Up** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/4` | 0.599604 | **Leveling Up** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/30` | 0.599604 | **Leveling Up** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/29` | 0.599604 | **Leveling Up** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/25` | 0.599604 | **Leveling Up** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/15/SectionHeader/0` | 0.564807 | LEVELING UP |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/21` | 0.519034 | You can perform the steps in the leveling-up process  in whichever order you want. For example, if you wanted  to take the skill feat Intimidating Prowess as your skill feat  at 10th level, but your c |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/6` | 0.512123 | If you're creating a higher-level character, it's a good idea  to begin with the instructions here, then turn to page 29 for  instructions on leveling up characters. |

### Query 97
- Text: Summarize Exploring the Galaxy
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/19', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/5', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/21']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/19', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/20', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/18']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/7/Text/20` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/7/Text/18` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/19` | 0.905652 | Exploring the Galaxy |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/5` | 0.768827 | **Exploring the ** **Galaxy** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/21` | 0.768827 | **Exploring the ** **Galaxy** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/27` | 0.726827 | **Exploring the ** **Galaxy** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/31` | 0.726827 | **Exploring the ** **Galaxy** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/30` | 0.726827 | **Exploring the ** **Galaxy** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/26` | 0.726827 | **Exploring the ** **Galaxy** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/10` | 0.531756 | **Exploring the ** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/4` | 0.504655 | This introduction is designed to help you understand the  basics of Starfinder. This chapter also includes the rules for  building and leveling up a character, as well as an example  of the character |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/5` | 0.447496 | their past, and think about how and why they adventure.  You'll want to peruse Starfinder's available ancestries,  backgrounds, and classes. The summaries on pages 27–28  might help you match your con |

### Query 98
- Text: Summarize Religion
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/20', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/31', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/6']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/20', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/21', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/19']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/7/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/7/Text/19` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/20` | 0.795689 | Religion |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/31` | 0.718409 | **Religion** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/6` | 0.718409 | **Religion** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/28` | 0.676409 | **Religion** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/22` | 0.676409 | **Religion** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/27` | 0.676409 | **Religion** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/32` | 0.676409 | **Religion** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/9` | 0.385211 | Write down the deity your character worships, if any.  Your character might worship several deities as part of a  personal pantheon. You might instead choose a philosophy  or decide your character is |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/1` | 0.357796 | character to hone in on how they think. If you follow a  deity, you might take inspiration from the edicts and  anathema listed for them on pages 35–39. Ancestry  entries list edicts and anathema prev |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/13` | 0.355828 | Perhaps you'd like to play a character who is a devout  follower of a specific deity. The peoples of the galaxy follow  myriad faiths and philosophies spanning a wide pantheon,  from Damoritosh, the C |

### Query 99
- Text: Summarize CLASSES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/22', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/7', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/24']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/22', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/21', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/23']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/7/Text/21` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/7/Text/23` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/22` | 0.906666 | CLASSES |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/7` | 0.882503 | CHAPTER 3: CLASSES |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/24` | 0.869259 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/33` | 0.839259 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/34` | 0.839259 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/30` | 0.839259 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/8` | 0.839259 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/29` | 0.839259 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/11/SectionHeader/14` | 0.479553 | CLASS DC |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/10` | 0.438775 | STEP 7: RECORD CLASS DETAILS |

### Query 100
- Text: Summarize EQUIPMENT
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/25', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/13', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/33']
- Expanded expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/25', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/26', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/24']
- Expanded expected found: `True`
- Expanded expected rank: `1`
- Expanded additions:
  - `PZO22001 Starfinder Player Core 014-029::/page/7/Text/26` (reasons: ['graph_depth_1'])
  - `PZO22001 Starfinder Player Core 014-029::/page/7/Text/24` (reasons: ['graph_depth_1'])

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/25` | 0.917220 | EQUIPMENT |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/13` | 0.882252 | CHAPTER 6: EQUIPMENT |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/33` | 0.853596 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/37` | 0.811596 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/27` | 0.811596 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/32` | 0.811596 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/17` | 0.648962 | STEP 8: BUY EQUIPMENT |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/11` | 0.519242 | **EQUIPMENT** **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/36` | 0.519242 | **EQUIPMENT** **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/12/Text/18` | 0.426903 | Next up, Jessica turns to Chapter 6: Equipment. She's trained  in medium armor and chooses commercial freebooter  armor (which comes with a built-in comm unit, like most  armor). When it comes to weap |
