# RulesLawyer Evaluation Report: bge-m3

## Summary
- Run ID: `None`
- Ruleset ID: `None`
- Document ID: `None`
- Chunk source: `enriched`
- Chunk count: `1751`
- Query count: `405`
- Evaluated queries: `405`
- Coverage: `1.0000`
- MRR: `0.8759`
- hit@1: `0.8198`
- hit@3: `0.9062`
- hit@5: `0.9580`
- hit@10: `0.9951`
- Embeddings reused: `False`
- Graph boost: `0.05` (depth=2, top_k=50, source=top, seed_top_n=3, same_kind_only=False, decay=0.4)

## Timings (ms)
- Embedding: `52278`
- Evaluation: `226`

## Query Details
### Query 0
- Text: Summarize USING THIS BOOK
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `30`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/3', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/1` | 0.863485 | USING THIS BOOK |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/3` | 0.659196 | CHAPTER 1: INTRODUCTION |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/16` | 0.655649 | INTRODUCTION |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.608665 | **OVERVIEW** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/9` | 0.598647 | CHAPTER 4: SKILLS |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/3` | 0.595421 | STEPS 1 AND 2 |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6` | 0.593206 | UNDERSTANDING ACTIONS |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/13` | 0.583402 | CHAPTER 6: EQUIPMENT |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/11` | 0.583369 | CHAPTER 5: FEATS |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/18` | 0.583181 | STEP 10: FINISHING DETAILS |

### Query 1
- Text: What is the rule about While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy as possible. Rules are grouped  together in chapters, with the early chapters focusing on  character creation. The following is a summary of what  you can expect to find in each chapter.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `35`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/2', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/4', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 1.018744 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/4` | 0.843174 | This introduction is designed to help you understand the  basics of Starfinder. This chapter also includes the rules for  building and leveling up a character, as well as an example  of the character |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/18` | 0.827391 | This important chapter contains  the universal rules needed to play  Starfinder, including rules for the  various modes of play, the basic  actions that every character can  perform, the rules for com |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/3` | 0.765461 | This section provides a step-by-step guide for creating a  character using the Starfinder rules, preceded by a guide to  help you understand attribute modifiers. These modifiers are a  critical part o |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/5` | 0.751455 | their past, and think about how and why they adventure.  You'll want to peruse Starfinder's available ancestries,  backgrounds, and classes. The summaries on pages 27–28  might help you match your con |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/1` | 0.714379 | Unless you're the GM, the first thing you need to do when playing Starfinder is create your character. It's  up to you to imagine your character's past experiences, personality, and view of the galaxy |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/5` | 0.710945 | The entries on the pages that follow describe six classes  in Starfinder. Each entry contains the information you  need to play a character of that class, as well as how to  develop them from their hu |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/2` | 0.679698 | Throughout this rulebook, you will see formatting  standards that might look a bit unusual at first. These  standards are in place to make the rules elements in this  book easier to recognize. |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/15` | 0.677919 | You might want to coordinate with other players when  forming your character concept. Your characters could have  something in common already; perhaps they are travelers  from the same home world, or |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.672895 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |

### Query 2
- Text: Summarize CHAPTER 1: INTRODUCTION
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/3', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/16', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/3` | 0.959952 | CHAPTER 1: INTRODUCTION |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/16` | 0.825131 | INTRODUCTION |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/18` | 0.747484 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/28` | 0.705484 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/24` | 0.705484 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/23` | 0.705484 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/27` | 0.705484 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/56` | 0.697484 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/29` | 0.697484 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/29` | 0.697484 | **INTRODUCTION** |

### Query 3
- Text: What is the rule about This introduction is designed to help you understand the  basics of Starfinder. This chapter also includes the rules for  building and leveling up a character, as well as an example  of the character creation process. The chapter ends with  an introduction to the galaxy and its gods.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `34`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/4', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/2', 'PZO22001 Starfinder Player Core 014-029::/page/3/Text/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/4` | 1.010440 | This introduction is designed to help you understand the  basics of Starfinder. This chapter also includes the rules for  building and leveling up a character, as well as an example  of the character |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.846119 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/3` | 0.816019 | This section provides a step-by-step guide for creating a  character using the Starfinder rules, preceded by a guide to  help you understand attribute modifiers. These modifiers are a  critical part o |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/1` | 0.758334 | Unless you're the GM, the first thing you need to do when playing Starfinder is create your character. It's  up to you to imagine your character's past experiences, personality, and view of the galaxy |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/18` | 0.750620 | This important chapter contains  the universal rules needed to play  Starfinder, including rules for the  various modes of play, the basic  actions that every character can  perform, the rules for com |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/5` | 0.735895 | The entries on the pages that follow describe six classes  in Starfinder. Each entry contains the information you  need to play a character of that class, as well as how to  develop them from their hu |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/5` | 0.735658 | their past, and think about how and why they adventure.  You'll want to peruse Starfinder's available ancestries,  backgrounds, and classes. The summaries on pages 27–28  might help you match your con |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/15` | 0.704969 | You might want to coordinate with other players when  forming your character concept. Your characters could have  something in common already; perhaps they are travelers  from the same home world, or |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.689531 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/12/Text/2` | 0.683608 | This step-by-step example illustrates the process of  creating a Starfinder character. |

### Query 4
- Text: What is the rule about CHAPTER 2: ANCESTRIES &  BACKGROUNDS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `30`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/5', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/21', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/33']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/5` | 0.887695 | CHAPTER 2: ANCESTRIES &  BACKGROUNDS |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/21` | 0.750286 | ANCESTRIES & BACKGROUNDS |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/33` | 0.705118 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/7` | 0.663118 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/29` | 0.663118 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/32` | 0.663118 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/23` | 0.663118 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/28` | 0.663118 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/57` | 0.655118 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/58` | 0.655118 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 5
- Text: What is the rule about The rules for ancestries and heritages representing the  Pact Worlds are in this chapter, including their ancestry  feat options. Backgrounds are at the end of this chapter,  along with a section about languages, as these are often  influenced by your choice of ancestry.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `32`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/6', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/10', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/6` | 1.014631 | The rules for ancestries and heritages representing the  Pact Worlds are in this chapter, including their ancestry  feat options. Backgrounds are at the end of this chapter,  along with a section abou |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.726170 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` | 0.723753 | Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/19` | 0.658109 | Select an ancestry for your character. The ancestry  summaries on page 27 provide an overview of Starfinder's  core ancestry options, and each is fully detailed in Chapter  2. Ancestry determines your |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/29` | 0.636526 | In addition to what you get from your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/16` | 0.632565 | Select feats as indicated on your class advancement  table. For ancestry feats, see Chapter 2. For class  feats, see your class entry in Chapter 3. For general  feats and skill feats, see Chapter 5. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/26` | 0.630002 | This section serves as a reminder of the ancestry feats your  character gains at 5th, 9th, 13th, and 17th levels. Ancestry  feats are detailed in each ancestry entry in Chapter 2, which  begins on pag |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.619959 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/7` | 0.616515 | You can find all the new abilities specific to your class,  including class feats, right in your class entry, though you  can also use class feats to take an archetype (page 174).  Your character's cl |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.612253 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |

### Query 6
- Text: Summarize CHAPTER 3: CLASSES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/7', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/22', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/7` | 0.964499 | CHAPTER 3: CLASSES |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/1` | 0.914499 | CHAPTER 3: CLASSES |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/22` | 0.790772 | CLASSES |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/9` | 0.728842 | CHAPTER 4: SKILLS |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/10` | 0.685887 | STEP 7: RECORD CLASS DETAILS |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26` | 0.676979 | CLASS FEATURES |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11` | 0.676979 | CLASS FEATURES |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/8` | 0.665578 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/29` | 0.665578 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/33` | 0.665578 | **CLASSES** |

### Query 7
- Text: What is the rule about This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the class feats available to members  of that class. At the end of this chapter are the rules for  archetypes—special options available to characters as they  increase in level. These rules allow a character to dabble in  the abilities of another class or concept.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `27`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/8', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/10', 'PZO22001 Starfinder Player Core 014-029::/page/15/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 1.012608 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.806570 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/7` | 0.784502 | You can find all the new abilities specific to your class,  including class feats, right in your class entry, though you  can also use class feats to take an archetype (page 174).  Your character's cl |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/7` | 0.745088 | **Archetypes** on page 174 gives you thematic options  that allow you to further customize your character's  abilities. Though these rules are not recommended for  beginners, the archetypes in this bo |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.737521 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.730191 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/6/Text/9` | 0.720206 | At this point, you need to decide your character's class. A class gives your character access to a suite of heroic abilities, determines how effectively they fight, and governs how easily they can sha |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 0.714471 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.706948 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.700552 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |

### Query 8
- Text: What is the rule about CHAPTER 4: SKILLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/9', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/23', 'PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/9` | 0.879600 | CHAPTER 4: SKILLS |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/23` | 0.731172 | SKILLS |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/13` | 0.731172 | SKILLS |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/45` | 0.604347 | SKILL FEATS 2ND |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/7` | 0.597069 | CHAPTER 3: CLASSES |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.595133 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/30` | 0.594784 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/9` | 0.594784 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/25` | 0.594784 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/34` | 0.594784 | **SKILLS** |

### Query 9
- Text: What is the rule about The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can define some of a character's  skill proficiencies, and each character can also select a few  additional skills to reflect their personality and training.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/10', 'PZO22001 Starfinder Player Core 014-029::/page/7/ListItem/13', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 1.016603 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/7/ListItem/13` | 0.807529 | The Initial Proficiencies section of your class entry indicates your character's starting proficiency ranks in a number of areas. Choose which skills your character is trained in and record those, alo |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.789971 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.741744 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.717932 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 0.713374 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/7` | 0.712961 | You can find all the new abilities specific to your class,  including class feats, right in your class entry, though you  can also use class feats to take an archetype (page 174).  Your character's cl |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.709640 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.706774 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/6/Text/9` | 0.700966 | At this point, you need to decide your character's class. A class gives your character access to a suite of heroic abilities, determines how effectively they fight, and governs how easily they can sha |

### Query 10
- Text: What is the rule about CHAPTER 5: FEATS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `21`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/11', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/24', 'PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/11` | 0.861744 | CHAPTER 5: FEATS |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/24` | 0.691666 | FEATS |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/16` | 0.634429 | Select feats as indicated on your class advancement  table. For ancestry feats, see Chapter 2. For class  feats, see your class entry in Chapter 3. For general  feats and skill feats, see Chapter 5. |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.608924 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.591140 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/8/SectionHeader/13` | 0.579083 | ANCESTRY FEATS 5TH |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11` | 0.578520 | CLASS FEATURES |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26` | 0.578520 | CLASS FEATURES |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.577764 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/10` | 0.573384 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |

### Query 11
- Text: What is the rule about As a character advances in level, they gain additional feats  to represent their growing abilities. General feats and skill  feats (which are a subset of general feats) are presented  in this chapter.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/12', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/6', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/12` | 0.952612 | As a character advances in level, they gain additional feats  to represent their growing abilities. General feats and skill  feats (which are a subset of general feats) are presented  in this chapter. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.769625 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.756959 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.740206 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.730731 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/10` | 0.727847 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.703588 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 0.685588 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/7` | 0.683908 | You can find all the new abilities specific to your class,  including class feats, right in your class entry, though you  can also use class feats to take an archetype (page 174).  Your character's cl |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/16` | 0.683689 | Select feats as indicated on your class advancement  table. For ancestry feats, see Chapter 2. For class  feats, see your class entry in Chapter 3. For general  feats and skill feats, see Chapter 5. |

### Query 12
- Text: Summarize CHAPTER 6: EQUIPMENT
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/13', 'PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/17', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/13` | 0.974688 | CHAPTER 6: EQUIPMENT |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/17` | 0.786243 | STEP 8: BUY EQUIPMENT |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/25` | 0.784374 | EQUIPMENT |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/9` | 0.699478 | CHAPTER 4: SKILLS |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/11` | 0.695267 | CHAPTER 5: FEATS |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/11` | 0.680966 | STEP 6 |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/27` | 0.671960 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/37` | 0.671960 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/33` | 0.671960 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/32` | 0.671960 | **EQUIPMENT** |

### Query 13
- Text: Summarize Armor, weapons, and other gear can all be found in this  chapter, along with the price for services, cost of living,  and transportation (such as hovercabs and gravtrains).
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `30`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/14', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/20', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/14` | 1.016283 | Armor, weapons, and other gear can all be found in this  chapter, along with the price for services, cost of living,  and transportation (such as hovercabs and gravtrains). |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/20` | 0.755899 | You'll also want equipment like cable line, flashlights,  toolkits, and other traveling gear, and maybe even a serum or  sprayflesh for emergency medical needs. Augmentations that  change your body, u |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/19` | 0.641840 | weapons, and other basic equipment. Your character's class  lists the types of weapons and armor with which they are  trained (or better!). Their weapons determine how much  damage they deal in combat |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/20` | 0.585825 | The back of this book has an  appendix with the rules for all of  the conditions that you will find  in the game. This section also  includes a blank character sheet,  and an index with a comprehensiv |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 0.583308 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/13` | 0.572618 | **Prerequisites** Any minimum attributes, feats, proficiency  ranks, and so forth you must have to select this rules  element are here. Feats also have a level prerequisite,  listed above. |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/13` | 0.571747 | CHAPTER 6: EQUIPMENT |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/10/Text/3` | 0.565630 | first page, depending on the weapon, and the rest  of their equipment in the Inventory section on the  second page. You'll calculate specific numbers for  melee Strikes and ranged Strikes with the wea |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/12/Text/18` | 0.552952 | Next up, Jessica turns to Chapter 6: Equipment. She's trained  in medium armor and chooses commercial freebooter  armor (which comes with a built-in comm unit, like most  armor). When it comes to weap |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/12` | 0.552264 | As a character advances in level, they gain additional feats  to represent their growing abilities. General feats and skill  feats (which are a subset of general feats) are presented  in this chapter. |

### Query 14
- Text: What is the rule about CHAPTER 7: SPELLS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/15', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/26', 'PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/15` | 0.904519 | CHAPTER 7: SPELLS |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/26` | 0.706794 | SPELLS |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/13` | 0.659463 | STEP 7 |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/38` | 0.607134 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/34` | 0.607134 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/33` | 0.607134 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/28` | 0.607134 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/10` | 0.601688 | STEP 7: RECORD CLASS DETAILS |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/33` | 0.599134 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/49` | 0.599134 | **SPELLS** |

### Query 15
- Text: What is the rule about This chapter starts with rules for casting spells,  determining their effects, and negating foes' spells  (called counteracting). After that, the spell lists for  each spellcasting tradition are included, making it easy  to quickly find spells by their rank. Next are rules for  every spell, presented in alphabetical order. Following  the spell descriptions are all of the focus spells—special  spells granted by specific class abilities and feats. While  most spells appear on multiple spell lists, focus spells  are granted only to members of a specific class and are  grouped together by class for ease of reference. Finally,  at the end of the chapter are rules for rituals, complicated  and risky spells that any character can attempt.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/16', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/19', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/16` | 1.020334 | This chapter starts with rules for casting spells,  determining their effects, and negating foes' spells  (called counteracting). After that, the spell lists for  each spellcasting tradition are inclu |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/19` | 0.786829 | Many characters can learn a few cantrips or focus spells,  but the mystic and witchwarper gain spellcasting—the  ability to cast a wide variety of spells. If your character's  class grants spells, you |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.726422 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/56` | 0.701913 | When a foe Casts a Spell that has the mental trait and you can  see or otherwise detect its manifestations, you use your psychic  powers to disrupt it. You expend 1 Focus Point to counter the  trigger |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/17` | 0.680973 | Add spells and spell slots if your class grants  spellcasting. See Chapter 7 for spells. |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.677084 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/6/Text/9` | 0.672228 | At this point, you need to decide your character's class. A class gives your character access to a suite of heroic abilities, determines how effectively they fight, and governs how easily they can sha |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.668928 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/7` | 0.654989 | Spellcasting classes grant a proficiency rank for spell  attacks and DCs, which are further detailed in each class's  entry. These classes rarely use their class DC. |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/7` | 0.653380 | You can find all the new abilities specific to your class,  including class feats, right in your class entry, though you  can also use class feats to take an archetype (page 174).  Your character's cl |

### Query 16
- Text: Summarize CHAPTER 8:  PLAYING THE  GAME
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/17', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/27', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/17` | 0.989965 | CHAPTER 8:  PLAYING THE  GAME |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/27` | 0.820611 | PLAYING THE GAME |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/29` | 0.738644 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/34` | 0.696644 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/37` | 0.696644 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/35` | 0.696644 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/39` | 0.696644 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/84` | 0.688644 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/50` | 0.688644 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/34` | 0.688644 | **PLAYING THE ** **GAME** |

### Query 17
- Text: What is the rule about This important chapter contains  the universal rules needed to play  Starfinder, including rules for the  various modes of play, the basic  actions that every character can  perform, the rules for combat, and  the rules for death and dying. Every  player should be familiar with this  chapter, especially the GM.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `38`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/18', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/2', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/18` | 1.023458 | This important chapter contains  the universal rules needed to play  Starfinder, including rules for the  various modes of play, the basic  actions that every character can  perform, the rules for com |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.801084 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/4` | 0.749255 | This introduction is designed to help you understand the  basics of Starfinder. This chapter also includes the rules for  building and leveling up a character, as well as an example  of the character |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/5` | 0.695663 | their past, and think about how and why they adventure.  You'll want to peruse Starfinder's available ancestries,  backgrounds, and classes. The summaries on pages 27–28  might help you match your con |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/3` | 0.695507 | This section provides a step-by-step guide for creating a  character using the Starfinder rules, preceded by a guide to  help you understand attribute modifiers. These modifiers are a  critical part o |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/1` | 0.693606 | Unless you're the GM, the first thing you need to do when playing Starfinder is create your character. It's  up to you to imagine your character's past experiences, personality, and view of the galaxy |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/7` | 0.653981 | Characters and their adversaries affect the galaxy of  Starfinder by using actions and producing effects. This is  especially the case during encounters, when every action  counts. When you use an act |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/5` | 0.647982 | The entries on the pages that follow describe six classes  in Starfinder. Each entry contains the information you  need to play a character of that class, as well as how to  develop them from their hu |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/15` | 0.644441 | You might want to coordinate with other players when  forming your character concept. Your characters could have  something in common already; perhaps they are travelers  from the same home world, or |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/3` | 0.624552 | The names of specific statistics, skills, feats, actions,  and some other mechanical elements in Starfinder are  capitalized. This way, when you see the statement "a  Strike targets Armor Class," you |

### Query 18
- Text: Summarize APPENDICES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/19', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/28', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/40']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/19` | 0.885670 | APPENDICES |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/28` | 0.735022 | CONDITIONS APPENDIX |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/40` | 0.701582 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/89` | 0.664861 | **APPENDIX** **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/30` | 0.659582 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/38` | 0.659582 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/13` | 0.659582 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/35` | 0.659582 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/36` | 0.659582 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/40` | 0.651582 | **CONDITIONS ** **APPENDIX** |

### Query 19
- Text: What is the rule about The back of this book has an  appendix with the rules for all of  the conditions that you will find  in the game. This section also  includes a blank character sheet,  and an index with a comprehensive  glossary of common terms and  traits that you'll encounter in  the game.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `37`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/0/Text/20', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/7', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/20` | 1.006991 | The back of this book has an  appendix with the rules for all of  the conditions that you will find  in the game. This section also  includes a blank character sheet,  and an index with a comprehensiv |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` | 0.683701 | Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.674661 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.616506 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.613805 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/6` | 0.612134 | The rules for ancestries and heritages representing the  Pact Worlds are in this chapter, including their ancestry  feat options. Backgrounds are at the end of this chapter,  along with a section abou |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/18` | 0.611935 | This important chapter contains  the universal rules needed to play  Starfinder, including rules for the  various modes of play, the basic  actions that every character can  perform, the rules for com |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.611332 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/16` | 0.597042 | This chapter starts with rules for casting spells,  determining their effects, and negating foes' spells  (called counteracting). After that, the spell lists for  each spellcasting tradition are inclu |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.595644 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |

### Query 20
- Text: Summarize FORMAT OF RULES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `36`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5', 'PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1` | 0.913269 | FORMAT OF RULES |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5` | 0.711036 | READING RULES |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/10` | 0.604463 | STEP 7: RECORD CLASS DETAILS |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/1` | 0.551272 | SAMPLE CHARACTER |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.550001 | **OVERVIEW** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/11` | 0.549423 | PHYSICAL DESCRIPTION |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/9/SectionHeader/11` | 0.549423 | PHYSICAL DESCRIPTION |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/13/SectionHeader/12` | 0.549423 | PHYSICAL DESCRIPTION |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/5/SectionHeader/11` | 0.549423 | PHYSICAL DESCRIPTION |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/29` | 0.547645 | GLOSSARY & INDEX |

### Query 21
- Text: What is the rule about Throughout this rulebook, you will see formatting  standards that might look a bit unusual at first. These  standards are in place to make the rules elements in this  book easier to recognize.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/2', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/2', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/2` | 0.983369 | Throughout this rulebook, you will see formatting  standards that might look a bit unusual at first. These  standards are in place to make the rules elements in this  book easier to recognize. |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.705042 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` | 0.678543 | Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.638920 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.633995 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/9` | 0.617300 | Spells, tech items, and magic items use a similar format,  but their stat blocks contain a number of unique elements,  such as the possible magical traditions for a spell (see  Chapter 7 for more on r |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/20` | 0.610064 | The back of this book has an  appendix with the rules for all of  the conditions that you will find  in the game. This section also  includes a blank character sheet,  and an index with a comprehensiv |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/16` | 0.605084 | This chapter starts with rules for casting spells,  determining their effects, and negating foes' spells  (called counteracting). After that, the spell lists for  each spellcasting tradition are inclu |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/8` | 0.594747 | Throughout this book, you will see special icons to  denote actions. |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.584764 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |

### Query 22
- Text: What is the rule about The names of specific statistics, skills, feats, actions,  and some other mechanical elements in Starfinder are  capitalized. This way, when you see the statement "a  Strike targets Armor Class," you know that both Strike and  Armor Class are referring to rules.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `35`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/3', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/5', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/3` | 1.002845 | The names of specific statistics, skills, feats, actions,  and some other mechanical elements in Starfinder are  capitalized. This way, when you see the statement "a  Strike targets Armor Class," you |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/5` | 0.720821 | Starfinder uses many terms that are typically expressed  as abbreviations, like AC for Armor Class, DC for Difficulty  Class, and HP for Hit Points. If you're ever confused about  a game term or an ab |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.691369 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/18` | 0.636963 | This important chapter contains  the universal rules needed to play  Starfinder, including rules for the  various modes of play, the basic  actions that every character can  perform, the rules for com |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/7` | 0.623707 | Characters and their adversaries affect the galaxy of  Starfinder by using actions and producing effects. This is  especially the case during encounters, when every action  counts. When you use an act |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/19` | 0.622141 | weapons, and other basic equipment. Your character's class  lists the types of weapons and armor with which they are  trained (or better!). Their weapons determine how much  damage they deal in combat |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/19` | 0.608991 | Select an ancestry for your character. The ancestry  summaries on page 27 provide an overview of Starfinder's  core ancestry options, and each is fully detailed in Chapter  2. Ancestry determines your |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/15` | 0.608492 | You might want to coordinate with other players when  forming your character concept. Your characters could have  something in common already; perhaps they are travelers  from the same home world, or |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/5` | 0.607753 | The entries on the pages that follow describe six classes  in Starfinder. Each entry contains the information you  need to play a character of that class, as well as how to  develop them from their hu |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/4` | 0.607038 | This introduction is designed to help you understand the  basics of Starfinder. This chapter also includes the rules for  building and leveling up a character, as well as an example  of the character |

### Query 23
- Text: What is the rule about If a word or a phrase is italicized, it's describing a spell  or a magic item. This way, when you see the statement  "the radiation from an *atomic blast* lingers in the room",  you know that the words denote the *atomic blast* spell,  rather than a non-magical atomic blast.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/4', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/16', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/4` | 0.994393 | If a word or a phrase is italicized, it's describing a spell  or a magic item. This way, when you see the statement  "the radiation from an *atomic blast* lingers in the room",  you know that the word |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.610749 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/3` | 0.599569 | The names of specific statistics, skills, feats, actions,  and some other mechanical elements in Starfinder are  capitalized. This way, when you see the statement "a  Strike targets Armor Class," you |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/9` | 0.546139 | Spells, tech items, and magic items use a similar format,  but their stat blocks contain a number of unique elements,  such as the possible magical traditions for a spell (see  Chapter 7 for more on r |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.542344 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/16` | 0.530745 | This chapter starts with rules for casting spells,  determining their effects, and negating foes' spells  (called counteracting). After that, the spell lists for  each spellcasting tradition are inclu |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/15` | 0.519354 | **Requirements** Sometimes you must have a certain item or  be in a certain circumstance to use an ability. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/29` | 0.510874 | **Prerequisites** trained in Arcana, Nature, Occultism, or Religion You can hear the thrum of magic as if it were a swirling note, a  shifting melody, a harmonic chord, or a percussive beat, pulsing |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/10/Text/21` | 0.506548 | You can choose to take on edicts and anathema to  reinforce your character's beliefs and guide how they'd  react in certain situations. **Edicts** are behaviors your  personal philosophy or code encou |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/5` | 0.494019 | Starfinder uses many terms that are typically expressed  as abbreviations, like AC for Armor Class, DC for Difficulty  Class, and HP for Hit Points. If you're ever confused about  a game term or an ab |

### Query 24
- Text: What is the rule about Starfinder uses many terms that are typically expressed  as abbreviations, like AC for Armor Class, DC for Difficulty  Class, and HP for Hit Points. If you're ever confused about  a game term or an abbreviation, you can always turn to the  Glossary and Index, beginning on page 442, and look it up.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `35`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/5', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/3', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/5` | 0.999055 | Starfinder uses many terms that are typically expressed  as abbreviations, like AC for Armor Class, DC for Difficulty  Class, and HP for Hit Points. If you're ever confused about  a game term or an ab |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/3` | 0.738485 | The names of specific statistics, skills, feats, actions,  and some other mechanical elements in Starfinder are  capitalized. This way, when you see the statement "a  Strike targets Armor Class," you |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.692294 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/18` | 0.632875 | This important chapter contains  the universal rules needed to play  Starfinder, including rules for the  various modes of play, the basic  actions that every character can  perform, the rules for com |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/23` | 0.626907 | Your character's Armor Class represents how difficult they  are to hit in combat. To calculate your AC, add 10 plus your  character's Dexterity modifier (up to their armor's Dexterity  modifier cap; p |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/15` | 0.608457 | For instance, this is the attribute modifier you'll use to  determine the Difficulty Class (DC) associated with your  character's class features and feats. This is called your  class DC. If your chara |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/5` | 0.605075 | The entries on the pages that follow describe six classes  in Starfinder. Each entry contains the information you  need to play a character of that class, as well as how to  develop them from their hu |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/5` | 0.604933 | their past, and think about how and why they adventure.  You'll want to peruse Starfinder's available ancestries,  backgrounds, and classes. The summaries on pages 27–28  might help you match your con |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/4` | 0.592642 | This introduction is designed to help you understand the  basics of Starfinder. This chapter also includes the rules for  building and leveling up a character, as well as an example  of the character |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/15` | 0.590954 | A class DC sets the difficulty for certain abilities granted  by your character's class. This DC equals 10 plus their  proficiency bonus for their class DC (+3 for most 1st-level  characters) plus the |

### Query 25
- Text: What is the rule about UNDERSTANDING ACTIONS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `18`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6', 'PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5', 'PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6` | 0.843787 | UNDERSTANDING ACTIONS |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5` | 0.640734 | READING RULES |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/6` | 0.606329 | PERCEPTION |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1` | 0.546171 | FORMAT OF RULES |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/20` | 0.544841 | You succinctly direct your allies to find cover by any means  necessary. You and all allies within 60 feet count any form of  lesser cover as standard cover until the start of your next turn. **Lead b |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/10/Text/21` | 0.529493 | You can choose to take on edicts and anathema to  reinforce your character's beliefs and guide how they'd  react in certain situations. **Edicts** are behaviors your  personal philosophy or code encou |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/25` | 0.525978 | **Lead by Example** If you used two actions, Seek. Each of  your allies within 100 feet who can sense you can also  immediately Seek as a reaction. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/3` | 0.525748 | **Directive**: Actions with this trait are special orders  that provide benefits for your allies if they follow  them. Your allies must be able to sense you to benefit  from your directives. This acti |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/15` | 0.525202 | People follow your lead because you help push them to  their ultimate potential. Each of your allies gain a second  reaction if they start their turn within 100 feet of you and  can perceive you. This |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/21` | 0.519625 | **Lead by Example** If you used two actions, Step or Stride.  Each of your allies within 100 feet who can sense you can  immediately Step or Stride up to half their Speed (rounded  down to the nearest |

### Query 26
- Text: What is the rule about Characters and their adversaries affect the galaxy of  Starfinder by using actions and producing effects. This is  especially the case during encounters, when every action  counts. When you use an action, you generate an effect.  This effect might be automatic, but sometimes actions  necessitate that you roll a die, and the effect is based on  what you rolled.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/7', 'PZO22001 Starfinder Player Core 014-029::/page/4/Text/15', 'PZO22001 Starfinder Player Core 014-029::/page/3/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/7` | 0.971784 | Characters and their adversaries affect the galaxy of  Starfinder by using actions and producing effects. This is  especially the case during encounters, when every action  counts. When you use an act |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/15` | 0.735422 | You might want to coordinate with other players when  forming your character concept. Your characters could have  something in common already; perhaps they are travelers  from the same home world, or |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/1` | 0.732153 | Unless you're the GM, the first thing you need to do when playing Starfinder is create your character. It's  up to you to imagine your character's past experiences, personality, and view of the galaxy |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/3` | 0.688755 | This section provides a step-by-step guide for creating a  character using the Starfinder rules, preceded by a guide to  help you understand attribute modifiers. These modifiers are a  critical part o |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/18` | 0.683017 | This important chapter contains  the universal rules needed to play  Starfinder, including rules for the  various modes of play, the basic  actions that every character can  perform, the rules for com |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.646487 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/3` | 0.633277 | The names of specific statistics, skills, feats, actions,  and some other mechanical elements in Starfinder are  capitalized. This way, when you see the statement "a  Strike targets Armor Class," you |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/5` | 0.626719 | their past, and think about how and why they adventure.  You'll want to peruse Starfinder's available ancestries,  backgrounds, and classes. The summaries on pages 27–28  might help you match your con |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/4` | 0.624795 | This introduction is designed to help you understand the  basics of Starfinder. This chapter also includes the rules for  building and leveling up a character, as well as an example  of the character |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/27` | 0.603814 | Despite the passage of time, you remain resolute in your  defiance of the Swarm and all forms of mental control. If you  roll a success on a Will saving throw against an effect that  was created by a |

### Query 27
- Text: What is the rule about Throughout this book, you will see special icons to  denote actions.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/8', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/6', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/8` | 0.938263 | Throughout this book, you will see special icons to  denote actions. |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.645485 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/2` | 0.644279 | Throughout this rulebook, you will see formatting  standards that might look a bit unusual at first. These  standards are in place to make the rules elements in this  book easier to recognize. |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.569794 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/20` | 0.563156 | The back of this book has an  appendix with the rules for all of  the conditions that you will find  in the game. This section also  includes a blank character sheet,  and an index with a comprehensiv |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.561439 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/3` | 0.554888 | The names of specific statistics, skills, feats, actions,  and some other mechanical elements in Starfinder are  capitalized. This way, when you see the statement "a  Strike targets Armor Class," you |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.554086 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/3` | 0.550013 | **Directive**: Actions with this trait are special orders  that provide benefits for your allies if they follow  them. Your allies must be able to sense you to benefit  from your directives. This acti |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5` | 0.548598 | READING RULES |

### Query 28
- Text: What is the rule about [one-action] Single Actions?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `10`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/9', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/10', 'PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/9` | 0.838518 | [one-action] Single Actions |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/10` | 0.725136 | Single actions use this symbol: [one-action]. They're the simplest,  most common type of action. You can use three single  actions on your turn in an encounter, in any order you see  fit. |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/10` | 0.646995 | **ACTION OR FEAT NAME **[one-action] **LEVEL** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/52` | 0.607593 | **Requirements** Your last action was a 1-action directive. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.596024 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/2` | 0.594487 | single action would allow. You have to spend all the actions  an activity requires for its effects to happen. Spellcasting  is one of the most common activities, as most spells take  more than a singl |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/39` | 0.594461 | **KEEP ON KEEPING ON!** [one-action]** TO **[two-actions] |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12` | 0.594184 | **GET 'EM! **[one-action]** TO **[two-actions] |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/9/SectionHeader/3` | 0.589580 | **STEEL YOURSELVES! **[one-action]** TO **[two-actions] |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.586153 | **INTO POSITION! **[one-action]** TO **[two-actions] |

### Query 29
- Text: What is the rule about Single actions use this symbol: [one-action]. They're the simplest,  most common type of action. You can use three single  actions on your turn in an encounter, in any order you see  fit.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `11`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/10', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/3', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/10` | 0.992827 | Single actions use this symbol: [one-action]. They're the simplest,  most common type of action. You can use three single  actions on your turn in an encounter, in any order you see  fit. |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.766259 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/14` | 0.746756 | Free actions use this symbol: [free-action]. Free actions don't require  you to spend any of your three single actions or your reaction.  A free action might have a trigger like a reaction does. If so |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/12` | 0.693065 | Reactions use this symbol: [reaction]. These actions can be used even  when it's not your turn. You only get one reaction per encounter  round, and you can use it only when its specific trigger is  fu |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/2` | 0.690843 | single action would allow. You have to spend all the actions  an activity requires for its effects to happen. Spellcasting  is one of the most common activities, as most spells take  more than a singl |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/9` | 0.685396 | [one-action] Single Actions |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/29` | 0.623665 | You've worked with a team for so long that you've learned  to convey orders with a glance, a single word, or the tiniest  flick of your hand (or suitable appendage, depending on  ancestry). Once per t |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/37` | 0.610770 | **Trigger** The final action on your turn is a 1-action directive. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/12/Text/15` | 0.595581 | You have six arms, which allows you to wield and hold up to six hands' worth of weapons and equipment. At any time, one pair of hands is designated as your active hands. You can change this designatio |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/20` | 0.595555 | You succinctly direct your allies to find cover by any means  necessary. You and all allies within 60 feet count any form of  lesser cover as standard cover until the start of your next turn. **Lead b |

### Query 30
- Text: What is the rule about [reaction] Reactions?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `10`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/12', 'PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/11` | 0.666298 | [reaction] Reactions |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/12` | 0.637260 | Reactions use this symbol: [reaction]. These actions can be used even  when it's not your turn. You only get one reaction per encounter  round, and you can use it only when its specific trigger is  fu |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5` | 0.559267 | READING RULES |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.538469 | **WATCH OUT **[reaction] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/9` | 0.525461 | **COMPETITIVE SPIRIT **[reaction] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/26` | 0.524297 | **QUIP **[reaction] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/9` | 0.521743 | **CHANGE OF PLANS **[reaction] **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29` | 0.515936 | **INFLUENCE **[reaction] **FEAT 4** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1` | 0.514320 | FORMAT OF RULES |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/8` | 0.509594 | **TAG TEAM **[reaction] **FEAT 10** |

### Query 31
- Text: What is the rule about Reactions use this symbol: [reaction]. These actions can be used even  when it's not your turn. You only get one reaction per encounter  round, and you can use it only when its specific trigger is  fulfilled. Often, the trigger is another creature's action.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `11`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/12', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/10', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/12` | 0.991317 | Reactions use this symbol: [reaction]. These actions can be used even  when it's not your turn. You only get one reaction per encounter  round, and you can use it only when its specific trigger is  fu |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/10` | 0.743141 | Single actions use this symbol: [one-action]. They're the simplest,  most common type of action. You can use three single  actions on your turn in an encounter, in any order you see  fit. |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/14` | 0.739567 | Free actions use this symbol: [free-action]. Free actions don't require  you to spend any of your three single actions or your reaction.  A free action might have a trigger like a reaction does. If so |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.682246 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/24` | 0.653963 | When you use limited telepathy to communicate with another  creature, the creature can give you a brief response as a reaction,  or as a free action at the beginning of their next turn. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/23` | 0.653327 | When you aren't directing allies, you focus on a situation's  shifting circumstances, readying to react. At the end of each of  your turns, you gain one additional reaction, which you can use  before |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/27` | 0.646490 | When you warn an ally of an attack, you follow up with a  shot at your enemy. The first time each round you use your  Watch Out reaction, you can make a melee or ranged Strike  against the triggering |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/26` | 0.645741 | **Lead by Example** If you used two actions, Strike the target to  focus their attention on you. The target takes a –1 circumstance  penalty on attacks made against other creatures until the start  of |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/15` | 0.639642 | You love helping your friends and allies achieve their goals. At  the start of your turn, you gain one additional reaction, which  you can use only to Aid. |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/14` | 0.629044 | **Frequency** The limit on how often you can use the ability. **Trigger** Reactions and some free actions have triggers that  must be met before they can be used. |

### Query 32
- Text: What is the rule about [free-action] Free Actions?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `14`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/14', 'PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/13` | 0.779918 | [free-action] Free Actions |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/14` | 0.718206 | Free actions use this symbol: [free-action]. Free actions don't require  you to spend any of your three single actions or your reaction.  A free action might have a trigger like a reaction does. If so |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/23` | 0.603326 | Assign any free attribute boosts and decide if you are  taking any voluntary flaws. |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/13` | 0.586552 | **CENTER THOUGHTS **[free-action] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/9` | 0.560314 | [one-action] Single Actions |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/9` | 0.558575 | **SILVER TONGUE **[free-action] |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/2` | 0.558269 | **EXTEND DIRECTIVE **[free-action] **FEAT 16** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/8/SectionHeader/17` | 0.556233 | **IMPROVISED MASTERY **[free-action] |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.549470 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/13` | 0.537589 | **ALL HANDS ON DECK **[free-action] **FEAT 9** |

### Query 33
- Text: What is the rule about Free actions use this symbol: [free-action]. Free actions don't require  you to spend any of your three single actions or your reaction.  A free action might have a trigger like a reaction does. If so,  you can use it just like a reaction—even if it's not your turn.  However, you can use only one free action per trigger, so if  you have multiple free actions with the same trigger, you  have to decide which to use. If a free action doesn't have a  trigger, you use it like a single action, just without spending  any of your actions for the turn.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `13`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/14', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/3', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/14` | 1.015936 | Free actions use this symbol: [free-action]. Free actions don't require  you to spend any of your three single actions or your reaction.  A free action might have a trigger like a reaction does. If so |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.811926 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/10` | 0.767918 | Single actions use this symbol: [one-action]. They're the simplest,  most common type of action. You can use three single  actions on your turn in an encounter, in any order you see  fit. |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/12` | 0.710360 | Reactions use this symbol: [reaction]. These actions can be used even  when it's not your turn. You only get one reaction per encounter  round, and you can use it only when its specific trigger is  fu |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/14` | 0.649047 | **Frequency** The limit on how often you can use the ability. **Trigger** Reactions and some free actions have triggers that  must be met before they can be used. |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/13` | 0.635442 | [free-action] Free Actions |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.635186 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.618634 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/2` | 0.616725 | single action would allow. You have to spend all the actions  an activity requires for its effects to happen. Spellcasting  is one of the most common activities, as most spells take  more than a singl |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/29` | 0.608734 | You've worked with a team for so long that you've learned  to convey orders with a glance, a single word, or the tiniest  flick of your hand (or suitable appendage, depending on  ancestry). Once per t |

### Query 34
- Text: What is the rule about Activities?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/15', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/16', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/15` | 0.700443 | Activities |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/16` | 0.670379 | Activities are special tasks that you complete by spending  one or more of your actions together. Usually, an activity  uses two or more actions and lets you do more than a |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/4` | 0.588765 | All tasks that take longer than a turn are activities. If an  activity is meant to be done during exploration, it has the  exploration trait. An activity that takes a day or more of  commitment and th |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/2` | 0.543155 | single action would allow. You have to spend all the actions  an activity requires for its effects to happen. Spellcasting  is one of the most common activities, as most spells take  more than a singl |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.537469 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.537402 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5` | 0.509734 | READING RULES |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1` | 0.501707 | FORMAT OF RULES |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/20` | 0.500452 | You succinctly direct your allies to find cover by any means  necessary. You and all allies within 60 feet count any form of  lesser cover as standard cover until the start of your next turn. **Lead b |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.495664 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |

### Query 35
- Text: What is the rule about Activities are special tasks that you complete by spending  one or more of your actions together. Usually, an activity  uses two or more actions and lets you do more than a?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `16`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/16', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/2', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/16` | 0.961383 | Activities are special tasks that you complete by spending  one or more of your actions together. Usually, an activity  uses two or more actions and lets you do more than a |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/2` | 0.778900 | single action would allow. You have to spend all the actions  an activity requires for its effects to happen. Spellcasting  is one of the most common activities, as most spells take  more than a singl |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.758011 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/4` | 0.696749 | All tasks that take longer than a turn are activities. If an  activity is meant to be done during exploration, it has the  exploration trait. An activity that takes a day or more of  commitment and th |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/10` | 0.652525 | Single actions use this symbol: [one-action]. They're the simplest,  most common type of action. You can use three single  actions on your turn in an encounter, in any order you see  fit. |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/18` | 0.651024 | Sometimes an ability will grant multiple actions or an  action in addition to other benefits. These are condensed  into a shorter format using the same categories, as seen  below. |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.620720 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/14` | 0.620712 | **Frequency** The limit on how often you can use the ability. **Trigger** Reactions and some free actions have triggers that  must be met before they can be used. |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.618697 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/15` | 0.618058 | Activities |

### Query 36
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/18']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `15`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/28', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/24', 'PZO22001 Starfinder Player Core 014-029::/page/15/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/28` | 0.913367 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/24` | 0.913367 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/23` | 0.913367 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/27` | 0.871367 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/18` | 0.871367 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/29` | 0.863367 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/57` | 0.863367 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/56` | 0.863367 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/31` | 0.863367 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/30` | 0.863367 | **INTRODUCTION** |

### Query 37
- Text: What is the rule about **Character ** **Creation**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `38`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/19', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/29', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/19` | 0.792792 | **Character ** **Creation** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/29` | 0.792792 | **Character ** **Creation** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/25` | 0.792792 | **Character ** **Creation** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/24` | 0.750792 | **Character ** **Creation** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/28` | 0.750792 | **Character ** **Creation** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/3` | 0.750792 | **Character ** **Creation** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/17` | 0.715995 | Character Creation |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/15` | 0.588938 | **CHARACTER ** **SHEET** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/9/ListItem/14` | 0.583602 | ** A character receives an attribute boost to their  class's key attribute. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/48` | 0.580938 | **CHARACTER ** **SHEET** |

### Query 38
- Text: Summarize **Leveling Up**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/20']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/30', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/26', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/30` | 0.931277 | **Leveling Up** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/26` | 0.931277 | **Leveling Up** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/29` | 0.931277 | **Leveling Up** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/25` | 0.889277 | **Leveling Up** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/4` | 0.889277 | **Leveling Up** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/20` | 0.889277 | **Leveling Up** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/SectionHeader/0` | 0.795615 | LEVELING UP |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/18` | 0.726502 | Leveling Up |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/15/SectionHeader/11` | 0.717281 | **LEVELING-UP CHECKLIST** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.651709 | **OVERVIEW** |

### Query 39
- Text: Summarize **Exploring the ** **Galaxy**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/21']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `17`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/31', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/27', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/30']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/31` | 0.950997 | **Exploring the ** **Galaxy** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/27` | 0.950997 | **Exploring the ** **Galaxy** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/30` | 0.950997 | **Exploring the ** **Galaxy** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/5` | 0.908997 | **Exploring the ** **Galaxy** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/26` | 0.908997 | **Exploring the ** **Galaxy** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/21` | 0.908997 | **Exploring the ** **Galaxy** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/10` | 0.760142 | **Exploring the ** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/31` | 0.664750 | **CONCENTRATE** **ENVOY** **EXPLORATION** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/14` | 0.654720 | WHILE EXPLORING... |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/35` | 0.653697 | **PLAYING THE ** **GAME** |

### Query 40
- Text: Summarize **Religion**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/22']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `15`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/9/Text/28', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/32', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/28` | 0.815691 | **Religion** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/32` | 0.815691 | **Religion** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/31` | 0.815691 | **Religion** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/6` | 0.773691 | **Religion** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/22` | 0.773691 | **Religion** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/27` | 0.773691 | **Religion** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.696976 | **OVERVIEW** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/20` | 0.652835 | Religion |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/56` | 0.641768 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/44` | 0.641768 | **BACKGROUNDS** |

### Query 41
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/23', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/32', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/23` | 0.830013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/7` | 0.830013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/32` | 0.830013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/29` | 0.788013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/33` | 0.788013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/28` | 0.788013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/67` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/64` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/30` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/31` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 42
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/24']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `15`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/34', 'PZO22001 Starfinder Player Core 014-029::/page/15/Text/29', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/34` | 0.866254 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/29` | 0.866254 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/8` | 0.866254 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/30` | 0.824254 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/33` | 0.824254 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/24` | 0.824254 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/23` | 0.816254 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/58` | 0.816254 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/32` | 0.816254 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/40` | 0.816254 | **CLASSES** |

### Query 43
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `16`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/25', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/35', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/25` | 0.777771 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/35` | 0.777771 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/34` | 0.777771 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/30` | 0.735771 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/31` | 0.735771 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/9` | 0.735771 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/23` | 0.733791 | SKILLS |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/13` | 0.733791 | SKILLS |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/45` | 0.727771 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/55` | 0.727771 | **SKILLS** |

### Query 44
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `16`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/26', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/36', 'PZO22001 Starfinder Player Core 014-029::/page/15/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/26` | 0.735680 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/36` | 0.735680 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/31` | 0.735680 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/10` | 0.693680 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/35` | 0.693680 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/32` | 0.693680 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/47` | 0.685680 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/85` | 0.685680 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/46` | 0.685680 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/36` | 0.685680 | **FEATS** |

### Query 45
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/27', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/37', 'PZO22001 Starfinder Player Core 014-029::/page/15/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/27` | 0.915652 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/37` | 0.915652 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/32` | 0.915652 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/33` | 0.873652 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/47` | 0.865652 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/84` | 0.865652 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/76` | 0.865652 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/47` | 0.865652 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/47` | 0.865652 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/37` | 0.865652 | **EQUIPMENT** |

### Query 46
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `18`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/28', 'PZO22001 Starfinder Player Core 014-029::/page/15/Text/33', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/28` | 0.806592 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/34` | 0.806592 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/33` | 0.806592 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/38` | 0.764592 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/26` | 0.758199 | SPELLS |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/33` | 0.756592 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/83` | 0.756592 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/48` | 0.756592 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/49` | 0.756592 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/85` | 0.756592 | **SPELLS** |

### Query 47
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/39', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/35', 'PZO22001 Starfinder Player Core 014-029::/page/15/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/35` | 0.938833 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/39` | 0.938833 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/34` | 0.938833 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/37` | 0.896833 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/29` | 0.896833 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/84` | 0.888833 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/49` | 0.888833 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/34` | 0.888833 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/50` | 0.888833 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/42` | 0.888833 | **PLAYING THE ** **GAME** |

### Query 48
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/30']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `13`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/40', 'PZO22001 Starfinder Player Core 014-029::/page/15/Text/35', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/36']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/40` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/35` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/36` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/13` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/30` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/38` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/87` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/40` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/46` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/43` | 0.900802 | **CONDITIONS ** **APPENDIX** |

### Query 49
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/31']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `13`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/41', 'PZO22001 Starfinder Player Core 014-029::/page/15/Text/36', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/41` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/36` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/31` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/37` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/39` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/14` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/41` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/71` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/47` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/51` | 0.879439 | **GLOSSARY & ** **INDEX** |

### Query 50
- Text: What is the rule about single action would allow. You have to spend all the actions  an activity requires for its effects to happen. Spellcasting  is one of the most common activities, as most spells take  more than a single action to cast.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/2', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/10', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/2` | 0.961755 | single action would allow. You have to spend all the actions  an activity requires for its effects to happen. Spellcasting  is one of the most common activities, as most spells take  more than a singl |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/10` | 0.712672 | Single actions use this symbol: [one-action]. They're the simplest,  most common type of action. You can use three single  actions on your turn in an encounter, in any order you see  fit. |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/16` | 0.702033 | Activities are special tasks that you complete by spending  one or more of your actions together. Usually, an activity  uses two or more actions and lets you do more than a |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.661587 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/4` | 0.618032 | **Flourish**: Actions with this trait are special  techniques that require too much exertion for you to  perform frequently. You can use only 1 action with the  flourish trait per turn. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/7` | 0.605187 | Spellcasting classes grant a proficiency rank for spell  attacks and DCs, which are further detailed in each class's  entry. These classes rarely use their class DC. |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/16` | 0.595634 | This chapter starts with rules for casting spells,  determining their effects, and negating foes' spells  (called counteracting). After that, the spell lists for  each spellcasting tradition are inclu |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/14` | 0.589474 | Free actions use this symbol: [free-action]. Free actions don't require  you to spend any of your three single actions or your reaction.  A free action might have a trigger like a reaction does. If so |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.582609 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/19` | 0.580437 | Many characters can learn a few cantrips or focus spells,  but the mystic and witchwarper gain spellcasting—the  ability to cast a wide variety of spells. If your character's  class grants spells, you |

### Query 51
- Text: What is the rule about Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you can cast in an instant, which use a free action  or a reaction.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `16`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/3', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/14', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.981407 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/14` | 0.810671 | Free actions use this symbol: [free-action]. Free actions don't require  you to spend any of your three single actions or your reaction.  A free action might have a trigger like a reaction does. If so |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/10` | 0.768397 | Single actions use this symbol: [one-action]. They're the simplest,  most common type of action. You can use three single  actions on your turn in an encounter, in any order you see  fit. |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/2` | 0.703398 | single action would allow. You have to spend all the actions  an activity requires for its effects to happen. Spellcasting  is one of the most common activities, as most spells take  more than a singl |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/12` | 0.695837 | Reactions use this symbol: [reaction]. These actions can be used even  when it's not your turn. You only get one reaction per encounter  round, and you can use it only when its specific trigger is  fu |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/16` | 0.683962 | Activities are special tasks that you complete by spending  one or more of your actions together. Usually, an activity  uses two or more actions and lets you do more than a |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.667229 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/14` | 0.652359 | **Frequency** The limit on how often you can use the ability. **Trigger** Reactions and some free actions have triggers that  must be met before they can be used. |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.628874 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/12/Text/15` | 0.624052 | You have six arms, which allows you to wield and hold up to six hands' worth of weapons and equipment. At any time, one pair of hands is designated as your active hands. You can change this designatio |

### Query 52
- Text: What is the rule about All tasks that take longer than a turn are activities. If an  activity is meant to be done during exploration, it has the  exploration trait. An activity that takes a day or more of  commitment and that can be done only during downtime  has the downtime trait.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/4', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/16', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/4` | 0.979721 | All tasks that take longer than a turn are activities. If an  activity is meant to be done during exploration, it has the  exploration trait. An activity that takes a day or more of  commitment and th |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/16` | 0.681886 | Activities are special tasks that you complete by spending  one or more of your actions together. Usually, an activity  uses two or more actions and lets you do more than a |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.672610 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/4` | 0.620946 | **Flourish**: Actions with this trait are special  techniques that require too much exertion for you to  perform frequently. You can use only 1 action with the  flourish trait per turn. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/2` | 0.574719 | single action would allow. You have to spend all the actions  an activity requires for its effects to happen. Spellcasting  is one of the most common activities, as most spells take  more than a singl |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.571188 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/3` | 0.564516 | **Directive**: Actions with this trait are special orders  that provide benefits for your allies if they follow  them. Your allies must be able to sense you to benefit  from your directives. This acti |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` | 0.563918 | Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.561947 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/26` | 0.559972 | Your varied life experiences let you adapt to nearly any  situation. When you gain skill feats using adaptive talent,  you gain two additional skill feats. In addition, you can adapt  to the day's cha |

### Query 53
- Text: Summarize READING RULES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `27`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5', 'PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5` | 0.897539 | READING RULES |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1` | 0.720411 | FORMAT OF RULES |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/8` | 0.655644 | READING CLASS ENTRIES |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6` | 0.596247 | UNDERSTANDING ACTIONS |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/9` | 0.525381 | CHAPTER 4: SKILLS |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/2` | 0.522624 | Throughout this rulebook, you will see formatting  standards that might look a bit unusual at first. These  standards are in place to make the rules elements in this  book easier to recognize. |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/1` | 0.521073 | SAMPLE CHARACTER |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/10` | 0.520971 | STEP 7: RECORD CLASS DETAILS |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.519250 | **OVERVIEW** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/7` | 0.519033 | CHAPTER 3: CLASSES |

### Query 54
- Text: What is the rule about This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an individual character often has special  rules that empower them to do things most other characters  can't. Most of these options are granted by feats, which are  gained by making certain choices at character creation or  when a character advances in level.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/6', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/12', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 1.009536 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/12` | 0.775170 | As a character advances in level, they gain additional feats  to represent their growing abilities. General feats and skill  feats (which are a subset of general feats) are presented  in this chapter. |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.774625 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.743136 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.727587 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.721821 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.719425 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.718755 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/7` | 0.689474 | You can find all the new abilities specific to your class,  including class feats, right in your class entry, though you  can also use class feats to take an archetype (page 174).  Your character's cl |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/16` | 0.677276 | This chapter starts with rules for casting spells,  determining their effects, and negating foes' spells  (called counteracting). After that, the spell lists for  each spellcasting tradition are inclu |

### Query 55
- Text: What is the rule about Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules element to life during play.  Where appropriate, rules presentations are introduced  with an explanation of their format. For example, the  Ancestry section of Chapter 2 contains rules for the ten  ancestries in this book, and an explanation of the ancestry  sections appears at the beginning of that chapter.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `36`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/7', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/8', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` | 1.024421 | Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.736384 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.734347 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/6` | 0.681460 | The rules for ancestries and heritages representing the  Pact Worlds are in this chapter, including their ancestry  feat options. Backgrounds are at the end of this chapter,  along with a section abou |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/9` | 0.680005 | Spells, tech items, and magic items use a similar format,  but their stat blocks contain a number of unique elements,  such as the possible magical traditions for a spell (see  Chapter 7 for more on r |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.659700 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/19` | 0.639505 | Select an ancestry for your character. The ancestry  summaries on page 27 provide an overview of Starfinder's  core ancestry options, and each is fully detailed in Chapter  2. Ancestry determines your |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/26` | 0.637444 | This section serves as a reminder of the ancestry feats your  character gains at 5th, 9th, 13th, and 17th levels. Ancestry  feats are detailed in each ancestry entry in Chapter 2, which  begins on pag |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.632790 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/2` | 0.630532 | On pages 27–28, you'll see a visual representation  of ancestries and classes that provides at-a-glance  information for players looking to make the most of  their starting attribute modifiers. In the |

### Query 56
- Text: What is the rule about The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, reactions, and free actions  each have the corresponding icon next to their name to  indicate their type. An activity that can be completed in  a single turn has a symbol indicating how many actions  are needed to complete it; activities that take longer to  perform omit these icons. If a character must attain a  certain level before accessing an ability, that level is  indicated to the right of the stat block's name. Rules also  often have traits associated with them (traits appear in the  Glossary and Index).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `32`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/8', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/7', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 1.018390 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` | 0.731874 | Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.705900 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.647233 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/9` | 0.645254 | Spells, tech items, and magic items use a similar format,  but their stat blocks contain a number of unique elements,  such as the possible magical traditions for a spell (see  Chapter 7 for more on r |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/13` | 0.642218 | **Prerequisites** Any minimum attributes, feats, proficiency  ranks, and so forth you must have to select this rules  element are here. Feats also have a level prerequisite,  listed above. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.641002 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/4` | 0.624167 | All tasks that take longer than a turn are activities. If an  activity is meant to be done during exploration, it has the  exploration trait. An activity that takes a day or more of  commitment and th |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.623040 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.619427 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |

### Query 57
- Text: What is the rule about Spells, tech items, and magic items use a similar format,  but their stat blocks contain a number of unique elements,  such as the possible magical traditions for a spell (see  Chapter 7 for more on reading spells).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `31`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/9', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/7', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/9` | 0.941232 | Spells, tech items, and magic items use a similar format,  but their stat blocks contain a number of unique elements,  such as the possible magical traditions for a spell (see  Chapter 7 for more on r |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` | 0.705805 | Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.641550 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/19` | 0.581282 | Many characters can learn a few cantrips or focus spells,  but the mystic and witchwarper gain spellcasting—the  ability to cast a wide variety of spells. If your character's  class grants spells, you |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/16` | 0.580963 | This chapter starts with rules for casting spells,  determining their effects, and negating foes' spells  (called counteracting). After that, the spell lists for  each spellcasting tradition are inclu |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/2` | 0.577914 | Throughout this rulebook, you will see formatting  standards that might look a bit unusual at first. These  standards are in place to make the rules elements in this  book easier to recognize. |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.561530 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/3` | 0.554298 | The names of specific statistics, skills, feats, actions,  and some other mechanical elements in Starfinder are  capitalized. This way, when you see the statement "a  Strike targets Armor Class," you |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/17` | 0.548910 | Add spells and spell slots if your class grants  spellcasting. See Chapter 7 for spells. |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/2` | 0.543976 | single action would allow. You have to spend all the actions  an activity requires for its effects to happen. Spellcasting  is one of the most common activities, as most spells take  more than a singl |

### Query 58
- Text: What is the rule about **ACTION OR FEAT NAME **[one-action] **LEVEL**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `6`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/10', 'PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/9', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/10` | 0.870330 | **ACTION OR FEAT NAME **[one-action] **LEVEL** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.681303 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/9` | 0.661275 | [one-action] Single Actions |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/10` | 0.632553 | Single actions use this symbol: [one-action]. They're the simplest,  most common type of action. You can use three single  actions on your turn in an encounter, in any order you see  fit. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22` | 0.627747 | **SEARCH HIGH AND LOW! **[one-action]** TO **[two-actions] **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.617898 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.617684 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/13` | 0.615181 | **DON'T YOU DIE ON ME **[one-action] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.612791 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12` | 0.610519 | **GET 'EM! **[one-action]** TO **[two-actions] |

### Query 59
- Text: What is the rule about **TRAITS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/12', 'PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/11', 'PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/12` | 0.785979 | **TRAITS** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/12/SectionHeader/10` | 0.729935 | TRAITS |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/12` | 0.729935 | TRAITS |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/10` | 0.725652 | **TRAITS ** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/4/SectionHeader/12` | 0.725652 | **TRAITS ** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/11` | 0.606724 | **Attribute Flaws** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1` | 0.598290 | FORMAT OF RULES |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/4` | 0.579874 | **Attributes** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/3` | 0.552743 | **Directive**: Actions with this trait are special orders  that provide benefits for your allies if they follow  them. Your allies must be able to sense you to benefit  from your directives. This acti |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/15` | 0.547952 | **CHARACTER SHEET** |

### Query 60
- Text: What are the requirements for **Prerequisites** Any minimum attributes, feats, proficiency  ranks, and so forth you must have to select this rules  element are here. Feats also have a level prerequisite,  listed above.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/13', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/10', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/13` | 1.016726 | **Prerequisites** Any minimum attributes, feats, proficiency  ranks, and so forth you must have to select this rules  element are here. Feats also have a level prerequisite,  listed above. |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.743900 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/12` | 0.722849 | As a character advances in level, they gain additional feats  to represent their growing abilities. General feats and skill  feats (which are a subset of general feats) are presented  in this chapter. |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.713277 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.690910 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/15` | 0.690257 | At every level that you gain an envoy feat, you can select  one of the following feats. You must satisfy any prerequisites  before selecting the feat. |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.679134 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.672403 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/15` | 0.671305 | **Requirements** Sometimes you must have a certain item or  be in a certain circumstance to use an ability. |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/16` | 0.666647 | Select feats as indicated on your class advancement  table. For ancestry feats, see Chapter 2. For class  feats, see your class entry in Chapter 3. For general  feats and skill feats, see Chapter 5. |

### Query 61
- Text: What is the rule about **Frequency** The limit on how often you can use the ability. **Trigger** Reactions and some free actions have triggers that  must be met before they can be used.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `16`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/14', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/19', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/14` | 0.933136 | **Frequency** The limit on how often you can use the ability. **Trigger** Reactions and some free actions have triggers that  must be met before they can be used. |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.815760 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/11` | 0.703862 | **Beginner's** **Luck** [free-action] (fortune) **Frequency** once per day;  **Trigger** You fail a skill check using a skill that you're  untrained in; **Effect** Reroll the triggering check and use |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/15` | 0.701272 | **Requirements** Sometimes you must have a certain item or  be in a certain circumstance to use an ability. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/14` | 0.639460 | Free actions use this symbol: [free-action]. Free actions don't require  you to spend any of your three single actions or your reaction.  A free action might have a trigger like a reaction does. If so |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/4` | 0.634837 | **Flourish**: Actions with this trait are special  techniques that require too much exertion for you to  perform frequently. You can use only 1 action with the  flourish trait per turn. |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/12` | 0.621282 | Reactions use this symbol: [reaction]. These actions can be used even  when it's not your turn. You only get one reaction per encounter  round, and you can use it only when its specific trigger is  fu |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.612085 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/2` | 0.606381 | single action would allow. You have to spend all the actions  an activity requires for its effects to happen. Spellcasting  is one of the most common activities, as most spells take  more than a singl |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/45` | 0.605575 | **Trigger** A creature critically fails a melee Strike against you. **Requirements** The triggering creature is within your reach,  you have at least one free active hand, and your target is  no more |

### Query 62
- Text: What is the rule about **Requirements** Sometimes you must have a certain item or  be in a certain circumstance to use an ability.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/15', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/19', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/15` | 0.905173 | **Requirements** Sometimes you must have a certain item or  be in a certain circumstance to use an ability. |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.686405 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/13` | 0.685210 | **Prerequisites** Any minimum attributes, feats, proficiency  ranks, and so forth you must have to select this rules  element are here. Feats also have a level prerequisite,  listed above. |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/14` | 0.644476 | **Frequency** The limit on how often you can use the ability. **Trigger** Reactions and some free actions have triggers that  must be met before they can be used. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.627485 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.611939 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.611261 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.611155 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/6` | 0.599874 | You're quick thinking and adaptable, capable of picking up  new skills and talents with little practice or training. During  your daily preparations, select one skill feat that you meet  the prerequis |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/4` | 0.593578 | **Flourish**: Actions with this trait are special  techniques that require too much exertion for you to  perform frequently. You can use only 1 action with the  flourish trait per turn. |

### Query 63
- Text: What is the rule about This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or grants a constant effect, the benefit is  explained here.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `33`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/16', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/17', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 1.026037 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.771881 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.711917 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/18` | 0.672207 | Sometimes an ability will grant multiple actions or an  action in addition to other benefits. These are condensed  into a shorter format using the same categories, as seen  below. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` | 0.655828 | Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.642836 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.620139 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/3` | 0.619353 | **Directive**: Actions with this trait are special orders  that provide benefits for your allies if they follow  them. Your allies must be able to sense you to benefit  from your directives. This acti |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 0.616664 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.616630 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |

### Query 64
- Text: What is the rule about **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/17', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/16', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 1.019833 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.768294 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/27` | 0.737863 | **Special** You can select this feat more than once. |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/24` | 0.737863 | **Special** You can select this feat more than once. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.732070 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.698375 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/13` | 0.681859 | **Prerequisites** Any minimum attributes, feats, proficiency  ranks, and so forth you must have to select this rules  element are here. Feats also have a level prerequisite,  listed above. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.678493 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.671266 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.657221 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |

### Query 65
- Text: What is the rule about Sometimes an ability will grant multiple actions or an  action in addition to other benefits. These are condensed  into a shorter format using the same categories, as seen  below.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/18', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/17', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/18` | 0.964179 | Sometimes an ability will grant multiple actions or an  action in addition to other benefits. These are condensed  into a shorter format using the same categories, as seen  below. |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.726261 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.723342 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/15` | 0.642030 | **Requirements** Sometimes you must have a certain item or  be in a certain circumstance to use an ability. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.638363 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.631598 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/16` | 0.629821 | Activities are special tasks that you complete by spending  one or more of your actions together. Usually, an activity  uses two or more actions and lets you do more than a |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.620028 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.611751 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/14` | 0.600000 | **Frequency** The limit on how often you can use the ability. **Trigger** Reactions and some free actions have triggers that  must be met before they can be used. |

### Query 66
- Text: What is the rule about **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed here; **Effect** this section explains  how the ability changes the world.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/2/Text/19', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/14', 'PZO22001 Starfinder Player Core 014-029::/page/2/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/19` | 0.980197 | **Name** [one-action] (traits) **Frequency** how often it can be used;  **Trigger** when a reaction or free action can be  used; **Requirements** some actions require specific  circumstances, listed h |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/14` | 0.830846 | **Frequency** The limit on how often you can use the ability. **Trigger** Reactions and some free actions have triggers that  must be met before they can be used. |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/15` | 0.709472 | **Requirements** Sometimes you must have a certain item or  be in a certain circumstance to use an ability. |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/11` | 0.685056 | **Beginner's** **Luck** [free-action] (fortune) **Frequency** once per day;  **Trigger** You fail a skill check using a skill that you're  untrained in; **Effect** Reroll the triggering check and use |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/16` | 0.655564 | This section describes the effects or benefits of a rules  element. If the rule is an action, it explains what the effect  is or what you must roll. If it's a feat that modifies an  existing action or |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/8` | 0.647884 | The general format for stat blocks is shown below.  Entries are omitted from a stat block when they don't  apply, so not all rule elements will have ever each of the  entries given below. Actions, rea |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/4` | 0.641459 | **Flourish**: Actions with this trait are special  techniques that require too much exertion for you to  perform frequently. You can use only 1 action with the  flourish trait per turn. |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/3` | 0.634164 | Activities that use two actions use this symbol: [two-actions].  Meanwhile, activities that use three actions use this  symbol: [three-actions]. There are also special activities, such as  spells you |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/14` | 0.630988 | Free actions use this symbol: [free-action]. Free actions don't require  you to spend any of your three single actions or your reaction.  A free action might have a trigger like a reaction does. If so |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.616488 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |

### Query 67
- Text: What is the rule about Unless you're the GM, the first thing you need to do when playing Starfinder is create your character. It's  up to you to imagine your character's past experiences, personality, and view of the galaxy, and this will  set the stage for your roleplaying during the game. You'll use the game's mechanics to determine your  character's ability to perform various tasks and use special abilities.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/3/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `39`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/3/Text/1', 'PZO22001 Starfinder Player Core 014-029::/page/3/Text/3', 'PZO22001 Starfinder Player Core 014-029::/page/4/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/1` | 1.007699 | Unless you're the GM, the first thing you need to do when playing Starfinder is create your character. It's  up to you to imagine your character's past experiences, personality, and view of the galaxy |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/3` | 0.827020 | This section provides a step-by-step guide for creating a  character using the Starfinder rules, preceded by a guide to  help you understand attribute modifiers. These modifiers are a  critical part o |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/5` | 0.803764 | their past, and think about how and why they adventure.  You'll want to peruse Starfinder's available ancestries,  backgrounds, and classes. The summaries on pages 27–28  might help you match your con |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.759048 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/15` | 0.756294 | You might want to coordinate with other players when  forming your character concept. Your characters could have  something in common already; perhaps they are travelers  from the same home world, or |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/4` | 0.755218 | This introduction is designed to help you understand the  basics of Starfinder. This chapter also includes the rules for  building and leveling up a character, as well as an example  of the character |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/18` | 0.746154 | This important chapter contains  the universal rules needed to play  Starfinder, including rules for the  various modes of play, the basic  actions that every character can  perform, the rules for com |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/7` | 0.722683 | Characters and their adversaries affect the galaxy of  Starfinder by using actions and producing effects. This is  especially the case during encounters, when every action  counts. When you use an act |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/5` | 0.677796 | The entries on the pages that follow describe six classes  in Starfinder. Each entry contains the information you  need to play a character of that class, as well as how to  develop them from their hu |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/9` | 0.664577 | Write down the deity your character worships, if any.  Your character might worship several deities as part of a  personal pantheon. You might instead choose a philosophy  or decide your character is |

### Query 68
- Text: What is the rule about This section provides a step-by-step guide for creating a  character using the Starfinder rules, preceded by a guide to  help you understand attribute modifiers. These modifiers are a  critical part of your character, and you will be asked to make  choices about them during many of the following steps. The  steps of character creation are presented in a suggested order,  but you can complete them in whatever order you prefer.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/3/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `42`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/3/Text/3', 'PZO22001 Starfinder Player Core 014-029::/page/0/Text/2', 'PZO22001 Starfinder Player Core 014-029::/page/3/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/3` | 1.029821 | This section provides a step-by-step guide for creating a  character using the Starfinder rules, preceded by a guide to  help you understand attribute modifiers. These modifiers are a  critical part o |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.850325 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/1` | 0.821828 | Unless you're the GM, the first thing you need to do when playing Starfinder is create your character. It's  up to you to imagine your character's past experiences, personality, and view of the galaxy |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/4` | 0.779415 | This introduction is designed to help you understand the  basics of Starfinder. This chapter also includes the rules for  building and leveling up a character, as well as an example  of the character |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/18` | 0.749815 | This important chapter contains  the universal rules needed to play  Starfinder, including rules for the  various modes of play, the basic  actions that every character can  perform, the rules for com |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/2` | 0.746599 | One of the most important aspects of your character is their attribute modifiers. These numbers represent your  character's raw potential, and they influence nearly every other statistic on your chara |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/19` | 0.743435 | At this point, you need to start building your character's  attribute modifiers. See the overview of attribute modifiers  on page 23 for more information about these important  aspects of your charact |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/15` | 0.740020 | You might want to coordinate with other players when  forming your character concept. Your characters could have  something in common already; perhaps they are travelers  from the same home world, or |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/12/Text/2` | 0.729705 | This step-by-step example illustrates the process of  creating a Starfinder character. |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/19` | 0.726451 | Select an ancestry for your character. The ancestry  summaries on page 27 provide an overview of Starfinder's  core ancestry options, and each is fully detailed in Chapter  2. Ancestry determines your |

### Query 69
- Text: Summarize STEP 1: CREATE A CONCEPT
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/3/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `29`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/3/SectionHeader/7', 'PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/3', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/3/SectionHeader/7` | 0.985136 | STEP 1: CREATE A CONCEPT |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/3` | 0.745931 | STEPS 1 AND 2 |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/3` | 0.738207 | CHAPTER 1: INTRODUCTION |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/6/SectionHeader/3` | 0.691608 | STEP 4: PICK A BACKGROUND |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/12` | 0.628606 | 1ST LEVEL |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/8` | 0.628606 | 1ST LEVEL |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/16` | 0.628606 | 1ST LEVEL |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/8` | 0.628606 | 1ST LEVEL |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/8` | 0.628606 | 1ST LEVEL |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/18` | 0.626755 | STEP 10: FINISHING DETAILS |

### Query 70
- Text: Summarize **Exploring the **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/3/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/3/Text/10', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/21', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/10` | 0.937935 | **Exploring the ** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/31` | 0.836807 | **Exploring the ** **Galaxy** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/21` | 0.836807 | **Exploring the ** **Galaxy** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/26` | 0.794807 | **Exploring the ** **Galaxy** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/27` | 0.794807 | **Exploring the ** **Galaxy** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/30` | 0.794807 | **Exploring the ** **Galaxy** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/5` | 0.794807 | **Exploring the ** **Galaxy** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.725777 | **OVERVIEW** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/12` | 0.717180 | **PLAYING THE ** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/86` | 0.709180 | **PLAYING THE ** |

### Query 71
- Text: Summarize **OVERVIEW**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `17`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/24', 'PZO22001 Starfinder Player Core 014-029::/page/15/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.926785 | **OVERVIEW** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/23` | 0.715141 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/24` | 0.715141 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/44` | 0.705564 | **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/67` | 0.705564 | **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/56` | 0.705564 | **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7` | 0.701955 | **HIT POINTS** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/28` | 0.673141 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/18` | 0.673141 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/27` | 0.673141 | **INTRODUCTION** |

### Query 72
- Text: Summarize FAITH
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `16`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/12', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/20', 'PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/12` | 0.792457 | FAITH |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/20` | 0.625728 | Religion |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/6` | 0.625304 | PERCEPTION |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/18` | 0.619121 | BELIEFS |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/5/SectionHeader/19` | 0.619121 | BELIEFS |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/13/SectionHeader/19` | 0.619121 | BELIEFS |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/9/SectionHeader/18` | 0.619121 | BELIEFS |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/24` | 0.575400 | FEATS |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.556003 | **OVERVIEW** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/51` | 0.555246 | **PERCEPTION** |

### Query 73
- Text: Summarize YOUR ALLIES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `5`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/14', 'PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6', 'PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/14` | 0.870074 | YOUR ALLIES |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/54` | 0.610472 | You provide a quick follow-up to your ongoing directive,  encouraging your ally when they successfully hit your |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/42` | 0.593298 | During your daily preparations, you can review stratagems  with up to five allies. Later, you can quickly advise each of  these allies on your schemes using the reaction below. |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6` | 0.578101 | UNDERSTANDING ACTIONS |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/15` | 0.574506 | With quick commands, you get your allies to ready their  equipment. You and all allies within 30 feet can Interact to  draw, Switch Hands, or swap weapons as a reaction. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/20` | 0.571373 | You succinctly direct your allies to find cover by any means  necessary. You and all allies within 60 feet count any form of  lesser cover as standard cover until the start of your next turn. **Lead b |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.568840 | **OVERVIEW** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/48` | 0.561373 | You instinctively react to trouble by directing your allies to  act at the exact moment their intervention would matter  most. Issue a 1-action directive. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/25` | 0.561062 | **Lead by Example** If you used two actions, you and your  selected ally count any enemies that you both threaten as |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/42` | 0.559718 | You're always ready to help your allies when they need you the  most. You can use Communalism once per hour, rather than  once per day. |

### Query 74
- Text: Summarize **Strength**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `18`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/5', 'PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1', 'PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/5` | 0.885663 | **Strength** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.728442 | **OVERVIEW** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/12` | 0.693395 | **TRAITS** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/31` | 0.650594 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/9` | 0.650594 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/35` | 0.650594 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/34` | 0.650594 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/30` | 0.650594 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/25` | 0.650594 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/11` | 0.649302 | **Intelligence** |

### Query 75
- Text: Summarize **Dexterity**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/7', 'PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/5', 'PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/7` | 0.890468 | **Dexterity** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/5` | 0.653622 | **Strength** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/12` | 0.633096 | **TRAITS** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.589464 | **OVERVIEW** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/11` | 0.587780 | **Intelligence** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/4/SectionHeader/12` | 0.583178 | **TRAITS ** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/10` | 0.583178 | **TRAITS ** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/4` | 0.580523 | **Attributes** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/25` | 0.579660 | **CHARACTER SHEET** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/16` | 0.579660 | **CHARACTER SHEET** |

### Query 76
- Text: Summarize **Constitution**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `17`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/9', 'PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/24']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/9` | 0.859875 | **Constitution** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.713748 | **OVERVIEW** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/24` | 0.665764 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/8` | 0.625692 | **8 + Constitution modifier** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/23` | 0.623764 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/18` | 0.623764 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/27` | 0.623764 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/28` | 0.623764 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/57` | 0.615764 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/30` | 0.615764 | **INTRODUCTION** |

### Query 77
- Text: Summarize **Intelligence**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `15`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/11', 'PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/13', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/11` | 0.884268 | **Intelligence** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/13` | 0.763812 | **Wisdom** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/25` | 0.737041 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/9` | 0.695041 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/30` | 0.695041 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/31` | 0.695041 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/35` | 0.695041 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/34` | 0.695041 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.690929 | **OVERVIEW** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/45` | 0.687041 | **SKILLS** |

### Query 78
- Text: Summarize **Wisdom**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `21`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/13', 'PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/11', 'PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/13` | 0.871335 | **Wisdom** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/11` | 0.744297 | **Intelligence** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.707818 | **OVERVIEW** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/25` | 0.663605 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/31` | 0.663605 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/9` | 0.663605 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/30` | 0.663605 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/35` | 0.663605 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/34` | 0.663605 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/84` | 0.655605 | **SKILLS** |

### Query 79
- Text: Summarize **Charisma**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/15', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/42', 'PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/15` | 0.880012 | **Charisma** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/5` | 0.830013 | **Charisma** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/8/Text/9` | 0.681920 | ATTRIBUTE FLAW Charisma |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/42` | 0.671832 | — Constitution Charisma Wisdom |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/15` | 0.649368 | **CHARACTER SHEET** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/21` | 0.607368 | **CHARACTER SHEET** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/15` | 0.607368 | **CHARACTER SHEET** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/25` | 0.607368 | **CHARACTER SHEET** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/16` | 0.607368 | **CHARACTER SHEET** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/38` | 0.606188 | Charisma, Free Dexterity, Charisma, Free Constitution, Wisdom, Free Dexterity, Charisma, Free |

### Query 80
- Text: Summarize STEP 3: SELECT AN ANCESTRY
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `35`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/18', 'PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/5', 'PZO22001 Starfinder Player Core 014-029::/page/6/SectionHeader/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/18` | 0.997827 | STEP 3: SELECT AN ANCESTRY |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/5` | 0.723041 | STEP 3 |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/6/SectionHeader/3` | 0.694229 | STEP 4: PICK A BACKGROUND |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/3/SectionHeader/7` | 0.646511 | STEP 1: CREATE A CONCEPT |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/28` | 0.626954 | ANCESTRY AND BACKGROUND |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/8` | 0.623124 | ANCESTRY, BACKGROUND, CLASS,  OR DETAILS |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/21` | 0.612821 | Pick the ancestry itself. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/8/SectionHeader/5` | 0.612039 | ADAPTIVE TALENT 3RD |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/8/SectionHeader/13` | 0.611179 | ANCESTRY FEATS 5TH |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/7` | 0.609059 | CHAPTER 3: CLASSES |

### Query 81
- Text: Summarize Pick the ancestry itself.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/21', 'PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/22', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/55']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/21` | 0.943471 | Pick the ancestry itself. |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/22` | 0.786556 | Select a heritage from those available within that  ancestry, further defining the traits your character was  born with. |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/55` | 0.714073 | VESK YSOKI These heritages can be chosen for a member of any ancestry. |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/24` | 0.649904 | Choose an ancestry feat, representing an ability your  hero learned at an early age. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/20` | 0.642098 | You'll have four decisions to make when you choosing your  character's ancestry. |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/13/SectionHeader/27` | 0.631855 | ANCESTRIES |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/21` | 0.629982 | ANCESTRIES & BACKGROUNDS |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/13/SectionHeader/54` | 0.618473 | ANCESTRIES VERSATILE HERITAGES |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/3` | 0.614546 | **Ancestry:** Each ancestry provides attribute boosts, and sometimes an attribute flaw. If you're taking any voluntary  flaws, apply them in this step (see the sidebar on page 25). |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/19` | 0.609219 | Select an ancestry for your character. The ancestry  summaries on page 27 provide an overview of Starfinder's  core ancestry options, and each is fully detailed in Chapter  2. Ancestry determines your |

### Query 82
- Text: Summarize Assign any free attribute boosts and decide if you are  taking any voluntary flaws.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `35`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/23', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/3', 'PZO22001 Starfinder Player Core 014-029::/page/9/ListItem/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/23` | 1.002551 | Assign any free attribute boosts and decide if you are  taking any voluntary flaws. |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/3` | 0.798258 | **Ancestry:** Each ancestry provides attribute boosts, and sometimes an attribute flaw. If you're taking any voluntary  flaws, apply them in this step (see the sidebar on page 25). |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/ListItem/13` | 0.757136 | * Any character can choose to take two free boosts  instead of the listed boosts and flaws (page 24). |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Footnote/61` | 0.713283 | *Any character can choose to take two free boosts instead of the listed boosts and flaws (page 24). |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/6` | 0.705831 | **Four Free Boosts:** After the other steps, you apply four more attribute boosts to attributes of your choice to finalize  your starting attribute modifiers. |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/9` | 0.696202 | Whenever your character receives an attribute  boost, the source indicates whether it must be applied  to a specific attribute modifier, to one in a limited list,  or whether it's a "free" boost that |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/7/ListItem/6` | 0.693732 | Then, apply four free attribute boosts to your character's attribute modifiers. Choose a different attribute modifier for each and increase that attribute modifier by 1. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/4` | 0.669670 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/10/Text/2` | 0.668926 | The attribute boosts and flaws listed in each ancestry  represent general trends or help guide players to  create the kinds of characters from that ancestry most  likely to pursue the life of an adven |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/5` | 0.664514 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |

### Query 83
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `15`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/28', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/24', 'PZO22001 Starfinder Player Core 014-029::/page/15/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/28` | 0.913367 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/24` | 0.913367 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/23` | 0.913367 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/27` | 0.871367 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/18` | 0.871367 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/29` | 0.863367 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/57` | 0.863367 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/56` | 0.863367 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/31` | 0.863367 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/30` | 0.863367 | **INTRODUCTION** |

### Query 84
- Text: Summarize **Leveling Up**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/30', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/26', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/30` | 0.931277 | **Leveling Up** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/26` | 0.931277 | **Leveling Up** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/29` | 0.931277 | **Leveling Up** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/25` | 0.889277 | **Leveling Up** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/4` | 0.889277 | **Leveling Up** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/20` | 0.889277 | **Leveling Up** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/SectionHeader/0` | 0.795615 | LEVELING UP |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/18` | 0.726502 | Leveling Up |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/15/SectionHeader/11` | 0.717281 | **LEVELING-UP CHECKLIST** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.651709 | **OVERVIEW** |

### Query 85
- Text: Summarize **Exploring the ** **Galaxy**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `17`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/31', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/27', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/30']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/31` | 0.950997 | **Exploring the ** **Galaxy** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/27` | 0.950997 | **Exploring the ** **Galaxy** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/30` | 0.950997 | **Exploring the ** **Galaxy** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/5` | 0.908997 | **Exploring the ** **Galaxy** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/26` | 0.908997 | **Exploring the ** **Galaxy** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/21` | 0.908997 | **Exploring the ** **Galaxy** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/10` | 0.760142 | **Exploring the ** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/31` | 0.664750 | **CONCENTRATE** **ENVOY** **EXPLORATION** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/14` | 0.654720 | WHILE EXPLORING... |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/35` | 0.653697 | **PLAYING THE ** **GAME** |

### Query 86
- Text: Summarize **Religion**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/32']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `15`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/9/Text/28', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/32', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/28` | 0.815691 | **Religion** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/32` | 0.815691 | **Religion** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/31` | 0.815691 | **Religion** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/6` | 0.773691 | **Religion** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/22` | 0.773691 | **Religion** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/27` | 0.773691 | **Religion** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.696976 | **OVERVIEW** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/20` | 0.652835 | Religion |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/56` | 0.641768 | **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/44` | 0.641768 | **BACKGROUNDS** |

### Query 87
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `15`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/34', 'PZO22001 Starfinder Player Core 014-029::/page/15/Text/29', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/34` | 0.866254 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/29` | 0.866254 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/8` | 0.866254 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/30` | 0.824254 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/33` | 0.824254 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/24` | 0.824254 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/23` | 0.816254 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/58` | 0.816254 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/32` | 0.816254 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/40` | 0.816254 | **CLASSES** |

### Query 88
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/37']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `19`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/1/Text/27', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/37', 'PZO22001 Starfinder Player Core 014-029::/page/15/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/27` | 0.915652 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/37` | 0.915652 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/32` | 0.915652 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/33` | 0.873652 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/47` | 0.865652 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/84` | 0.865652 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/76` | 0.865652 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/47` | 0.865652 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/47` | 0.865652 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/37` | 0.865652 | **EQUIPMENT** |

### Query 89
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/39']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/39', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/35', 'PZO22001 Starfinder Player Core 014-029::/page/15/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/35` | 0.938833 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/39` | 0.938833 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/34` | 0.938833 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/37` | 0.896833 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/29` | 0.896833 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/84` | 0.888833 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/49` | 0.888833 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/34` | 0.888833 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/50` | 0.888833 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/42` | 0.888833 | **PLAYING THE ** **GAME** |

### Query 90
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/40']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `13`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/40', 'PZO22001 Starfinder Player Core 014-029::/page/15/Text/35', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/36']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/40` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/35` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/36` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/13` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/30` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/38` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/87` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/40` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/46` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/43` | 0.900802 | **CONDITIONS ** **APPENDIX** |

### Query 91
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `13`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/5/Text/41', 'PZO22001 Starfinder Player Core 014-029::/page/15/Text/36', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/41` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/36` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/31` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/37` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/39` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/14` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/41` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/71` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/47` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/51` | 0.879439 | **GLOSSARY & ** **INDEX** |

### Query 92
- Text: Summarize STEP 5: CHOOSE \Delta CL\DeltaSS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/6/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/6/SectionHeader/8', 'PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/9', 'PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/6/SectionHeader/8` | 1.008781 | STEP 5: CHOOSE \Delta CL\DeltaSS |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/9` | 0.703129 | STEP 5 |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/4` | 0.629580 | STEP 9: CALCULATE MODIFIERS |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/3` | 0.582445 | STEPS 1 AND 2 |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/10` | 0.580100 | 5TH LEVEL |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/4` | 0.580100 | 5TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/11` | 0.580100 | 5TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/34` | 0.580100 | 5TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/10` | 0.578297 | STEP 7: RECORD CLASS DETAILS |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/18` | 0.573768 | STEP 10: FINISHING DETAILS |

### Query 93
- Text: Summarize PLAYER CORE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/0']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/0', 'PZO22001 Starfinder Player Core 014-029::/page/7/Text/27', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/0` | 0.916335 | PLAYER CORE |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/27` | 0.711777 | PLAYING THE GAME |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/29` | 0.677590 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/39` | 0.635590 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/34` | 0.635590 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/37` | 0.635590 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/35` | 0.635590 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/63` | 0.630643 | **GAME** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/50` | 0.627590 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/51` | 0.627590 | **PLAYING THE ** **GAME** |

### Query 94
- Text: Summarize STEP 7: RECORD CLASS DETAILS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `29`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/10', 'PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/13', 'PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/10` | 0.991880 | STEP 7: RECORD CLASS DETAILS |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/13` | 0.732996 | STEP 7 |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/18` | 0.690719 | STEP 10: FINISHING DETAILS |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/7` | 0.610429 | CHAPTER 3: CLASSES |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11` | 0.608540 | CLASS FEATURES |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26` | 0.608540 | CLASS FEATURES |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/15` | 0.606274 | CHAPTER 7: SPELLS |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/1` | 0.602429 | CHAPTER 3: CLASSES |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/9/SectionHeader/1` | 0.602047 | LEADER'S CONFIDENCE 7TH |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/3` | 0.600169 | STEP 6: FINISH ATTRIBUTE MODIFIERS |

### Query 95
- Text: Summarize INTRODUCTION
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/16', 'PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/3', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/16` | 0.840367 | INTRODUCTION |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/3` | 0.782738 | CHAPTER 1: INTRODUCTION |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/18` | 0.781165 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/24` | 0.739165 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/28` | 0.739165 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/27` | 0.739165 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/23` | 0.739165 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/31` | 0.731165 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/29` | 0.731165 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/29` | 0.731165 | **INTRODUCTION** |

### Query 96
- Text: Summarize Leveling Up
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `17`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/18', 'PZO22001 Starfinder Player Core 014-029::/page/13/Text/4', 'PZO22001 Starfinder Player Core 014-029::/page/11/Text/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/18` | 0.856618 | Leveling Up |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/4` | 0.754362 | **Leveling Up** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/29` | 0.754362 | **Leveling Up** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/20` | 0.712362 | **Leveling Up** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/25` | 0.712362 | **Leveling Up** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/26` | 0.712362 | **Leveling Up** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/30` | 0.712362 | **Leveling Up** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/15/SectionHeader/0` | 0.705738 | LEVELING UP |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/407` | 0.664214 | Your Level |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/541` | 0.655963 | Level |

### Query 97
- Text: Summarize Exploring the Galaxy
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `30`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/19', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/31', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/19` | 0.731385 | Exploring the Galaxy |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/31` | 0.720827 | **Exploring the ** **Galaxy** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/21` | 0.720827 | **Exploring the ** **Galaxy** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/26` | 0.678826 | **Exploring the ** **Galaxy** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/5` | 0.678826 | **Exploring the ** **Galaxy** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/27` | 0.678826 | **Exploring the ** **Galaxy** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/30` | 0.678826 | **Exploring the ** **Galaxy** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/10` | 0.547721 | **Exploring the ** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/14` | 0.526679 | WHILE EXPLORING... |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/4` | 0.513613 | This introduction is designed to help you understand the  basics of Starfinder. This chapter also includes the rules for  building and leveling up a character, as well as an example  of the character |

### Query 98
- Text: Summarize Religion
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `21`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/20', 'PZO22001 Starfinder Player Core 014-029::/page/5/Text/32', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/20` | 0.725238 | Religion |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/32` | 0.604936 | **Religion** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/22` | 0.604936 | **Religion** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/31` | 0.562936 | **Religion** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/6` | 0.562936 | **Religion** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/28` | 0.562936 | **Religion** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/27` | 0.562936 | **Religion** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/12` | 0.551637 | FAITH |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/21` | 0.504423 | You're fascinated with a particular topic, such as the  religion of a small sect of worshippers, the process of  spaghettification, or the songs sung by asterays. You gain  the Additional Lore feat an |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/14` | 0.500878 | SOCIETY |

### Query 99
- Text: Summarize CLASSES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `18`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/22', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/24', 'PZO22001 Starfinder Player Core 014-029::/page/15/Text/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/22` | 0.809926 | CLASSES |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/24` | 0.713123 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/29` | 0.713123 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/8` | 0.671123 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/30` | 0.671123 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/34` | 0.671123 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/33` | 0.671123 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11` | 0.665585 | CLASS FEATURES |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26` | 0.665585 | CLASS FEATURES |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/33` | 0.663123 | **CLASSES** |

### Query 100
- Text: Summarize EQUIPMENT
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `18`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 014-029::/page/7/Text/25', 'PZO22001 Starfinder Player Core 014-029::/page/1/Text/27', 'PZO22001 Starfinder Player Core 014-029::/page/9/Text/33']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/25` | 0.840643 | EQUIPMENT |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/27` | 0.774296 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/33` | 0.774296 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/37` | 0.732296 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/32` | 0.732296 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/43` | 0.724296 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/32` | 0.724296 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/48` | 0.724296 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/59` | 0.724296 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/47` | 0.724296 | **EQUIPMENT** |

### Query 101
- Text: Summarize CHAPTER 3: CLASSES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `17`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26', 'PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/1` | 0.964499 | CHAPTER 3: CLASSES |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/7` | 0.914499 | CHAPTER 3: CLASSES |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/22` | 0.740772 | CLASSES |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11` | 0.726979 | CLASS FEATURES |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26` | 0.726979 | CLASS FEATURES |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/9` | 0.678842 | CHAPTER 4: SKILLS |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/10` | 0.677886 | STEP 7: RECORD CLASS DETAILS |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/8` | 0.669183 | READING CLASS ENTRIES |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/23` | 0.665578 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/40` | 0.665578 | **CLASSES** |

### Query 102
- Text: What is the rule about Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  character's class is perhaps the most important decision you will make for them. Groups of players  often create characters whose skills and abilities complement each other mechanically—for example,  ensuring your party includes a healer, a combat-oriented character, a stealthy character, and someone  with command over magic—so you may wish to discuss options with your group before deciding!?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `17`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/2', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/4', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` | 1.006258 | Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  char |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 0.757311 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.756213 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/6/Text/9` | 0.737091 | At this point, you need to decide your character's class. A class gives your character access to a suite of heroic abilities, determines how effectively they fight, and governs how easily they can sha |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.725309 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/15` | 0.724837 | You might want to coordinate with other players when  forming your character concept. Your characters could have  something in common already; perhaps they are travelers  from the same home world, or |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/10` | 0.712454 | from their class features; and more. Your character's class  entry also provides the information needed when they  gain levels, so it will be a vital reference throughout the  course of your campaign. |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/6/Text/10` | 0.698447 | You don't need to write down all of your character's class features yet. You simply need to know which class you want to play, which determines the attribute modifiers that will be most important for |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/7` | 0.693880 | You can find all the new abilities specific to your class,  including class feats, right in your class entry, though you  can also use class feats to take an archetype (page 174).  Your character's cl |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/5` | 0.692009 | their past, and think about how and why they adventure.  You'll want to peruse Starfinder's available ancestries,  backgrounds, and classes. The summaries on pages 27–28  might help you match your con |

### Query 103
- Text: What is the rule about The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't follow the instructions to bake  them a cake. Or perhaps you want your character to be a  bullet-spewing veteran who shrugs off bullets when she  activates her force field. Maybe they'll be a cool-headed  witchwarper whose far-off gaze seems to look past our  reality into potential timelines long lost. The choices you  make for your character within their class—such as a  mystic's choice of connection, a soldier's choice of fighting  style, or a witchwarper's anchor—bring these visions to life  within the context of the rules and the world.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/4', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/2', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 1.012161 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` | 0.770894 | Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  char |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.710053 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/6/Text/9` | 0.696003 | At this point, you need to decide your character's class. A class gives your character access to a suite of heroic abilities, determines how effectively they fight, and governs how easily they can sha |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/15` | 0.683491 | You might want to coordinate with other players when  forming your character concept. Your characters could have  something in common already; perhaps they are travelers  from the same home world, or |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.673176 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/6` | 0.671658 | Each player takes a different approach to creating a  character. Some want a character who will fit well into the  story, while others look for a combination of abilities that  complement each other m |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/12` | 0.666460 | The first section of each class describes the interests and  tendencies typical of that class, as well as information  on how others view them. This can help inspire you as  you determine your charact |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.662150 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.657799 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |

### Query 104
- Text: What is the rule about The entries on the pages that follow describe six classes  in Starfinder. Each entry contains the information you  need to play a character of that class, as well as how to  develop them from their humble beginnings at 1st level to  the dizzying heights of power at 20th level. In addition to  the class entries, you might need to reference the following  sections, which detail additional character options and  how to advance your character in level.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/5', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/10', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/5` | 1.003596 | The entries on the pages that follow describe six classes  in Starfinder. Each entry contains the information you  need to play a character of that class, as well as how to  develop them from their hu |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/4` | 0.745767 | This introduction is designed to help you understand the  basics of Starfinder. This chapter also includes the rules for  building and leveling up a character, as well as an example  of the character |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/2` | 0.741270 | While this chapter is here to teach you the basics of  Starfinder, the rest of this rulebook serves as a reference  manual during play, and it is organized to make finding  the rule you need as easy a |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/10` | 0.739679 | from their class features; and more. Your character's class  entry also provides the information needed when they  gain levels, so it will be a vital reference throughout the  course of your campaign. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.739035 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.733461 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/5` | 0.725903 | their past, and think about how and why they adventure.  You'll want to peruse Starfinder's available ancestries,  backgrounds, and classes. The summaries on pages 27–28  might help you match your con |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/3` | 0.718805 | This section provides a step-by-step guide for creating a  character using the Starfinder rules, preceded by a guide to  help you understand attribute modifiers. These modifiers are a  critical part o |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/18` | 0.715831 | This important chapter contains  the universal rules needed to play  Starfinder, including rules for the  various modes of play, the basic  actions that every character can  perform, the rules for com |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/1` | 0.699449 | Unless you're the GM, the first thing you need to do when playing Starfinder is create your character. It's  up to you to imagine your character's past experiences, personality, and view of the galaxy |

### Query 105
- Text: What is the rule about **Leveling Up **on page 29 tells you how to make your  character stronger when you get enough Experience  Points to reach a new level.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `27`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/6', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/2', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/24']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/6` | 0.934717 | **Leveling Up **on page 29 tells you how to make your  character stronger when you get enough Experience  Points to reach a new level. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 0.698703 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/5` | 0.694402 | Each time your character reaches 1,000 Experience Points,  their level increases by 1. On your character sheet, indicate  your character's new level beside the name of their class,  and deduct 1,000 X |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/6` | 0.688872 | If you're creating a higher-level character, it's a good idea  to begin with the instructions here, then turn to page 29 for  instructions on leveling up characters. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/24` | 0.673729 | At 5th level and every 5 levels thereafter, your character  boosts four different attribute modifiers. This is described  briefly in the class. For the full details on attribute  modifiers and applyin |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/1` | 0.673602 | With each terrifying beast and deadly trap bested, a character earns Experience Points (XP)  that allow them to increase in level. Each level grants greater skill, increased resiliency, and new  capab |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/9` | 0.645590 | Once you've made all your choices for your  character's new level, be sure to go over your  character sheet and adjust any values that  have changed. At a bare minimum, your  trained or higher profici |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/20` | 0.638072 | modifier, recalculate their maximum Hit  Points using their new Constitution modifier  (typically, this adds 1 Hit Point per level). If  an attribute boost increases your character's  Intelligence mod |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/6` | 0.627562 | Next, return to your character's class entry. Increase  your character's total Hit Points by the number indicated  for your class. Then, take a look at the class advancement  table and find the row fo |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.627112 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |

### Query 106
- Text: What is the rule about **Archetypes** on page 174 gives you thematic options  that allow you to further customize your character's  abilities. Though these rules are not recommended for  beginners, the archetypes in this book allow you to  gain abilities from other classes starting at 2nd level.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/7', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/17', 'PZO22001 Starfinder Player Core 098-113::/page/8/Text/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/ListItem/7` | 0.981019 | **Archetypes** on page 174 gives you thematic options  that allow you to further customize your character's  abilities. Though these rules are not recommended for  beginners, the archetypes in this bo |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.747845 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.713450 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/3` | 0.698029 | You gain more skill increases than members of other classes.  At 2nd level and every level thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you' |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/7` | 0.696396 | You can find all the new abilities specific to your class,  including class feats, right in your class entry, though you  can also use class feats to take an archetype (page 174).  Your character's cl |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.662693 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.653075 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.644129 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/Table/2` | 0.639152 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat2Envoy feat, skill feat, skill increase3Adaptive talent, genera |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.637854 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |

### Query 107
- Text: Summarize READING CLASS ENTRIES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `16`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/8', 'PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/8` | 0.889963 | READING CLASS ENTRIES |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/1` | 0.677461 | CHAPTER 3: CLASSES |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26` | 0.659752 | CLASS FEATURES |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5` | 0.651614 | READING RULES |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/22` | 0.644652 | CLASSES |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/7` | 0.627461 | CHAPTER 3: CLASSES |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11` | 0.617752 | CLASS FEATURES |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/11` | 0.591722 | PLAYING THE CLASS |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6` | 0.590970 | UNDERSTANDING ACTIONS |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/10` | 0.589756 | STEP 7: RECORD CLASS DETAILS |

### Query 108
- Text: What is the rule about Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each class provides your character  with an attribute boost to a key attribute; a number of  Hit Points they receive at each level; proficiency ranks for  various abilities, equipment, and skills; special abilities?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/9', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/10', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.998194 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/10` | 0.841455 | from their class features; and more. Your character's class  entry also provides the information needed when they  gain levels, so it will be a vital reference throughout the  course of your campaign. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` | 0.825462 | This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chos |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/6` | 0.769174 | Next, return to your character's class entry. Increase  your character's total Hit Points by the number indicated  for your class. Then, take a look at the class advancement  table and find the row fo |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.759144 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.753384 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/3` | 0.738229 | The summaries of the classes on page 28 list each  class's key attribute—the attribute modifier used to  calculate the potency of many of their class abilities.  Characters receive an attribute boost |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.735811 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.734668 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/20` | 0.728411 | modifier, recalculate their maximum Hit  Points using their new Constitution modifier  (typically, this adds 1 Hit Point per level). If  an attribute boost increases your character's  Intelligence mod |

### Query 109
- Text: What is the rule about from their class features; and more. Your character's class  entry also provides the information needed when they  gain levels, so it will be a vital reference throughout the  course of your campaign.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/10', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/9', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/10` | 0.920731 | from their class features; and more. Your character's class  entry also provides the information needed when they  gain levels, so it will be a vital reference throughout the  course of your campaign. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.778830 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.743865 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/7/ListItem/14` | 0.686391 | See the class advancement table in your class entry to learn the class features your character gains at 1st level. You have already chosen an ancestry, background, and free attribute boosts, but these |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` | 0.682947 | Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  char |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/7` | 0.681771 | You can find all the new abilities specific to your class,  including class feats, right in your class entry, though you  can also use class feats to take an archetype (page 174).  Your character's cl |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.676781 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` | 0.670397 | This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chos |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/6` | 0.663085 | Next, return to your character's class entry. Increase  your character's total Hit Points by the number indicated  for your class. Then, take a look at the class advancement  table and find the row fo |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.660972 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |

### Query 110
- Text: Summarize PLAYING THE CLASS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/1', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/69']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/11` | 0.923376 | PLAYING THE CLASS |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/27` | 0.754143 | PLAYING THE GAME |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/1` | 0.730688 | CHAPTER 3: CLASSES |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/69` | 0.711442 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/17` | 0.697674 | CHAPTER 8:  PLAYING THE  GAME |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/22` | 0.684133 | CLASSES |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/7` | 0.680688 | CHAPTER 3: CLASSES |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/87` | 0.672634 | **SPELLS** **PLAYING THE ** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/51` | 0.669442 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/19` | 0.669442 | **PLAYING THE ** **GAME** |

### Query 111
- Text: What is the rule about The first section of each class describes the interests and  tendencies typical of that class, as well as information  on how others view them. This can help inspire you as  you determine your character's actions and define their  personality, but you aren't obligated to play your character  as this section describes.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/12', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/10', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/12` | 1.007421 | The first section of each class describes the interests and  tendencies typical of that class, as well as information  on how others view them. This can help inspire you as  you determine your charact |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.723677 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.714842 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.708783 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/7/ListItem/13` | 0.705699 | The Initial Proficiencies section of your class entry indicates your character's starting proficiency ranks in a number of areas. Choose which skills your character is trained in and record those, alo |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.683244 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/6/Text/9` | 0.679068 | At this point, you need to decide your character's class. A class gives your character access to a suite of heroic abilities, determines how effectively they fight, and governs how easily they can sha |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/6/Text/10` | 0.673505 | You don't need to write down all of your character's class features yet. You simply need to know which class you want to play, which determines the attribute modifiers that will be most important for |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/10` | 0.667309 | from their class features; and more. Your character's class  entry also provides the information needed when they  gain levels, so it will be a vital reference throughout the  course of your campaign. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 0.665937 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |

### Query 112
- Text: Summarize KEY ATTRIBUTE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `15`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/4', 'PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/13` | 0.866928 | KEY ATTRIBUTE |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/4` | 0.789983 | **KEY ATTRIBUTE** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/1` | 0.654515 | **KEY TERMS** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/4` | 0.607623 | **Attributes** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/30` | 0.607015 | CHARACTER Sheet |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/1` | 0.602070 | SAMPLE CHARACTER |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11` | 0.593806 | CLASS FEATURES |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26` | 0.593806 | CLASS FEATURES |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/25` | 0.591801 | **CHARACTER SHEET** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/15` | 0.591801 | **CHARACTER SHEET** |

### Query 113
- Text: What is the rule about This is the attribute modifier that a member of your class  cares about the most. Many of your most useful and  powerful abilities are tied to this attribute in some way.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `15`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/14', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/15', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/14` | 0.953387 | This is the attribute modifier that a member of your class  cares about the most. Many of your most useful and  powerful abilities are tied to this attribute in some way. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/15` | 0.736398 | For instance, this is the attribute modifier you'll use to  determine the Difficulty Class (DC) associated with your  character's class features and feats. This is called your  class DC. If your chara |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/5` | 0.711326 | **Class: **Your character's class applies an attribute boost to their key attribute: the attribute modifier most important for  that class. |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.698985 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/4` | 0.671712 | Excellence in an attribute modifier improves the checks and statistics related to that ability, as described below. When  imagining your character, you should also decide what attribute modifiers you |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/2` | 0.664205 | One of the most important aspects of your character is their attribute modifiers. These numbers represent your  character's raw potential, and they influence nearly every other statistic on your chara |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/16` | 0.663726 | Most classes are associated with one key attribute  modifier, but some allow you to choose from two options.  For instance, if you're a witchwarper, you can choose  either Intelligence or Charisma as |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/6/Text/10` | 0.654288 | You don't need to write down all of your character's class features yet. You simply need to know which class you want to play, which determines the attribute modifiers that will be most important for |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/3` | 0.648516 | The summaries of the classes on page 28 list each  class's key attribute—the attribute modifier used to  calculate the potency of many of their class abilities.  Characters receive an attribute boost |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` | 0.643489 | Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  char |

### Query 114
- Text: What is the rule about For instance, this is the attribute modifier you'll use to  determine the Difficulty Class (DC) associated with your  character's class features and feats. This is called your  class DC. If your character is a member of a spellcasting  class, this key attribute is used to calculate spell DCs and  similar values.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `18`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/15', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/14', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/15` | 0.981421 | For instance, this is the attribute modifier you'll use to  determine the Difficulty Class (DC) associated with your  character's class features and feats. This is called your  class DC. If your chara |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/15` | 0.806924 | A class DC sets the difficulty for certain abilities granted  by your character's class. This DC equals 10 plus their  proficiency bonus for their class DC (+3 for most 1st-level  characters) plus the |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/14` | 0.741741 | This is the attribute modifier that a member of your class  cares about the most. Many of your most useful and  powerful abilities are tied to this attribute in some way. |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 0.705735 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/23` | 0.701938 | Your character's Armor Class represents how difficult they  are to hit in combat. To calculate your AC, add 10 plus your  character's Dexterity modifier (up to their armor's Dexterity  modifier cap; p |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.674684 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/10` | 0.671670 | modifiers, spell DC, and class DC all increase by at least 1. You  might need to change other values because of skill increases,  attribute boosts, or class features that either increase your  profici |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/5` | 0.663675 | **Class: **Your character's class applies an attribute boost to their key attribute: the attribute modifier most important for  that class. |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/2` | 0.663588 | One of the most important aspects of your character is their attribute modifiers. These numbers represent your  character's raw potential, and they influence nearly every other statistic on your chara |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/3` | 0.659597 | The summaries of the classes on page 28 list each  class's key attribute—the attribute modifier used to  calculate the potency of many of their class abilities.  Characters receive an attribute boost |

### Query 115
- Text: What is the rule about Most classes are associated with one key attribute  modifier, but some allow you to choose from two options.  For instance, if you're a witchwarper, you can choose  either Intelligence or Charisma as your key attribute.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/16', 'PZO22001 Starfinder Player Core 098-113::/page/12/Text/18', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/16` | 1.005925 | Most classes are associated with one key attribute  modifier, but some allow you to choose from two options.  For instance, if you're a witchwarper, you can choose  either Intelligence or Charisma as |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/18` | 0.759127 | You're an efficient multitasker, and you always have more  than one goal in mind or scheme on the go. You can maintain  twice your Charisma modifier of assets. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 0.709405 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/3` | 0.692915 | Attribute modifiers are split into two main groups: physical and mental. Strength, Dexterity, and Constitution are physical  attribute modifiers, measuring your character's physical power, agility, an |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/15` | 0.677922 | For instance, this is the attribute modifier you'll use to  determine the Difficulty Class (DC) associated with your  character's class features and feats. This is called your  class DC. If your chara |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/16` | 0.676248 | Charisma measures your character's personal magnetism  and strength of personality. A high Charisma modifier  helps you build relationships and influence the thoughts  and moods of others with social |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.670830 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/5` | 0.657181 | Prioritize Charisma. Dexterity, Intelligence, and  Constitution round out your abilities and defenses. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/36` | 0.656959 | You can maintain a number of assets equal to your Charisma  modifier. If you Size Up other assets after that, your new asset  replaces a previous one. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/6` | 0.645855 | At 1st level, your class gives you  an attribute boost to Charisma. |

### Query 116
- Text: What is the rule about Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see page 23.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `14`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/17', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/24', 'PZO22001 Starfinder Player Core 098-113::/page/6/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.975581 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/24` | 0.816608 | At 5th level and every 5 levels thereafter, your character  boosts four different attribute modifiers. This is described  briefly in the class. For the full details on attribute  modifiers and applyin |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/5` | 0.802307 | **Class: **Your character's class applies an attribute boost to their key attribute: the attribute modifier most important for  that class. |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/20` | 0.796448 | Your character's attribute modifiers each start at +0, and as  you select your ancestry, background, and class, you'll apply  attribute boosts, which increase a modifier by 1, and attribute |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/8` | 0.789522 | An attribute boost normally increases an attribute  modifier's value by 1. However, if the attribute modifier  to which you're applying an attribute boost is already +4  or higher, instead mark "parti |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/5` | 0.780411 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/3` | 0.757464 | The summaries of the classes on page 28 list each  class's key attribute—the attribute modifier used to  calculate the potency of many of their class abilities.  Characters receive an attribute boost |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/10` | 0.743389 | modifiers, spell DC, and class DC all increase by at least 1. You  might need to change other values because of skill increases,  attribute boosts, or class features that either increase your  profici |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/9` | 0.736627 | Whenever your character receives an attribute  boost, the source indicates whether it must be applied  to a specific attribute modifier, to one in a limited list,  or whether it's a "free" boost that |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/4` | 0.730796 | A character's background also affects their attribute  modifiers, though there's more flexibility in the  attribute boosts from backgrounds than in those from  classes. For descriptions of backgrounds |

### Query 117
- Text: What is the rule about HIT POINTS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `29`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/18` | 0.770602 | HIT POINTS |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7` | 0.671307 | **HIT POINTS** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` | 0.633833 | This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chos |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/11/SectionHeader/20` | 0.604157 | HERO POINTS |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/14` | 0.586604 | Increase your maximum Hit Points by the amount  listed in your class entry in Chapter 3. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/31` | 0.585244 | Your confidence is a battery that keeps your allies going.  When you use a directive that grants temporary Hit Points, |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 0.578843 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/7/ListItem/12` | 0.556539 | To determine your total starting Hit Points, add together the number of Hit Points your character gains from their ancestry (chosen in Step 3) and the number of Hit Points they gain from their class. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/32` | 0.555814 | increase the temporary Hit Points by your level. When you  use a directive that doesn't grant temporary Hit Points, you  can grant one ally affected by that directive temporary Hit  Points equal to ha |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/11` | 0.552852 | **Trigger** The target of your Get 'Em! is reduced to 0 Hit Points. **Requirements** You used Get 'Em! against a creature on your  last turn. |

### Query 118
- Text: What is the rule about This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chose their ancestry and the amount  listed in this entry, which equals your Constitution modifier  plus a fixed number. Classes that intend for characters to?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `21`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/19', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/2', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` | 1.027595 | This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chos |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 0.894327 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/7/ListItem/12` | 0.842905 | To determine your total starting Hit Points, add together the number of Hit Points your character gains from their ancestry (chosen in Step 3) and the number of Hit Points they gain from their class. |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.818417 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/6` | 0.758574 | Next, return to your character's class entry. Increase  your character's total Hit Points by the number indicated  for your class. Then, take a look at the class advancement  table and find the row fo |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/20` | 0.746167 | modifier, recalculate their maximum Hit  Points using their new Constitution modifier  (typically, this adds 1 Hit Point per level). If  an attribute boost increases your character's  Intelligence mod |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/10` | 0.728286 | from their class features; and more. Your character's class  entry also provides the information needed when they  gain levels, so it will be a vital reference throughout the  course of your campaign. |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/5` | 0.722883 | Each time your character reaches 1,000 Experience Points,  their level increases by 1. On your character sheet, indicate  your character's new level beside the name of their class,  and deduct 1,000 X |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/10` | 0.722878 | Constitution measures your character's health and stamina,  and is important for all characters, especially those who  fight in close range. Your Constitution modifier is added to  your Hit Points and |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.712493 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |

### Query 119
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `15`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/15/Text/31', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/31', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/21` | 0.913367 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/31` | 0.913367 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/31` | 0.913367 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/56` | 0.871367 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/57` | 0.863367 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/29` | 0.863367 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/28` | 0.863367 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/29` | 0.863367 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/27` | 0.863367 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/30` | 0.863367 | **INTRODUCTION** |

### Query 120
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `15`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/32', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/22', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/57']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/22` | 0.830013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/32` | 0.830013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/57` | 0.830013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/23` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/67` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/29` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/30` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/64` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/30` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/28` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 121
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `16`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/23', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/58', 'PZO22001 Starfinder Player Core 098-113::/page/15/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/23` | 0.866254 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/58` | 0.866254 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/32` | 0.866254 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/40` | 0.824254 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/50` | 0.824254 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/28` | 0.824254 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/33` | 0.824254 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/45` | 0.816254 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/29` | 0.816254 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/33` | 0.816254 | **CLASSES** |

### Query 122
- Text: Summarize **Envoy**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/24']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/15/Text/33', 'PZO22001 Starfinder Player Core 098-113::/page/7/Text/51', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/24']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/33` | 0.873711 | **Envoy** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/51` | 0.873711 | **Envoy** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/24` | 0.873711 | **Envoy** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/59` | 0.831711 | **Envoy** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/29` | 0.831711 | **Envoy** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/41` | 0.831711 | **Envoy** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/34` | 0.831711 | **Envoy** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/1` | 0.790740 | **Sample Envoy** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/31` | 0.753648 | **ENVOY** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/18` | 0.753648 | **ENVOY** |

### Query 123
- Text: Summarize **Mystic**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/25']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/11/Text/30', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/60', 'PZO22001 Starfinder Player Core 098-113::/page/7/Text/52']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/30` | 0.853583 | **Mystic** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/60` | 0.853583 | **Mystic** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/52` | 0.853583 | **Mystic** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/42` | 0.811583 | **Mystic** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/35` | 0.811583 | **Mystic** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/25` | 0.811583 | **Mystic** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/23` | 0.669011 | **Mystic** **Page 114** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.572629 | **OVERVIEW** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/51` | 0.544351 | **ENVOY** **FLOURISH** **MENTAL** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7` | 0.540946 | **HIT POINTS** |

### Query 124
- Text: Summarize **Operative **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `27`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/26', 'PZO22001 Starfinder Player Core 098-113::/page/15/Text/34', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/26` | 0.888875 | **Operative ** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/34` | 0.888875 | **Operative ** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/31` | 0.888875 | **Operative ** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/43` | 0.846875 | **Operative ** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/36` | 0.846875 | **Operative ** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/61` | 0.846875 | **Operative ** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/53` | 0.846875 | **Operative ** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.704500 | **OVERVIEW** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7` | 0.668943 | **HIT POINTS** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/38` | 0.660003 | **Soldier** |

### Query 125
- Text: Summarize **Solarian**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/27', 'PZO22001 Starfinder Player Core 098-113::/page/15/Text/35', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/27` | 0.888958 | **Solarian** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/35` | 0.888958 | **Solarian** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/32` | 0.888958 | **Solarian** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/37` | 0.846958 | **Solarian** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/44` | 0.846958 | **Solarian** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/62` | 0.846958 | **Solarian** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/54` | 0.846958 | **Solarian** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/10` | 0.714511 | **Solarian** **Page 138** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.625730 | **OVERVIEW** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/33` | 0.613248 | **Soldier** |

### Query 126
- Text: Summarize **Soldier**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/28']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `29`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/15/Text/36', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/33', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/63']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/36` | 0.857669 | **Soldier** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/33` | 0.857669 | **Soldier** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/63` | 0.857669 | **Soldier** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/55` | 0.815669 | **Soldier** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/45` | 0.815669 | **Soldier** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/38` | 0.815669 | **Soldier** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/28` | 0.815669 | **Soldier** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.621080 | **OVERVIEW** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/32` | 0.607307 | **Solarian** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/35` | 0.607307 | **Solarian** |

### Query 127
- Text: Summarize **Witchwarper**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `13`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/9/Text/46', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/64', 'PZO22001 Starfinder Player Core 098-113::/page/15/Text/37']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/46` | 0.855156 | **Witchwarper** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/64` | 0.855156 | **Witchwarper** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/37` | 0.855156 | **Witchwarper** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/40` | 0.813156 | **Witchwarper** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/34` | 0.813156 | **Witchwarper** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/29` | 0.813156 | **Witchwarper** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/56` | 0.813156 | **Witchwarper** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/39` | 0.693431 | **Witchwarper** **Page 162** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.597737 | **OVERVIEW** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/15` | 0.563351 | **SKITTERMANDER** |

### Query 128
- Text: Summarize **Archetypes**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/30']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `19`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/7/Text/57', 'PZO22001 Starfinder Player Core 098-113::/page/9/Text/47', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/65']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/57` | 0.918834 | **Archetypes** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/47` | 0.918834 | **Archetypes** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/65` | 0.918834 | **Archetypes** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/38` | 0.876834 | **Archetypes** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/30` | 0.876834 | **Archetypes** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/41` | 0.876834 | **Archetypes** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/35` | 0.759186 | **Archetypes** **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/4` | 0.675978 | **Attributes** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.664063 | **OVERVIEW** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/8` | 0.655688 | **CHARACTER SHEET ** |

### Query 129
- Text: What is the rule about **SKILLS** **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/31']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `16`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/9/Text/48', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/66', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/48` | 0.823624 | **SKILLS** **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/66` | 0.823624 | **SKILLS** **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/42` | 0.823624 | **SKILLS** **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/58` | 0.781624 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/31` | 0.781624 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/15` | 0.781624 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/83` | 0.773624 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/46` | 0.773624 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16` | 0.683811 | Skill Feats |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/55` | 0.661015 | **SKILLS** |

### Query 130
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/32']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `21`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/11/Text/37', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/67', 'PZO22001 Starfinder Player Core 098-113::/page/9/Text/49']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/37` | 0.915652 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/67` | 0.915652 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/49` | 0.915652 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/40` | 0.873652 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/32` | 0.873652 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/43` | 0.873652 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/17` | 0.873652 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/59` | 0.873652 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/27` | 0.865652 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/37` | 0.865652 | **EQUIPMENT** |

### Query 131
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/33']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `16`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/33', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/68', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/38']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/33` | 0.806592 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/68` | 0.806592 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/38` | 0.806592 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/18` | 0.764592 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/44` | 0.764592 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/60` | 0.764592 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/41` | 0.764592 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/50` | 0.764592 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/34` | 0.756592 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/85` | 0.756592 | **SPELLS** |

### Query 132
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/34']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `14`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/7/Text/61', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/69', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/69` | 0.938833 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/34` | 0.938833 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/61` | 0.938833 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/42` | 0.896833 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/39` | 0.896833 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/51` | 0.896833 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/19` | 0.896833 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/45` | 0.896833 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/49` | 0.888833 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/39` | 0.888833 | **PLAYING THE ** **GAME** |

### Query 133
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `8`
- Graph boost applied: `True`
- Graph boosted count: `19`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/15/Text/43', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/40', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/46']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/46` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/40` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/43` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/62` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/70` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/52` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/20` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/35` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/40` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/87` | 0.900802 | **CONDITIONS ** **APPENDIX** |

### Query 134
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/36']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `21`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/15/Text/44', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/41', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/71']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/41` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/71` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/44` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/36` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/47` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/53` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/51` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/51` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/36` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/31` | 0.879439 | **GLOSSARY & ** **INDEX** |

### Query 135
- Text: What is the rule about rush into battle with weapons raised gain a higher number  of Hit Points each level, while characters who cast spells or  engage in trickery gain fewer.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `35`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/1', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/2', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/1` | 0.939806 | rush into battle with weapons raised gain a higher number  of Hit Points each level, while characters who cast spells or  engage in trickery gain fewer. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 0.674123 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/9` | 0.643730 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/20` | 0.606021 | modifier, recalculate their maximum Hit  Points using their new Constitution modifier  (typically, this adds 1 Hit Point per level). If  an attribute boost increases your character's  Intelligence mod |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/428` | 0.596719 | Attribute boosts, envoy feat, skill feat, skill increase |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/448` | 0.596719 | Attribute boosts, envoy feat, skill feat, skill increase |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/21` | 0.596518 | Your character usually begins each game session with 1 Hero  Point, and you can gain additional Hero Points during sessions  by performing heroic deeds or enthusiastic gameplay. Your  character can us |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.592349 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` | 0.590789 | This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chos |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/6` | 0.589829 | Next, return to your character's class entry. Increase  your character's total Hit Points by the number indicated  for your class. Then, take a look at the class advancement  table and find the row fo |

### Query 136
- Text: What is the rule about Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining their Hit Points, see page 21.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `18`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/2', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/19', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/24']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 1.011536 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/19` | 0.882649 | This section tells you how many Hit Points your character  gains from their class at each level. To determine your  character's starting Hit Points, add together the Hit Points  they got when you chos |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/20` | 0.804155 | modifier, recalculate their maximum Hit  Points using their new Constitution modifier  (typically, this adds 1 Hit Point per level). If  an attribute boost increases your character's  Intelligence mod |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/24` | 0.752802 | At 5th level and every 5 levels thereafter, your character  boosts four different attribute modifiers. This is described  briefly in the class. For the full details on attribute  modifiers and applyin |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/10` | 0.749152 | Constitution measures your character's health and stamina,  and is important for all characters, especially those who  fight in close range. Your Constitution modifier is added to  your Hit Points and |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/10` | 0.732018 | modifiers, spell DC, and class DC all increase by at least 1. You  might need to change other values because of skill increases,  attribute boosts, or class features that either increase your  profici |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/9` | 0.718737 | Once you've made all your choices for your  character's new level, be sure to go over your  character sheet and adjust any values that  have changed. At a bare minimum, your  trained or higher profici |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/5` | 0.707997 | Each time your character reaches 1,000 Experience Points,  their level increases by 1. On your character sheet, indicate  your character's new level beside the name of their class,  and deduct 1,000 X |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.705971 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/6` | 0.702890 | Next, return to your character's class entry. Increase  your character's total Hit Points by the number indicated  for your class. Then, take a look at the class advancement  table and find the row fo |

### Query 137
- Text: Summarize INITIAL PROFICIENCIES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `16`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/3', 'PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/6', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/49']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/3` | 0.889588 | INITIAL PROFICIENCIES |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/6` | 0.889588 | INITIAL PROFICIENCIES |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/49` | 0.850526 | **INITIAL PROFICIENCIES** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/7` | 0.670260 | At 1st level, you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start  of this class. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/16` | 0.614086 | INTRODUCTION |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/3` | 0.612218 | CHAPTER 1: INTRODUCTION |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/19` | 0.604647 | **Prerequisites **Improvised Mastery |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/9` | 0.600112 | CHAPTER 4: SKILLS |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/7/ListItem/13` | 0.589273 | The Initial Proficiencies section of your class entry indicates your character's starting proficiency ranks in a number of areas. Choose which skills your character is trained in and record those, alo |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/16` | 0.585654 | 1ST LEVEL |

### Query 138
- Text: What is the rule about When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency ranks range from trained to legendary.  For instance, a character trained with a battle ribbon can  use it effectively to dispatch foes, while a character who  is legendary with the weapon might be able to spell out  their name in decorative cursive script with just a flick of  their wrist!?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/4', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/5', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 1.019972 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.818451 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 0.797653 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/7/ListItem/13` | 0.777629 | The Initial Proficiencies section of your class entry indicates your character's starting proficiency ranks in a number of areas. Choose which skills your character is trained in and record those, alo |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.770804 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` | 0.722114 | Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  char |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/6/Text/9` | 0.707671 | At this point, you need to decide your character's class. A class gives your character access to a suite of heroic abilities, determines how effectively they fight, and governs how easily they can sha |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.705368 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.700363 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/19` | 0.698125 | weapons, and other basic equipment. Your character's class  lists the types of weapons and armor with which they are  trained (or better!). Their weapons determine how much  damage they deal in combat |

### Query 139
- Text: What is the rule about Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exact number depends on your  class, and some classes specify certain additional skills  that you're trained in. If your class would make you  trained in a skill you're already trained in (typically due to  your background), you can select another skill to become  trained in.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/5', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/6', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 1.022421 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 0.872743 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/8` | 0.831259 | If something isn't listed in your character's class entry,  their proficiency rank in that statistic is untrained unless  they gain training from another source. If your character  is untrained in som |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/7/ListItem/13` | 0.823809 | The Initial Proficiencies section of your class entry indicates your character's starting proficiency ranks in a number of areas. Choose which skills your character is trained in and record those, alo |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.798253 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/50` | 0.754459 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/1` | 0.754290 | performing arts. You gain the trained proficiency rank in  Acrobatics and Performance. If you would automatically become  trained in one of those skills (from your background or class, for  example), |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.747819 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/15` | 0.743147 | A class DC sets the difficulty for certain abilities granted  by your character's class. This DC equals 10 plus their  proficiency bonus for their class DC (+3 for most 1st-level  characters) plus the |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.724976 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |

### Query 140
- Text: What is the rule about A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is trained in Perception, a saving throw,  or another statistic, they gain a proficiency bonus equal to  their level + 2, while if they have expert proficiency, they  gain a proficiency bonus equal to their level + 4. For more  about proficiency ranks, see page 24.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/6', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/5', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 1.022806 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.863143 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/10/Text/5` | 0.844377 | With most of the big decisions for your character made,  it's time to calculate the modifiers for each of the following  statistics. If your proficiency rank for a statistic is trained,  expert, maste |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/8` | 0.832664 | If something isn't listed in your character's class entry,  their proficiency rank in that statistic is untrained unless  they gain training from another source. If your character  is untrained in som |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.771435 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/9` | 0.758355 | Once you've made all your choices for your  character's new level, be sure to go over your  character sheet and adjust any values that  have changed. At a bare minimum, your  trained or higher profici |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/18` | 0.749847 | Increase all of your trained or higher proficiency  bonuses by 1 from your new level, and make other  increases to your proficiency bonuses as necessary  from skill increases or other class features. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.735175 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.733979 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/10/Text/7` | 0.727211 | Your character's Perception modifier measures how alert  they are, and is equal to their proficiency bonus in Perception  plus their Wisdom modifier. See page 396 for more. |

### Query 141
- Text: What is the rule about Spellcasting classes grant a proficiency rank for spell  attacks and DCs, which are further detailed in each class's  entry. These classes rarely use their class DC.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/7', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/5', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/7` | 0.947012 | Spellcasting classes grant a proficiency rank for spell  attacks and DCs, which are further detailed in each class's  entry. These classes rarely use their class DC. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.682750 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 0.659678 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/8` | 0.622516 | If something isn't listed in your character's class entry,  their proficiency rank in that statistic is untrained unless  they gain training from another source. If your character  is untrained in som |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/15` | 0.622010 | A class DC sets the difficulty for certain abilities granted  by your character's class. This DC equals 10 plus their  proficiency bonus for their class DC (+3 for most 1st-level  characters) plus the |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/19` | 0.619972 | Many characters can learn a few cantrips or focus spells,  but the mystic and witchwarper gain spellcasting—the  ability to cast a wide variety of spells. If your character's  class grants spells, you |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/15` | 0.614001 | For instance, this is the attribute modifier you'll use to  determine the Difficulty Class (DC) associated with your  character's class features and feats. This is called your  class DC. If your chara |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/16` | 0.601180 | This chapter starts with rules for casting spells,  determining their effects, and negating foes' spells  (called counteracting). After that, the spell lists for  each spellcasting tradition are inclu |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.593118 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/17` | 0.584779 | Add spells and spell slots if your class grants  spellcasting. See Chapter 7 for spells. |

### Query 142
- Text: What is the rule about If something isn't listed in your character's class entry,  their proficiency rank in that statistic is untrained unless  they gain training from another source. If your character  is untrained in something, you add a proficiency bonus of  +0 when attempting a check or calculating a DC related to  that statistic.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/8', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/6', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/50']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/8` | 1.006865 | If something isn't listed in your character's class entry,  their proficiency rank in that statistic is untrained unless  they gain training from another source. If your character  is untrained in som |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 0.813015 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/50` | 0.796855 | At 1st level, you gain the listed  proficiency ranks in the following  statistics. You are untrained in anything  not listed unless you gain a better  proficiency rank in some other way. |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.765375 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/10/Text/5` | 0.751141 | With most of the big decisions for your character made,  it's time to calculate the modifiers for each of the following  statistics. If your proficiency rank for a statistic is trained,  expert, maste |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/18` | 0.697961 | Increase all of your trained or higher proficiency  bonuses by 1 from your new level, and make other  increases to your proficiency bonuses as necessary  from skill increases or other class features. |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/10/Text/14` | 0.682271 | In the second box to the right of each skill on your character  sheet, there's an abbreviation to remind you of the attribute  modifier for that skill. For each skill in which your character is  train |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/15` | 0.675103 | A class DC sets the difficulty for certain abilities granted  by your character's class. This DC equals 10 plus their  proficiency bonus for their class DC (+3 for most 1st-level  characters) plus the |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/9` | 0.674959 | Once you've made all your choices for your  character's new level, be sure to go over your  character sheet and adjust any values that  have changed. At a bare minimum, your  trained or higher profici |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.674637 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |

### Query 143
- Text: Summarize ADVANCEMENT TABLE
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/9', 'PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/1', 'PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/407']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/9` | 0.928781 | ADVANCEMENT TABLE |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/1` | 0.689562 | **ENVOY ADVANCEMENT** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/407` | 0.617768 | Your Level |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/15/SectionHeader/11` | 0.608251 | **LEVELING-UP CHECKLIST** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/10` | 0.597724 | STEP 7: RECORD CLASS DETAILS |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.594632 | **OVERVIEW** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.585594 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/1` | 0.582319 | **ATTRIBUTE MODIFIER OVERVIEW** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/13/SectionHeader/37` | 0.580958 | ATTRIBUTE BOOSTS* |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/13/SectionHeader/21` | 0.580958 | ATTRIBUTE BOOSTS* |

### Query 144
- Text: What is the rule about This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the second column lists each feature  your character receives when they reach that level. The  1st-level entry includes a reminder to select your ancestry  and background.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/10', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/29', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 1.009583 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/7/ListItem/14` | 0.850243 | See the class advancement table in your class entry to learn the class features your character gains at 1st level. You have already chosen an ancestry, background, and free attribute boosts, but these |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/29` | 0.817561 | In addition to what you get from your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/26` | 0.780663 | This section serves as a reminder of the ancestry feats your  character gains at 5th, 9th, 13th, and 17th levels. Ancestry  feats are detailed in each ancestry entry in Chapter 2, which  begins on pag |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.734462 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/10` | 0.733278 | from their class features; and more. Your character's class  entry also provides the information needed when they  gain levels, so it will be a vital reference throughout the  course of your campaign. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 0.729280 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/7` | 0.712646 | You can find all the new abilities specific to your class,  including class feats, right in your class entry, though you  can also use class feats to take an archetype (page 174).  Your character's cl |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.709052 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.706631 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |

### Query 145
- Text: What is the rule about CLASS FEATURES?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26', 'PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/408']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11` | 0.842523 | CLASS FEATURES |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26` | 0.842523 | CLASS FEATURES |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/408` | 0.731246 | Class Features |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/14` | 0.597605 | Class Feats |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/22` | 0.596565 | CLASSES |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.590636 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.579609 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/1` | 0.569715 | FORMAT OF RULES |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/1` | 0.560183 | CHAPTER 3: CLASSES |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/11` | 0.555422 | PLAYING THE CLASS |

### Query 146
- Text: What is the rule about This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `27`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/12', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/19', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 0.989891 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.813950 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.812170 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.765999 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.762382 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/27` | 0.756026 | You gain these abilities as an envoy. Abilities gained at higher levels list the level at  which you gain them next to the features' names. |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.753734 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/12` | 0.752213 | As a character advances in level, they gain additional feats  to represent their growing abilities. General feats and skill  feats (which are a subset of general feats) are presented  in this chapter. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.750039 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.745589 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |

### Query 147
- Text: What is the rule about required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to choose between options. Unless the specific  ability states otherwise, such decisions can't be changed  without retraining (as explained on page 433).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/13', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/9', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.985984 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/9` | 0.740802 | Every class entry includes information about typical  members of the class, plus suggestions for roleplaying  characters of that class and playing these characters in the  game's various modes. Each c |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.727545 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/13` | 0.715066 | **Prerequisites** Any minimum attributes, feats, proficiency  ranks, and so forth you must have to select this rules  element are here. Feats also have a level prerequisite,  listed above. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.702578 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/6/Text/9` | 0.697246 | At this point, you need to decide your character's class. A class gives your character access to a suite of heroic abilities, determines how effectively they fight, and governs how easily they can sha |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.689332 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 0.681528 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.680262 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/7/ListItem/14` | 0.674325 | See the class advancement table in your class entry to learn the class features your character gains at 1st level. You have already chosen an ancestry, background, and free attribute boosts, but these |

### Query 148
- Text: What is the rule about Class Feats?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/14', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/15', 'PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/14` | 0.801346 | Class Feats |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.670952 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/11` | 0.663435 | CLASS FEATURES |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/26` | 0.621435 | CLASS FEATURES |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/408` | 0.603422 | Class Features |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/16` | 0.594429 | Select feats as indicated on your class advancement  table. For ancestry feats, see Chapter 2. For class  feats, see your class entry in Chapter 3. For general  feats and skill feats, see Chapter 5. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16` | 0.564520 | Skill Feats |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/18` | 0.545776 | General Feats |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.544780 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.540916 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |

### Query 149
- Text: What is the rule about This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, depending on the class. Specific class feats are  detailed at the end of each class entry.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/15', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/17', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 1.012567 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.889590 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.871707 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/16` | 0.745247 | Select feats as indicated on your class advancement  table. For ancestry feats, see Chapter 2. For class  feats, see your class entry in Chapter 3. For general  feats and skill feats, see Chapter 5. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.743423 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.735385 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/7` | 0.726829 | You can find all the new abilities specific to your class,  including class feats, right in your class entry, though you  can also use class feats to take an archetype (page 174).  Your character's cl |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/8` | 0.722351 | This chapter contains the rules for 8 classes. Each class  entry includes guidelines on playing the class, rules for  building and advancing a character of that class, sample  builds, and all of the c |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.716051 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/10` | 0.715954 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |

### Query 150
- Text: What is the rule about Skill Feats?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `34`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/17', 'PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/45']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16` | 0.821981 | Skill Feats |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.678628 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/45` | 0.640010 | SKILL FEATS 2ND |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/15` | 0.596669 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/66` | 0.596669 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/31` | 0.596669 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/42` | 0.596669 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/58` | 0.596669 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/48` | 0.596669 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.589124 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |

### Query 151
- Text: What is the rule about This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every two levels thereafter, most classes gain a skill feat,  though some classes may get them at different levels, like the  envoy using adaptive talent. Your character must be trained  in the corresponding skill to take a skill feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `27`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/17', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/15', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 1.025249 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.897052 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.882984 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.819495 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.793792 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/7` | 0.763787 | You can find all the new abilities specific to your class,  including class feats, right in your class entry, though you  can also use class feats to take an archetype (page 174).  Your character's cl |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/26` | 0.757329 | This section serves as a reminder of the ancestry feats your  character gains at 5th, 9th, 13th, and 17th levels. Ancestry  feats are detailed in each ancestry entry in Chapter 2, which  begins on pag |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/12` | 0.754506 | As a character advances in level, they gain additional feats  to represent their growing abilities. General feats and skill  feats (which are a subset of general feats) are presented  in this chapter. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/10` | 0.751842 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/6` | 0.742197 | This book contains many rules elements that give characters  new and interesting ways to respond to situations in the  game. All characters can use the basic actions found in  Chapter 8, but an indivi |

### Query 152
- Text: What is the rule about General Feats?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/19', 'PZO22001 Starfinder Player Core 098-113::/page/8/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/18` | 0.777418 | General Feats |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.627857 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/10` | 0.617839 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/8/SectionHeader/9` | 0.558884 | GENERAL FEATS 3RD |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/12` | 0.541150 | As a character advances in level, they gain additional feats  to represent their growing abilities. General feats and skill  feats (which are a subset of general feats) are presented  in this chapter. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/14` | 0.537871 | Class Feats |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16` | 0.534541 | Skill Feats |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/24` | 0.529966 | FEATS |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/16` | 0.527305 | Select feats as indicated on your class advancement  table. For ancestry feats, see Chapter 2. For class  feats, see your class entry in Chapter 3. For general  feats and skill feats, see Chapter 5. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.508003 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |

### Query 153
- Text: What is the rule about This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select any general feat (including skill feats) as long  as your character qualifies for it. More information can be  found in Chapter 5 (page 210).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/19', 'PZO22001 Starfinder Player Core 098-113::/page/8/Text/10', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 1.024590 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/10` | 0.903875 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.890814 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.844498 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/12` | 0.777411 | As a character advances in level, they gain additional feats  to represent their growing abilities. General feats and skill  feats (which are a subset of general feats) are presented  in this chapter. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.757721 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.749702 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/16` | 0.740108 | Select feats as indicated on your class advancement  table. For ancestry feats, see Chapter 2. For class  feats, see your class entry in Chapter 3. For general  feats and skill feats, see Chapter 5. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/12` | 0.739927 | This section presents all the abilities the class grants  your character. An ability gained at a higher level lists the |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/7` | 0.737660 | You can find all the new abilities specific to your class,  including class feats, right in your class entry, though you  can also use class feats to take an archetype (page 174).  Your character's cl |

### Query 154
- Text: What is the rule about Skill Increases?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `35`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/20', 'PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/448', 'PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/428']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/20` | 0.818806 | Skill Increases |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/448` | 0.686882 | Attribute boosts, envoy feat, skill feat, skill increase |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/428` | 0.686882 | Attribute boosts, envoy feat, skill feat, skill increase |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/8/SectionHeader/1` | 0.643859 | SKILL INCREASES 2ND |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/436` | 0.641556 | Envoy feat, skill feat, skill increase |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/440` | 0.641556 | Envoy feat, skill feat, skill increase |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/432` | 0.641556 | Envoy feat, skill feat, skill increase |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/420` | 0.641556 | Envoy feat, skill feat, skill increase |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/416` | 0.641556 | Envoy feat, skill feat, skill increase |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/424` | 0.641556 | Envoy feat, skill feat, skill increase |

### Query 155
- Text: What is the rule about This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though envoys gain them earlier and more often.  Your character can use a skill increase to either become  trained in one skill in which they're untrained, or to become  an expert in one skill in which they're already trained.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `30`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/21', 'PZO22001 Starfinder Player Core 098-113::/page/8/Text/3', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 1.019262 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/3` | 0.851951 | You gain more skill increases than members of other classes.  At 2nd level and every level thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you' |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.850856 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/19` | 0.769537 | This section specifies the levels at which your character  gains general feats. Most classes grant a general feat at 3rd  level and every 4 levels thereafter. At each of these levels,  you can select |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/22` | 0.765402 | If your character is at least 7th level, they can use a  skill increase to become a master of a skill in which they're  already an expert. If they're at least 15th level, they can use  an increase to |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/8` | 0.764852 | As your envoy level increases, so does your ability to adapt  to new situations. At 9th level and 15th level, increase the  number of skill feats you gain this way by 1. You can use  feats that you te |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/10` | 0.749605 | The rules for using skills are presented in this chapter,  and they detail what a character can do with a given  skill, based on that character's proficiency rank. Ancestry,  background, and class can |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 0.748025 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/15` | 0.744211 | This section specifies the levels at which your character  gains class feats—special feats that only members of that  class can access. Class feats are granted beginning at 1st or  2nd level, dependin |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.741063 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |

### Query 156
- Text: What is the rule about If your character is at least 7th level, they can use a  skill increase to become a master of a skill in which they're  already an expert. If they're at least 15th level, they can use  an increase to become legendary in a skill in which they're  already a master.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `31`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/22', 'PZO22001 Starfinder Player Core 098-113::/page/8/Text/4', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/22` | 0.985581 | If your character is at least 7th level, they can use a  skill increase to become a master of a skill in which they're  already an expert. If they're at least 15th level, they can use  an increase to |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/4` | 0.932140 | At 7th level, you can use skill increases to become a master  in a skill in which you're already an expert, and at 15th level,  you can use them to become legendary in a skill in which  you're already |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/21` | 0.750150 | This section specifies the levels at which your character  can increase their proficiency rank in a skill. At 3rd level  and every 2 levels thereafter, most classes grant a skill  increase, though env |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/3` | 0.714129 | You gain more skill increases than members of other classes.  At 2nd level and every level thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you' |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/9` | 0.663454 | You've learned how to inflict greater injuries with the  weapons you know best. You deal 2 additional damage with  weapons and unarmed attacks in which you're an expert.  This damage increases to 3 da |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/27` | 0.646383 | Your damage from weapon specialization increases to 4 with  weapons and unarmed attacks in which you're an expert, 6 if  you're a master, and 8 if you're legendary. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/4` | 0.644949 | When you choose your character's class, they gain a set of  initial proficiencies. Proficiencies measure your character's  ability to perform tasks, use abilities, and succeed at  checks. Proficiency |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.641303 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/8` | 0.639180 | As your envoy level increases, so does your ability to adapt  to new situations. At 9th level and 15th level, increase the  number of skill feats you gain this way by 1. You can use  feats that you te |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/18` | 0.633210 | Increase all of your trained or higher proficiency  bonuses by 1 from your new level, and make other  increases to your proficiency bonuses as necessary  from skill increases or other class features. |

### Query 157
- Text: Summarize Attribute Boosts
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `14`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/23', 'PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/3', 'PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/448']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/23` | 0.919436 | Attribute Boosts |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/7` | 0.817029 | **Attribute Boosts** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/3` | 0.766808 | ATTRIBUTE BOOSTS |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/448` | 0.754471 | Attribute boosts, envoy feat, skill feat, skill increase |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/6` | 0.716808 | ATTRIBUTE BOOSTS |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/428` | 0.712471 | Attribute boosts, envoy feat, skill feat, skill increase |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/13/SectionHeader/21` | 0.691190 | ATTRIBUTE BOOSTS* |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/13/SectionHeader/37` | 0.691190 | ATTRIBUTE BOOSTS* |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/13/SectionHeader/49` | 0.691190 | ATTRIBUTE BOOSTS* |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/14/Footnote/3` | 0.668229 | **A character receives an attribute boost to their class's key attribute. |

### Query 158
- Text: What is the rule about At 5th level and every 5 levels thereafter, your character  boosts four different attribute modifiers. This is described  briefly in the class. For the full details on attribute  modifiers and applying them during character creation,  see page 23.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `15`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/24', 'PZO22001 Starfinder Player Core 098-113::/page/6/Text/5', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/24` | 1.001096 | At 5th level and every 5 levels thereafter, your character  boosts four different attribute modifiers. This is described  briefly in the class. For the full details on attribute  modifiers and applyin |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/5` | 0.882472 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.835022 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/20` | 0.767880 | Your character's attribute modifiers each start at +0, and as  you select your ancestry, background, and class, you'll apply  attribute boosts, which increase a modifier by 1, and attribute |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/8` | 0.766048 | An attribute boost normally increases an attribute  modifier's value by 1. However, if the attribute modifier  to which you're applying an attribute boost is already +4  or higher, instead mark "parti |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/6` | 0.747544 | Next, return to your character's class entry. Increase  your character's total Hit Points by the number indicated  for your class. Then, take a look at the class advancement  table and find the row fo |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/20` | 0.744319 | modifier, recalculate their maximum Hit  Points using their new Constitution modifier  (typically, this adds 1 Hit Point per level). If  an attribute boost increases your character's  Intelligence mod |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/2` | 0.744302 | Each attribute modifier starts at +0, representing the average. As you make character choices, you'll adjust these  modifiers by applying attribute boosts, which increase an attribute modifier, and at |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/6` | 0.736952 | **Four Free Boosts:** After the other steps, you apply four more attribute boosts to attributes of your choice to finalize  your starting attribute modifiers. |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/19` | 0.736921 | At this point, you need to start building your character's  attribute modifiers. See the overview of attribute modifiers  on page 23 for more information about these important  aspects of your charact |

### Query 159
- Text: What is the rule about Ancestry Feats?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `14`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/25', 'PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/442', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/25` | 0.745871 | Ancestry Feats |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/442` | 0.638075 | Ancestry feat, greater resolve, incredible senses, inscrutable, skill increase |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/26` | 0.613400 | This section serves as a reminder of the ancestry feats your  character gains at 5th, 9th, 13th, and 17th levels. Ancestry  feats are detailed in each ancestry entry in Chapter 2, which  begins on pag |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/434` | 0.568058 | Ancestry feat, light armor expertise, skill increase, tactician, weapon mastery |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/16` | 0.566875 | Select feats as indicated on your class advancement  table. For ancestry feats, see Chapter 2. For class  feats, see your class entry in Chapter 3. For general  feats and skill feats, see Chapter 5. |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/7` | 0.543714 | Regardless of the game mechanic they convey, rules  elements are always presented in the form of a stat block,  a summary of the rules necessary to bring the monster,  character, item, or other rules |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/3` | 0.543073 | **Ancestry:** Each ancestry provides attribute boosts, and sometimes an attribute flaw. If you're taking any voluntary  flaws, apply them in this step (see the sidebar on page 25). |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/6` | 0.540965 | The rules for ancestries and heritages representing the  Pact Worlds are in this chapter, including their ancestry  feat options. Backgrounds are at the end of this chapter,  along with a section abou |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/20` | 0.539447 | You'll have four decisions to make when you choosing your  character's ancestry. |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/7` | 0.537385 | You can find all the new abilities specific to your class,  including class feats, right in your class entry, though you  can also use class feats to take an archetype (page 174).  Your character's cl |

### Query 160
- Text: What is the rule about This section serves as a reminder of the ancestry feats your  character gains at 5th, 9th, 13th, and 17th levels. Ancestry  feats are detailed in each ancestry entry in Chapter 2, which  begins on page 40.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/2/Text/26', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/17', 'PZO22001 Starfinder Player Core 098-113::/page/8/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/26` | 0.998602 | This section serves as a reminder of the ancestry feats your  character gains at 5th, 9th, 13th, and 17th levels. Ancestry  feats are detailed in each ancestry entry in Chapter 2, which  begins on pag |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/17` | 0.784867 | This section specifies the levels at which your character gains  feats with the skill trait, called skill feats. Skill feats can be  found in Chapter 5, beginning on page 210. At 2nd level and  every |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/14` | 0.779715 | In addition to the initial ancestry feat you started with, you  gain an ancestry feat at 5th level and every 4 levels thereafter. |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/16` | 0.731060 | Select feats as indicated on your class advancement  table. For ancestry feats, see Chapter 2. For class  feats, see your class entry in Chapter 3. For general  feats and skill feats, see Chapter 5. |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/7` | 0.724684 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a pahtra, you choose from among the  following an |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/6/Text/2` | 0.715162 | your character's ancestry provides them with special abilities, write them in the appropriate spaces, such as darkvision in the Senses section on the first page and innate spells on the fourth page. W |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.713971 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/7` | 0.713872 | You can find all the new abilities specific to your class,  including class feats, right in your class entry, though you  can also use class feats to take an archetype (page 174).  Your character's cl |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/7` | 0.704240 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a lashunta, you choose from among  the following |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/11` | 0.703529 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a shirren, you choose from among the  following a |

### Query 161
- Text: Summarize **Envoy** **Page 102**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/3', 'PZO22001 Starfinder Player Core 098-113::/page/15/Text/33', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/3` | 0.935922 | **Envoy** **Page 102** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/33` | 0.782928 | **Envoy** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/29` | 0.782928 | **Envoy** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/59` | 0.740928 | **Envoy** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/41` | 0.740928 | **Envoy** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/34` | 0.740928 | **Envoy** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/51` | 0.740928 | **Envoy** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/24` | 0.740928 | **Envoy** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/1` | 0.718557 | **Sample Envoy** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/9` | 0.655068 | **ENVOY** |

### Query 162
- Text: What is the rule about The envoy is a plucky leader who supports their  allies with battlefield directives, social savviness, and  a suite of skills. Envoys call out directives to their  allies, granting powerful boons that improve if the  envoy performs an action to lead by example. Envoys  are full of sassy quips and always have useful tricks  up their sleeves. Play the envoy if you want to be a  smooth talker with a plethora of skills who helps your  allies win battles and acts as the "face" of the party.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `48`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/4', 'PZO22001 Starfinder Player Core 098-113::/page/6/Text/9', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/4` | 0.983578 | The envoy is a plucky leader who supports their  allies with battlefield directives, social savviness, and  a suite of skills. Envoys call out directives to their  allies, granting powerful boons that |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/9` | 0.822997 | Envoys encourage their allies with directives. A directive is  an order that benefits allies who follow it. Envoy directives  include a way for the envoy to lead by example by spending  more actions f |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/11` | 0.744046 | You issue directives to your allies, granting benefits and letting you take the lead.  Your words and deeds bolster your allies or harry your foes, and your cunning can  get you and your team out of d |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/10` | 0.662931 | You begin with one envoy directive. You can learn more  directives through the envoy class, envoy class feats, and your  leadership style. You can issue one directive a round. Unless  otherwise stated |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/20` | 0.658640 | You urge your allies to hustle into the fight or to get out of  the way. Until the beginning of your next turn, you and your  allies within 100 feet who can sense you gain a +5-foot status  bonus to S |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/24` | 0.650824 | You alert your allies to look for enemies and hidden things in a  stressful situation, coordinating their efforts so they can do so  more efficiently. Until the beginning of your next turn, you and  y |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/3` | 0.637441 | **Directive**: Actions with this trait are special orders  that provide benefits for your allies if they follow  them. Your allies must be able to sense you to benefit  from your directives. This acti |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/410` | 0.630264 | Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/2` | 0.629531 | You're a master influencer. You make your way in the universe with a charming smile, quick wit, and keen  sense of self-preservation. You're a leader who motivates your teammates, pushes them past the |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/19` | 0.628927 | You're most comfortable leading your allies from the front lines  of battle while you fight alongside them. You might raise a  shield to help weather the storm of incoming gunfire or simply  lead with |

### Query 163
- Text: Summarize **Navasi**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `17`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/6', 'PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/31', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/6` | 0.858894 | **Navasi** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/31` | 0.624164 | **Obozaya** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/7` | 0.622998 | **Navasi**, the human envoy, is a former space  pirate with a heart of gold. She's got a witty  remark for every occasion and a bullet for  anyone who would hurt one of her friends. |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.609215 | **OVERVIEW** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/70` | 0.575899 | **Kasatha** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/71` | 0.575899 | **Kasatha** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/33` | 0.575899 | **Kasatha** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/34` | 0.575899 | **Kasatha** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/34` | 0.575899 | **Kasatha** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7` | 0.571887 | **HIT POINTS** |

### Query 164
- Text: What is the rule about **Navasi**, the human envoy, is a former space  pirate with a heart of gold. She's got a witty  remark for every occasion and a bullet for  anyone who would hurt one of her friends.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `40`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/7', 'PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/6', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/7` | 0.952835 | **Navasi**, the human envoy, is a former space  pirate with a heart of gold. She's got a witty  remark for every occasion and a bullet for  anyone who would hurt one of her friends. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/6` | 0.531372 | **Navasi** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/31` | 0.529895 | Your confidence is a battery that keeps your allies going.  When you use a directive that grants temporary Hit Points, |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/4` | 0.490621 | The envoy is a plucky leader who supports their  allies with battlefield directives, social savviness, and  a suite of skills. Envoys call out directives to their  allies, granting powerful boons that |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/444` | 0.487146 | Envoy feat, skill feat, skill increase |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/424` | 0.487146 | Envoy feat, skill feat, skill increase |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/432` | 0.487146 | Envoy feat, skill feat, skill increase |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/436` | 0.487146 | Envoy feat, skill feat, skill increase |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/440` | 0.487146 | Envoy feat, skill feat, skill increase |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/420` | 0.487146 | Envoy feat, skill feat, skill increase |

### Query 165
- Text: Summarize **Solarian** **Page 138**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/10', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/32', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/27']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/10` | 0.956564 | **Solarian** **Page 138** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/32` | 0.777839 | **Solarian** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/27` | 0.777839 | **Solarian** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/37` | 0.735839 | **Solarian** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/35` | 0.735839 | **Solarian** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/44` | 0.735839 | **Solarian** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/54` | 0.735839 | **Solarian** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/62` | 0.735839 | **Solarian** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/23` | 0.614061 | **Mystic** **Page 114** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/3` | 0.592197 | **Envoy** **Page 102** |

### Query 166
- Text: What is the rule about The solarian is a warrior who channels the  cosmic cycle. Every solarian creates weapons of pure  stellar energy that they can manifest at will. Cycling  between graviton and photon attunement, a solarian's  abilities gain different effects based on their current  state, allowing them to execute incredible combination  attacks. Play the solarian if you want to dash into  close combat and cycle your attacks between powerful  control and damage abilities.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/11', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/29', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/11` | 0.987171 | The solarian is a warrior who channels the  cosmic cycle. Every solarian creates weapons of pure  stellar energy that they can manifest at will. Cycling  between graviton and photon attunement, a sola |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/29` | 0.646688 | The soldier is a weapons expert with a mountain  of Hit Points who isn't afraid to get between their allies  and danger. They unleash suppressing attacks with  area weapons that pin foes. They designa |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 0.620169 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/24` | 0.575331 | The mystic is a spellcaster with a connection  to a divine, occult, or primal aspect of the universe. A  mystic casts powerful spells, learning new epiphanies  based on their chosen connection, and he |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/7` | 0.574759 | Characters and their adversaries affect the galaxy of  Starfinder by using actions and producing effects. This is  especially the case during encounters, when every action  counts. When you use an act |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/35` | 0.569650 | The operative brings precision and tactical  training to any situation. In battle, they use the Aim  action to reduce enemy cover and deal extra precision  damage. Some operatives are snipers shooting |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/4` | 0.561511 | The envoy is a plucky leader who supports their  allies with battlefield directives, social savviness, and  a suite of skills. Envoys call out directives to their  allies, granting powerful boons that |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/28` | 0.552829 | You control the flow of information, playing a critical role  during a battle or while planning your next mission. You might  give commands through a comm unit or datapad or using  telepathic communic |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/12/Text/10` | 0.552642 | Jessica writes "solarian" on the class line of her character  sheet and fills in the number 1 in the level box. The solarian  class grants an attribute boost to its key attribute, which is  Strength, |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/41` | 0.544813 | You deftly step out of the way of an attack, letting the  blow continue to the creature next to you. You redirect  the attack to a creature of your choice that's adjacent to  you and within range or r |

### Query 167
- Text: Summarize **Dae**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/13', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7', 'PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/13` | 0.846247 | **Dae** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7` | 0.631754 | **HIT POINTS** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.618091 | **OVERVIEW** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/10` | 0.607141 | **Feats** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/35` | 0.554848 | **Solarian** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/62` | 0.554848 | **Solarian** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/27` | 0.554848 | **Solarian** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/44` | 0.554848 | **Solarian** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/32` | 0.554848 | **Solarian** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/54` | 0.554848 | **Solarian** |

### Query 168
- Text: Summarize The pahtra solarian **Dae** loves showing off  by combining their flashy dance moves with  solar flares or turning their battle ribbon into  a electrotether or a whip of solar fire.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `11`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/14', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/11', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/38']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/14` | 1.031551 | The pahtra solarian **Dae** loves showing off  by combining their flashy dance moves with  solar flares or turning their battle ribbon into  a electrotether or a whip of solar fire. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/11` | 0.622848 | The solarian is a warrior who channels the  cosmic cycle. Every solarian creates weapons of pure  stellar energy that they can manifest at will. Cycling  between graviton and photon attunement, a sola |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/38` | 0.563353 | The android operative **Iseph** has modified their  body into a perfect weapon, and their gun is an  extension of their hard-earned power and grace. |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/20` | 0.552357 | Many pahtras cling fiercely to their ancestral Pulonian  traditions in an effort to keep their cultures alive after  enduring generations of oppression by the Veskarium.  Pulonian culture values perso |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/9` | 0.548716 | Pahtras evolved on a low-gravity jungle world called Pulonis,  where they fought a long war for independence from their  Veskarium conquerors. Recently, pahtra freedom fighters  defeated the last Vesk |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/33` | 0.543423 | Pahtras are competitive and  graceful, valuing competition,  music, and their own freedom.  Page 62. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/4` | 0.540002 | **ShimmeringDazzle**[one-action] (mental, visual) **Frequency** once per hour;  **Effect** Your chitin flares and shimmers in a hypnotic display of  shifting color and soothing motion. Pick a creature |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/4/Text/2` | 0.537593 | Pahtras are a humanoid feline species from a nearby star system. They're highly competitive and known for their achievements in magic, music, and war. Their home world was recently freed from the Vesk |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/10` | 0.535361 | If you want to play a character who fights for freedom with  grace and style, you should play a pahtra. |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/12/Text/16` | 0.529321 | Moving on to class features, Jessica makes note of her  solar manifestations. She chooses a halberd as her solar  weapon and writes its graviton and solar forms in the  Melee Strikes area, noting its |

### Query 169
- Text: What is the rule about **SKILLS** **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/15']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `16`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/9/Text/48', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/66', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/48` | 0.823624 | **SKILLS** **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/66` | 0.823624 | **SKILLS** **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/42` | 0.823624 | **SKILLS** **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/58` | 0.781624 | **SKILLS** **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/31` | 0.781624 | **SKILLS** **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/15` | 0.781624 | **SKILLS** **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/83` | 0.773624 | **SKILLS** **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/46` | 0.773624 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/16` | 0.683811 | Skill Feats |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/55` | 0.661015 | **SKILLS** |

### Query 170
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/17']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `21`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/11/Text/37', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/67', 'PZO22001 Starfinder Player Core 098-113::/page/9/Text/49']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/37` | 0.915652 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/67` | 0.915652 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/49` | 0.915652 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/40` | 0.873652 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/32` | 0.873652 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/43` | 0.873652 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/17` | 0.873652 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/59` | 0.873652 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/27` | 0.865652 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/37` | 0.865652 | **EQUIPMENT** |

### Query 171
- Text: What is the rule about **INTRODUCTION** **ANCESTRIES & ** **BACKGROUNDS** **CLASSES** **Envoy** **Mystic** **Operative ** **Solarian** **Soldier** **Witchwarper** **Archetypes**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/46']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/46', 'PZO22001 Starfinder Player Core 098-113::/page/9/Text/39', 'PZO22001 Starfinder Player Core 098-113::/page/7/Text/49']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/46` | 0.845792 | **INTRODUCTION** **ANCESTRIES & ** **BACKGROUNDS** **CLASSES** **Envoy** **Mystic** **Operative ** **Solarian** **Soldier** **Witchwarper** **Archetypes** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/39` | 0.658254 | **INTRODUCTION** **ANCESTRIES & ** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/49` | 0.658254 | **INTRODUCTION** **ANCESTRIES & ** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/27` | 0.616254 | **INTRODUCTION** **ANCESTRIES & ** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/22` | 0.611189 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/32` | 0.611189 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/57` | 0.611189 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/31` | 0.603189 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/30` | 0.603189 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/29` | 0.603189 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 172
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/18']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `16`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/1/Text/33', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/68', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/38']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/33` | 0.806592 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/68` | 0.806592 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/38` | 0.806592 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/18` | 0.764592 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/44` | 0.764592 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/60` | 0.764592 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/41` | 0.764592 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/50` | 0.764592 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/34` | 0.756592 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/85` | 0.756592 | **SPELLS** |

### Query 173
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/19']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `14`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/7/Text/61', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/69', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/69` | 0.938833 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/34` | 0.938833 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/61` | 0.938833 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/42` | 0.896833 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/39` | 0.896833 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/51` | 0.896833 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/19` | 0.896833 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/45` | 0.896833 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/49` | 0.888833 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/39` | 0.888833 | **PLAYING THE ** **GAME** |

### Query 174
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/20']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `19`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/15/Text/43', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/40', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/46']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/46` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/40` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/43` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/62` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/70` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/52` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/20` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/35` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/40` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/87` | 0.900802 | **CONDITIONS ** **APPENDIX** |

### Query 175
- Text: Summarize **GLOSSARY & **
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/21', 'PZO22001 Starfinder Player Core 098-113::/page/7/Text/63', 'PZO22001 Starfinder Player Core 098-113::/page/15/Text/44']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/21` | 0.879706 | **GLOSSARY & ** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/63` | 0.879706 | **GLOSSARY & ** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/44` | 0.824245 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/71` | 0.782245 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/53` | 0.782245 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/47` | 0.782245 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/41` | 0.782245 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/36` | 0.782245 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/52` | 0.774245 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/51` | 0.774245 | **GLOSSARY & ** **INDEX** |

### Query 176
- Text: Summarize **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/47']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `14`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/7/Text/64', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/47', 'PZO22001 Starfinder Player Core 098-113::/page/15/Text/44']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/64` | 0.902583 | **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/47` | 0.902583 | **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/44` | 0.808971 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/71` | 0.766971 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/41` | 0.766971 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/53` | 0.766971 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/47` | 0.766971 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/36` | 0.766971 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/41` | 0.758971 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/51` | 0.758971 | **GLOSSARY & ** **INDEX** |

### Query 177
- Text: What is the rule about **CHARACTER ** **SHEET**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/22']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `14`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/22', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/48', 'PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/48` | 0.834532 | **CHARACTER ** **SHEET** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/22` | 0.834532 | **CHARACTER ** **SHEET** |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/15` | 0.784532 | **CHARACTER ** **SHEET** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/52` | 0.784532 | **CHARACTER ** **SHEET** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/25` | 0.751052 | **CHARACTER SHEET** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/16` | 0.751052 | **CHARACTER SHEET** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/15` | 0.751052 | **CHARACTER SHEET** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/21` | 0.751052 | **CHARACTER SHEET** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/15` | 0.751052 | **CHARACTER SHEET** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/8` | 0.748438 | **CHARACTER SHEET ** |

### Query 178
- Text: Summarize **Mystic** **Page 114**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `21`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/23', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/30', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/60']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/23` | 0.929954 | **Mystic** **Page 114** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/60` | 0.761412 | **Mystic** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/30` | 0.761412 | **Mystic** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/42` | 0.719412 | **Mystic** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/25` | 0.719412 | **Mystic** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/35` | 0.719412 | **Mystic** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/52` | 0.719412 | **Mystic** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/28` | 0.590895 | **PSYCHIC MASTERY** **FEAT 9** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/32` | 0.589786 | **PSYCHIC MASTER** **FEAT 9** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/10` | 0.581485 | **Solarian** **Page 138** |

### Query 179
- Text: What is the rule about The mystic is a spellcaster with a connection  to a divine, occult, or primal aspect of the universe. A  mystic casts powerful spells, learning new epiphanies  based on their chosen connection, and heals allies  using a vitality network that acts as a floating pool of  Hit Points. Play the mystic if you want to be a powerful  spellcaster who also heals your allies through your  supernatural bonds while casting powerful spells.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/24', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/4', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/24` | 0.998564 | The mystic is a spellcaster with a connection  to a divine, occult, or primal aspect of the universe. A  mystic casts powerful spells, learning new epiphanies  based on their chosen connection, and he |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 0.690125 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/2` | 0.653807 | You're a master influencer. You make your way in the universe with a charming smile, quick wit, and keen  sense of self-preservation. You're a leader who motivates your teammates, pushes them past the |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/19` | 0.603900 | Many characters can learn a few cantrips or focus spells,  but the mystic and witchwarper gain spellcasting—the  ability to cast a wide variety of spells. If your character's  class grants spells, you |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/11` | 0.596755 | The solarian is a warrior who channels the  cosmic cycle. Every solarian creates weapons of pure  stellar energy that they can manifest at will. Cycling  between graviton and photon attunement, a sola |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/4` | 0.592804 | The envoy is a plucky leader who supports their  allies with battlefield directives, social savviness, and  a suite of skills. Envoys call out directives to their  allies, granting powerful boons that |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/29` | 0.590992 | The soldier is a weapons expert with a mountain  of Hit Points who isn't afraid to get between their allies  and danger. They unleash suppressing attacks with  area weapons that pin foes. They designa |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/2` | 0.588234 | Just as your character's ancestry plays a key role in expressing their identity and worldview, their  class indicates the training they have and will improve upon as an adventurer. Choosing your  char |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/41` | 0.587276 | A witchwarper alters reality by drawing on the  infinite possibilities of other universes and timelines.  Every witchwarper is influenced by an event, and they  can harness paradoxical powers to creat |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/32` | 0.585666 | Your psychic abilities have grown stronger, allowing you to  tap into entirely new dimensions of psychic power. Choose  one common 2nd-rank spell from the occult spell list. You can  cast that spell a |

### Query 180
- Text: Summarize **Chk Chk**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `11`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/26', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/26` | 0.875291 | **Chk Chk** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7` | 0.669718 | **HIT POINTS** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/42` | 0.655870 | **CONCENTRATE** **ENVOY** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.644332 | **OVERVIEW** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/8` | 0.629384 | **CHARACTER SHEET ** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/6/SectionHeader/11` | 0.629384 | **CHARACTER SHEET ** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/6/SectionHeader/5` | 0.629384 | **CHARACTER SHEET ** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/15` | 0.627885 | **CHARACTER SHEET** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/21` | 0.627885 | **CHARACTER SHEET** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/25` | 0.627885 | **CHARACTER SHEET** |

### Query 181
- Text: Summarize The shirren mystic **Chk Chk** worships Zon-Shelyn, the god of creating art from suffering.  He enjoys creatively expressing himself by  writing poetry and dueling enemies with his painglaive.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `15`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/27', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/44', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/24']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/27` | 1.036880 | The shirren mystic **Chk Chk** worships Zon-Shelyn, the god of creating art from suffering.  He enjoys creatively expressing himself by  writing poetry and dueling enemies with his painglaive. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/19` | 0.605106 | Shirrens define themselves by their choices and bristle against  all forms of oppression. They enjoy cultural exchange, and  while most eagerly adopt the deities and practices of other  communities, o |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/44` | 0.579389 | **Zemir** the human witchwarper jumps between  realities and timelines, trusting his uncanny  luck and years of experience to keep him  anchored while searching for the loved ones he  lost years ago t |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/35` | 0.567087 | Shirrens are telepaths searching  for meaning and peace after  freeing themselves from the  Swarm hive mind. Page 66. |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/27` | 0.558238 | You have an undeniable streak of luck that you believe is a  blessing from your ancestral god Meyel. You might come from |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/15` | 0.557207 | Shirrens value individual choice and rights, having escaped  from the Swarm thanks to an adaptation to their physiology  that causes pleasure when they make choices for themselves.  Shirren culture is |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/10` | 0.555308 | If you want a character who enjoys working as part of  a team while still valuing independence, you should play a  shirren. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/8/Text/2` | 0.551797 | The insectile shirrens split from the destructive Swarm, forsaking the ruthless hive mind to pursue personal freedom and end the cycle of interstellar violence. Shirrens are a species of telepaths dev |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/24` | 0.551466 | The mystic is a spellcaster with a connection  to a divine, occult, or primal aspect of the universe. A  mystic casts powerful spells, learning new epiphanies  based on their chosen connection, and he |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/3` | 0.525776 | You descend from shirrens who were originally programmed as  decoys for the ravenous Swarm. Your chitin is iridescent and  creates shimmering patterns that fascinate and distract most  other creatures |

### Query 182
- Text: What is the rule about The soldier is a weapons expert with a mountain  of Hit Points who isn't afraid to get between their allies  and danger. They unleash suppressing attacks with  area weapons that pin foes. They designate a primary  target within their area attacks, granting them extra  shots while firing their heavy weapons. Play a soldier  if you want to control the battlefield with area-of-effect?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `41`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/29', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/35', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/29` | 0.982856 | The soldier is a weapons expert with a mountain  of Hit Points who isn't afraid to get between their allies  and danger. They unleash suppressing attacks with  area weapons that pin foes. They designa |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/35` | 0.712756 | The operative brings precision and tactical  training to any situation. In battle, they use the Aim  action to reduce enemy cover and deal extra precision  damage. Some operatives are snipers shooting |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/1` | 0.693910 | rush into battle with weapons raised gain a higher number  of Hit Points each level, while characters who cast spells or  engage in trickery gain fewer. |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/14` | 0.622535 | You single out an enemy for you and your allies to focus your  attacks on. Select an enemy within 60 feet that you can see.  You and your allies gain a +1 status bonus to attacks against  that target |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/19` | 0.606423 | You're most comfortable leading your allies from the front lines  of battle while you fight alongside them. You might raise a  shield to help weather the storm of incoming gunfire or simply  lead with |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/16` | 0.605537 | **Lead by Example** If you used two actions, you can Strike,  Area Fire, or Auto-Fire with a weapon you drew or swapped to  (including by changing active set of hands). If your Strike hits  or if a ta |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/4` | 0.605119 | The envoy is a plucky leader who supports their  allies with battlefield directives, social savviness, and  a suite of skills. Envoys call out directives to their  allies, granting powerful boons that |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/25` | 0.597129 | You've learned a few tricks with your weapons. Your  proficiency ranks for simple weapons, martial weapons, and  unarmed attacks increase to expert. Whenever you attack  the target of your Get 'Em!, y |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/11` | 0.595756 | You issue directives to your allies, granting benefits and letting you take the lead.  Your words and deeds bolster your allies or harry your foes, and your cunning can  get you and your team out of d |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/12` | 0.594401 | You seize the opening your ally has provided, quickly  attacking your foe. Make a Strike against the triggering  creature. If it's a ranged Strike, it must be in your weapon's  first range increment. |

### Query 183
- Text: What is the rule about attacks while soaking attacks from enemies.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/48']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `45`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/48', 'PZO22001 Starfinder Player Core 098-113::/page/7/Text/8', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/48` | 0.855277 | attacks while soaking attacks from enemies. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/8` | 0.619914 | **Lead by Example** If you used two actions, Hide or Sneak.  Until the start of your next turn, you can Strike the enemy  target as a reaction the first time the ally you targeted attacks  your design |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/20` | 0.606930 | You succinctly direct your allies to find cover by any means  necessary. You and all allies within 60 feet count any form of  lesser cover as standard cover until the start of your next turn. **Lead b |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/27` | 0.560861 | When you warn an ally of an attack, you follow up with a  shot at your enemy. The first time each round you use your  Watch Out reaction, you can make a melee or ranged Strike  against the triggering |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/29` | 0.558934 | **Trigger** A creature within 30 feet is damaged by an ally's Strike. You follow up on your ally's success by hurling a cunning, welltimed taunt at a foe they wounded. Attempt to Demoralize the  trigg |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/12` | 0.556296 | When the target you directed your allies to take down falls  unconscious or is destroyed, you quickly direct them at another  target. You use Get 'Em! against a new target following all the  normal ta |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/18` | 0.548817 | You follow-up your issued directive with an understood  order by attacking a notable foe. Make a Strike. If the Strike  hits, the target is affected by a 1-action Get 'Em. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/14` | 0.545124 | You single out an enemy for you and your allies to focus your  attacks on. Select an enemy within 60 feet that you can see.  You and your allies gain a +1 status bonus to attacks against  that target |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/34` | 0.543266 | **Lead by Example** If you used two actions, you Strike the  target. You and your allies gain a +1 circumstance bonus to AC  against attacks made by the target until the start of your next  turn. If t |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/25` | 0.540273 | You call on allies to get out of a threat's area or close on a threat.  Select an enemy within 60 feet. Allies within the target's reach  can Step as a reaction. Allies within 30 feet of you and not |

### Query 184
- Text: Summarize **Obozaya**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/31', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/61', 'PZO22001 Starfinder Player Core 098-113::/page/15/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/31` | 0.886660 | **Obozaya** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/34` | 0.652377 | **Operative ** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/61` | 0.652377 | **Operative ** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.649987 | **OVERVIEW** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/43` | 0.610377 | **Operative ** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/53` | 0.610377 | **Operative ** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/26` | 0.610377 | **Operative ** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/36` | 0.610377 | **Operative ** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/31` | 0.610377 | **Operative ** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/35` | 0.601209 | **Solarian** |

### Query 185
- Text: Summarize **Iseph**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `17`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/37', 'PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/10', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/37` | 0.862471 | **Iseph** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.628192 | **OVERVIEW** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/10` | 0.614904 | **Feats** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7` | 0.610987 | **HIT POINTS** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/15` | 0.573673 | **CHARACTER SHEET** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/21` | 0.573673 | **CHARACTER SHEET** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/16` | 0.573673 | **CHARACTER SHEET** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/25` | 0.573673 | **CHARACTER SHEET** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/15` | 0.573673 | **CHARACTER SHEET** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/8` | 0.569148 | **CHARACTER SHEET ** |

### Query 186
- Text: Summarize **Witchwarper** **Page 162**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `14`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/39', 'PZO22001 Starfinder Player Core 098-113::/page/15/Text/37', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/64']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/39` | 0.925372 | **Witchwarper** **Page 162** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/37` | 0.752053 | **Witchwarper** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/64` | 0.752053 | **Witchwarper** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/34` | 0.710053 | **Witchwarper** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/29` | 0.710053 | **Witchwarper** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/40` | 0.710053 | **Witchwarper** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/56` | 0.710053 | **Witchwarper** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/46` | 0.710053 | **Witchwarper** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/23` | 0.589682 | **Mystic** **Page 114** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/3` | 0.587072 | **Envoy** **Page 102** |

### Query 187
- Text: Summarize **Zemir**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/42']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `12`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/42', 'PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/1', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/42` | 0.866399 | **Zemir** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.585306 | **OVERVIEW** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/1` | 0.567443 | **KEY TERMS** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7` | 0.562187 | **HIT POINTS** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/31` | 0.525991 | **ZOOMIES **[one-action] **FEAT 9** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/20` | 0.524358 | **CONCENTRATE** **SKITTERMANDER** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/12/SectionHeader/0` | 0.520868 | **STARFINDER ** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/4/SectionHeader/0` | 0.520868 | **STARFINDER ** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/0` | 0.520868 | **STARFINDER ** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/9` | 0.516977 | **SKITTERMANDER** |

### Query 188
- Text: Summarize **Zemir** the human witchwarper jumps between  realities and timelines, trusting his uncanny  luck and years of experience to keep him  anchored while searching for the loved ones he  lost years ago to the perils of infinite worlds.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/3/Text/44', 'PZO22001 Starfinder Player Core 098-113::/page/3/Text/41', 'PZO22001 Starfinder Player Core 098-113::/page/15/Text/37']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/44` | 1.017434 | **Zemir** the human witchwarper jumps between  realities and timelines, trusting his uncanny  luck and years of experience to keep him  anchored while searching for the loved ones he  lost years ago t |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/41` | 0.685789 | A witchwarper alters reality by drawing on the  infinite possibilities of other universes and timelines.  Every witchwarper is influenced by an event, and they  can harness paradoxical powers to creat |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/37` | 0.578218 | **Witchwarper** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/3/SectionHeader/42` | 0.542370 | **Zemir** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/46` | 0.536218 | **Witchwarper** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/56` | 0.536218 | **Witchwarper** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/34` | 0.536218 | **Witchwarper** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/40` | 0.536218 | **Witchwarper** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/29` | 0.536218 | **Witchwarper** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/64` | 0.536218 | **Witchwarper** |

### Query 189
- Text: Summarize ENVOY
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `50`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/1', 'PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/43', 'PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/1` | 0.867912 | ENVOY |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/43` | 0.788983 | ENVOY FEATS |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/14` | 0.788983 | ENVOY FEATS |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/3` | 0.733760 | **ENVOY** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/31` | 0.733760 | **ENVOY** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/51` | 0.733760 | **ENVOY** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/10` | 0.733760 | **ENVOY** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/45` | 0.733760 | **ENVOY** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/25` | 0.733760 | **ENVOY** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/21` | 0.733760 | **ENVOY** |

### Query 190
- Text: Summarize **KEY ATTRIBUTE**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `16`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/4', 'PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/13', 'PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/4` | 0.906147 | **KEY ATTRIBUTE** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/13` | 0.823643 | KEY ATTRIBUTE |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/4` | 0.781964 | **Attributes** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/1` | 0.738850 | **KEY TERMS** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/21` | 0.718555 | **CHARACTER SHEET** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/15` | 0.718555 | **CHARACTER SHEET** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/16` | 0.718555 | **CHARACTER SHEET** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/15` | 0.718555 | **CHARACTER SHEET** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/25` | 0.718555 | **CHARACTER SHEET** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/6/SectionHeader/11` | 0.718388 | **CHARACTER SHEET ** |

### Query 191
- Text: Summarize **Charisma**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `9`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/5', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/11', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/5` | 0.880013 | **Charisma** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/15` | 0.830012 | **Charisma** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/8/Text/9` | 0.681920 | ATTRIBUTE FLAW Charisma |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/11` | 0.626498 | **Success** The target gains temporary Hit Points equal to their  level plus your Charisma modifier. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/42` | 0.621832 | — Constitution Charisma Wisdom |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/10` | 0.613203 | **Critical Success** The target gains temporary Hit Points equal  to double their level plus your Charisma modifier. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/7` | 0.601570 | Charisma Free |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/25` | 0.599368 | **CHARACTER SHEET** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/15` | 0.599368 | **CHARACTER SHEET** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/21` | 0.599368 | **CHARACTER SHEET** |

### Query 192
- Text: Summarize At 1st level, your class gives you  an attribute boost to Charisma.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `29`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/6', 'PZO22001 Starfinder Player Core 098-113::/page/6/Text/4', 'PZO22001 Starfinder Player Core 098-113::/page/1/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/6` | 1.008617 | At 1st level, your class gives you  an attribute boost to Charisma. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/4` | 0.808848 | In addition to what you get from your class at 1st level, you  have four free boosts to different attribute modifiers. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/17` | 0.793946 | Additionally, when you choose your character's class,  they gain an attribute boost to their key attribute modifier,  increasing that attribute modifier by 1. For more about  attribute boosts, see pag |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/7/ListItem/14` | 0.725114 | See the class advancement table in your class entry to learn the class features your character gains at 1st level. You have already chosen an ancestry, background, and free attribute boosts, but these |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.724554 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/14/Footnote/3` | 0.714695 | **A character receives an attribute boost to their class's key attribute. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/15` | 0.712238 | **Lead by Example** If you used two actions, Strike the target.  You gain a status bonus to the damage roll equal to your  Charisma modifier. Regardless of whether the Strike hits, you  and your allie |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/1` | 0.711958 | designated target. Your ally gains a status bonus to damage  equal to your Charisma modifier. |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/9/ListItem/14` | 0.708165 | ** A character receives an attribute boost to their  class's key attribute. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/29` | 0.704335 | In addition to what you get from your class at 1st level, you have the benefits of  your selected ancestry and background, as described in Chapter 2. |

### Query 193
- Text: Summarize You increase your maximum number  of HP by this number at 1st level and  every level thereafter.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/9', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/2', 'PZO22001 Starfinder Player Core 098-113::/page/2/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/9` | 0.984135 | You increase your maximum number  of HP by this number at 1st level and  every level thereafter. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/2` | 0.750500 | Each time your character gains a level, they increase  their maximum Hit Points by the amount listed in this entry.  For more about calculating your character's Constitution  modifier and determining |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/13` | 0.724770 | Increase your level by 1 and subtract 1,000 XP from  your XP total. |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/1` | 0.695109 | rush into battle with weapons raised gain a higher number  of Hit Points each level, while characters who cast spells or  engage in trickery gain fewer. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/18` | 0.685970 | Increase all of your trained or higher proficiency  bonuses by 1 from your new level, and make other  increases to your proficiency bonuses as necessary  from skill increases or other class features. |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/14` | 0.669936 | Increase your maximum Hit Points by the amount  listed in your class entry in Chapter 3. |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/20` | 0.657673 | modifier, recalculate their maximum Hit  Points using their new Constitution modifier  (typically, this adds 1 Hit Point per level). If  an attribute boost increases your character's  Intelligence mod |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/5` | 0.657317 | Each time your character reaches 1,000 Experience Points,  their level increases by 1. On your character sheet, indicate  your character's new level beside the name of their class,  and deduct 1,000 X |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/5` | 0.651089 | At 5th level and every 5 levels thereafter, you get four free  boosts to different attribute modifiers. If an attribute modifier  is already +4 or higher, it takes two boosts to increase it; you  get |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/3` | 0.650523 | You gain more skill increases than members of other classes.  At 2nd level and every level thereafter, you gain a skill  increase. You can use this increase to either become trained  in one skill you' |

### Query 194
- Text: Summarize DURING COMBAT ENCOUNTERS...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `29`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/12', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10` | 0.928570 | DURING COMBAT ENCOUNTERS... |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/12` | 0.757100 | DURING SOCIAL ENCOUNTERS... |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/14` | 0.714571 | WHILE EXPLORING... |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/16` | 0.667936 | IN DOWNTIME... |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/18` | 0.655518 | From the Front |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/48` | 0.590703 | attacks while soaking attacks from enemies. |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6` | 0.570546 | UNDERSTANDING ACTIONS |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/7` | 0.566404 | **HIT POINTS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/1/SectionHeader/18` | 0.564744 | HIT POINTS |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.558079 | **OVERVIEW** |

### Query 195
- Text: Summarize You issue directives to your allies, granting benefits and letting you take the lead.  Your words and deeds bolster your allies or harry your foes, and your cunning can  get you and your team out of danger.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `46`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/11', 'PZO22001 Starfinder Player Core 098-113::/page/6/Text/9', 'PZO22001 Starfinder Player Core 098-113::/page/13/Text/54']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/11` | 1.009160 | You issue directives to your allies, granting benefits and letting you take the lead.  Your words and deeds bolster your allies or harry your foes, and your cunning can  get you and your team out of d |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/9` | 0.807325 | Envoys encourage their allies with directives. A directive is  an order that benefits allies who follow it. Envoy directives  include a way for the envoy to lead by example by spending  more actions f |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/54` | 0.791181 | You provide a quick follow-up to your ongoing directive,  encouraging your ally when they successfully hit your |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/19` | 0.745589 | You're most comfortable leading your allies from the front lines  of battle while you fight alongside them. You might raise a  shield to help weather the storm of incoming gunfire or simply  lead with |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/48` | 0.742614 | You instinctively react to trouble by directing your allies to  act at the exact moment their intervention would matter  most. Issue a 1-action directive. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/3` | 0.739534 | **Directive**: Actions with this trait are special orders  that provide benefits for your allies if they follow  them. Your allies must be able to sense you to benefit  from your directives. This acti |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/36` | 0.737549 | You step up to lead during difficult times. You might have  experienced a traumatic event, perhaps escaping a pirate ship  during a mutiny, or you fought in some notorious battle. Your  allies trust y |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/15` | 0.725203 | People follow your lead because you help push them to  their ultimate potential. Each of your allies gain a second  reaction if they start their turn within 100 feet of you and  can perceive you. This |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/4` | 0.724301 | The envoy is a plucky leader who supports their  allies with battlefield directives, social savviness, and  a suite of skills. Envoys call out directives to their  allies, granting powerful boons that |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/18` | 0.717747 | You broadcast helpful encouragement or pertinent information  to your ally's mind. Your ally rerolls the triggering skill check and  takes the better result. |

### Query 196
- Text: Summarize DURING SOCIAL ENCOUNTERS...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `21`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/12', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/12` | 0.920528 | DURING SOCIAL ENCOUNTERS... |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10` | 0.776644 | DURING COMBAT ENCOUNTERS... |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/16` | 0.713995 | IN DOWNTIME... |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/14` | 0.655177 | WHILE EXPLORING... |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6` | 0.603139 | UNDERSTANDING ACTIONS |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/67` | 0.592260 | **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/44` | 0.592260 | **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/56` | 0.592260 | **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/22` | 0.588349 | OTHERS PROBABLY... |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/18` | 0.588182 | From the Front |

### Query 197
- Text: Summarize WHILE EXPLORING...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/14', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/14` | 0.877651 | WHILE EXPLORING... |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10` | 0.732027 | DURING COMBAT ENCOUNTERS... |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/16` | 0.719774 | IN DOWNTIME... |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/3/Text/10` | 0.685448 | **Exploring the ** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/12` | 0.663619 | DURING SOCIAL ENCOUNTERS... |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6` | 0.645861 | UNDERSTANDING ACTIONS |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/31` | 0.641346 | **Exploring the ** **Galaxy** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/21` | 0.641346 | **Exploring the ** **Galaxy** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/26` | 0.641346 | **Exploring the ** **Galaxy** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/30` | 0.641346 | **Exploring the ** **Galaxy** |

### Query 198
- Text: Summarize IN DOWNTIME...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/16', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/16` | 0.882907 | IN DOWNTIME... |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10` | 0.722223 | DURING COMBAT ENCOUNTERS... |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/14` | 0.709330 | WHILE EXPLORING... |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/12` | 0.647494 | DURING SOCIAL ENCOUNTERS... |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/69` | 0.591241 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/51` | 0.591241 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/61` | 0.591241 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/39` | 0.591241 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/45` | 0.591241 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/34` | 0.591241 | **PLAYING THE ** **GAME** |

### Query 199
- Text: Summarize You look for new opportunities to make a name for yourself, work your way up  through the ranks of an organization, or establish an enterprise of your own.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/Text/17', 'PZO22001 Starfinder Player Core 098-113::/page/5/ListItem/19', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/17` | 0.999750 | You look for new opportunities to make a name for yourself, work your way up  through the ranks of an organization, or establish an enterprise of your own. |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/ListItem/19` | 0.747027 | Aspire to lead a business or military organization, or captain a starship. |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/13` | 0.657861 | You're often the face for your team, whether you use diplomacy, lies, threats, or  whatever words it takes to get your way. |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/2` | 0.644069 | Constantly strive to improve yourself through practicing  skills and honing your powers. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/18` | 0.607016 | Whether through conversation, clever lies, dazzling  performances, or threats, you rely on charm and cunning to  influence others. You crave being in the spotlight. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/ListItem/25` | 0.605469 | Assume you like being in charge. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/ListItem/24` | 0.604544 | Ask for your help navigating complex social situations. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/36` | 0.603221 | You step up to lead during difficult times. You might have  experienced a traumatic event, perhaps escaping a pirate ship  during a mutiny, or you fought in some notorious battle. Your  allies trust y |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/5/ListItem/8` | 0.599300 | Assume you're looking for an excuse to prove yourself  in a fight. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/17` | 0.599036 | Whether it comes naturally, or you trained for it, you've  developed a personal style of leading others. At 1st level,  select a leadership style. You become trained in the indicated  leadership skill |

### Query 200
- Text: Summarize YOU MIGHT...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `18`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/22', 'PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/18` | 0.840459 | YOU MIGHT... |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/22` | 0.746164 | OTHERS PROBABLY... |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/5/SectionHeader/5` | 0.696164 | OTHERS PROBABLY... |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/13/SectionHeader/5` | 0.696164 | OTHERS PROBABLY... |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/5` | 0.696164 | OTHERS PROBABLY... |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/9/SectionHeader/5` | 0.696164 | OTHERS PROBABLY... |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/16` | 0.670362 | IN DOWNTIME... |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/14` | 0.605732 | WHILE EXPLORING... |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/12` | 0.570992 | DURING SOCIAL ENCOUNTERS... |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10` | 0.561680 | DURING COMBAT ENCOUNTERS... |

### Query 201
- Text: Lookup values for Your LevelClass Features1Ancestry and background, attribute boosts,
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/6/Table/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/6/Table/2', 'PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/418', 'PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/410']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/6/Table/2` | 0.775481 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat2Envoy feat, skill feat, skill increase3Adaptive talent, genera |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/418` | 0.720753 | Ancestry feat, attribute boosts, improvised mastery, perception expertise, skill increase, weapon expertise |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/410` | 0.720529 | Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/7/ListItem/14` | 0.701917 | See the class advancement table in your class entry to learn the class features your character gains at 1st level. You have already chosen an ancestry, background, and free attribute boosts, but these |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/20` | 0.692472 | Your character's attribute modifiers each start at +0, and as  you select your ancestry, background, and class, you'll apply  attribute boosts, which increase a modifier by 1, and attribute |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/7/ListItem/5` | 0.678672 | First, make sure you've applied all the attribute boosts and attribute flaws you've noted in previous steps (from your ancestry, background, and class). |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/15` | 0.671144 | Add class features from your class advancement  table, including attribute boosts and skill increases. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/10` | 0.666241 | This table summarizes the feats, skill increases, attribute  boosts, and other benefits your character gains as they  advance in level. The first column of the class table  indicates a level, and the |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/4` | 0.663332 | **Background:** Your character's background provides two attribute boosts. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/6` | 0.662672 | At 1st level, your class gives you  an attribute boost to Charisma. |

### Query 202
- Text: What are the requirements for **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `32`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17', 'PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.942294 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.827147 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.802087 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.753818 | **READY ARMS! **[one-action]** TO **[two-actions] |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12` | 0.742232 | **GET 'EM! **[one-action]** TO **[two-actions] |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/22` | 0.740511 | **DANCE PARTNER! **[one-action]** TO **[two-actions] |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.724834 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22` | 0.718746 | **SEARCH HIGH AND LOW! **[one-action]** TO **[two-actions] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/39` | 0.717687 | **KEEP ON KEEPING ON!** [one-action]** TO **[two-actions] |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/5` | 0.711524 | **COORDINATED AMBUSH! **[one-action]** TO **[two-actions] |

### Query 203
- Text: What are the requirements for **PARDON ME** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `11`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/21', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/30', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/600']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/21` | 0.835870 | **PARDON ME** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/30` | 0.663327 | **SIZE UP** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/600` | 0.659913 | Pardon Me |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26` | 0.634367 | **HYPER** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/18` | 0.615985 | **COMMANDING PHEROMONES** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/25` | 0.610977 | **LINGUISTIC PRODIGY** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/1` | 0.601681 | **PSYCHIC TALENT** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/29` | 0.601681 | **PSYCHIC TALENT** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/15` | 0.598966 | **DAUNTLESS** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/3` | 0.596135 | **PREDATORY** **FEAT 1** |

### Query 204
- Text: What are the requirements for **Prerequisites** trained in Deception?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `27`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/23', 'PZO22001 Starfinder Player Core 098-113::/page/12/Text/22', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/23` | 0.906005 | **Prerequisites** trained in Deception |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/22` | 0.906005 | **Prerequisites** trained in Deception |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25` | 0.864888 | **Prerequisites** trained in Deception or Diplomacy |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/5` | 0.770726 | **Prerequisites** master in Deception |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.737230 | **Prerequisites** trained in Intimidation |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/56` | 0.672073 | Trained in one of the following skills  of your choice: Deception, Diplomacy,  Intimidation |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/46` | 0.637695 | **Prerequisites** master in Intimidation |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.601268 | **Prerequisites** Psychic Mastery |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.599158 | **Prerequisites** Psychic Talent |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.599158 | **Prerequisites** Psychic Talent |

### Query 205
- Text: What are the requirements for **QUIP **[reaction] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/26', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/41', 'PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/26` | 0.875422 | **QUIP **[reaction] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.736993 | **WATCH OUT **[reaction] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/9` | 0.681831 | **COMPETITIVE SPIRIT **[reaction] **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.667854 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26` | 0.627345 | **HYPER** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/37` | 0.615820 | **SIDESTEP **[reaction] **FEAT 8** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.614209 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/9` | 0.611838 | **CHANGE OF PLANS **[reaction] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/13` | 0.594183 | **COMMUNALISM **[reaction] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/18` | 0.593984 | **COMMANDING PHEROMONES** **FEAT 1** |

### Query 206
- Text: What are the requirements for **Prerequisites** trained in Intimidation?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `27`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/28', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/46', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.945656 | **Prerequisites** trained in Intimidation |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/46` | 0.852092 | **Prerequisites** master in Intimidation |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/23` | 0.762451 | **Prerequisites** trained in Deception |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/22` | 0.720451 | **Prerequisites** trained in Deception |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25` | 0.686520 | **Prerequisites** trained in Deception or Diplomacy |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/19` | 0.636337 | **Prerequisites **Improvised Mastery |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/56` | 0.635860 | Trained in one of the following skills  of your choice: Deception, Diplomacy,  Intimidation |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/5` | 0.635013 | **Prerequisites** master in Deception |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.624486 | **Prerequisites** Psychic Mastery |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/20` | 0.601901 | **Prerequisites** trained in Medicine |

### Query 207
- Text: What are the requirements for **SIZE UP** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/30']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `10`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/30', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/7', 'PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/30` | 0.846696 | **SIZE UP** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/7` | 0.754516 | **Prerequisites** Size Up |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17` | 0.754516 | **Prerequisites** Size Up |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/612` | 0.650935 | Size Up |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26` | 0.598727 | **HYPER** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/15/SectionHeader/11` | 0.584319 | **LEVELING-UP CHECKLIST** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/29` | 0.574940 | **SKITTERMANDER LORE** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/9` | 0.571218 | **CLINGING BITE** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/21` | 0.570566 | **PARDON ME** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/22` | 0.563833 | **DISTANT TELEPATH** **FEAT 1** |

### Query 208
- Text: What are the requirements for **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `37`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37', 'PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12', 'PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.899896 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12` | 0.830188 | **GET 'EM! **[one-action]** TO **[two-actions] |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.809673 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.759306 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.744577 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.742838 | **READY ARMS! **[one-action]** TO **[two-actions] |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/39` | 0.721268 | **KEEP ON KEEPING ON!** [one-action]** TO **[two-actions] |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/9/SectionHeader/3` | 0.706300 | **STEEL YOURSELVES! **[one-action]** TO **[two-actions] |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/22` | 0.705324 | **DANCE PARTNER! **[one-action]** TO **[two-actions] |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/5` | 0.686373 | **COORDINATED AMBUSH! **[one-action]** TO **[two-actions] |

### Query 209
- Text: What are the requirements for **WATCH OUT **[reaction] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `30`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/41', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.893709 | **WATCH OUT **[reaction] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34` | 0.766357 | **Prerequisites** Watch Out |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/26` | 0.766357 | **Prerequisites** Watch Out |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/26` | 0.704244 | **QUIP **[reaction] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/9` | 0.661966 | **COMPETITIVE SPIRIT **[reaction] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.651158 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.643305 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/9` | 0.637514 | **CHANGE OF PLANS **[reaction] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/55` | 0.625326 | **Requirements** You have at least 1 Focus Point. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.624705 | **READY ARMS! **[one-action]** TO **[two-actions] |

### Query 210
- Text: Lookup values for FeatLevelAcquire Asset2Change of Plans2Cheer Up8Confounding Disquisition8Cut 'Em Deep10Dirty Retort6Distant Feint6Diverse Schemes4Don't You Die on Me2Down to the Wire14Effortless Influencer16Endlessly Adaptive20Extend Directive16Fast Synergy18Get in There!2Get Them!16Go to Ground!1Got 'Em!10Hang in There6Hurry6Improvised Legend18
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/Table/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/11/Table/3', 'PZO22001 Starfinder Player Core 098-113::/page/11/Table/16', 'PZO22001 Starfinder Player Core 098-113::/page/6/Table/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/Table/3` | 0.998262 | FeatLevelAcquire Asset2Change of Plans2Cheer Up8Confounding Disquisition8Cut 'Em Deep10Dirty Retort6Distant Feint6Diverse Schemes4Don't You Die on Me2Down to the Wire14Effortless Influencer16Endlessly |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/Table/16` | 0.896297 | FeatLevelInfluence4Look Alive8Master Plan14Not in the Face4Pardon Me1Quip1Ready to Roll14Saw it Coming4Search High and Low!2Secondary Directive12Size Up1Sidestep8Situational Awareness12Smooth Diversio |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/6/Table/2` | 0.717928 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat2Envoy feat, skill feat, skill increase3Adaptive talent, genera |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/11` | 0.658430 | Size Up (1st), Acquire Asset (2nd), Influence (4th),  Smooth Diversions (10th) |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22` | 0.643377 | **SEARCH HIGH AND LOW! **[one-action]** TO **[two-actions] **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.621560 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/10` | 0.619332 | **ACTION OR FEAT NAME **[one-action] **LEVEL** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/19` | 0.609527 | Adjust bonuses from feats and other abilities that  are based on your level. |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/13` | 0.609464 | **Prerequisites** Any minimum attributes, feats, proficiency  ranks, and so forth you must have to select this rules  element are here. Feats also have a level prerequisite,  listed above. |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/20` | 0.603446 | modifier, recalculate their maximum Hit  Points using their new Constitution modifier  (typically, this adds 1 Hit Point per level). If  an attribute boost increases your character's  Intelligence mod |

### Query 211
- Text: Lookup values for 2ND LEVEL
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/Table/4']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/584', 'PZO22001 Starfinder Player Core 098-113::/page/11/Table/4', 'PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/16']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/584` | 0.853671 | 2ND LEVEL |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/Table/4` | 0.853671 | 2ND LEVEL |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/16` | 0.686899 | 1ST LEVEL |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/8` | 0.636899 | 1ST LEVEL |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/12` | 0.636899 | 1ST LEVEL |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/8` | 0.636899 | 1ST LEVEL |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/8` | 0.636899 | 1ST LEVEL |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/40` | 0.633844 | 6TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/13` | 0.631520 | 4TH LEVEL |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/34` | 0.628997 | 5TH LEVEL |

### Query 212
- Text: What are the requirements for **ACQUIRE ASSET **[one-action] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `29`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/5', 'PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/542']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/5` | 0.893050 | **ACQUIRE ASSET **[one-action] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.722654 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/542` | 0.722035 | Acquire Asset |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.648106 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12` | 0.642745 | **GET 'EM! **[one-action]** TO **[two-actions] |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.631501 | **READY ARMS! **[one-action]** TO **[two-actions] |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.629497 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/13` | 0.628291 | **DON'T YOU DIE ON ME **[one-action] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/35` | 0.615742 | You gain the benefits of the 2-action Get 'Em! when using  1-action Get 'Em! on an asset. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.608167 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |

### Query 213
- Text: What are the requirements for **Prerequisites** Size Up?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `18`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/11/Text/7', 'PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/612']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/7` | 0.920795 | **Prerequisites** Size Up |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17` | 0.920795 | **Prerequisites** Size Up |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/612` | 0.751945 | Size Up |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/30` | 0.665186 | **SIZE UP** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/34` | 0.656206 | **Prerequisites** Hyper |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/26` | 0.645380 | **Prerequisites** Watch Out |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34` | 0.645380 | **Prerequisites** Watch Out |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/51` | 0.635428 | **Prerequisites** Zoomies |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/63` | 0.635428 | **Prerequisites** Zoomies |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/19` | 0.619443 | **Prerequisites** Long Whiskered |

### Query 214
- Text: What are the requirements for **CHANGE OF PLANS **[reaction] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `38`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/9', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/544', 'PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/9` | 0.884216 | **CHANGE OF PLANS **[reaction] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/544` | 0.706451 | Change of Plans |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.684681 | **READY ARMS! **[one-action]** TO **[two-actions] |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.637179 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.623899 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.616032 | **WATCH OUT **[reaction] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.613171 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12` | 0.596659 | **GET 'EM! **[one-action]** TO **[two-actions] |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/5` | 0.593822 | **COORDINATED AMBUSH! **[one-action]** TO **[two-actions] |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/26` | 0.590996 | **QUIP **[reaction] **FEAT 1** |

### Query 215
- Text: What are the requirements for **DON'T YOU DIE ON ME **[one-action] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `33`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/13', 'PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/558']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/13` | 0.857379 | **DON'T YOU DIE ON ME **[one-action] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.695519 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/558` | 0.686104 | Don't You Die on Me |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.642229 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/5` | 0.628211 | **ACQUIRE ASSET **[one-action] **FEAT 2** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.606501 | **READY ARMS! **[one-action]** TO **[two-actions] |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.606232 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/39` | 0.603810 | **KEEP ON KEEPING ON!** [one-action]** TO **[two-actions] |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12` | 0.593336 | **GET 'EM! **[one-action]** TO **[two-actions] |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/22` | 0.591377 | **DANCE PARTNER! **[one-action]** TO **[two-actions] |

### Query 216
- Text: Lookup values for FeatLevelInfluence4Look Alive8Master Plan14Not in the Face4Pardon Me1Quip1Ready to Roll14Saw it Coming4Search High and Low!2Secondary Directive12Size Up1Sidestep8Situational Awareness12Smooth Diversions10Tag Team10Take 'Em Alive!1That'll Show 'Em12True Leader20Unstoppable Directives12Watch Out1You Can Do It14
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/Table/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `35`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/11/Table/16', 'PZO22001 Starfinder Player Core 098-113::/page/11/Table/3', 'PZO22001 Starfinder Player Core 098-113::/page/12/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/Table/16` | 0.996057 | FeatLevelInfluence4Look Alive8Master Plan14Not in the Face4Pardon Me1Quip1Ready to Roll14Saw it Coming4Search High and Low!2Secondary Directive12Size Up1Sidestep8Situational Awareness12Smooth Diversio |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/Table/3` | 0.856785 | FeatLevelAcquire Asset2Change of Plans2Cheer Up8Confounding Disquisition8Cut 'Em Deep10Dirty Retort6Distant Feint6Diverse Schemes4Don't You Die on Me2Down to the Wire14Effortless Influencer16Endlessly |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/11` | 0.712593 | Size Up (1st), Acquire Asset (2nd), Influence (4th),  Smooth Diversions (10th) |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22` | 0.630235 | **SEARCH HIGH AND LOW! **[one-action]** TO **[two-actions] **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/Table/2` | 0.626855 | Your LevelClass Features1Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat2Envoy feat, skill feat, skill increase3Adaptive talent, genera |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/608` | 0.608504 | Search High and Low! |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.600389 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/13` | 0.594258 | 4TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/10` | 0.593476 | **ACTION OR FEAT NAME **[one-action] **LEVEL** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/407` | 0.587985 | Your Level |

### Query 217
- Text: What are the requirements for **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `40`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23', 'PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.929799 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.840917 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12` | 0.827651 | **GET 'EM! **[one-action]** TO **[two-actions] |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.781763 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.762815 | **READY ARMS! **[one-action]** TO **[two-actions] |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.744623 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/22` | 0.731287 | **DANCE PARTNER! **[one-action]** TO **[two-actions] |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/39` | 0.729798 | **KEEP ON KEEPING ON!** [one-action]** TO **[two-actions] |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/9/SectionHeader/3` | 0.729010 | **STEEL YOURSELVES! **[one-action]** TO **[two-actions] |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/5` | 0.717367 | **COORDINATED AMBUSH! **[one-action]** TO **[two-actions] |

### Query 218
- Text: What are the requirements for **SEARCH HIGH AND LOW! **[one-action]** TO **[two-actions] **FEAT 2**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `38`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22', 'PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17', 'PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22` | 0.917057 | **SEARCH HIGH AND LOW! **[one-action]** TO **[two-actions] **FEAT 2** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.761560 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.757494 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12` | 0.701809 | **GET 'EM! **[one-action]** TO **[two-actions] |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.701609 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/31` | 0.673051 | **DIGITAL ASSESSMENT! **[one-action]** TO **[two-actions] |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/22` | 0.672210 | **DANCE PARTNER! **[one-action]** TO **[two-actions] |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/5` | 0.669607 | **COORDINATED AMBUSH! **[one-action]** TO **[two-actions] |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/608` | 0.669057 | Search High and Low! |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.664888 | **READY ARMS! **[one-action]** TO **[two-actions] |

### Query 219
- Text: What are the requirements for **DIVERSE SCHEMES** **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/14', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/556', 'PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/14` | 0.856240 | **DIVERSE SCHEMES** **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/556` | 0.692472 | Diverse Schemes |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/13` | 0.668735 | 4TH LEVEL |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/6/SectionHeader/3` | 0.601818 | STEP 4: PICK A BACKGROUND |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/7` | 0.594086 | STEP 4 |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/9` | 0.577443 | CHAPTER 4: SKILLS |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/39` | 0.568483 | **MASTER PLAN** **FEAT 14** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/35` | 0.548088 | **SAW IT COMING **[free-action] **FEAT 4** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29` | 0.544393 | **INFLUENCE **[reaction] **FEAT 4** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/33` | 0.539055 | 14TH LEVEL |

### Query 220
- Text: What are the requirements for **Prerequisites** Size Up?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `18`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/11/Text/7', 'PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/612']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/7` | 0.920795 | **Prerequisites** Size Up |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17` | 0.920795 | **Prerequisites** Size Up |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/612` | 0.751945 | Size Up |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/30` | 0.665186 | **SIZE UP** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/34` | 0.656206 | **Prerequisites** Hyper |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/26` | 0.645380 | **Prerequisites** Watch Out |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34` | 0.645380 | **Prerequisites** Watch Out |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/51` | 0.635428 | **Prerequisites** Zoomies |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/63` | 0.635428 | **Prerequisites** Zoomies |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/19` | 0.619443 | **Prerequisites** Long Whiskered |

### Query 221
- Text: What are the requirements for **NOT IN THE FACE **[reaction] **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `30`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/19', 'PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/19` | 0.849952 | **NOT IN THE FACE **[reaction] **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29` | 0.689798 | **INFLUENCE **[reaction] **FEAT 4** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/34` | 0.639453 | **DOWN TO THE WIRE **[reaction] **FEAT 14** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/35` | 0.585037 | **SAW IT COMING **[free-action] **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/598` | 0.580854 | Not in the Face |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.576140 | **WATCH OUT **[reaction] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/6/SectionHeader/3` | 0.571962 | STEP 4: PICK A BACKGROUND |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/7` | 0.568482 | STEP 4 |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/37` | 0.559790 | **SIDESTEP **[reaction] **FEAT 8** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/9` | 0.559624 | **CHANGE OF PLANS **[reaction] **FEAT 2** |

### Query 222
- Text: What are the requirements for **Prerequisites** trained in Deception?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/12/Text/22']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `27`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/10/Text/23', 'PZO22001 Starfinder Player Core 098-113::/page/12/Text/22', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/23` | 0.906005 | **Prerequisites** trained in Deception |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/22` | 0.906005 | **Prerequisites** trained in Deception |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25` | 0.864888 | **Prerequisites** trained in Deception or Diplomacy |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/5` | 0.770726 | **Prerequisites** master in Deception |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.737230 | **Prerequisites** trained in Intimidation |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/56` | 0.672073 | Trained in one of the following skills  of your choice: Deception, Diplomacy,  Intimidation |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/46` | 0.637695 | **Prerequisites** master in Intimidation |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.601268 | **Prerequisites** Psychic Mastery |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.599158 | **Prerequisites** Psychic Talent |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.599158 | **Prerequisites** Psychic Talent |

### Query 223
- Text: What are the requirements for **INFLUENCE **[reaction] **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `27`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29', 'PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/19', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/58']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29` | 0.842258 | **INFLUENCE **[reaction] **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/19` | 0.689651 | **NOT IN THE FACE **[reaction] **FEAT 4** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/58` | 0.678123 | **Prerequisites** Influence |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/35` | 0.619913 | **SAW IT COMING **[free-action] **FEAT 4** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.605375 | **WATCH OUT **[reaction] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/9` | 0.594935 | **COMPETITIVE SPIRIT **[reaction] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/9` | 0.594426 | **CHANGE OF PLANS **[reaction] **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/26` | 0.590484 | **QUIP **[reaction] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/592` | 0.587826 | Influence |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/34` | 0.586409 | **DOWN TO THE WIRE **[reaction] **FEAT 14** |

### Query 224
- Text: What are the requirements for **SAW IT COMING **[free-action] **FEAT 4**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/35']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `31`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/35', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44', 'PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/35` | 0.878511 | **SAW IT COMING **[free-action] **FEAT 4** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44` | 0.689661 | **READY TO ROLL **[free-action] **FEAT 14** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.638017 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/7` | 0.591815 | STEP 4 |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/6/SectionHeader/3` | 0.587863 | STEP 4: PICK A BACKGROUND |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.576420 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/2` | 0.576368 | **HELPING HAND **[free-action] **FEAT 5** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/29` | 0.573113 | **INFLUENCE **[reaction] **FEAT 4** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49` | 0.572719 | **YOU CAN DO IT **[one-action] **FEAT 14** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/606` | 0.571880 | Saw it Coming |

### Query 225
- Text: What are the requirements for **DIRTY RETORT **[reaction] **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/41']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `32`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/41', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/14', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/552']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/41` | 0.842791 | **DIRTY RETORT **[reaction] **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/14` | 0.665341 | **HURRY **[one-action] **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/552` | 0.639771 | Dirty Retort |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/40` | 0.584950 | 6TH LEVEL |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.581793 | **WATCH OUT **[reaction] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/26` | 0.580994 | **QUIP **[reaction] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/9` | 0.579977 | **CHANGE OF PLANS **[reaction] **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/34` | 0.579192 | **DOWN TO THE WIRE **[reaction] **FEAT 14** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/2` | 0.578943 | **DISTANT FEINT** **FEAT 6** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/11` | 0.574677 | STEP 6 |

### Query 226
- Text: What are the requirements for **DISTANT FEINT** **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/2', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/554', 'PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/40']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/2` | 0.830264 | **DISTANT FEINT** **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/22` | 0.629453 | **DISTANT TELEPATH** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/19` | 0.629453 | **DISTANT TELEPATH** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/554` | 0.629133 | Distant Feint |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/40` | 0.609148 | 6TH LEVEL |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/11` | 0.561537 | STEP 6 |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/17` | 0.557305 | **Trigger** An ally within 10 feet fails a skill check requiring 3  actions or fewer. |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/13` | 0.547661 | CHAPTER 6: EQUIPMENT |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/14` | 0.546154 | **HURRY **[one-action] **FEAT 6** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/13` | 0.537828 | **SENSITIVE ANTENNAE** **FEAT 5** |

### Query 227
- Text: What are the requirements for **HANG IN THERE **[one-action] **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/5', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/14', 'PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/5` | 0.877071 | **HANG IN THERE **[one-action] **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/14` | 0.715204 | **HURRY **[one-action] **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.674473 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/578` | 0.616143 | Hang in There |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/11` | 0.601624 | STEP 6 |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.592086 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.586469 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/2` | 0.580677 | **DISTANT FEINT** **FEAT 6** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/40` | 0.563766 | 6TH LEVEL |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/12` | 0.560846 | **Failure** The target is unaffected, and you can't use Hang in  There again for 1 minute. |

### Query 228
- Text: What are the requirements for **Prerequisites** expert in Diplomacy?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/8', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25', 'PZO22001 Starfinder Player Core 098-113::/page/5/Text/56']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/8` | 0.906185 | **Prerequisites** expert in Diplomacy |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25` | 0.745807 | **Prerequisites** trained in Deception or Diplomacy |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/40` | 0.649305 | **Prerequisites** expert in Performance |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/53` | 0.624220 | **Prerequisites** expert in Occultism, focus pool |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/56` | 0.616314 | Trained in one of the following skills  of your choice: Deception, Diplomacy,  Intimidation |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/5` | 0.566686 | **Prerequisites** master in Deception |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/12` | 0.548598 | **Trigger** You roll a skill check for any of the following skills  you're legendary in: Deception, Diplomacy, Intimidation, or  your leadership skill. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/4` | 0.546526 | Your ability to adapt to various beliefs instills you with  knowledge of many cultures. You gain the trained proficiency  rank in Diplomacy and Society. If you would automatically  become trained in o |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/410` | 0.546402 | Ancestry and background, attribute boosts, initial proficiencies, envoy directives, leadership style, envoy feat |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/46` | 0.546217 | **Prerequisites** master in Intimidation |

### Query 229
- Text: What are the requirements for **HURRY **[one-action] **FEAT 6**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `30`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/14', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/5', 'PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/14` | 0.878573 | **HURRY **[one-action] **FEAT 6** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/5` | 0.703105 | **HANG IN THERE **[one-action] **FEAT 6** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.673563 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/580` | 0.617320 | Hurry |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/11` | 0.616218 | STEP 6 |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.610978 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.605489 | **READY ARMS! **[one-action]** TO **[two-actions] |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26` | 0.598706 | **HYPER** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/26` | 0.597880 | **QUIP **[reaction] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/2` | 0.596449 | **DISTANT FEINT** **FEAT 6** |

### Query 230
- Text: What are the requirements for **CHEER UP **[one-action] **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `31`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/37', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/546']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18` | 0.884673 | **CHEER UP **[one-action] **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/37` | 0.678630 | **SIDESTEP **[reaction] **FEAT 8** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/546` | 0.675812 | Cheer Up |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/21` | 0.619424 | You encourage an adjacent ally to overcome their minor  ailments by patting them on the back, providing them useful  advice, or offering some form of comfort or inspiration. The  target reduces the va |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/17` | 0.610612 | STEP 8 |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/14` | 0.606659 | **HURRY **[one-action] **FEAT 6** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.602732 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/18` | 0.597182 | **HUSH **[one-action] **FEAT 9** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.596820 | **READY ARMS! **[one-action]** TO **[two-actions] |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.594492 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |

### Query 231
- Text: What are the requirements for **Prerequisites** trained in Medicine?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/20', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/28']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/20` | 0.864930 | **Prerequisites** trained in Medicine |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25` | 0.656136 | **Prerequisites** trained in Deception or Diplomacy |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.648678 | **Prerequisites** trained in Intimidation |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/23` | 0.593025 | **Prerequisites** trained in Deception |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/22` | 0.593025 | **Prerequisites** trained in Deception |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.575916 | **Prerequisites** Psychic Mastery |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/37` | 0.567961 | **Leadership Skill **Medicine |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/5` | 0.553896 | **Prerequisites** master in Deception |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/34` | 0.553290 | **Prerequisites** Hyper |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/46` | 0.551483 | **Prerequisites** master in Intimidation |

### Query 232
- Text: What are the requirements for **CONFOUNDING DISQUISITION **[two-actions] **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `31`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/22', 'PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/5', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/548']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/22` | 0.873459 | **CONFOUNDING DISQUISITION **[two-actions] **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/5` | 0.632435 | **ACQUIRE ASSET **[one-action] **FEAT 2** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/548` | 0.632435 | Confounding Disquisition |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/17` | 0.600103 | STEP 8: BUY EQUIPMENT |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/19` | 0.589870 | **SITUATIONAL AWARENESS **[two-actions] **FEAT 12** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.587833 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.579506 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/22` | 0.576527 | **SEARCH HIGH AND LOW! **[one-action]** TO **[two-actions] **FEAT 2** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/31` | 0.576315 | **DIGITAL ASSESSMENT! **[one-action]** TO **[two-actions] |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/17` | 0.570194 | STEP 8 |

### Query 233
- Text: What are the requirements for **Prerequisites** trained in Deception or Diplomacy?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/23', 'PZO22001 Starfinder Player Core 098-113::/page/12/Text/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25` | 0.949447 | **Prerequisites** trained in Deception or Diplomacy |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/23` | 0.834922 | **Prerequisites** trained in Deception |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/22` | 0.834922 | **Prerequisites** trained in Deception |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/56` | 0.745855 | Trained in one of the following skills  of your choice: Deception, Diplomacy,  Intimidation |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/5` | 0.717953 | **Prerequisites** master in Deception |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.681755 | **Prerequisites** trained in Intimidation |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/8` | 0.667416 | **Prerequisites** expert in Diplomacy |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/12` | 0.614222 | **Trigger** You roll a skill check for any of the following skills  you're legendary in: Deception, Diplomacy, Intimidation, or  your leadership skill. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/46` | 0.599225 | **Prerequisites** master in Intimidation |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/33` | 0.599211 | **Trigger** You're about to roll a Deception, Diplomacy, or  Intimidation check, but you haven't rolled yet. |

### Query 234
- Text: What are the requirements for **LOOK ALIVE** **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/31', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/594', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/31` | 0.794439 | **LOOK ALIVE** **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/594` | 0.631105 | Look Alive |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/17` | 0.624298 | 8TH LEVEL |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/17` | 0.591501 | STEP 8 |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18` | 0.585581 | **CHEER UP **[one-action] **FEAT 8** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/17` | 0.570171 | STEP 8: BUY EQUIPMENT |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/37` | 0.557894 | **SIDESTEP **[reaction] **FEAT 8** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34` | 0.551577 | **Prerequisites** Watch Out |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/26` | 0.551577 | **Prerequisites** Watch Out |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/88` | 0.536999 | **CONDITIONS ** |

### Query 235
- Text: What are the requirements for **Prerequisites** Watch Out?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/26', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34` | 0.885660 | **Prerequisites** Watch Out |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/26` | 0.885660 | **Prerequisites** Watch Out |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/7` | 0.670396 | **Prerequisites** Size Up |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/51` | 0.628929 | **Prerequisites** Zoomies |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/63` | 0.628929 | **Prerequisites** Zoomies |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17` | 0.628396 | **Prerequisites** Size Up |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/630` | 0.624907 | Watch Out |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.601744 | **Prerequisites** trained in Intimidation |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/19` | 0.599263 | **Prerequisites** Long Whiskered |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.590341 | **WATCH OUT **[reaction] **FEAT 1** |

### Query 236
- Text: What are the requirements for **SIDESTEP **[reaction] **FEAT 8**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/37', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/37` | 0.880031 | **SIDESTEP **[reaction] **FEAT 8** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/18` | 0.681974 | **CHEER UP **[one-action] **FEAT 8** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/26` | 0.666591 | **QUIP **[reaction] **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/17` | 0.636247 | STEP 8 |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.615837 | **WATCH OUT **[reaction] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/9` | 0.599769 | **CHANGE OF PLANS **[reaction] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/31` | 0.590765 | **LOOK ALIVE** **FEAT 8** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/17` | 0.590110 | STEP 8: BUY EQUIPMENT |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/17` | 0.583974 | 8TH LEVEL |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/614` | 0.580199 | Sidestep |

### Query 237
- Text: What are the requirements for **CUT 'EM DEEP** **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/43', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/550', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/49']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/43` | 0.759269 | **CUT 'EM DEEP** **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/550` | 0.655740 | Cut 'Em Deep |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/49` | 0.631325 | **GOT 'EM **[free-action] **FEAT 10** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/42` | 0.587979 | 10TH LEVEL |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/21` | 0.571741 | STEP 10 |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/18` | 0.568412 | STEP 10: FINISHING DETAILS |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/2` | 0.543784 | **SMOOTH DIVERSIONS** **FEAT 10** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17` | 0.527902 | **Prerequisites** Size Up |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/7` | 0.527902 | **Prerequisites** Size Up |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/17` | 0.526341 | **Trigger** An ally within 10 feet fails a skill check requiring 3  actions or fewer. |

### Query 238
- Text: What are the requirements for **Prerequisites** master in Intimidation?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/46']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `27`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/46', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/28', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/46` | 0.922341 | **Prerequisites** master in Intimidation |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.836157 | **Prerequisites** trained in Intimidation |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/5` | 0.745056 | **Prerequisites** master in Deception |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.653999 | **Prerequisites** Psychic Mastery |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/19` | 0.648382 | **Prerequisites **Improvised Mastery |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/22` | 0.606648 | **Prerequisites** trained in Deception |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/23` | 0.606648 | **Prerequisites** trained in Deception |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25` | 0.599240 | **Prerequisites** trained in Deception or Diplomacy |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/56` | 0.564476 | Trained in one of the following skills  of your choice: Deception, Diplomacy,  Intimidation |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/42` | 0.562050 | **Prerequisites** Psychic Bully, Psychic Scholar, or Psychic Talent |

### Query 239
- Text: What are the requirements for **GOT 'EM **[free-action] **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/49']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `33`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/49', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/43', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/49` | 0.843367 | **GOT 'EM **[free-action] **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/43` | 0.654145 | **CUT 'EM DEEP** **FEAT 10** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44` | 0.629576 | **READY TO ROLL **[free-action] **FEAT 14** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/21` | 0.606167 | STEP 10 |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/13` | 0.591646 | **ALL HANDS ON DECK **[free-action] **FEAT 9** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.576891 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/576` | 0.575789 | Got 'Em! |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/8` | 0.572723 | **TAG TEAM **[reaction] **FEAT 10** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12` | 0.572208 | **GET 'EM! **[one-action]** TO **[two-actions] |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/42` | 0.569815 | 10TH LEVEL |

### Query 240
- Text: What are the requirements for **SMOOTH DIVERSIONS** **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `15`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/2', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/42', 'PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/2` | 0.840974 | **SMOOTH DIVERSIONS** **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/42` | 0.605659 | 10TH LEVEL |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/2` | 0.590890 | **DISTANT FEINT** **FEAT 6** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/21` | 0.590798 | STEP 10 |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/18` | 0.563292 | STEP 10: FINISHING DETAILS |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/43` | 0.557152 | **CUT 'EM DEEP** **FEAT 10** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/17` | 0.543864 | **Trigger** An ally within 10 feet fails a skill check requiring 3  actions or fewer. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/26` | 0.533852 | **MELODIC ADAPTATION** **FEAT 9** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/22` | 0.533225 | **ENDLESSLY ADAPTIVE** **FEAT 20** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/11` | 0.528880 | Size Up (1st), Acquire Asset (2nd), Influence (4th),  Smooth Diversions (10th) |

### Query 241
- Text: What are the requirements for **Prerequisites** master in Deception?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/14/Text/5', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/23', 'PZO22001 Starfinder Player Core 098-113::/page/12/Text/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/5` | 0.884995 | **Prerequisites** master in Deception |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/23` | 0.783318 | **Prerequisites** trained in Deception |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/22` | 0.783318 | **Prerequisites** trained in Deception |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25` | 0.731346 | **Prerequisites** trained in Deception or Diplomacy |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/46` | 0.718739 | **Prerequisites** master in Intimidation |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.651386 | **Prerequisites** Psychic Mastery |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.634924 | **Prerequisites** trained in Intimidation |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/19` | 0.621580 | **Prerequisites **Improvised Mastery |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/56` | 0.607784 | Trained in one of the following skills  of your choice: Deception, Diplomacy,  Intimidation |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.574510 | **Prerequisites** Psychic Talent |

### Query 242
- Text: What are the requirements for **TAG TEAM **[reaction] **FEAT 10**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `31`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/8', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/620', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/8` | 0.837314 | **TAG TEAM **[reaction] **FEAT 10** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/620` | 0.668945 | Tag Team |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.613440 | **WATCH OUT **[reaction] **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/21` | 0.590213 | STEP 10 |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/42` | 0.574517 | **OPPORTUNISTIC HUG **[reaction] **FEAT 13** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/17` | 0.571683 | **Trigger** An ally within 10 feet fails a skill check requiring 3  actions or fewer. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/49` | 0.566098 | **GOT 'EM **[free-action] **FEAT 10** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/42` | 0.565041 | 10TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/18` | 0.558596 | STEP 10: FINISHING DETAILS |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/37` | 0.557518 | **SIDESTEP **[reaction] **FEAT 8** |

### Query 243
- Text: What are the requirements for **SECONDARY DIRECTIVE **[one-action] **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `43`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/14', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/610', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/28']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/14` | 0.872509 | **SECONDARY DIRECTIVE **[one-action] **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/610` | 0.720760 | Secondary Directive |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/28` | 0.685617 | **UNSTOPPABLE DIRECTIVES** **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/19` | 0.633144 | **SITUATIONAL AWARENESS **[two-actions] **FEAT 12** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/2` | 0.618921 | **EXTEND DIRECTIVE **[free-action] **FEAT 16** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/17` | 0.617303 | **Requirements** Your last action this turn was issuing a  2-action directive. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/13` | 0.607502 | 12TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/52` | 0.603715 | **Requirements** Your last action was a 1-action directive. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.578478 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/13` | 0.574685 | **DON'T YOU DIE ON ME **[one-action] **FEAT 2** |

### Query 244
- Text: What are the requirements for **SITUATIONAL AWARENESS **[two-actions] **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `31`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/19', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/616', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/19` | 0.871144 | **SITUATIONAL AWARENESS **[two-actions] **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/616` | 0.675297 | Situational Awareness |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/14` | 0.666783 | **SECONDARY DIRECTIVE **[one-action] **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/23` | 0.605451 | **INTO POSITION! **[one-action]** TO **[two-actions] |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.597354 | **READY ARMS! **[one-action]** TO **[two-actions] |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/88` | 0.574706 | **CONDITIONS ** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/5` | 0.574280 | **COORDINATED AMBUSH! **[one-action]** TO **[two-actions] |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/31` | 0.574210 | **DIGITAL ASSESSMENT! **[one-action]** TO **[two-actions] |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.568826 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/17` | 0.564397 | **Requirements** Your last action this turn was issuing a  2-action directive. |

### Query 245
- Text: What are the requirements for **THAT'LL SHOW 'EM** **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `36`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/23', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/624', 'PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/23` | 0.826342 | **THAT'LL SHOW 'EM** **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/624` | 0.697410 | That'll Show 'Em |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/7` | 0.605004 | **GET THEM!** **FEAT 16** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/13` | 0.556416 | 12TH LEVEL |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/28` | 0.535177 | **UNSTOPPABLE DIRECTIVES** **FEAT 12** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/11` | 0.519418 | You gain the Get 'Em! envoy directive. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/625` | 0.516099 | 12 |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17` | 0.515971 | **Prerequisites** Size Up |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/7` | 0.515971 | **Prerequisites** Size Up |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/14` | 0.513216 | **SECONDARY DIRECTIVE **[one-action] **FEAT 12** |

### Query 246
- Text: What are the requirements for **Prerequisites** Watch Out?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/Text/26']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34', 'PZO22001 Starfinder Player Core 098-113::/page/14/Text/26', 'PZO22001 Starfinder Player Core 098-113::/page/11/Text/7']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34` | 0.885660 | **Prerequisites** Watch Out |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/26` | 0.885660 | **Prerequisites** Watch Out |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/7` | 0.670396 | **Prerequisites** Size Up |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/51` | 0.628929 | **Prerequisites** Zoomies |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/63` | 0.628929 | **Prerequisites** Zoomies |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17` | 0.628396 | **Prerequisites** Size Up |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/630` | 0.624907 | Watch Out |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.601744 | **Prerequisites** trained in Intimidation |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/19` | 0.599263 | **Prerequisites** Long Whiskered |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.590341 | **WATCH OUT **[reaction] **FEAT 1** |

### Query 247
- Text: What are the requirements for **UNSTOPPABLE DIRECTIVES** **FEAT 12**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `37`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/28', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/628', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/28` | 0.849657 | **UNSTOPPABLE DIRECTIVES** **FEAT 12** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/628` | 0.767984 | Unstoppable Directives |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/14` | 0.674409 | **SECONDARY DIRECTIVE **[one-action] **FEAT 12** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/8` | 0.594786 | ENVOY DIRECTIVES |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/13` | 0.575795 | 12TH LEVEL |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/2` | 0.573438 | **EXTEND DIRECTIVE **[free-action] **FEAT 16** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/47` | 0.542194 | **UNCONVENTIONAL EXPERTISE** **FEAT 13** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/19` | 0.540654 | **SITUATIONAL AWARENESS **[two-actions] **FEAT 12** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/22` | 0.538863 | **Leadership Directive **Into Position! |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/23` | 0.536535 | **DIRECTIVE** **ENVOY** |

### Query 248
- Text: What are the requirements for **DOWN TO THE WIRE **[reaction] **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `40`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/34', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44', 'PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/34` | 0.845001 | **DOWN TO THE WIRE **[reaction] **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44` | 0.683881 | **READY TO ROLL **[free-action] **FEAT 14** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.645150 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.598072 | **WATCH OUT **[reaction] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49` | 0.596143 | **YOU CAN DO IT **[one-action] **FEAT 14** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/33` | 0.589256 | 14TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.588325 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/26` | 0.573827 | **QUIP **[reaction] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/19` | 0.571365 | **NOT IN THE FACE **[reaction] **FEAT 4** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.561477 | **READY ARMS! **[one-action]** TO **[two-actions] |

### Query 249
- Text: What are the requirements for **MASTER PLAN** **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/39', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/33', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/596']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/39` | 0.819811 | **MASTER PLAN** **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/33` | 0.675368 | 14TH LEVEL |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/596` | 0.639988 | Master Plan |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44` | 0.568632 | **READY TO ROLL **[free-action] **FEAT 14** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/43` | 0.547638 | **LINGUISTIC MASTER** **FEAT 13** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/597` | 0.538719 | 14 |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/10` | 0.536436 | STEP 7: RECORD CLASS DETAILS |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/9/SectionHeader/30` | 0.533260 | REFLEX MASTERY 15TH |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49` | 0.533205 | **YOU CAN DO IT **[one-action] **FEAT 14** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/0/SectionHeader/9` | 0.529132 | CHAPTER 4: SKILLS |

### Query 250
- Text: What are the requirements for **READY TO ROLL **[free-action] **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `33`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44', 'PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/35', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44` | 0.881694 | **READY TO ROLL **[free-action] **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/35` | 0.652612 | **SAW IT COMING **[free-action] **FEAT 4** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49` | 0.632475 | **YOU CAN DO IT **[one-action] **FEAT 14** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/2` | 0.581248 | **EXTEND DIRECTIVE **[free-action] **FEAT 16** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/34` | 0.575505 | **DOWN TO THE WIRE **[reaction] **FEAT 14** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.568248 | **READY ARMS! **[one-action]** TO **[two-actions] |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/42` | 0.567916 | **SCRUPULOUS STALKER **[free-action] **FEAT 13** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/13` | 0.567111 | **ALL HANDS ON DECK **[free-action] **FEAT 9** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/39` | 0.565825 | **MASTER PLAN** **FEAT 14** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/33` | 0.559141 | 14TH LEVEL |

### Query 251
- Text: What are the requirements for **YOU CAN DO IT **[one-action] **FEAT 14**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `35`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/632']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49` | 0.883192 | **YOU CAN DO IT **[one-action] **FEAT 14** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44` | 0.680147 | **READY TO ROLL **[free-action] **FEAT 14** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/632` | 0.676229 | You Can Do It |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/11/SectionHeader/18` | 0.626839 | **GET IN THERE! **[one-action]** TO **[two-actions] **FEAT 2** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.617698 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/37` | 0.598611 | **TAKE 'EM ALIVE! **[one-action]** TO **[two-actions] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/33` | 0.591718 | 14TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/13` | 0.588382 | **READY ARMS! **[one-action]** TO **[two-actions] |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/12` | 0.587293 | **GET 'EM! **[one-action]** TO **[two-actions] |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/9` | 0.586137 | [one-action] Single Actions |

### Query 252
- Text: What are the requirements for **EFFORTLESS INFLUENCER** **FEAT 16**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/55']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/55', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/562', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/54']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/55` | 0.788609 | **EFFORTLESS INFLUENCER** **FEAT 16** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/562` | 0.654667 | Effortless Influencer |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/54` | 0.623277 | 16TH LEVEL |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/7` | 0.556484 | **GET THEM!** **FEAT 16** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/22` | 0.556284 | **ENDLESSLY ADAPTIVE** **FEAT 20** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/2` | 0.539812 | **INFLUENCER** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/48` | 0.539175 | **BOUNDLESS BRACHIATOR** **FEAT 17** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/2` | 0.534169 | **EXTEND DIRECTIVE **[free-action] **FEAT 16** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/58` | 0.524375 | **Prerequisites** Influence |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/Table/16` | 0.517355 | FeatLevelInfluence4Look Alive8Master Plan14Not in the Face4Pardon Me1Quip1Ready to Roll14Saw it Coming4Search High and Low!2Secondary Directive12Size Up1Sidestep8Situational Awareness12Smooth Diversio |

### Query 253
- Text: What are the requirements for **Prerequisites** Influence?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/14/Text/58']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/14/Text/58', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/592', 'PZO22001 Starfinder Player Core 098-113::/page/10/Text/28']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/58` | 0.874744 | **Prerequisites** Influence |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/592` | 0.701815 | Influence |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.680916 | **Prerequisites** trained in Intimidation |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/34` | 0.663218 | **Prerequisites** Hyper |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/63` | 0.640687 | **Prerequisites** Zoomies |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/51` | 0.640687 | **Prerequisites** Zoomies |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/25` | 0.633731 | **Prerequisites** adaptive talent |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34` | 0.623443 | **Prerequisites** Watch Out |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/26` | 0.623443 | **Prerequisites** Watch Out |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/40` | 0.622648 | **Prerequisites** expert in Performance |

### Query 254
- Text: What are the requirements for **EXTEND DIRECTIVE **[free-action] **FEAT 16**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `36`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/2', 'PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/566', 'PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/2` | 0.915106 | **EXTEND DIRECTIVE **[free-action] **FEAT 16** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/566` | 0.723117 | Extend Directive |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44` | 0.680054 | **READY TO ROLL **[free-action] **FEAT 14** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/14` | 0.630796 | **SECONDARY DIRECTIVE **[one-action] **FEAT 12** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/16` | 0.606777 | **IMPROVISED LEGEND **[free-action] **FEAT 18** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/28` | 0.601016 | **UNSTOPPABLE DIRECTIVES** **FEAT 12** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/7` | 0.590100 | **GET THEM!** **FEAT 16** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/55` | 0.588617 | **EFFORTLESS INFLUENCER** **FEAT 16** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/42` | 0.578573 | **SCRUPULOUS STALKER **[free-action] **FEAT 13** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/54` | 0.575765 | 16TH LEVEL |

### Query 255
- Text: Summarize LASHUNTA
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `45`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/11', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1` | 0.872961 | LASHUNTA |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/11` | 0.794306 | **LASHUNTA** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/20` | 0.794306 | **LASHUNTA** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/24` | 0.752306 | **LASHUNTA** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/30` | 0.752306 | **LASHUNTA** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/20` | 0.752306 | **LASHUNTA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/2` | 0.752306 | **LASHUNTA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/11` | 0.752306 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/7` | 0.752306 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/15` | 0.752306 | **LASHUNTA** |

### Query 256
- Text: What is the rule about Long ago, lashuntas evolved psychic abilities and a unique dimorphism that helped them survive on their home world of Castrovel. In modern times, lashuntas manipulate their own genetics at puberty, allowing each individual to develop into an enhanced scholar or warrior, though not every lashunta commits to these traditional choices.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/0/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/0/Text/2', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/9', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/2` | 0.972584 | Long ago, lashuntas evolved psychic abilities and a unique dimorphism that helped them survive on their home world of Castrovel. In modern times, lashuntas manipulate their own genetics at puberty, al |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/9` | 0.776124 | Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/13` | 0.747059 | Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Las |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/23` | 0.674542 | Around puberty, many lashuntas choose to embrace a genetic  path that determines their physiology and role in society.  Choose one of the following lashunta heritages at 1st level. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/30` | 0.639554 | Lashuntas are charming  telepaths from Castrovel who  are known for their unique  dimorphism. Page 58. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/31` | 0.637300 | You've studied the lives and achievements of other  lashuntas who have improved both their psychic powers  and their communities. You gain the trained proficiency  rank in Occultism and Society. If yo |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/10` | 0.627850 | If you want to play a character who strives for selfimprovement and has innate psychic abilities, you should play  a lashunta. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/27` | 0.607045 | You've chosen the adaptive genetics to become a korasha. You  might be stockier and more muscular than other lashuntas. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.604835 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/12` | 0.584484 | Damayas tend to be tall and graceful with delicate features and  are traditionally pushed toward artistic or intellectual pursuits  and political occupations. Korashas are shorter, more muscular,  and |

### Query 257
- Text: Summarize SIZE: MEDIUM SPEED: 25 FEET
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/0/Text/5']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `37`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/8/Text/7', 'PZO22001 Starfinder Player Core 058-073::/page/4/Text/7', 'PZO22001 Starfinder Player Core 058-073::/page/0/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/8/Text/7` | 0.978918 | SIZE: MEDIUM SPEED: 25 FEET |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/4/Text/7` | 0.978918 | SIZE: MEDIUM SPEED: 25 FEET |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/5` | 0.978918 | SIZE: MEDIUM SPEED: 25 FEET |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/12/Text/5` | 0.887601 | SIZE: SMALL SPEED: 25 FEET |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26` | 0.595999 | **HYPER** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/30` | 0.594480 | **SIZE UP** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/1` | 0.585707 | **SHIRREN LORE** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/14` | 0.578808 | **CLIMBING CLAWS** **FEAT 5** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/19` | 0.577671 | **DISTANT TELEPATH** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/22` | 0.577671 | **DISTANT TELEPATH** **FEAT 1** |

### Query 258
- Text: Summarize ATTRIBUTE BOOSTS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `6`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/6', 'PZO22001 Starfinder Player Core 058-073::/page/4/Text/8', 'PZO22001 Starfinder Player Core 058-073::/page/12/Text/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/6` | 0.899383 | ATTRIBUTE BOOSTS |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/6/SectionHeader/3` | 0.849383 | ATTRIBUTE BOOSTS |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/13/SectionHeader/37` | 0.794746 | ATTRIBUTE BOOSTS* |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/SectionHeader/21` | 0.794746 | ATTRIBUTE BOOSTS* |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/13/SectionHeader/49` | 0.794746 | ATTRIBUTE BOOSTS* |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/SectionHeader/23` | 0.724439 | Attribute Boosts |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/7` | 0.698793 | **Attribute Boosts** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/1` | 0.660281 | **ATTRIBUTE MODIFIER OVERVIEW** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/4/Text/8` | 0.651425 | ATTRIBUTE BOOSTS Charisma Dexterity Free |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/12/Text/6` | 0.651425 | ATTRIBUTE BOOSTS Charisma Dexterity Free |

### Query 259
- Text: Summarize Charisma Free
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/0/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `11`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/0/Text/7', 'PZO22001 Starfinder Player Core 058-073::/page/12/Text/6', 'PZO22001 Starfinder Player Core 058-073::/page/4/Text/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/7` | 0.887800 | Charisma Free |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/12/Text/6` | 0.706971 | ATTRIBUTE BOOSTS Charisma Dexterity Free |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/4/Text/8` | 0.706971 | ATTRIBUTE BOOSTS Charisma Dexterity Free |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/8/Text/9` | 0.631701 | ATTRIBUTE FLAW Charisma |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/38` | 0.614417 | Charisma, Free Dexterity, Charisma, Free Constitution, Wisdom, Free Dexterity, Charisma, Free |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/5` | 0.603638 | **Charisma** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/15` | 0.603638 | **Charisma** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/42` | 0.575924 | — Constitution Charisma Wisdom |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/8/Text/8` | 0.549880 | **ATTRIBUTE **BOOSTS Constitution Wisdom Free |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/562` | 0.542429 | Effortless Influencer |

### Query 260
- Text: Summarize LANGUAGES Castrovelian, Common
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `31`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/8', 'PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/10', 'PZO22001 Starfinder Player Core 058-073::/page/4/SectionHeader/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/8` | 0.978947 | LANGUAGES Castrovelian, Common |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/10` | 0.787328 | LANGUAGES Common, Shirren |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/4/SectionHeader/10` | 0.708282 | LANGUAGES Common, Pahtra, Vesk |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/72` | 0.533063 | **Languages** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/44` | 0.533063 | **Languages** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/82` | 0.533063 | **Languages** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/81` | 0.533063 | **Languages** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/44` | 0.511312 | **Backgrounds** **Languages** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/43` | 0.511312 | **Backgrounds** **Languages** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/12/Text/8` | 0.489796 | One regional language of your choice |

### Query 261
- Text: What is the rule about Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent on your home world).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/0/Text/9']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `10`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/4/Text/11', 'PZO22001 Starfinder Player Core 058-073::/page/12/Text/9', 'PZO22001 Starfinder Player Core 058-073::/page/0/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/4/Text/11` | 0.944766 | Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/12/Text/9` | 0.944766 | Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/9` | 0.944766 | Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/8/Text/11` | 0.871051 | One regional language of your choice Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have acc |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/58` | 0.626701 | Trained in a number of additional  skills equal to 6 plus your Intelligence  modifier |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/28` | 0.623693 | Learning new languages comes naturally to you. You gain two  additional languages of your choice, chosen from among the  common and uncommon languages available to you. Every time  you take the Multil |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/20` | 0.616630 | modifier, recalculate their maximum Hit  Points using their new Constitution modifier  (typically, this adds 1 Hit Point per level). If  an attribute boost increases your character's  Intelligence mod |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/2` | 0.577412 | Each attribute modifier starts at +0, representing the average. As you make character choices, you'll adjust these  modifiers by applying attribute boosts, which increase an attribute modifier, and at |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/10/Text/17` | 0.571894 | If your character has any modifiers, bonuses, or  penalties from feats or abilities that always apply,  add them into the total modifiers. For ones that  apply only in certain situations, note them ne |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/10/Text/7` | 0.571365 | Your character's Perception modifier measures how alert  they are, and is equal to their proficiency bonus in Perception  plus their Wisdom modifier. See page 396 for more. |

### Query 262
- Text: What is the rule about **TRAITS **?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `12`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/4/SectionHeader/12', 'PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/10', 'PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/10` | 0.796994 | **TRAITS ** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/4/SectionHeader/12` | 0.796994 | **TRAITS ** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/12` | 0.766427 | TRAITS |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/12` | 0.752714 | **TRAITS** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/12/SectionHeader/10` | 0.724427 | TRAITS |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/4` | 0.604765 | **Attributes** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/11` | 0.577428 | **Attribute Flaws** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/46` | 0.569479 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/83` | 0.569479 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/6/SectionHeader/11` | 0.567135 | **CHARACTER SHEET ** |

### Query 263
- Text: Summarize HUMANOID LASHUNTA
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/0/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `49`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/0/Text/11', 'PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/11` | 0.912941 | HUMANOID LASHUNTA |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1` | 0.732291 | LASHUNTA |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/26` | 0.678639 | **LASHUNTA** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/30` | 0.636639 | **LASHUNTA** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/59` | 0.636639 | **LASHUNTA** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/20` | 0.636639 | **LASHUNTA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/30` | 0.636639 | **LASHUNTA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/20` | 0.636639 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/24` | 0.636639 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/15` | 0.636639 | **LASHUNTA** |

### Query 264
- Text: Summarize LIMITED TELEPATHY
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/12']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/14', 'PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/12', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/14` | 0.876527 | LIMITED TELEPATHY |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/12` | 0.876527 | LIMITED TELEPATHY |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/25` | 0.751347 | **Prerequisites** limited telepathy |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22` | 0.709347 | **Prerequisites** limited telepathy |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/21` | 0.709347 | **Prerequisites** limited telepathy |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/23` | 0.709347 | **Prerequisites** limited telepathy |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/26` | 0.567049 | Whether through training or innate talent, you've expanded  the range at which you can telepathically communicate.  Increase the range of your limited telepathy by 15 feet. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/23` | 0.555049 | Whether through training or innate talent,  you've expanded the range at which you can  telepathically communicate. Increase the range of  your limited telepathy by 15 feet. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/24` | 0.553900 | When you use limited telepathy to communicate with another  creature, the creature can give you a brief response as a reaction,  or as a free action at the beginning of their next turn. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/22` | 0.551562 | When you use limited telepathy to communicate with another  creature, you act as a conduit for their thoughts, allowing them  to respond to you for a few scant moments—if they wish. The  creature can |

### Query 265
- Text: What is the rule about You can communicate mentally with creatures within 30 feet. You can communicate only with creatures that share a language with you. This doesn't give you any access to their thoughts and communicates no more information than normal speech would.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/0/Text/13']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/8/Text/15', 'PZO22001 Starfinder Player Core 058-073::/page/0/Text/13', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/8/Text/15` | 0.964577 | You can communicate mentally with creatures within 30 feet. You can communicate only with creatures that share a language with you. This doesn't give you any access to their thoughts and communicates |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/13` | 0.964577 | You can communicate mentally with creatures within 30 feet. You can communicate only with creatures that share a language with you. This doesn't give you any access to their thoughts and communicates |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/22` | 0.719851 | When you use limited telepathy to communicate with another  creature, you act as a conduit for their thoughts, allowing them  to respond to you for a few scant moments—if they wish. The  creature can |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/16` | 0.662787 | Your antennae are covered in fine hairs that make them  more sensitive to psychic vibrations than most. You gain  thoughtsense as a vague sense with a range of 30 feet. This  means you can use your an |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/24` | 0.623451 | When you use limited telepathy to communicate with another  creature, the creature can give you a brief response as a reaction,  or as a free action at the beginning of their next turn. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/41` | 0.622283 | You never let the inability to communicate stop you from  chatting with nufriends! You gain *speak with animals* as  a 2nd-rank primal innate spell, and *speak with plants* and  *translate* as 3rd-ran |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/25` | 0.607377 | Your telepathy is stronger than most shirrens', allowing you to  combine physical, verbal, and telepathic communication. You  can transmit emotions alongside your messages whenever  you use limited te |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/26` | 0.606299 | Whether through training or innate talent, you've expanded  the range at which you can telepathically communicate.  Increase the range of your limited telepathy by 15 feet. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/23` | 0.606299 | Whether through training or innate talent,  you've expanded the range at which you can  telepathically communicate. Increase the range of  your limited telepathy by 15 feet. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/26` | 0.600400 | You attempt to enthrall a foe with a convoluted and  utterly pointless monologue that leaves your audience  dumbfounded. Attempt a Deception or Diplomacy check  against the Will DC of a single creatur |

### Query 266
- Text: What is the rule about Constantly strive to improve yourself through practicing  skills and honing your powers.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `16`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/2', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/20', 'PZO22001 Starfinder Player Core 058-073::/page/6/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/2` | 0.886626 | Constantly strive to improve yourself through practicing  skills and honing your powers. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/20` | 0.673862 | **Popular Edicts** become the best version of yourself, never stop  learning, train your mind or body daily |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/14` | 0.605400 | You push yourself to be the best by competing with the  triggering ally. Until the end of your next turn, you can attempt  the same skill check to perform the same action or activity  that the trigger |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/59` | 0.543539 | You put forth your best effort and focus everything you've  got on the task at hand, putting allsix of your hands (three  of your sets of arms) into it! The next time you roll an attack  roll or skill |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/4` | 0.540363 | Hold yourself to a much higher standard than you  apply to others. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/6` | 0.539348 | You're quick thinking and adaptable, capable of picking up  new skills and talents with little practice or training. During  your daily preparations, select one skill feat that you meet  the prerequis |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/414` | 0.539260 | Adaptive talent, general feat, skill increase, wise to the game |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/15` | 0.530358 | You adapt to situations and excel at motivating your team to overcome obstacles. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/21` | 0.528613 | You trust your instincts to see you through.  You gain master proficiency with the  triggering skill for the skill check. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/430` | 0.528079 | General feat, perception mastery, resolve, savvy improviser, skill increase |

### Query 267
- Text: What is the rule about Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/13', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3` | 0.964777 | Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/13` | 0.689263 | Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Las |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.687982 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/12` | 0.635684 | Damayas tend to be tall and graceful with delicate features and  are traditionally pushed toward artistic or intellectual pursuits  and political occupations. Korashas are shorter, more muscular,  and |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/9` | 0.621394 | Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/5` | 0.616051 | Prioritize Charisma. Dexterity, Intelligence, and  Constitution round out your abilities and defenses. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/3` | 0.607666 | You decided against activating your ancestry's adaptive  genetics. You might show a combination of damaya and  korasha traits; you might be tall and muscular or short and  lithe, or perhaps you have u |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/27` | 0.594971 | You've chosen the adaptive genetics to become a korasha. You  might be stockier and more muscular than other lashuntas. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/8` | 0.593389 | **Prerequisites** korasha lashunta or unbound lashunta heritage You can leverage your telepathic abilities to influence the  minds of others, imparting orders or inflaming fears. You can  cast *comman |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/10` | 0.561712 | If you want to play a character who strives for selfimprovement and has innate psychic abilities, you should play  a lashunta. |

### Query 268
- Text: Summarize Hold yourself to a much higher standard than you  apply to others.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/4', 'PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/2', 'PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/4` | 0.973133 | Hold yourself to a much higher standard than you  apply to others. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/2` | 0.678250 | Constantly strive to improve yourself through practicing  skills and honing your powers. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/6` | 0.650647 | Think you're a perfectionist and find your pursuit of  self-improvement tiresome. |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/ListItem/23` | 0.638882 | Like you, or at least respect you. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/ListItem/25` | 0.610353 | Assume you like being in charge. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/18` | 0.604675 | Whether through conversation, clever lies, dazzling  performances, or threats, you rely on charm and cunning to  influence others. You crave being in the spotlight. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/9/ListItem/7` | 0.595395 | Believe you overvalue and overthink simple choices. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/15` | 0.590352 | You adapt to situations and excel at motivating your team to overcome obstacles. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/9/ListItem/3` | 0.586590 | Enjoy your freedom and delight in the opportunity to  make your own decisions. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/9/ListItem/2` | 0.584976 | Build deep and powerful bonds with your comrades. |

### Query 269
- Text: Summarize OTHERS PROBABLY...
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/5']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `18`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/9/SectionHeader/5', 'PZO22001 Starfinder Player Core 058-073::/page/5/SectionHeader/5', 'PZO22001 Starfinder Player Core 058-073::/page/13/SectionHeader/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/9/SectionHeader/5` | 0.937541 | OTHERS PROBABLY... |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/13/SectionHeader/5` | 0.937541 | OTHERS PROBABLY... |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/5/SectionHeader/5` | 0.937541 | OTHERS PROBABLY... |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/5` | 0.895541 | OTHERS PROBABLY... |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/22` | 0.887541 | OTHERS PROBABLY... |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/18` | 0.697439 | YOU MIGHT... |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/16` | 0.638348 | IN DOWNTIME... |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/14` | 0.614094 | WHILE EXPLORING... |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/12` | 0.586789 | DURING SOCIAL ENCOUNTERS... |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/5/SectionHeader/10` | 0.556721 | DURING COMBAT ENCOUNTERS... |

### Query 270
- Text: Summarize Think you're a perfectionist and find your pursuit of  self-improvement tiresome.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/6', 'PZO22001 Starfinder Player Core 058-073::/page/9/ListItem/7', 'PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/6` | 0.986614 | Think you're a perfectionist and find your pursuit of  self-improvement tiresome. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/9/ListItem/7` | 0.648660 | Believe you overvalue and overthink simple choices. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/2` | 0.642127 | Constantly strive to improve yourself through practicing  skills and honing your powers. |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/4` | 0.589753 | Hold yourself to a much higher standard than you  apply to others. |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/5/ListItem/7` | 0.589467 | Envy your musical talent. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/5/ListItem/25` | 0.586065 | Assume you like being in charge. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/5/ListItem/6` | 0.571596 | Think you struggle with computers, vehicles, and  other technology. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/9/ListItem/8` | 0.571043 | Are disconcerted by your insectile physiology and  telepathy. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/57` | 0.568549 | **Trigger** You're targeted by a mental effect. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/13/ListItem/8` | 0.564300 | Assume you're flighty or unreliable and that you don't  take yourself seriously. |

### Query 271
- Text: Summarize Distrust your psychic abilities, fearing you'll read their  minds.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `33`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/7', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/27', 'PZO22001 Starfinder Player Core 058-073::/page/9/ListItem/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/7` | 0.980505 | Distrust your psychic abilities, fearing you'll read their  minds. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/27` | 0.670553 | Your psychic training allows you to block attempts to read  your thoughts. Any effect that specifically attempts to read  your mind to glean information must succeed at a counteract  check against the |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/9/ListItem/8` | 0.656805 | Are disconcerted by your insectile physiology and  telepathy. |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/43` | 0.589071 | You can use your telepathic abilities to quickly assess your  circumstances or subtly glean information from the minds of  others. You can cast *hypercognition* and *mind reading* as 3rdrank occult in |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/9/ListItem/7` | 0.575313 | Believe you overvalue and overthink simple choices. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/58` | 0.572738 | You can shield your mind by using similar techniques that  your ancestors once mastered to escape the Swarm. You block  the intruding effect by scattering your thoughts, making you  immune to the trig |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/21` | 0.567869 | You trust your instincts to see you through.  You gain master proficiency with the  triggering skill for the skill check. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/13/ListItem/7` | 0.561976 | Expect you to want to help them and act surprised if  you don't. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/13/ListItem/8` | 0.558636 | Assume you're flighty or unreliable and that you don't  take yourself seriously. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/16` | 0.557687 | Your antennae are covered in fine hairs that make them  more sensitive to psychic vibrations than most. You gain  thoughtsense as a vague sense with a range of 30 feet. This  means you can use your an |

### Query 272
- Text: Summarize Idealize or label you based on your genetic expression.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/8', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/57', 'PZO22001 Starfinder Player Core 058-073::/page/13/ListItem/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/8` | 0.979553 | Idealize or label you based on your genetic expression. |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/22` | 0.662788 | Select a heritage from those available within that  ancestry, further defining the traits your character was  born with. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/57` | 0.605286 | **Trigger** You're targeted by a mental effect. |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/13/ListItem/6` | 0.594327 | Are in awe of your boundless energy, enthusiasm, and  positivity (or another emotion you express most often). |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/21` | 0.590836 | Pick the ancestry itself. |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/4` | 0.585010 | Excellence in an attribute modifier improves the checks and statistics related to that ability, as described below. When  imagining your character, you should also decide what attribute modifiers you |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/5/ListItem/23` | 0.566522 | Like you, or at least respect you. |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/19` | 0.562610 | Adjust bonuses from feats and other abilities that  are based on your level. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/47` | 0.551928 | **Trigger** You roll initiative. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/5/ListItem/8` | 0.549482 | Assume you're looking for an excuse to prove yourself  in a fight. |

### Query 273
- Text: What is the rule about Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, driven, and self-reflective, with a perpetual  desire for growth—both in terms of personal advancement and  self-improvement. This cultural push to know oneself, embrace  one's strengths, surpass one's past successes, and strive for evergreater goals drives lashuntas to value education, focus, and  training as well as to explore new discoveries, technologies, and  modes of thought. While many lashuntas today still fulfill the  traditional role of the enlightened warrior or the consummate  scholar, time and shifting social norms have gifted lashuntas  the freedom to branch out in countless ways, developing their  own interests, hobbies, and genetic expressions, with no regard  to their heritage or societal standing.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `27`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/9', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/13', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/9` | 0.979852 | Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/13` | 0.838112 | Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Las |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/12` | 0.767956 | Damayas tend to be tall and graceful with delicate features and  are traditionally pushed toward artistic or intellectual pursuits  and political occupations. Korashas are shorter, more muscular,  and |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/2` | 0.722258 | Long ago, lashuntas evolved psychic abilities and a unique dimorphism that helped them survive on their home world of Castrovel. In modern times, lashuntas manipulate their own genetics at puberty, al |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/23` | 0.679440 | Around puberty, many lashuntas choose to embrace a genetic  path that determines their physiology and role in society.  Choose one of the following lashunta heritages at 1st level. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.664053 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3` | 0.645734 | Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/27` | 0.634635 | You've chosen the adaptive genetics to become a korasha. You  might be stockier and more muscular than other lashuntas. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/19` | 0.613844 | Lashunta cultures value education, self-improvement, and  community defense. Religious lashuntas tend to identify with  faiths that encourage balance, knowledge, meditative practice,  and seeking enli |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/31` | 0.607576 | You've studied the lives and achievements of other  lashuntas who have improved both their psychic powers  and their communities. You gain the trained proficiency  rank in Occultism and Society. If yo |

### Query 274
- Text: What is the rule about If you want to play a character who strives for selfimprovement and has innate psychic abilities, you should play  a lashunta.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `31`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/10', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/9', 'PZO22001 Starfinder Player Core 058-073::/page/0/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/10` | 0.935485 | If you want to play a character who strives for selfimprovement and has innate psychic abilities, you should play  a lashunta. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/9` | 0.683984 | Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/2` | 0.672902 | Long ago, lashuntas evolved psychic abilities and a unique dimorphism that helped them survive on their home world of Castrovel. In modern times, lashuntas manipulate their own genetics at puberty, al |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/8` | 0.614714 | **Prerequisites** korasha lashunta or unbound lashunta heritage You can leverage your telepathic abilities to influence the  minds of others, imparting orders or inflaming fears. You can  cast *comman |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3` | 0.599072 | Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/10` | 0.598998 | If you want to play a character who fights for freedom with  grace and style, you should play a pahtra. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/7` | 0.585205 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a lashunta, you choose from among  the following |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/13` | 0.577570 | Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Las |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/31` | 0.572104 | You've studied the lives and achievements of other  lashuntas who have improved both their psychic powers  and their communities. You gain the trained proficiency  rank in Occultism and Society. If yo |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/23` | 0.567978 | Around puberty, many lashuntas choose to embrace a genetic  path that determines their physiology and role in society.  Choose one of the following lashunta heritages at 1st level. |

### Query 275
- Text: Summarize PHYSICAL DESCRIPTION
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/11']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `12`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/5/SectionHeader/11', 'PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/11', 'PZO22001 Starfinder Player Core 058-073::/page/13/SectionHeader/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/5/SectionHeader/11` | 0.896888 | PHYSICAL DESCRIPTION |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/11` | 0.896888 | PHYSICAL DESCRIPTION |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/13/SectionHeader/12` | 0.896888 | PHYSICAL DESCRIPTION |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/9/SectionHeader/11` | 0.854888 | PHYSICAL DESCRIPTION |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/30` | 0.561284 | CHARACTER Sheet |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/18` | 0.557238 | STEP 10: FINISHING DETAILS |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/16` | 0.552752 | INTRODUCTION |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/1` | 0.546085 | SAMPLE CHARACTER |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.545223 | **OVERVIEW** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/63` | 0.542349 | **INTRODUCTION** |

### Query 276
- Text: What is the rule about Damayas tend to be tall and graceful with delicate features and  are traditionally pushed toward artistic or intellectual pursuits  and political occupations. Korashas are shorter, more muscular,  and gravitate toward military service, manual labor, and wartime  leadership. Regardless of heritage, all lashuntas have short  forehead antennae that focus their telepathy, with colorful  bumps and facial markings unique to each individual. Lashuntas  produce pheromones that subtly broadcast their moods in ways  that other ancestries might find alluring or unnerving.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `32`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/12', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/9', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/12` | 0.996482 | Damayas tend to be tall and graceful with delicate features and  are traditionally pushed toward artistic or intellectual pursuits  and political occupations. Korashas are shorter, more muscular,  and |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/9` | 0.805034 | Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/13` | 0.729191 | Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Las |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3` | 0.663735 | Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities. |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.658587 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/27` | 0.609858 | You've chosen the adaptive genetics to become a korasha. You  might be stockier and more muscular than other lashuntas. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/3` | 0.602697 | You decided against activating your ancestry's adaptive  genetics. You might show a combination of damaya and  korasha traits; you might be tall and muscular or short and  lithe, or perhaps you have u |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/2` | 0.588324 | Long ago, lashuntas evolved psychic abilities and a unique dimorphism that helped them survive on their home world of Castrovel. In modern times, lashuntas manipulate their own genetics at puberty, al |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/19` | 0.560461 | Lashunta cultures value education, self-improvement, and  community defense. Religious lashuntas tend to identify with  faiths that encourage balance, knowledge, meditative practice,  and seeking enli |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/23` | 0.557957 | Around puberty, many lashuntas choose to embrace a genetic  path that determines their physiology and role in society.  Choose one of the following lashunta heritages at 1st level. |

### Query 277
- Text: What is the rule about Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Lashuntas achieve their choice through  a combination of psychic rituals and gene therapy. Today,  many young lashuntas have chosen to tread their own path  and abstain from this choice, instead becoming "unbound."  Unbound lashuntas defy traditional roles and labels, and they  might express traits and innate proclivities common to both  of or neither of these groups. A growing minority of lashuntas  instead pushes for further genetic diversification and aims to  express unique or long-buried genetic permutations, pioneering  entirely new chosen heritages. Whether such experimentation  will prove fruitful remains to be seen.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/13', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/9', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/13` | 1.005484 | Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Las |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/9` | 0.852552 | Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/23` | 0.796113 | Around puberty, many lashuntas choose to embrace a genetic  path that determines their physiology and role in society.  Choose one of the following lashunta heritages at 1st level. |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/12` | 0.700272 | Damayas tend to be tall and graceful with delicate features and  are traditionally pushed toward artistic or intellectual pursuits  and political occupations. Korashas are shorter, more muscular,  and |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/2` | 0.697778 | Long ago, lashuntas evolved psychic abilities and a unique dimorphism that helped them survive on their home world of Castrovel. In modern times, lashuntas manipulate their own genetics at puberty, al |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3` | 0.694538 | Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/3` | 0.657508 | You decided against activating your ancestry's adaptive  genetics. You might show a combination of damaya and  korasha traits; you might be tall and muscular or short and  lithe, or perhaps you have u |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/27` | 0.653708 | You've chosen the adaptive genetics to become a korasha. You  might be stockier and more muscular than other lashuntas. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.637581 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/8` | 0.585909 | **Prerequisites** korasha lashunta or unbound lashunta heritage You can leverage your telepathic abilities to influence the  minds of others, imparting orders or inflaming fears. You can  cast *comman |

### Query 278
- Text: Summarize SOCIETY
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `14`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/14', 'PZO22001 Starfinder Player Core 058-073::/page/13/SectionHeader/14', 'PZO22001 Starfinder Player Core 058-073::/page/5/SectionHeader/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/14` | 0.715815 | SOCIETY |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/13/SectionHeader/14` | 0.715815 | SOCIETY |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/5/SectionHeader/14` | 0.715815 | SOCIETY |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/9/SectionHeader/14` | 0.673815 | SOCIETY |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/542` | 0.537113 | Acquire Asset |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/15` | 0.526997 | **CONCENTRATE** **FORTUNE** **SHIRREN** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/1` | 0.526992 | SAMPLE CHARACTER |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/13` | 0.512306 | SKILLS |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/23` | 0.512306 | SKILLS |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.511788 | **OVERVIEW** |

### Query 279
- Text: Summarize Since time immemorial, lashuntas have dwelled in sprawling,
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `45`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/15', 'PZO22001 Starfinder Player Core 058-073::/page/0/Text/2', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/15` | 0.975350 | Since time immemorial, lashuntas have dwelled in sprawling, |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/2` | 0.661418 | Long ago, lashuntas evolved psychic abilities and a unique dimorphism that helped them survive on their home world of Castrovel. In modern times, lashuntas manipulate their own genetics at puberty, al |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/9` | 0.637541 | Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/30` | 0.567874 | Lashuntas are charming  telepaths from Castrovel who  are known for their unique  dimorphism. Page 58. |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/23` | 0.543836 | Around puberty, many lashuntas choose to embrace a genetic  path that determines their physiology and role in society.  Choose one of the following lashunta heritages at 1st level. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/9` | 0.535248 | Shirrens were originally members of the Swarm, a collection  of colonies controlled by a hive mind that devoured entire  planets. In time, shirrens gained a sense of individual self  and rejected the |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/13` | 0.532353 | Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Las |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/19` | 0.504004 | Lashunta cultures value education, self-improvement, and  community defense. Religious lashuntas tend to identify with  faiths that encourage balance, knowledge, meditative practice,  and seeking enli |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/6` | 0.503907 | While most shirrens broke away from the Swarm long ago, |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/2` | 0.501963 | UNBOUND LASHUNTA |

### Query 280
- Text: Summarize picturesque cities along the shores and wildlands of Castrovel,  a lush jungle world teeming with dangerous predators and  extreme weather. These independent settlements are protected  by a mighty military caste of psychic warriors, technological  defenses, and magical countermeasures. The most iconic of  these soldiers are the shotalashu cavalry, lightly armored riders  who form telepathic bonds with (and take their name from)  their saurian mounts.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/16']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/16', 'PZO22001 Starfinder Player Core 058-073::/page/0/Text/2', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/16` | 1.025279 | picturesque cities along the shores and wildlands of Castrovel,  a lush jungle world teeming with dangerous predators and  extreme weather. These independent settlements are protected  by a mighty mil |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/2` | 0.606939 | Long ago, lashuntas evolved psychic abilities and a unique dimorphism that helped them survive on their home world of Castrovel. In modern times, lashuntas manipulate their own genetics at puberty, al |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/25` | 0.576542 | You descend from a long line of hunters, and your fur is  especially well suited to blending into multiple environments.  As long as you're in a natural and undeveloped environment,  you gain a +2 cir |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/ListItem/20` | 0.563833 | Have friends—and enemies—in unexpected places. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/30` | 0.554484 | Lashuntas are charming  telepaths from Castrovel who  are known for their unique  dimorphism. Page 58. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/27` | 0.533579 | You have an undeniable streak of luck that you believe is a  blessing from your ancestral god Meyel. You might come from |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/28` | 0.532451 | You grew up in the subterranean realm of Gadraveech, or a  similar dangerous underground environment. You have wispy, |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/20` | 0.528269 | Kasathas are four-armed  migrants from a dying world  who value cosmic balance and  tradition. Page 54. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/41` | 0.524034 | Whether through intense musical training, magical insight, or  Meyel's divine blessing, you can feel the rhythm of the world  around you and tug on time's chords to manipulate its melody  and flow. Yo |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/4/Text/2` | 0.516802 | Pahtras are a humanoid feline species from a nearby star system. They're highly competitive and known for their achievements in magic, music, and war. Their home world was recently freed from the Vesk |

### Query 281
- Text: Summarize **Sample Names:** Lashunta naming conventions often use  tonal elements. Some sample lashunta names are Domash,  Hesori, Imaaz, Kima, Kopalo, Maenala, Nomae, Oraeus, Raia,  Shess, Soryn, Stretto, Taeon, and Varikuara.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `48`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/17', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/18', 'PZO22001 Starfinder Player Core 058-073::/page/13/Text/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/17` | 1.044200 | **Sample Names:** Lashunta naming conventions often use  tonal elements. Some sample lashunta names are Domash,  Hesori, Imaaz, Kima, Kopalo, Maenala, Nomae, Oraeus, Raia,  Shess, Soryn, Stretto, Taeo |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/18` | 0.759269 | **Sample Names:** Traditional pahtra names contain  auspicious elements determined by a mystic. Pahtra names  include Cahnex, Dae, Fetenekku, Hafoumei, Ifset, Ihrasara,  Jeviish, Khieper, Lealorn, Mah |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/18` | 0.661195 | **Sample Names:** Ayoka, Baazo, Bixby, Dakoyo, Fipzul, Gazigaz,  Jomp, Kayoko, Kimikim, Mimzy, Nako, Prismacora, Quonx,  Rudfuz, Sprax, Timinim, Tipps, Tonkona, Viverivim |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/41` | 0.597178 | **UNCOMMON** **LASHUNTA** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/15` | 0.584386 | **CONCENTRATE** **FORTUNE** **LASHUNTA** **MENTAL** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/47` | 0.583607 | **LASHUNTA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/24` | 0.583607 | **LASHUNTA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/2` | 0.583607 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/59` | 0.583607 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/11` | 0.583607 | **LASHUNTA** |

### Query 282
- Text: Summarize BELIEFS
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/18']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `15`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/5/SectionHeader/19', 'PZO22001 Starfinder Player Core 058-073::/page/9/SectionHeader/18', 'PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/5/SectionHeader/19` | 0.833577 | BELIEFS |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/9/SectionHeader/18` | 0.833577 | BELIEFS |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/18` | 0.833577 | BELIEFS |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/13/SectionHeader/19` | 0.791577 | BELIEFS |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/12` | 0.586422 | FAITH |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/9/ListItem/7` | 0.585782 | Believe you overvalue and overthink simple choices. |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/1/SectionHeader/6` | 0.583102 | UNDERSTANDING ACTIONS |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/6` | 0.577569 | PERCEPTION |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/SectionHeader/43` | 0.563644 | ENVOY FEATS |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/14` | 0.563644 | ENVOY FEATS |

### Query 283
- Text: What is the rule about Lashunta cultures value education, self-improvement, and  community defense. Religious lashuntas tend to identify with  faiths that encourage balance, knowledge, meditative practice,  and seeking enlightenment, such as Eloritu, Ibra, or Yaraesa.  Other lashuntas shun religion entirely in favor of adopting a  philosophy like the Cycle or the Green Faith, honoring a state  leader, or following historic community traditions.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `39`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/19', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/9', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/19` | 0.999917 | Lashunta cultures value education, self-improvement, and  community defense. Religious lashuntas tend to identify with  faiths that encourage balance, knowledge, meditative practice,  and seeking enli |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/9` | 0.674510 | Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/13` | 0.602985 | Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Las |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3` | 0.558397 | Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities. |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/19` | 0.556838 | Shirrens define themselves by their choices and bristle against  all forms of oppression. They enjoy cultural exchange, and  while most eagerly adopt the deities and practices of other  communities, o |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/12` | 0.548219 | Damayas tend to be tall and graceful with delicate features and  are traditionally pushed toward artistic or intellectual pursuits  and political occupations. Korashas are shorter, more muscular,  and |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/23` | 0.540815 | Around puberty, many lashuntas choose to embrace a genetic  path that determines their physiology and role in society.  Choose one of the following lashunta heritages at 1st level. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/31` | 0.537590 | You've studied the lives and achievements of other  lashuntas who have improved both their psychic powers  and their communities. You gain the trained proficiency  rank in Occultism and Society. If yo |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/15` | 0.530161 | Shirrens value individual choice and rights, having escaped  from the Swarm thanks to an adaptation to their physiology  that causes pleasure when they make choices for themselves.  Shirren culture is |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/13` | 0.518485 | Perhaps you'd like to play a character who is a devout  follower of a specific deity. The peoples of the galaxy follow  myriad faiths and philosophies spanning a wide pantheon,  from Damoritosh, the C |

### Query 284
- Text: Summarize **Popular Edicts** become the best version of yourself, never stop  learning, train your mind or body daily
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/20']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/20', 'PZO22001 Starfinder Player Core 058-073::/page/9/Text/20', 'PZO22001 Starfinder Player Core 058-073::/page/13/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/20` | 1.008361 | **Popular Edicts** become the best version of yourself, never stop  learning, train your mind or body daily |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/20` | 0.746256 | **Popular Edicts** make your own choices, try to solve problems  peacefully, work for the greater good of the group |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/21` | 0.734417 | **Popular Edicts** be kind, help others, respect and nurture living  beings |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/21` | 0.666675 | **Popular Edicts** challenge yourself and your allies, perform  music and dance daily, take pride in your accomplishments **Popular Anathema** abandon your ancestral traditions, bow to  tyrants, give |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/2` | 0.665087 | Constantly strive to improve yourself through practicing  skills and honing your powers. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/13/ListItem/6` | 0.570539 | Are in awe of your boundless energy, enthusiasm, and  positivity (or another emotion you express most often). |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/9/ListItem/3` | 0.557122 | Enjoy your freedom and delight in the opportunity to  make your own decisions. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/ListItem/23` | 0.545079 | Like you, or at least respect you. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/430` | 0.538909 | General feat, perception mastery, resolve, savvy improviser, skill increase |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/8` | 0.527608 | Your savvy and skill are unparalleled. No matter the situation,  you quickly course correct to set the tone you need to succeed.  You gain the following action. |

### Query 285
- Text: Summarize **Popular Anathema** neglect your goals, wallow in failure
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/21', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/21', 'PZO22001 Starfinder Player Core 058-073::/page/13/Text/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/21` | 0.995726 | **Popular Anathema** neglect your goals, wallow in failure |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/21` | 0.698451 | **Popular Edicts** challenge yourself and your allies, perform  music and dance daily, take pride in your accomplishments **Popular Anathema** abandon your ancestral traditions, bow to  tyrants, give |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/22` | 0.666858 | **Popular Anathema** cause intentional harm without reason,  pollute the environment, refuse to help someone in dire need |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/21` | 0.597528 | **Popular Anathema** inflict thoughtless destruction, take away  another's right to make choices |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/6` | 0.567430 | Think you're a perfectionist and find your pursuit of  self-improvement tiresome. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/9/ListItem/7` | 0.554383 | Believe you overvalue and overthink simple choices. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/20` | 0.511914 | **Popular Edicts** become the best version of yourself, never stop  learning, train your mind or body daily |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/47` | 0.511127 | Your insults and threats almost always hit the mark. When  you roll a failure on a Demoralize action, you get a success  instead. You can still critically fail. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/13/ListItem/8` | 0.507345 | Assume you're flighty or unreliable and that you don't  take yourself seriously. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/15` | 0.505467 | **CONCENTRATE** **FORTUNE** **LASHUNTA** **MENTAL** |

### Query 286
- Text: Summarize LASHUNTA HERITAGES
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `46`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/22', 'PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/6']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/22` | 0.938749 | LASHUNTA HERITAGES |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1` | 0.803529 | LASHUNTA |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/6` | 0.728806 | LASHUNTA ANCESTRY  FEATS |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/2` | 0.685957 | **LASHUNTA** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/7` | 0.685957 | **LASHUNTA** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/24` | 0.685957 | **LASHUNTA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/30` | 0.685957 | **LASHUNTA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/11` | 0.685957 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/20` | 0.685957 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/11` | 0.685957 | **LASHUNTA** |

### Query 287
- Text: What is the rule about Around puberty, many lashuntas choose to embrace a genetic  path that determines their physiology and role in society.  Choose one of the following lashunta heritages at 1st level.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/23', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/13', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/23` | 0.989070 | Around puberty, many lashuntas choose to embrace a genetic  path that determines their physiology and role in society.  Choose one of the following lashunta heritages at 1st level. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/13` | 0.775463 | Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Las |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/9` | 0.726195 | Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/2` | 0.649415 | Long ago, lashuntas evolved psychic abilities and a unique dimorphism that helped them survive on their home world of Castrovel. In modern times, lashuntas manipulate their own genetics at puberty, al |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/7` | 0.632111 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a lashunta, you choose from among  the following |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/24` | 0.607667 | A skittermander's heritage is influenced by the environment  they grew up in or the climate they adapted to. Choose one of  the following skittermander heritages at 1st level. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/10` | 0.594739 | If you want to play a character who strives for selfimprovement and has innate psychic abilities, you should play  a lashunta. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/31` | 0.583426 | You've studied the lives and achievements of other  lashuntas who have improved both their psychic powers  and their communities. You gain the trained proficiency  rank in Occultism and Society. If yo |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/27` | 0.578723 | You've chosen the adaptive genetics to become a korasha. You  might be stockier and more muscular than other lashuntas. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3` | 0.576818 | Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities. |

### Query 288
- Text: Summarize DAMAYA LASHUNTA
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `44`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/24', 'PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/2']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/24` | 0.897064 | DAMAYA LASHUNTA |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1` | 0.712121 | LASHUNTA |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/2` | 0.655273 | **LASHUNTA** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/7` | 0.613274 | **LASHUNTA** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/26` | 0.613274 | **LASHUNTA** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/11` | 0.613274 | **LASHUNTA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/20` | 0.613274 | **LASHUNTA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/30` | 0.613274 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/24` | 0.613274 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/15` | 0.613274 | **LASHUNTA** |

### Query 289
- Text: What is the rule about You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In addition to what you gain from your ancestry, you gain  an attribute boost to Intelligence and an attribute flaw to  Constitution, but the free ancestry boost can't also be Intelligence.  You become trained in Diplomacy. If you would automatically  become trained in Diplomacy (from your background or class,  for example), you become trained in another skill of your choice.  You gain the Additional Lore general feat.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `18`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/25', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/3', 'PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 1.019171 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/3` | 0.744300 | You decided against activating your ancestry's adaptive  genetics. You might show a combination of damaya and  korasha traits; you might be tall and muscular or short and  lithe, or perhaps you have u |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3` | 0.727440 | Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities. |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/4` | 0.685073 | Your ability to adapt to various beliefs instills you with  knowledge of many cultures. You gain the trained proficiency  rank in Diplomacy and Society. If you would automatically  become trained in o |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/27` | 0.674472 | You've chosen the adaptive genetics to become a korasha. You  might be stockier and more muscular than other lashuntas. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/9` | 0.662002 | Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/1` | 0.647423 | In addition to what you gain from your ancestry, you gain an  attribute boost to Strength and an attribute flaw to Wisdom,  but the free ancestry boost can't also be Strength. You gain 8  Hit Points f |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/31` | 0.646338 | You've studied the lives and achievements of other  lashuntas who have improved both their psychic powers  and their communities. You gain the trained proficiency  rank in Occultism and Society. If yo |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/12` | 0.643276 | Damayas tend to be tall and graceful with delicate features and  are traditionally pushed toward artistic or intellectual pursuits  and political occupations. Korashas are shorter, more muscular,  and |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/13` | 0.638338 | Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Las |

### Query 290
- Text: Summarize KORASHA LASHUNTA
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `47`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/26', 'PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/26` | 0.883339 | KORASHA LASHUNTA |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1` | 0.671939 | LASHUNTA |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/15` | 0.639547 | **LASHUNTA** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/11` | 0.597547 | **LASHUNTA** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/7` | 0.597547 | **LASHUNTA** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/47` | 0.597547 | **LASHUNTA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/24` | 0.597547 | **LASHUNTA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/20` | 0.597547 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/20` | 0.597547 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/30` | 0.597547 | **LASHUNTA** |

### Query 291
- Text: Summarize You've chosen the adaptive genetics to become a korasha. You  might be stockier and more muscular than other lashuntas.
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `34`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/27', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/3', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/27` | 1.012528 | You've chosen the adaptive genetics to become a korasha. You  might be stockier and more muscular than other lashuntas. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/3` | 0.741830 | You decided against activating your ancestry's adaptive  genetics. You might show a combination of damaya and  korasha traits; you might be tall and muscular or short and  lithe, or perhaps you have u |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.728090 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/13` | 0.675030 | Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Las |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/9` | 0.669826 | Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/2` | 0.659880 | Long ago, lashuntas evolved psychic abilities and a unique dimorphism that helped them survive on their home world of Castrovel. In modern times, lashuntas manipulate their own genetics at puberty, al |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3` | 0.635142 | Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/23` | 0.634616 | Around puberty, many lashuntas choose to embrace a genetic  path that determines their physiology and role in society.  Choose one of the following lashunta heritages at 1st level. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/12` | 0.626253 | Damayas tend to be tall and graceful with delicate features and  are traditionally pushed toward artistic or intellectual pursuits  and political occupations. Korashas are shorter, more muscular,  and |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/10` | 0.614485 | If you want to play a character who strives for selfimprovement and has innate psychic abilities, you should play  a lashunta. |

### Query 292
- Text: Summarize **INTRODUCTION**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/29']
- Expected found: `True`
- Expected rank: `7`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/Text/57', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/29', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/63']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/57` | 0.913367 | **INTRODUCTION** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/63` | 0.913367 | **INTRODUCTION** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/29` | 0.913367 | **INTRODUCTION** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/30` | 0.871367 | **INTRODUCTION** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/66` | 0.871367 | **INTRODUCTION** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/65` | 0.871367 | **INTRODUCTION** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/29` | 0.871367 | **INTRODUCTION** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/30` | 0.871367 | **INTRODUCTION** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/31` | 0.863367 | **INTRODUCTION** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/56` | 0.863367 | **INTRODUCTION** |

### Query 293
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/30']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `16`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/15/Text/67', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/30', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/64']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/67` | 0.830013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/30` | 0.830013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/64` | 0.830013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/66` | 0.788013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/31` | 0.788013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/31` | 0.788013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/58` | 0.788013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/30` | 0.788013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/29` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/23` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 294
- Text: Summarize **Android**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/31']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `22`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/15/Text/68', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/31', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/65']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/68` | 0.841986 | **Android** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/31` | 0.841986 | **Android** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/65` | 0.841986 | **Android** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/59` | 0.799986 | **Android** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/31` | 0.799986 | **Android** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/32` | 0.799986 | **Android** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/32` | 0.799986 | **Android** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/67` | 0.799986 | **Android** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.675179 | **OVERVIEW** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/77` | 0.636029 | **Versatile ** |

### Query 295
- Text: Summarize **Barathu** **Human**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/32']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `22`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/9/Text/33', 'PZO22001 Starfinder Player Core 058-073::/page/13/Text/33', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/33` | 0.928040 | **Barathu** **Human** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/33` | 0.928040 | **Barathu** **Human** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/32` | 0.928040 | **Barathu** **Human** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/69` | 0.791759 | **Barathu** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/68` | 0.791759 | **Barathu** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/60` | 0.791759 | **Barathu** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/66` | 0.791759 | **Barathu** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/32` | 0.791759 | **Barathu** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/61` | 0.696880 | **Human** **Kasatha** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/33` | 0.686615 | **Human** |

### Query 296
- Text: Summarize **Kasatha**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/33']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `31`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/11/Text/70', 'PZO22001 Starfinder Player Core 058-073::/page/15/Text/71', 'PZO22001 Starfinder Player Core 058-073::/page/9/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/70` | 0.852037 | **Kasatha** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/71` | 0.852037 | **Kasatha** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/34` | 0.852037 | **Kasatha** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/33` | 0.810037 | **Kasatha** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/34` | 0.810037 | **Kasatha** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/61` | 0.760544 | **Human** **Kasatha** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/34` | 0.741664 | **Kasatha** **Lashunta** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/68` | 0.741664 | **Kasatha** **Lashunta** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.654660 | **OVERVIEW** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/11` | 0.639326 | **LASHUNTA** |

### Query 297
- Text: Summarize **Lashunta**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/34']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `40`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/13/Text/35', 'PZO22001 Starfinder Player Core 058-073::/page/15/Text/72', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/71']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/35` | 0.869464 | **Lashunta** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/72` | 0.869464 | **Lashunta** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/71` | 0.869464 | **Lashunta** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/34` | 0.827464 | **Lashunta** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/62` | 0.827464 | **Lashunta** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/26` | 0.806386 | **LASHUNTA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/11` | 0.806386 | **LASHUNTA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/2` | 0.806386 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/7` | 0.806386 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/20` | 0.806386 | **LASHUNTA** |

### Query 298
- Text: Summarize **Pahtra**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/35']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `46`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/5/Text/35', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/35', 'PZO22001 Starfinder Player Core 058-073::/page/15/Text/73']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/35` | 0.829643 | **Pahtra** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/73` | 0.829643 | **Pahtra** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/35` | 0.829643 | **Pahtra** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/63` | 0.787643 | **Pahtra** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/72` | 0.787643 | **Pahtra** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/36` | 0.787643 | **Pahtra** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/50` | 0.744532 | **PAHTRA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/23` | 0.744532 | **PAHTRA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/54` | 0.744532 | **PAHTRA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/33` | 0.744532 | **PAHTRA** |

### Query 299
- Text: Summarize **Shirren**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/36']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `39`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/15/Text/74', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/36', 'PZO22001 Starfinder Player Core 058-073::/page/13/Text/37']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/74` | 0.882308 | **Shirren** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/36` | 0.882308 | **Shirren** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/37` | 0.882308 | **Shirren** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/64` | 0.840308 | **Shirren** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/73` | 0.840308 | **Shirren** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/36` | 0.840308 | **Shirren** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/36` | 0.840308 | **Shirren** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/55` | 0.764532 | **SHIRREN** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/8` | 0.764532 | **SHIRREN** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/3` | 0.764532 | **SHIRREN** |

### Query 300
- Text: Summarize **Skittermander**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/37']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `49`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/71', 'PZO22001 Starfinder Player Core 058-073::/page/13/Text/38', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/37']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/71` | 0.871057 | **Skittermander** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/37` | 0.871057 | **Skittermander** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/38` | 0.871057 | **Skittermander** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/37` | 0.829057 | **Skittermander** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/37` | 0.829057 | **Skittermander** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/75` | 0.829057 | **Skittermander** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/74` | 0.829057 | **Skittermander** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/65` | 0.829057 | **Skittermander** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/44` | 0.758907 | **SKITTERMANDER** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/17` | 0.758907 | **SKITTERMANDER** |

### Query 301
- Text: Summarize **Vesk**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/38']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/38', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/75', 'PZO22001 Starfinder Player Core 058-073::/page/9/Text/38']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/38` | 0.858738 | **Vesk** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/75` | 0.858738 | **Vesk** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/38` | 0.858738 | **Vesk** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/72` | 0.816738 | **Vesk** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/38` | 0.816738 | **Vesk** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/76` | 0.816738 | **Vesk** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/39` | 0.816738 | **Vesk** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/66` | 0.816738 | **Vesk** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.609118 | **OVERVIEW** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/68` | 0.570933 | **Versatile ** |

### Query 302
- Text: Summarize **Ysoki**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/39']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `30`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/73', 'PZO22001 Starfinder Player Core 058-073::/page/7/Text/67', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/39']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/73` | 0.860672 | **Ysoki** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/67` | 0.860672 | **Ysoki** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/39` | 0.860672 | **Ysoki** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/76` | 0.818672 | **Ysoki** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/39` | 0.818672 | **Ysoki** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/77` | 0.818672 | **Ysoki** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/40` | 0.818672 | **Ysoki** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/39` | 0.818672 | **Ysoki** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.613365 | **OVERVIEW** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/48` | 0.587009 | Ysoki are flexible in both mind  and body, using their skills for  their communities and family.  Page 78. |

### Query 303
- Text: Summarize **Versatile ** **Heritages**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/40']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/40', 'PZO22001 Starfinder Player Core 058-073::/page/9/Text/40', 'PZO22001 Starfinder Player Core 058-073::/page/13/Text/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/40` | 0.922329 | **Versatile ** **Heritages** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/40` | 0.922329 | **Versatile ** **Heritages** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/41` | 0.922329 | **Versatile ** **Heritages** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/40` | 0.880329 | **Versatile ** **Heritages** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/78` | 0.880329 | **Versatile ** **Heritages** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/74` | 0.880329 | **Versatile ** **Heritages** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/68` | 0.739238 | **Versatile ** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/77` | 0.739238 | **Versatile ** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/13/SectionHeader/54` | 0.667922 | ANCESTRIES VERSATILE HERITAGES |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/10` | 0.659741 | **TRAITS ** |

### Query 304
- Text: Summarize **Borai**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/41']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/15/Text/79', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/75', 'PZO22001 Starfinder Player Core 058-073::/page/9/Text/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/79` | 0.852576 | **Borai** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/75` | 0.852576 | **Borai** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/41` | 0.852576 | **Borai** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/41` | 0.810576 | **Borai** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/41` | 0.810576 | **Borai** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/42` | 0.810576 | **Borai** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/69` | 0.692309 | **Heritages** **Borai** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/78` | 0.692309 | **Heritages** **Borai** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.572751 | **OVERVIEW** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/32` | 0.524107 | **Solarian** |

### Query 305
- Text: Summarize **Prismeni**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/42']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `36`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/42', 'PZO22001 Starfinder Player Core 058-073::/page/15/Text/80', 'PZO22001 Starfinder Player Core 058-073::/page/13/Text/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/42` | 0.885823 | **Prismeni** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/80` | 0.885823 | **Prismeni** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/43` | 0.885823 | **Prismeni** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/76` | 0.843823 | **Prismeni** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/70` | 0.843823 | **Prismeni** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/42` | 0.843823 | **Prismeni** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/42` | 0.843823 | **Prismeni** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/79` | 0.843823 | **Prismeni** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.632643 | **OVERVIEW** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/49` | 0.595085 | **SPELLS** |

### Query 306
- Text: What is the rule about **Backgrounds** **Languages**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/43', 'PZO22001 Starfinder Player Core 058-073::/page/13/Text/44', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/80']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/43` | 0.797805 | **Backgrounds** **Languages** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/44` | 0.797805 | **Backgrounds** **Languages** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/80` | 0.721725 | **Backgrounds** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/43` | 0.679725 | **Backgrounds** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/43` | 0.679725 | **Backgrounds** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/81` | 0.679725 | **Backgrounds** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/71` | 0.679725 | **Backgrounds** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/77` | 0.679725 | **Backgrounds** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/81` | 0.648939 | **Languages** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/82` | 0.636939 | **Languages** |

### Query 307
- Text: Summarize **CLASSES**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/44']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `19`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/5/Text/45', 'PZO22001 Starfinder Player Core 058-073::/page/13/Text/45', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/44']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/45` | 0.866254 | **CLASSES** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/44` | 0.866254 | **CLASSES** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/45` | 0.866254 | **CLASSES** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/83` | 0.824254 | **CLASSES** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/73` | 0.824254 | **CLASSES** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/82` | 0.824254 | **CLASSES** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/28` | 0.816254 | **CLASSES** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/23` | 0.816254 | **CLASSES** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/34` | 0.816254 | **CLASSES** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/29` | 0.816254 | **CLASSES** |

### Query 308
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/45']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `14`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/45', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/80', 'PZO22001 Starfinder Player Core 058-073::/page/9/Text/45']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/45` | 0.777771 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/80` | 0.777771 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/45` | 0.777771 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/74` | 0.735771 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/46` | 0.735771 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/84` | 0.735771 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/30` | 0.727771 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/31` | 0.727771 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/25` | 0.727771 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/35` | 0.727771 | **SKILLS** |

### Query 309
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/46']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `12`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/13/Text/47', 'PZO22001 Starfinder Player Core 058-073::/page/15/Text/85', 'PZO22001 Starfinder Player Core 058-073::/page/9/Text/46']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/85` | 0.735680 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/46` | 0.735680 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/47` | 0.735680 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/46` | 0.693680 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/81` | 0.693680 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/75` | 0.693680 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/36` | 0.685680 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/32` | 0.685680 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/26` | 0.685680 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/31` | 0.685680 | **FEATS** |

### Query 310
- Text: Summarize **EQUIPMENT**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/47']
- Expected found: `True`
- Expected rank: `6`
- Graph boost applied: `True`
- Graph boosted count: `10`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/9/Text/47', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/84', 'PZO22001 Starfinder Player Core 058-073::/page/7/Text/76']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/76` | 0.915652 | **EQUIPMENT** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/47` | 0.915652 | **EQUIPMENT** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/84` | 0.915652 | **EQUIPMENT** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/47` | 0.873652 | **EQUIPMENT** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/48` | 0.873652 | **EQUIPMENT** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/47` | 0.873652 | **EQUIPMENT** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/86` | 0.873652 | **EQUIPMENT** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/82` | 0.873652 | **EQUIPMENT** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/27` | 0.865652 | **EQUIPMENT** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/37` | 0.865652 | **EQUIPMENT** |

### Query 311
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/48']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `16`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/83', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/48', 'PZO22001 Starfinder Player Core 058-073::/page/13/Text/49']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/49` | 0.806592 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/83` | 0.806592 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/48` | 0.806592 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/48` | 0.764592 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/85` | 0.764592 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/77` | 0.764592 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/48` | 0.764592 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/33` | 0.756592 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/44` | 0.756592 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/50` | 0.756592 | **SPELLS** |

### Query 312
- Text: Summarize **PLAYING THE ** **GAME**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/49']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `16`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/5/Text/49', 'PZO22001 Starfinder Player Core 058-073::/page/9/Text/49', 'PZO22001 Starfinder Player Core 058-073::/page/13/Text/50']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/49` | 0.938833 | **PLAYING THE ** **GAME** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/49` | 0.938833 | **PLAYING THE ** **GAME** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/50` | 0.938833 | **PLAYING THE ** **GAME** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/49` | 0.896833 | **PLAYING THE ** **GAME** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/84` | 0.896833 | **PLAYING THE ** **GAME** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/78` | 0.896833 | **PLAYING THE ** **GAME** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/34` | 0.888833 | **PLAYING THE ** **GAME** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/34` | 0.888833 | **PLAYING THE ** **GAME** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/42` | 0.888833 | **PLAYING THE ** **GAME** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/39` | 0.888833 | **PLAYING THE ** **GAME** |

### Query 313
- Text: Summarize **CONDITIONS ** **APPENDIX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/50']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `18`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/11/Text/87', 'PZO22001 Starfinder Player Core 058-073::/page/7/Text/79', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/50']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/79` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/87` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/50` | 0.950802 | **CONDITIONS ** **APPENDIX** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/51` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/85` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/50` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/50` | 0.908802 | **CONDITIONS ** **APPENDIX** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/46` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/40` | 0.900802 | **CONDITIONS ** **APPENDIX** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/43` | 0.900802 | **CONDITIONS ** **APPENDIX** |

### Query 314
- Text: Summarize **GLOSSARY & ** **INDEX**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/51']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `16`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/5/Text/51', 'PZO22001 Starfinder Player Core 058-073::/page/9/Text/51', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/51']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/51` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/51` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/51` | 0.929439 | **GLOSSARY & ** **INDEX** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/86` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/80` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/88` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/52` | 0.887439 | **GLOSSARY & ** **INDEX** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/41` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/47` | 0.879439 | **GLOSSARY & ** **INDEX** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/36` | 0.879439 | **GLOSSARY & ** **INDEX** |

### Query 315
- Text: What is the rule about **CHARACTER ** **SHEET**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/52']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `6`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/52', 'PZO22001 Starfinder Player Core 058-073::/page/4/SectionHeader/12', 'PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/52` | 0.834532 | **CHARACTER ** **SHEET** |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/15` | 0.784532 | **CHARACTER ** **SHEET** |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/3/Text/22` | 0.784532 | **CHARACTER ** **SHEET** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/48` | 0.784532 | **CHARACTER ** **SHEET** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/15` | 0.751052 | **CHARACTER SHEET** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/21` | 0.751052 | **CHARACTER SHEET** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/15` | 0.751052 | **CHARACTER SHEET** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/5/SectionHeader/25` | 0.751052 | **CHARACTER SHEET** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/16` | 0.751052 | **CHARACTER SHEET** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/6/SectionHeader/11` | 0.748438 | **CHARACTER SHEET ** |

### Query 316
- Text: Summarize 59
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/53']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `9`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/53', 'PZO22001 Starfinder Player Core 058-073::/page/5/SectionHeader/14', 'PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/53` | 0.770939 | 59 |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/SectionHeader/14` | 0.561652 | SOCIETY |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/5/SectionHeader/14` | 0.561652 | SOCIETY |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/425` | 0.542464 | 9 |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/4/SectionHeader/1` | 0.526352 | **OVERVIEW** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/SectionHeader/10` | 0.523243 | ENVOY EXPERTISE 9TH |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/19` | 0.522477 | STEP 9 |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/417` | 0.522213 | 5 |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/13/SectionHeader/14` | 0.519652 | SOCIETY |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/9/SectionHeader/14` | 0.519652 | SOCIETY |

### Query 317
- Text: What is the rule about In addition to what you gain from your ancestry, you gain an  attribute boost to Strength and an attribute flaw to Wisdom,  but the free ancestry boost can't also be Strength. You gain 8  Hit Points from your ancestry instead of 6, and you gain a +1  circumstance bonus to Athletics checks to Shove or Trip.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `7`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/1', 'PZO22001 Starfinder Player Core 058-073::/page/6/Text/7', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/1` | 0.979918 | In addition to what you gain from your ancestry, you gain an  attribute boost to Strength and an attribute flaw to Wisdom,  but the free ancestry boost can't also be Strength. You gain 8  Hit Points f |
| 2 | `PZO22001 Starfinder Player Core 014-029::/page/10/Text/2` | 0.698542 | The attribute boosts and flaws listed in each ancestry  represent general trends or help guide players to  create the kinds of characters from that ancestry most  likely to pursue the life of an adven |
| 3 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/3` | 0.688086 | **Ancestry:** Each ancestry provides attribute boosts, and sometimes an attribute flaw. If you're taking any voluntary  flaws, apply them in this step (see the sidebar on page 25). |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/7` | 0.652353 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a pahtra, you choose from among the  following an |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/12` | 0.649117 | Attribute flaws are not nearly as common in Starfinder as  attribute boosts. If your character has an attribute flaw likely from their ancestry—you decrease that attribute  modifier by 1. Vesk, for ex |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.647234 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/17` | 0.640215 | Sometimes, it's fun to play a character with a major  flaw regardless of your ancestry. You can elect to take  additional attribute flaws when applying the attribute  boosts and attribute flaws from y |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/9` | 0.638328 | Whenever your character receives an attribute  boost, the source indicates whether it must be applied  to a specific attribute modifier, to one in a limited list,  or whether it's a "free" boost that |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/20` | 0.638003 | modifier, recalculate their maximum Hit  Points using their new Constitution modifier  (typically, this adds 1 Hit Point per level). If  an attribute boost increases your character's  Intelligence mod |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/20` | 0.632699 | Your character's attribute modifiers each start at +0, and as  you select your ancestry, background, and class, you'll apply  attribute boosts, which increase a modifier by 1, and attribute |

### Query 318
- Text: Summarize UNBOUND LASHUNTA
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `43`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/2', 'PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/41']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/2` | 0.890652 | UNBOUND LASHUNTA |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1` | 0.734944 | LASHUNTA |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/41` | 0.713773 | **UNCOMMON** **LASHUNTA** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/30` | 0.659723 | **LASHUNTA** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/20` | 0.659723 | **LASHUNTA** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/11` | 0.659723 | **LASHUNTA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/2` | 0.659723 | **LASHUNTA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/15` | 0.659723 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/24` | 0.659723 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/30` | 0.659723 | **LASHUNTA** |

### Query 319
- Text: What is the rule about You decided against activating your ancestry's adaptive  genetics. You might show a combination of damaya and  korasha traits; you might be tall and muscular or short and  lithe, or perhaps you have unusual features, such as bumps  and swirls covering your body or long, fuzzy antennae. You  gain the Unbound Mind reaction.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/3', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/25', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/27']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/3` | 0.995765 | You decided against activating your ancestry's adaptive  genetics. You might show a combination of damaya and  korasha traits; you might be tall and muscular or short and  lithe, or perhaps you have u |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.713210 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/27` | 0.710794 | You've chosen the adaptive genetics to become a korasha. You  might be stockier and more muscular than other lashuntas. |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/13` | 0.645115 | Around puberty, lashuntas traditionally choose whether  to express damaya or korasha genetics—a decision that  determines their physical development and influences their  potential societal roles. Las |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3` | 0.638925 | Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/12` | 0.586405 | Damayas tend to be tall and graceful with delicate features and  are traditionally pushed toward artistic or intellectual pursuits  and political occupations. Korashas are shorter, more muscular,  and |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/5/ListItem/22` | 0.565594 | Select a heritage from those available within that  ancestry, further defining the traits your character was  born with. |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/3` | 0.565128 | **Ancestry:** Each ancestry provides attribute boosts, and sometimes an attribute flaw. If you're taking any voluntary  flaws, apply them in this step (see the sidebar on page 25). |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/9` | 0.560704 | Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/17` | 0.560130 | Sometimes, it's fun to play a character with a major  flaw regardless of your ancestry. You can elect to take  additional attribute flaws when applying the attribute  boosts and attribute flaws from y |

### Query 320
- Text: What is the rule about **Unbound Mind **[reaction] **Trigger** You attempt a saving throw against  a mental effect, but you haven't rolled yet; **Effect** You refuse  to conform to the will of others, shaking off their attempts  to control you with sheer determination. You gain a +1  circumstance bonus to the triggering saving throw and other  saves against mental effects until the start of your next turn.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/4']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/4', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/17', 'PZO22001 Starfinder Player Core 058-073::/page/9/Text/27']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/4` | 0.986891 | **Unbound Mind **[reaction] **Trigger** You attempt a saving throw against  a mental effect, but you haven't rolled yet; **Effect** You refuse  to conform to the will of others, shaking off their atte |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/17` | 0.788161 | **Trigger** You fail a Will saving throw against a mental effect. You center your thoughts and focus your mind, shaking off  emotional turmoil and harmful mental intrusions. Reroll the  triggering sav |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/27` | 0.734347 | Despite the passage of time, you remain resolute in your  defiance of the Swarm and all forms of mental control. If you  roll a success on a Will saving throw against an effect that  was created by a |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/18` | 0.679818 | You're rarely discouraged or afraid. You gain a +1 circumstance  bonus to saves against fear and to your Will DC against  attempts to Demoralize you. If you get a success on a save  against a fear eff |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/14` | 0.673493 | You push yourself to be the best by competing with the  triggering ally. Until the end of your next turn, you can attempt  the same skill check to perform the same action or activity  that the trigger |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/7` | 0.671450 | **Lead** **by** **Example** If you spends two actions, you Brace For  Impact. You and any ally who Braces for Impact before the  start of your next turn also gain a +1 status bonus to saving  throws a |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/35` | 0.653427 | You warn your ally to move away from danger. You can use  Watch Out before an ally in range attempts a Reflex save in  addition to its original trigger. If you do, the circumstance  bonus applies to t |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/28` | 0.651602 | **Rebellious** **Defiance** [one-action] (mental) **Frequency** once per day;  **Effect** You decry one foe within 100 feet that you can see as  a tyrant or villain and prepare yourself to defy them, |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/12` | 0.644908 | Using your words to influence others is what you do, and you  easily recognize when others attempt to use the same tactics  against you. You gain a +1 status bonus to your Perception DC  against attem |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/57` | 0.644560 | **Trigger** You're targeted by a mental effect. |

### Query 321
- Text: What is the rule about LASHUNTA ANCESTRY  FEATS?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/6']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `45`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/6', 'PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/6` | 0.877052 | LASHUNTA ANCESTRY  FEATS |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1` | 0.709694 | LASHUNTA |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/15` | 0.647641 | **LASHUNTA** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/30` | 0.605641 | **LASHUNTA** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/20` | 0.605641 | **LASHUNTA** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/11` | 0.605641 | **LASHUNTA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/7` | 0.605641 | **LASHUNTA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/30` | 0.605641 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/20` | 0.605641 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/24` | 0.605641 | **LASHUNTA** |

### Query 322
- Text: What is the rule about At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a lashunta, you choose from among  the following ancestry feats.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/7']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `15`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/7', 'PZO22001 Starfinder Player Core 058-073::/page/6/Text/7', 'PZO22001 Starfinder Player Core 058-073::/page/10/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/7` | 0.983831 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a lashunta, you choose from among  the following |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/7` | 0.907000 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a pahtra, you choose from among the  following an |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/11` | 0.872384 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a shirren, you choose from among the  following a |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/7` | 0.821259 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a skittermander, you choose from  among the follo |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/14` | 0.804882 | In addition to the initial ancestry feat you started with, you  gain an ancestry feat at 5th level and every 4 levels thereafter. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/26` | 0.728503 | This section serves as a reminder of the ancestry feats your  character gains at 5th, 9th, 13th, and 17th levels. Ancestry  feats are detailed in each ancestry entry in Chapter 2, which  begins on pag |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/23` | 0.671213 | Around puberty, many lashuntas choose to embrace a genetic  path that determines their physiology and role in society.  Choose one of the following lashunta heritages at 1st level. |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/15/ListItem/16` | 0.662266 | Select feats as indicated on your class advancement  table. For ancestry feats, see Chapter 2. For class  feats, see your class entry in Chapter 3. For general  feats and skill feats, see Chapter 5. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.657094 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/10` | 0.655447 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |

### Query 323
- Text: Summarize 1ST LEVEL
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/8']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/8', 'PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/8', 'PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/8']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/8` | 0.853644 | 1ST LEVEL |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/8` | 0.853644 | 1ST LEVEL |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/8` | 0.853644 | 1ST LEVEL |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/12` | 0.811644 | 1ST LEVEL |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/16` | 0.803644 | 1ST LEVEL |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/7` | 0.637047 | At 1st level, you gain a number of proficiencies that represent  your basic training. These proficiencies are noted at the start  of this class. |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/3` | 0.626419 | STEPS 1 AND 2 |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/3/SectionHeader/7` | 0.618847 | STEP 1: CREATE A CONCEPT |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/Table/4` | 0.616541 | 2ND LEVEL |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/11/TableCell/584` | 0.616541 | 2ND LEVEL |

### Query 324
- Text: What are the requirements for **ALLURING PHEROMONES** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `31`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/9', 'PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/18', 'PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/9` | 0.802615 | **ALLURING PHEROMONES** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/18` | 0.725225 | **COMMANDING PHEROMONES** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26` | 0.633426 | **HYPER** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/28` | 0.566619 | **LASHUNTA LORE** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/29` | 0.549795 | **SKITTERMANDER LORE** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/1` | 0.549065 | **SHIRREN LORE** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/3` | 0.548770 | **PREDATORY** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/15` | 0.548616 | **DAUNTLESS** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/34` | 0.548312 | **FOCUS PHEROMONES **[one-action] **FEAT 13** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/21` | 0.545851 | **PARDON ME** **FEAT 1** |

### Query 325
- Text: Summarize **LASHUNTA**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/11']
- Expected found: `True`
- Expected rank: `11`
- Graph boost applied: `True`
- Graph boosted count: `41`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/7', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/2', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/7` | 0.887783 | **LASHUNTA** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/2` | 0.887783 | **LASHUNTA** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/11` | 0.887783 | **LASHUNTA** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/20` | 0.845783 | **LASHUNTA** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/47` | 0.845783 | **LASHUNTA** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/26` | 0.845783 | **LASHUNTA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/30` | 0.845783 | **LASHUNTA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/15` | 0.845783 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/30` | 0.845783 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/24` | 0.845783 | **LASHUNTA** |

### Query 326
- Text: What is the rule about You influence others with pheromones, even when you lack  other means of communication. You can use Diplomacy  to Make an Impression on creatures with whom you don't  share a language and to make simple Requests of them. This  could include getting directions or getting the target to pick a  specific individual out from a crowd. When you do, Make an  Impression and Request lose the linguistic trait and gain the  olfactory trait.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/12', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/21', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/38']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/12` | 0.988726 | You influence others with pheromones, even when you lack  other means of communication. You can use Diplomacy  to Make an Impression on creatures with whom you don't  share a language and to make simp |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/21` | 0.759337 | You can leverage your alluring pheromones to soothe ill will  and take the edge off your threats, turning your attempts  at coercion into acts of leadership. When you Coerce a  creature, if your targe |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/38` | 0.735915 | You can purposefully deploy your pheromones to manipulate  the reactions of those around you. If your next action is to  attempt a Deception check to Create a Diversion, a Diplomacy  check to Request, |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/34` | 0.636896 | With masterful timing and a careful choice of words, you  can manipulate the emotions and thoughts of others. You  roll the triggering Deception, Diplomacy, or Intimidation  check twice, and use the h |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/8` | 0.619455 | **Prerequisites** korasha lashunta or unbound lashunta heritage You can leverage your telepathic abilities to influence the  minds of others, imparting orders or inflaming fears. You can  cast *comman |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/18` | 0.612525 | Whether through conversation, clever lies, dazzling  performances, or threats, you rely on charm and cunning to  influence others. You crave being in the spotlight. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/9` | 0.607821 | Envoys encourage their allies with directives. A directive is  an order that benefits allies who follow it. Envoy directives  include a way for the envoy to lead by example by spending  more actions f |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/25` | 0.606688 | Your telepathy is stronger than most shirrens', allowing you to  combine physical, verbal, and telepathic communication. You  can transmit emotions alongside your messages whenever  you use limited te |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/46` | 0.602894 | Your mastery of language reaches supernatural levels. You can  cast *truespeech* as a 5th-rank occult innate spell once per day on  yourself only. You gain a +1 status bonus to Diplomacy checks  for t |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/12` | 0.590983 | Using your words to influence others is what you do, and you  easily recognize when others attempt to use the same tactics  against you. You gain a +1 status bonus to your Perception DC  against attem |

### Query 327
- Text: What are the requirements for **CENTER THOUGHTS **[free-action] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/13', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/55', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/48']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/13` | 0.865612 | **CENTER THOUGHTS **[free-action] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/55` | 0.669906 | **Requirements** You have at least 1 Focus Point. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/48` | 0.658692 | **Prerequisites** Center Thoughts |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/9` | 0.606287 | **COMPETITIVE SPIRIT **[reaction] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/45` | 0.600191 | **CENTERED MIND** **FEAT 17** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.599449 | **WATCH OUT **[reaction] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26` | 0.594622 | **HYPER** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.592944 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/29` | 0.590960 | **PSYCHIC TALENT** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/1` | 0.590960 | **PSYCHIC TALENT** **FEAT 1** |

### Query 328
- Text: Summarize **CONCENTRATE** **FORTUNE** **LASHUNTA** **MENTAL**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `35`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/15', 'PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/15', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/52']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/15` | 1.002572 | **CONCENTRATE** **FORTUNE** **LASHUNTA** **MENTAL** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/15` | 0.838473 | **CONCENTRATE** **FORTUNE** **SHIRREN** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/52` | 0.833339 | **LASHUNTA** **MENTAL** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/36` | 0.758887 | **FORTUNE** **LASHUNTA** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/42` | 0.713821 | **CONCENTRATE** **ENVOY** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/31` | 0.700784 | **CONCENTRATE** **ENVOY** **EXPLORATION** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/30` | 0.684971 | **LASHUNTA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/30` | 0.684971 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/15` | 0.684971 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/20` | 0.684971 | **LASHUNTA** |

### Query 329
- Text: Summarize **Frequency** once per day
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/16']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `18`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/35', 'PZO22001 Starfinder Player Core 058-073::/page/15/Text/21', 'PZO22001 Starfinder Player Core 058-073::/page/15/Text/57']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/35` | 0.887553 | **Frequency** once per day |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/21` | 0.887553 | **Frequency** once per day |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/57` | 0.887553 | **Frequency** once per day |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/16` | 0.845553 | **Frequency** once per day |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/56` | 0.845553 | **Frequency** once per day |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/16` | 0.845553 | **Frequency** once per day |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/19` | 0.837553 | **Frequency** once per day |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/32` | 0.818844 | **Frequency **once per day |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/12` | 0.807714 | **Frequency** once per hour |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/27` | 0.807714 | **Frequency** once per hour |

### Query 330
- Text: What is the rule about **Trigger** You fail a Will saving throw against a mental effect. You center your thoughts and focus your mind, shaking off  emotional turmoil and harmful mental intrusions. Reroll the  triggering saving throw and use the better result.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/17', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/4', 'PZO22001 Starfinder Player Core 058-073::/page/9/Text/27']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/17` | 0.975873 | **Trigger** You fail a Will saving throw against a mental effect. You center your thoughts and focus your mind, shaking off  emotional turmoil and harmful mental intrusions. Reroll the  triggering sav |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/4` | 0.787532 | **Unbound Mind **[reaction] **Trigger** You attempt a saving throw against  a mental effect, but you haven't rolled yet; **Effect** You refuse  to conform to the will of others, shaking off their atte |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/27` | 0.688321 | Despite the passage of time, you remain resolute in your  defiance of the Swarm and all forms of mental control. If you  roll a success on a Will saving throw against an effect that  was created by a |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/13` | 0.664977 | You've become an expert at veiling your schemes. When a  creature rolls a critical success to Sense Motive against you,  or a skill check to Gather Information or Recall Knowledge  about your secrets, |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/13` | 0.664331 | You can reroll the triggering skill check and use the better result. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/33` | 0.656379 | Your ambition and stubbornness grant you mental resiliency.  Your proficiency rank for Will saves increases to legendary.  When you roll a success on a Will save, you get a critical  success instead. |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/37` | 0.640039 | It's nigh impossible for your enemies to unravel your schemes  or your long-term plans. When a creature rolls a critical success  or success on a Perception check to Sense Motive against you,  or on a |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/18` | 0.639619 | You broadcast helpful encouragement or pertinent information  to your ally's mind. Your ally rerolls the triggering skill check and  takes the better result. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/17` | 0.626917 | You've strengthened your mind with an inner reservoir of  determination. Your proficiency rank for Will saves increases  to master. When you roll a success on a Will save, you get a  critical success |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/57` | 0.623948 | **Trigger** You're targeted by a mental effect. |

### Query 331
- Text: What are the requirements for **COMMANDING PHEROMONES** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `32`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/18', 'PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/9', 'PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/18` | 0.818642 | **COMMANDING PHEROMONES** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/9` | 0.734715 | **ALLURING PHEROMONES** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26` | 0.648291 | **HYPER** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/21` | 0.569720 | **PARDON ME** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/25` | 0.568782 | **LINGUISTIC PRODIGY** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/22` | 0.564511 | **DISTANT TELEPATH** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/19` | 0.564511 | **DISTANT TELEPATH** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/34` | 0.563673 | **FOCUS PHEROMONES **[one-action] **FEAT 13** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/3` | 0.560543 | **PREDATORY** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/29` | 0.558800 | **PSYCHIC TALENT** **FEAT 1** |

### Query 332
- Text: Summarize **LASHUNTA**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/20']
- Expected found: `True`
- Expected rank: `12`
- Graph boost applied: `True`
- Graph boosted count: `41`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/7', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/2', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/7` | 0.887783 | **LASHUNTA** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/2` | 0.887783 | **LASHUNTA** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/11` | 0.887783 | **LASHUNTA** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/20` | 0.845783 | **LASHUNTA** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/47` | 0.845783 | **LASHUNTA** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/26` | 0.845783 | **LASHUNTA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/30` | 0.845783 | **LASHUNTA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/15` | 0.845783 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/30` | 0.845783 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/24` | 0.845783 | **LASHUNTA** |

### Query 333
- Text: What is the rule about You can leverage your alluring pheromones to soothe ill will  and take the edge off your threats, turning your attempts  at coercion into acts of leadership. When you Coerce a  creature, if your target would become unfriendly (and they  aren't already unfriendly or hostile), they become indifferent  instead.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `14`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/21', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/12', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/38']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/21` | 0.982891 | You can leverage your alluring pheromones to soothe ill will  and take the edge off your threats, turning your attempts  at coercion into acts of leadership. When you Coerce a  creature, if your targe |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/12` | 0.756569 | You influence others with pheromones, even when you lack  other means of communication. You can use Diplomacy  to Make an Impression on creatures with whom you don't  share a language and to make simp |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/38` | 0.732913 | You can purposefully deploy your pheromones to manipulate  the reactions of those around you. If your next action is to  attempt a Deception check to Create a Diversion, a Diplomacy  check to Request, |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/21` | 0.649054 | You encourage an adjacent ally to overcome their minor  ailments by patting them on the back, providing them useful  advice, or offering some form of comfort or inspiration. The  target reduces the va |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/11` | 0.632418 | You issue directives to your allies, granting benefits and letting you take the lead.  Your words and deeds bolster your allies or harry your foes, and your cunning can  get you and your team out of d |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/27` | 0.626157 | Despite the passage of time, you remain resolute in your  defiance of the Swarm and all forms of mental control. If you  roll a success on a Will saving throw against an effect that  was created by a |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/24` | 0.611537 | You wave your arms to shield your face from harm and  cower, acting meek and pitiful. Attempt a Deception check  against the triggering creature's Will DC. The triggering  creature is then immune to N |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/13/Text/26` | 0.604258 | You attempt to enthrall a foe with a convoluted and  utterly pointless monologue that leaves your audience  dumbfounded. Attempt a Deception or Diplomacy check  against the Will DC of a single creatur |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/15` | 0.600196 | People follow your lead because you help push them to  their ultimate potential. Each of your allies gain a second  reaction if they start their turn within 100 feet of you and  can perceive you. This |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/39` | 0.599517 | You urge your allies to take down your enemies without  incurring any loss of life. Until the beginning of your next  turn, you and your allies can add the nonlethal trait (page  399) to your attacks |

### Query 334
- Text: What are the requirements for **DISTANT TELEPATH** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `40`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/22', 'PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/19', 'PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/22` | 0.859296 | **DISTANT TELEPATH** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/19` | 0.859296 | **DISTANT TELEPATH** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26` | 0.640552 | **HYPER** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/2` | 0.597116 | **DISTANT FEINT** **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/21` | 0.591601 | **Prerequisites** limited telepathy |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/25` | 0.591601 | **Prerequisites** limited telepathy |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22` | 0.591601 | **Prerequisites** limited telepathy |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/23` | 0.591601 | **Prerequisites** limited telepathy |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/23` | 0.574667 | Whether through training or innate talent,  you've expanded the range at which you can  telepathically communicate. Increase the range of  your limited telepathy by 15 feet. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/26` | 0.574667 | Whether through training or innate talent, you've expanded  the range at which you can telepathically communicate.  Increase the range of your limited telepathy by 15 feet. |

### Query 335
- Text: Summarize **LASHUNTA**
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/24']
- Expected found: `True`
- Expected rank: `10`
- Graph boost applied: `True`
- Graph boosted count: `41`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/7', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/2', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/11']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/7` | 0.887783 | **LASHUNTA** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/2` | 0.887783 | **LASHUNTA** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/11` | 0.887783 | **LASHUNTA** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/20` | 0.845783 | **LASHUNTA** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/47` | 0.845783 | **LASHUNTA** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/26` | 0.845783 | **LASHUNTA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/30` | 0.845783 | **LASHUNTA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/15` | 0.845783 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/30` | 0.845783 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/24` | 0.845783 | **LASHUNTA** |

### Query 336
- Text: What are the requirements for **Prerequisites** limited telepathy?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/25']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `33`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/25', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/21` | 0.917483 | **Prerequisites** limited telepathy |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/25` | 0.917483 | **Prerequisites** limited telepathy |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22` | 0.917483 | **Prerequisites** limited telepathy |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/23` | 0.875483 | **Prerequisites** limited telepathy |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/12` | 0.706373 | LIMITED TELEPATHY |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/14` | 0.706373 | LIMITED TELEPATHY |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/23` | 0.613649 | Whether through training or innate talent,  you've expanded the range at which you can  telepathically communicate. Increase the range of  your limited telepathy by 15 feet. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/26` | 0.613649 | Whether through training or innate talent, you've expanded  the range at which you can telepathically communicate.  Increase the range of your limited telepathy by 15 feet. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.611281 | **Prerequisites** Psychic Talent |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.611281 | **Prerequisites** Psychic Talent |

### Query 337
- Text: What is the rule about **Special** You can select this feat more than once.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `13`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/27', 'PZO22001 Starfinder Player Core 058-073::/page/10/Text/24', 'PZO22001 Starfinder Player Core 058-073::/page/7/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/27` | 0.860951 | **Special** You can select this feat more than once. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/24` | 0.860951 | **Special** You can select this feat more than once. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/9` | 0.723980 | **Special** You can take this feat a second time. If you do, select  the other attack from the options above. |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/17` | 0.711571 | **Special** Any special qualities of the rule are explained in  this section. Usually this section appears in feats you  can select more than once, explaining what happens  when you do. |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/4` | 0.618843 | **Flourish**: Actions with this trait are special  techniques that require too much exertion for you to  perform frequently. You can use only 1 action with the  flourish trait per turn. |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/7/Text/47` | 0.602914 | At 2nd level and every 2 levels thereafter, you gain a skill feat.  You must be trained or better in the corresponding skill to  select a skill feat. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/11` | 0.558002 | **Beginner's** **Luck** [free-action] (fortune) **Frequency** once per day;  **Trigger** You fail a skill check using a skill that you're  untrained in; **Effect** Reroll the triggering check and use |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/13` | 0.553869 | required level next to the ability's name. All classes include  the class features detailed below, and each class also gets  special class features specific to it. Many class features  require you to |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/6` | 0.550065 | With exceptional flair, you can repeat your orders with a  single word or gesture. You immediately issue the 1-action  version of the directive that you issued on your previous  turn. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/15` | 0.549917 | At every level that you gain an envoy feat, you can select  one of the following feats. You must satisfy any prerequisites  before selecting the feat. |

### Query 338
- Text: What are the requirements for **LASHUNTA LORE** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `48`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/28', 'PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/29', 'PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/28` | 0.816423 | **LASHUNTA LORE** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/29` | 0.672669 | **SKITTERMANDER LORE** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/1` | 0.671404 | LASHUNTA |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/30` | 0.637476 | **LASHUNTA** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/2` | 0.625476 | **LASHUNTA** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/7` | 0.625476 | **LASHUNTA** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/11` | 0.625476 | **LASHUNTA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/47` | 0.625476 | **LASHUNTA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/30` | 0.625476 | **LASHUNTA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/26` | 0.625476 | **LASHUNTA** |

### Query 339
- Text: What is the rule about You've studied the lives and achievements of other  lashuntas who have improved both their psychic powers  and their communities. You gain the trained proficiency  rank in Occultism and Society. If you would automatically  become trained in one of those skills (from your background  or class, for example), you instead become trained in a skill  of your choice.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/31', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/4', 'PZO22001 Starfinder Player Core 058-073::/page/14/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/31` | 0.985219 | You've studied the lives and achievements of other  lashuntas who have improved both their psychic powers  and their communities. You gain the trained proficiency  rank in Occultism and Society. If yo |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/4` | 0.779237 | Your ability to adapt to various beliefs instills you with  knowledge of many cultures. You gain the trained proficiency  rank in Diplomacy and Society. If you would automatically  become trained in o |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/32` | 0.716694 | You're gregarious and friendly but also passionately  interested in the history of your people, going out of  your way to learn traditional stories and unearth  lost secrets. You gain the trained prof |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/1` | 0.669967 | performing arts. You gain the trained proficiency rank in  Acrobatics and Performance. If you would automatically become  trained in one of those skills (from your background or class, for  example), |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.646803 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/9` | 0.642311 | Lashuntas are natural psychics with adaptive genetics who  traditionally develop into one of two heritages at puberty:  damayas or korashas. They have a well-earned reputation for  being charismatic, |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/6` | 0.633030 | A proficiency rank can unlock various feats and class  features, and it also helps determine the modifier for any  check you roll or DC you calculate related to that statistic.  If your character is t |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.632898 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/10` | 0.632760 | If you're trained in all martial weapons, you can instead  choose an uncommon advanced weapon that has an ancestry's  trait or is common in another culture. You gain access to that  weapon and have fa |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/2` | 0.632059 | Long ago, lashuntas evolved psychic abilities and a unique dimorphism that helped them survive on their home world of Castrovel. In modern times, lashuntas manipulate their own genetics at puberty, al |

### Query 340
- Text: What is the rule about You also gain the Additional Lore general feat for  Lashunta Lore.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `37`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/Text/32', 'PZO22001 Starfinder Player Core 058-073::/page/7/Text/2', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/32` | 0.927467 | You also gain the Additional Lore general feat for  Lashunta Lore. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/2` | 0.810272 | You also gain the Additional Lore general feat for Pahtra Lore. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/5` | 0.793714 | You also gain the Additional Lore general feat for Shirren Lore. |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/33` | 0.588402 | You also gain the Additional Lore general feat for  Skittermander Lore, and you learn Morandomandranan,  the original skittermander language that has long been  suppressed by the Veskarium. |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/7` | 0.565460 | At 1st level, you gain one ancestry feat, and you gain an  additional ancestry feat every 4 levels thereafter (at 5th, 9th,  13th, and 17th level). As a lashunta, you choose from among  the following |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/21` | 0.560839 | You're fascinated with a particular topic, such as the  religion of a small sect of worshippers, the process of  spaghettification, or the songs sung by asterays. You gain  the Additional Lore feat an |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/25` | 0.549558 | You've chosen the adaptive genetics to become a damaya. You  might have a leaner, lither body type than other lashuntas and  are likely encouraged to pursue work as a scholar or politician.  In additi |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/10` | 0.535462 | At 3rd level and every 4 levels thereafter, you gain a general  feat. General feats are listed in Chapter 5. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/6/TableCell/446` | 0.532266 | General feat, light armor mastery, silver tongue, skill increase |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/6` | 0.520078 | LASHUNTA ANCESTRY  FEATS |

### Query 341
- Text: What are the requirements for **PSYCHIC TALENT** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/1']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `30`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/1', 'PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/29', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/1` | 0.789536 | **PSYCHIC TALENT** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/29` | 0.789536 | **PSYCHIC TALENT** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.751005 | **Prerequisites** Psychic Talent |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.709005 | **Prerequisites** Psychic Talent |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/42` | 0.655121 | **Prerequisites** Psychic Bully, Psychic Scholar, or Psychic Talent |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.602853 | **Prerequisites** Psychic Mastery |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/9` | 0.583140 | **PSYCHIC SCHOLAR** **FEAT 5** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/25` | 0.577480 | **Prerequisites** adaptive talent |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26` | 0.573737 | **HYPER** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/25` | 0.573662 | **LINGUISTIC PRODIGY** **FEAT 1** |

### Query 342
- Text: What is the rule about Your psychic abilities have developed beyond simple  communication. Choose one cantrip from the occult spell list. You  can cast this cantrip as an occult innate spell at will. A cantrip is  heightened to a spell rank equal to half your level rounded up.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/3', 'PZO22001 Starfinder Player Core 058-073::/page/10/Text/32', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/3` | 0.972906 | Your psychic abilities have developed beyond simple  communication. Choose one cantrip from the occult spell list. You  can cast this cantrip as an occult innate spell at will. A cantrip is  heightene |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/32` | 0.972906 | Your psychic abilities have developed beyond simple  communication. Choose one cantrip from the occult spell list. You  can cast this cantrip as an occult innate spell at will. A cantrip is  heightene |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/32` | 0.806461 | Your psychic abilities have grown stronger, allowing you to  tap into entirely new dimensions of psychic power. Choose  one common 2nd-rank spell from the occult spell list. You can  cast that spell a |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/36` | 0.751468 | Your psychic abilities have grown stronger. Choose one  common 2nd-rank spell from the occult spell list. You can cast  that spell as an occult innate spell once per day. |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/61` | 0.739472 | Your psychic abilities have grown stronger. Choose one  common 6th-rank spell from the occult spell list. You can cast  that spell as an occult innate spell once per day. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/46` | 0.691732 | Your mastery of language reaches supernatural levels. You can  cast *truespeech* as a 5th-rank occult innate spell once per day on  yourself only. You gain a +1 status bonus to Diplomacy checks  for t |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/43` | 0.652727 | You can use your telepathic abilities to quickly assess your  circumstances or subtly glean information from the minds of  others. You can cast *hypercognition* and *mind reading* as 3rdrank occult in |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/8` | 0.649222 | **Prerequisites** korasha lashunta or unbound lashunta heritage You can leverage your telepathic abilities to influence the  minds of others, imparting orders or inflaming fears. You can  cast *comman |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/11/Text/19` | 0.632175 | Many characters can learn a few cantrips or focus spells,  but the mystic and witchwarper gain spellcasting—the  ability to cast a wide variety of spells. If your character's  class grants spells, you |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/12` | 0.620746 | **Prerequisites** damaya lashunta or unbound lashunta heritage You can transfer vast amounts of information to the minds of  others in mere moments. You can cast *mindlink* as a 1st-rank  occult innat |

### Query 343
- Text: What are the requirements for **PSYCHIC BULLY** **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/5']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `31`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/5', 'PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/9', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/5` | 0.802741 | **PSYCHIC BULLY** **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/9` | 0.688499 | **PSYCHIC SCHOLAR** **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/42` | 0.682355 | **Prerequisites** Psychic Bully, Psychic Scholar, or Psychic Talent |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.585693 | **Prerequisites** Psychic Talent |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.585693 | **Prerequisites** Psychic Talent |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/4` | 0.572221 | 5TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.569604 | **Prerequisites** Psychic Mastery |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/14` | 0.562117 | **CLIMBING CLAWS** **FEAT 5** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/11` | 0.560221 | 5TH LEVEL |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/34` | 0.560221 | 5TH LEVEL |

### Query 344
- Text: What are the requirements for **Prerequisites** korasha lashunta or unbound lashunta heritage You can leverage your telepathic abilities to influence the  minds of others, imparting orders or inflaming fears. You can  cast *command* and *fear* as 1st-rank occult innate spells. You  can cast each of these occult innate spells once per day.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/8']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `36`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/8', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/12', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/8` | 0.997829 | **Prerequisites** korasha lashunta or unbound lashunta heritage You can leverage your telepathic abilities to influence the  minds of others, imparting orders or inflaming fears. You can  cast *comman |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/12` | 0.797765 | **Prerequisites** damaya lashunta or unbound lashunta heritage You can transfer vast amounts of information to the minds of  others in mere moments. You can cast *mindlink* as a 1st-rank  occult innat |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/43` | 0.754482 | You can use your telepathic abilities to quickly assess your  circumstances or subtly glean information from the minds of  others. You can cast *hypercognition* and *mind reading* as 3rdrank occult in |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/46` | 0.675082 | Your mastery of language reaches supernatural levels. You can  cast *truespeech* as a 5th-rank occult innate spell once per day on  yourself only. You gain a +1 status bonus to Diplomacy checks  for t |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/32` | 0.673519 | Your psychic abilities have grown stronger, allowing you to  tap into entirely new dimensions of psychic power. Choose  one common 2nd-rank spell from the occult spell list. You can  cast that spell a |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/36` | 0.667447 | Your psychic abilities have grown stronger. Choose one  common 2nd-rank spell from the occult spell list. You can cast  that spell as an occult innate spell once per day. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/61` | 0.659337 | Your psychic abilities have grown stronger. Choose one  common 6th-rank spell from the occult spell list. You can cast  that spell as an occult innate spell once per day. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/13` | 0.629460 | You're an accomplished battledancer and warrior, blessed  by seers, honed by ancestral tradition, and capable of feats  beyond the natural abilities of your peers. You gain *tailwind* as  a 1st-rank p |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/1/ListItem/3` | 0.623548 | Prioritize learning and diplomacy if you're a damaya, or  physique and tactical prowess if you're a korasha—or if  you're an unbound lashunta, you have different priorities. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/32` | 0.623045 | Your psychic abilities have developed beyond simple  communication. Choose one cantrip from the occult spell list. You  can cast this cantrip as an occult innate spell at will. A cantrip is  heightene |

### Query 345
- Text: What are the requirements for **PSYCHIC SCHOLAR** **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/9', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/42', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/5']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/9` | 0.771886 | **PSYCHIC SCHOLAR** **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/42` | 0.678881 | **Prerequisites** Psychic Bully, Psychic Scholar, or Psychic Talent |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/5` | 0.666414 | **PSYCHIC BULLY** **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/4` | 0.595246 | 5TH LEVEL |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.595122 | **Prerequisites** Psychic Talent |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.595122 | **Prerequisites** Psychic Talent |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.588851 | **Prerequisites** Psychic Mastery |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/10` | 0.583246 | 5TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/11` | 0.583246 | 5TH LEVEL |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/34` | 0.583246 | 5TH LEVEL |

### Query 346
- Text: What are the requirements for **Prerequisites** damaya lashunta or unbound lashunta heritage You can transfer vast amounts of information to the minds of  others in mere moments. You can cast *mindlink* as a 1st-rank  occult innate spell twice per day.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/12']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `34`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/12', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/8', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/43']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/12` | 0.998077 | **Prerequisites** damaya lashunta or unbound lashunta heritage You can transfer vast amounts of information to the minds of  others in mere moments. You can cast *mindlink* as a 1st-rank  occult innat |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/8` | 0.787080 | **Prerequisites** korasha lashunta or unbound lashunta heritage You can leverage your telepathic abilities to influence the  minds of others, imparting orders or inflaming fears. You can  cast *comman |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/43` | 0.719066 | You can use your telepathic abilities to quickly assess your  circumstances or subtly glean information from the minds of  others. You can cast *hypercognition* and *mind reading* as 3rdrank occult in |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/32` | 0.644605 | Your psychic abilities have grown stronger, allowing you to  tap into entirely new dimensions of psychic power. Choose  one common 2nd-rank spell from the occult spell list. You can  cast that spell a |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/46` | 0.637839 | Your mastery of language reaches supernatural levels. You can  cast *truespeech* as a 5th-rank occult innate spell once per day on  yourself only. You gain a +1 status bonus to Diplomacy checks  for t |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/36` | 0.628600 | Your psychic abilities have grown stronger. Choose one  common 2nd-rank spell from the occult spell list. You can cast  that spell as an occult innate spell once per day. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/61` | 0.606177 | Your psychic abilities have grown stronger. Choose one  common 6th-rank spell from the occult spell list. You can cast  that spell as an occult innate spell once per day. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/3` | 0.604580 | Your psychic abilities have developed beyond simple  communication. Choose one cantrip from the occult spell list. You  can cast this cantrip as an occult innate spell at will. A cantrip is  heightene |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/32` | 0.604580 | Your psychic abilities have developed beyond simple  communication. Choose one cantrip from the occult spell list. You  can cast this cantrip as an occult innate spell at will. A cantrip is  heightene |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/13` | 0.599735 | You're an accomplished battledancer and warrior, blessed  by seers, honed by ancestral tradition, and capable of feats  beyond the natural abilities of your peers. You gain *tailwind* as  a 1st-rank p |

### Query 347
- Text: What are the requirements for **SENSITIVE ANTENNAE** **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `34`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/13', 'PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/14', 'PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/13` | 0.845681 | **SENSITIVE ANTENNAE** **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/14` | 0.622478 | **CLIMBING CLAWS** **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/12` | 0.607455 | **EAGER ASSISTANT** **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/17` | 0.564855 | **ELECTROMAGNETIC WHISKERS** **FEAT 5** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/11` | 0.559019 | 5TH LEVEL |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/20` | 0.558518 | **TELEPATHIC CONDUIT** **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/18` | 0.558518 | **TELEPATHIC CONDUIT** **FEAT 5** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/15` | 0.558464 | **HARMONIC SENSITIVITY** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/8/SectionHeader/22` | 0.555536 | PERCEPTION EXPERTISE 5TH |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/7` | 0.554629 | **LUCKY IMPROVISER** **FEAT 5** |

### Query 348
- Text: What are the requirements for **TELEPATHIC CONDUIT** **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/18']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `41`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/18', 'PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/20', 'PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/19']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/18` | 0.804080 | **TELEPATHIC CONDUIT** **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/20` | 0.804080 | **TELEPATHIC CONDUIT** **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/19` | 0.669693 | **DISTANT TELEPATH** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/22` | 0.627693 | **DISTANT TELEPATH** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/13` | 0.620727 | **SENSITIVE ANTENNAE** **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/14` | 0.597522 | **CLIMBING CLAWS** **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/9` | 0.583945 | STEP 5 |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/16` | 0.580595 | **LEARNING EXPERIENCE** **FEAT 5** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/25` | 0.575719 | **Prerequisites** limited telepathy |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22` | 0.575719 | **Prerequisites** limited telepathy |

### Query 349
- Text: What are the requirements for **Prerequisites** limited telepathy?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/21']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `33`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/25', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/21` | 0.917483 | **Prerequisites** limited telepathy |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/25` | 0.917483 | **Prerequisites** limited telepathy |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22` | 0.917483 | **Prerequisites** limited telepathy |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/23` | 0.875483 | **Prerequisites** limited telepathy |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/12` | 0.706373 | LIMITED TELEPATHY |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/14` | 0.706373 | LIMITED TELEPATHY |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/23` | 0.613649 | Whether through training or innate talent,  you've expanded the range at which you can  telepathically communicate. Increase the range of  your limited telepathy by 15 feet. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/26` | 0.613649 | Whether through training or innate talent, you've expanded  the range at which you can telepathically communicate.  Increase the range of your limited telepathy by 15 feet. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.611281 | **Prerequisites** Psychic Talent |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.611281 | **Prerequisites** Psychic Talent |

### Query 350
- Text: What is the rule about When you use limited telepathy to communicate with another  creature, you act as a conduit for their thoughts, allowing them  to respond to you for a few scant moments—if they wish. The  creature can give you a brief response as a reaction, or as a  free action at the beginning of their next turn as long as they  remain within range of your telepathy.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/22', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/24', 'PZO22001 Starfinder Player Core 058-073::/page/9/Text/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/22` | 0.974771 | When you use limited telepathy to communicate with another  creature, you act as a conduit for their thoughts, allowing them  to respond to you for a few scant moments—if they wish. The  creature can |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/24` | 0.908311 | When you use limited telepathy to communicate with another  creature, the creature can give you a brief response as a reaction,  or as a free action at the beginning of their next turn. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/25` | 0.730794 | Your telepathy is stronger than most shirrens', allowing you to  combine physical, verbal, and telepathic communication. You  can transmit emotions alongside your messages whenever  you use limited te |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/13` | 0.684197 | You can communicate mentally with creatures within 30 feet. You can communicate only with creatures that share a language with you. This doesn't give you any access to their thoughts and communicates |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/8/Text/15` | 0.684197 | You can communicate mentally with creatures within 30 feet. You can communicate only with creatures that share a language with you. This doesn't give you any access to their thoughts and communicates |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/23` | 0.658426 | Whether through training or innate talent,  you've expanded the range at which you can  telepathically communicate. Increase the range of  your limited telepathy by 15 feet. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/26` | 0.658426 | Whether through training or innate talent, you've expanded  the range at which you can telepathically communicate.  Increase the range of your limited telepathy by 15 feet. |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/12` | 0.610049 | Reactions use this symbol: [reaction]. These actions can be used even  when it's not your turn. You only get one reaction per encounter  round, and you can use it only when its specific trigger is  fu |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/16` | 0.609945 | Your antennae are covered in fine hairs that make them  more sensitive to psychic vibrations than most. You gain  thoughtsense as a vague sense with a range of 30 feet. This  means you can use your an |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/23` | 0.604127 | **Prerequisites** limited telepathy |

### Query 351
- Text: What are the requirements for **GUARDED THOUGHTS** **FEAT 9**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/24', 'PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/28', 'PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/23']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/24` | 0.785097 | **GUARDED THOUGHTS** **FEAT 9** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/28` | 0.650446 | **PSYCHIC MASTERY** **FEAT 9** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/23` | 0.649643 | 9TH LEVEL |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/12` | 0.607643 | 9TH LEVEL |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/25` | 0.607643 | 9TH LEVEL |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/21` | 0.607643 | 9TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/19` | 0.602496 | STEP 9 |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/32` | 0.601061 | **PSYCHIC MASTER** **FEAT 9** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/9/SectionHeader/12` | 0.589296 | HIDDEN AGENDA 9TH |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/22` | 0.588064 | **HARMONIC SHIELDING** **FEAT 9** |

### Query 352
- Text: What is the rule about Your psychic training allows you to block attempts to read  your thoughts. Any effect that specifically attempts to read  your mind to glean information must succeed at a counteract  check against the higher of your class DC or your spell DC  to do so successfully; otherwise, it gains no information. The  counteract rank is equal to half your level rounded up.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/27']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `21`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/27', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/56', 'PZO22001 Starfinder Player Core 058-073::/page/6/Text/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/27` | 1.011352 | Your psychic training allows you to block attempts to read  your thoughts. Any effect that specifically attempts to read  your mind to glean information must succeed at a counteract  check against the |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/56` | 0.769345 | When a foe Casts a Spell that has the mental trait and you can  see or otherwise detect its manifestations, you use your psychic  powers to disrupt it. You expend 1 Focus Point to counter the  trigger |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/14` | 0.666300 | You push yourself to be the best by competing with the  triggering ally. Until the end of your next turn, you can attempt  the same skill check to perform the same action or activity  that the trigger |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/12` | 0.645727 | Using your words to influence others is what you do, and you  easily recognize when others attempt to use the same tactics  against you. You gain a +1 status bonus to your Perception DC  against attem |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/16` | 0.627317 | This chapter starts with rules for casting spells,  determining their effects, and negating foes' spells  (called counteracting). After that, the spell lists for  each spellcasting tradition are inclu |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/8` | 0.623286 | If something isn't listed in your character's class entry,  their proficiency rank in that statistic is untrained unless  they gain training from another source. If your character  is untrained in som |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/5` | 0.621792 | Each class entry specifies your character's initial  proficiency rank in Perception, saving throws, attacks,  defenses, and class DC. You gain the trained proficiency  rank in several skills. The exac |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/2/Text/7` | 0.619119 | Spellcasting classes grant a proficiency rank for spell  attacks and DCs, which are further detailed in each class's  entry. These classes rarely use their class DC. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/13` | 0.617100 | You've become an expert at veiling your schemes. When a  creature rolls a critical success to Sense Motive against you,  or a skill check to Gather Information or Recall Knowledge  about your secrets, |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/37` | 0.616677 | It's nigh impossible for your enemies to unravel your schemes  or your long-term plans. When a creature rolls a critical success  or success on a Perception check to Sense Motive against you,  or on a |

### Query 353
- Text: What are the requirements for **PSYCHIC MASTERY** **FEAT 9**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/28']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/28', 'PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/32', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/60']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/28` | 0.796465 | **PSYCHIC MASTERY** **FEAT 9** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/32` | 0.774212 | **PSYCHIC MASTER** **FEAT 9** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.728949 | **Prerequisites** Psychic Mastery |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.626374 | **Prerequisites** Psychic Talent |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.626374 | **Prerequisites** Psychic Talent |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/12` | 0.615792 | 9TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/21` | 0.615792 | 9TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/25` | 0.615792 | 9TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/23` | 0.615792 | 9TH LEVEL |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/42` | 0.608016 | **Prerequisites** Psychic Bully, Psychic Scholar, or Psychic Talent |

### Query 354
- Text: What are the requirements for **Prerequisites** Psychic Talent?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/31', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/35', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/42']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.884008 | **Prerequisites** Psychic Talent |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.884008 | **Prerequisites** Psychic Talent |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/42` | 0.790892 | **Prerequisites** Psychic Bully, Psychic Scholar, or Psychic Talent |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.718281 | **Prerequisites** Psychic Mastery |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/25` | 0.658547 | **Prerequisites** adaptive talent |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22` | 0.582909 | **Prerequisites** limited telepathy |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/25` | 0.582909 | **Prerequisites** limited telepathy |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/21` | 0.582909 | **Prerequisites** limited telepathy |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/23` | 0.582909 | **Prerequisites** limited telepathy |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.582475 | **Prerequisites** trained in Intimidation |

### Query 355
- Text: What is the rule about Your psychic abilities have grown stronger, allowing you to  tap into entirely new dimensions of psychic power. Choose  one common 2nd-rank spell from the occult spell list. You can  cast that spell as an occult innate spell once per day.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/32']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `22`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/32', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/36', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/61']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/32` | 0.967491 | Your psychic abilities have grown stronger, allowing you to  tap into entirely new dimensions of psychic power. Choose  one common 2nd-rank spell from the occult spell list. You can  cast that spell a |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/36` | 0.943814 | Your psychic abilities have grown stronger. Choose one  common 2nd-rank spell from the occult spell list. You can cast  that spell as an occult innate spell once per day. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/61` | 0.893762 | Your psychic abilities have grown stronger. Choose one  common 6th-rank spell from the occult spell list. You can cast  that spell as an occult innate spell once per day. |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/32` | 0.751237 | Your psychic abilities have developed beyond simple  communication. Choose one cantrip from the occult spell list. You  can cast this cantrip as an occult innate spell at will. A cantrip is  heightene |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/3` | 0.751237 | Your psychic abilities have developed beyond simple  communication. Choose one cantrip from the occult spell list. You  can cast this cantrip as an occult innate spell at will. A cantrip is  heightene |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/46` | 0.704237 | Your mastery of language reaches supernatural levels. You can  cast *truespeech* as a 5th-rank occult innate spell once per day on  yourself only. You gain a +1 status bonus to Diplomacy checks  for t |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/43` | 0.698274 | You can use your telepathic abilities to quickly assess your  circumstances or subtly glean information from the minds of  others. You can cast *hypercognition* and *mind reading* as 3rdrank occult in |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/8` | 0.684629 | **Prerequisites** korasha lashunta or unbound lashunta heritage You can leverage your telepathic abilities to influence the  minds of others, imparting orders or inflaming fears. You can  cast *comman |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/13` | 0.671014 | You're an accomplished battledancer and warrior, blessed  by seers, honed by ancestral tradition, and capable of feats  beyond the natural abilities of your peers. You gain *tailwind* as  a 1st-rank p |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/12` | 0.665506 | **Prerequisites** damaya lashunta or unbound lashunta heritage You can transfer vast amounts of information to the minds of  others in mere moments. You can cast *mindlink* as a 1st-rank  occult innat |

### Query 356
- Text: What are the requirements for **FOCUS PHEROMONES **[one-action] **FEAT 13**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/34', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/55', 'PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/18']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/34` | 0.832452 | **FOCUS PHEROMONES **[one-action] **FEAT 13** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/55` | 0.668095 | **Requirements** You have at least 1 Focus Point. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/18` | 0.667840 | **COMMANDING PHEROMONES** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/9` | 0.622249 | **ALLURING PHEROMONES** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/48` | 0.577591 | **SUPERSONIC SPEED** **FEAT 13** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/42` | 0.576770 | **OPPORTUNISTIC HUG **[reaction] **FEAT 13** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/13` | 0.561653 | **CENTER THOUGHTS **[free-action] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/47` | 0.558177 | **UNCONVENTIONAL EXPERTISE** **FEAT 13** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/42` | 0.557313 | **SCRUPULOUS STALKER **[free-action] **FEAT 13** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/49` | 0.556964 | **YOU CAN DO IT **[one-action] **FEAT 14** |

### Query 357
- Text: What is the rule about You can purposefully deploy your pheromones to manipulate  the reactions of those around you. If your next action is to  attempt a Deception check to Create a Diversion, a Diplomacy  check to Request, or an Intimidation check to Demoralize, roll  that skill check twice and use the better result.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/38']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `17`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/38', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/12', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/38` | 0.980236 | You can purposefully deploy your pheromones to manipulate  the reactions of those around you. If your next action is to  attempt a Deception check to Create a Diversion, a Diplomacy  check to Request, |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/34` | 0.772335 | With masterful timing and a careful choice of words, you  can manipulate the emotions and thoughts of others. You  roll the triggering Deception, Diplomacy, or Intimidation  check twice, and use the h |
| 3 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/12` | 0.739791 | **Trigger** You roll a skill check for any of the following skills  you're legendary in: Deception, Diplomacy, Intimidation, or  your leadership skill. |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/12` | 0.713036 | You influence others with pheromones, even when you lack  other means of communication. You can use Diplomacy  to Make an Impression on creatures with whom you don't  share a language and to make simp |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/21` | 0.705595 | You can leverage your alluring pheromones to soothe ill will  and take the edge off your threats, turning your attempts  at coercion into acts of leadership. When you Coerce a  creature, if your targe |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/19` | 0.666436 | You can use Improvised Mastery twice per day. Additionally,  the first time per day when you roll a natural 1 on a Deception,  Diplomacy, or Intimidation check, you don't automatically  reduce your de |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/33` | 0.656046 | **Trigger** You're about to roll a Deception, Diplomacy, or  Intimidation check, but you haven't rolled yet. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/12` | 0.645755 | Using your words to influence others is what you do, and you  easily recognize when others attempt to use the same tactics  against you. You gain a +1 status bonus to your Perception DC  against attem |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/13` | 0.640760 | You can reroll the triggering skill check and use the better result. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/18` | 0.633199 | You broadcast helpful encouragement or pertinent information  to your ally's mind. Your ally rerolls the triggering skill check and  takes the better result. |

### Query 358
- Text: What are the requirements for **PSYCHIC INVESTIGATOR** **FEAT 13**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/39']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `33`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/39', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/42', 'PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/37']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/39` | 0.703433 | **PSYCHIC INVESTIGATOR** **FEAT 13** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/42` | 0.634767 | **Prerequisites** Psychic Bully, Psychic Scholar, or Psychic Talent |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/37` | 0.623400 | 13TH LEVEL |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/33` | 0.581400 | 13TH LEVEL |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/36` | 0.581400 | 13TH LEVEL |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/37` | 0.581400 | 13TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.579063 | **Prerequisites** Psychic Talent |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.579063 | **Prerequisites** Psychic Talent |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.566247 | **Prerequisites** Psychic Mastery |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/47` | 0.564497 | **UNCONVENTIONAL EXPERTISE** **FEAT 13** |

### Query 359
- Text: What are the requirements for **Prerequisites** Psychic Bully, Psychic Scholar, or Psychic Talent?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/42']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/42', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/31', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/35']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/42` | 0.923480 | **Prerequisites** Psychic Bully, Psychic Scholar, or Psychic Talent |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.787761 | **Prerequisites** Psychic Talent |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.787761 | **Prerequisites** Psychic Talent |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.677989 | **Prerequisites** Psychic Mastery |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/25` | 0.578489 | **Prerequisites** adaptive talent |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.559044 | **Prerequisites** trained in Intimidation |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/53` | 0.558169 | **Prerequisites** expert in Occultism, focus pool |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/5` | 0.547382 | **PSYCHIC BULLY** **FEAT 5** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/9` | 0.544791 | **PSYCHIC SCHOLAR** **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/46` | 0.543807 | **Prerequisites** master in Intimidation |

### Query 360
- Text: What is the rule about You can use your telepathic abilities to quickly assess your  circumstances or subtly glean information from the minds of  others. You can cast *hypercognition* and *mind reading* as 3rdrank occult innate spells. You can cast each of these occult  innate spells once per day.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/43']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/43', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/8', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/43` | 0.969430 | You can use your telepathic abilities to quickly assess your  circumstances or subtly glean information from the minds of  others. You can cast *hypercognition* and *mind reading* as 3rdrank occult in |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/8` | 0.777776 | **Prerequisites** korasha lashunta or unbound lashunta heritage You can leverage your telepathic abilities to influence the  minds of others, imparting orders or inflaming fears. You can  cast *comman |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/32` | 0.742242 | Your psychic abilities have grown stronger, allowing you to  tap into entirely new dimensions of psychic power. Choose  one common 2nd-rank spell from the occult spell list. You can  cast that spell a |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/46` | 0.699780 | Your mastery of language reaches supernatural levels. You can  cast *truespeech* as a 5th-rank occult innate spell once per day on  yourself only. You gain a +1 status bonus to Diplomacy checks  for t |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/12` | 0.697756 | **Prerequisites** damaya lashunta or unbound lashunta heritage You can transfer vast amounts of information to the minds of  others in mere moments. You can cast *mindlink* as a 1st-rank  occult innat |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/36` | 0.686374 | Your psychic abilities have grown stronger. Choose one  common 2nd-rank spell from the occult spell list. You can cast  that spell as an occult innate spell once per day. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/61` | 0.675972 | Your psychic abilities have grown stronger. Choose one  common 6th-rank spell from the occult spell list. You can cast  that spell as an occult innate spell once per day. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/41` | 0.667100 | Whether through intense musical training, magical insight, or  Meyel's divine blessing, you can feel the rhythm of the world  around you and tug on time's chords to manipulate its melody  and flow. Yo |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/41` | 0.652354 | You never let the inability to communicate stop you from  chatting with nufriends! You gain *speak with animals* as  a 2nd-rank primal innate spell, and *speak with plants* and  *translate* as 3rd-ran |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/3` | 0.642379 | Your psychic abilities have developed beyond simple  communication. Choose one cantrip from the occult spell list. You  can cast this cantrip as an occult innate spell at will. A cantrip is  heightene |

### Query 361
- Text: What are the requirements for **CENTERED MIND** **FEAT 17**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/45']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `33`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/45', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/55', 'PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/53']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/45` | 0.791134 | **CENTERED MIND** **FEAT 17** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/55` | 0.645035 | **Requirements** You have at least 1 Focus Point. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/53` | 0.621844 | 17TH LEVEL |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/44` | 0.591844 | 17TH LEVEL |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/47` | 0.579844 | 17TH LEVEL |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/52` | 0.579844 | 17TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/48` | 0.570714 | **BOUNDLESS BRACHIATOR** **FEAT 17** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/30` | 0.565851 | **SIZE UP** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/42` | 0.556716 | **CONCENTRATE** **ENVOY** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/50` | 0.552285 | **MENTAL DEFLECTION **[reaction] **FEAT 17** |

### Query 362
- Text: What are the requirements for **Prerequisites** Center Thoughts?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/48']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/48', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/60', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/48` | 0.868630 | **Prerequisites** Center Thoughts |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.669081 | **Prerequisites** Psychic Mastery |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.662279 | **Prerequisites** Psychic Talent |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.620279 | **Prerequisites** Psychic Talent |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/34` | 0.607914 | **Prerequisites** Hyper |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/41` | 0.604395 | **Prerequisites** Communalism |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/55` | 0.602813 | **Requirements** You have at least 1 Focus Point. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/51` | 0.602537 | **Prerequisites** Zoomies |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/63` | 0.602537 | **Prerequisites** Zoomies |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/26` | 0.581122 | **Prerequisites** Watch Out |

### Query 363
- Text: What are the requirements for **MENTAL DEFLECTION **[reaction] **FEAT 17**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/50']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `31`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/50', 'PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/57', 'PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/53']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/50` | 0.857176 | **MENTAL DEFLECTION **[reaction] **FEAT 17** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/57` | 0.718794 | **PSYCHIC PARAGON** **FEAT 17** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/53` | 0.713628 | **SCATTER THOUGHTS **[reaction] **FEAT 17** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/45` | 0.652210 | **CENTERED MIND** **FEAT 17** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/52` | 0.630735 | 17TH LEVEL |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/47` | 0.618735 | 17TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/53` | 0.618735 | 17TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/44` | 0.618735 | 17TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/9` | 0.613551 | **COMPETITIVE SPIRIT **[reaction] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.599301 | **Prerequisites** Psychic Mastery |

### Query 364
- Text: What are the requirements for **Prerequisites** expert in Occultism, focus pool?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/53']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `24`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/53', 'PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/40', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/60']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/53` | 0.954464 | **Prerequisites** expert in Occultism, focus pool |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/40` | 0.656643 | **Prerequisites** expert in Performance |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.626152 | **Prerequisites** Psychic Mastery |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/8` | 0.616013 | **Prerequisites** expert in Diplomacy |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/55` | 0.575413 | **Requirements** You have at least 1 Focus Point. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/42` | 0.567158 | **Prerequisites** Psychic Bully, Psychic Scholar, or Psychic Talent |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.564398 | **Prerequisites** Psychic Talent |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.564398 | **Prerequisites** Psychic Talent |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25` | 0.547438 | **Prerequisites** trained in Deception or Diplomacy |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/5` | 0.540230 | **Prerequisites** master in Deception |

### Query 365
- Text: What is the rule about **Trigger** A creature Casts a Spell with the mental trait.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/54']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `18`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/54', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/56', 'PZO22001 Starfinder Player Core 058-073::/page/15/Text/45']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/54` | 0.869740 | **Trigger** A creature Casts a Spell with the mental trait. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/56` | 0.664793 | When a foe Casts a Spell that has the mental trait and you can  see or otherwise detect its manifestations, you use your psychic  powers to disrupt it. You expend 1 Focus Point to counter the  trigger |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/45` | 0.662068 | **Trigger** A creature critically fails a melee Strike against you. **Requirements** The triggering creature is within your reach,  you have at least one free active hand, and your target is  no more |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/57` | 0.586651 | **Trigger** You're targeted by a mental effect. |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/4` | 0.567879 | **Unbound Mind **[reaction] **Trigger** You attempt a saving throw against  a mental effect, but you haven't rolled yet; **Effect** You refuse  to conform to the will of others, shaking off their atte |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/23` | 0.563210 | **Trigger** A creature targets you with a melee attack. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/46` | 0.562876 | Your mastery of language reaches supernatural levels. You can  cast *truespeech* as a 5th-rank occult innate spell once per day on  yourself only. You gain a +1 status bonus to Diplomacy checks  for t |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/11` | 0.561692 | **Trigger** The target of your Get 'Em! is critically hit by an  ally's attack or critically fails a Reflex save against an  ally's attack or spell. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/41` | 0.559486 | You never let the inability to communicate stop you from  chatting with nufriends! You gain *speak with animals* as  a 2nd-rank primal innate spell, and *speak with plants* and  *translate* as 3rd-ran |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/29` | 0.555965 | **Trigger** A creature within 30 feet is damaged by an ally's Strike. You follow up on your ally's success by hurling a cunning, welltimed taunt at a foe they wounded. Attempt to Demoralize the  trigg |

### Query 366
- Text: What is the rule about When a foe Casts a Spell that has the mental trait and you can  see or otherwise detect its manifestations, you use your psychic  powers to disrupt it. You expend 1 Focus Point to counter the  triggering creature's casting of the spell. You then attempt  to counteract the triggering spell using your spellcasting  attribute modifier plus your spellcasting proficiency bonus as  your counteract modifier and half your level, rounded up, as  your counteract rank.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/56']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `19`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/56', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/27', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/56` | 0.971648 | When a foe Casts a Spell that has the mental trait and you can  see or otherwise detect its manifestations, you use your psychic  powers to disrupt it. You expend 1 Focus Point to counter the  trigger |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/27` | 0.789091 | Your psychic training allows you to block attempts to read  your thoughts. Any effect that specifically attempts to read  your mind to glean information must succeed at a counteract  check against the |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/4` | 0.709799 | **Unbound Mind **[reaction] **Trigger** You attempt a saving throw against  a mental effect, but you haven't rolled yet; **Effect** You refuse  to conform to the will of others, shaking off their atte |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/16` | 0.699561 | This chapter starts with rules for casting spells,  determining their effects, and negating foes' spells  (called counteracting). After that, the spell lists for  each spellcasting tradition are inclu |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/14` | 0.658625 | You push yourself to be the best by competing with the  triggering ally. Until the end of your next turn, you can attempt  the same skill check to perform the same action or activity  that the trigger |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/13` | 0.637585 | You've become an expert at veiling your schemes. When a  creature rolls a critical success to Sense Motive against you,  or a skill check to Gather Information or Recall Knowledge  about your secrets, |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/54` | 0.635789 | **Trigger** A creature Casts a Spell with the mental trait. |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/6/Text/26` | 0.634765 | **Lead by Example** If you used two actions, Strike the target to  focus their attention on you. The target takes a –1 circumstance  penalty on attacks made against other creatures until the start  of |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/12` | 0.627333 | Using your words to influence others is what you do, and you  easily recognize when others attempt to use the same tactics  against you. You gain a +1 status bonus to your Perception DC  against attem |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/20` | 0.626563 | modifier, recalculate their maximum Hit  Points using their new Constitution modifier  (typically, this adds 1 Hit Point per level). If  an attribute boost increases your character's  Intelligence mod |

### Query 367
- Text: What are the requirements for **PSYCHIC PARAGON** **FEAT 17**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/57']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `35`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/57', 'PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/53', 'PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/47']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/57` | 0.796628 | **PSYCHIC PARAGON** **FEAT 17** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/53` | 0.640450 | 17TH LEVEL |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/47` | 0.640450 | 17TH LEVEL |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/44` | 0.598450 | 17TH LEVEL |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/52` | 0.598450 | 17TH LEVEL |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/48` | 0.592336 | **BOUNDLESS BRACHIATOR** **FEAT 17** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.586183 | **Prerequisites** Psychic Mastery |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/50` | 0.584864 | **MENTAL DEFLECTION **[reaction] **FEAT 17** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.581983 | **Prerequisites** Psychic Talent |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.581983 | **Prerequisites** Psychic Talent |

### Query 368
- Text: What are the requirements for **Prerequisites** Psychic Mastery?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/60']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `21`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/60', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/31', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/35']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.892122 | **Prerequisites** Psychic Mastery |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.775044 | **Prerequisites** Psychic Talent |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.775044 | **Prerequisites** Psychic Talent |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/42` | 0.688614 | **Prerequisites** Psychic Bully, Psychic Scholar, or Psychic Talent |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/19` | 0.657308 | **Prerequisites **Improvised Mastery |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/46` | 0.653976 | **Prerequisites** master in Intimidation |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/5` | 0.628377 | **Prerequisites** master in Deception |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.610169 | **Prerequisites** trained in Intimidation |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/25` | 0.580594 | **Prerequisites** trained in Deception or Diplomacy |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/34` | 0.578138 | **Prerequisites** Hyper |

### Query 369
- Text: What is the rule about Your psychic abilities have grown stronger. Choose one  common 6th-rank spell from the occult spell list. You can cast  that spell as an occult innate spell once per day.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/61']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `16`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/61', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/36', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/32']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/61` | 0.941144 | Your psychic abilities have grown stronger. Choose one  common 6th-rank spell from the occult spell list. You can cast  that spell as an occult innate spell once per day. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/36` | 0.884971 | Your psychic abilities have grown stronger. Choose one  common 2nd-rank spell from the occult spell list. You can cast  that spell as an occult innate spell once per day. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/32` | 0.877291 | Your psychic abilities have grown stronger, allowing you to  tap into entirely new dimensions of psychic power. Choose  one common 2nd-rank spell from the occult spell list. You can  cast that spell a |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/32` | 0.721896 | Your psychic abilities have developed beyond simple  communication. Choose one cantrip from the occult spell list. You  can cast this cantrip as an occult innate spell at will. A cantrip is  heightene |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/3` | 0.721896 | Your psychic abilities have developed beyond simple  communication. Choose one cantrip from the occult spell list. You  can cast this cantrip as an occult innate spell at will. A cantrip is  heightene |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/46` | 0.688764 | Your mastery of language reaches supernatural levels. You can  cast *truespeech* as a 5th-rank occult innate spell once per day on  yourself only. You gain a +1 status bonus to Diplomacy checks  for t |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/8` | 0.655994 | **Prerequisites** korasha lashunta or unbound lashunta heritage You can leverage your telepathic abilities to influence the  minds of others, imparting orders or inflaming fears. You can  cast *comman |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/13` | 0.654748 | You're an accomplished battledancer and warrior, blessed  by seers, honed by ancestral tradition, and capable of feats  beyond the natural abilities of your peers. You gain *tailwind* as  a 1st-rank p |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/43` | 0.654049 | You can use your telepathic abilities to quickly assess your  circumstances or subtly glean information from the minds of  others. You can cast *hypercognition* and *mind reading* as 3rdrank occult in |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/41` | 0.628628 | Whether through intense musical training, magical insight, or  Meyel's divine blessing, you can feel the rhythm of the world  around you and tug on time's chords to manipulate its melody  and flow. Yo |

### Query 370
- Text: What is the rule about **ANCESTRIES & ** **BACKGROUNDS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/64']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `16`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/15/Text/67', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/30', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/64']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/67` | 0.830013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/30` | 0.830013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/64` | 0.830013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/66` | 0.788013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/31` | 0.788013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/31` | 0.788013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/58` | 0.788013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/30` | 0.788013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/29` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/23` | 0.780013 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 371
- Text: What is the rule about **Backgrounds**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/77']
- Expected found: `True`
- Expected rank: `4`
- Graph boost applied: `True`
- Graph boosted count: `20`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/5/Text/43', 'PZO22001 Starfinder Player Core 058-073::/page/7/Text/71', 'PZO22001 Starfinder Player Core 058-073::/page/15/Text/81']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/71` | 0.749566 | **Backgrounds** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/43` | 0.749566 | **Backgrounds** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/81` | 0.749566 | **Backgrounds** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/77` | 0.707566 | **Backgrounds** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/80` | 0.707566 | **Backgrounds** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/43` | 0.707566 | **Backgrounds** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/44` | 0.648178 | **Backgrounds** **Languages** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/43` | 0.648178 | **Backgrounds** **Languages** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/67` | 0.627269 | **ANCESTRIES & ** **BACKGROUNDS** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/66` | 0.627269 | **ANCESTRIES & ** **BACKGROUNDS** |

### Query 372
- Text: What is the rule about **SKILLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/80']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `14`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/1/Text/45', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/80', 'PZO22001 Starfinder Player Core 058-073::/page/9/Text/45']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/45` | 0.777771 | **SKILLS** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/80` | 0.777771 | **SKILLS** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/45` | 0.777771 | **SKILLS** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/74` | 0.735771 | **SKILLS** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/46` | 0.735771 | **SKILLS** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/84` | 0.735771 | **SKILLS** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/30` | 0.727771 | **SKILLS** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/31` | 0.727771 | **SKILLS** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/25` | 0.727771 | **SKILLS** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/35` | 0.727771 | **SKILLS** |

### Query 373
- Text: What is the rule about **FEATS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/81']
- Expected found: `True`
- Expected rank: `5`
- Graph boost applied: `True`
- Graph boosted count: `12`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/13/Text/47', 'PZO22001 Starfinder Player Core 058-073::/page/15/Text/85', 'PZO22001 Starfinder Player Core 058-073::/page/9/Text/46']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/85` | 0.735680 | **FEATS** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/46` | 0.735680 | **FEATS** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/47` | 0.735680 | **FEATS** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/46` | 0.693680 | **FEATS** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/81` | 0.693680 | **FEATS** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/75` | 0.693680 | **FEATS** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/36` | 0.685680 | **FEATS** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/32` | 0.685680 | **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/1/Text/26` | 0.685680 | **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/31` | 0.685680 | **FEATS** |

### Query 374
- Text: What is the rule about **SPELLS**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/83']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `16`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/3/Text/83', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/48', 'PZO22001 Starfinder Player Core 058-073::/page/13/Text/49']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/49` | 0.806592 | **SPELLS** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/83` | 0.806592 | **SPELLS** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/48` | 0.806592 | **SPELLS** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/48` | 0.764592 | **SPELLS** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/85` | 0.764592 | **SPELLS** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/77` | 0.764592 | **SPELLS** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/48` | 0.764592 | **SPELLS** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/33` | 0.756592 | **SPELLS** |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/44` | 0.756592 | **SPELLS** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/9/Text/50` | 0.756592 | **SPELLS** |

### Query 375
- Text: What is the rule about Pahtras are a humanoid feline species from a nearby star system. They're highly competitive and known for their achievements in magic, music, and war. Their home world was recently freed from the Veskarium's occupation, and they've joined the Pact Worlds.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/4/Text/2']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `35`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/4/Text/2', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/9', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/20']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/4/Text/2` | 0.947816 | Pahtras are a humanoid feline species from a nearby star system. They're highly competitive and known for their achievements in magic, music, and war. Their home world was recently freed from the Vesk |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/9` | 0.756098 | Pahtras evolved on a low-gravity jungle world called Pulonis,  where they fought a long war for independence from their  Veskarium conquerors. Recently, pahtra freedom fighters  defeated the last Vesk |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/20` | 0.706379 | Many pahtras cling fiercely to their ancestral Pulonian  traditions in an effort to keep their cultures alive after  enduring generations of oppression by the Veskarium.  Pulonian culture values perso |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/15` | 0.656072 | Pahtra cultures are steeped in tradition and highly competitive,  with individuals vying for recognition and resources in a  struggle that mimics the harsh natural order of their planet.  Before the V |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/12` | 0.633110 | Pahtras are feline humanoids covered in fur. Their coats vary  from black, white, blue, calico, bi-colored, and tabby, often  possessing unique patterns of irregular shapes that seers  traditionally u |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/33` | 0.630550 | Pahtras are competitive and  graceful, valuing competition,  music, and their own freedom.  Page 62. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/5` | 0.567569 | Your ancestors roamed blasted terrain leached of vital nutrients  by the Veskarium. You're shorter and stockier than most  pahtras, with wide, tufted ears and fur-covered paw pads. Your  size is Small |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/13` | 0.561664 | Pahtras have sharp teeth and retractable claws on their  hands and feet. They have a unique set of sensory organs  across their muzzles, with functions varying from individual  to individual. The most |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/10` | 0.555968 | If you want to play a character who fights for freedom with  grace and style, you should play a pahtra. |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/0/Text/6` | 0.514023 | The rules for ancestries and heritages representing the  Pact Worlds are in this chapter, including their ancestry  feat options. Backgrounds are at the end of this chapter,  along with a section abou |

### Query 376
- Text: What is the rule about Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent on your home world).?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/4/Text/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `10`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/4/Text/11', 'PZO22001 Starfinder Player Core 058-073::/page/12/Text/9', 'PZO22001 Starfinder Player Core 058-073::/page/0/Text/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/4/Text/11` | 0.944766 | Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/12/Text/9` | 0.944766 | Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/0/Text/9` | 0.944766 | Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have access (such as the languages prevalent |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/8/Text/11` | 0.871051 | One regional language of your choice Additional languages equal to your Intelligence modifier (if it's positive). Choose from the list of common languages and any other languages to which you have acc |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/5/Text/58` | 0.626701 | Trained in a number of additional  skills equal to 6 plus your Intelligence  modifier |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/28` | 0.623693 | Learning new languages comes naturally to you. You gain two  additional languages of your choice, chosen from among the  common and uncommon languages available to you. Every time  you take the Multil |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/15/Text/20` | 0.616630 | modifier, recalculate their maximum Hit  Points using their new Constitution modifier  (typically, this adds 1 Hit Point per level). If  an attribute boost increases your character's  Intelligence mod |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/9/Text/2` | 0.577412 | Each attribute modifier starts at +0, representing the average. As you make character choices, you'll adjust these  modifiers by applying attribute boosts, which increase an attribute modifier, and at |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/10/Text/17` | 0.571894 | If your character has any modifiers, bonuses, or  penalties from feats or abilities that always apply,  add them into the total modifiers. For ones that  apply only in certain situations, note them ne |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/10/Text/7` | 0.571365 | Your character's Perception modifier measures how alert  they are, and is equal to their proficiency bonus in Perception  plus their Wisdom modifier. See page 396 for more. |

### Query 377
- Text: What is the rule about **TRAITS **?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/4/SectionHeader/12']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `12`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/4/SectionHeader/12', 'PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/10', 'PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/10` | 0.796994 | **TRAITS ** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/4/SectionHeader/12` | 0.796994 | **TRAITS ** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/12` | 0.766427 | TRAITS |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/12` | 0.752714 | **TRAITS** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/12/SectionHeader/10` | 0.724427 | TRAITS |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/4` | 0.604765 | **Attributes** |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/9/SectionHeader/11` | 0.577428 | **Attribute Flaws** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/46` | 0.569479 | **SKILLS** **FEATS** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/83` | 0.569479 | **SKILLS** **FEATS** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/6/SectionHeader/11` | 0.567135 | **CHARACTER SHEET ** |

### Query 378
- Text: What is the rule about You can see in darkness and dim light just as well as you can see in bright light, though your vision in darkness is in black and white.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/4/Text/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `14`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/4/Text/15', 'PZO22001 Starfinder Player Core 058-073::/page/12/Text/13', 'PZO22001 Starfinder Player Core 058-073::/page/14/Text/1']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/4/Text/15` | 0.871672 | You can see in darkness and dim light just as well as you can see in bright light, though your vision in darkness is in black and white. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/12/Text/13` | 0.653285 | You can see in dim light as though it were bright light, and you ignore the concealed condition due to dim light. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/1` | 0.597829 | pale-colored fur, a slender build, and large, luminous eyes. You  gain darkvision. |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/12/SectionHeader/12` | 0.462431 | **LOW-LIGHT VISION ** |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/5/Text/14` | 0.457528 | Wisdom measures your character's common sense,  awareness, and intuition. High Wisdom helps your  character detect hidden things and resist mental effects.  Your Wisdom modifier is added to your Perce |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/1/Text/4` | 0.450513 | The rules within each class allow you to bring a wealth of  character concepts to life. Perhaps you want to create an  observant but impulsive mystic who can see the pain in  someone's eyes but can't |
| 7 | `PZO22001 Starfinder Player Core 014-029::/page/10/Text/21` | 0.449157 | You can choose to take on edicts and anathema to  reinforce your character's beliefs and guide how they'd  react in certain situations. **Edicts** are behaviors your  personal philosophy or code encou |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/10/SectionHeader/6` | 0.445277 | PERCEPTION |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/2/SectionHeader/5` | 0.434558 | READING RULES |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/29` | 0.431966 | **Prerequisites** trained in Arcana, Nature, Occultism, or Religion You can hear the thrum of magic as if it were a swirling note, a  shifting melody, a harmonic chord, or a percussive beat, pulsing |

### Query 379
- Text: What is the rule about Pahtras evolved on a low-gravity jungle world called Pulonis,  where they fought a long war for independence from their  Veskarium conquerors. Recently, pahtra freedom fighters  defeated the last Veskarium occupiers, then voted to join the  Pact Worlds as a sovereign planet. Today, Pulonis is a lush,  verdant world wracked by dangerous magnetic storms and  scarred by the Veskarium's brutal invasion. The struggles of  survival have influenced many pahtra traditions, leading to a  culture of competitive war games, time-honored mysticism,  and unorthodox technology. Music accompanies everything  in pahtra culture, from popular entertainment to traditional  battle tactics, with martial combat even categorized as a form  of battle dance.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/5/Text/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `33`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/5/Text/9', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/20', 'PZO22001 Starfinder Player Core 058-073::/page/5/Text/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/9` | 0.988919 | Pahtras evolved on a low-gravity jungle world called Pulonis,  where they fought a long war for independence from their  Veskarium conquerors. Recently, pahtra freedom fighters  defeated the last Vesk |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/20` | 0.822199 | Many pahtras cling fiercely to their ancestral Pulonian  traditions in an effort to keep their cultures alive after  enduring generations of oppression by the Veskarium.  Pulonian culture values perso |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/15` | 0.816531 | Pahtra cultures are steeped in tradition and highly competitive,  with individuals vying for recognition and resources in a  struggle that mimics the harsh natural order of their planet.  Before the V |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/4/Text/2` | 0.696971 | Pahtras are a humanoid feline species from a nearby star system. They're highly competitive and known for their achievements in magic, music, and war. Their home world was recently freed from the Vesk |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/33` | 0.603177 | Pahtras are competitive and  graceful, valuing competition,  music, and their own freedom.  Page 62. |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/12` | 0.571267 | Pahtras are feline humanoids covered in fur. Their coats vary  from black, white, blue, calico, bi-colored, and tabby, often  possessing unique patterns of irregular shapes that seers  traditionally u |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/5` | 0.567713 | Your ancestors roamed blasted terrain leached of vital nutrients  by the Veskarium. You're shorter and stockier than most  pahtras, with wide, tufted ears and fur-covered paw pads. Your  size is Small |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/3` | 0.566606 | You've adapted to cold environments by growing a fluffy  fur coat. You might be the descendant of ancient pahtras  who dwelled in the frigid regions of Pulonis long before the  Veskarium's exploitatio |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/10` | 0.557073 | If you want to play a character who fights for freedom with  grace and style, you should play a pahtra. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/13` | 0.521260 | Pahtras have sharp teeth and retractable claws on their  hands and feet. They have a unique set of sensory organs  across their muzzles, with functions varying from individual  to individual. The most |

### Query 380
- Text: What is the rule about If you want to play a character who fights for freedom with  grace and style, you should play a pahtra.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/5/Text/10']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/5/Text/10', 'PZO22001 Starfinder Player Core 058-073::/page/1/Text/10', 'PZO22001 Starfinder Player Core 058-073::/page/9/Text/10']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/10` | 0.945336 | If you want to play a character who fights for freedom with  grace and style, you should play a pahtra. |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/1/Text/10` | 0.648068 | If you want to play a character who strives for selfimprovement and has innate psychic abilities, you should play  a lashunta. |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/9/Text/10` | 0.643604 | If you want a character who enjoys working as part of  a team while still valuing independence, you should play a  shirren. |
| 4 | `PZO22001 Starfinder Player Core 014-029::/page/13/Text/33` | 0.624303 | Pahtras are competitive and  graceful, valuing competition,  music, and their own freedom.  Page 62. |
| 5 | `PZO22001 Starfinder Player Core 014-029::/page/4/Text/11` | 0.581950 | Building a character around a specific ancestry,  background, or class can be a fun way to interact with the  galaxy's lore. For example, you could play a pacifist vesk who  prefers negotiation over c |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/25` | 0.577537 | You're an expert in both the traditional and modern pahtra |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/9` | 0.573657 | Pahtras evolved on a low-gravity jungle world called Pulonis,  where they fought a long war for independence from their  Veskarium conquerors. Recently, pahtra freedom fighters  defeated the last Vesk |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/20` | 0.571421 | Many pahtras cling fiercely to their ancestral Pulonian  traditions in an effort to keep their cultures alive after  enduring generations of oppression by the Veskarium.  Pulonian culture values perso |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/13/Text/11` | 0.544120 | If you want to play a character who's friendly and emotional  and who enjoys helping others, you should play a skittermander. |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/12/Text/5` | 0.541572 | Prioritize Charisma. Dexterity, Intelligence, and  Constitution round out your abilities and defenses. |

### Query 381
- Text: What are the requirements for **COMPETITIVE SPIRIT **[reaction] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/9']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `30`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/9', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/1', 'PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/9` | 0.847813 | **COMPETITIVE SPIRIT **[reaction] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/26` | 0.665718 | **QUIP **[reaction] **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/1` | 0.653112 | **PSYCHIC TALENT** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/29` | 0.653112 | **PSYCHIC TALENT** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.630370 | **WATCH OUT **[reaction] **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/13` | 0.608276 | **COMMUNALISM **[reaction] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/13` | 0.581693 | **CENTER THOUGHTS **[free-action] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26` | 0.581569 | **HYPER** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/15` | 0.578468 | **HARMONIC SENSITIVITY** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/18` | 0.573998 | **COMMANDING PHEROMONES** **FEAT 1** |

### Query 382
- Text: What are the requirements for **HARMONIC SENSITIVITY** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/15']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `36`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/15', 'PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/24', 'PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/15` | 0.839110 | **HARMONIC SENSITIVITY** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/24` | 0.752793 | **Prerequisites** Harmonic Sensitivity |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26` | 0.623547 | **HYPER** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/22` | 0.573576 | **HARMONIC SHIELDING** **FEAT 9** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/13` | 0.566556 | **SENSITIVE ANTENNAE** **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/1` | 0.566340 | **PSYCHIC TALENT** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/29` | 0.566340 | **PSYCHIC TALENT** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/55` | 0.564522 | **Requirements** You have at least 1 Focus Point. |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.558298 | **WATCH OUT **[reaction] **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/18` | 0.557947 | **COMMANDING PHEROMONES** **FEAT 1** |

### Query 383
- Text: What are the requirements for **LONG WHISKERED** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/19']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `35`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/19', 'PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/19', 'PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/19` | 0.796337 | **Prerequisites** Long Whiskered |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/19` | 0.794114 | **LONG WHISKERED** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26` | 0.647092 | **HYPER** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/30` | 0.591659 | **SIZE UP** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/25` | 0.583448 | **LINGUISTIC PRODIGY** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/9` | 0.579424 | **CLINGING BITE** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/29` | 0.577113 | **SKITTERMANDER LORE** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/22` | 0.568777 | **DISTANT TELEPATH** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/19` | 0.568777 | **DISTANT TELEPATH** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/15` | 0.560738 | **DAUNTLESS** **FEAT 1** |

### Query 384
- Text: What are the requirements for **PAHTRA LORE** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/6/Text/23']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `46`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/6/Text/23', 'PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/28', 'PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/29']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/23` | 0.756038 | **PAHTRA LORE** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/28` | 0.673145 | **LASHUNTA LORE** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/29` | 0.667664 | **SKITTERMANDER LORE** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/1` | 0.584859 | **SHIRREN LORE** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/24` | 0.551922 | **PAHTRA** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/2` | 0.540580 | You also gain the Additional Lore general feat for Pahtra Lore. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/18` | 0.539922 | **PAHTRA** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/33` | 0.539922 | **PAHTRA** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/39` | 0.539922 | **PAHTRA** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/28` | 0.539922 | **PAHTRA** |

### Query 385
- Text: What are the requirements for **PREDATORY** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/Text/3']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `33`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/Text/3', 'PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26', 'PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/3` | 0.825523 | **PREDATORY** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26` | 0.639115 | **HYPER** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/25` | 0.634789 | **LINGUISTIC PRODIGY** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/22` | 0.560480 | **DISTANT TELEPATH** **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/19` | 0.560480 | **DISTANT TELEPATH** **FEAT 1** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/21` | 0.559428 | **PARDON ME** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/29` | 0.558551 | **SKITTERMANDER LORE** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/18` | 0.556971 | **COMMANDING PHEROMONES** **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/15` | 0.546906 | **DAUNTLESS** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/28` | 0.546893 | **LASHUNTA LORE** **FEAT 1** |

### Query 386
- Text: What are the requirements for **BATTLEBLESSED** **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/11']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `27`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/11', 'PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/15', 'PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/14']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/11` | 0.785363 | **BATTLEBLESSED** **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/15` | 0.647327 | **DAUNTLESS** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/14` | 0.645984 | **CLIMBING CLAWS** **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/7` | 0.587662 | **LUCKY IMPROVISER** **FEAT 5** |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/22` | 0.580170 | **ENDLESSLY ADAPTIVE** **FEAT 20** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/13` | 0.579590 | **SENSITIVE ANTENNAE** **FEAT 5** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/2` | 0.578775 | **HELPING HAND **[free-action] **FEAT 5** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/10` | 0.577659 | 5TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/9` | 0.577613 | STEP 5 |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/5` | 0.573433 | **PSYCHIC BULLY** **FEAT 5** |

### Query 387
- Text: What are the requirements for **CLIMBING CLAWS** **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/14']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/14', 'PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/34', 'PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/4']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/14` | 0.816985 | **CLIMBING CLAWS** **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/4` | 0.611662 | 5TH LEVEL |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/34` | 0.611662 | 5TH LEVEL |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/10` | 0.569662 | 5TH LEVEL |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/11` | 0.569662 | 5TH LEVEL |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/16` | 0.565208 | You can extend your claws to aid you in climbing. You gain a  climb Speed equal to your land Speed. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/12` | 0.554912 | **EAGER ASSISTANT** **FEAT 5** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/9` | 0.546446 | STEP 5 |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/7` | 0.537616 | **LUCKY IMPROVISER** **FEAT 5** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/30` | 0.535527 | 20 feet. In addition, when you fall, you take no falling damage. |

### Query 388
- Text: What are the requirements for **ELECTROMAGNETIC WHISKERS** **FEAT 5**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/17']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `33`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/17', 'PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/12', 'PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/13']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/17` | 0.801566 | **ELECTROMAGNETIC WHISKERS** **FEAT 5** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/12` | 0.653367 | **EAGER ASSISTANT** **FEAT 5** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/13` | 0.630524 | **SENSITIVE ANTENNAE** **FEAT 5** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/14` | 0.585571 | **CLIMBING CLAWS** **FEAT 5** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/7` | 0.557658 | **LUCKY IMPROVISER** **FEAT 5** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/20` | 0.556870 | You've honed your whiskers' sensitivity to the degree that you  can sense the movement of the weak electric fields emitted  by potential enemies. You gain electromagnetic sense as an  imprecise sense |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/20` | 0.551425 | **TELEPATHIC CONDUIT** **FEAT 5** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/18` | 0.551425 | **TELEPATHIC CONDUIT** **FEAT 5** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/22` | 0.547112 | Your whiskers function as advanced electroreceptors,  allowing you to orient yourself more easily. At the end  of each round in which you're untethered, attempt a  DC 15 flat check. On a success, you |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/11` | 0.535655 | 5TH LEVEL |

### Query 389
- Text: What are the requirements for **Prerequisites** Long Whiskered?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/19']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `25`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/19', 'PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/19', 'PZO22001 Starfinder Player Core 058-073::/page/15/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/19` | 0.925246 | **Prerequisites** Long Whiskered |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/19` | 0.646692 | **LONG WHISKERED** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/34` | 0.638356 | **Prerequisites** Hyper |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/51` | 0.586585 | **Prerequisites** Zoomies |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/63` | 0.586585 | **Prerequisites** Zoomies |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/28` | 0.571339 | **Prerequisites** trained in Intimidation |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/34` | 0.562413 | **Prerequisites** Watch Out |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/14/Text/26` | 0.562413 | **Prerequisites** Watch Out |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/11/Text/7` | 0.561161 | **Prerequisites** Size Up |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/12/SectionHeader/17` | 0.561161 | **Prerequisites** Size Up |

### Query 390
- Text: What are the requirements for **HARMONIC SHIELDING** **FEAT 9**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/22']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `31`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/22', 'PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/26', 'PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/15']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/22` | 0.848038 | **HARMONIC SHIELDING** **FEAT 9** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/26` | 0.638415 | **MELODIC ADAPTATION** **FEAT 9** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/15` | 0.605418 | **HARMONIC SENSITIVITY** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/13` | 0.560321 | **ALL HANDS ON DECK **[free-action] **FEAT 9** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/28` | 0.553464 | **PSYCHIC MASTERY** **FEAT 9** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/21` | 0.552414 | 9TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/31` | 0.551007 | **MEYEL'S MELODY** **FEAT 9** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/19` | 0.548119 | STEP 9 |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/32` | 0.547073 | **PSYCHIC MASTER** **FEAT 9** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/26` | 0.544658 | **BASIC INSECTILE FLIGHT** **FEAT 9** |

### Query 391
- Text: What are the requirements for **Prerequisites** Harmonic Sensitivity?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/24']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `27`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/24', 'PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/25']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/24` | 0.909337 | **Prerequisites** Harmonic Sensitivity |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22` | 0.664115 | **Prerequisites** limited telepathy |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/25` | 0.664115 | **Prerequisites** limited telepathy |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/21` | 0.622115 | **Prerequisites** limited telepathy |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/23` | 0.622115 | **Prerequisites** limited telepathy |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/15` | 0.614872 | **HARMONIC SENSITIVITY** **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/34` | 0.611404 | **Prerequisites** Hyper |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.611243 | **Prerequisites** Psychic Talent |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.611243 | **Prerequisites** Psychic Talent |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.607241 | **Prerequisites** Psychic Mastery |

### Query 392
- Text: What are the requirements for **MELODIC ADAPTATION** **FEAT 9**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/26']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/26', 'PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/22', 'PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/31']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/26` | 0.858083 | **MELODIC ADAPTATION** **FEAT 9** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/22` | 0.680189 | **HARMONIC SHIELDING** **FEAT 9** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/31` | 0.678981 | **MEYEL'S MELODY** **FEAT 9** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/28` | 0.600803 | **PSYCHIC MASTERY** **FEAT 9** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/32` | 0.596302 | **PSYCHIC MASTER** **FEAT 9** |
| 6 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/19` | 0.592826 | STEP 9 |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/21` | 0.587518 | 9TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/25` | 0.575518 | 9TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/23` | 0.575518 | 9TH LEVEL |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/12` | 0.575518 | 9TH LEVEL |

### Query 393
- Text: What are the requirements for **Prerequisites** trained in Arcana, Nature, Occultism, or Religion You can hear the thrum of magic as if it were a swirling note, a  shifting melody, a harmonic chord, or a percussive beat, pulsing  in tune with your heart. You can detect the presence of magic  as though you were always using a 1st-rank *detect magic* spell.  This detects magic within a 30-foot emanation.?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/Text/29']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `27`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/Text/29', 'PZO22001 Starfinder Player Core 058-073::/page/7/Text/41', 'PZO22001 Starfinder Player Core 058-073::/page/6/Text/17']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/29` | 1.001081 | **Prerequisites** trained in Arcana, Nature, Occultism, or Religion You can hear the thrum of magic as if it were a swirling note, a  shifting melody, a harmonic chord, or a percussive beat, pulsing |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/41` | 0.652619 | Whether through intense musical training, magical insight, or  Meyel's divine blessing, you can feel the rhythm of the world  around you and tug on time's chords to manipulate its melody  and flow. Yo |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/6/Text/17` | 0.649081 | You've developed keen organs that have a sensitivity to sound and you know how to put them to use. You become trained in  Performance or gain the Assurance skill feat with Performance  if you're are a |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/16` | 0.597525 | Your antennae are covered in fine hairs that make them  more sensitive to psychic vibrations than most. You gain  thoughtsense as a vague sense with a range of 30 feet. This  means you can use your an |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/20` | 0.595881 | You've honed your whiskers' sensitivity to the degree that you  can sense the movement of the weak electric fields emitted  by potential enemies. You gain electromagnetic sense as an  imprecise sense |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/8/Text/21` | 0.588340 | You trust your instincts to see you through.  You gain master proficiency with the  triggering skill for the skill check. |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/35` | 0.577144 | Divine rhythm pulses through your blood, and your life is the  music. You gain a +2 status bonus to Performance checks.  In addition, you can use Performance to Create a Diversion,  Demoralize, or Mak |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/43` | 0.573210 | You can use your telepathic abilities to quickly assess your  circumstances or subtly glean information from the minds of  others. You can cast *hypercognition* and *mind reading* as 3rdrank occult in |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/46` | 0.567789 | You quickly scan your surroundings for threats. You Seek. If  you use electromagnetic sense, you gain a +2 circumstance  bonus to this check. |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/2/Text/13` | 0.563931 | **Prerequisites** Any minimum attributes, feats, proficiency  ranks, and so forth you must have to select this rules  element are here. Feats also have a level prerequisite,  listed above. |

### Query 394
- Text: What are the requirements for **MEYEL'S MELODY** **FEAT 9**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/31']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `29`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/31', 'PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/26', 'PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/28']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/31` | 0.806584 | **MEYEL'S MELODY** **FEAT 9** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/26` | 0.720524 | **MELODIC ADAPTATION** **FEAT 9** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/28` | 0.663016 | **PSYCHIC MASTERY** **FEAT 9** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/22` | 0.618862 | **HARMONIC SHIELDING** **FEAT 9** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/25` | 0.613512 | 9TH LEVEL |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/12` | 0.613512 | 9TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/21` | 0.613512 | 9TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/23` | 0.613512 | 9TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/32` | 0.610598 | **PSYCHIC MASTER** **FEAT 9** |
| 10 | `PZO22001 Starfinder Player Core 014-029::/page/12/SectionHeader/19` | 0.593200 | STEP 9 |

### Query 395
- Text: What are the requirements for **Prerequisites** Meyel's chosen pahtra heritage?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/34']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `44`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/34', 'PZO22001 Starfinder Player Core 058-073::/page/5/SectionHeader/26', 'PZO22001 Starfinder Player Core 058-073::/page/5/SectionHeader/22']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/34` | 0.898746 | **Prerequisites** Meyel's chosen pahtra heritage |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/5/SectionHeader/26` | 0.715882 | MEYEL'S CHOSEN PAHTRA |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/5/SectionHeader/22` | 0.601788 | PAHTRA HERITAGES |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/62` | 0.543758 | **Prerequisites** Swarm exile shirren heritage |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/27` | 0.539746 | You have an undeniable streak of luck that you believe is a  blessing from your ancestral god Meyel. You might come from |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/14/Text/12` | 0.522307 | **Prerequisites** everwhelp skittermander heritage |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/26` | 0.522307 | **Prerequisites** everwhelp skittermander heritage |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/20` | 0.512106 | Many pahtras cling fiercely to their ancestral Pulonian  traditions in an effort to keep their cultures alive after  enduring generations of oppression by the Veskarium.  Pulonian culture values perso |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/7/Text/41` | 0.507325 | Whether through intense musical training, magical insight, or  Meyel's divine blessing, you can feel the rhythm of the world  around you and tug on time's chords to manipulate its melody  and flow. Yo |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/5/Text/23` | 0.506116 | Pahtras have a variety of heritages throughout their species.  Choose one of the following pahtra heritages at 1st level. |

### Query 396
- Text: What are the requirements for **REMIX WORLD'S RHYTHM** **FEAT 13**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/37']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `29`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/37', 'PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/37', 'PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/33']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/37` | 0.801374 | **REMIX WORLD'S RHYTHM** **FEAT 13** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/37` | 0.627988 | 13TH LEVEL |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/33` | 0.627988 | 13TH LEVEL |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/36` | 0.597988 | 13TH LEVEL |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/37` | 0.585988 | 13TH LEVEL |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/88` | 0.568922 | **CONDITIONS ** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/34` | 0.558332 | **FOCUS PHEROMONES **[one-action] **FEAT 13** |
| 8 | `PZO22001 Starfinder Player Core 014-029::/page/7/Text/28` | 0.555225 | CONDITIONS APPENDIX |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/47` | 0.552115 | **UNCONVENTIONAL EXPERTISE** **FEAT 13** |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/9/SectionHeader/24` | 0.551364 | WEAPON MASTERY 13TH |

### Query 397
- Text: What are the requirements for **Prerequisites** expert in Performance?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/40']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `16`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/40', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/53', 'PZO22001 Starfinder Player Core 058-073::/page/15/Text/34']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/40` | 0.909564 | **Prerequisites** expert in Performance |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/8` | 0.677819 | **Prerequisites** expert in Diplomacy |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/53` | 0.667091 | **Prerequisites** expert in Occultism, focus pool |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/34` | 0.628288 | **Prerequisites** Hyper |
| 5 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/25` | 0.592114 | **Prerequisites** adaptive talent |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/15/Text/19` | 0.572746 | **Prerequisites **Improvised Mastery |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/60` | 0.572350 | **Prerequisites** Psychic Mastery |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/42` | 0.565609 | **Prerequisites** Psychic Bully, Psychic Scholar, or Psychic Talent |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.564486 | **Prerequisites** Psychic Talent |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.564486 | **Prerequisites** Psychic Talent |

### Query 398
- Text: What are the requirements for **SCRUPULOUS STALKER **[free-action] **FEAT 13**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/42']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `26`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/42', 'PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/42', 'PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/33']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/42` | 0.861954 | **SCRUPULOUS STALKER **[free-action] **FEAT 13** |
| 2 | `PZO22001 Starfinder Player Core 098-113::/page/14/SectionHeader/44` | 0.617342 | **READY TO ROLL **[free-action] **FEAT 14** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/42` | 0.604715 | **OPPORTUNISTIC HUG **[reaction] **FEAT 13** |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/33` | 0.604373 | 13TH LEVEL |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/34` | 0.566960 | **FOCUS PHEROMONES **[one-action] **FEAT 13** |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/37` | 0.562373 | 13TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/37` | 0.562373 | 13TH LEVEL |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/36` | 0.562373 | 13TH LEVEL |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/2` | 0.555081 | **EXTEND DIRECTIVE **[free-action] **FEAT 16** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/39` | 0.549601 | **PSYCHIC INVESTIGATOR** **FEAT 13** |

### Query 399
- Text: What are the requirements for **BOUNDLESS BRACHIATOR** **FEAT 17**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/48']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `27`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/48', 'PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/60', 'PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/44']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/48` | 0.861047 | **BOUNDLESS BRACHIATOR** **FEAT 17** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/60` | 0.624841 | **BOUNDLESS ENERGY** **FEAT 17** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/44` | 0.557019 | 17TH LEVEL |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/47` | 0.527019 | 17TH LEVEL |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/52` | 0.515019 | 17TH LEVEL |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/53` | 0.515019 | 17TH LEVEL |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/9/SectionHeader/32` | 0.510832 | GREATER RESOLVE 17TH |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/9/SectionHeader/34` | 0.509844 | INCREDIBLE SENSES 17TH |
| 9 | `PZO22001 Starfinder Player Core 098-113::/page/9/SectionHeader/36` | 0.507023 | INSCRUTABLE 17TH |
| 10 | `PZO22001 Starfinder Player Core 098-113::/page/15/SectionHeader/22` | 0.503258 | **ENDLESSLY ADAPTIVE** **FEAT 20** |

### Query 400
- Text: What are the requirements for **SONG OF MY PEOPLE** **FEAT 17**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/52']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `28`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/52', 'PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/53', 'PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/47']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/52` | 0.770889 | **SONG OF MY PEOPLE** **FEAT 17** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/15/SectionHeader/53` | 0.620562 | 17TH LEVEL |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/47` | 0.620562 | 17TH LEVEL |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/44` | 0.578562 | 17TH LEVEL |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/52` | 0.578562 | 17TH LEVEL |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/7/SectionHeader/48` | 0.549028 | **BOUNDLESS BRACHIATOR** **FEAT 17** |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/45` | 0.538396 | **CENTERED MIND** **FEAT 17** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/3/SectionHeader/57` | 0.535683 | **PSYCHIC PARAGON** **FEAT 17** |
| 9 | `PZO22001 Starfinder Player Core 014-029::/page/7/SectionHeader/10` | 0.532812 | STEP 7: RECORD CLASS DETAILS |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/15/Text/88` | 0.527931 | **CONDITIONS ** |

### Query 401
- Text: What are the requirements for **COMMUNALISM **[reaction] **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/13']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `23`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/13', 'PZO22001 Starfinder Player Core 058-073::/page/11/Text/41', 'PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/9']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/13` | 0.826322 | **COMMUNALISM **[reaction] **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/41` | 0.749378 | **Prerequisites** Communalism |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/9` | 0.663511 | **COMPETITIVE SPIRIT **[reaction] **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/26` | 0.591067 | **QUIP **[reaction] **FEAT 1** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/11/SectionHeader/38` | 0.577216 | **CONSISTENT COMMUNALISM** **FEAT 13** |
| 6 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/41` | 0.576989 | **WATCH OUT **[reaction] **FEAT 1** |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/17` | 0.545423 | **GO TO GROUND! **[one-action]** TO **[two-actions] **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/13` | 0.532584 | **CENTER THOUGHTS **[free-action] **FEAT 1** |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/15` | 0.532253 | **HARMONIC SENSITIVITY** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/42` | 0.531110 | You're always ready to help your allies when they need you the  most. You can use Communalism once per hour, rather than  once per day. |

### Query 402
- Text: What are the requirements for **DISTANT TELEPATH** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/19']
- Expected found: `True`
- Expected rank: `2`
- Graph boost applied: `True`
- Graph boosted count: `40`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/22', 'PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/19', 'PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/22` | 0.859296 | **DISTANT TELEPATH** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/19` | 0.859296 | **DISTANT TELEPATH** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26` | 0.640552 | **HYPER** **FEAT 1** |
| 4 | `PZO22001 Starfinder Player Core 098-113::/page/13/SectionHeader/2` | 0.597116 | **DISTANT FEINT** **FEAT 6** |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/21` | 0.591601 | **Prerequisites** limited telepathy |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/25` | 0.591601 | **Prerequisites** limited telepathy |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22` | 0.591601 | **Prerequisites** limited telepathy |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/23` | 0.591601 | **Prerequisites** limited telepathy |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/23` | 0.574667 | Whether through training or innate talent,  you've expanded the range at which you can  telepathically communicate. Increase the range of  your limited telepathy by 15 feet. |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/26` | 0.574667 | Whether through training or innate talent, you've expanded  the range at which you can telepathically communicate.  Increase the range of your limited telepathy by 15 feet. |

### Query 403
- Text: What are the requirements for **Prerequisites** limited telepathy?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22']
- Expected found: `True`
- Expected rank: `3`
- Graph boost applied: `True`
- Graph boosted count: `33`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22', 'PZO22001 Starfinder Player Core 058-073::/page/2/Text/25', 'PZO22001 Starfinder Player Core 058-073::/page/3/Text/21']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/21` | 0.917483 | **Prerequisites** limited telepathy |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/25` | 0.917483 | **Prerequisites** limited telepathy |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/22` | 0.917483 | **Prerequisites** limited telepathy |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/23` | 0.875483 | **Prerequisites** limited telepathy |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/0/SectionHeader/12` | 0.706373 | LIMITED TELEPATHY |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/8/SectionHeader/14` | 0.706373 | LIMITED TELEPATHY |
| 7 | `PZO22001 Starfinder Player Core 058-073::/page/10/Text/23` | 0.613649 | Whether through training or innate talent,  you've expanded the range at which you can  telepathically communicate. Increase the range of  your limited telepathy by 15 feet. |
| 8 | `PZO22001 Starfinder Player Core 058-073::/page/2/Text/26` | 0.613649 | Whether through training or innate talent, you've expanded  the range at which you can telepathically communicate.  Increase the range of your limited telepathy by 15 feet. |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/11/Text/35` | 0.611281 | **Prerequisites** Psychic Talent |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/31` | 0.611281 | **Prerequisites** Psychic Talent |

### Query 404
- Text: What are the requirements for **LINGUISTIC PRODIGY** **FEAT 1**?
- Expected chunk IDs: ['PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/25']
- Expected found: `True`
- Expected rank: `1`
- Graph boost applied: `True`
- Graph boosted count: `37`
- Graph boost seed source: `top`
- Graph boost seed ids: ['PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/25', 'PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26', 'PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/12']

| Rank | Chunk ID | Score | Preview |
| --- | --- | --- | --- |
| 1 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/25` | 0.784849 | **LINGUISTIC PRODIGY** **FEAT 1** |
| 2 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/26` | 0.631035 | **HYPER** **FEAT 1** |
| 3 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/12` | 0.630753 | 1ST LEVEL |
| 4 | `PZO22001 Starfinder Player Core 058-073::/page/2/SectionHeader/8` | 0.588753 | 1ST LEVEL |
| 5 | `PZO22001 Starfinder Player Core 058-073::/page/6/SectionHeader/8` | 0.588753 | 1ST LEVEL |
| 6 | `PZO22001 Starfinder Player Core 058-073::/page/14/SectionHeader/8` | 0.588753 | 1ST LEVEL |
| 7 | `PZO22001 Starfinder Player Core 098-113::/page/10/Text/30` | 0.583438 | **SIZE UP** **FEAT 1** |
| 8 | `PZO22001 Starfinder Player Core 098-113::/page/10/SectionHeader/16` | 0.580753 | 1ST LEVEL |
| 9 | `PZO22001 Starfinder Player Core 058-073::/page/10/SectionHeader/29` | 0.580435 | **PSYCHIC TALENT** **FEAT 1** |
| 10 | `PZO22001 Starfinder Player Core 058-073::/page/3/Text/1` | 0.580435 | **PSYCHIC TALENT** **FEAT 1** |
